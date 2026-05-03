# Analytics

The site uses [GoatCounter](https://www.goatcounter.com/) — privacy-friendly, cookieless, no GDPR consent banner needed. Set up and live.

## How to check the numbers

Dashboard: **<https://suneman.goatcounter.com>** (the site code is `suneman`, set in `src/layouts/BaseLayout.astro`).

Login is the email used at signup; password reset works if forgotten. The dashboard shows pageviews by path, referrer, browser, screen size, and country (IP-derived, then the IP is discarded). No cookies, no fingerprinting, no cross-site tracking. Localhost visits are ignored automatically.

## How to turn it off

In `src/layouts/BaseLayout.astro`, set `const GOATCOUNTER_CODE = ""` (empty string). On the next push, GitHub Actions rebuilds and the script tag stops rendering. Setting it back to `"suneman"` re-enables it.

## Pricing

Free for personal / non-commercial sites under ~100k pageviews per month. Nowhere near that ceiling.
