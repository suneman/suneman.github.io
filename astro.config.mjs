import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";
import remarkHeadingId from "remark-heading-id";
import remarkEmbeds from "./src/lib/remark-embeds.mjs";

export default defineConfig({
  site: "https://sunelehmann.com",
  trailingSlash: "ignore",
  build: {
    format: "directory",
  },
  integrations: [sitemap()],
  markdown: {
    remarkPlugins: [remarkHeadingId, remarkEmbeds],
  },
});
