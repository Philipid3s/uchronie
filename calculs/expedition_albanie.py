"""Bilans de l'expedition d'Albanie (campagne de 1950).

Ordres de grandeur pour le chapitre 18. Toutes les hypotheses sont en tete
de fichier et peuvent etre modifiees. Unites : milles nautiques, noeuds,
tonnes, jours.
"""

# --- Route (milles) ------------------------------------------------------
LEGS = [
    ("Cagliari -> La Valette", 325),
    ("La Valette -> Vlore", 361),
    ("Vlore -> La Valette", 361),
    ("La Valette -> Asinara (par le cap Teulada et la cote ouest)", 510),
]
CONVOY_KN = 9.0          # vitesse du convoi, fixee par le cargo
STAY_VLORE_D = 50        # sejour en baie de Vlore
STAY_MALTA_D = 5         # trois jours a l'aller (chargement), deux au retour

# --- Consommations ------------------------------------------------------
# Georges Leygues, chaufferie charbon, 9 noeuds (150 t/j a 12 nd au ch. 15 ;
# puissance ~ v^3, plus une charge fixe d'auxiliaires)
GL_COAL_12KN = 150.0
GL_HOTEL_COAL = 12.0     # feux couverts, dynamos, bouilleurs, cuisine
def gl_coal_per_day(v):
    return GL_HOTEL_COAL + (GL_COAL_12KN - GL_HOTEL_COAL) * (v / 12.0) ** 3

CARGO_COAL_DAY = 30.0    # vapeur de 3 500 tpl, charbon du Sulcis
CARGO_COAL_PORT = 3.0
TANKER_OIL_DAY = 25.0    # petrolier a vapeur de ~10 000 tpl, 9 noeuds
TANKER_OIL_PORT_D = 10   # jours au mouillage avant de bruler le brut
TANKER_OIL_PORT = 4.0
GL_OIL_RESERVE = 250.0   # chaufferie mazout : ~15 h de pousse
TANKER_MARGIN = 60.0
SHORE_COAL = 600.0       # chaudiere de chantier, pompes, rechauffage du brut
GL_PATROL_COAL = 200.0   # reconnaissances dans la baie, alertes

# --- Personnel ----------------------------------------------------------
CREW = {
    "Georges Leygues": 420,
    "Petrolier": 50,
    "Cargo (equipage)": 35,
    "Fusiliers marins": 100,
    "Equipes techniques": 60,
    "Service de sante": 8,
    "Interpretes et negociateurs": 5,
}
FOOD_KG_DAY = 1.0        # ration de force, vivres secs et conserves
WATER_L_DAY = 6.0
FOOD_MARGIN = 1.3        # avaries, imprevus, retour retarde

def main():
    days_at_sea = sum(d for _, d in LEGS) / CONVOY_KN / 24
    total_days = days_at_sea + STAY_VLORE_D + STAY_MALTA_D
    print(f"Distance totale : {sum(d for _, d in LEGS)} milles")
    for name, d in LEGS:
        print(f"  {name:62s} {d:4d} mi  {d / CONVOY_KN:5.1f} h")
    print(f"Jours de mer : {days_at_sea:.1f} ; duree totale hors quarantaine : {total_days:.0f} j")

    gl_day = gl_coal_per_day(CONVOY_KN)
    gl_sea = gl_day * days_at_sea
    gl_port = GL_HOTEL_COAL * (STAY_VLORE_D + STAY_MALTA_D)
    gl_total = gl_sea + gl_port + GL_PATROL_COAL
    # charbon embarque a Malte pour l'aller-retour Malte - Vlore - Malte
    leg_mv = 361 / CONVOY_KN / 24
    gl_from_malta = 2 * leg_mv * gl_day + GL_HOTEL_COAL * STAY_VLORE_D + GL_PATROL_COAL
    cargo_total = CARGO_COAL_DAY * days_at_sea + CARGO_COAL_PORT * (STAY_VLORE_D + STAY_MALTA_D)
    coal_total = gl_total + cargo_total + SHORE_COAL
    print(f"\nCharbon GL : {gl_day:.0f} t/j a {CONVOY_KN:.0f} nd ; total {gl_total:.0f} t ;"
          f" besoin depuis Malte {gl_from_malta:.0f} t (soutes 1 500 t)")
    print(f"Charbon cargo : {cargo_total:.0f} t ; chantier : {SHORE_COAL:.0f} t")
    print(f"Charbon total : {coal_total:.0f} t")

    outbound = (325 + 361) / CONVOY_KN / 24
    tanker_oil = TANKER_OIL_DAY * outbound + TANKER_OIL_PORT * TANKER_OIL_PORT_D
    oil_embarked = tanker_oil + TANKER_MARGIN + GL_OIL_RESERVE
    oil_burned_expected = tanker_oil + 0.2 * GL_OIL_RESERVE
    print(f"\nMazout petrolier (aller + 10 j au mouillage) : {tanker_oil:.0f} t")
    print(f"Mazout embarque : {oil_embarked:.0f} t = {oil_embarked / 10000:.1%} de la reserve")
    print(f"Mazout brule (attendu, sans combat) : {oil_burned_expected:.0f} t"
          f" = {oil_burned_expected / 10000:.1%}")

    n = sum(CREW.values())
    food = n * FOOD_KG_DAY * total_days * FOOD_MARGIN / 1000
    water = n * WATER_L_DAY / 1000
    print(f"\nPersonnel : {n}")
    print(f"Vivres : {food:.0f} t ; eau : {water:.1f} t/j")

    for crude in (4000, 6000, 8000):
        fuel = crude * 0.85
        print(f"Brut rapporte {crude} t -> ~{fuel:.0f} t de fioul ;"
              f" rapport gain/mazout brule {fuel / oil_burned_expected:.0f}")

if __name__ == "__main__":
    main()
