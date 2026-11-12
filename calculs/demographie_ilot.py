"""Modele demographique de l'ilot de Sardaigne (1940-1960).

Ordres de grandeur pour le chapitre 21. Toutes les hypotheses sont en tete
de fichier. Methode : projection par composantes (ages simples, deux sexes),
pas annuel, a partir d'une population de 1946 reconstituee groupe par groupe.

Contraintes du canon (chap. 11) : ~49 000 habitants en 1946, ~55 000 en 1950,
~77 000 en 1960. Les naissances reprennent a partir de 1947.
"""
import numpy as np

MAXAGE = 90  # derniere classe ouverte 90+

# ---------------------------------------------------------------------------
# 1. Population de 1946 par groupe d'origine
#    Chaque groupe : effectif 1946, part d'hommes adultes, de femmes adultes,
#    d'enfants (<15 ans en 1946), et forme de la distribution des ages adultes.
# ---------------------------------------------------------------------------
# Profils d'age adultes (bornes d'age en 1946, poids relatifs par tranche de 5 ans)
def profile(bins):
    """bins : liste (age_debut, poids) par tranche de 5 ans -> vecteur 0..MAXAGE."""
    v = np.zeros(MAXAGE + 1)
    for a0, w in bins:
        v[a0:a0 + 5] += w / 5
    return v / v.sum()

# Marins de 1940 : 18-50 ans, mediane ~25 ans en 1940, donc ~31 ans en 1946
P_MARINS = profile([(20, 10), (25, 30), (30, 25), (35, 15), (40, 9), (45, 6), (50, 4), (55, 1)])
# Civils adultes (Oran, Corses, Bizerte, Malte) : actifs, peu de vieux (eux ont peu survecu)
P_CIVILS = profile([(15, 8), (20, 14), (25, 17), (30, 17), (35, 14), (40, 11), (45, 8), (50, 6), (55, 3), (60, 1.5), (65, 0.5)])
# Survivants sardes : la famine tue d'abord les vieux et les petits enfants.
# Ceux qui avaient 10-35 ans en 1940 (16-41 en 1946) sont sur-representes.
P_SARDES = profile([(15, 12), (20, 17), (25, 17), (30, 15), (35, 12), (40, 9), (45, 7), (50, 5), (55, 3), (60, 2), (65, 1)])
# Enfants de 1946 : nes avant 1940 (6-14 ans), peu nombreux ; nes 1941-43
# presque aucun (amenorrhee de famine) ; reprise 1944-46.
P_ENFANTS = np.zeros(MAXAGE + 1)
for age, w in {0: 16, 1: 13, 2: 9, 3: 3, 4: 2, 5: 3, 6: 6, 7: 7, 8: 7,
               9: 7, 10: 7, 11: 7, 12: 7, 13: 6, 14: 6}.items():
    P_ENFANTS[age] = w
P_ENFANTS /= P_ENFANTS.sum()

# (nom, effectif 1946, hommes adultes, femmes adultes, enfants, profil adulte H, profil adulte F)
GROUPES_1946 = [
    ("Marins et militaires des flottes (FR, GB, Toulon, Bizerte)", 13_400, 0.985, 0.015, 0.0, P_MARINS, P_CIVILS),
    ("Civils d'Oran et de Gibraltar",        2_900, 0.40, 0.36, 0.24, P_CIVILS, P_CIVILS),
    ("Rescapes civils de Bizerte",             400, 0.40, 0.36, 0.24, P_CIVILS, P_CIVILS),
    ("Refugies corses",                      3_000, 0.44, 0.34, 0.22, P_CIVILS, P_CIVILS),
    ("Survivants maltais",                     250, 0.42, 0.38, 0.20, P_CIVILS, P_CIVILS),
    ("Militaires italiens",                  3_300, 1.00, 0.00, 0.0, P_MARINS, P_CIVILS),
    ("Marins et familles de Toulon (1944)",    1_000, 0.60, 0.25, 0.15, P_MARINS, P_CIVILS),  # second depart (chap. 33)
    ("Civils sardes",                       24_750, 0.32, 0.47, 0.21, P_SARDES, P_SARDES),
]

def pop_1946():
    m = np.zeros(MAXAGE + 1)
    f = np.zeros(MAXAGE + 1)
    rows = []
    for name, n, sh_m, sh_f, sh_c, pm, pf in GROUPES_1946:
        gm = n * sh_m * pm + n * sh_c * 0.51 * P_ENFANTS
        gf = n * sh_f * pf + n * sh_c * 0.49 * P_ENFANTS
        m += gm
        f += gf
        rows.append((name, n, gm.sum(), gf.sum(), (gm[:15] + gf[:15]).sum()))
    return m, f, rows

