"""Défense du golfe de Cagliari : distances, portées et couverture de l'entrée.

Chapitre 24 (le Hood, forteresse du golfe). Positions approchées [canon provisoire],
portées des pièces à vérifier (🔎). Sortie : python calculs/defense_golfe.py
"""
from math import radians, sin, cos, asin, sqrt

R_TERRE = 6371.0  # km


def dist(a, b):
    """Distance orthodromique en km entre deux points (lat, lon) en degrés."""
    la1, lo1, la2, lo2 = map(radians, (a[0], a[1], b[0], b[1]))
    h = sin((la2 - la1) / 2) ** 2 + cos(la1) * cos(la2) * sin((lo2 - lo1) / 2) ** 2
    return 2 * R_TERRE * asin(sqrt(h))


POINTS = {
    "Hood posé (devant Su Siccu)": (39.1795, 9.128),
    "Dunkerque (mouillage de Su Siccu)": (39.193, 9.1255),
    "Batterie du port (Sella del Diavolo)": (39.188, 9.164),
    "Batterie de l'est (Capo Boi, lisière de la Zone)": (39.130, 9.360),
    "Batterie de l'ouest (Capo di Pula, Nora)": (38.990, 9.016),
    "Capo Carbonara (dans la Zone)": (39.098, 9.520),
    "Capo Spartivento": (38.877, 8.845),
}

PORTEE_381 = 27.6  # km : 381 mm Mk I, tourelle Mk II, hausse 30° [à vérifier]
PORTEE_102 = 18.0  # km : 102 mm QF Mk XVI [à vérifier]


def couverture(segment, batteries, n=2000):
    """Part (en %) d'un segment située à portée d'au moins une des batteries (pos, portée)."""
    (a, b), ok = segment, 0
    for i in range(n + 1):
        t = i / n
        p = (a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1]))
        ok += any(dist(p, pos) <= r for pos, r in batteries)
    return 100 * ok / (n + 1)


def horizon(h_m):
    """Distance de l'horizon géométrique (km) pour un œil à h_m mètres, réfraction comprise."""
    return 3.57 * sqrt(h_m)


if __name__ == "__main__":
    hood = POINTS["Hood posé (devant Su Siccu)"]
    est = POINTS["Batterie de l'est (Capo Boi, lisière de la Zone)"]
    ouest = POINTS["Batterie de l'ouest (Capo di Pula, Nora)"]
    entree = (ouest, POINTS["Capo Carbonara (dans la Zone)"])

    print("Distances depuis le Hood posé :")
    for nom, pos in POINTS.items():
        if pos != hood:
            print(f"  {nom:<50} {dist(hood, pos):5.1f} km")
    print(f"\nLargeur de l'entrée (Pula – Carbonara) : {dist(*entree):.1f} km")
    print(f"Batterie de l'est – Capo Carbonara : {dist(est, entree[1]):.1f} km")

    print("\nCouverture de la ligne d'entrée Pula – Carbonara :")
    print(f"  381 mm du Hood seul        : {couverture(entree, [(hood, PORTEE_381)]):5.0f} %")
    print(f"  102 mm des deux caps       : {couverture(entree, [(est, PORTEE_102), (ouest, PORTEE_102)]):5.0f} %")
    print(f"  ensemble                   : {couverture(entree, [(hood, PORTEE_381), (est, PORTEE_102), (ouest, PORTEE_102)]):5.0f} %")

    print("\nHorizon (km) :")
    for h, nom in [(35, "direction de tir du Hood"), (120, "Sella del Diavolo (Sant'Elia)"), (1067, "vigie du Serpeddì")]:
        print(f"  {nom:<32} {h:5d} m  -> {horizon(h):6.1f} km")
