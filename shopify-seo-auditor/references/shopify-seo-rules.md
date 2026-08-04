# Shopify SEO Rules and Platform Behavior

The platform-specific knowledge that separates a real Shopify SEO audit from generic advice. Verify current behavior against Shopify's docs, since the platform evolves.

## 1. URL structure

Shopify enforces fixed URL prefixes that cannot be removed:

- Products: `/products/<handle>`
- Collections: `/collections/<handle>`
- Pages: `/pages/<handle>`
- Blogs: `/blogs/<blog>/<article>`
- Product within a collection context: `/collections/<collection>/products/<handle>`

**Rule:** The same product is reachable at both `/products/<handle>` and `/collections/<collection>/products/<handle>`. By default Shopify sets the canonical of the collection-scoped URL to the clean `/products/<handle>` URL. Confirm this is intact — themes and apps can break it.

**Rule:** Avoid building internal links to the collection-scoped product URL where possible; prefer the canonical `/products/<handle>` to keep signals consolidated.

## 2. Canonicals

- Shopify outputs `{{ canonical_url }}` in `theme.liquid`. Most well-built themes render a correct self-referential canonical.
- **Risk:** SEO apps or theme edits can override canonicals incorrectly (e.g. pointing every variant or filtered URL to a single page, or stripping canonicals). Always inspect the rendered `<link rel="canonical">` on each template type.
- **Rule:** Variant URLs (`?variant=123`) should canonicalize to the base product URL. Do not let each variant become its own indexable page unless intentionally built as such.

## 3. Pagination

- Shopify paginates collections and blogs with `?page=N`.
- `rel="next"/"prev"` are no longer used by Google as an indexing signal, so the priority is **crawlability**: ensure paginated pages are reachable and that deep products are discoverable.
- **Rule:** Do not canonicalize `?page=2+` to page 1; this can hide deep products from discovery. Let paginated pages self-canonicalize, but keep their titles/meta from being pure duplicates where possible.
- If the theme uses infinite scroll or "load more", verify there are real crawlable `<a href>` paginated links as a fallback.

## 4. Faceted navigation and tag pages

- Filtering is commonly implemented via tag-based URLs (`/collections/<handle>/<tag>`) or query parameters (Storefront filtering: `?filter.v...`).
- **Risk:** Filters can generate a near-infinite number of low-value, thin, duplicate URLs and flood the index / waste crawl budget.
- **Rules:**
  - Decide deliberately which facet pages deserve indexation (those matching real search demand, e.g. "black running shoes") and build them as clean, optimized landing pages.
  - Keep the rest out of the index (avoid internal links into them; use canonical to the parent collection; control parameters).
  - Avoid linking bots into deep filter combinations from the main navigation.

## 5. robots.txt and sitemaps

- `robots.txt` is editable via `robots.txt.liquid`. Shopify ships sensible defaults (it disallows `/cart`, `/checkout`, `/account`, internal search, etc.).
- **Rule:** Only customize `robots.txt.liquid` with a clear reason. A wrong rule can block important sections. Document any customization.
- Sitemaps are auto-generated at `/sitemap.xml` and split into child sitemaps (products, collections, pages, blogs). They include only indexable URLs.
- **Rule:** Submit `/sitemap.xml` in Search Console and verify child sitemaps reflect the live, canonical, indexable URLs.

## 6. Titles, meta, and headings

- Title and meta description are editable per product/collection/page/article in the admin; the theme falls back to defaults if empty.
- **Rule:** Never ship supplier/default titles at scale. Ensure templates don't produce duplicate title patterns across thousands of URLs.
- **Rule:** One H1 per page that matches intent. Many themes mis-assign H1s (logo, section headings) — verify in the rendered HTML.

## 7. Duplicate content sources specific to Shopify

- Supplier/manufacturer product descriptions reused verbatim (common in dropshipping and distribution).
- The collection-scoped vs clean product URL duplication (handled by canonical — verify).
- Tag/filter URLs.
- Internal search results pages if linked or indexable.
- Multiple markets sharing a language (see international).

## 8. Structured data

- Themes often include Product schema; quality varies. Validate with the Rich Results Test.
- **Rule:** Mark up only what is true and visible (price, availability, real reviews). Never inject fake review markup.
- Keep `availability` and `price` in schema consistent with the live PDP.

## 9. International (Shopify Markets)

- Markets can be served via subfolders (`/fr`, `/de`), subdomains, or top-level domains.
- **Rule:** Each localized URL must carry correct, reciprocal `hreflang` (including `x-default`), and canonicals should point within the same market/language, not across markets.
- **Risk:** Two markets sharing a language (e.g. France and Belgium in French) can compete/duplicate. Differentiate or consolidate deliberately.

## 10. Performance and Core Web Vitals

- Shopify hosting is fast, but themes and apps add weight. Heavy apps, render-blocking scripts, and unoptimized images hurt LCP/INP.
- **Rule:** Use Shopify's responsive image filters (`image_url` with `width`), lazy-load below-the-fold media, and audit app script bloat. (Hand depth to `shopify-liquid-reviewer`.)

## 11. Things you cannot change on Shopify (set expectations)

