import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const posts = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/posts" }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    slug: z.string().optional(),
    status: z.string().default("publish"),
    author: z.string().optional(),
    categories: z.array(z.string()).default([]),
    tags: z.array(z.string()).default([]),
    images: z.array(z.string()).default([]),
    original_url: z.string().optional(),
  }),
});

const pages = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/pages" }),
  schema: z.object({
    title: z.string(),
    slug: z.string().optional(),
    status: z.string().default("publish"),
    date: z.coerce.date().optional(),
    author: z.string().optional(),
    original_url: z.string().optional(),
  }),
});

// Featured publications. One markdown file per paper:
// frontmatter holds the metadata, the body is the blurb.
// Order on the page is by `year` desc, then file order.
const papers = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/papers" }),
  schema: z.object({
    slug: z.string(),
    title: z.string(),
    authors: z.string(),
    venue: z.string(),
    year: z.number(),
    pdf: z.string().optional(),
    thumb: z.string().optional(),
    links: z
      .array(
        z.object({
          label: z.string(),
          href: z.string(),
        })
      )
      .default([]),
  }),
});

export const collections = { posts, pages, papers };
