# 16 — Les voix dans la nuit : qui émet encore, et qui la Sardaigne peut-elle entendre ?

> **Question de l'auteur** : quelles zones de vie émettent encore par radio et pourraient être contactées depuis la Sardaigne ?
>
> Les distances sont des [calcul] (`python calculs/radio_contacts.py`). La propagation est un [calcul] d'ordre de grandeur (`python calculs/radio_propagation.py`, sortie dans [annexes/resultats_radio.txt](annexes/resultats_radio.txt)) : bilan de liaison en ondes courtes avec l'activité solaire réelle de 1940-1960 (§2 bis). Les effets de l'impact sur l'ionosphère sont des [estimation]. La liste des stations et leur sort sont [canon provisoire], sauf mention contraire.

## 1. Les moyens de l'îlot

- **Les émetteurs** : les stations radio du *Dunkerque* et de l'*Ark Royal*, celle de la Marine italienne à Cagliari, puis une **station à terre** montée avec le matériel des navires désarmés et alimentée par le charbon et les barrages ([15](15-energie.md)). Un grand bâtiment de 1940 porte des émetteurs **en ondes moyennes** (autour de 500 kHz, la fréquence internationale de détresse) et **en ondes courtes** (environ 2 à 20 MHz), de quelques centaines de watts à environ 1 à 2 kW [ordre de grandeur, à vérifier]. Le modèle retient **1 kW** pour la station de l'îlot.
- **Les antennes** : de longs fils et, pour la station à terre, des **antennes en losange** orientées vers Gibraltar et Dakar, qui gagnent quelques décibels dans leur direction. Elles ne coûtent que du fil de cuivre et des poteaux.
- **Les récepteurs** : les récepteurs de trafic des navires, avec des **filtres à quartz** étroits qui isolent un signal Morse [histoire]. Les lampes de rechange sont le vrai capital : sans elles, la radio meurt en une dizaine d'années [estimation].
- **Le mode** : surtout la **télégraphie en Morse**, qui porte bien plus loin que la voix à puissance égale. Les **codes Q** internationaux, que connaissent tous les radios de marine du monde, contournent la barrière des langues.
- **Les hommes et les femmes** : le corps des Transmissions ([13](13-societe-de-bord.md) §4 ter) tient une **veille permanente**.
- **La politique** : de 1944 à 1949, l'Île fermée **écoute mais ne répond presque plus**, pour ne pas attirer les bateaux de réfugiés ([14](14-epidemie.md) §5.5).

## 1 bis. Les stations de l'îlot : deux sites au bord du golfe et des vigies en altitude [canon : principe ; provisoire : détail]

**Décision de l'auteur** (option C) : l'**émetteur** et le **récepteur** sont séparés, sur deux sites plats au bord du golfe de Cagliari ; des **vigies** en altitude guettent et relaient.

