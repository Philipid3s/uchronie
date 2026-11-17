"""Plan de la première édition de la bible (1940-1960).

Chaque partie liste ses chapitres dans l'ordre de lecture, par le nom de leur fichier source.
Les chapitres sont renumérotés de 1 à N dans cet ordre ; les renvois de la bible
(« [12](12-flottes-survivantes.md) §3 ») sont convertis en « chap. 9, § 3 ».

`titres` remplace le titre d'un chapitre quand celui de la source ne convient pas à un livre.
`figures` insère une figure de l'atlas après le premier titre de section qui contient le texte
donné (ou à la fin du chapitre si le texte est None).
"""

TITRE = "L'Îlot"
SOUS_TITRE = "Bible de l'uchronie · Première édition · 1940-1960"

PARTIES = [
    ("I", "La catastrophe", "1er – 2 juillet 1940", [
        "01-parametres-physiques.md",
        "02-impact-rambouillet.md",
        "03-impact-pacifique.md",
        "04-climat.md",
        "05-population.md",
    ]),
    ("II", "La fondation", "juillet – décembre 1940", [
        "06-mers-el-kebir.md",
        "10-choix-du-refuge.md",
        "11-ilot-de-civilisation.md",
        "12-flottes-survivantes.md",
    ]),
    ("III", "Le monde après", "1940 – 1960", [
        "07-le-monde-apres.md",
        "16-contacts-radio.md",
        "33-toulon.md",
    ]),
    ("IV", "Les années fermées", "1940 – 1948", [
        "14-epidemie.md",
        "15-energie.md",
        "36-expedition-de-la-manche.md",
        "17-autosuffisance-alimentaire.md",
    ]),
    ("V", "La société de l'Îlot", "1940 – 1960", [
        "13-societe-de-bord.md",
        "22-organisation-militaire.md",
        "21-demographie.md",
        "19-savoir-et-medecine.md",
        "30-formation-technique.md",
    ]),
    ("VI", "Les navires-bords", "1940 – 1960", [
        "23-dunkerque-siege-du-conseil.md",
        "24-hood-forteresse-du-golfe.md",
        "25-ark-royal.md",
        "26-provence.md",
        "27-strasbourg.md",
        "28-bretagne.md",
        "31-commandant-teste.md",
    ]),
    ("VII", "La réouverture", "1949 – 1960", [
        "18-expedition-albanie.md",
        "34-avant-poste-d-albanie.md",
        "32-avant-poste-de-malte.md",
        "20-capacites-aeronavales.md",
        "29-flotte-des-annees-1950.md",
        "35-navires-de-l-ilot.md",
    ]),
]

# Annexes : (lettre, titre, source). Une source None est une annexe construite par le script.
ANNEXES = [
    ("A", "Chronologie 1940-1960", "08-chronologie.md"),
    ("B", "Sources", "annexes/sources.md"),
    ("C", "État de la bible", None),
    ("D", "Index", None),
]

AVANT_PROPOS = "edition/avant-propos.md"

# Remplacements propres à l'édition, appliqués après le nettoyage (motif, remplacement).
REMPLACEMENTS = {
    "08-chronologie.md": [
        (r"^Légende :.*$", "Les faits marqués **[H]** sont historiques ; les événements marqués **[U]** "
                           "appartiennent à l'uchronie."),
        (r"^\*\*Périmètre\*\*.*$", "La chronologie couvre les années **1940-1960**. Les dates postérieures "
                                   "(démolitions, relève des fondateurs) ne sont que des perspectives."),
    ],
}

