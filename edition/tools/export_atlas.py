"""Exporte les planches et graphiques de l'atlas (cartes/index.html) en PNG haute définition
pour l'édition imprimée, avec leurs titres dans figures/atlas/legendes.json.

- Planches cartographiques : seule la carte (#map-<nom>) est capturée.
- Tableaux de bord (mazout, population, pyramide, métiers) : chaque graphique (.card) est
  capturé à part, sans les éléments interactifs ni les mentions de travail.

Usage : python edition/tools/export_atlas.py [nom ...]
"""
import json
import pathlib
import sys

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "edition" / "figures" / "atlas"
PLATES = ["france", "pacifique", "mediterranee", "sardaigne", "cagliari", "routes", "malte",
          "albanie", "kucova"]
BOARDS = ["mazout", "population"]
PANELS = ["pyramide", "metiers"]  # un graphique dans .chartpanel (la pyramide : une image par année)
PRINT_CSS = """
details.data, p.src, .chips, .tabbar, .loading { display: none !important; }
.card { box-shadow: none !important; }
"""

only = sys.argv[1:] or PLATES + BOARDS + PANELS
OUT.mkdir(parents=True, exist_ok=True)
leg_path = OUT / "legendes.json"
legendes = json.loads(leg_path.read_text(encoding="utf-8")) if leg_path.exists() else {}

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome")
    page = browser.new_page(viewport={"width": 1400, "height": 1000}, device_scale_factor=2.5,
                            color_scheme="light")
    page.goto((ROOT / "cartes" / "index.html").as_uri(), wait_until="networkidle")
    page.add_style_tag(content=PRINT_CSS)
    for t in only:
        page.evaluate(f"document.getElementById('tab-{t}').click()")
        page.wait_for_timeout(2500)
        sec = page.locator(f"#view-{t}")
        if t in PLATES:
            page.locator(f"#map-{t}").screenshot(path=str(OUT / f"{t}.png"))
            legendes[t] = {
                "titre": sec.locator(".legend h2").inner_text(),
                "sous_titre": sec.locator(".legend .meta").inner_text(),
            }
            print("planche", t)
        elif t in PANELS:
            titre = sec.locator(".legend h2").inner_text()
            legendes[t] = {"titre": titre, "sous_titre": sec.locator(".legend .meta").inner_text(),
                           "graphiques": []}
            chips = sec.locator(".chips button")
            n = chips.count()
            for i in range(max(n, 1)):
                if n:
                    chips.nth(i).evaluate("b => b.click()")
                    page.wait_for_timeout(1200)
                label = chips.nth(i).inner_text() if n else ""
                name = f"{t}-{label}" if label else t
                sec.locator(".chartpanel").screenshot(path=str(OUT / f"{name}.png"))
                legendes[t]["graphiques"].append({"fichier": f"{name}.png", "titre": titre,
                                                  "sous_titre": label})
                print("graphique", name)
        else:
            cards = sec.locator(".card")
            legendes[t] = {"titre": sec.locator(".board-head h2").inner_text(), "graphiques": []}
            for i in range(cards.count()):
                c = cards.nth(i)
                name = f"{t}-{i + 1}"
                c.screenshot(path=str(OUT / f"{name}.png"))
                sub = c.locator("p.sub")
                legendes[t]["graphiques"].append({
                    "fichier": f"{name}.png",
                    "titre": c.locator("h3").inner_text(),
                    "sous_titre": sub.inner_text() if sub.count() else "",
                })
                print("graphique", name)
    browser.close()

leg_path.write_text(json.dumps(legendes, ensure_ascii=False, indent=2), encoding="utf-8")
