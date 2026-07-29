# Example Output — Shopify SEO Auditor

A complete, worked example of the deliverable on a **fictional store**. Use it to calibrate depth, tone, and specificity — every finding cites evidence, every recommendation is Shopify-specific and actionable. Do **not** reuse these findings or numbers on a real store; produce your own from the actual data.

**Fictional context used below:** Atelier Nova (`atelier-nova.fr`), a French women's fashion brand on Shopify. 612 products, 47 collections, 128 blog articles. Theme redesigned in November 2025. Data provided: Screaming Frog crawl, 16 months of Search Console, GA4 organic trend. Goal: "recover non-brand organic traffic".

---

## 1. SEO diagnosis

> **Baseline.** Organic sessions are 36,400/month (June 2026), down 21% YoY. The decline is concentrated in non-brand: brand clicks are stable (-2% YoY) while non-brand clicks are down 34% YoY. Traffic is now 62% brand / 38% non-brand — a year ago it was 51/49. GSC reports 6,240 indexed URLs against roughly 810 legitimate canonical URLs (612 products + 47 collections + 128 articles + ~20 pages), plus 7,100 URLs in "Crawled — currently not indexed". The decline begins in the weeks following the November 2025 theme redesign.
>
> **Headline.** Two findings explain most of the problem. (1) Since the redesign, tag-filtered collection URLs (`/collections/robes/noir`, `/collections/robes/soie`…) **self-canonicalize instead of pointing to the parent collection**: the crawl found 13,900 of these thin near-duplicates, and ~5,400 are indexed. They dilute and cannibalize the clean collection pages, which have visibly lost rankings (e.g. "robe en soie": position 6 → 14 since December). (2) The redesign replaced numbered pagination with **infinite scroll without crawlable `<a href>` links**: products beyond the first page load of a collection are no longer discoverable by crawling — 241 products received zero organic clicks in the last 90 days vs 96 a year ago.
>
> **Scope & data used.** Screaming Frog crawl (15,400 URLs, June 2026), GSC performance + coverage (16 months), GA4 organic sessions (24 months). Not available: server logs (crawl-budget analysis is inferred, not measured) and backlink export (link equity to filtered URLs not assessed). Both are flagged as follow-ups, not blockers.

---

## 2. Critical issues

Issues actively costing traffic or revenue. Severity: Critical / High / Medium.

| # | Issue | Area | Severity | Evidence | Impact if unfixed |
| --- | --- | --- | --- | --- | --- |
| 1 | Tag-filtered collection URLs self-canonicalize since the Nov 2025 redesign; 13,900 thin variants crawled, ~5,400 indexed | Canonicals / Faceted nav | Critical | Crawl: `<link rel="canonical">` on `/collections/robes/noir` points to itself, not `/collections/robes`. GSC: indexed count 6,240 vs ~810 legitimate URLs | Continued dilution and cannibalization of collection rankings; "robe en soie" already dropped pos. 6 → 14, same pattern on 11 of the top 20 collections |
| 2 | Infinite scroll with no crawlable pagination links; products beyond the first ~24 items of each collection are undiscoverable by crawl | Indexation / Internal linking | Critical | Theme loads products via JS on scroll; no `<a href="?page=2">` fallback in rendered HTML. GSC: 241 products with 0 organic clicks in 90 days (vs 96 a year ago) | ~40% of the catalog invisible to organic; new products never rank |
| 3 | 187 of 612 products use the supplier's description verbatim (dropship segment), duplicated across competitor sites | Duplicate content | High | Crawl extraction: identical description blocks on 187 PDPs; spot-checked 12, all found word-for-word on 3+ other domains | These PDPs rank only on brand+product queries; the non-brand product long tail is ceded to competitors with the same text and stronger domains |
| 4 | 31 of 47 collections have no intro copy, and title tags follow one duplicate pattern (`<Collection> \| Atelier Nova`) with no intent qualifiers | Collections / Content | High | Crawl: missing/empty collection description on 31 collections; title report shows single pattern across all 47 | Collection pages — the store's main non-brand asset — compete on thin pages; recovery of issue #1 will be partial without content |
| 5 | Product schema emits `aggregateRating` markup from a theme setting although no review app is installed (0 reviews exist) | Structured data | Medium | Rich Results Test on 5 PDPs: rating 4.8/213 reviews hardcoded in theme snippet `product-schema.liquid` | Risk of a structured-data manual action / loss of all rich results; misleading markup |
| 6 | Mobile PDP LCP at 4.3s (CrUX fail); hero image unoptimized, 2 render-blocking app scripts | Performance | Medium | PageSpeed Insights field data on top-3 PDPs: LCP 4.1–4.6s mobile; 480KB hero without `width` param, app scripts loaded in `<head>` | Depressed rankings and conversion on mobile (68% of organic sessions); compounds every other fix |

