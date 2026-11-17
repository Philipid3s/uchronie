"""Construit la première édition imprimable de la bible à partir des chapitres sources.

    python edition/build.py              # livre complet : HTML + PDF
    python edition/build.py --parties I  # seulement certaines parties (prototype)
    python edition/build.py --html       # HTML seulement, sans PDF

Les fichiers .md de la bible restent la seule source : ce script les nettoie (marqueurs de
travail, décisions de l'auteur, questions ouvertes), renumérote les chapitres, convertit les
renvois, insère les cartes de l'atlas et met le tout en page (A4) avec Paged.js, puis Chrome
imprime le PDF.
"""
import argparse
import datetime
import html
import json
import pathlib
import re
import sys

import markdown

ROOT = pathlib.Path(__file__).resolve().parents[1]
ED = ROOT / "edition"
BUILD = ED / "build"
sys.path.insert(0, str(ED))
import plan  # noqa: E402

ORDINAUX = {"I": "Première", "II": "Deuxième", "III": "Troisième", "IV": "Quatrième",
            "V": "Cinquième", "VI": "Sixième", "VII": "Septième"}

# --- Nettoyage -------------------------------------------------------------------------------

SECTIONS_RETIREES = re.compile(
    r"questions ouvertes|ce qui reste ouvert|décisions de l'auteur|ce que la bible dit déjà|"
    r"points à vérifier|décisions arrêtées",
    re.I)
SECTIONS_QUESTIONS = re.compile(r"questions ouvertes|ce qui reste ouvert|questions suivantes", re.I)
BLOCS_RETIRES = re.compile(r"\*\*\[canon|\*\*Statut|\*\*Question de l'auteur|\*\*Constat de l'auteur|\*\*Note v\d|^>\s*Légende\s*:", re.M)

MARQUEURS = [
    (r"[🔎🔧❓]\s?", ""),
    # ✅ marque une décision prise, sauf dans les tableaux où c'est un symbole de légende
    (r"(?m)^((?!\s*\||\*\*Légende).*?)✅\s?", r"\1"),
    (r"(?m)^((?!\s*\||\*\*Légende).*?)✅\s?", r"\1"),
    (r"\[histoire\s*:\s*([^\]]+)\]", r"(\1)"),
    (r"\s*\[(?:canon|estimation|calcul|histoire|illustration|proposition|position provisoire|"
     r"personnage|inventé|texte inventé|ordre de grandeur|identité à|à |nom à|noms à|date à|lieu à|emplacement à)[^\]]*\]", ""),
    (r"\s*\*\(prov\.\)\*", ""),
    (r"Écarts au canon", "Écarts au texte"),
    # « Décision de l'auteur : les postes… » -> « Les postes… »
    (r"\*\*(?:Décision|Décisions) de l'auteur\*\*\s*(?:\([^)]*\))?\s*:\s*(\*\*)?([a-zéèêàâîôûç]?)",
     lambda m: (m.group(1) or "") + m.group(2).upper()),
    (r"\*\*Validé par l'auteur\*\*\s*:[^\n]*", ""),
    (r"\s*\((?:décision de l'auteur|options? [0-9A-D])[^)]*\)", ""),
]
NETTOYAGE = [
    (r"\*\*[ \t]*\*\*[ \t]*", ""),
    (r",\s*\)", ")"),
    (r"\(\s*[,;]?\s*\)", ""),
    (r"\(\s*;\s*", "("),
    (r"[ \t]+([,.])", r"\1"),
    (r"(?<=\S)[ \t]{2,}", " "),
    (r"(^|[\s(])\*\*\s+(?=\S)", r"\1**"),
    (r";\s*;", ";"),
    (r"\s+\)", ")"),
]


def table_chapitres():
    """Associe chaque fichier source à son numéro de chapitre ou à sa lettre d'annexe."""
    renvois, n = {}, 0
    for _, _, _, fichiers in plan.PARTIES:
        for f in fichiers:
            n += 1
            renvois[f] = f"chap. {n}"
    for lettre, _, f in plan.ANNEXES:
        renvois[f] = f"annexe {lettre}"
    return renvois


def titre_html(t):
    """Titre de chapitre ou d'annexe en HTML : échappé, avec *italique* (noms de navires) en <em>."""
    return re.sub(r"\*([^*]+)\*", r"<em>\1</em>", html.escape(t))


