// Répète l'en-tête (thead) des tableaux coupés entre deux pages.
// Adapté du gestionnaire « RepeatingTableHeaders » diffusé par la communauté Paged.js.
class RepeterEntetes extends Paged.Handler {
  constructor(chunker, polisher, caller) {
    super(chunker, polisher, caller);
    this.coupes = [];
  }

  afterPageLayout(pageElement, page, breakToken, chunker) {
    this.chunker = chunker;
    this.coupes = [];
    if (!breakToken) return;
    const node = breakToken.node;
    const tables = this.ancetres(node, "table");
    if (node.tagName === "TABLE") tables.push(node);
    if (!tables.length) return;
    this.coupes = tables.map((t) => t.dataset.ref);
    const thead = node.tagName === "THEAD" ? node : this.premierAncetre(node, "thead");
    if (thead) {
      const dernier = thead.hasChildNodes() ? thead.lastChild : thead;
      breakToken.node = this.noeudApres(dernier, chunker.source);
    }
    this.masquerVides(pageElement, node);
  }

  layout(rendered) {
    this.coupes.forEach((ref) => {
      const rendu = rendered.querySelector("[data-ref='" + ref + "']");
      if (!rendu || rendu.getAttribute("entetes-repetees")) return;
      const source = this.chunker.source.querySelector("[data-ref='" + ref + "']");
      const thead = source && source.querySelector("thead");
      if (thead) rendu.insertBefore(thead.cloneNode(true), rendu.firstChild);
      rendu.setAttribute("entetes-repetees", "1");
    });
  }

  masquerVides(pageElement, noeudCoupe) {
    this.coupes.forEach((ref) => {
      const table = pageElement.querySelector("[data-ref='" + ref + "']");
      if (!table) return;
      const ligne = table.querySelector("tbody > tr");
      if (!ligne || (ligne.firstElementChild && noeudCoupe.dataset &&
          ligne.firstElementChild.dataset.ref === noeudCoupe.dataset.ref)) {
        table.style.visibility = "hidden";
        table.style.position = "absolute";
      }
    });
  }

  premierAncetre(el, sel) {
    while (el.parentNode && el.parentNode.nodeType === 1) {
      if (el.parentNode.matches(sel)) return el.parentNode;
      el = el.parentNode;
    }
    return null;
  }

  ancetres(el, sel) {
    const out = [];
    while (el.parentNode && el.parentNode.nodeType === 1) {
      if (el.parentNode.matches(sel)) out.unshift(el.parentNode);
      el = el.parentNode;
    }
    return out;
  }

  noeudApres(node, limite) {
    if (limite && node === limite) return;
    let s = this.suivant(node);
    if (s) return s;
    while ((node = node.parentNode)) {
      if (limite && node === limite) return;
      s = this.suivant(node);
      if (s) return s;
    }
  }

  suivant(n) {
    while ((n = n.nextSibling)) {
      if (!(n.nodeType === 8 || (n.nodeType === 3 && !/[^\t\n\r ]/.test(n.textContent)))) return n;
    }
    return null;
  }
}
Paged.registerHandlers(RepeterEntetes);
