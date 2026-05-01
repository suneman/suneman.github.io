# Analytics

The site uses [GoatCounter](https://www.goatcounter.com/) — a privacy-friendly,
cookieless web analytics service that's free for non-commercial use. No GDPR
consent banner is required because no personal data is stored.

## How it's wired in

A single `<script>` tag in `src/layouts/BaseLayout.astro` loads the GoatCounter
beacon on every page. The site code (the subdomain you pick at signup) is held
in one constant near the top of that file:

```js
const GOATCOUNTER_CODE = "";
```

While `GOATCOUNTER_CODE` is empty, no script is rendered and no requests go to
GoatCounter. Drop in your code and rebuild — that's the whole switch.

## Sign up (one-time, ~3 minutes)

1. Visit <https://www.goatcounter.com/signup>.
2. Pick a **site code** — this becomes the subdomain of your dashboard, e.g.
   `sunelehmann` → `sunelehmann.goatcounter.com`. Keep it short; it ends up in
   every page's HTML.
3. Set the **site domain** to `sunelehmann.com`.
4. Use your DTU email (or any email you'll remember). No credit card.
5. Confirm the signup email.

GoatCounter will show you an example `<script>` tag on the dashboard. You don't
need to copy that — the script is already in `BaseLayout.astro`. You just need
the site code.

## Turn it on

1. Open `src/layouts/BaseLayout.astro`.
2. Set the constant to your chosen code:
   ```js
   const GOATCOUNTER_CODE = "sunelehmann";
   ```
3. Commit and push to `main`. GitHub Actions will rebuild and deploy.
4. Load the live site once, then check
   `https://sunelehmann.goatcounter.com` — you should see one pageview.

## Turn it off

Set `GOATCOUNTER_CODE` back to `""` and push. The script tag stops rendering
on the next build.

## What gets tracked

- Path, referrer, browser, screen size, country (from IP, then the IP is
  discarded).
- No cookies, no fingerprinting, no cross-site tracking, no personal data.
- Localhost visits are ignored automatically, so `npm run dev` won't pollute
  the numbers.

## Pricing

Free for personal / non-commercial sites under ~100k pageviews per month. This
site will not come close to that ceiling. If GoatCounter ever asks you to move
to a paid plan, the dashboard will tell you well in advance.

## Alternatives, if GoatCounter ever stops fitting

- **Cloudflare Web Analytics** — also free and cookieless; needs a Cloudflare
  account; slightly nicer dashboard.
- **Plausible (self-hosted)** — open source, more features, but you have to
  run a server. Overkill for this site.
- **Umami (self-hosted or hosted free tier)** — similar tradeoff to Plausible.
