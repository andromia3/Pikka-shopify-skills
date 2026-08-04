# Audit scripts

Three read-only helpers that turn a live store and its exports into facts the audit reasons about, instead of impressions read off a truncated HTML blob.

**Requirements:** Python 3.8+. Standard library only — nothing to install.

**They are read-only by construction.** GET requests only, no credentials, no form submission, no writes to the store. Redirects are followed manually so the chain stays visible rather than silently resolved.

---

## `seo_fetch.py` — per-URL SEO signals

```bash
python scripts/seo_fetch.py --sample https://store.com     # standard Shopify sample
python scripts/seo_fetch.py URL1 URL2 URL3                 # a chosen URL set
python scripts/seo_fetch.py --file urls.txt                # one URL per line
python scripts/seo_fetch.py --json URL                     # raw JSON
```

**Extracts per URL:** HTTP status, full redirect chain, response time, page weight, `X-Robots-Tag`, title (+ length), meta description (+ length), meta robots, canonical (+ whether it is self-referential), every H1, all hreflang pairs, JSON-LD `@type` values and parse errors, whether crawlable pagination links exist, internal link count, image count and how many lack alt text.

**Options:** `--delay` (default 1.0s between requests), `--timeout` (15s), `--max` (60 URL cap).

**Build the sample to cover every template class:** home, top collections, a filtered/tag collection URL, a paginated `?page=2` URL, products including one collection-scoped `/collections/x/products/y`, blog index, an article, `robots.txt`, `sitemap.xml`, and one URL per locale if the store is international.

**Limits.** It reads server-rendered HTML. Content injected client-side by the theme or by apps will not appear — that is a real signal about what a crawler sees on first pass, but confirm rendered-DOM questions with a browser tool before asserting them. `<title>` inside inline `<svg>` is ignored so payment-icon labels do not masquerade as the page title.

---

## `gsc_report.py` — collapse a Search Console export

```bash
python scripts/gsc_report.py Queries.csv --brand "brandname,brand name"
python scripts/gsc_report.py Pages.csv
python scripts/gsc_report.py export.csv --brand mybrand --top 25
```

A GSC export routinely runs to tens of thousands of rows. This collapses it to:

- **Brand vs non-brand split** — usually the single most telling number in the audit. Requires `--brand`.
- **Striking distance** — queries at position 4-20 with real impressions. Cheaper to move than new pages.
- **Ranking but not clicked** — top-10 positions with CTR under 2%. Usually a title/meta or SERP-feature problem.
- **Cannibalisation clusters** — one query, several URLs. Needs an export carrying **both** Query and Page; the default `Queries.csv` has queries only.
- **Top pages and click concentration** — for `Pages.csv`.

Handles localised GSC headers, `;` or tab delimiters, `%` in CTR, and European decimal commas.

---

## `psi_report.py` — Core Web Vitals

```bash
export PAGESPEED_API_KEY=...          # strongly recommended
python scripts/psi_report.py https://store.com/ https://store.com/collections/x
python scripts/psi_report.py --strategy desktop URL
```

Reports **CrUX field data first** — what real users experienced, which is what Google acts on — and falls back to origin-level field data, then Lighthouse lab metrics, when a URL has too little traffic. Also surfaces total page weight, the heaviest third parties by main-thread blocking time (on Shopify the culprit is usually apps, not the theme), and the top opportunities by estimated saving.

**Get a key.** The anonymous quota is shared globally and is normally exhausted; without `PAGESPEED_API_KEY` you will mostly get HTTP 429. Free key: <https://developers.google.com/speed/docs/insights/v5/get-started>

**Measure mobile** (the default) — Google indexes mobile-first. Each call takes 15-60s, so keep it to the three key templates: home, a top collection, a top product.

---

## Interpreting output

These scripts report **observations, not verdicts**. `canonical_is_self: False` is a fact; whether it is a problem depends on the template and on Shopify's expected behavior for it — see `references/shopify-seo-rules.md`. Feed the output into the analysis tracks; do not paste it into a client deliverable as-is.
