#!/usr/bin/env node
// Refresh src/data/popular-posts.json from the GoatCounter stats API.
//
// Writes the top blog posts by pageviews over the trailing RANGE_MONTHS,
// plus the current month stamp. The month stamp changes once a month even
// when the ranking doesn't, which is what guarantees the weekly CI run
// commits (and therefore rebuilds the site) at least once per month so the
// homepage's archive pick rotates.
//
// Token: GOATCOUNTER_TOKEN env var, or ~/.config/goatcounter-token.

import { readFileSync, writeFileSync } from "node:fs";
import { homedir } from "node:os";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const SITE = "https://suneman.goatcounter.com";
const RANGE_MONTHS = 3;
const TOP_N = 10; // keep spares so the homepage can skip duplicate slugs
const OUT = join(dirname(fileURLToPath(import.meta.url)), "..", "src", "data", "popular-posts.json");

function token() {
  if (process.env.GOATCOUNTER_TOKEN) return process.env.GOATCOUNTER_TOKEN.trim();
  try {
    return readFileSync(join(homedir(), ".config", "goatcounter-token"), "utf8").trim();
  } catch {
    console.error("No token: set GOATCOUNTER_TOKEN or create ~/.config/goatcounter-token");
    process.exit(1);
  }
}

async function api(path, params) {
  const url = `${SITE}/api/v0/${path}?` + new URLSearchParams(params);
  // The hosted API intermittently returns 4xx for valid requests; retry.
  for (let attempt = 0; ; attempt++) {
    const resp = await fetch(url, { headers: { Authorization: `Bearer ${token()}` } });
    if (resp.ok) return resp.json();
    if (attempt === 3) {
      console.error(`API error ${resp.status} on ${url}: ${(await resp.text()).slice(0, 300)}`);
      process.exit(1);
    }
    await new Promise((r) => setTimeout(r, 1000 * (attempt + 1)));
  }
}

function isPost(path) {
  const parts = path.replace(/^\/+|\/+$/g, "").split("/");
  return parts.length === 2 && parts[0] === "blog";
}

const end = new Date();
const start = new Date(end);
start.setDate(start.getDate() - RANGE_MONTHS * 30);
const day = (d) => d.toISOString().slice(0, 10);

const posts = [];
const seenIds = [];
while (posts.length < TOP_N) {
  const params = { start: day(start), end: day(end), limit: "100" };
  if (seenIds.length) params.exclude_paths = seenIds.join(",");
  const data = await api("stats/hits", params);
  const hits = data.hits ?? [];
  for (const h of hits) {
    seenIds.push(h.path_id);
    if (isPost(h.path)) posts.push(h);
  }
  if (!data.more || hits.length === 0) break;
}

posts.sort((a, b) => b.count - a.count);

const out = {
  month: day(end).slice(0, 7),
  range: { start: day(start), end: day(end), months: RANGE_MONTHS },
  posts: posts.slice(0, TOP_N).map((h) => ({
    slug: h.path.replace(/^\/+|\/+$/g, "").split("/")[1],
    count: h.count,
  })),
};

writeFileSync(OUT, JSON.stringify(out, null, 2) + "\n");
console.log(`Wrote ${OUT}: top ${out.posts.length} posts, ${out.range.start} → ${out.range.end}`);
