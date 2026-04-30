import rss from "@astrojs/rss";
import { getCollection } from "astro:content";

export async function GET(context) {
  const posts = (await getCollection("posts", ({ data }) => data.status === "publish"))
    .sort((a, b) => b.data.date.getTime() - a.data.date.getTime());

  return rss({
    title: "sunelehmann.com — intermittent updates",
    description:
      "Sune Lehmann's personal blog. Networks, complexity, computational social science, and assorted asides.",
    site: context.site,
    items: posts.map((post) => {
      const slug = post.data.slug ?? post.id;
      return {
        title: post.data.title,
        pubDate: post.data.date,
        link: `/blog/${slug}/`,
        content: post.body,
        categories: post.data.categories,
      };
    }),
    customData: "<language>en-us</language>",
  });
}