def convertir_liens(texte, renvois):
    def lien(m):
        cible = m.group(2).split("#")[0]
        if cible in renvois:
            return renvois[cible]
        if cible.startswith("09-"):
            return "annexe C"
        return m.group(1)
    # liens internes vers d'autres chapitres, le README, les calculs, les annexes
    texte = re.sub(r"\[([^\]]*)\]\(((?:\d\d-[\w-]+\.md|README\.md)(?:#[\w-]*)?)\)", lien, texte)
    texte = re.sub(r"\s*\(\[(?:sources|sortie)\]\([^)]*\)\)", "", texte)
    texte = re.sub(r"\s*\(\[[^\]]+\]\(annexes/resultats_calculs\.md[^)]*\)\)", "", texte)
    texte = re.sub(r"\[([^\]]+)\]\((?:calculs|annexes)/[^)]*\)", r"\1", texte)
    texte = re.sub(r"(?<!!)\[([^\]]+)\]\(https?://[^)]*\)", r"\1", texte)
    texte = re.sub(r"\bau chapitre chap\.", "au chap.", texte)
    texte = re.sub(r"\bles chapitres (chap\.)", r"les \1", texte)
    texte = re.sub(r"\bchapitre (chap\.)", r"\1", texte)
    # l'annexe C (état de la bible) n'est pas un renvoi de lecture : on retire ces renvois du texte
    texte = re.sub(r"\s*;\s*annexe C(?:,? §?\s?[A-Z]?\d+)?(?=\))", "", texte)
    texte = re.sub(r",\s*annexe C(?:,? §?\s?[A-Z]?\d+)?(?=\))", "", texte)
    texte = re.sub(r"\s*\(annexe C(?:,? §?\s?[A-Z]?\d+)?\)", "", texte)
    texte = re.sub(r"(chap\. \d+|annexe [A-E]) §", r"\1, §", texte)
    texte = re.sub(r"§\s?(\d)", "§ \\1", texte)
    return texte


def capitaliser_debuts(lignes):
    """Après le retrait d'un « Décision de l'auteur : », remet une majuscule en tête."""
    out = []
    for l in lignes:
        m = re.match(r"^((?:>\s*)?\s*(?:[-*]\s+)?(?:\*\*)?)([a-zéèêàâîôûç])", l)
        if m and (l.lstrip().startswith("**") or not l.startswith(" ")):
            l = m.group(1) + m.group(2).upper() + l[m.end():]
        out.append(l)
    return out


def aerer_blocs(lignes):
    """Python-Markdown exige une ligne vide avant une liste ou un tableau : les sources de la
    bible n'en mettent pas toujours."""
    out = []
    for l in lignes:
        # sous-listes et tableaux indentés de 1 à 3 espaces : Python-Markdown en veut 4
        l = re.sub(r"^ {1,3}(?=(?:[-*]|\d+\.)\s|\|)", "    ", l)
        if out and out[-1].strip():
            prec = out[-1].lstrip()
            liste = re.match(r"^\s*(?:[-*]|\d+\.)\s", l) and not re.match(r"^\s*(?:[-*]|\d+\.)\s", out[-1])
            liste = liste and not out[-1].startswith((" ", "\t")) and not l.startswith((" ", "\t"))
            tableau = l.startswith("|") and not prec.startswith("|")
            if liste or tableau:
                out.append("")
        out.append(l)
    return out