**Pourquoi pas une station au sommet** [calcul, ordre de grandeur] : l'altitude ne sert vraiment qu'aux liaisons en ligne droite (horizon radio ≈ 4,1 × √h km : ~45 km depuis une colline de 120 m, ~130 km depuis un sommet de 1 000 m). En ondes courtes à longue distance, ce qui compte est l'**angle de départ** (des antennes hautes par rapport à la longueur d'onde), un **sol conducteur** (l'eau de mer gagne plusieurs décibels aux angles bas) et la **place** pour de grandes antennes. En ondes moyennes, l'onde de sol porte mieux sur la mer et les terrains salés. Les marines de l'époque séparaient l'émetteur et le récepteur de plusieurs kilomètres, pour que le premier n'assourdisse pas le second [histoire].

| Site | Rôle | Pourquoi là | Mise en service |
|---|---|---|---|
| **Molentargius – Poetto**, à l'est de Cagliari | **Centre d'émission** : émetteurs d'ondes courtes (1 kW) et d'ondes moyennes (500 kHz) | Terrain plat et salé entre les bassins des salines et la plage : un excellent sol électrique, de la place pour les **antennes en losange** orientées vers Gibraltar et Dakar (plusieurs centaines de mètres) et des **antennes verticales** au bord de l'eau. Proche de l'électricité de la ville | **1942**, quand les navires du golfe sont désarmés et cèdent leurs émetteurs |
| **Elmas**, à l'ouest de Cagliari | **Centre de réception** et veille permanente | À une dizaine de kilomètres de l'émetteur, sur l'aérodrome plat et silencieux. La radio de l'aviation y était déjà ; la Flottille y revient en 1949 ([20](20-capacites-aeronavales.md)) | **1942** |
| **Le *Dunkerque*** (siège du Conseil) | **Salle des transmissions** : le Conseil y reçoit les messages | Les deux centres y sont reliés par des **lignes téléphoniques** ; l'émetteur est manipulé à distance depuis Elmas [histoire : pratique courante des stations côtières] | 1942 |
| **Guardia Vecchia** (La Maddalena) | **Vigie du nord** : les Bouches de Bonifacio, la Corse, les barques de réfugiés | Le fort domine l'archipel ; la Regia Marina y avait un poste de signaux [histoire, à vérifier] | **Dès 1940** |
| **Monte Serpeddì** (1 067 m, Sette Fratelli) | **Vigie du sud-est** : la côte du Sarrabus, la Ligne de la Zone, le golfe de Cagliari | Le plus haut sommet au-dessus de Cagliari, à la limite de la Zone ([14](14-epidemie.md) §5.4) | **1944**, avec la Zone |
| **Monte Limbara** (1 359 m, Gallura) | **Vigie du nord-est** : la Gallura, les Bouches, la mer Tyrrhénienne | Le sommet de la Gallura ; il n'est accessible qu'avec l'expansion vers le nord ([21](21-demographie.md) §5.6) | **Vers 1958** |

**Les vigies** [canon provisoire] : un petit poste de 4 à 8 personnes, relevé chaque mois. On y guette les voiles à la lunette, on y fait des **relevés météorologiques** pour les cultures et la navigation, on signale de jour par projecteur et pavillons, et l'on dispose d'un **poste radio de 50 à 100 W** pour prévenir Cagliari. Une vigie en altitude voit un navire à 60-80 km par temps clair : c'est elle qui donne l'alerte avant la garde des côtes.

**Ce que cela coûte** : l'émetteur au bord de la plage est **vulnérable** à un débarquement ; il est gardé comme un dépôt. Les lignes entre Elmas, Cagliari et le Poetto doivent être entretenues ; une coupure isole le Conseil, et le *Dunkerque* garde ses propres émetteurs en secours.

## 2. La physique : une ionosphère malade, puis un ciel radio exceptionnel [estimation]

À longue distance, les ondes courtes rebondissent sur l'**ionosphère**, entre 60 et 400 km d'altitude. **Les poussières et la suie de l'hiver d'impact sont plus bas**, dans la stratosphère (20 à 50 km). Elles n'empêchent pas le soleil d'ioniser la haute atmosphère. La radio fonctionne donc même dans la nuit d'impact, mais de façon perturbée.

| Période | État de l'ionosphère | Effet sur la radio |
|---|---|---|
| **Juillet 1940 – 1941** | Trois effets de l'impact se superposent [estimation] : (1) les **oxydes d'azote** produits par la rentrée des éjectas renforcent la couche D, qui **absorbe les ondes le jour** ; (2) le panache de l'impact océanique a chauffé la haute atmosphère et l'a chargée de **vapeur d'eau** : les électrons de la couche F2 se recombinent plus vite, comme pendant un « orage ionosphérique négatif » prolongé, et les **fréquences utilisables baissent** d'un quart à un tiers ; (3) les **atomes métalliques** des éjectas (sodium, fer, magnésium) nourrissent la **couche E sporadique**, comme le font les étoiles filantes dans la réalité | **Le jour, presque rien en ondes courtes**, sauf par l'onde de sol en ondes moyennes (moins de 500 km) et par l'E sporadique (500 à 2 200 km, sans prévenir). **La nuit, les liaisons passent** : toute la Méditerranée et l'Atlantique proche sont sûrs, et l'on peut entendre, par moments, des stations à 8 000 km |
| **1942 – 1943** | Les oxydes d'azote et les métaux retombent, la thermosphère se refroidit | Retour à la normale. Le jour se rouvre jusqu'à 2 500 km |
| **1944** | **Minimum du cycle solaire 17** (février 1944) [histoire] : soleil calme | Les fréquences hautes se ferment. Mais la nuit, sur 6 à 9 MHz, **les longues distances restent possibles** (§2 bis) |
| **1946 – 1949** | **Maximum du cycle 18** (1947), l'un des plus forts connus à l'époque [histoire] | **« L'été radio »** : les liaisons à 7 000-8 000 km (Martinique, Ceylan, Floride) deviennent **sûres de nuit et possibles de jour** ; Perth et la Nouvelle-Zélande sont entendues par moments |
| **1953 – 1955** | **Minimum du cycle 19** (1954, le soleil le plus calme du siècle) [histoire] | Le monde lointain redevient intermittent, juste au moment où l'île se rouvre |
| **1956 – 1959** | **Maximum du cycle 19** (1957-1958), **le plus fort jamais mesuré** [histoire] | **Le second été radio**, plus fort que le premier. L'îlot, rouvert, peut cette fois **répondre** |

**Une curiosité** : l'**antipode de Cagliari** est dans le Pacifique Sud, à environ 1 200 km de Wellington. Les ondes courtes qui font le tour de la Terre **convergent vers l'antipode**, par tous les chemins à la fois. C'est un phénomène connu des radioamateurs. Le gain est réel mais capricieux : **la Nouvelle-Zélande reste l'une des stations les plus difficiles**, mais certains soirs, sans raison apparente, elle arrive aussi clairement que Dakar.

**Une chance inattendue : le silence.** En 1939, les ondes courtes étaient brouillées par le bruit des réseaux électriques, des moteurs et des tramways. En 1941, ce bruit a presque disparu de la planète. Le récepteur de Cagliari n'entend plus que le bruit naturel : les orages lointains et le bruit galactique. **À puissance égale, on entend plus loin qu'avant la catastrophe** [estimation, ordre de grandeur : une dizaine de décibels gagnés en zone urbaine].

## 2 bis. Le calcul : jusqu'où porte un kilowatt ? [calcul, ordre de grandeur]

### La méthode

Le script `calculs/radio_propagation.py` fait, pour chaque station et chaque période, un **bilan de liaison** simplifié, inspiré des méthodes de l'UIT (recommandations P.533 et P.372) :

1. **L'activité solaire** : le **nombre de taches solaires** annuel réel de 1940 à 1960 [histoire] (série du SIDC) : 68 en 1940, 10 en 1944, 152 en 1947, 4 en 1954, 190 en 1957.
2. **La couche F2** : sa fréquence critique, de jour et de nuit, selon l'activité solaire ; on en tire la **fréquence maximale utilisable** sur chaque bond. Un bond porte au plus à **environ 3 200 km** (couche à 300 km, départ à 3° au-dessus de l'horizon). Gibraltar est à un bond, Dakar à deux, la Martinique à trois, la Nouvelle-Zélande à six.
3. **Les pertes** : la dispersion sur le trajet, l'**absorption de la couche D** le jour (formule de George et Bradley), une perte à chaque réflexion sur la mer et des pertes diverses.
4. **Le bruit** : bruit galactique, orages lointains (bien plus forts la nuit) et bruit humain d'un site très calme.
5. **Le résultat** : le **rapport signal/bruit** en télégraphie Morse, dans un filtre de 500 Hz. Comme le signal varie de ±10 dB d'une minute à l'autre (le fading), il faut environ **15 dB** pour une liaison **sûre**, **5 dB** pour une liaison **intermittente**, et vers 0 dB elle devient **rare**.

