# Redirect Mapping Framework

How to map every valued old URL to its best new Shopify destination, plus the rules and edge cases that prevent traffic loss.

## 1. Core principles

- **301 (permanent)** for every URL that moves and still has a relevant destination.
- **Map to the closest equivalent**, not the home page. Bulk-redirecting everything to the home page destroys rankings and looks like soft-404s to Google.
- **Single hop.** Redirect directly to the final live URL. No chains (A->B->C) and no loops.
- **410 (Gone)** for content that is genuinely retired with no equivalent — this is cleaner than a 404 and tells search engines it's intentional.
- **Preserve the redirect for the long term.** Don't remove redirects after a few weeks; backlinks and bookmarks persist for years.

## 2. Mapping by content type

### Products
- Old product URL -> new `/products/<handle>`.
- Keep handles consistent with old slugs where it simplifies pattern-based mapping.
- Discontinued products: redirect to the closest in-stock alternative or the parent collection; if nothing fits, 410.

### Categories -> Collections
- Old category URL -> new `/collections/<handle>`.
- Merge/split categories: map to the collection that best matches the old page's intent. Document merges (many old -> one new).

### CMS pages
- Old `/about`, `/shipping`, etc. -> new `/pages/<handle>`.

### Blog / articles
- Old article URL -> new `/blogs/<blog>/<article>`.
- Preserve high-traffic articles; consolidate thin ones into stronger pages with redirects.

### Filter / parameter / faceted URLs
- Decide which had real organic value. Map valuable ones to the equivalent Shopify collection (or a curated collection). Let the rest resolve to the parent collection.
- Do not attempt to recreate infinite filter combinations.

### Pagination
- Old `?page=N` URLs generally map to the parent collection; Shopify handles its own pagination.

## 3. Mapping methods

1. **Pattern-based (rules).** When old and new follow predictable patterns, define regex/rules (e.g. `/product/{slug}` -> `/products/{slug}`). Fast and scalable.
2. **Exact (one-to-one).** For high-value URLs, map explicitly in a table. Always do this for the top pages by clicks/backlinks.
3. **Hybrid.** Use rules for the long tail, explicit maps for the priority list. This is the usual approach.

**Validation:** after generating the map, crawl the *old* URL list through the redirects and confirm each returns a single 301 to a live 200 page. Flag any 404, 5xx, chain, or loop.

## 4. The mapping table

| old_url | type | organic_clicks | backlinks | new_url | redirect_type | status | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [ ] | product | [ ] | [ ] | [ ] | 301 | validated | [ ] |
| [ ] | category | [ ] | [ ] | [ ] | 301 | validated | merged |
| [ ] | blog | [ ] | [ ] | [ ] | 301 | pending | [ ] |
| [ ] | retired | [ ] | [ ] | — | 410 | n/a | no equivalent |

## 5. Implementing redirects on Shopify

- Shopify supports URL redirects in the admin (`Online Store > Navigation > URL Redirects`) and bulk import via CSV.
- For large or rule-based maps, use bulk CSV import and/or a reputable redirect app; review entries before applying.
- Shopify cannot redirect from URL prefixes it doesn't own; ensure the domain points to Shopify so the redirects take effect.
- **Safety:** export the current redirect list before any bulk change so you can roll back. Never bulk-delete redirects without a backup and confirmation.

## 6. Edge cases and gotchas

- **Trailing slashes / case sensitivity:** normalize and test both forms.
- **Query strings:** decide whether redirects should ignore or preserve parameters.
- **Old domain change at the same time:** chain risk multiplies; redirect old domain -> new canonical URL directly.
- **HTTPS / www consolidation:** ensure one canonical host; redirect the rest.
- **Internal links:** update internal links to point to final new URLs, not through redirects.