def nettoyer(texte, renvois):
    """Retourne (markdown nettoyé, titre source, sections de questions ouvertes retirées)."""
    lignes = texte.split("\n")
    titre = re.sub(r"^#\s*(\d+\s*—\s*)?", "", lignes[0]).strip() if lignes[0].startswith("# ") else ""
    if titre:
        lignes = lignes[1:]
    corps, questions, retires = [], [], []
    i = 0
    while i < len(lignes):
        l = lignes[i]
        # blocs de citation de travail (statut, décisions, notes de version)
        if l.startswith(">"):
            bloc = []
            while i < len(lignes) and lignes[i].startswith(">"):
                bloc.append(lignes[i])
                i += 1
            if not BLOCS_RETIRES.search("\n".join(bloc)):
                corps.extend(bloc)
            continue
        m = re.match(r"^(#{2,4})\s+(.*)", l)
        if m and SECTIONS_RETIREES.search(m.group(2)):
            niveau = len(m.group(1))
            section = [l]
            i += 1
            while i < len(lignes):
                m2 = re.match(r"^(#{2,4})\s", lignes[i])
                if m2 and len(m2.group(1)) <= niveau:
                    break
                section.append(lignes[i])
                i += 1
            if SECTIONS_QUESTIONS.search(m.group(2)):
                questions.append("\n".join(section[1:]).strip())
            mn = re.match(r"(\d+)\.", m.group(2))
            if niveau == 2 and mn:
                retires.append(int(mn.group(1)))
            continue
        corps.append(l)
        i += 1
    md = "\n".join(corps)
    for motif, rempl in MARQUEURS:
        md = re.sub(motif, rempl, md)
    md = convertir_liens(md, renvois)
    for motif, rempl in NETTOYAGE:
        md = re.sub(motif, rempl, md)
    md = "\n".join(aerer_blocs(capitaliser_debuts(md.split("\n"))))
    # chemins des images, relatifs au livre construit dans edition/build/
    md = md.replace("](illustrations/", "](../../illustrations/")
    return md, titre, questions, retires


def nettoyer_fichier(f, renvois):
    """Nettoie un fichier source et applique les remplacements propres à l'édition."""
    md, titre, questions, retires = nettoyer((ROOT / f).read_text(encoding="utf-8"), renvois)
    for motif, rempl in plan.REMPLACEMENTS.get(f, []):
        md = re.sub(motif, rempl, md, flags=re.M)
    return md.strip(), titre, questions, carte_numeros(md, retires)


# --- Annexe C : l'état de la bible ----------------------------------------------------------------

def etat_de_la_bible(toutes_questions, renvois):
    """Les questions encore ouvertes, chapitre par chapitre (les points réglés, marqués ✅, sont
    omis)."""
    parties = ["Cette édition fixe l'état de la bible au moment de sa publication. Les points "
               "ci-dessous restent à décider ou à documenter ; ils sont classés par chapitre."]
    for n, titre, blocs in toutes_questions:
        items = []
        for bloc in blocs:
            courant = []
            for l in bloc.split("\n"):
                if re.match(r"^(\d+\.|[-*])\s", l):
                    if courant:
                        items.append(courant)
                    courant = [l]
                elif courant:
                    courant.append(l)
            if courant:
                items.append(courant)
        # les points réglés : ✅, ou « Décidé » / « intégré » dans le texte
        items = [i for i in items if "✅" not in i[0]
                 and not re.search(r"\bDécidé|\bdécidé :|\bintégré (dans|au)", "\n".join(i))]
        if not items:
            continue
        texte = "\n".join("\n".join(i) for i in items)
        texte = re.sub(r"^\d+\.\s", "- ", texte, flags=re.M)
        texte = re.sub(r"[🔎🔧❓✅]\s?", "", texte)
        texte = convertir_liens(texte, renvois)
        texte = re.sub(r"\s*\((?:lié à |voir )?annexe C[^)]*\)", "", texte)
        texte = "\n".join(aerer_blocs(capitaliser_debuts(texte.split("\n"))))
        parties.append(f"### Chap. {n} — {titre}\n\n{texte}")
    return "\n\n".join(parties)


# --- Annexe D : l'index ---------------------------------------------------------------------------