# ---------------------------------------------------------------------------
# 2. Mortalite (quotients annuels par age), 1946 -> 1960
#    Pays mediterraneen pauvre d'avant-guerre (Sardaigne 1936 : e0 ~ 50 ans),
#    sans antibiotiques ni vaccins neufs, mais avec visite quotidienne,
#    hygiene navale et ration garantie.
# ---------------------------------------------------------------------------
def q_age(year, sex):
    t = min(max((year - 1946) / 14, 0), 1)  # amelioration lineaire 1946 -> 1960
    q = np.zeros(MAXAGE + 1)
    q[0] = 0.130 - 0.050 * t          # mortalite infantile 130 -> 80 pour mille
    q[1:5] = 0.025 - 0.012 * t
    q[5:15] = 0.004
    q[15:50] = 0.005 if sex == "f" else 0.007   # hommes : mines, mer, accidents
    q[50:65] = 0.018
    q[65:75] = 0.045
    q[75:] = 0.12
    if sex == "f":
        q[18:45] += 0.003              # mortalite maternelle (~6 pour 1 000 naissances)
    return q

MORIA_EXTRA_DEATHS = {1946: 450, 1947: 150}   # fin de la Moria (chap. 14)

# ---------------------------------------------------------------------------
# 3. Fecondite
#    Fecondite naturelle des femmes mariees (Coale-Trussell, n(a)),
#    x part de femmes mariees x facteur de reprise (sous-fecondite d'apres
#    famine, allaitement long, rations).
# ---------------------------------------------------------------------------
NATURAL = {15: 0.300, 20: 0.460, 25: 0.431, 30: 0.396, 35: 0.321, 40: 0.167, 45: 0.024}
MARRIED = {15: 0.35, 20: 0.88, 25: 0.95, 30: 0.95, 35: 0.93, 40: 0.90, 45: 0.88}
REPRISE = {1946: 0.38, 1947: 0.55, 1948: 0.65, 1949: 0.68}  # puis 0.70
REPRISE_DEFAULT = 0.70
SEX_RATIO_BIRTH = 1.05

def asfr(year):
    r = REPRISE.get(year, REPRISE_DEFAULT)
    v = np.zeros(MAXAGE + 1)
    for a0 in NATURAL:
        v[a0:a0 + 5] = NATURAL[a0] * MARRIED[a0] * r
    return v

# ---------------------------------------------------------------------------
# 4. Immigration (solde migratoire annuel), par profil
# ---------------------------------------------------------------------------
# 1949-1951 : quelques admissions (Malte, epaves recueillies)
# 1952-1960 : patente de sante, l'ile est ouverte (Gozo, Corse, Barbagia,
#             Gibraltar, Afrique du Nord, ilot de l'Est...)
IMMIG = {1949: 250, 1950: 350, 1951: 450}
IMMIG_OPEN = 850  # par an a partir de 1952 (ajuste pour ~77 000 en 1960)
# profil des immigres : jeunes adultes, legere majorite d'hommes, quelques enfants
IMMIG_M = 0.40 * (0.85 * profile([(15, 15), (20, 30), (25, 25), (30, 15), (35, 8), (40, 5), (45, 2)]) + 0.15 * P_ENFANTS)
IMMIG_F = 0.60 * (0.85 * profile([(15, 15), (20, 30), (25, 25), (30, 15), (35, 8), (40, 5), (45, 2)]) + 0.15 * P_ENFANTS)

# Bilan des entrees 1949-1959 par origine et par voie (chap. 21 §4.7).
# (origine, voie, effectif, part de femmes). La somme doit egaler le solde
# migratoire du modele, et la part de femmes rester proche de 60 %.
ORIGINES = [
    ("Sardes de l'interieur (Barbagia, Gallura, Logudoro), descendus seuls", "spontanee", 1_400, 0.75),
    ("Barbagia : villages entres par pacte (1955-1959)",                   "pacte",       1_000, 0.50),
    ("Corse, traversees des bouches de Bonifacio",                          "spontanee", 1_800, 0.60),
    ("Corse, expeditions de recueil (1955-1959)",                           "expedition",  900, 0.55),
    ("Cote italienne et archipel toscan, expeditions (1957-1959)",          "expedition",  700, 0.55),
    ("Afrique du Nord, barques recueillies en mer",                         "spontanee", 1_500, 0.60),
    ("Malte, Gozo, epaves (1949-1952)",                                     "spontanee",   300, 0.50),
    ("Autres (Baleares, Sicile, en mer)",                                   "spontanee",   250, 0.50),
]

