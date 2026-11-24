"""Construit le PDF de lecture des chapitres écrits du tome 1 (« Le Ciel de cendre »).

    python roman/tome-1/edition/build.py            # un PDF par partie (chapitre-NN.md présents)
    python roman/tome-1/edition/build.py --html     # HTML seulement

Les chapitres .md restent la seule source. La mise en page (format roman 140 × 215 mm)
est faite par Paged.js, et le PDF est imprimé par Chrome, comme pour l'édition de la bible
(edition/build.py, dont on réutilise rendre_pdf).
"""
import argparse
import datetime
import html
import pathlib
import re
import sys

import markdown

ICI = pathlib.Path(__file__).resolve().parent
TOME = ICI.parent
ROOT = TOME.parents[1]
BUILD = ICI / "build"
sys.path.insert(0, str(ROOT / "edition"))
from build import rendre_pdf  # noqa: E402

TITRE = "Le Ciel de cendre"

PARTIES = {  # premier chapitre de chaque partie (plan.md §4)
    1: ("Première partie", "La nuit de feu"),
    7: ("Deuxième partie", "Préservez la flotte"),
    13: ("Troisième partie", "Sous les canons"),
    19: ("Quatrième partie", "Le premier froid"),
}

GABARIT = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>{titre}</title>
<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=IBM+Plex+Mono:wght@400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../roman.css">
<script>window.PagedConfig = {{ auto: true, after: () => {{ window.__pagedDone = true; }} }};</script>
<script src="../../../../edition/vendor/paged.polyfill.js"></script>
</head>
<body>
<section class="titre">
  <p class="auteur">L'Îlot · roman</p>
  <h1>{titre}</h1>
  <p class="tome">Tome I · {partie}</p>
  <p class="etat">Chapitres {premiers} · version de travail<br>{date}</p>
</section>
<section class="faux-titre">
  <p>Du 30 juin 1940, veille de la nuit de feu,<br>à l'installation de l'îlot à Cagliari, à la fin de l'automne.</p>
</section>
{corps}
</body>
</html>
"""


def chapitre_html(n, texte):
    lignes = [l for l in texte.splitlines() if not re.match(r"^#{1,2}\s", l)]
    texte = "\n".join(lignes)
    m = re.search(r"^###\s*\d+\.\s*(.+)$", texte, re.M)
    nom = m.group(1).strip()
    texte = texte[m.end():]
    m2 = re.search(r"^\*([^*\n]+)\*\s*$", texte, re.M)
    lieu = m2.group(1).strip()
    texte = texte[m2.end():]
    corps = markdown.markdown(texte, extensions=["sane_lists", "attr_list"], output_format="html5")
    # la pièce d'époque en tête de chapitre : le premier bloc de citation
    corps = re.sub(r"^\s*<blockquote>(.*?)</blockquote>",
                   lambda m: '<div class="piece">' + m.group(1) + '</div>', corps,
                   count=1, flags=re.S)
    # classes explicites : Paged.js applique mal les sélecteurs de frères adjacents
    corps = re.sub(r"<hr>\s*<p>", '<hr><p class="suite">', corps)
    corps = re.sub(r"(</div>\s*|^\s*)<p>", lambda m: m.group(1) + '<p class="ouverture">',
                   corps, count=1)
    return (f'<section class="chapitre"><h3><span class="no">{n}</span><span class="nom">{html.escape(nom)}</span></h3>'
            f'<p class="lieu">{html.escape(lieu)}</p>{corps}</section>')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--html", action="store_true")
    args = ap.parse_args()
    fichiers = sorted(TOME.glob("chapitre-*.md"))
    nums = [int(re.search(r"(\d+)", f.stem).group(1)) for f in fichiers]
    # un PDF par partie : chaque chapitre va dans la partie qui le contient
    debuts = sorted(PARTIES)
    groupes = {}
    for n, f in zip(nums, fichiers):
        debut = max(d for d in debuts if d <= n)
        groupes.setdefault(debut, []).append((n, f))
    BUILD.mkdir(exist_ok=True)
    for ancien in BUILD.glob("le-ciel-de-cendre-ch*.*"):  # anciens PDF d'un seul tenant
        ancien.unlink()
    for no, debut in enumerate(debuts, 1):
        if debut not in groupes:
            continue
        chapitres = groupes[debut]
        num, titre = PARTIES[debut]
        corps = [f'<section class="partie"><p class="num">{num}</p><h2>{titre}</h2></section>']
        corps += [chapitre_html(n, f.read_text(encoding="utf-8")) for n, f in chapitres]
        a, b = chapitres[0][0], chapitres[-1][0]
        premiers = f"{a} à {b}" if a != b else str(a)
        nom = f"le-ciel-de-cendre-partie-{no}"
        html_path = BUILD / f"{nom}.html"
        html_path.write_text(GABARIT.format(titre=TITRE, partie=f"{num} : {titre}", premiers=premiers,
                                            date=datetime.date.today().strftime("%d/%m/%Y"),
                                            corps="\n".join(corps)), encoding="utf-8")
        print("HTML :", html_path.relative_to(ROOT))
        if not args.html:
            pdf_path = BUILD / f"{nom}.pdf"
            n = rendre_pdf(html_path, pdf_path)
            print(f"PDF  : {pdf_path.relative_to(ROOT)} ({n} pages)")


if __name__ == "__main__":
    main()
