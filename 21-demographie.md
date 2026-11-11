# 21 — La population de l'îlot : démographie et métiers (1940-1960)

> **Statut** : les totaux de 1946, 1950 et 1960 sont au **[canon]** ([11](11-ilot-de-civilisation.md) §2). **Décisions de l'auteur** : immigration féminine organisée (A2, §4.4), grands travaux puis expansion vers le nord (B1 puis B2, §5.6), natalisme de bord et protection des mères (C3, §4.6), expéditions de recueil (§4.5). Les chiffres (âges, sexes, naissances, métiers) restent **[canon provisoire]**, tirés du modèle [calculs/demographie_ilot.py](calculs/demographie_ilot.py) (sortie brute : [annexes/resultats_demographie.txt](annexes/resultats_demographie.txt)). Décisions et questions suivantes : §8.

## 1. La méthode [estimation]

- **Point de départ : 1946**, l'année où la population est la plus basse et la mieux connue (le canon donne la composition par origine, [11](11-ilot-de-civilisation.md) §2). Chaque groupe d'origine reçoit une structure par âge et par sexe plausible.
- **Projection année par année jusqu'en 1960**, par âge simple et par sexe :
  - **mortalité** d'un pays méditerranéen pauvre d'avant-guerre (la Sardaigne de 1936 avait une espérance de vie d'environ 50 ans), sans antibiotiques mais avec la visite quotidienne et la ration garantie. La mortalité infantile passe de 130 ‰ en 1946 à 80 ‰ en 1960 ;
  - **fécondité naturelle** des femmes mariées (barème de Coale et Trussell), réduite d'environ 30 % par l'allaitement long et les séquelles de la famine. Presque toutes les femmes se marient, puisque les hommes sont en surnombre ;
  - **immigration** : quelques centaines par an de 1949 à 1951, puis environ **850 par an** à partir de la patente de 1952 ([14](14-epidemie.md) §5.6), dont **60 % de femmes** (§4.4).
- **Avant 1946**, on ne projette pas : les années 1940-1945 sont trop chaotiques. On les décrit par les ordres de grandeur du canon.

## 2. L'évolution de 1940 à 1960

### 2.1 La courbe [canon pour les totaux ; provisoire pour le détail]

| Date | Population | Hommes / 100 femmes | Ce qui se passe |
|---|---|---|---|
| Juillet 1940 | ~21 000 arrivants + ~650 000 Sardes | Arrivants : ~450 | Les flottes arrivent. Les Sardes meurent par dizaines de milliers |
| Mars 1941 | ~205 000 | — | Le premier hiver |
| Fin 1941 | ~95 000 | — | L'année sans soleil, le typhus |
| 1943 | ~54 000 | ~175 | Première vraie récolte. Plus aucune naissance depuis deux ans |
| **1946** | **~49 000** | **~172** | Point bas. La Morìa ([14](14-epidemie.md)) |
| **1950** | **~54 000** (canon : ~55 000) | ~162 | Le « grand berceau » : 2 400 à 2 500 naissances par an |
| 1955 | ~65 000 | ~144 | Les premières dotées de la patente (§4.4) |
| **1960** | **~77 000** | ~132 | Plus d'un habitant sur trois a moins de 15 ans |

### 2.2 Naissances, décès, immigration (1946-1960) [canon provisoire]

| Année | Naissances | Décès | Immigrés | Natalité (‰) | Mortalité (‰) |
|---|---|---|---|---|---|
| 1946 | ~1 400 | ~1 100 | — | 29 | 22 (dont la Morìa) |
| 1947 | ~2 000 | ~900 | — | 41 | 18 |
| 1948 | ~2 350 | ~830 | — | 47 | 16 |
| 1950 | ~2 500 | ~920 | ~350 | 46 | 17 |
| 1952 | ~2 500 | ~960 | ~850 | 43 | 17 |
| 1955 | ~2 550 | ~990 | ~850 | 40 | 15 |
| 1959 | ~2 650 | ~1 040 | ~850 | 35 | 14 |

**Ce que montrent ces chiffres** :
- **Le « grand berceau » de 1947-1950** : une natalité de 45 ‰, comparable à celle des pays les plus féconds de 1940. C'est le baby-boom de l'après-catastrophe, comme après chaque grande famine ou épidémie [histoire : la reprise des naissances après la peste noire et après la famine irlandaise est bien documentée].
- **Le plafond des naissances** : elles plafonnent vers **2 500 par an**, parce que le nombre de **femmes en âge d'avoir des enfants** ne bouge presque pas (environ 11 000 à 12 500 de 1946 à 1960). **Ce sont les femmes, et non les hommes ou les vivres, qui limitent la croissance de l'îlot.**
- **L'accroissement naturel** est d'environ 1 500 personnes par an (près de 3 % par an). Pour atteindre 77 000 habitants en 1960, il faut **en plus environ 850 immigrés par an** à partir de 1952. Parce que l'îlot choisit surtout des femmes (§4.4), chaque immigrée **fait aussi monter les naissances** : il en faut moins que si l'on admettait autant d'hommes que de femmes.

## 3. La pyramide des âges

### 3.1 En 1946 : une pyramide en forme de toupie [canon provisoire]

| Âge | Hommes | Femmes | H/100 F | % |
|---|---|---|---|---|
| 0-4 | 1 430 | 1 370 | 104 | 5,7 |
| 5-9 | 1 000 | 960 | 104 | 4,0 |
| 10-14 | 1 100 | 1 050 | 104 | 4,4 |
| 15-19 | 1 210 | 1 650 | 73 | 5,8 |
| 20-24 | 3 440 | 2 410 | 143 | 11,9 |
| **25-29** | **6 820** | 2 480 | **275** | **19,0** |
| **30-34** | **5 830** | 2 240 | **260** | **16,5** |
| 35-39 | 3 850 | 1 800 | 213 | 11,5 |
| 40-44 | 2 530 | 1 370 | 185 | 7,9 |
| 45-49 | 1 790 | 1 050 | 171 | 5,8 |
| 50-54 | 1 240 | 760 | 164 | 4,1 |
| 55-64 | 700 | 720 | 98 | 2,9 |
| 65 + | 100 | 130 | 72 | 0,5 |
| **Total** | **~31 000** | **~18 000** | **172** | 100 |

**Lecture** :
- **Un ventre d'hommes de 25 à 40 ans** : ce sont les marins de 1940, qui avaient alors 19 à 34 ans. À eux seuls, les 25-34 ans font plus d'un tiers de l'îlot.
- **Presque pas de vieux** : moins de 1 % de plus de 65 ans (contre environ 8 % en Sardaigne en 1936). Les vieillards sont morts les premiers en 1940-41.
- **Les « classes creuses » de la Nuit** : les enfants nés de 1941 à 1943 sont presque absents (aménorrhée de famine, mortalité des nourrissons). Ils seront une génération rare, et ils le sauront : on les appelle **« les enfants de la Nuit »** [canon provisoire].
- **Les 15-19 ans** sont la seule tranche où les filles sont plus nombreuses : les garçons sardes de cet âge ont été plus nombreux à mourir dans la violence de 1940-41 (vols de vivres, bandes, réquisitions).
- **Un rapport de dépendance très faible** : 17 inactifs (enfants et vieillards) pour 100 personnes de 15 à 64 ans. L'îlot de 1946 est une **société de travailleurs**, ce qui l'aide à survivre.

### 3.2 En 1950 : le grand berceau [canon provisoire]

| Âge | Hommes | Femmes | H/100 F | % |
|---|---|---|---|---|
| **0-4** | **4 010** | **3 820** | 105 | **14,5** |
| 5-9 | 920 | 880 | 104 | 3,4 |
| 10-14 | 1 100 | 1 060 | 104 | 4,0 |
| 15-24 | 2 700 | 2 900 | 93 | 10,4 |
| 25-34 | 10 350 | 4 690 | 221 | 27,9 |
| 35-44 | 8 670 | 3 710 | 234 | 23,1 |
| 45-54 | 3 870 | 2 190 | 177 | 11,3 |
| 55-64 | 1 400 | 1 010 | 139 | 4,4 |
| 65 + | 220 | 310 | 73 | 1,0 |
| **Total** | **~33 250** | **~20 600** | **162** | 100 |

Un enfant de moins de cinq ans pour sept habitants : **les crèches et les maternités deviennent un besoin de premier rang** (§5). Au-dessus, le creux des enfants de la Nuit (5-9 ans) est très visible.

### 3.3 En 1960 : une pyramide qui se retourne [canon provisoire]

| Âge | Hommes | Femmes | H/100 F | % |
|---|---|---|---|---|
| 0-14 | 14 710 | 14 200 | 104 | **37** |
| 15-19 (les enfants de la Nuit) | 1 100 | 1 180 | 93 | 3,0 |
| 20-34 (dont les dotées) | 5 240 | 6 220 | 84 | 14,9 |
| 35-49 (les marins de 1940) | 15 170 | 7 240 | 210 | 29,1 |
| 50-64 | 6 490 | 3 460 | 188 | 12,9 |
| 65 + | 1 190 | 920 | 129 | 2,7 |
| **Total** | **~43 900** | **~33 200** | **132** | 100 |

- **Deux îlots dans l'îlot** : au-dessous de 35 ans, une population **jeune, où les femmes sont même un peu plus nombreuses** (l'effet des dotées, §4.4) ; au-dessus, la **génération des fondateurs**, masculine aux deux tiers.
- **Le rapport de dépendance monte à 67 pour 100** : l'îlot doit maintenant nourrir, vêtir et instruire 29 000 enfants. L'école devient le premier poste de dépense après les vivres et le charbon.
- **Le goulot des années 1960** : quand les enfants de la Nuit arrivent à l'âge de travailler et de se marier (1956-1963), ils sont trois fois moins nombreux que les générations qui les encadrent. C'est aussi le creux du concours de l'École navale ([13](13-societe-de-bord.md) §4 quater). Peu d'apprentis, peu de mariages, peu de naissances vers 1965 : **un écho du creux de 1941-43** [estimation].