def check_origines():
    total = sum(n for _, _, n, _ in ORIGINES)
    femmes = sum(n * fw for _, _, n, fw in ORIGINES)
    model = sum(immig(y) for y in range(1949, 1960))
    print("\n=== Entrees 1949-1959 par origine ===")
    for name, voie, n, fw in ORIGINES:
        print(f"{name:70s} {voie:10s} {n:6,.0f}  femmes {100*fw:3.0f} %")
    by = {}
    for _, voie, n, _ in ORIGINES:
        by[voie] = by.get(voie, 0) + n
    print(f"Total {total:,.0f} (modele : {model:,.0f}) ; femmes {100*femmes/total:.0f} % ; par voie : {by}")
    assert abs(total - model) < 50, "le bilan par origine ne colle pas au modele"

def immig(year):
    return IMMIG.get(year, IMMIG_OPEN if year >= 1952 else 0)

# ---------------------------------------------------------------------------
# 5. Projection
# ---------------------------------------------------------------------------
def project(m, f, y0=1946, y1=1960):
    states = {y0: (m.copy(), f.copy())}
    flows = {}
    for y in range(y0, y1):
        qm, qf = q_age(y, "m"), q_age(y, "f")
        births = (f * asfr(y)).sum()
        bm, bf = births * SEX_RATIO_BIRTH / (1 + SEX_RATIO_BIRTH), births / (1 + SEX_RATIO_BIRTH)
        deaths = (m * qm).sum() + (f * qf).sum()
        # deces supplementaires de la Moria, repartis au prorata
        extra = MORIA_EXTRA_DEATHS.get(y, 0)
        tot = m.sum() + f.sum()
        m = m * (1 - qm) * (1 - extra / tot)
        f = f * (1 - qf) * (1 - extra / tot)
        # vieillissement
        m = np.concatenate([[bm * (1 - qm[0] / 2)], m[:-2], [m[-2] + m[-1]]])
        f = np.concatenate([[bf * (1 - qf[0] / 2)], f[:-2], [f[-2] + f[-1]]])
        n_im = immig(y)
        m = m + n_im * IMMIG_M
        f = f + n_im * IMMIG_F
        flows[y] = dict(births=births, deaths=deaths + extra + births * qm[0] / 2, immig=n_im)
        states[y + 1] = (m.copy(), f.copy())
    return states, flows

def bins5(v):
    out = [v[a:a + 5].sum() for a in range(0, 65, 5)]
    out.append(v[65:].sum())
    return out

LABELS = [f"{a}-{a+4}" for a in range(0, 65, 5)] + ["65+"]

def report():
    m, f, rows = pop_1946()
    print("=== Population de 1946 par groupe ===")
    print(f"{'Groupe':58s} {'Total':>7s} {'Hommes':>7s} {'Femmes':>7s} {'<15 ans':>7s}")
    for name, n, gm, gf, ch in rows:
        print(f"{name:58s} {n:7,.0f} {gm:7,.0f} {gf:7,.0f} {ch:7,.0f}")
    print(f"{'TOTAL':58s} {m.sum()+f.sum():7,.0f} {m.sum():7,.0f} {f.sum():7,.0f} {(m[:15]+f[:15]).sum():7,.0f}")

    states, flows = project(m, f)
    print("\n=== Effectifs, naissances, deces ===")
    print("Annee   Pop.  Hommes Femmes  H/100F  H/100F(20-39)  Naiss. Deces  Immig.  TBN  TBM")
    for y in range(1946, 1961):
        mm, ff = states[y]
        p = mm.sum() + ff.sum()
        sr = 100 * mm.sum() / ff.sum()
        sr2 = 100 * mm[20:40].sum() / ff[20:40].sum()
        fl = flows.get(y, {})
        b, d, i = fl.get("births", 0), fl.get("deaths", 0), fl.get("immig", 0)
        print(f"{y}  {p:7,.0f} {mm.sum():6,.0f} {ff.sum():6,.0f}  {sr:5.0f}   {sr2:5.0f}        {b:6,.0f} {d:5,.0f}  {i:5,.0f}  {1000*b/p:4.0f} {1000*d/p:4.0f}")

    for y in (1946, 1950, 1955, 1960):
        mm, ff = states[y]
        print(f"\n=== Pyramide {y} (tranches de 5 ans) ===")
        print("Age      Hommes  Femmes   H/100F   % pop")
        tot = mm.sum() + ff.sum()
        for lab, a, b in zip(LABELS, bins5(mm), bins5(ff)):
            print(f"{lab:7s} {a:7,.0f} {b:7,.0f}   {100*a/max(b,1):5.0f}   {100*(a+b)/tot:5.1f}")
        young = (mm[:15] + ff[:15]).sum()
        old = (mm[65:] + ff[65:]).sum()
        act = tot - young - old
        print(f"<15 ans : {100*young/tot:.0f} %  15-64 : {100*act/tot:.0f} %  65+ : {100*old/tot:.1f} %  "
              f"dependance : {100*(young+old)/act:.0f} pour 100 actifs")
        print(f"Femmes 15-44 : {ff[15:45].sum():,.0f}  Hommes 15-44 : {mm[15:45].sum():,.0f}  "
              f"Hommes 15-44 'sans epouse possible' : {mm[18:45].sum()-ff[16:42].sum():,.0f}")