def indexer(html_chap, cid, entrees):
    """Repère, dans le HTML d'un chapitre, la première mention de chaque entrée et y pose une
    ancre ; note l'ancre dans `entrees[(catégorie, terme)]`."""
    pieces = re.split(r"(<[^>]+>)", html_chap)
    vus = set()
    termes = ([("Navires", t, True) for t in plan.INDEX_NAVIRES] +
              [("Personnes", t, False) for t in plan.INDEX_PERSONNES] +
              [("Lieux", t, False) for t in plan.INDEX_LIEUX] +
              [("Notions", t, False) for t in plan.INDEX_NOTIONS])
    dans_em = dans_titre = False
    for k, p in enumerate(pieces):
        if p.startswith("<"):
            tag = p.lower()
            if tag.startswith("<em"):
                dans_em = True
            elif tag.startswith("</em"):
                dans_em = False
            elif re.match(r"<h[1-4]", tag) or tag.startswith("<figcaption"):
                dans_titre = True
            elif re.match(r"</h[1-4]", tag) or tag.startswith("</figcaption"):
                dans_titre = False
            continue
        if dans_titre or not p.strip():
            continue
        for cat, terme, italique in termes:
            if (cat, terme) in vus or italique != dans_em:
                continue
            motif = rf"(?<![\wÀ-ÿ']){re.escape(terme)}(?![\wÀ-ÿ])"
            if italique:
                motif = rf"^{re.escape(terme)}$"
            m = re.search(motif, p)
            if not m:
                continue
            vus.add((cat, terme))
            ancre = f"ix-{cid}-{len(vus)}"
            entrees.setdefault((cat, terme), []).append(ancre)
            p = p[:m.start()] + f'<span id="{ancre}"></span>' + p[m.start():]
        pieces[k] = p
    return "".join(pieces)


def page_index(entrees):
    blocs = []
    for cat in ["Personnes", "Navires", "Lieux", "Notions"]:
        termes = sorted([t for (c, t) in entrees if c == cat],
                        key=lambda t: t.lower().replace("é", "e").replace("è", "e").replace("ç", "c"))
        lignes = []
        for t in termes:
            liens = "".join(f'<a class="ixp" href="#{a}"></a>' for a in entrees[(cat, t)])
            nom = f"<em>{html.escape(t)}</em>" if cat == "Navires" else html.escape(t)
            lignes.append(f'<li><span class="ixt">{nom}</span>{liens}</li>')
        blocs.append(f'<h2>{cat}</h2><ul class="index">{"".join(lignes)}</ul>')
    return "".join(blocs)


# --- Renumérotation des sections ---------------------------------------------------------------

def carte_numeros(md, retires):
    """Quand une section de travail numérotée a été retirée avant d'autres (« 1. Décisions de
    l'auteur »), les sections restantes sont renumérotées à partir de 1. Retourne la table
    ancien numéro -> nouveau, vide si rien ne change."""
    if not retires:
        return {}
    restants = []
    for m in re.finditer(r"^## (\d+)\b", md, re.M):
        k = int(m.group(1))
        if k not in restants:
            restants.append(k)
    carte = {ancien: nouveau for nouveau, ancien in enumerate(restants, 1)}
    return {} if all(a == b for a, b in carte.items()) else carte


def renumeroter(md, n, cartes):
    """Applique les tables de renumérotation aux titres du chapitre n et à tous les renvois
    « § N » (ceux du chapitre lui-même et les « chap. K, § N » vers d'autres chapitres)."""
    propre = cartes.get(n, {})
    if propre:
        md = re.sub(r"^(#{2,4}) (\d+)\b", lambda m: f"{m.group(1)} {propre.get(int(m.group(2)), int(m.group(2)))}",
                    md, flags=re.M)

    def ref(m):
        prefixe, cible, num = m.group(1) or "", m.group(2), int(m.group(3))
        if prefixe.startswith("annexe"):
            return m.group(0)
        if not cible:
            # « chap. 28, § 3 bis et § 10 » : le second § suit le chapitre cité juste avant
            avant = m.string[max(0, m.start() - 40):m.start()]
            mc = re.search(r"chap\. (\d+), §[^()]*$", avant)
            cible = mc.group(1) if mc else None
        carte = cartes.get(int(cible), {}) if cible else propre
        return f"{prefixe}§\u00a0{carte.get(num, num)}"
    return re.sub("((?:chap\\. (\\d+)|annexe [A-E]), )?§[ \u00a0](\\d+)", ref, md)


# --- Figures de l'atlas ------------------------------------------------------------------------

def figure_atlas(cle, legendes):
    nom = cle.split(":", 1)[1]
    base = nom.split("-")[0]
    info = legendes.get(base, {})
    titre, sous = info.get("titre", ""), info.get("sous_titre", "")
    for g in info.get("graphiques", []):
        if g["fichier"] == f"{nom}.png":
            titre, sous = g["titre"], g["sous_titre"]
            if base == "pyramide":
                titre, sous = f"La pyramide des âges en {g['sous_titre']}", info.get("sous_titre", "")
    genre = "Graphique" if "graphiques" in info else "Carte"
    leg = f"<strong>{html.escape(titre)}</strong>" + (f" — {html.escape(sous)}" if sous else "")
    return (f'\n\n<figure class="atlas"><img src="../figures/atlas/{nom}.png" alt="{html.escape(titre)}">'
            f'<figcaption><span class="genre">{genre}</span> {leg}</figcaption></figure>\n\n')


