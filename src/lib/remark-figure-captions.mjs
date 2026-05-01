import { visit, SKIP } from "unist-util-visit";

// Promotes a markdown image with both alt text and a title attribute,
// when it sits alone in its paragraph, into a <figure>/<figcaption> pair.
//
//   ![Alt for screen readers](/img.jpg "Visible caption")
//
// becomes
//
//   <figure>
//     <img src="/img.jpg" alt="Alt for screen readers" />
//     <figcaption>Visible caption</figcaption>
//   </figure>
//
// Images without a title (the common case) are left as plain <img>.
// Images without alt are also left alone — this is intentional so that
// legacy WordPress-imported posts whose images carry vestigial title
// attributes but empty alts don't suddenly sprout captions.

function isWhitespaceOrBreak(node) {
  if (node.type === "break") return true;
  if (node.type === "text" && /^\s*$/.test(node.value)) return true;
  return false;
}

function escapeAttr(s) {
  return String(s)
    .replace(/&/g, "&amp;")
    .replace(/"/g, "&quot;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

function escapeText(s) {
  return String(s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

export default function remarkFigureCaptions() {
  return (tree) => {
    visit(tree, "paragraph", (node, index, parent) => {
      if (!parent || typeof index !== "number") return;
      if (!node.children || node.children.length === 0) return;

      const meaningful = node.children.filter((c) => !isWhitespaceOrBreak(c));
      if (meaningful.length !== 1) return;

      const img = meaningful[0];
      if (img.type !== "image") return;
      if (!img.title) return;
      if (!img.alt) return;

      const figureHtml =
        `<figure>` +
        `<img src="${escapeAttr(img.url)}" alt="${escapeAttr(img.alt)}" />` +
        `<figcaption>${escapeText(img.title)}</figcaption>` +
        `</figure>`;

      parent.children.splice(index, 1, { type: "html", value: figureHtml });
      return [SKIP, index + 1];
    });
  };
}