if __name__ == "__main__":
    report()

# ---------------------------------------------------------------------------
# 6. Les metiers de 1950, deduits des besoins de l'ile (chap. 15, 17, 19)
#    Chaque ligne : (secteur, besoin physique, productivite par travailleur,
#    effectif = besoin / productivite, part de femmes [canon provisoire]).
# ---------------------------------------------------------------------------
POP_1950 = 55_000
BIRTHS_1950 = 2_500
UNDER5_1950 = 7_800
PUPILS_1950 = 4_000      # enfants de 6 a 14 ans scolarises le matin

def metiers_1950():
    P = POP_1950
    rows = [
        # secteur, besoin, unite, productivite, unite prod., part femmes
        ("Cultures (cereales, legumineuses, pommes de terre, potagers)", 11_500, "ha", 3.0, "ha/travailleur", 0.35),
        ("Elevage et bergers (ovins, caprins, porcs, basse-cour)", 60_000, "tetes", 100, "tetes/travailleur", 0.25),
        ("Peche (etangs, cote, chalut, madragues)", 3_300, "t/an", 3.0, "t/pecheur/an", 0.05),
        ("Transformation (moulins, fours, huile, salaisons, fromage)", 14_000 + 3_300, "t/an", 30, "t/travailleur/an", 0.45),
        ("Cuisines et distribution de la ration", P, "rations/jour", 60, "rations/travailleur", 0.60),
        ("Mines de charbon (fond et jour)", 200_000, "t/an", 60, "t/mineur/an", 0.03),
        ("Bois, sel, chaux (chaulage des sols)", 1, "forfait", 1 / 900, "", 0.10),
        ("Centrales, barrages, gaz, distillerie de goudron", 1, "forfait", 1 / 550, "", 0.10),
        ("Bords a flot (navires armes, sous-marins, chalutiers)", 1, "forfait", 1 / 2_000, "", 0.0),
        ("Arsenal, chantiers, forges, ateliers", 1, "forfait", 1 / 1_400, "", 0.10),
        ("Garde (cotes, depots, Ligne, Asinara) et avant-postes", 1, "forfait", 1 / 1_900, "", 0.02),
        ("Batiment et entretien des logements", P, "habitants", 40, "habitants/ouvrier", 0.05),
        ("Textile, vetement, cuir, chaussures", P, "habitants", 40, "habitants/ouvrier", 0.70),
        ("Transports (charrois, voie ferree, cabotage)", 1, "forfait", 1 / 800, "", 0.05),
        ("Sante (hopitaux, Zone, maternites, visite)", P, "habitants", 65, "habitants/soignant", 0.70),
        ("Creches et garde des petits enfants", UNDER5_1950, "enfants <5 ans", 10, "enfants/gardienne", 0.95),
        ("Ecoles, Ecole navale, universite, bibliotheque", PUPILS_1950, "eleves", 25, "eleves/enseignant", 0.55),
        ("Inscription, commissariat, transmissions, justice, aumoniers", P, "habitants", 90, "habitants/agent", 0.40),
    ]
    print("\n=== Metiers de 1950 deduits des besoins ===")
    total = women = 0
    for name, need, unit, prod, punit, fw in rows:
        n = need / prod
        total += n
        women += n * fw
        print(f"{name:66s} {n:7,.0f}  femmes {100*fw:3.0f} %")
    print(f"{'TOTAL des postes permanents':66s} {total:7,.0f}  dont femmes {women:,.0f} ({100*women/total:.0f} %)")
    return total, women

if __name__ == "__main__":
    metiers_1950()
    check_origines()