**Hypothèses** : l'îlot émet 1 kW avec des antennes en losange ; les grandes stations (Gibraltar, Dakar, la Nouvelle-Zélande) 2 kW ; un navire 1 kW ; une petite garnison 300 à 500 W ; l'Oural 5 kW. « Nuit » veut dire **la meilleure fenêtre de la journée**, quand tout le trajet est dans l'obscurité : pour les très longues distances, elle ne dure qu'une ou deux heures, à l'aube ou au crépuscule selon la saison.

### Les résultats : ce que la physique permet

Verdict **de nuit / de jour** (OK : sûr ; ~ : intermittent ; rare ; – : impossible) :

| Station | Distance | Bonds | Automne 1940 | 1941 | 1944 (minimum) | 1947 (été radio) | 1954 (minimum) | 1957 (second été) |
|---|---|---|---|---|---|---|---|---|
| Minorque | 422 km | 1 | OK / – | OK / ~ | OK / OK | OK / OK | OK / OK | OK / OK |
| Malte | 602 km | 1 | OK / – | OK / rare | OK / OK | OK / OK | OK / OK | OK / OK |
| Gibraltar | 1 316 km | 1 | OK / rare | OK / OK | OK / OK | OK / OK | OK / OK | OK / OK |
| Crète | 1 385 km | 1 | OK / – | OK / OK | OK / OK | OK / OK | OK / OK | OK / OK |
| Casablanca | 1 620 km | 1 | OK / rare | OK / OK | OK / OK | OK / OK | OK / OK | OK / OK |
| Écosse | 2 122 km | 1 | OK / ~ | OK / OK | OK / OK | OK / OK | OK / OK | OK / OK |
| Canaries | 2 573 km | 1 | OK / rare | OK / OK | OK / OK | OK / OK | OK / OK | OK / OK |
| Açores | 3 244 km | 2 | OK / – | OK / – | OK / OK | OK / OK | OK / OK | OK / OK |
| Dakar | 3 761 km | 2 | OK / – | OK / – | OK / OK | OK / OK | OK / OK | OK / OK |
| Oural | 4 172 km | 2 | OK / – | OK / – | OK / OK | OK / OK | OK / OK | OK / OK |
| Freetown | 4 079 km | 2 | OK / – | OK / – | OK / OK | OK / OK | OK / OK | OK / OK |
| Martinique | 7 291 km | 3 | ~ / – | ~ / – | ~ / OK | **OK / OK** | ~ / ~ | **OK / OK** |
| Ceylan | 7 865 km | 3 | ~ / – | ~ / – | ~ / ~ | **OK / OK** | ~ / ~ | **OK** / ~ |
| Maurice | 8 299 km | 3 | rare / – | rare / – | ~ / ~ | ~ / ~ | ~ / ~ | ~ / ~ |
| Floride | 8 385 km | 3 | ~ / – | ~ / – | ~ / ~ | **OK** / ~ | ~ / ~ | **OK** / ~ |
| Perth | 13 518 km | 5 | rare / – | rare / – | rare / – | ~ / – | rare / – | ~ / – |
| Nouvelle-Zélande | 18 600 km | 6 | rare / – | rare / – | rare / – | ~ / – | rare / – | ~ / – |

