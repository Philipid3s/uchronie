"""
Calculs d'effets d'impact pour l'uchronie "Comete de juillet 1940".

Modele : Collins, Melosh & Marcus (2005), "Earth Impact Effects Program",
Meteoritics & Planetary Science 40(6), 817-840 (equations reprises ici).
Tsunami : modele d'onde de bord en 1/r (Ward & Asphaug 2000 ; Impact:Earth).

Usage : python impact_effects.py > ../annexes/resultats_calculs.md
"""
import math

# --- constantes -------------------------------------------------------------
G = 9.81            # m/s2
R_E = 6.371e6       # m
H = 8000.0          # hauteur d'echelle atmospherique (m)
RHO0 = 1.0          # densite de l'air au sol (kg/m3) (valeur Collins)
CD = 2.0            # coefficient de trainee
P0 = 1.0e5          # pression atmospherique (Pa)
C0 = 330.0          # vitesse du son (m/s)
ETA = 3e-3          # efficacite lumineuse (fraction de E en rayonnement)
MT = 4.184e15       # J par megatonne
RHO_W = 1000.0
# Couplage au sol pour les tres grandes energies : quand la boule de feu depasse
# largement la hauteur d'echelle (8 km), le panache perce l'atmosphere et une
# part importante de l'energie s'echappe vers l'espace. Variante [canon] : 1/3.
COUPLING = 1 / 3


def haversine(lat1, lon1, lat2, lon2):
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp, dl = p2 - p1, math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * R_E * math.asin(math.sqrt(a))


# --- entree atmospherique (Collins sec. 4) -----------------------------------
def entry(L0, rho_i, v0, theta_deg):
    th = math.radians(theta_deg)
    Yi = 10 ** (2.107 + 0.0624 * math.sqrt(rho_i))           # resistance (Pa)
    If = 4.07 * CD * H * Yi / (rho_i * L0 * v0 ** 2 * math.sin(th))
    out = {"Yi": Yi, "If": If}
    if If >= 1:
        out.update(z_star=0, v_ground=v0, L_ground=L0, airburst=False)
        return out
    z_star = -H * (math.log(Yi / (RHO0 * v0 ** 2)) + 1.308 - 0.314 * If
                   - 1.303 * math.sqrt(1 - If))
    rho_zs = RHO0 * math.exp(-z_star / H)
    v_zs = v0 * math.exp(-3 * rho_zs * CD * H / (4 * rho_i * L0 * math.sin(th)))
    l = L0 * math.sin(th) * math.sqrt(rho_i / (CD * rho_zs))
    fp = 7.0
    z_b = z_star - 2 * H * math.log(1 + (l / (2 * H)) * math.sqrt(fp ** 2 - 1))

    def L_of(z):
        return L0 * math.sqrt(1 + (2 * H / l) ** 2 *
                              (math.exp((z_star - z) / (2 * H)) - 1) ** 2)

    # integration numerique de la deceleration de z* jusqu'au sol (ou z_b)
    z_end = max(z_b, 0.0)
    n = 4000
    dz = (z_star - z_end) / n
    integ = 0.0
    for k in range(n):
        z = z_star - (k + 0.5) * dz
        integ += math.exp((z_star - z) / H) * L_of(z) ** 2 * dz
    v_end = v_zs * math.exp(-0.75 * CD * rho_zs * integ /
                            (rho_i * L0 ** 3 * math.sin(th)))
    out.update(z_star=z_star, z_b=z_b, v_zs=v_zs, v_ground=v_end,
               L_ground=L_of(z_end), airburst=z_b > 0)
    return out