## 4. Hommes et femmes : le problème central

### 4.1 Les chiffres [canon provisoire]

| | 1946 | 1950 | 1955 | 1960 |
|---|---|---|---|---|
| Hommes pour 100 femmes (tous âges) | 172 | 161 | 144 | 132 |
| Hommes pour 100 femmes (20-39 ans) | 223 | 201 | 156 | 104 |
| Femmes de 15 à 44 ans | ~11 950 | ~11 300 | ~12 000 | ~12 550 |
| **Hommes de 18 à 44 ans sans épouse possible** | **~12 000** | **~11 000** | **~8 500** | **~5 000** |

*Avec l'immigration féminine (§4.4). Sans elle, il resterait environ 6 000 hommes sans épouse possible en 1960.*

**Note** : le modèle retient **82 % d'hommes parmi les arrivants** ([11](11-ilot-de-civilisation.md) §1), mais environ 98 % parmi les seuls marins. Le chapitre 13 a été aligné sur ce chiffre.

### 4.2 D'où vient le déséquilibre

- **Les flottes** : environ 21 000 hommes pour quelques centaines de femmes (infirmières, Wrens de Gibraltar).
- **Les militaires italiens** : environ 3 300 survivants, tous des hommes.
- **Chez les civils sardes, c'est l'inverse** : environ 15 000 femmes pour 11 000 hommes en 1946. La famine tue davantage les hommes (c'est un fait observé dans presque toutes les grandes famines [histoire]), et les hommes sardes sont morts en plus grand nombre dans les combats pour les vivres de 1940-41 ([11](11-ilot-de-civilisation.md) §7).
- **Résultat** : presque toutes les femmes de l'îlot sont mariées, et **une femme sarde sur deux épouse un marin des flottes** [estimation]. Pourtant, en 1946, environ **12 000 hommes jeunes** n'ont aucune perspective de mariage.

### 4.3 Les précédents historiques [histoire]

| Société | Situation | Ce qui s'est passé |
|---|---|---|
| **La Nouvelle-France** (1663-1673) | Une colonie de soldats, de trappeurs et d'engagés, très majoritairement masculine | Le roi y envoie environ 800 **« filles du Roi »**, dotées par l'État. Presque toutes se marient dans l'année. Elles sont les ancêtres d'une grande partie des Québécois |
| **La Nouvelle-Galles du Sud** (1788-1840) | Colonie pénitentiaire, avec plusieurs hommes pour une femme [ordre de grandeur, à vérifier] | Violence, prostitution, alcoolisme. Le gouvernement finance ensuite l'**immigration de jeunes femmes** libres |
| **Pitcairn** (1790-1800) | 9 mutins, 6 Tahitiens, 12 Tahitiennes | Les meurtres liés aux femmes détruisent presque tous les hommes en dix ans ([13](13-societe-de-bord.md) §1) |
| **La France après 1918** | Le cas inverse : environ 1,4 million d'hommes tués | Une génération de femmes seules, les « veuves blanches » |

**La leçon** : un déséquilibre de cette ampleur est une **menace pour l'ordre**. Les sociétés qui l'ont traversé l'ont fait par la **discipline** et par une **immigration féminine organisée**.

### 4.4 Ce que fait l'îlot : la loi de bord et les dotées [canon : principe ; provisoire : détail]

**Décision de l'auteur** : une **immigration féminine organisée** après la patente de 1952, à la manière des filles du Roi (option A2).

**Jusqu'en 1952 : la loi de bord** [canon provisoire]
- **La loi de bord tient les hommes** : les rixes pour une femme relèvent du conseil de discipline ; la violence contre une femme est jugée au conseil de guerre ([13](13-societe-de-bord.md) §5).
- **Le mariage est civil et enregistré par l'Inscription**. Il exige le **consentement de la femme**, recueilli par l'officier d'Inscription hors de la présence de sa famille ; pour les inscrits, il faut aussi l'autorisation du commandant de bord, comme pour les marins de 1940. Les aumôniers le bénissent.
- **Les célibataires** vivent à bord ou dans les postes d'équipage, comme dans la marine. Les bords à flot, les mines, la garde et les avant-postes recrutent surtout parmi eux.

**À partir de 1952 : les dotées** [canon provisoire]
- **Le principe** : parmi les étrangers admis après la quarantaine de l'Asinara, **la priorité va aux femmes et aux familles**, comme elle va aux ingénieurs et aux savants ([19](19-savoir-et-medecine.md)). Le Conseil fixe un objectif d'**environ 60 % de femmes** parmi les adultes admis.
- **La dot de l'Inscription** : une femme admise reçoit un logement, un **trousseau du bord** (toile, laine, ustensiles), la ration pleine et, à son mariage, **une terre** dans un bord de terre. On les appelle **« les dotées »**.
- **La liberté de choix** : une dotée est inscrite comme tout le monde. **Elle n'est pas tenue de se marier**, ni d'épouser un homme désigné. Les règles de la fréquentation (bals du dimanche, visites sous l'œil de la Maistrance) sont celles des bords, pas celles d'un marché. C'est ce qui distingue l'îlot des chefferies, où l'on razzie des femmes ([07](07-le-monde-apres.md) §1 bis).
- **D'où viennent-elles** : de l'intérieur de la Sardaigne (Barbagia, Gallura), de Corse, des côtes d'Afrique du Nord, de Malte et de Gozo, puis de la côte italienne. Le bilan chiffré, par origine et par voie d'entrée, est au §4.7.
- **Ce que cela change** : le déséquilibre des 20-39 ans disparaît vers 1960 (104 hommes pour 100 femmes) ; les naissances dépassent 2 600 par an à la fin des années 1950.
- **Le prix** [canon provisoire] : les dotées arrivent dans une société où presque tous les hommes de 35 à 50 ans sont des marins des flottes, et dans une langue qu'elles ne parlent pas. Beaucoup épousent des hommes de quinze ans plus âgés qu'elles. Les **veuves** de la génération des fondateurs seront nombreuses dans les années 1970.

### 4.5 Les expéditions de recueil [canon : principe ; provisoire : détail]

**Décision de l'auteur** : des expéditions sont organisées vers la **Corse**, ou même vers la **côte italienne**, pour recueillir d'éventuels rescapés, **à la condition que le flux naturel des nouveaux arrivants ne suffise pas**.

**La règle du flux** [canon provisoire] : chaque printemps, le Conseil des Amiraux compare les admissions de l'année écoulée à l'objectif (environ **850 admis par an, dont 60 % de femmes**, §4.4). **L'objectif est aussi un plafond** : la quarantaine de l'Asinara ne peut recevoir qu'une centaine de personnes à la fois, soit environ 850 par an avec des séjours de quarante jours. Ceux qui arrivent en surnombre attendent leur tour, comme les Corses du quota de 1940 ([11](11-ilot-de-civilisation.md) §1 bis). Une expédition de recueil n'est décidée que si le flux naturel tombe **au-dessous des deux tiers de l'objectif** (moins d'environ 550 admis, ou moins de la moitié de femmes). Le recueil coûte du charbon, des vivres et des hommes, et chaque contact avec l'extérieur est un risque de peste : on ne va chercher que ce qui ne vient pas seul.

**Le flux naturel et le déclenchement** [estimation, canon provisoire] :

| Période | Flux naturel | Pourquoi | Expéditions |
|---|---|---|---|
| **1949-1951** | ~350 par an | Avant la patente, l'île n'admet presque pas d'étrangers ([14](14-epidemie.md) §5.6) : ce sont surtout des **Sardes de l'intérieur** qui descendent, et quelques Maltais | Aucune |
| **1952-1954** | ~900 par an, **850 admis** | L'attente accumulée depuis la fermeture de 1944 : Corses massés à Bonifacio, Gozitains, filles de la Barbagia. Le petit surplus attend son tour et entre en 1955, avec le flux de cette année-là | Aucune : le flux suffit |
| **1955-1957** | ~550 par an | Les sources proches s'épuisent : ceux qui pouvaient traverser seuls l'ont fait | **Déclenchement en 1955** : ~300 recueillis par an |
| **1958-1959** | ~500 par an | Les premiers pactes de la Barbagia ([13](13-societe-de-bord.md) §6 bis) et quelques familles de la Gallura, à mesure que l'expansion avance (§5.6) | ~350 recueillis par an |

**Les destinations** [canon provisoire] :

| Destination | Distance depuis La Maddalena [ordre de grandeur] | Pourquoi | Première expédition |
|---|---|---|---|
| **Côte orientale de la Corse** (Porto-Vecchio, plaine d'Aléria, Bastia) | 50 à 170 km | Les villages côtiers hors des grandes chefferies de l'intérieur ; des parents des Corses de l'îlot | **1955** |
| **Archipel toscan** (île d'Elbe, Giglio, Capraia) | 200 à 250 km | Des îles, donc des refuges comme Gozo ; les mines de fer de l'Elbe ont pu servir d'abri en 1940 | **1957** |
| **Côte tyrrhénienne** (Maremme, Argentario, Civitavecchia, La Spezia, Livourne) | 250 à 350 km | Les familles des marins italiens de l'îlot ; les bases de la Regia Marina | 1958-1960, avec prudence |

**Comment se passe une expédition** [canon provisoire] :
- **Le départ** : La Maddalena, la base la plus proche de la Corse et de l'Italie. Un aviso charbonnier (la *Tornade* ou le *Typhon*, [29](29-flotte-des-annees-1950.md)), un cargo pour les passagers, une section de fusiliers marins, deux médecins, un aumônier et des **interprètes** (des Corses et des Italiens de l'îlot).
- **Le contact** : l'expédition annonce sa venue (feux, pavillon, porte-voix), mouille au large et reçoit les candidats sur une plage ou à un ponton. **On n'emmène que des volontaires.** On n'enlève personne, on ne force aucun village.
- **Le tri** : la visite médicale à bord. Tout cas de fièvre fait renvoyer le bateau à l'Asinara.
- **Le retour** : quarantaine de quarante jours à l'**Asinara** ([14](14-epidemie.md) §5.6), puis l'essai et l'inscription, comme pour tous les étrangers admis.
- **Le bilan** : chaque expédition ramène **150 à 400 personnes**. De 1955 à 1959, les expéditions apportent environ **1 600 personnes** (900 de Corse, 700 de la côte italienne), soit plus du tiers des admissions de la période. Le total de 1960 (~77 000) ne change pas : ce que le flux naturel ne donne plus, les expéditions le complètent.

**Ce que cela change** :
- **La Corse** cesse d'être seulement une blessure ([11](11-ilot-de-civilisation.md) §1 bis) : les Corses de l'îlot vont chercher leurs parents.
- **Les marins italiens** de l'îlot retrouvent, parfois, la trace de leurs familles. C'est un lien nouveau entre l'îlot et la péninsule.
- **Les chefferies** voient arriver les navires de l'îlot. Certaines laissent partir leurs gens, d'autres les retiennent. C'est le premier contact suivi entre l'îlot et le monde des chefferies ([07](07-le-monde-apres.md) §1 bis).

### 4.6 La politique des naissances : natalisme de bord et protection des mères [canon : principe ; provisoire : détail]

**Décision de l'auteur** : un natalisme de bord, plus une protection des mères (option C3).

| Mesure | Contenu |
|---|---|
| **Ration de mère** | La ration d'enfant et de mère ([13](13-societe-de-bord.md) §4) est due **dès la déclaration de grossesse et jusqu'au sevrage**, vers deux ans |
| **Congé de maternité** | Six semaines avant et huit semaines après la naissance, à ration pleine |
| **Travaux interdits** | Aux femmes enceintes et allaitantes : le fond de la mine, le quart de nuit, les fours à chaux, le **vert de Paris** (larvicide à l'arsenic des grands travaux, §5.6) et les soins dans la Zone |
| **Sages-femmes** | **Une sage-femme dans chaque bord de terre et de fond**, formée à l'**École de sages-femmes** de l'Hôpital de l'Îlot, à Cagliari ([19](19-savoir-et-medecine.md) §4), qui fait ses accouchements sur le *Provence*, maternité de l'îlot jusqu'en 1952 ([26](26-provence.md) §4). Il en faut environ **40 en 1950** et **60 en 1960** |
| **Crèches de bord** | Chaque bord de plus de 300 personnes tient une crèche, pour que les mères reprennent le travail à mi-temps |
| **L'honneur** | Chaque naissance est annoncée au **salut aux couleurs** du bord. Les mères de quatre enfants reçoivent un brassard d'honneur |
| **Le logement** | Les familles ont la priorité sur les logements à terre ; les célibataires restent à bord |

**Ce que l'îlot ne fait pas** : il n'accorde **aucun avancement aux pères**. Ce serait contraire au principe du **mérite** ([13](13-societe-de-bord.md) §4 bis). Le natalisme passe par la ration, le logement et l'honneur, jamais par le grade.

### 4.7 Le bilan des entrées (1949-1959) : qui arrive, par quelle voie [canon provisoire]

Ce tableau fait la somme des dotées (§4.4), des expéditions de recueil (§4.5) et des pactes de la Barbagia ([13](13-societe-de-bord.md) §6 bis). **Il est calé sur le modèle** : son total est le solde migratoire qui donne ~77 000 habitants en 1960 ([calculs/demographie_ilot.py](calculs/demographie_ilot.py), qui vérifie l'égalité).

| Origine | Voie d'entrée | Effectif | Femmes |
|---|---|---|---|
| **Sardes de l'intérieur** (Barbagia, Gallura, Logudoro) | Descendus seuls vers les bords, surtout des filles | ~1 400 | 75 % |
| **Barbagia** | **Pactes de village** (1955-1959) : des villages entiers | ~1 000 | 50 % |
| **Corse** | Traversées des bouches de Bonifacio | ~1 800 | 60 % |
| **Corse** | **Expéditions de recueil** (1955-1959) | ~900 | 55 % |
| **Côte italienne et archipel toscan** | **Expéditions de recueil** (1957-1959) | ~700 | 55 % |
| **Afrique du Nord** | Barques recueillies en mer par les navires de l'îlot | ~1 500 | 60 % |
| **Malte, Gozo**, épaves | Avant et pendant la patente (dont les 41 Gozitains de 1952, [18](18-expedition-albanie.md) §5 ter) | ~300 | 50 % |
| **Autres** | Baléares, Sicile, rescapés en mer | ~250 | 50 % |
| **Total** | | **~7 850** | **~60 %** |

**Par voie** : ~5 250 arrivées spontanées (67 %), ~1 600 par les expéditions de recueil (20 %), ~1 000 par les pactes de la Barbagia (13 %).

**Ce qu'on ne compte pas** : la population de l'îlot est celle des **inscrits**. Les survivants **hors-rôle** de l'intérieur de la Sardaigne n'y figurent pas : environ **8 000 à 12 000 personnes en 1950** [estimation], dont 4 000 à 6 000 dans la Barbagia proprement dite. C'est le réservoir d'où viennent les Sardes de l'intérieur et les villages des pactes. Après 1960, chaque nouveau pacte fait monter la population de l'îlot **en plus** de la courbe du §2.

## 5. Les métiers : ce dont l'île a besoin

### 5.1 La méthode

On part des **besoins de l'île en 1950** (nourriture, énergie, vêtements, santé, défense), tels que les fixent les chapitres [15](15-energie.md), [17](17-autosuffisance-alimentaire.md) et [19](19-savoir-et-medecine.md). Pour chacun, on estime la **productivité d'un travailleur** sans moteurs ni carburant, avec la ration de 1950. L'effectif nécessaire en découle.

### 5.2 Les postes permanents en 1950 [estimation, canon provisoire]

| Secteur | Besoin de l'île | Productivité | Effectif | Femmes |
|---|---|---|---|---|
| **Cultures** | ~11 500 ha cultivés ([17](17-autosuffisance-alimentaire.md) §6) | ~3 ha par travailleur, à la houe et à l'âne | **~3 800** | 35 % |
| **Élevage** | ~60 000 têtes en reconstitution | ~100 têtes par berger | ~600 | 25 % |
| **Pêche** | ~3 300 t de poisson par an | ~3 t par pêcheur et par an | **~1 100** | 5 % |
| **Transformation** | ~14 000 t de grain, poisson, huile, fromage | Moulins, fours, salaisons, poutargue | ~600 | 45 % |
| **Cuisines et ration** | 55 000 rations par jour | ~60 rations par cuisinier ou distributeur | ~900 | 60 % |
| **Mines de charbon** | ~200 000 t par an ([15](15-energie.md)) | ~60 t par mineur et par an (contre ~85 avant-guerre, avec les machines) | **~3 300** | 3 % |
| **Bois, sel, chaux** | Bois de mine et de chauffage ; salines de Cagliari ; chaux pour le chaulage des sols | — | ~900 | 10 % |
| **Énergie** | Centrales des navires, barrages du Tirso, usine à gaz, distillerie de goudron | — | ~550 | 10 % |
| **Bords à flot** | *Georges Leygues*, contre-torpilleurs, sous-marins, chalutiers armés | — | **~2 000** | 0 % |
| **Arsenal et ateliers** | Entretien de la flotte, forges, outils, pièces | — | ~1 400 | 10 % |
| **Garde et avant-postes** | Côtes, dépôts, la Ligne, l'Asinara ; Malte (~250), Sazan (~60) | — | ~1 900 | 2 % |
| **Bâtiment** | Logements, toits, citernes, fours | ~1 ouvrier pour 40 habitants | ~1 400 | 5 % |
| **Textile, vêtement, cuir** | Laine, lin, chanvre, peaux : tout ce que l'on porte | ~1 ouvrier pour 40 habitants | ~1 400 | 70 % |
| **Transports** | Charrois, voie ferrée du Sulcis, cabotage | — | ~800 | 5 % |
| **Santé** | Hôpitaux, la Zone, maternités, la visite ([19](19-savoir-et-medecine.md)) | ~1 soignant pour 65 habitants, dont ~70 médecins et ~40 sages-femmes | ~850 | 70 % |
| **Crèches** | ~7 800 enfants de moins de 5 ans | ~1 gardienne pour 10 enfants | ~800 | 95 % |
| **Écoles et savoir** | ~4 000 élèves ; École navale, université, bibliothèque | ~1 maître pour 25 élèves | ~160 | 55 % |
| **Administration** | Inscription, commissariat, transmissions, justice, aumôniers | — | ~600 | 40 % |
| **Total** | | | **~23 000** | **~24 %** |

### 5.3 Ce que montre ce bilan

- **Nourrir l'île occupe environ 7 000 personnes**, soit un tiers des postes ; **l'énergie et la mine, environ 4 700** ; **la mer et la garde (flotte, arsenal, garde), environ 5 300**. C'est la structure d'une **base navale agricole** : un tiers aux champs et à la pêche, un tiers à la mine et à la mer, un tiers aux services.
- **Les femmes tiennent les services** : santé, crèches, cuisines, vêtement. C'est exactement le rôle que leur donne le canon ([13](13-societe-de-bord.md) §4 ter).
- **Le vêtement est un vrai problème** : sans importations, il faut tondre, filer, tisser, tanner et coudre tout ce que portent 55 000 personnes. Les uniformes des flottes sont usés jusqu'à la corde vers 1945. Le métier à tisser à bras revient dans chaque bord de terre [estimation].
- **La pêche demande beaucoup de bras** pour peu de calories (7 %), mais elle fournit les protéines ([17](17-autosuffisance-alimentaire.md) §6). Les Corses en sont le noyau.

### 5.4 Les bras disponibles

| | Hommes | Femmes | Total |
|---|---|---|---|
| Population de 15 à 64 ans en 1950 | ~27 000 | ~14 500 | ~41 500 |
| Malades, invalides, paludisme (~8 %) | −2 200 | −1 200 | −3 400 |
| Mères de nourrissons (à mi-temps) | — | −2 400 | −2 400 |
| **Disponibles** | **~24 800** | **~10 900** | **~35 700** |
| Postes permanents (§5.2) | ~17 500 | ~5 500 | ~23 000 |
| **Marge** | **~7 300** | **~5 400** | **~12 700** |

**Cette marge n'est pas oisive** :
- **Les pointes saisonnières** : la moisson et les semailles demandent **8 000 à 10 000 bras de plus** pendant six semaines ; c'est le **branle-bas des moissons** ([17](17-autosuffisance-alimentaire.md) §2.5).
- **Le travail domestique** : l'eau, le bois, la lessive, les potagers familiaux, la couture de la famille. Il pèse surtout sur les femmes.
- **Les mousses** (12-16 ans) travaillent l'après-midi ([13](13-societe-de-bord.md) §4), mais ce sont les enfants de la Nuit : ils sont très peu nombreux.
- **Le reste est une réserve** que le Conseil emploie aux grands travaux, puis à l'expansion (§5.6).

**Note** : le chapitre 17 affirme que « le facteur limitant est le travail, pas la terre ». Le modèle le précise : le travail manque **aux pointes de la moisson et pour les bêtes de trait**, pas en moyenne sur l'année. Le chapitre 17 a été nuancé dans ce sens.

### 5.5 L'évolution des métiers (1940-1960) [canon provisoire]

| Période | Ce qui domine |
|---|---|
| **1940-1943** | **La garde et la survie** : garder les dépôts, collecter le grain, abattre le cheptel, tenir la mine. Les marins font tout. Presque pas d'artisans, aucun enfant à garder |
| **1944-1947** | **La Morìa** : la garde des côtes et de la Ligne, la Zone, les soignants. Les premiers champs reconstitués |
| **1948-1952** | **Le grand berceau** : les maternités et les crèches ; les champs atteignent l'autosuffisance ; les marins des grands navires désarmés passent à la mine et aux champs ; les **chauffeurs** du charbon remplacent les mécaniciens du mazout ([15](15-energie.md)) |
| **1950-1955** | **Les grands travaux** (§5.6) : drainage, chaulage, reconstruction. Environ 5 000 hommes dans les bords du Génie |
| **1955-1960** | **L'expansion** vers le nord (§5.6) et **l'école** : avec 29 000 enfants en 1960, il faut environ **800 maîtres** (contre 160 en 1950). Les métiers du savoir montent ([19](19-savoir-et-medecine.md) §3.5). Les immigrés sont choisis selon les besoins : ingénieurs, médecins, artisans, **et des femmes** (§4.4) |

### 5.6 L'emploi de la réserve : les grands travaux, puis l'expansion [canon : principe ; provisoire : détail]

**Décision de l'auteur** : la réserve de bras va d'abord aux **grands travaux**, puis à l'**expansion** vers le nord de l'île (option B1 puis B2).

**1950-1955 : les grands travaux.** Le Conseil crée des **bords du Génie** : environ 5 000 hommes, surtout des célibataires des flottes, qui rejoignent la moisson à la saison.

| Chantier | Pourquoi | Où |
|---|---|---|
| **Le drainage contre le paludisme** | Sans DDT, c'est la seule arme durable ([17](17-autosuffisance-alimentaire.md) §7) : curage des canaux, comblement des mares, assèchement des marais, poissons gambusies, vert de Paris | Campidano, abords de Santa Gilla et de Cagliari, plaine d'Oristano |
| **Le chaulage** | Neutraliser les sols acidifiés de 1940-41 ([17](17-autosuffisance-alimentaire.md) §2) | Fours à chaux de l'Iglesiente |
| **La reconstruction** | Remettre en état les villages vides du Campidano pour les familles (§4.6) | Le long de la voie ferrée Cagliari – Oristano |
| **Les voies** | Voie ferrée du Sulcis et ligne Cagliari – Oristano, routes empierrées | Sud et ouest |

**[histoire] Le précédent** : la bonification d'**Arborea** (alors Mussolinia), dans les années 1920-30, a asséché les marais de Sassu, près d'Oristano, et installé des familles de colons. L'îlot reprend ses canaux et ses fermes.

**1955-1960 : l'expansion vers le nord.** Les grands travaux ouvrent la route aux nouveaux **bords de terre** :
- **la plaine d'Oristano et d'Arborea** (vers 1955), puis le **Marghine** et le **Logudoro** ;
- **Sassari et Porto Torres** vers 1958-1960, à la limite de la Gallura ;
- **les colons sont des couples** : un homme des flottes ou des bords du Génie et, souvent, une dotée (§4.4). Ils reçoivent la terre à leur mariage ;
- **la Barbagia est contournée, pas conquise** : l'expansion longe la montagne par l'ouest. La montagne est **intégrée petit à petit**, village par village, par le troc, le médecin, les mariages et le **pacte de village** ([13](13-societe-de-bord.md) §6 bis).

**Ce que cela coûte** : l'expansion disperse l'îlot. Les nouveaux bords sont à 100 ou 200 km de Cagliari, à deux jours de charroi. Il faut des postes de garde, une voie ferrée tenue, et des sages-femmes et des maîtres dans chaque bord.

## 6. Les origines : un peuple en fusion

| Origine | 1946 | Part | En 1960 |
|---|---|---|---|
| Sardes (civils) | ~25 750 | 53 % | Toujours la majorité, mais les enfants de couples mixtes sont **la moitié des naissances** |
| Marins et civils des flottes (Français, Britanniques) | ~16 300 | 33 % | Une génération d'hommes de 40 à 60 ans, au sommet de la hiérarchie |
| Militaires italiens | ~3 300 | 7 % | Fondus dans la population |
| Corses | ~3 000 | 6 % | Pêcheurs, marins, médecins |
| Rescapés de Bizerte et Maltais | ~650 | 1 % | — |
| Entrées de 1949-1959 : dotées, recueillis, villages de la Barbagia (§4.7) | — | — | ~7 850 (10 %) |

La première génération née dans l'île (après 1944) est **sarde par la mère et étrangère par le père** dans un cas sur deux. C'est elle qui parle la **langue de bord** comme langue maternelle ([13](13-societe-de-bord.md) §7).

## 7. Points à vérifier

- ✅ Corrigé le 10 novembre 2026 : chapitre 13 (« environ 82 % d'hommes ») ; chapitre 17 §6 (le travail manque aux pointes de la moisson) ; chapitre 05 §4 (reprise forte des naissances en 1947).
- 🔧 Le total de 1950 du modèle (~54 000) est légèrement sous le canon (~55 000). Écart acceptable.
- 🔎 Démographie de la Sardaigne en 1936 (pyramide, espérance de vie, mortalité infantile) ; surmortalité masculine dans les grandes famines (Irlande 1846-51, Leningrad, Bengale 1943).
- 🔎 Effectifs et rapport des sexes en Nouvelle-Galles du Sud ; nombre exact des filles du Roi.

## 8. Décisions arrêtées et questions suivantes

| Question | Décision de l'auteur | Où |
|---|---|---|
| A. Le déséquilibre des sexes | **A2** : immigration féminine organisée après 1952, les dotées | §4.4 |
| B. La réserve de bras | **B1 puis B2** : grands travaux (1950-1955), puis expansion vers le nord (1955-1960) | §5.6 |
| C. La politique des naissances | **C3** : natalisme de bord et protection des mères | §4.6 |
| D. Les Corses et les autres rescapés | **Expéditions de recueil** vers la Corse et la côte italienne, **seulement si le flux naturel ne suffit pas** | §4.5, bilan §4.7 |
| E. La relève des fondateurs | **Renouvellement des élites par le mérite** : les meilleurs élèves formés à l'**École navale de l'Îlot** ; le creux des enfants de la Nuit (1959-1963), puis les promotions du grand berceau (1965-1970) | [13](13-societe-de-bord.md) §4 quater |
| F. La Barbagia | **Intégrée petit à petit** : troc, médecin, mariages, puis pacte de village | [13](13-societe-de-bord.md) §6 bis |

**Questions qui en découlent** :
1. ❓ **Le rachat des captifs** : quand une chefferie retient des gens qui veulent partir, l'îlot peut-il payer leur liberté (grain, sel, charbon), comme les ordres de la Rédemption des captifs rachetaient les chrétiens captifs à Alger et à Tunis aux XVIᵉ-XVIIIᵉ siècles [histoire] ? Ou s'y refuse-t-il, pour ne pas faire des captifs une marchandise ?