# Index : pour chaque entrée, la page de sa première mention dans chaque chapitre.
# Les navires ne sont repérés qu'en italique (le *Provence*, et non la Provence).
INDEX_NAVIRES = [
    "Algérie", "Alagi", "Anadyr", "Aradam", "Arethusa", "Ark Royal", "Axum", "Bretagne", "Canopo",
    "Cassiopea", "Colbert", "Commandant Teste", "Dunkerque", "Dupleix", "Enterprise", "Faulknor",
    "Foch", "Foxhound", "Georges Leygues", "Gloire", "Har Zion", "Hood", "Jacques Schiaffino",
    "Jean Bart", "Jean de Vienne", "Kersaint", "La Galissonnière", "Le Terrible", "Lynx",
    "Marseillaise", "Mogador", "Montcalm", "Orione", "Provence", "Resolution", "Richelieu",
    "San Adolfo", "Strasbourg", "Tigre", "Tornade", "Turchese", "Typhon", "Valiant", "Vidette",
    "Volta", "Vortigern", "Warspite", "Wrestler", "Béarn", "Émile Bertin",
]
INDEX_PERSONNES = [
    "Brotzu", "Collinet", "Cunningham", "Duplat", "Devin", "Ferrandi", "Ferretti", "Gensoul",
    "Godfroy", "Halloran", "Holland", "Kerlann", "Le Pivain", "Mercadier", "Pigliaru", "Sartori",
    "Scanagatta", "Somerville", "Spanedda", "Sportiello", "Vespignani",
]
INDEX_LIEUX = [
    "Alexandrie", "Alger", "Arborea", "Asinara", "Augusta", "Barbagia", "Bizerte", "Bonaria",
    "Bonifacio", "Cagliari", "Campidano", "Carbonia", "Carloforte", "Corse", "Crète", "Dakar",
    "Elmas", "Ferryville", "Gallura", "Gennargentu", "Gibraltar", "Gozo", "Iglesias", "Kuçova",
    "La Maddalena", "La Valette", "Malte", "Martinique", "Mers el-Kébir", "Molentargius", "Narta",
    "Nérac", "Nouvelle-Zélande", "Oran", "Oristano", "Rambouillet", "Saint-Mandrier",
    "Sant'Antioco", "Sarrabus", "Sazan", "Souda", "Spinalonga", "Su Siccu", "Sulcis", "Toulon",
    "Vlorë", "golfe de Palmas",
]
INDEX_NOTIONS = [
    "accord de Bonaria", "accord de Cagliari", "accord de Narta", "Cahiers techniques",
    "Capitaineries", "Chambre des warrants", "Code de l'Îlot", "Collège de l'Îlot",
    "Conseil des Amiraux", "Conseil scientifique", "Conservatoire de l'Îlot", "dotées",
    "École navale", "École technique", "Flottille", "Grand Carré", "Inscription générale",
    "Maistrance", "Morìa", "Nuit de feu", "patente de santé", "Plan de l'Arche",
    "règle de Joseph", "règle de Marseille", "réserve de l'Amirauté",
]

TITRES = {
    "01-parametres-physiques.md": "La comète",
    "02-impact-rambouillet.md": "L'impact de Rambouillet",
    "03-impact-pacifique.md": "L'impact du Pacifique Nord",
    "04-climat.md": "La nuit et l'hiver d'impact",
    "05-population.md": "La quasi-extinction",
    "08-chronologie.md": "Chronologie 1940-1960",
}

FIGURES = {
    "02-impact-rambouillet.md": [("Rayons caractéristiques", "atlas:france")],
    "03-impact-pacifique.md": [("Le méga-tsunami", "atlas:pacifique")],
    "05-population.md": [("Les vagues de mortalité", "atlas:population-1")],
    "06-mers-el-kebir.md": [(None, "atlas:mediterranee")],
    "11-ilot-de-civilisation.md": [(None, "atlas:sardaigne")],
    "15-energie.md": [("La courbe du mazout", "atlas:mazout-1"),
                      ("La courbe du mazout", "atlas:mazout-2"),
                      ("La campagne des dépôts", "atlas:mazout-3")],
    "21-demographie.md": [(None, "atlas:population-2"), (None, "atlas:population-3"),
                          (None, "atlas:population-4"), (None, "atlas:population-5"),
                          (None, "atlas:population-6"), (None, "atlas:pyramide-1946"),
                          (None, "atlas:pyramide-1960"), (None, "atlas:metiers")],
    "23-dunkerque-siege-du-conseil.md": [("Le mouillage", "atlas:cagliari")],
    "29-flotte-des-annees-1950.md": [("Les lignes des avant-postes", "atlas:routes")],
    "18-expedition-albanie.md": [("Les trois navires", "atlas:albanie")],
    "34-avant-poste-d-albanie.md": [("La garnison", "atlas:kucova")],
    "32-avant-poste-de-malte.md": [("Les lieux", "atlas:malte")],
}