def inserer_figures(md, fichier, legendes):
    for ancre, cle in plan.FIGURES.get(fichier, []):
        fig = figure_atlas(cle, legendes)
        if ancre is None:
            md += fig
            continue
        m = re.search(rf"^#{{2,4}}[^\n]*{re.escape(ancre)}[^\n]*\n", md, re.M)
        if not m:
            print(f"  ! ancre introuvable dans {fichier} : {ancre}", file=sys.stderr)
            md += fig
            continue
        # après le premier paragraphe qui suit le titre
        fin = md.find("\n\n", m.end())
        fin = len(md) if fin == -1 else fin
        md = md[:fin] + fig + md[fin:]
    return md


# --- Assemblage ----------------------------------------------------------------------------

def md_html(md):
    return markdown.markdown(md, extensions=["tables", "sane_lists", "attr_list"],
                             output_format="html5")


def construire(parties_voulues, avec_annexes):
    renvois = table_chapitres()
    legendes = json.loads((ED / "figures" / "atlas" / "legendes.json").read_text(encoding="utf-8"))
    toc, corps, toutes_questions, entrees = [], [], [], {}
    # première passe : nettoyer tous les chapitres, pour connaître les renumérotations
    nettoyes, cartes, n = {}, {}, 0
    for _, _, _, fichiers in plan.PARTIES:
        for f in fichiers:
            n += 1
            nettoyes[f] = nettoyer_fichier(f, renvois)
            cartes[n] = nettoyes[f][3]
    n = 0
    for num, nom, dates, fichiers in plan.PARTIES:
        inclus = parties_voulues is None or num in parties_voulues
        if not inclus:
            n += len(fichiers)
            continue
        pid = f"partie-{num}"
        toc.append(f'<li class="toc-partie"><a href="#{pid}">{ORDINAUX[num]} partie — {html.escape(nom)}</a></li>')
        corps.append(f'<section class="partie" id="{pid}"><p class="partie-num">{ORDINAUX[num]} partie</p>'
                     f'<h1 class="partie-titre">{html.escape(nom)}</h1><p class="partie-dates">{dates}</p></section>')
        for f in fichiers:
            n += 1
            md, titre_src, questions, _ = nettoyes[f]
            md = renumeroter(md, n, cartes)
            titre = plan.TITRES.get(f, titre_src)
            md = inserer_figures(md, f, legendes)
            if questions:
                toutes_questions.append((n, titre, questions))
            cid = f"chap-{n}"
            toc.append(f'<li class="toc-chap"><a href="#{cid}"><span class="n">{n}</span><span class="titre">{titre_html(titre)}</span></a></li>')
            corps.append(f'<section class="chapitre" id="{cid}" data-partie="{html.escape(nom)}">'
                         f'<header class="chap-tete"><p class="chap-num">Chapitre {n}</p>'
                         f'<h1 class="chap-titre">{titre_html(titre)}</h1></header>'
                         f'{indexer(md_html(md), cid, entrees)}</section>')
    if avec_annexes:
        toc.append('<li class="toc-partie"><a href="#annexes">Annexes</a></li>')
        corps.append('<section class="partie" id="annexes"><p class="partie-num">&nbsp;</p>'
                     '<h1 class="partie-titre">Annexes</h1><p class="partie-dates">&nbsp;</p></section>')
        for lettre, titre, f in plan.ANNEXES:
            aid = f"annexe-{lettre}"
            if f is not None:
                md = renumeroter(nettoyer_fichier(f, renvois)[0], None, cartes)
                contenu = md_html(md)
            elif titre == "Index":
                contenu = page_index(entrees)
            else:
                contenu = md_html(etat_de_la_bible(toutes_questions, renvois))
            toc.append(f'<li class="toc-chap"><a href="#{aid}"><span class="n">{lettre}</span><span class="titre">{titre_html(titre)}</span></a></li>')
            corps.append(f'<section class="chapitre annexe" id="{aid}" data-partie="Annexes">'
                         f'<header class="chap-tete"><p class="chap-num">Annexe {lettre}</p>'
                         f'<h1 class="chap-titre">{titre_html(titre)}</h1></header>{contenu}</section>')
    return toc, corps, toutes_questions