# --- cratere (Collins sec. 6) -----------------------------------------------
def crater_land(L, rho_i, v, theta_deg, rho_t=2500.0):
    th = math.radians(theta_deg)
    Dtc = 1.161 * (rho_i / rho_t) ** (1 / 3) * L ** 0.78 * v ** 0.44 * \
        G ** -0.22 * math.sin(th) ** (1 / 3)
    Dc = 3200.0  # transition simple/complexe (roches sedimentaires ~ 2-4 km)
    if Dtc * 1.25 < Dc:
        Dfr = 1.25 * Dtc
    else:
        Dfr = 1.17 * Dtc ** 1.13 / Dc ** 0.13
    # Collins eq. 28 : profondeur des crateres complexes, D en km
    depth = (0.294 * (Dfr / 1000) ** 0.301 * 1000 if Dfr > Dc
             else Dtc / (2 * math.sqrt(2)))
    return Dtc, Dfr, depth


def crater_water(L, rho_i, v, theta_deg, depth_w):
    th = math.radians(theta_deg)
    Dtcw = 1.365 * (rho_i / RHO_W) ** (1 / 3) * L ** 0.78 * v ** 0.44 * \
        G ** -0.22 * math.sin(th) ** (1 / 3)
    v_sf = v * math.exp(-3 * RHO_W * CD * depth_w / (2 * rho_i * L * math.sin(th)))
    return Dtcw, v_sf


# --- effets a distance --------------------------------------------------------
def overpressure(E_J, r):
    """Surpression (Pa) - explosion de surface, loi d'echelle 1 kt (Collins eq. 54)."""
    E_kt = E_J / (MT / 1000)
    r1 = r / E_kt ** (1 / 3)
    px, rx = 75000.0, 290.0
    return px * rx / (4 * r1) * (1 + 3 * (rx / r1) ** 1.3)


def wind(p):
    return 5 * p / (7 * P0) * C0 / math.sqrt(1 + 6 * p / (7 * P0))


def thermal(E_J, r):
    """Exposition thermique (J/m2) avec fraction de boule de feu au-dessus de l'horizon."""
    Rf = 0.002 * E_J ** (1 / 3)
    delta = r / R_E
    h = (1 - math.cos(delta)) * R_E / math.cos(delta)
    if h >= Rf:
        return 0.0, Rf
    d = math.acos(h / Rf)
    f = 2 / math.pi * (d - (h / Rf) * math.sin(d))
    return f * ETA * E_J / (2 * math.pi * r ** 2), Rf


def thermal_thresholds(E_J):
    """Seuils (J/m2) a 1 Mt (Collins tab. 3), mis a l'echelle E^(1/6)."""
    s = (E_J / MT) ** (1 / 6)
    base = {"vetements s'enflamment": 1.0e6, "contreplaque s'enflamme": 0.67e6,
            "brulures 3e degre": 0.42e6, "herbe seche s'enflamme": 0.38e6,
            "brulures 2e degre": 0.25e6, "brulures 1er degre": 0.13e6}
    return {k: v * s for k, v in base.items()}


def seismic(E_J, r):
    M = 0.67 * math.log10(E_J) - 5.87
    rk = r / 1000
    if rk < 60:
        Me = M - 0.0238 * rk
    elif rk < 700:
        Me = M - 0.0048 * rk - 1.1644
    else:
        Me = M - 1.66 * math.log10(rk / 111.2) - 6.399
    return M, Me


def mercalli(Me):
    table = [(1, "I"), (2, "I-II"), (3, "III-IV"), (4, "IV-V"), (5, "VI-VII"),
             (6, "VII-VIII"), (7, "VIII-IX"), (8, "IX-X"), (9, "X-XI")]
    for lim, lab in table:
        if Me < lim:
            return lab
    return "XII"


def ejecta(Dtc, r):
    return Dtc ** 4 / (112 * r ** 3)


def blast_damage(p):
    if p > 4.26e5: return "beton arme detruit"
    if p > 2.73e5: return "ponts metalliques effondres"
    if p > 1.0e5:  return "immeubles beton/acier gravement endommages"
    if p > 4.0e4:  return "immeubles maconnes effondres"
    if p > 2.7e4:  return "maisons ossature bois detruites, maconnerie fissuree"
    if p > 1.4e4:  return "toitures arrachees, murs fissures"
    if p > 6.9e3:  return "vitres brisees, degats legers"
    if p > 1.5e3:  return "quelques vitres brisees"
    return "-"


