"""Bilan de liaison radio en ondes courtes (HF) depuis Cagliari, 1940-1960.

Ordres de grandeur pour le chapitre 16. Methode simplifiee, inspiree des
methodes CCIR / UIT-R (Rec. P.533, P.372, rapport CCIR 252) :

  1. Activite solaire : nombre de Wolf annuel reel (SIDC, serie version 1).
  2. Couche F2 : frequence critique foF2 de jour et de nuit en fonction de R ;
     frequence maximale utilisable (MUF) par la loi de la secante, terre courbe.
  3. Nombre de bonds : bond maximal pour un angle de depart de 3 degres.
  4. Pertes : espace libre sur le trajet oblique + absorption de la couche D
     (formule de George-Bradley / CCIR 252) + reflexions au sol + pertes
     diverses.
  5. Bruit : bruit galactique, bruit atmospherique, bruit humain d'un site
     rural tres calme (il n'y a presque plus de reseaux electriques).
  6. Rapport signal/bruit en telegraphie Morse (bande de 500 Hz) et en
     telephonie (6 kHz).

Les effets propres a l'uchronie (absorption renforcee par les oxydes d'azote,
couche E sporadique due aux metaux des ejectas) sont des hypotheses
[estimation], parametrees en tete de fichier.
Usage : python calculs/radio_propagation.py
"""
from math import radians, degrees, sin, cos, tan, acos, asin, atan, sqrt, log10, ceil, pi

R_EARTH = 6371.0
CAGLIARI = (39.22, 9.11)
ANTIPODE = (-CAGLIARI[0], CAGLIARI[1] - 180)

# ---------------------------------------------------------------------------
# 1. Activite solaire [histoire] : nombre de Wolf moyen annuel (SIDC, V1)
# ---------------------------------------------------------------------------
WOLF = {1940: 67.8, 1941: 47.5, 1942: 30.6, 1943: 16.3, 1944: 9.6, 1945: 33.2,
        1946: 92.6, 1947: 151.6, 1948: 136.3, 1949: 134.7, 1950: 83.9,
        1951: 69.4, 1952: 31.5, 1953: 13.9, 1954: 4.4, 1955: 38.0,
        1956: 141.7, 1957: 190.2, 1958: 184.8, 1959: 159.0, 1960: 112.3}

# ---------------------------------------------------------------------------
# 2. Effets de l'impact sur l'ionosphere [estimation, hypotheses]
#    - les oxydes d'azote produits par la rentree des ejectas ionisent la
#      couche D sous le rayonnement Lyman-alpha : absorption de jour renforcee ;
#    - les atomes metalliques deposes (Na, Fe, Mg) nourrissent la couche E
#      sporadique : liaisons courtes (500-2 200 km) erratiques.
# ---------------------------------------------------------------------------
ABS_FACTOR = {1940: 4.0, 1941: 3.0, 1942: 1.8, 1943: 1.3}   # puis 1.0
ES_BONUS = {1940: "tres frequente", 1941: "frequente", 1942: "accrue"}
#    - la thermosphere, chauffee et chargee de vapeur d'eau et d'azote par le
#      panache de l'impact oceanique, recombine plus vite les electrons de la
#      couche F2 : comme un « orage ionospherique negatif » prolonge, foF2 baisse.
F2_FACTOR = {1940: 0.65, 1941: 0.75, 1942: 0.9}    # puis 1.0

# ---------------------------------------------------------------------------
# 3. Couche F2 : moyennes annuelles grossieres pour les latitudes moyennes
#    (foF2 de midi ~5-6 MHz au minimum solaire, ~12-13 MHz a R = 150 ;
#     de nuit ~2,8 MHz au minimum, ~5,5 MHz a R = 150).
# ---------------------------------------------------------------------------
H_F2 = 300.0        # km
H_D = 90.0          # km, hauteur de la couche absorbante
MIN_ELEV = 3.0      # degres, angle de depart minimal des antennes

def fof2(R, day):
    R = min(R, 200)
    return (5.5 + 0.045 * R) if day else (2.8 + 0.018 * R)

def hop_geometry(hop_km, h):
    """Angle de depart (deg) et angle d'incidence a la hauteur h (rad)."""
    theta = hop_km / (2 * R_EARTH)
    beta = atan((cos(theta) - R_EARTH / (R_EARTH + h)) / sin(theta))
    inc = asin(R_EARTH * cos(beta) / (R_EARTH + h))
    return degrees(beta), inc

def max_hop(h=H_F2, elev=MIN_ELEV):
    lo, hi = 100.0, 6000.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if hop_geometry(mid, h)[0] > elev:
            lo = mid
        else:
            hi = mid
    return lo

MAX_HOP = max_hop()

def slant_length(hop_km, h):
    """Longueur du rayon pour un bond (aller et retour dans la couche)."""
    theta = hop_km / (2 * R_EARTH)
    a, b = R_EARTH, R_EARTH + h
    return 2 * sqrt(a * a + b * b - 2 * a * b * cos(theta))