### Ce que le calcul apprend

- **La Méditerranée et l'Atlantique proche (moins de 4 500 km) sont toujours joignables la nuit**, même dans la nuit d'impact, avec de larges marges (25 à 45 dB). Ce n'est pas la physique qui a coupé la Crète en novembre 1940 ([07](07-le-monde-apres.md) §3) : c'est l'îlot de l'Est qui s'est tu (énergie, lampes, épidémie, choix politique).
- **Le jour, en 1940-41, l'îlot est sourd** au-delà de l'horizon des ondes moyennes. Il faut attendre la nuit pour parler à Gibraltar.
- **Les 7 000 à 8 500 km** (Martinique, Ceylan, Floride, Maurice) sont **possibles de nuit dès 1940**, mais seulement intermittents. L'été radio les rend **sûrs**.
- **Perth et la Nouvelle-Zélande** restent à la limite pendant toute la période : jamais sûres, intermittentes aux maximums solaires, avec des soirs d'exception par l'antipode.
- **En téléphonie**, il faut environ **11 dB de plus** qu'en Morse. La voix passe la nuit jusqu'à environ 4 000 km (Dakar, les Canaries) ; **au-delà, seul le Morse passe**.
- **L'onde de sol en ondes moyennes** (500 kHz) porte de jour à 300-500 km sur mer : la Corse, Bizerte, Minorque, Malte à la limite. C'est la radio des **expéditions de recueil** et des liaisons avec La Maddalena.

**🔧 Ce que cela corrige** : la version précédente de ce chapitre disait que les liaisons de plus de 6 000 km étaient « rares avant 1946 ». **La physique les permet de nuit dès 1940.** Si l'îlot n'entend presque rien de lointain avant 1947, c'est pour d'autres raisons (§7).

## 3. Les stations possibles [canon provisoire]

La survie dépend de la distance à l'impact A ([03](03-impact-pacifique.md) §4) : l'**anneau de moindre flux (65-115°)** est la zone favorable. Il faut aussi une **institution** qui garde un émetteur et de l'énergie : une base navale, un navire, un abri d'État, une mine.

### 3.1 La Méditerranée et ses abords

