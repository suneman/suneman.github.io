import youtubeMatcher from "@astro-community/astro-embed-youtube/matcher";
import twitterMatcher from "@astro-community/astro-embed-twitter/matcher";
import { visit, SKIP } from "unist-util-visit";

function embedHtmlFor(url) {
  const ytId = youtubeMatcher(url);
  if (ytId) {
    return (
      `<div class="embed embed--youtube">` +
      `<iframe src="https://www.youtube.com/embed/${ytId}" ` +
      `frameborder="0" loading="lazy" ` +
      `allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" ` +
      `allowfullscreen></iframe>` +
      `</div>`
    );
  }

  const twId = twitterMatcher(url);
  if (twId) {
    return (
      `<blockquote class="twitter-tweet" data-dnt="true" data-theme="light">` +
      `<a href="${url}"></a>` +
      `</blockquote>`
    );
  }

  return null;
}

function isEmbeddableUrlLink(node) {
  if (!node || node.type !== "link") return false;
  if (!node.children || node.children.length !== 1) return false;
  const child = node.children[0];
  if (child.type !== "text" || child.value !== node.url) return false;
  return embedHtmlFor(node.url) !== null;
}

function chunkHasContent(children) {
  return children.some((c) => {
    if (c.type === "break") return false;
    if (c.type === "text" && /^\s*$/.test(c.value)) return false;
    return true;
  });
}

function trimEdgeWhitespace(children) {
  let start = 0;
  let end = children.length;
  while (
    start < end &&
    (children[start].type === "break" ||
      (children[start].type === "text" && /^\s*$/.test(children[start].value)))
  ) {
    start++;
  }
  while (
    end > start &&
    (children[end - 1].type === "break" ||
      (children[end - 1].type === "text" &&
        /^\s*$/.test(children[end - 1].value)))
  ) {
    end--;
  }
  return children.slice(start, end);
}

export default function remarkEmbeds() {
  return (tree) => {
    visit(tree, "paragraph", (node, index, parent) => {
      if (!parent || typeof index !== "number") return;
      if (!node.children || node.children.length === 0) return;

      // Quick exit if there are no embeddable URLs in this paragraph at all.
      const hasEmbeddable = node.children.some(isEmbeddableUrlLink);
      if (!hasEmbeddable) return;

      // Walk children, splitting at each embeddable URL link.
      const out = [];
      let buffer = [];
      const flushBuffer = () => {
        const trimmed = trimEdgeWhitespace(buffer);
        if (trimmed.length > 0 && chunkHasContent(trimmed)) {
          out.push({ type: "paragraph", children: trimmed });
        }
        buffer = [];
      };

      for (const child of node.children) {
        if (isEmbeddableUrlLink(child)) {
          flushBuffer();
          out.push({ type: "html", value: embedHtmlFor(child.url) });
        } else {
          buffer.push(child);
        }
      }
      flushBuffer();

      if (out.length === 0) return;
      parent.children.splice(index, 1, ...out);
      return [SKIP, index + out.length];
    });
  };
}