- The `/products/`, `/collections/`, `/pages/`, `/blogs/` URL prefixes are fixed.
- The checkout (on standard plans) is largely controlled by Shopify.
- Some `.liquid` system templates have constraints. Recommend within the platform's reality; do not propose changes the platform doesn't allow.

## 12. Common pitfalls (symptom → likely cause → fix)

Use this table to move from a symptom to the most probable Shopify-specific cause before inventing exotic explanations. Confirm with evidence; don't diagnose from the symptom alone.

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| GSC indexed count is many multiples of the real catalog size | Tag/filter collection URLs self-canonicalizing (theme or app override) and/or internally linked | Restore canonical to the parent collection; stop linking into filter URLs; staged `noindex` only after the canonical fix is measured |
| Organic decline starting 2–6 weeks after a theme redesign or app install | The release silently changed canonicals, pagination, H1s, titles, or removed content | Diff the rendered HTML of each template type against the old version (theme backup, Wayback Machine); restore what changed |
| Products beyond the first page of collections get zero impressions | Infinite scroll / "load more" without crawlable `<a href>` pagination links | Render real `{% paginate %}` links in the HTML even if the UX stays infinite scroll; verify with a JS-disabled crawl |
| Collection page outranked by its own products, or rankings oscillate between near-duplicate URLs | Cannibalization: thin collection page, duplicate title patterns, or indexed facet variants competing with the parent | Differentiate titles/intro copy by intent; consolidate facet variants via canonical; strengthen internal links to the winner |
| PDPs indexed but ranking only on brand + product-name queries | Supplier/manufacturer descriptions reused verbatim across the web | Rewrite descriptions, prioritized by margin and search demand — not alphabetically |
| Rich results (stars, price) suddenly gone | Schema broken by a theme/app update, or review markup with no real reviews | Run Rich Results Test per template type; remove any markup not backed by true, visible data |
| GSC shows "Duplicate, Google chose different canonical" at scale | Internal links pointing to collection-scoped product URLs (`/collections/x/products/y`) or cross-market duplication | Link to `/products/<handle>` everywhere; verify per-market canonicals and hreflang |
| One market's pages missing from its local index, or two markets cannibalize | Non-reciprocal hreflang, or canonicals crossing markets (e.g. `/fr-be/` canonicalizing to `/fr/`) | Verify Markets emits reciprocal hreflang incl. `x-default`; keep canonicals within each market |
| Large "Crawled — currently not indexed" bucket that keeps growing | Quality problem, not a technical one: thin tags, empty collections, boilerplate pages | Consolidate or improve the pages; do not just resubmit sitemaps — Google is declining them, not missing them |
| 404 spike and traffic loss after a catalog cleanup | Deleted products/collections with traffic or backlinks, no redirects | Map each valued deleted URL to its closest live equivalent via URL Redirects; 410 only what genuinely has no successor |

## 13. Decision guides

Apply these instead of a blanket rule. Each ends in an explicit decision, so two auditors reach the same call.

### Should this facet/tag page be indexable?

1. **Demand:** is there real search volume for the exact combination (e.g. "robe soie noire")? No → canonical to parent collection. Done.
2. **Substance:** can the page sustain ≥8–10 relevant products and a unique title/H1/intro? No → canonical to parent.
3. **Competition inside the site:** does an existing collection already target this intent? Yes → strengthen that collection instead.
4. All yes → treat it as a **curated landing page**: unique title/H1/intro copy, linked from the parent collection, exempted from the canonical rule. Keep the allowlist small (single digits per category) and review it quarterly.

### Out-of-stock or discontinued product: keep, redirect, or remove?

1. **Temporary OOS** → keep the page live (200), mark availability in schema, offer back-in-stock capture. Never redirect temporary stock-outs.
2. **Discontinued, has traffic/backlinks, close substitute exists** → 301 to the substitute (a truly comparable product, not the home page).
3. **Discontinued, has traffic/backlinks, no substitute** → 301 to the parent collection, or keep the page with an explanation + alternatives if it earns meaningful traffic.
4. **Discontinued, no traffic, no links** → let it 404/410. Deleting quietly is fine here — value first, sentiment never.

### Several URLs rank for one query: which one owns the intent?

Shopify makes this common — a product, its collection, a tag page, and a blog article can all target "masque led visage".

1. **Identify the intent.** Transactional/category → a collection owns it. Single-product transactional → the PDP owns it. Informational → the article owns it, and links down to the commercial page.
2. **Pick the incumbent.** Prefer the URL already ranking best on the query, not the one you wish ranked. Fighting Google's choice is expensive.
3. **Act on the losers.**
   - Near-duplicate of the winner (facet variant, duplicate collection) → canonical to the winner.
   - Genuinely different intent → differentiate title, H1, and intro copy so they stop overlapping.
   - Thin and redundant → merge into the winner and 301.
4. **Rewire internal links.** Point internal anchors for that intent at the winner. Cannibalisation usually persists because the site keeps sending mixed signals.
5. **Record the decision** so the next audit does not re-litigate it.

### Thin blog article: keep, merge, or remove?

1. Earns clicks, impressions, or backlinks (check 12 months, not 90 days) → **keep and refresh**.
2. No traction but the topic matches catalog intent → **merge** into a hub/guide and 301 the old URL to it.
3. No traction, off-topic or outdated → **unpublish** (404 is acceptable at this value level; redirect only if backlinks exist).
