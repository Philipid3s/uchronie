# 01 — Paramètres physiques : la comète

## 1. Nature de l'objet [canon]

**Un noyau cométaire dormant de type Halley**, de période d'environ 70 à 150 ans, sur une **orbite rétrograde** très inclinée. Diamètre équivalent initial : environ 10,3 km. C'est un gros noyau, mais pas exceptionnel : Hale-Bopp mesurait environ 60 km, Halley environ 11 km.

| Propriété | Valeur | Justification |
|---|---|---|
| Densité | 600 kg/m³ | 67P : 533 kg/m³ ; 9P/Tempel 1 : ~400-600 |
| Albédo | 0,04 | Noyaux cométaires sombres |
| Résistance mécanique | ~4 300 Pa [calcul] | Objet très friable |
| Vitesse | 50 km/s | Orbite rétrograde (Halley : 66 km/s) |
| Composition | ~50 % de glaces, ~50 % de matière réfractaire de type chondrite carbonée (~3 % de soufre) | Rosetta, Stardust |
| Activité | Quasi nulle | Noyau éteint sous un manteau de poussières (Damocloïdes) |

## 2. Scission et train de deux fragments

**Analogue : la comète de Biela.** Elle s'est scindée vers 1842-1845. En 1852, ses deux composantes étaient séparées d'environ 2,4 millions de km.

[canon] Le noyau s'est scindé lors de son passage précédent au périhélie : une masse de 10 km et une de 2 km. À l'arrivée, elles sont écartées de **2,16 millions de km, soit 12 heures**. Pendant ce délai, la Terre tourne d'environ 180°. Les deux impacts ont donc lieu à la **même latitude** (48,585° N) et **en longitudes opposées**, vers 7 h du matin, heure solaire locale. L'hémisphère du matin fait face à l'apex de la Terre, ce qui est cohérent avec un objet rétrograde rapide.

## 3. Détection [estimation]

- Fragment A : magnitude absolue H ≈ 14,1. Il atteint la magnitude 12 environ 2 jours avant l'impact, 9 environ 12 h avant, et devient visible à l'œil nu dans les 2 à 3 dernières heures, dans le ciel nocturne du Pacifique Nord, une zone presque déserte.
- Fragment B : il arrive en plein jour sur la France, et il est invisible.
- Il n'existe en 1940 aucune surveillance systématique du ciel. **[canon] Aucune alerte.** Au mieux, quelques observateurs isolés notent un « astre mobile » dans la dernière heure.

## 4. Chronologie physique [canon + calcul]

Fuseaux horaires de 1940 : Londres à UTC+1 ; Paris (zone occupée) à UTC+2 ; Vichy à UTC+1 ; Hawaï à UTC−10 h 30 ; Japon à UTC+9 ; Californie à UTC−8. En Méditerranée occidentale, le soleil se couche vers 19:30 UTC début juillet.

| UTC | Événement |
|---|---|
| **1er juil. 19:00** | **Impact A.** Boule de feu de 146 km de rayon. Séisme M 9,9 |
| 19:00 – 19:15 | Le panache d'éjectas sort de l'atmosphère. Des centaines de milliers de km³ de roche fondue et vaporisée sont projetés sur des trajectoires balistiques |
| 19:10 – 19:40 | **Pluie d'éjectas près de l'impact** (moins de 3 000 km) : Aléoutiennes, Alaska, Kamtchatka, Hokkaido. Le ciel s'embrase |
| 19:15 – 19:20 | Les ondes sismiques atteignent la Méditerranée (secousses faibles, sismographes saturés) |
| 19:30 | Tsunami de **plus de 1 000 m** au large d'Adak |
| **19:35 – 20:30** | **Pluie d'éjectas en Europe, en Afrique du Nord et au Moyen-Orient** (distance de 90 à 100°). En Méditerranée occidentale, juste après le coucher du soleil, des étoiles filantes de plus en plus denses, puis un **ciel incandescent pendant environ 30 à 45 minutes** ([03](03-impact-pacifique.md) §4) |
| 19:50 – 21:00 | Pluie d'éjectas à l'antipode et autour (Atlantique Sud, Afrique australe, Argentine) : **flux renforcé par focalisation** |
| 20:25 | Tsunami de 390 m au large de Dutch Harbor |
| ~22:00 – 23:00 | L'onde de pression atteint Hawaï et le Japon |
| **23:55** | **Tsunami sur Hawaï** (~110 m au large) |
| **2 juil. 00:05** | **Tsunami sur le Japon** (~105 m au large) |
| 01:25 | Tsunami sur San Francisco (~86 m au large) |
| ~02:30 – 03:00 | L'onde de pression atteint l'Europe |
| **07:00** | **Impact B, Rambouillet** |
| 07:03 | Le souffle atteint Paris |
| 07:15 – 07:18 | Le souffle atteint Vichy, Bruxelles et Londres |
| 08:00 – 08:15 | Détonation lointaine à Cagliari, Alger, Mers el-Kébir et Gibraltar |
| 2 juil., journée | Le voile de poussières et de suies se referme sur l'hémisphère Nord |
| **3 – 5 juil.** | **La nuit d'impact s'installe sur toute la planète** |

## 5. Entrée atmosphérique [calcul]

Les deux fragments commencent à se fragmenter vers 106 km d'altitude mais atteignent le sol avec 97 à 99 % de leur énergie. Ce sont de vrais impacts cratérisants. Le fragment A traverse la colonne d'eau de 5,5 km sans ralentir notablement, et sa cavité excave le plancher océanique sur plus de 25 km de profondeur.

## 6. Limites du modèle

- Pour les très grandes énergies, le panache perce l'atmosphère et une part de l'énergie s'échappe vers l'espace. **[canon] On applique un couplage d'un tiers pour le souffle et le rayonnement direct** (colonnes « canon » du script).
- **La pluie d'éjectas n'est pas calculée par le script.** Elle est estimée à partir de la littérature sur Chicxulub (voir [03](03-impact-pacifique.md) §4). C'est l'incertitude la plus lourde de conséquences pour la survie.
- Pour le tsunami, le modèle d'onde de bord en 1/r est incertain d'un facteur 2 à 3.