---

## 3. Technical recommendations

| # | Recommendation | Area | Why | How (Shopify-specific) | Owner |
| --- | --- | --- | --- | --- | --- |
| T1 | Restore canonical from tag-filtered URLs to the parent collection | Canonicals | Removes 13,900 thin duplicates from indexation pressure; re-consolidates signals on the 47 clean collections | In the theme's `theme.liquid` / head snippet: when `current_tags` is present, output `<link rel="canonical" href="{{ collection.url }}">`. Test on 5 collections first, verify in Rich Results/View Source, then roll out. Do **not** add `noindex` in the same release — one change at a time | Dev |
| T2 | Reintroduce crawlable pagination alongside infinite scroll | Indexation | Makes the full catalog discoverable again | Keep the infinite-scroll UX but render real `<a href="{{ paginate.next.url }}">` links inside `{% paginate %}` (hidden visually if needed, present in HTML). Verify with a JS-disabled crawl | Dev |
| T3 | Remove fake review markup | Structured data | Eliminates manual-action risk | Delete the `aggregateRating` block from `snippets/product-schema.liquid`; re-add only when a real review app provides data | Dev |
| T4 | Fix PDP LCP | Performance | Mobile rankings + CVR | Serve the hero via `image_url` with explicit `width`/`widths` + `image_tag` (responsive srcset), `loading="eager"` + `fetchpriority="high"` on the LCP image only; move the 2 app scripts to deferred loading; hand depth to `shopify-liquid-reviewer` | Dev |
| T5 | De-index residual junk once T1 is live and re-crawled | Indexation | Cleans the index faster than canonical alone | After 2–4 weeks of T1: for tag URLs still indexed, evaluate `noindex` via the theme on `current_tags` pages. Staged, reversible, after measurement — not simultaneous with T1 | Dev + SEO |
| T6 | Keep 3–5 high-demand facet pages indexable as curated landing pages | Faceted nav | Real search demand exists for a few combinations (e.g. "robe soie noire", 1,900 srch/mo) | Exempt an allowlist of tag pages from T1's canonical rule; give each unique title/H1/intro copy and link them from the parent collection. Treat them as collections editorially | SEO + Content |

## 4. Content recommendations

| # | Recommendation | Target (collection/product/blog) | Search intent | Action | Owner |
| --- | --- | --- | --- | --- | --- |
| C1 | Write intro copy + differentiated titles for the top 20 collections by revenue | Collections | Commercial ("robe en soie", "jupe midi"…) | 120–200 words of genuinely useful intro (fit, matière, guide) above the grid; title pattern `<Intent qualifier> <Collection> \| Atelier Nova`; unique meta description. Prioritize the 11 collections that lost rankings | Content |
| C2 | Rewrite the 187 supplier descriptions, starting with the 40 highest-margin products | Products | Product long tail | Unique copy: matière, coupe, entretien, porté avec — not spun supplier text. Batch of 20/week | Content |
| C3 | Prune or consolidate thin blog content | Blog | Informational | Of 128 articles, 74 are <200-word lookbook posts with 0 clicks/90d: consolidate into seasonal guides or unpublish. Keep and refresh the 12 articles that still earn clicks | Content |
| C4 | Build 4 guide pages targeting commercial-investigation queries feeding the top collections | Blog / Pages | Commercial-investigation ("comment choisir une robe en soie") | One guide per top category, internally linked to the collection and its curated facet pages (T6) | Content |

