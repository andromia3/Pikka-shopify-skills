# Performance Rules

What to inspect for theme performance and Core Web Vitals. Tie findings to a metric (LCP, INP, CLS) where possible.

## 1. Core Web Vitals targets

- **LCP (Largest Contentful Paint)** < 2.5s — usually the hero image or main product image.
- **INP (Interaction to Next Paint)** < 200ms — responsiveness; hurt by heavy JS / long tasks.
- **CLS (Cumulative Layout Shift)** < 0.1 — caused by images without dimensions, injected content, late fonts.

## 2. Image handling

- Use Shopify's image filters: `image_url: width: 800` (+ responsive `srcset`/`sizes`) and `image_tag`, not raw full-size images.
- Set explicit `width`/`height` (or aspect ratio) to prevent CLS.
- `loading="lazy"` for below-the-fold images; **not** for the LCP/hero image (load it eagerly, consider `fetchpriority="high"` / preload).
- Serve modern formats; let Shopify's CDN handle sizing/format. Avoid oversized PNGs where a sized WebP/JPEG works.
- Avoid background-image hacks for important imagery (harder for the browser to prioritize).

## 3. Liquid rendering efficiency

- Avoid expensive loops over large collections in templates (e.g. looping all products to compute something). Paginate or precompute.
- Don't call costly operations repeatedly; `assign` once and reuse.
- Avoid dumping huge `| json` blobs into the DOM.
- Minimize nested loops, especially across `collections`/`products`/`variants`.

## 4. JavaScript

- **Weight and blocking.** Flag large bundles, render-blocking `<script>` in `<head>` without `defer`/`async`, and synchronous third-party scripts.
- **Defer non-critical JS.** Use `defer`/`async`; load below-the-fold/interaction-only code lazily.
- **Avoid jQuery and heavy libraries** if the theme only needs small vanilla helpers.
- **INP.** Long tasks, excessive event listeners, and layout thrashing hurt responsiveness. Flag heavy work on the main thread.
- **Duplicate listeners** from section re-rendering in the editor (re-init/cleanup on `shopify:section:load/unload`).

## 5. CSS

- **Bloat.** Flag large, unused CSS shipped on every page. Split or scope CSS to where it's used.
- **Critical CSS** in `<head>`; defer the rest where possible.
- Avoid heavy frameworks shipping thousands of unused utility classes.
- Watch for `@import` chains and many separate stylesheet requests.

## 6. Apps and third-party scripts

- App scripts are the most common cause of slow Shopify themes. Inventory app embeds/blocks and the scripts they inject.
- Flag apps that load synchronously, run on every page (even where unused), or duplicate functionality.
- Recommend removing leftover scripts from uninstalled apps.
- Note: many third-party tags (reviews, chat, popups, analytics) compound; quantify the count and weight.

## 7. Fonts

- Limit font families/weights; use `font-display: swap` to avoid invisible text and reduce CLS.
- Prefer Shopify-hosted/system fonts or preloaded self-hosted fonts over multiple external font requests.

## 8. Measurement

- Recommend measuring with Lighthouse (lab) and field data (Chrome UX Report / Web Vitals), on **mobile** and on representative templates (home, collection, PDP).
- Always compare against a baseline; attribute regressions to specific changes/apps.

## 9. Performance findings format

For each finding, capture: the file/asset, the metric affected (LCP/INP/CLS), the estimated cost (e.g. "blocking 600ms script"), and the fix. Prioritize the few changes that move LCP/INP most before micro-optimizations.
