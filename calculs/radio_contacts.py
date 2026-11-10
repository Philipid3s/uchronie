"""Distances des stations survivantes plausibles : depuis Cagliari (portee radio)
et depuis l'impact A (pluie d'ejectas, voir 03 §4). Usage : python calculs/radio_contacts.py"""
from math import radians, degrees, sin, cos, acos

CAGLIARI = (39.22, 9.11)
IMPACT_A = (48.585, -178.255)
R = 6371.0

STATIONS = [
    ("Gibraltar", 36.14, -5.35), ("Malte (La Valette)", 35.90, 14.51),
    ("Bizerte", 37.27, 9.87), ("Minorque (Mahon)", 39.89, 4.26),
    ("Souda (Crete)", 35.49, 24.08), ("Alexandrie", 31.20, 29.92),
    ("Haifa", 32.82, 34.99), ("Chypre (Famagouste)", 35.12, 33.94),
    ("Sebastopol", 44.62, 33.52), ("Casablanca", 33.59, -7.62),
    ("Dakar", 14.69, -17.44), ("Acores (Ponta Delgada)", 37.74, -25.67),
    ("Canaries (Las Palmas)", 28.12, -15.43), ("Scapa Flow", 58.90, -3.10),
    ("Clyde (Greenock)", 55.95, -4.76), ("Islande (Reykjavik)", 64.15, -21.94),
    ("Freetown", 8.48, -13.23), ("Aden", 12.79, 45.03),
    ("Bombay", 18.94, 72.84), ("Ceylan (Trincomalee)", 8.57, 81.23),
    ("Diego-Suarez", -12.28, 49.29), ("Maurice (Port-Louis)", -20.16, 57.50),
    ("Mombasa", -4.05, 39.67), ("Simonstown (Le Cap)", -34.19, 18.43),
    ("Martinique (Fort-de-France)", 14.60, -61.07), ("Floride (Key West)", 24.56, -81.78),
    ("Rio de Janeiro", -22.91, -43.17), ("Saigon", 10.78, 106.70),
    ("Singapour", 1.29, 103.85), ("Surabaya", -7.25, 112.75),
    ("Nouvelle-Zelande (Wellington)", -41.29, 174.78), ("Perth (Fremantle)", -32.06, 115.74),
    ("Oural (Sverdlovsk)", 56.84, 60.60), ("Chili austral (Punta Arenas)", -53.16, -70.91),
]

def ang(a, b):
    la1, lo1, la2, lo2 = map(radians, (a[0], a[1], b[0], b[1]))
    c = sin(la1)*sin(la2) + cos(la1)*cos(la2)*cos(lo2-lo1)
    return degrees(acos(max(-1.0, min(1.0, c))))

print("| Station | Distance de Cagliari (km) | Distance angulaire de l'impact A |")
print("|---|---|---|")
for name, la, lo in sorted(STATIONS, key=lambda s: ang(CAGLIARI, s[1:])):
    print(f"| {name} | {ang(CAGLIARI,(la,lo))*R*3.14159265/180:,.0f} | {ang(IMPACT_A,(la,lo)):.1f} deg |")
