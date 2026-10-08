// Moves the GFM footnotes section under a "## Notes" heading, when a post has one.
//
// remark-rehype always appends the footnotes as the last block of the document
// (a <section data-footnotes class="footnotes"> with a visually hidden
// "Footnotes" heading). A post that wants something *after* its notes, say an
// appendix, cannot get it there from markdown alone. If the post contains an
// <h2> whose text is exactly "Notes", this plugin lifts the footnotes section
// out of the tail and inserts it directly after that heading, dropping the
// section's own hidden heading so the page does not announce "Notes" twice.
//
// Posts without a "Notes" heading, or without footnotes, are untouched.

function textOf(node) {
  if (!node) return "";
  if (node.type === "text") return node.value;
  if (!node.children) return "";
  return node.children.map(textOf).join("");
}

function isFootnotesSection(node) {
  if (node.type !== "element" || node.tagName !== "section") return false;
  const props = node.properties || {};
  if (props.dataFootnotes !== undefined) return true;
  const cls = props.className;
  return Array.isArray(cls) ? cls.includes("footnotes") : cls === "footnotes";
}

function isNotesHeading(node) {
  return (
    node.type === "element" &&
    node.tagName === "h2" &&
    textOf(node).trim() === "Notes"
  );
}

export default function rehypeNotesPlacement() {
  return (tree) => {
    const kids = tree.children;
    if (!Array.isArray(kids)) return;

    const sectionIndex = kids.findIndex(isFootnotesSection);
    if (sectionIndex === -1) return;
    const headingIndex = kids.findIndex(isNotesHeading);
    if (headingIndex === -1 || headingIndex > sectionIndex) return;

    const [section] = kids.splice(sectionIndex, 1);
    section.children = (section.children || []).filter(
      (c) =>
        !(
          c.type === "element" &&
          /^h[1-6]$/.test(c.tagName) &&
          textOf(c).trim() === "Footnotes"
        ),
    );
    kids.splice(headingIndex + 1, 0, section);
  };
}