# ---------------------------------------------------------------------------
# 4. Pertes
# ---------------------------------------------------------------------------
F_GYRO = 1.2        # MHz
L_GROUND = 2.5      # dB par reflexion au sol supplementaire (mer surtout)
L_EXCESS = 10.0     # dB, pertes diverses (polarisation, fading moyen...)

def absorption(f, R, n_hops, inc_d, day, year):
    """Formule de George-Bradley (CCIR 252), angle zenithal solaire 50 deg."""
    if not day:
        return 0.5 * n_hops
    chi = radians(50)
    a = 677.2 * (1 + 0.0037 * R) * (cos(0.881 * chi)) ** 1.3 / ((f + F_GYRO) ** 1.98 + 10.2)
    return a * n_hops / cos(inc_d) * ABS_FACTOR.get(year, 1.0)

# ---------------------------------------------------------------------------
# 5. Bruit (facteur de bruit d'antenne Fa en dB au-dessus de kT0b)
# ---------------------------------------------------------------------------
def noise_fa(f, day):
    galactic = 52.0 - 23.0 * log10(f)
    rural_calme = 53.6 - 28.6 * log10(f)      # UIT-R P.372, site rural calme
    # bruit atmospherique (orages lointains), latitudes moyennes, ordre de grandeur
    # UIT-R P.372 : ~95 dB a 1 MHz la nuit, ~50 dB a 10 MHz ; ~25 dB de moins le jour
    atmos = (95.0 if not day else 72.0) - 45.0 * log10(f)
    # somme en puissance
    return 10 * log10(sum(10 ** (x / 10) for x in (galactic, rural_calme, atmos)))

def noise_dbm(f, day, bw_hz):
    return -174.0 + 10 * log10(bw_hz) + noise_fa(f, day)

# ---------------------------------------------------------------------------
# 6. Les stations [canon provisoire pour leur existence et leur puissance]
#    (nom, lat, lon, puissance d'emission en W, gain d'antenne dBi)
# ---------------------------------------------------------------------------
ILOT_TX_W = 1000      # station de l'ilot (chap. 16 §1)
ILOT_GAIN = 4.0       # gain supplementaire des antennes de l'ilot (losanges orientes)
FADING_MARGIN = 0.0   # le verdict (§ verdict) tient compte du fading

def g_elev(elev_deg):
    """Gain d'un doublet horizontal a ~1/2 longueur d'onde du sol selon l'angle de depart.
    Tres faible au ras de l'horizon (reflexion sur le sol), ~+6 dBi au-dessus de 20 deg."""
    from math import exp
    return 6.0 - 14.0 * exp(-elev_deg / 6.0)

STATIONS = [
    ("Minorque (Mahon)",              39.89,   4.26,  300, 0),
    ("Malte",                         35.90,  14.51,  500, 0),
    ("Gibraltar",                     36.14,  -5.35, 2000, 3),
    ("Crete (Souda)",                 35.49,  24.08, 1000, 0),
    ("Casablanca (Jean Bart)",        33.59,  -7.62, 1000, 0),
    ("Ecosse (Clyde)",                55.95,  -4.76, 1000, 0),
    ("Canaries (Las Palmas)",         28.12, -15.43,  300, 0),
    ("Acores (Horta)",                38.53, -28.63,  500, 0),
    ("Dakar (Richelieu, station AOF)",14.69, -17.44, 2000, 3),
    ("Oural (Sverdlovsk)",            56.84,  60.60, 5000, 3),
    ("Freetown",                       8.48, -13.23,  500, 0),
    ("Ceylan (Colombo)",               6.93,  79.85, 1000, 0),
    ("Martinique (Bearn)",            14.60, -61.07, 1000, 0),
    ("Maurice (Port-Louis)",         -20.16,  57.50,  300, 0),
    ("Floride (Key West)",            24.56, -81.78, 1000, 0),
    ("Perth (Fremantle)",            -32.06, 115.74, 1000, 0),
    ("Nouvelle-Zelande (Wellington)",-41.29, 174.78, 2000, 3),
]

def gc_km(a, b):
    la1, lo1, la2, lo2 = map(radians, (a[0], a[1], b[0], b[1]))
    c = sin(la1) * sin(la2) + cos(la1) * cos(la2) * cos(lo2 - lo1)
    return degrees(acos(max(-1.0, min(1.0, c)))) * pi / 180 * R_EARTH

def link(d_km, year, day, tx_w, tx_gain, rx_gain, bw_hz=500):
    """Renvoie (frequence MHz, SNR dB, n bonds) ; frequence = 0,85 x MUF."""
    R = WOLF[year]
    n = max(1, ceil(d_km / MAX_HOP))
    hop = d_km / n
    _, inc_f = hop_geometry(hop, H_F2)
    fo = fof2(R, day) * F2_FACTOR.get(year, 1.0)
    if not day and n >= 3:
        fo *= 0.8          # sur un long trajet de nuit, le point le plus faible (avant l'aube) commande
    muf = 1.1 * fo / cos(inc_f)
    f = min(max(0.85 * muf, 2.0), 22.0)     # bandes des emetteurs de 1940
    path = n * slant_length(hop, H_F2)
    fsl = 32.45 + 20 * log10(f) + 20 * log10(path)
    _, inc_d = hop_geometry(hop, H_D)
    loss = fsl + absorption(f, R, n, inc_d, day, year) + L_GROUND * (n - 1) + L_EXCESS
    elev, _ = hop_geometry(hop, H_F2)
    ge = g_elev(elev)
    p_rx = 10 * log10(tx_w * 1000) + tx_gain + rx_gain + 2 * ge - loss
    snr = p_rx - noise_dbm(f, day, bw_hz)
    return f, snr, n

