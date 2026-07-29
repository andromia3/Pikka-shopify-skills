# Shopify SEO Audit Checklist

Work through every area. For each item, record: **Status** (Pass / Issue / Critical), **Evidence** (URL, crawl finding, GSC number), and **Fix**.

## 1. Collections
- [ ] Each important collection has a unique, intent-matched title tag and meta description.
- [ ] Collection pages have unique, useful intro copy (not empty, not boilerplate, not duplicated across collections).
- [ ] H1 matches the collection topic and search intent.
- [ ] Collection URLs are clean and stable (`/collections/<handle>`), not auto-generated junk.
- [ ] Important collections are reachable within a few clicks from the home page.
- [ ] Empty or near-empty collections are not indexable revenue-thin pages.
- [ ] Default product sort and curation surface relevant products (helps engagement signals).

## 2. Product pages
- [ ] Unique title tags and meta descriptions per product (not supplier defaults).
- [ ] Product descriptions are unique, not copy-pasted from the manufacturer/supplier across the web.
- [ ] One clear H1 (the product name) per page.
- [ ] Images have descriptive alt text.
- [ ] Canonical points to the product's canonical URL, not a collection-scoped variant (see `shopify-seo-rules.md`).
- [ ] Out-of-stock / discontinued product handling is defined (keep, redirect, or noindex with intent).

## 3. Internal linking
- [ ] Collections link to relevant sub-collections and key products.
- [ ] Products link to related products / parent collections.
- [ ] Blog content links to relevant collections/products with descriptive anchors.
- [ ] Important pages are not orphaned (reachable from navigation or contextual links).
- [ ] Link equity flows to priority pages, not diluted across low-value tag pages.

## 4. Duplicate content
- [ ] Supplier-fed product descriptions are rewritten or differentiated.
- [ ] Filtered/sorted collection URLs do not create indexable duplicates.
- [ ] The same product under multiple collections does not create duplicate indexable URLs (canonical strategy in place).
- [ ] No `http`/`https` or `www`/non-`www` duplication; one canonical host.
- [ ] Tag pages and search results pages are not generating thin duplicate content in the index.

## 5. Canonical tags
- [ ] Products served under `/collections/.../products/...` canonicalize to `/products/...`.
- [ ] Filtered collection URLs canonicalize to the clean collection URL (where appropriate).
- [ ] No accidental cross-canonicalization (e.g. all products canonicalizing to one URL).
- [ ] Canonicals are self-referential on primary pages.
- [ ] Any app- or theme-injected canonical overrides are intentional and correct.

## 6. Indexation
- [ ] Search Console coverage: count of valid vs excluded; investigate spikes.
- [ ] No important pages blocked by `robots.txt` or `noindex`.
- [ ] No index bloat from filters, tags, search, or cart/account URLs.
- [ ] `robots.txt` customizations (via `robots.txt.liquid`) are intentional and safe.
- [ ] XML sitemaps (`/sitemap.xml`) submitted and reflect current, indexable URLs.

## 7. Pagination
- [ ] Paginated collection URLs (`?page=2`) are crawlable so deep products are discoverable.
- [ ] Pagination does not create thin duplicate title/meta across pages.
- [ ] Paginated pages are not canonicalized to page 1 (which can hide deep products).
- [ ] Consider load-more/infinite scroll implications: ensure crawlable links exist.

## 8. Faceted navigation
- [ ] Filter/facet URLs (color, size, price, tag-based) are controlled — not flooding the index.
- [ ] Valuable facet combinations that match real search demand are handled deliberately (indexable landing pages); the rest are kept out of the index.
- [ ] Filters do not generate infinite crawl paths (parameter combinations).
- [ ] Internal links do not point bots into low-value facet URLs at scale.

## 9. Structured data
- [ ] Product schema present and valid (name, image, description, offers, price, availability).
- [ ] Review/rating schema only when reviews genuinely exist (no fake markup).
- [ ] BreadcrumbList schema present and matches the visible breadcrumb.
- [ ] Organization/Website schema on the home page.
- [ ] No schema errors in Search Console / Rich Results Test.

## 10. Blog / content strategy
- [ ] Blog targets informational and commercial-investigation queries relevant to the catalog.
- [ ] Articles link to relevant collections/products.
- [ ] No thin, outdated, or duplicate articles dragging quality down.
- [ ] Content is organized by topic; key topics have a hub/cluster structure.
- [ ] Author/freshness signals where relevant.

## 11. Migration risks
- [ ] If the store recently migrated or changed URLs, redirects are in place and resolve 200 (not chained or broken).
- [ ] Legacy URLs with backlinks/traffic are preserved or redirected. (Hand deep migration work to `shopify-migration-seo-guardian`.)
- [ ] Recent indexation/traffic drops are checked against any structural change.

## 12. International SEO (if relevant)
- [ ] Markets configured correctly (Shopify Markets) with the right domains/subfolders.
- [ ] `hreflang` annotations are present, reciprocal, and correct for each locale.
- [ ] No duplicate-content conflicts between markets sharing a language.
- [ ] Currency/language switching does not create crawl traps or cloaking.
- [ ] Correct canonical strategy per market.

---

## Scoring anchors for the priority matrix

Use these anchors when scoring issues, so two runs of the audit produce comparable scores. Score what the evidence supports, not what feels urgent.

**Impact (1–5)**

| Score | Anchor |
| --- | --- |
| 5 | Affects >20% of organic traffic or an entire template class sitewide (all collections, all PDPs); or actively suppressing indexation/discovery of a large share of the catalog |
| 4 | Affects a major template class or the top revenue-driving pages (top collections / top landing pages) |
| 3 | Affects a meaningful segment (a category, a market, a subset of pages/queries) |
| 2 | Affects individual pages or a marginal query set |
| 1 | Hygiene/cosmetic; no measurable traffic path |

**Effort (1–5)**

| Score | Anchor |
| --- | --- |
| 1 | Under half a day; admin/config or one-line theme change; no release risk |
| 2 | A few days; one template or one content batch; low regression risk |
| 3 | 1–2 weeks; multiple templates or cross-team (dev + content) |
| 4 | Multi-week sustained effort (content at scale, structural internal-linking work) |
| 5 | Project-level: architecture change, migration-adjacent, or heavy custom development |

**Tie-breakers.** At equal score, prefer: lower risk (a canonical mistake can deindex revenue pages — see Quality rules), faster time-to-impact, and dependency order (indexation fixes before content scale-up). State the tie-breaker used.
