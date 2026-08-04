# Full audit output — Shopify SEO Auditor Skill

Unedited transcript of a Claude Code session running the `shopify-seo-auditor` Skill against a live store.

- **Store audited:** `https://www.nooance-paris.com/`
- **Prompt:** `Can you make a seo audit of the following shopify store https://www.nooance-paris.com/ ? I want to increase my trafic`

---

```
❯ Can you make a seo audit of the following shopify store                       
  https://www.nooance-paris.com/ ? I want to increase my trafic                 

● Skill(shopify-seo-auditor)
  ⎿  Successfully loaded skill

  Read 3 files (ctrl+o to expand)

● I'll now fetch a small sample of live pages from the store to check
  Shopify-specific SEO signals (canonicals, titles, robots.txt, sitemap,
  structured data).

  Ran 2 shell commands, searched memories (ctrl+o to expand)

● This reveals a huge structural issue: the store has ~200 Shopify Markets
  locale subfolders (en-us, en-gb, fr-be, es-es, de-de, etc.), each generating a
  full duplicate sitemap set. Let me check the actual page markup now —
  canonical tags, hreflang, titles.

  Ran 3 shell commands (ctrl+o to expand)

● Good — title/meta description/canonical are present and correct on the
  homepage. But notably zero hreflang tags despite ~200 market subfolders. Let
  me confirm and check a product page, collection page, and one locale
  subfolder.

  Read 1 file, ran 3 shell commands (ctrl+o to expand)

● This is a major finding: ~200 market subfolders exist and are sitemapped, but
  hreflang only declares ~18 of them. Let me verify whether these extra locale
  pages are actually live, indexable, and how they canonicalize — that
  determines the severity.

  Ran 15 shell commands (ctrl+o to expand)

  [... intermediate tool calls omitted: the Skill crawled the store and extracted structured data ...]

  Read 1 file, ran 7 shell commands (ctrl+o to expand)

● SEO Audit — Nooance Paris (nooance-paris.com)

  Method: live crawl sample (not a full crawl) — homepage, 2 "all products"
  collections, 1 filtered/concern collection, 1 stale promo collection, 1
  product page, 3 blog indexes, robots.txt, the full sitemap index + 3 child
  sitemaps, and 12 Shopify Markets locale homepages. No Search Console or GA4
  data was provided, so I can't quantify current traffic/ranking loss per issue
  — only diagnose structural causes. Get me a GSC export (queries + coverage)
  and I can turn this into a prioritized, quantified plan.

  1. Diagnosis

  Baseline (inferred, not measured): small, well-merchandised catalog — 68
  products, 88 collection URLs, 120 active blog articles (/blogs/journal, last
  updated 2026-07-08) plus 39 in /blogs/experiences. Theme is a modern Shopify
  Horizon-style build. Core technical hygiene (canonicals, pagination,
  faceted-nav strategy) is actually good — better than most Shopify stores I
  check. The traffic ceiling here isn't "broken SEO," it's a handful of specific
  structural leaks plus under-used structured data.

  Headline: the biggest single issue is that the store runs two competing "all 
  products" pages, both linked from the homepage nav — /collections/all (thin,
  Shopify's default auto-title "All", no meta description) and
  /collections/tous-les-produits (properly optimized, its own
  title/description). Splitting your single highest-value non-brand page in two,
  with internal links dividing between them, is a self-inflicted
  cannibalization on the page category most likely to rank for generic "soins
  visage / beauty tech" queries.

  2. Critical issues

  #: 1
  Issue: Two indexable "all products" collections, both linked from the homepage

    nav
  Area: Duplicate content / Collections
  Severity: High
  Evidence: /collections/all → title "All", no meta description, index,follow.
    /collections/tous-les-produits → title "Soins et beauty tech Nooance" + full

    meta description, index,follow. Homepage links to /collections/all 4× and
    /collections/tous-les-produits 5×. 16 of ~27 sampled products appear on both
  Impact if unfixed: Link equity and rankings for your broadest commercial
  intent
    are split between a thin default page and your real one, instead of
    consolidating on one
  ────────────────────────────────────────
  #: 2
  Issue: /fr-be/ is declared as a reciprocal hreflang target on every page of 
  the
     site, but the page itself is noindex, nofollow
  Area: International / hreflang
  Severity: High
  Evidence: Every sampled page (home, all 12 markets, both "all" collections)
    emits <link rel="alternate" hreflang="fr-BE" href=".../fr-be/">; fetching
    /fr-be/ returns noindex, nofollow while every other declared market (fr-ca,
    fr-ch, fr-ma, en-us, en-gb, en-ca, de-de, de-ch, it-it, it-ch, es-es) is
    index, follow
  Impact if unfixed: A broken node in a sitewide hreflang cluster; Belgian
  French
    searchers get no clean indexed local page, and it's an invalid annotation on

    every indexed URL on the site
  ────────────────────────────────────────
  #: 3
  Issue: ~180 extra Shopify Markets locale subfolders (en-ad, fr-ga, en-africa,
    es-mx, etc. — nearly every country code) each generate full
    product/collection/page/blog XML sitemaps listed in the master /sitemap.xml,

    despite every one of those pages being noindex, nofollow
  Area: Indexation / Sitemap hygiene
  Severity: Medium
  Evidence: Sitemap index lists ~200 locale prefixes × 5 sub-sitemaps each;
    sampled en-ad, fr-ga both return 200 + noindex, nofollow with
    self-referential canonical
  Impact if unfixed: Wastes crawl budget on thousands of URLs Google will fetch
    and discard every cycle; per the platform rule, sitemaps should only list
    indexable URLs
  ────────────────────────────────────────
  #: 4
  Issue: Stale, dated promotional collections still live and indexed
  Area: Content quality
  Severity: Medium
  Evidence: /collections/offre-hiver-2023 ("Offres hiver 2023") — index, follow,

    ~2.5 years old; /collections/soldes-dete-2024 also in sitemap
  Impact if unfixed: Outdated seasonal offers sitting in the index look stale to

    both users and Google, and dilute the quality signal of your collection
    template class
  ────────────────────────────────────────
  #: 5
  Issue: 3 of 5 blogs (/blogs/blog, /blogs/youtube, /blogs/presse) are indexed
    with zero articles — only empty tag-filter links
  Area: Blog / Content
  Severity: Medium
  Evidence: /blogs/blog returns index, follow; the only internal links found are

    tagged/actifs, tagged/anti-age, etc. — no actual articles
  Impact if unfixed: Empty, indexed listing pages contribute to "thin content"
    quality signals for no traffic upside
  ────────────────────────────────────────
  #: 6
  Issue: Product pages have no aggregateRating/review schema despite Yotpo
    reviews genuinely present on the page
  Area: Structured data
  Severity: Medium
  Evidence: JSON-LD on /products/serum-bulles-d-hydratation-apaisant-regenerant
  =
    Organization + ProductGroup/Offer only; page visibly contains ~80+
    review-related elements from Yotpo, but no rating markup
  Impact if unfixed: Missing star-rating rich results in search = lower organic
    CTR on your highest-intent pages

  3. Technical recommendations

  #: T1
  Recommendation: Pick one "all products" page and retire the other
  Area: Duplicate content
  Why: Fixes issue #1 directly
  How (Shopify-specific): Keep /collections/tous-les-produits (it's the
  optimized
    one). Remove /collections/all from all nav/homepage links; 301
    /collections/all → /collections/tous-les-produits via Online Store → 
    Navigation → URL Redirects (Shopify's default all collection can't be
    deleted, but it can be redirected)
  Owner: Dev
  ────────────────────────────────────────
  #: T2
  Recommendation: Fix the fr-be hreflang/index mismatch
  Area: International
  Why: Fixes issue #2
  How (Shopify-specific): In Settings → Markets, either activate fr-be as a real

    indexable market (if Belgium is a target) or, if not, remove Belgium from
  the
     market whose hreflang set includes it — don't leave a hreflang target
    permanently pointing at a noindex page
  Owner: Dev/Ops
  ────────────────────────────────────────
  #: T3
  Recommendation: Stop sitemapping non-indexable Markets subfolders
  Area: Sitemap hygiene
  Why: Fixes issue #3, recovers crawl budget
  How (Shopify-specific): This is generated by Shopify Markets automatically per

    configured market/country; audit Settings → Markets and  remove
  country-level
     entries you don't actually intend  to serve/index rather than leaving them
    in a catch-all  "Rest of world" bucket that still emits sitemaps
  Owner: Dev/Ops
  ────────────────────────────────────────
  #: T4
  Recommendation: Add Review/aggregateRating schema to PDPs
  Area: Structured data
  Why: Fixes issue #6
  How (Shopify-specific): Check Yotpo's app settings for "structured data" /
    schema markup output (most Yotpo plans support this natively) rather than
    hand-rolling it in the theme; validate with Google's Rich Results Test after

    enabling
  Owner: Dev
  ────────────────────────────────────────
  #: T5
  Recommendation: Add BreadcrumbList schema to product templates
  Area: Structured data
  Why: Collections already have breadcrumb microdata; products don't
  How (Shopify-specific): Reuse the same
    itemscope/itemtype="https://schema.org/BreadcrumbList" pattern already
    implemented in the collection template's breadcrumbs__list, inside
    product.liquid
  Owner: Dev

  4. Content recommendations

  #: C1
  Recommendation: Unpublish or unlink offre-hiver-2023, soldes-dete-2024 and any

    other dated promo collections no longer active
  Target: Collections
  Search intent: N/A (hygiene)
  Action: Set to draft/unpublished, or 301 to the live equivalent seasonal
    collection if one exists
  Owner: Content
  ────────────────────────────────────────
  #: C2
  Recommendation: Unpublish the 3 empty blogs (blog, youtube, presse) or merge
    their intent into journal
  Target: Blog
  Search intent: N/A (hygiene)
  Action: If presse/youtube are meant for press/video content later, keep as
    draft until populated rather than live-and-empty
  Owner: Content
  ────────────────────────────────────────
  #: C3
  Recommendation: Audit the 88 collections against the 68-product catalog for
    overlap beyond the "all products" pair
  Target: Collections
  Search intent: Commercial
  Action: You have roughly 1.3 collections per product — review offres /
    offres-duos / offres-trios / offres-decouverte / les-incontournables /
    meilleurs-ventes for the same cannibalization pattern found in #1
  Owner: Content
  ────────────────────────────────────────
  #: C4
  Recommendation: Keep investing in /blogs/journal — it's your real
    content-marketing asset
  Target: Blog
  Search intent: Informational
  Action: 120 articles, actively updated (last: 2026-07-08). This is working;
    don't dilute it by spreading new content across the empty blogs instead
  Owner: Content

  5. Priority matrix

  ┌─────────┬──────────────────────────┬────────────────────────────────────┐
  │         │        Low effort        │            High effort             │
  ├─────────┼──────────────────────────┼────────────────────────────────────┤
  │ High    │ T1 duplicate "all" fix · │ C3 collection-overlap audit        │
  │ impact  │  T2 hreflang/fr-be fix   │                                    │
  ├─────────┼──────────────────────────┼────────────────────────────────────┤
  │ Low     │ C1 stale promos · C2     │ T3 Markets sitemap cleanup · T4    │
  │ impact  │ empty blogs              │ review schema · T5 breadcrumb      │
  │         │                          │ schema                             │
  └─────────┴──────────────────────────┴────────────────────────────────────┘

  Ranked shortlist:

  ┌──────┬───────────────────────────────────────┬────────┬────────┬─────────┐
  │ Rank │                 Item                  │ Impact │ Effort │  Type   │
  ├──────┼───────────────────────────────────────┼────────┼────────┼─────────┤
  │ 1    │ T1 — merge/redirect /collections/all  │ 4      │ 1      │ Tech    │
  │      │ → tous-les-produits                   │        │        │         │
  ├──────┼───────────────────────────────────────┼────────┼────────┼─────────┤
  │ 2    │ T2 — fix fr-be hreflang/index         │ 3      │ 1      │ Tech    │
  │      │ mismatch                              │        │        │         │
  ├──────┼───────────────────────────────────────┼────────┼────────┼─────────┤
  │ 3    │ C1 — unpublish stale seasonal         │ 2      │ 1      │ Content │
  │      │ collections                           │        │        │         │
  ├──────┼───────────────────────────────────────┼────────┼────────┼─────────┤
  │ 4    │ C2 — unpublish empty blogs            │ 2      │ 1      │ Content │
  ├──────┼───────────────────────────────────────┼────────┼────────┼─────────┤
  │ 5    │ T4 — enable review schema via Yotpo   │ 3      │ 2      │ Tech    │
  ├──────┼───────────────────────────────────────┼────────┼────────┼─────────┤
  │ 6    │ T5 — breadcrumb schema on PDPs        │ 2      │ 2      │ Tech    │
  ├──────┼───────────────────────────────────────┼────────┼────────┼─────────┤
  │ 7    │ C3 — audit 88 collections for overlap │ 4      │ 3      │ Content │
  ├──────┼───────────────────────────────────────┼────────┼────────┼─────────┤
  │ 8    │ T3 — trim Markets sitemap bloat       │ 2      │ 3      │ Tech    │
  └──────┴───────────────────────────────────────┴────────┴────────┴─────────┘

  6. Implementation checklist

  - [ ] T1 — Redirect /collections/all to /collections/tous-les-produits, remove
  duplicate nav links — Dev — verify: only one "all products" URL indexable,
  old one 301s
  - [ ] T2 — Resolve fr-be Markets config — Dev/Ops — verify: hreflang set no
  longer references a noindex page
  - [ ] C1/C2 — Unpublish stale collections and empty blogs — Content — verify:
  removed from /sitemap.xml on next regeneration
  - [ ] T4 — Enable Yotpo schema output — Dev — verify: Rich Results Test shows
  valid AggregateRating
  - [ ] T5 — Add breadcrumb schema to PDPs — Dev — verify: Rich Results Test
  passes on 3 sample products
  - [ ] C3 — Manual pass over all 88 collections vs. 68 products — Content —
  verify: overlap map documented, consolidation decisions logged
  - [ ] T3 — Review Shopify Markets country list — Dev/Ops — verify: sitemap
  index no longer lists noindex-only market subfolders

  Validation after changes: re-crawl the sampled URLs above, recheck the sitemap
  index size, and — critically — connect Search Console so future passes can be
  quantified against actual indexed-page counts and query data instead of
  inference.

  ---What this can't tell you without Search Console/GA4 access: which of these
  issues is actually suppressing the most real traffic, and what your non-brand
  query gaps are. If you connect GSC + GA4 (or export the coverage/performance
  reports), I can turn this into a quantified, ranked plan the same way.

✻ Worked for 7m 39s```
