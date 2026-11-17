"""Autonomie du prototype de longue expédition (chapitre 35 §6.3 ter).

Ordres de grandeur [estimation 🔧] pour un cargo de 1940 d'environ 2 500 tpl,
machine à triple expansion, chaudières cylindriques, chauffé au charbon du Sulcis
(~5 000 kcal/kg, un tiers de moins qu'un bon charbon gallois, [15] §5).
Gibraltar n'a pas de charbon à lui : son dépôt est fait de charbon du Sulcis
apporté par l'Anadyr ([07] §2 bis).

Sortie : python calculs/autonomie_prototype.py
"""

# ---------------------------------------------------------------- navire
DEPLACEMENT_T = 3800        # t, en charge (cargo de ~2 500 tpl, ~80 m)
PORT_EN_LOURD_T = 2500      # t
C_AMIRAUTE = 200            # coefficient de l'Amirauté (base ch indiqués) : Δ^(2/3)·V³/P
CONSO_GALLOIS = 0.70        # kg de charbon par ch indiqué et par heure, bon charbon gallois [histoire, ordre de grandeur]
RAPPORT_SULCIS = 7500 / 5000  # il en faut 1,5 fois plus avec le charbon du Sulcis
CONSO_SULCIS = CONSO_GALLOIS * RAPPORT_SULCIS   # ~1,05 kg/ch/h
AUX_ROUTE_T_J = 1.0         # t/jour : dynamo, treuils, cuisine, évaporateur, en route
FEUX_COUVERTS_T_J = 3.0     # t/jour au mouillage, une chaudière sous pression (dynamo, cuisine, eau douce, grue)
VEILLE_T_J = 1.5            # t/jour au mouillage, chaudière en veille, dynamo arrêtée la nuit
GAIN_VOILE = 0.10           # économie prudente de la voile d'appoint sur les traversées océaniques
RESERVE = 0.15              # réserve de sécurité : on ne compte jamais sur les 15 derniers %


def puissance_ch(v_noeuds):
    return DEPLACEMENT_T ** (2 / 3) * v_noeuds ** 3 / C_AMIRAUTE


def conso_jour(v, voile=False):
    """t de charbon par jour de route à v nœuds."""
    t = puissance_ch(v) * CONSO_SULCIS * 24 / 1000 + AUX_ROUTE_T_J
    return t * (1 - GAIN_VOILE) if voile else t


def conso_mille(v, voile=False):
    return conso_jour(v, voile) / (24 * v)


# ---------------------------------------------------------------- route
# milles marins, estimés sur la carte [estimation]
ETAPES = [
    ("Cagliari – Gibraltar (nord des Baléares)", 820, True),
    ("Gibraltar – Lorient", 900, True),
    ("Lorient – Brest", 130, False),
    ("Brest – Plymouth", 120, False),
    ("Plymouth – Portsmouth", 150, False),
    ("Portsmouth – baie de Seine", 100, False),
    ("Baie de Seine – Ouessant", 300, False),
    ("Ouessant – Gibraltar", 1000, True),
    ("Gibraltar – Cagliari", 820, True),
]
DEPLACEMENTS_LOCAUX = 0.10   # +10 % pour les allées et venues dans les rades et les passes
EXTENSION_CLYDE = 1150       # Plymouth – Milford Haven – la Clyde – retour à Plymouth [B77]
V_ROUTE = 9.0
V_MANCHE = 8.0               # prudence : mines, épaves, passes
JOURS_SUR_PLACE = 60
PART_FEUX_COUVERTS = 0.5     # moitié du temps sur place feux couverts, moitié en veille


def bilan(soute_depart, plein_gibraltar, clyde=False, jours=JOURS_SUR_PLACE):
    """Suit le charbon étape par étape ; renvoie (journal, reste à l'arrivée, minimum atteint)."""
    soute, journal, mini = soute_depart, [], soute_depart
    capacite = soute_depart
    etapes = list(ETAPES)
    if clyde:
        etapes.insert(4, ("Plymouth – Milford Haven – Clyde – Plymouth", EXTENSION_CLYDE, True))
    for nom, milles, ocean in etapes:
        v = V_ROUTE if ocean else V_MANCHE
        milles_eff = milles * (1 + (0 if ocean else DEPLACEMENTS_LOCAUX))
        brule = milles_eff * conso_mille(v, voile=ocean)
        soute -= brule
        mini = min(mini, soute)
        journal.append((nom, milles_eff, milles_eff / v / 24, brule, soute))
        if nom.startswith("Lorient – Brest"):
            sur_place = jours * (PART_FEUX_COUVERTS * FEUX_COUVERTS_T_J + (1 - PART_FEUX_COUVERTS) * VEILLE_T_J)
            soute -= sur_place
            mini = min(mini, soute)
            journal.append((f"Séjour sur place ({jours} j)", 0, jours, sur_place, soute))
        if plein_gibraltar and nom.endswith("(nord des Baléares)"):
            soute = capacite
            journal.append(("Plein à Gibraltar", 0, 2, 0, soute))
        if plein_gibraltar and nom.startswith("Ouessant – Gibraltar"):
            soute = capacite
            journal.append(("Plein à Gibraltar", 0, 2, 0, soute))
    return journal, soute, mini