| Station | Distance de Cagliari | Distance de l'impact A | Qui émet | 1940-41 | 1942-45 | 1946-50 |
|---|---|---|---|---|---|---|
| **Bizerte** (Tunisie) | **227 km** | 93,8° | Base navale française, arsenal de Ferryville | ✅ Fort jusqu'à l'automne, puis ❌ (§4) | ❌ | ❌ |
| **Minorque** (Mahón) | 422 km | 91,5° | Poche de la Marine espagnole ([06](06-mers-el-kebir.md) §6) | ✅ | 🟡 Intermittent | 🟡 |
| **Malte** | 602 km | 94,8° | Garnison britannique dans les galeries | ✅ jusqu'à l'hiver | ❌ L'île meurt de faim ([10](10-choix-du-refuge.md)) | ❌ |
| **Gibraltar** | 1 316 km | 95,0° | La garnison restée dans le Rocher | ✅ Liaison quotidienne | ✅ | ✅ Avant-poste et partenaire [canon] ([07](07-le-monde-apres.md) §2 bis) |
| **Crète** (îlot de l'Est) | 1 385 km | 93,6° | Cunningham et Godfroy | ✅ jusqu'en octobre 1940 | ❌ **Silence [canon]** | ❌ |
| **Casablanca** | 1 620 km | 97,4° | Le cuirassé inachevé ***Jean Bart***, réfugié là depuis juin 1940 [histoire], et la base navale | ✅ | 🟡 | 🟡 La Morìa atteint le Maroc en 1945 |
| **Alexandrie** et delta du Nil | 2 084 km | 96,3° | Restes de la base, survivants du delta | ✅ Appels de détresse | 🟡 Appels sur la peste en 1943, puis ❌ | ❌ |
| **Sébastopol** | 2 098 km | 82,7° | Flotte soviétique de la mer Noire. La mer Noire est un réservoir thermique, comme la Méditerranée | 🟡 En russe | 🟡 | ❌ après la Morìa (1944) |
| **Chypre, Haïfa** | 2 200 – 2 400 km | 91-93° | Garnisons britanniques | ✅ | 🟡 Appels sur la peste en 1943, puis ❌ | ❌ |

### 3.2 L'Atlantique

| Station | Distance de Cagliari | Distance de l'impact A | Qui émet | 1940-41 | 1942-45 | 1946-50 |
|---|---|---|---|---|---|---|
| **Écosse** (Clyde, Scapa Flow) | 2 100 – 2 350 km | 72-75° | Home Fleet, administration britannique repliée, mines de charbon | 🟡 Intermittent ([07](07-le-monde-apres.md)) | 🟡 Très affaibli par le froid | 🟡 |
| **Canaries** | 2 573 km | 101,8° | Garnison espagnole, port de Las Palmas | 🟡 | 🟡 | ✅ |
| **Açores** | 3 013 km | 90,3° | Garnison portugaise, **stations des câbles transatlantiques** de Horta | 🟡 | 🟡 | ✅ |
| **Islande** | 3 431 km | 65,7° | Troupes britanniques d'occupation (depuis mai 1940) [histoire] ; chaleur géothermique | ❌ Bord de la zone d'incendies | ❌ | 🟡 Possible petite poche |
| **Dakar** | 3 761 km | 114,5° | **Le cuirassé *Richelieu*, réfugié là depuis juin 1940** [histoire], et la base de l'Afrique-Occidentale française | ✅ | ✅ | ✅ |
| **Freetown** | 4 079 km | 121,4° | Base britannique des convois | 🟡 | 🟡 | ✅ |
| **Martinique** | 7 291 km | 95,9° | Le porte-avions ***Béarn*** et le croiseur ***Émile Bertin***, arrivés en juin 1940 [histoire], et l'or de la Banque de France | 🟡 Rare | 🟡 Possible de nuit, mais personne ne connaît les heures d'écoute de l'autre (§7) | ✅ **L'été radio** |
| **Floride** (Key West, golfe du Mexique) | 8 385 km | 75,9° | Bases de la US Navy, radioamateurs américains (encore actifs en 1940) | 🟡 | 🟡 Rare : les stations se taisent pour économiser l'énergie | ✅ |
| **Rio de Janeiro** | 8 787 km | 136,3° | Marine brésilienne | ❌ Zone d'incendies | ❌ | 🟡 |
| **Le Cap** (Simonstown) | 8 219 km | **161,0°** | — | ❌ **Focalisation antipodale** : tout a brûlé | ❌ | ❌ |

### 3.3 L'océan Indien, l'Asie et l'Océanie

| Station | Distance de Cagliari | Distance de l'impact A | Qui émet | 1940-41 | 1942-45 | 1946-50 |
|---|---|---|---|---|---|---|
| **Aden** | 4 587 km | 107,7° | Base britannique | 🟡 | ❌ La Morìa (1943) | ❌ |
| **Bombay** | 6 452 km | 87,7° | Base de la Royal Indian Navy | 🟡 | ❌ La Morìa (1943-44) | 🟡 |
| **Ceylan** (Trincomalee, Colombo) | 7 869 km | 90,4° | Base de l'East Indies Fleet | 🟡 | 🟡 | ✅ |
| **Mombasa, Diego-Suarez, Maurice** | 5 700 – 8 300 km | 125-127° | Bases britannique et française, garnisons | 🟡 | 🟡 | ✅ |
| **Saïgon, Singapour, Surabaya** | 9 900 – 11 700 km | 72-82° | Marines française, britannique et néerlandaise | ❌ | ❌ | 🟡 La Morìa y passe en 1944-45 |
| **Perth** (Fremantle) | 13 518 km | 99,8° | Australie occidentale, abritée du tsunami du Pacifique | ❌ | ❌ | ✅ |
| **Nouvelle-Zélande** | 18 779 km | 90,1° | Société organisée, marine, hydroélectricité ([07](07-le-monde-apres.md)) | ❌ | 🟡 Rare, par l'antipode | ✅ **Par l'antipode** |
| **Oural** (Sverdlovsk) | 4 172 km | 63,9° | Abris de l'appareil d'État soviétique | 🟡 Émissions codées | 🟡 | 🟡 Méfiant |

**Légende** : ✅ contact probable ; 🟡 contact possible ou intermittent ; ❌ silence. Ces colonnes combinent la **physique** (§2 bis) et le **sort de chaque station** (qui émet encore, [canon provisoire]). Un ❌ signifie presque toujours que la station n'existe plus, pas que l'onde ne passe pas.

## 4. Bizerte : l'effondrement [canon]

**Décision de l'auteur** : Bizerte **s'effondre**.

**Bizerte est à 227 km de Cagliari**, plus près que tout autre port. En juillet 1940, c'est une grande base de la Marine française, avec l'arsenal de Ferryville, des torpilleurs et des sous-marins [histoire]. Elle est dans l'anneau de moindre flux (93,8°) et **survit à la nuit de feu**.

**Pourquoi elle sombre** [canon provisoire] :
- **Les réfugiés** : Tunis (plus de 200 000 habitants) et les campagnes du nord de la Tunisie affluent vers la base, ses magasins et ses navires dès juillet 1940. Contrairement à Mers el-Kébir, Bizerte n'a pas de flotte assez nombreuse pour tenir la foule à distance, et pas de plan de départ.
- **Les hésitations** : son commandement refuse d'abord de rallier le Conseil des Amiraux, puis veut attendre des ordres de Vichy qui ne viendront jamais. Quand il se décide, il est trop tard.
- **L'hiver 1940-41** : émeutes de la faim, assaut contre l'arsenal de Ferryville, **incendie des dépôts de mazout**, mutineries. Les dernières émissions de Bizerte, en décembre 1940, sont des appels au secours.
- **Les rescapés** [canon : principe ; provisoire : détail] : environ **1 500 personnes** gagnent la Sardaigne, à 227 km, en trois vagues. Elles débarquent à **Sant'Antioco** et à **Carloforte**, les ports les plus proches.

  | Vague | Qui | Comment |
  |---|---|---|
  | **Octobre – novembre 1940** | Les officiers et les équipages qui voulaient rallier le Conseil, avec leurs familles (~600 personnes) | Un torpilleur, un aviso et deux sous-marins appareillent sans ordre, de nuit, avant que la base ne soit submergée |
  | **Décembre 1940** | Marins et **ouvriers de l'arsenal de Ferryville** fuyant les émeutes (~700 personnes) | Remorqueurs, chalutiers, vedettes, tout ce qui flotte |
  | **1941** | Petits groupes (~200 personnes) | Barques de pêche et voiliers, souvent à la dérive |

- **Leur poids dans l'îlot** : les **ouvriers de Ferryville** (chaudronniers, mécaniciens, électriciens, soudeurs) sont un apport précieux. Ce sont eux qui, avec l'arsenal de Cagliari, convertiront les navires au charbon ([15](15-energie.md) §5). Les « gens de Bizerte » forment un bord à part entière.

**Conséquences** :
- La côte tunisienne reste peuplée de **poches de survivants désorganisées**. C'est l'une d'elles qui transmet la Morìa à Carloforte en 1945 ([14](14-epidemie.md) §5.3).
- **Bizerte devient une leçon** dans la mémoire de l'îlot : une base intacte, à une nuit de mer, perdue faute de discipline et de décision. Elle justifie la société de bord ([13](13-societe-de-bord.md)).
- **Les ruines de Ferryville** (outillage, pièces, cales sèches) sont un objectif d'expédition après la réouverture de 1949. Les dépôts de mazout ayant brûlé, la courbe du mazout ([15](15-energie.md) §3) ne change pas.

## 5. Ce que la Sardaigne entend : la chronologie de l'écoute [canon provisoire]

| Période | Ce qu'on entend à Cagliari |
|---|---|
| **2 – 31 juillet 1940** | **Un vacarme de détresse** : des centaines d'appels venus de toute l'Europe et de la Méditerranée. Gibraltar, Mers el-Kébir, Alger, Bizerte, Toulon, Malte, Alexandrie. Quelques messages de Londres, puis d'Écosse. Rome et Berlin se taisent |
| **Août – octobre 1940** | Les voix s'éteignent une à une. Contacts réguliers avec la Crète, Gibraltar, Dakar et Casablanca. L'ionosphère brouille tout le jour |
| **Novembre 1940** | **Dernier message de la Crète** [canon] |
| **Décembre 1940** | **Derniers appels au secours de Bizerte** [canon] |
| **1941 – 1942** | Une poignée de stations fidèles : Gibraltar, Dakar, Casablanca, Minorque, l'Écosse par intermittence. On s'échange des nouvelles du froid, des stocks, des épidémies |
| **1943** | **Des appels du Levant et d'Égypte parlent d'une « peste noire »** ([14](14-epidemie.md) §5.1). Ils se taisent dans l'année |
| **1944 – 1946** | L'Île fermée **écoute en silence**. Le minimum solaire réduit la portée. Le monde semble se réduire à la Méditerranée occidentale et à l'Afrique de l'Ouest |
| **1947 – 1949 : l'été radio** | **Le monde réapparaît.** On entend la Martinique, la Floride, Ceylan, Maurice, Perth, et même la Nouvelle-Zélande par l'antipode. Des voix en anglais, en français, en espagnol, en portugais. L'îlot découvre qu'il n'est pas seul, mais aussi **combien le monde est vide** |
| **Juillet 1950** | *(prov.)* Grâce au pli rapporté par l'expédition d'Albanie, Cagliari **écoute la Crète aux heures de vacation qu'elle a données** ([18](18-expedition-albanie.md) §7.5). Date du premier échange [à décider] |
| **1950 – 1952** | Avec la réouverture de l'île, l'îlot répond de nouveau. Les premiers échanges réguliers s'organisent avec Dakar, Gibraltar, les Canaries et la Martinique, à **heures fixes** (§7) |
| **1953 – 1955** | *(prov.)* **Le creux** : minimum solaire de 1954. Les voix lointaines faiblissent ; les liaisons méditerranéennes et atlantiques restent sûres la nuit |
| **1956 – 1959 : le second été radio** | *(prov.)* Le cycle solaire le plus fort jamais mesuré. L'îlot, rouvert, **répond** cette fois : vacations régulières avec la Martinique, Ceylan, peut-être la Floride ; contacts occasionnels avec Perth et la Nouvelle-Zélande. C'est la première fois depuis 1940 que l'îlot **parle** au monde lointain, au lieu de seulement l'écouter |

## 6. Les partenaires les plus probables

1. **Gibraltar** : proche, britannique, lié à la Force H. C'est le premier interlocuteur : **avant-poste et partenaire** de l'îlot [canon].
2. **Dakar** : le *Richelieu*, la Marine française, une mer chaude, et **épargné par la Morìa**. C'est la voix la plus stable de toute la période. Un allié naturel pour les années 1950.
3. **Casablanca** : le *Jean Bart*, à mi-chemin de Dakar.
4. **La Martinique** : le *Béarn*, l'*Émile Bertin* et l'or de la Banque de France. Lointaine, mais épargnée par la peste.
5. **La Nouvelle-Zélande** : la plus lointaine, mais organisée, et parfois étonnamment claire grâce à l'antipode.

## 7. Ce qui limite vraiment le contact : les hommes, pas les ondes [estimation, canon provisoire]

Le calcul (§2 bis) montre que la physique est généreuse. Ce qui rend le contact difficile, ce sont quatre contraintes très concrètes :

| Contrainte | Pourquoi | Conséquence |
|---|---|---|
| **Le rendez-vous** | Pour se parler à 8 000 km, il faut écouter **la bonne fréquence, à la bonne heure, dans la bonne fenêtre** de propagation, qui ne dure parfois qu'une heure. Sans horaire convenu, deux stations peuvent se manquer pendant des années | Les contacts lointains naissent par hasard, puis deviennent réguliers dès qu'on convient de **vacations** (heures fixes et fréquences). C'est ce que fait l'îlot de l'Est avec son pli de 1950 ([18](18-expedition-albanie.md) §7.5) |
| **L'énergie** | Un émetteur d'un kilowatt consomme plusieurs kilowatts. Une station qui rationne son charbon ou son mazout n'émet que quelques minutes par jour | La plupart des stations lointaines émettent peu, et à heures fixes. Celles qui disposent d'hydroélectricité (la Nouvelle-Zélande) ou d'un navire (Dakar, la Martinique) sont les plus constantes |
| **Les lampes** | Les tubes électroniques s'usent (quelques milliers d'heures) et ne se fabriquent plus | Les stations se taisent une à une dans les années 1950, faute de lampes, sauf celles qui ont de gros stocks (les arsenaux, les navires). L'îlot garde ses lampes sous clé et n'émet que l'essentiel |
| **Les opérateurs et les langues** | Le Morse, les **codes Q** et les abréviations internationales permettent de se comprendre sans langue commune | Une station sans opérateur formé est muette. L'îlot forme ses opérateurs dans le corps du Pont (spécialité transmissions, [22](22-organisation-militaire.md) §5) |