def thermal_effect(phi, th):
    for k in ["vetements s'enflamment", "brulures 3e degre", "herbe seche s'enflamme",
              "brulures 2e degre", "brulures 1er degre"]:
        if phi >= th[k]:
            return k
    return "-"


# --- scenario -------------------------------------------------------------------
RHO_I = 600.0
V0 = 50000.0
THETA = 45.0

EUROPE = dict(name="Fragment B - Rambouillet", L=2000.0, lat=48.585, lon=1.745)
PACIF = dict(name="Fragment A - Pacifique Nord", L=10000.0, lat=48.585, lon=-178.255,
             depth=5500.0)

SITES_EU = [
    ("Rambouillet", 48.644, 1.830), ("Epernon", 48.610, 1.675),
    ("Chartres", 48.447, 1.489), ("Versailles", 48.805, 2.120),
    ("Paris (Notre-Dame)", 48.853, 2.349), ("Saint-Denis", 48.936, 2.357),
    ("Dreux", 48.737, 1.366), ("Etampes", 48.435, 2.161),
    ("Melun", 48.540, 2.660), ("Fontainebleau", 48.405, 2.702),
    ("Evreux", 49.024, 1.151), ("Orleans", 47.903, 1.909),
    ("Beauvais", 49.430, 2.081), ("Rouen", 49.443, 1.099),
    ("Compiegne", 49.418, 2.826), ("Le Mans", 48.006, 0.199),
    ("Tours", 47.394, 0.684), ("Reims", 49.258, 4.032),
    ("Amiens", 49.894, 2.296), ("Caen", 49.183, -0.370),
    ("Le Havre", 49.494, 0.108), ("Lille", 50.629, 3.057),
    ("Vichy", 46.127, 3.426), ("Bruxelles", 50.850, 4.352),
    ("Londres", 51.507, -0.128), ("Portsmouth", 50.805, -1.087),
    ("Brest", 48.390, -4.486), ("Lyon", 45.764, 4.836),
    ("Nerac (Amiraute)", 44.136, 0.339), ("Bordeaux", 44.838, -0.579),
    ("Strasbourg", 48.573, 7.752), ("Cologne", 50.938, 6.960),
    ("QG Tannenberg (Foret-Noire)", 48.470, 8.270), ("Berlin", 52.520, 13.405),
    ("Toulon", 43.124, 5.928), ("Gibraltar", 36.140, -5.353),
    ("Mers el-Kebir", 35.728, -0.706),
    ("Ajaccio (Corse)", 41.919, 8.738), ("La Maddalena (Sardaigne)", 41.214, 9.408),
    ("Cagliari (Sardaigne)", 39.223, 9.122), ("Carbonia (Sulcis)", 39.167, 8.522),
    ("Palma (Majorque)", 39.570, 2.650), ("Mahon (Minorque)", 39.889, 4.265),
    ("La Valette (Malte)", 35.899, 14.514), ("Souda (Crete)", 35.488, 24.075),
    ("Rome", 41.902, 12.496), ("Alger", 36.754, 3.058),
]

SITES_PAC = [
    ("Adak (Aleoutiennes)", 51.88, -176.65), ("Dutch Harbor", 53.89, -166.54),
    ("Midway", 28.21, -177.37), ("Petropavlovsk", 53.02, 158.65),
    ("Kodiak", 57.79, -152.41), ("Sitka", 57.05, -135.33),
    ("Kushiro (Hokkaido)", 42.98, 144.38), ("Kamaishi (Sanriku)", 39.27, 141.89),
    ("Choshi (Boso)", 35.73, 140.83), ("Yokosuka", 35.28, 139.67),
    ("Tokyo", 35.68, 139.77), ("Osaka", 34.69, 135.50),
    ("Kure (mer interieure)", 34.24, 132.56), ("Honolulu", 21.31, -157.86),
    ("Pearl Harbor", 21.35, -157.97), ("Hilo", 19.72, -155.07),
    ("Wake", 19.28, 166.65), ("Guam", 13.44, 144.79),
    ("Vancouver (abrite)", 49.28, -123.12), ("Astoria (Columbia)", 46.19, -123.83),
    ("San Francisco", 37.77, -122.42), ("Los Angeles (San Pedro)", 33.74, -118.27),
    ("San Diego", 32.70, -117.20), ("Manille", 14.60, 120.98),
    ("Shanghai", 31.23, 121.47), ("Hong Kong", 22.30, 114.17),
    ("Callao (Perou)", -12.05, -77.15), ("Valparaiso", -33.05, -71.62),
    ("Sydney", -33.87, 151.21), ("Auckland", -36.85, 174.76),
]