# ---------------------------------------------------------------- électricité
TENSION_V = 110             # continu, comme sur les navires de 1940
DYNAMOS_KW = (25, 25)       # deux dynamos à vapeur, dont une en secours [estimation]
# charges en mode « machine et chaudières arrêtées » (le pire cas : on ne vit que sur les batteries)
CHARGES_SECOURS_KWH_J = {
    "émetteur de secours (~150 W antenne, ~400 W absorbés, 1 h/j)": 0.4,
    "récepteur de trafic (40 W, 12 h/j)": 0.5,
    "éclairage de secours (300 W, 6 h/j)": 1.8,
    "infirmerie (100 W, 8 h/j)": 0.8,
    "sondeur et divers": 0.3,
}
# les feux de route sont doublés de fanaux à pétrole ; la station principale (1 kW antenne,
# ~3 kW absorbés) ne tourne que sur dynamo
JOURS_SANS_VAPEUR = 10
DECHARGE_UTILE = 0.5        # on ne descend pas une batterie au plomb sous 50 %
WH_PAR_KG = 25              # accumulateurs au plomb stationnaires des années 1940 [ordre de grandeur]
TENSION_ELEMENT = 2.0


# ---------------------------------------------------------------- eau, vivres, essence
PERSONNES = 60
RECUEILLIS = 30             # survivants recueillis, pour 60 jours
EAU_L_J = 10                # boisson, cuisine, toilette minimale
EAU_CHAUDIERE_PERTE = 0.01  # 1 % de la vapeur perdue, à compenser en eau douce
VAPEUR_KG_CH_H = 6.5
CAISSES_EAU_T = 150         # double fond : ~100 t d'eau d'alimentation, ~50 t d'eau de boisson
EAU_BOISSON_T = 50
VIVRES_KG_J = 1.3           # vivres secs et conserves, emballage compris
JOURS_VIVRES = 120
ESSENCE_T = 4.0
LOIRE_KG_H = 133            # ~400 kg pour un vol de 3 h ([36] §3.2)
PERTES_ESSENCE = 0.15       # évaporation et essais