GABARIT = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>{titre} — {sous_titre}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Sans+Condensed:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../livre.css">
<script>window.PagedConfig = {{ auto: true, after: () => {{ window.__pagedDone = true; }} }};</script>
<script src="../vendor/paged.polyfill.js"></script>
<script src="../vendor/repeter-entetes.js"></script>
</head>
<body>
<section class="couverture">
  <p class="couv-sur">Bible de l'uchronie</p>
  <h1 class="couv-titre">{titre}</h1>
  <p class="couv-sous">Une civilisation née du bord en Sardaigne<br>après la comète de juillet 1940</p>
  <p class="couv-ed">Première édition · 1940 – 1960</p>
</section>
<section class="faux-titre">
  <h1>{titre}</h1>
  <p>{sous_titre}</p>
  <p class="colophon">Édition générée le {date} à partir des chapitres de la bible.<br>
  Les cartes et les graphiques sont tirés de l'atlas de l'Îlot.</p>
</section>
<nav class="sommaire">
  <h1>Sommaire</h1>
  <ol>{toc}</ol>
</nav>
{avant_propos}
{corps}
</body>
</html>
"""


def rendre_pdf(html_path, pdf_path):
    """Sert le dépôt en HTTP local (Paged.js ne peut pas relire les feuilles de style en
    file://), laisse Paged.js paginer, puis fait imprimer le PDF par Chrome."""
    import functools
    import http.server
    import threading
    from playwright.sync_api import sync_playwright

    class Silencieux(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass

    serveur = http.server.ThreadingHTTPServer(
        ("127.0.0.1", 0), functools.partial(Silencieux, directory=str(ROOT)))
    threading.Thread(target=serveur.serve_forever, daemon=True).start()
    url = f"http://127.0.0.1:{serveur.server_address[1]}/{html_path.relative_to(ROOT).as_posix()}"
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(channel="chrome")
            page = browser.new_page()
            page.on("pageerror", lambda e: print("  ! erreur JS :", e, file=sys.stderr))
            page.goto(url, wait_until="networkidle")
            page.wait_for_function("window.__pagedDone === true", timeout=900_000, polling=2000)
            page.pdf(path=str(pdf_path), prefer_css_page_size=True, print_background=True)
            n = page.evaluate("document.querySelectorAll('.pagedjs_page').length")
            browser.close()
    finally:
        serveur.shutdown()
    return n


def avant_propos():
    md = (ROOT / plan.AVANT_PROPOS).read_text(encoding="utf-8")
    return (f'<section class="avant-propos"><h1 class="ap-titre">Avant-propos</h1>'
            f'{md_html(md)}</section>')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--parties", nargs="*", help="numéros des parties à inclure (ex. I II)")
    ap.add_argument("--html", action="store_true", help="ne pas produire le PDF")
    args = ap.parse_args()
    complet = not args.parties
    toc, corps, questions = construire(None if complet else set(args.parties), complet)
    BUILD.mkdir(parents=True, exist_ok=True)
    nom = "bible-1940-1960" if complet else "bible-1940-1960-partie-" + "-".join(args.parties)
    html_path = BUILD / f"{nom}.html"
    html_path.write_text(GABARIT.format(
        titre=html.escape(plan.TITRE), sous_titre=html.escape(plan.SOUS_TITRE),
        date=datetime.date.today().strftime("%d/%m/%Y"),
        toc="\n".join(toc), corps="\n".join(corps),
        avant_propos=avant_propos() if complet else ""), encoding="utf-8")
    print("HTML :", html_path.relative_to(ROOT))
    if not args.html:
        pdf_path = BUILD / f"{nom}.pdf"
        n = rendre_pdf(html_path, pdf_path)
        print(f"PDF  : {pdf_path.relative_to(ROOT)} ({n} pages)")


if __name__ == "__main__":
    main()
