# Migration Risk, URL Inventory, and Pre-launch Checklist

## 1. Risk assessment

Score each factor (Low / Medium / High). The overall risk is driven by the highest factors.

| Factor | Low | Medium | High |
| --- | --- | --- | --- |
| URL change scope | Same URLs preserved | Some patterns change | All URLs change (typical platform switch) |
| Traffic concentration | Spread across many pages | Mixed | A few pages drive most organic traffic |
| Backlink exposure | Few external links | Moderate | Many high-value backlinks to specific URLs |
| Catalog size | Small (< 200 URLs) | Medium | Large (thousands of URLs) |
| International | Single market | 2 markets | Many markets / hreflang clusters |
| Content parity | Content preserved | Partial | Major content/IA redesign at the same time |
| Timeline | Generous, with staging | Tight | Hard deadline, no staging validation |

**Rule:** Migrating platform *and* redesigning IA *and* changing content simultaneously multiplies risk. Where possible, separate these changes in time so you can attribute any drop.

## 2. URL inventory method

Build one master list of old URLs from multiple sources, because no single source is complete:

1. **Full crawl** of the old site (Screaming Frog / Sitebulb).
2. **XML sitemaps** of the old site.
3. **Search Console**: Pages report (last 12-16 months) — captures URLs that get impressions/clicks even if not in the crawl.
4. **Analytics**: top organic and overall landing pages.
5. **Backlink export** (Ahrefs / Semrush / GSC Links): URLs that receive external links.
6. **Server logs** if available: URLs Googlebot actually requests.

Deduplicate into a master sheet with columns: `old_url`, `status_code`, `type` (product/category/cms/blog/other), `organic_clicks`, `backlinks`, `conversions`, `keep?`, `new_url`, `redirect_type`, `notes`.

**Prioritize** by clicks + backlinks + conversions. The top of this list must be perfect.

## 3. Metadata and content preservation

- [ ] Title tags mapped/migrated per URL (not reverted to Shopify defaults).
- [ ] Meta descriptions migrated.
- [ ] H1s preserved or improved (one per page).
- [ ] Unique product and category copy migrated (don't drop to supplier defaults).
- [ ] Image alt text preserved.
- [ ] Structured data re-implemented on Shopify (Product, Breadcrumb, Organization).
- [ ] Blog content and publish dates preserved; internal links updated to new URLs.

## 4. Products, variants, images

- [ ] Product handles defined (clean, stable, ideally close to old slugs where it helps redirects).
- [ ] Variant model mapped: old variant URLs map to the new product (avoid orphan/duplicate variant URLs).
- [ ] No products silently dropped; discontinued items have a redirect or 410 decision.
- [ ] Images migrated at full quality; alt text retained; responsive image setup in theme.
- [ ] Inventory and pricing verified post-import.

## 5. International / hreflang (if relevant)

- [ ] Market structure decided (subfolder/subdomain/domain via Shopify Markets).
- [ ] hreflang clusters mapped old -> new, reciprocal, with `x-default`.
- [ ] Per-market canonicals correct.
- [ ] No two markets cannibalizing the same language without a plan.

## 6. Analytics continuity

- [ ] GA4 and ads tracking configured on Shopify before launch (verify with `shopify-tracking-ga4-auditor`).
- [ ] Same property or a clean migration plan so pre/post comparison is possible.
- [ ] Search Console property ready for the new setup (domain property recommended); old property kept for monitoring.
- [ ] Annotate the launch date in analytics.

## 7. Pre-launch validation (on staging)

- [ ] Crawl the staging/new site: no unexpected 404s, redirect chains, or broken internal links.
- [ ] Redirect map tested against a sample of high-value old URLs (resolves to 200 final, single hop).
- [ ] Canonicals correct on each template type.
- [ ] `robots.txt` and sitemaps correct; staging is `noindex` but production plan is `index`.
- [ ] Titles/meta present and unique on key templates.
- [ ] Structured data validates.
- [ ] Performance check on key templates (LCP/INP) — no regression vs old site.
- [ ] Staging is password-protected / not indexable so it can't be crawled and indexed prematurely.
