import { defineConfig } from "astro/config";
import remarkHeadingId from "remark-heading-id";
import remarkEmbeds from "./src/lib/remark-embeds.mjs";

export default defineConfig({
  site: "https://sunelehmann.com",
  trailingSlash: "ignore",
  build: {
    format: "directory",
  },
  markdown: {
    remarkPlugins: [remarkHeadingId, remarkEmbeds],
  },
});