---

## 5. Priority matrix (impact vs effort)

| | Low effort | High effort |
| --- | --- | --- |
| **High impact** | T1 canonical fix · T3 fake schema removal · T2 crawlable pagination | C1 collection content · C2 description rewrites |
| **Low impact** | T5 residual noindex (sequenced) · C3 blog pruning | C4 guides · T6 facet landing pages |

Ranked shortlist:

| Rank | Item | Impact (1-5) | Effort (1-5) | Type (Tech/Content) |
| --- | --- | --- | --- | --- |
| 1 | T1 Canonical on tag-filtered URLs | 5 | 2 | Tech |
| 2 | T2 Crawlable pagination | 5 | 2 | Tech |
| 3 | T3 Remove fake review markup | 3 | 1 | Tech |
| 4 | C1 Top-20 collection copy + titles | 4 | 3 | Content |
| 5 | T4 PDP LCP fix | 3 | 3 | Tech |
| 6 | C2 Supplier description rewrites (first 40) | 3 | 4 | Content |
| 7 | T6 Curated facet landing pages | 2 | 3 | Tech+Content |
| 8 | T5 Residual noindex pass | 2 | 2 | Tech |
| 9 | C3 Blog pruning | 2 | 2 | Content |
| 10 | C4 Commercial guides | 2 | 4 | Content |

---

## 6. Implementation checklist

Ordered so dependencies come first (canonical/indexation before content scale-up; one indexation change at a time).

- [ ] Week 1 — Dev — Ship T1 canonical fix on 5 test collections; verify rendered canonical + no layout regression. **Done =** canonical of `/collections/robes/noir` points to `/collections/robes` in live HTML.
- [ ] Week 1 — Dev — Ship T3 (remove `aggregateRating`). **Done =** Rich Results Test shows no review markup on PDPs.
- [ ] Week 2 — Dev — Roll T1 to all collections (minus T6 allowlist); request recrawl of top collections in GSC. **Done =** spot-check of 20 tag URLs all canonicalize to parent.
- [ ] Week 2 — Dev — Ship T2 crawlable pagination. **Done =** JS-disabled crawl reaches 100% of products in the 5 largest collections.
- [ ] Week 3 — Content — C1 batch 1: 10 collections (the 11 that lost rankings first). **Done =** unique title, meta, H1, ≥120-word intro live.
- [ ] Week 3 — Dev — T4 LCP fixes on the PDP template. **Done =** lab LCP <2.5s on top-3 PDPs, field data monitored.
- [ ] Week 4–6 — Content — C1 batch 2 (10 collections) + C2 batches of 20 products/week.
- [ ] Week 6 — SEO — Review GSC coverage: indexed count should be trending from 6,240 toward ~900. Decide T5 (residual noindex) based on the curve, not the calendar.
- [ ] Week 6–8 — SEO + Content — T6: build the 3–5 curated facet pages with unique content; add internal links from parent collections.
- [ ] Week 8+ — Content — C3 blog consolidation, then C4 guides.

**Validation after changes:** re-crawl after each technical release; watch GSC coverage weekly (indexed count and "Crawled — currently not indexed"); track the 11 affected collection queries in a rank tracker; compare non-brand clicks 28d vs prior 28d from week 4. Expected shape: indexed-count decline within 2–4 weeks, ranking recovery on collections within 4–10 weeks. If indexed count hasn't moved by week 6, escalate T5.

---

*End of example. Note what makes this credible: a single coherent narrative (redesign → canonical break → dilution → non-brand decline), numbers that reconcile with each other, evidence cited for every finding, Shopify-specific fixes (Liquid constructs, `current_tags`, `paginate`, `image_url`), sequencing that respects dependencies, and honest gaps (no server logs, no backlink data) stated up front.*