def fmt(x, unit=""):
    if x >= 1e6: return f"{x/1e6:.1f} M{unit}"
    if x >= 1e3: return f"{x/1e3:.1f} k{unit}"
    return f"{x:.2f} {unit}"


def main():
    print("# Resultats des calculs (genere par calculs/impact_effects.py)\n")
    print(f"Hypotheses communes : noyau cometaire, densite {RHO_I:.0f} kg/m3, "
          f"vitesse d'entree {V0/1000:.0f} km/s, angle {THETA:.0f} deg.\n")

    for frag in (PACIF, EUROPE):
        L = frag["L"]
        m = RHO_I * math.pi * L ** 3 / 6
        E0 = 0.5 * m * V0 ** 2
        ent = entry(L, RHO_I, V0, THETA)
        E = 0.5 * m * ent["v_ground"] ** 2
        print(f"## {frag['name']}\n")
        print(f"- Point d'impact : {frag['lat']:.3f} N, {frag['lon']:.3f} E")
        print(f"- Diametre : {L:.0f} m ; masse : {m:.3e} kg")
        print(f"- Energie a l'entree : {E0:.3e} J = {E0/MT:,.0f} Mt")
        print(f"- Fragmentation atmospherique a z* = {ent['z_star']/1000:.0f} km "
              f"(resistance {ent['Yi']:.0f} Pa) ; atteint le sol : "
              f"{'non (explosion aerienne)' if ent['airburst'] else 'oui'}")
        print(f"- Diametre du nuage de debris au sol : {ent['L_ground']:.0f} m ; "
              f"vitesse au sol : {ent['v_ground']/1000:.1f} km/s")
        print(f"- Energie deposee au sol : {E:.3e} J = {E/MT:,.0f} Mt")
        # L'energie perdue par freinage l'est a ~90 % sous 10 km d'altitude :
        # elle s'ajoute au souffle et au rayonnement (explosion basse + impact).
        # Souffle/thermique -> energie totale E0 ; cratere/seisme -> energie au sol E.
        E_air = E0
        print(f"- Energie retenue pour souffle et rayonnement : {E_air/MT:,.0f} Mt")
        M, _ = seismic(E, 1)
        print(f"- Magnitude sismique equivalente : {M:.1f}")
        _, Rf = thermal(E_air, 1000)
        print(f"- Rayon maximal de la boule de feu : {Rf/1000:.1f} km")

        if "depth" in frag:
            Dtcw, v_sf = crater_water(L, RHO_I, ent["v_ground"], THETA, frag["depth"])
            print(f"- Profondeur d'eau : {frag['depth']:.0f} m")
            print(f"- Cratere transitoire dans l'eau : {Dtcw/1000:.1f} km de diametre, "
                  f"~{Dtcw/2.828/1000:.1f} km de profondeur (> profondeur d'eau : "
                  f"le fond est atteint)")
            print(f"- Vitesse residuelle du projectile au fond (modele Collins) : "
                  f"{v_sf:.2e} m/s -> cratere du plancher par le projectile negligeable ;"
                  f" excavation du fond par la cavite d'eau elle-meme")
            A_rw = min(Dtcw / 14.1, frag["depth"])
            R_rw = 0.75 * Dtcw
            print(f"- Onde de bord : amplitude {A_rw:.0f} m a {R_rw/1000:.0f} km\n")
            print("| Lieu | Distance (km) | Amplitude au large (m) | Arrivee (h) | "
                  "Surpression (kPa) | Seisme (Mercalli) |")
            print("|---|---|---|---|---|---|")
            for name, la, lo in SITES_PAC:
                r = haversine(frag["lat"], frag["lon"], la, lo)
                A = A_rw * R_rw / r
                t = r / 1000 / 720.0
                p = overpressure(E_air, r)
                _, Me = seismic(E, r)
                print(f"| {name} | {r/1000:,.0f} | {A:.1f} | {t:.1f} | "
                      f"{p/1000:.2f} | {mercalli(Me)} |")
            print()
        else:
            Dtc, Dfr, dep = crater_land(L, RHO_I, ent["v_ground"], THETA)
            print(f"- Cratere transitoire : {Dtc/1000:.1f} km ; cratere final : "
                  f"{Dfr/1000:.1f} km ; profondeur finale : ~{dep:.0f} m")
            th = thermal_thresholds(E_air)
            print("- Seuils thermiques (mis a l'echelle) : " +
                  "; ".join(f"{k} {v/1e6:.2f} MJ/m2" for k, v in th.items()) + "\n")
            Ec = E_air * COUPLING
            thc = thermal_thresholds(Ec)
            print("Colonnes 'brut' : loi d'echelle directe. Colonnes 'canon' : "
                  f"couplage {COUPLING:.2f} (echappement du panache).\n")
            print("| Lieu | Distance (km) | Surpression brut (kPa) | Surpression canon (kPa) | "
                  "Vent canon (m/s) | Degats canon | Thermique canon (MJ/m2) | "
                  "Effet thermique canon | Ejectas (cm) | Seisme (Mercalli) | "
                  "Arrivee souffle (min) |")
            print("|---|---|---|---|---|---|---|---|---|---|---|")
            for name, la, lo in SITES_EU:
                r = haversine(frag["lat"], frag["lon"], la, lo)
                p = overpressure(E_air, r)
                pc = overpressure(Ec, r)
                phic, _ = thermal(Ec, r)
                _, Me = seismic(E, r)
                t_e = ejecta(Dtc, r) * 100
                print(f"| {name} | {r/1000:,.0f} | {p/1000:.1f} | {pc/1000:.1f} | "
                      f"{wind(pc):.0f} | {blast_damage(pc)} | {phic/1e6:.2f} | "
                      f"{thermal_effect(phic, thc)} | {t_e:.2f} | {mercalli(Me)} | "
                      f"{r/C0/60:.0f} |")
            print()
            # rayons caracteristiques
            print("### Rayons caracteristiques\n")
            def radius(fn, thr):
                lo_, hi_ = 100.0, 3e6
                for _ in range(80):
                    mid = (lo_ + hi_) / 2
                    if fn(mid) > thr: lo_ = mid
                    else: hi_ = mid
                return lo_ / 1000
            for lab, thr in [("beton arme detruit (426 kPa)", 4.26e5),
                             ("immeubles beton/acier gravement endommages (100 kPa)", 1e5),
                             ("immeubles maconnes effondres (40 kPa)", 4e4),
                             ("maisons detruites (27 kPa)", 2.7e4),
                             ("toitures arrachees (14 kPa)", 1.4e4),
                             ("vitres brisees (6.9 kPa)", 6.9e3)]:
                print(f"- {lab} : brut {radius(lambda r: overpressure(E_air, r), thr):.0f} km"
                      f" / canon {radius(lambda r: overpressure(Ec, r), thr):.0f} km")
            for k in ["vetements s'enflamment", "brulures 3e degre",
                      "herbe seche s'enflamme", "brulures 2e degre"]:
                print(f"- {k} : brut {radius(lambda r: thermal(E_air, r)[0], th[k]):.0f} km"
                      f" / canon {radius(lambda r: thermal(Ec, r)[0], thc[k]):.0f} km")
            print()


if __name__ == "__main__":
    main()