**Le choix de l'îlot de 1944 à 1949** : l'Île fermée **écoute mais ne répond presque plus** (§1). Elle garde donc ses lampes, mais elle laisse passer l'été radio sans établir de vacations : quand elle se met à répondre, en 1950, le maximum solaire s'achève. **Il faut attendre le second été radio (1956-1959) pour des liaisons lointaines régulières.**

### Le réseau de l'îlot

| Liaison | Distance | Moyen | Fiabilité |
|---|---|---|---|
| Cagliari – La Maddalena, l'Asinara, les bords du nord | 50 à 250 km | Ondes moyennes (onde de sol), jour et nuit | Sûre |
| Cagliari – Malte, Sazan | 600 à 900 km | Ondes courtes, un bond ; la nuit en 1940-41, à toute heure ensuite | Sûre |
| Cagliari – Gibraltar | 1 316 km | Ondes courtes, vacation quotidienne | Sûre (la nuit seulement en 1940-41) |
| Cagliari – les expéditions de recueil (Corse, côte italienne) | 100 à 350 km | Ondes moyennes et ondes courtes | Sûre |
| Cagliari – l'expédition d'Albanie (Vlorë) | ~900 km | Ondes courtes, un bond | Sûre |

## 8. Questions ouvertes

1. ❓ **Les vacations lointaines** : avec quelles stations l'îlot établit-il des heures fixes pendant le second été radio (1956-1959) ? Qui répond le premier ?
2. ✅ **La station à terre** : émetteur à Molentargius – Poetto, récepteur à Elmas (1942), vigies à Guardia Vecchia (1940), au Serpeddì (1944) et au Limbara (vers 1958) (§1 bis).
3. ❓ **Les lampes** : l'îlot a-t-il un stock suffisant pour tenir jusqu'aux années 1960, ou doit-il apprendre à refaire des tubes à vide (verrerie, vide, filaments) ?
4. 🔎 **À vérifier** : puissance et bandes des émetteurs de bord des grands bâtiments français, britanniques et italiens en 1940 ; récepteurs de trafic en service ; durée de vie des lampes d'émission.
5. 🔎 **À vérifier** : les hypothèses propres à l'uchronie (absorption par les oxydes d'azote, baisse de la couche F2 après un impact océanique, couche E sporadique) ; ordres de grandeur dans la littérature sur les impacts et sur les orages ionosphériques.