def main():
    print("=" * 78)
    print("1. PROPULSION (charbon du Sulcis)")
    print(f"   Consommation spécifique : {CONSO_SULCIS:.2f} kg/ch/h (gallois : {CONSO_GALLOIS:.2f})")
    print(f"   {'Vitesse':>8} {'Puissance':>10} {'t/jour':>8} {'kg/mille':>9} {'avec voile':>11}")
    for v in (7, 8, 9, 10):
        print(f"   {v:>6} nd {puissance_ch(v):>8.0f} ch {conso_jour(v):>8.1f} {1000*conso_mille(v):>9.0f} "
              f"{1000*conso_mille(v, True):>9.0f}")

    print("\n   Rayon d'action brut (réserve de 15 % gardée), sans séjour :")
    for soute in (700, 1000):
        utile = soute * (1 - RESERVE)
        ligne = "   " + f"{soute:>5} t : " + ", ".join(
            f"{v} nd → {utile / conso_mille(v, True):,.0f} milles".replace(",", " ") for v in (7, 8, 9))
        print(ligne)

    print("\n" + "=" * 78)
    print("2. LE VOYAGE TYPE : Cagliari – Bretagne – Manche – Cagliari, 60 jours sur place")
    route = sum(m for _, m, _ in ETAPES)
    print(f"   Route : {route} milles sur la carte, ~{route * 1.03:.0f} avec les allées et venues")
    cas = [
        ("A. 700 t, plein à Gibraltar à l'aller et au retour", 700, True, False),
        ("A bis. 700 t, sans Gibraltar", 700, False, False),
        ("B. 1 000 t (cale 2 en soute de réserve), plein à Gibraltar", 1000, True, False),
        ("C. 1 000 t, sans Gibraltar", 1000, False, False),
        ("D. 1 000 t, plein à Gibraltar, extension vers la Clyde", 1000, True, True),
        ("E. 700 t, plein à Gibraltar, extension vers la Clyde", 700, True, True),
    ]
    for titre, soute, plein, clyde in cas:
        journal, fin, mini = bilan(soute, plein, clyde)
        jours = sum(j for _, _, j, _, _ in journal)
        ok = "OK" if mini >= soute * RESERVE else "RÉSERVE ENTAMÉE" if mini > 0 else "IMPOSSIBLE"
        print(f"\n   {titre}")
        for nom, milles, j, brule, reste in journal:
            print(f"     {nom:<44} {milles:>6.0f} mi {j:>5.1f} j  -{brule:>5.0f} t  reste {reste:>6.0f} t")
        print(f"     → durée ~{jours:.0f} jours ; point bas {mini:.0f} t ({100*mini/soute:.0f} %) ; {ok}")

    # combien de jours sur place au maximum (cas B), en gardant la réserve au point bas
    for soute in (700, 1000):
        j = 0
        while bilan(soute, True, False, j)[2] >= soute * RESERVE:
            j += 5
        print(f"\n   Séjour maximal sur place avec {soute} t et pleins à Gibraltar : ~{j - 5} jours")

    print("\n" + "=" * 78)
    print("3. ÉLECTRICITÉ ET BATTERIES")
    print(f"   Réseau {TENSION_V} V continu ; dynamos à vapeur {DYNAMOS_KW[0]} + {DYNAMOS_KW[1]} kW")
    jour = sum(CHARGES_SECOURS_KWH_J.values())
    for k, w in CHARGES_SECOURS_KWH_J.items():
        print(f"     {k:<62} {w:>4.1f} kWh/j")
    utile = jour * JOURS_SANS_VAPEUR
    nominal = utile / DECHARGE_UTILE
    ah = nominal * 1000 / TENSION_V
    elements = TENSION_V / TENSION_ELEMENT
    masse = nominal * 1000 / WH_PAR_KG
    print(f"   Besoin de secours : {jour:.1f} kWh/j ; {JOURS_SANS_VAPEUR} jours sans vapeur → {utile:.0f} kWh utiles")
    print(f"   Batterie : {nominal:.0f} kWh nominaux, {elements:.0f} éléments de 2 V de ~{ah:.0f} Ah, "
          f"~{masse/1000:.1f} t (≈{masse/elements:.0f} kg par élément)")
    print(f"   Recharge sur dynamo à C/10 : ~{ah/10:.0f} A, ~{ah/10*TENSION_V/1000:.0f} kW, une douzaine d'heures")
    print("   Groupe de secours semi-Diesel de 5 kW au brut d'Albanie (après 1951) : ~0,5 kg de brut par kWh,")
    print(f"     soit ~{nominal*0.5:.0f} kg de brut pour une recharge complète")

    print("\n" + "=" * 78)
    print("4. EAU, VIVRES, ESSENCE")
    eau_equipage = PERSONNES * EAU_L_J / 1000
    eau_chaud = puissance_ch(V_ROUTE) * VAPEUR_KG_CH_H * EAU_CHAUDIERE_PERTE * 24 / 1000
    print(f"   Eau de boisson : {eau_equipage:.1f} t/j pour {PERSONNES} ; "
          f"{(PERSONNES+RECUEILLIS)*EAU_L_J/1000:.1f} t/j avec {RECUEILLIS} recueillis")
    print(f"   Appoint des chaudières en route : ~{eau_chaud:.1f} t/j (1 % de la vapeur)")
    print(f"   Sans évaporateur, l'eau de boisson ({EAU_BOISSON_T} t) dure ~{EAU_BOISSON_T/eau_equipage:.0f} jours "
          f"(~{EAU_BOISSON_T/((PERSONNES+RECUEILLIS)*EAU_L_J/1000):.0f} avec les recueillis)")
    vivres = PERSONNES * VIVRES_KG_J * JOURS_VIVRES / 1000 + RECUEILLIS * VIVRES_KG_J * 60 / 1000
    print(f"   Vivres pour {JOURS_VIVRES} jours (+ recueillis 60 j) : ~{vivres:.0f} t")
    heures = ESSENCE_T * 1000 * (1 - PERTES_ESSENCE) / LOIRE_KG_H
    print(f"   Essence d'aviation : {ESSENCE_T:.0f} t → ~{heures:.0f} h de vol, ~{heures/3:.0f} vols de 3 h")

    print("\n" + "=" * 78)
    print("5. MASSES EMBARQUÉES (port en lourd 2 500 t)")
    for soute in (700, 1000):
        postes = {
            "charbon": soute, "eau (caisses pleines)": CAISSES_EAU_T, "vivres": vivres,
            "essence, huiles": ESSENCE_T + 3, "hydravion": 3.5, "vedette": 5,
            "hommes et bagages": 10, "armes et munitions": 3, "matériel scientifique, rechanges": 20,
        }
        tot = sum(postes.values())
        print(f"   Soute de {soute} t : total {tot:.0f} t ; reste {PORT_EN_LOURD_T - tot:.0f} t "
              f"pour le grain des échanges, les recueillis, les plans et les livres, et le lest")


if __name__ == "__main__":
    main()