def antipode_gain(lat, lon):
    d = gc_km(ANTIPODE, (lat, lon))
    return max(0.0, 10.0 * (1 - d / 2000.0))

def verdict(snr):
    """SNR median en telegraphie, 500 Hz. Le fading fait varier le signal de
    +/- 10 dB : il faut ~15 dB de median pour une liaison sure 90 % du temps."""
    if snr >= 15:
        return "sur"
    if snr >= 5:
        return "interm."
    if snr >= -3:
        return "rare"
    return "--"

PERIODES = [
    (1940, "automne 1940 : ionosphere tres perturbee"),
    (1941, "1941 : ionosphere perturbee, cycle descendant"),
    (1944, "1944 : minimum du cycle 17"),
    (1947, "1947 : maximum du cycle 18 (l'ete radio)"),
    (1954, "1954 : minimum du cycle 19"),
    (1957, "1957 : maximum du cycle 19, le plus fort jamais mesure"),
]

def report():
    print(f"Bond maximal (F2 a {H_F2:.0f} km, depart a {MIN_ELEV:.0f} deg) : {MAX_HOP:,.0f} km")
    print(f"Antipode de Cagliari : {ANTIPODE[0]:.2f}, {ANTIPODE[1]:.2f}\n")
    print("Activite solaire (nombre de Wolf annuel) :")
    print("  " + "  ".join(f"{y}:{r:.0f}" for y, r in WOLF.items()))
    for year, label in PERIODES:
        R = WOLF[year]
        print(f"\n=== {label} (R = {R:.0f}) ===")
        k = F2_FACTOR.get(year, 1.0)
        print(f"foF2 jour {k*fof2(R, True):.1f} MHz, nuit {k*fof2(R, False):.1f} MHz ; "
              f"facteur d'absorption {ABS_FACTOR.get(year, 1.0)} ; E sporadique : {ES_BONUS.get(year, 'normale')}")
        print(f"{'Station':32s} {'km':>6s} bonds | {'JOUR f':>6s} {'S/B':>5s} {'':6s} | {'NUIT f':>6s} {'S/B':>5s} {'':6s} | retour nuit")
        for name, la, lo, w, g in STATIONS:
            d = gc_km(CAGLIARI, (la, lo))
            ga = antipode_gain(la, lo)
            fd, sd, n = link(d, year, True, w, g + ga, ILOT_GAIN)
            fn, sn, _ = link(d, year, False, w, g + ga, ILOT_GAIN)
            # sens retour : l'ilot emet 1 kW vers la station
            _, sr, _ = link(d, year, False, ILOT_TX_W, ILOT_GAIN + ga, g)
            print(f"{name:32s} {d:6,.0f} {n:5d} | {fd:6.1f} {sd:5.0f} {verdict(sd):6s} | {fn:6.1f} {sn:5.0f} {verdict(sn):6s} | {sr:5.0f} {verdict(sr)}")
    # ondes moyennes / onde de sol
    print("\n=== Onde de sol, 500 kHz (frequence de detresse), 1 kW, mer [estimation] ===")
    print("Portee de jour ~ 300-500 km (Bizerte, Corse, Minorque, Malte limite) ; de nuit, onde")
    print("d'espace en ondes moyennes : 1 000 a 2 000 km.")
    # telephonie
    print("\n=== Telephonie (6 kHz) : il faut environ 11 dB de plus que la telegraphie (500 Hz) ===")

SYM = {"sur": "OK", "interm.": "~", "rare": "rare", "--": "-"}

def summary():
    """Tableau de synthese : verdict de nuit (meilleure fenetre) / de jour, par periode."""
    print("\n=== Synthese (nuit / jour) : OK sur, ~ intermittent, rare, - impossible ===")
    print(f"{'Station':32s} " + " ".join(f"{y:>11d}" for y, _ in PERIODES))
    for name, la, lo, w, g in STATIONS:
        d = gc_km(CAGLIARI, (la, lo))
        ga = antipode_gain(la, lo)
        cells = []
        for y, _ in PERIODES:
            _, sn, _ = link(d, y, False, w, g + ga, ILOT_GAIN)
            _, sd, _ = link(d, y, True, w, g + ga, ILOT_GAIN)
            cells.append(f"{SYM[verdict(sn)]}/{SYM[verdict(sd)]}")
        print(f"{name:32s} " + " ".join(f"{c:>11s}" for c in cells))

if __name__ == "__main__":
    report()
    summary()
