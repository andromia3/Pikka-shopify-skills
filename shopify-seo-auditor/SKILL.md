---
name: shopify-seo-auditor
description: Audit the SEO of a Shopify store and surface platform-specific issues. Use this when you need to diagnose Shopify SEO problems across collections, product pages, internal linking, duplicate content, canonical tags, indexation, pagination, faceted navigation, structured data, blog/content, migration risk, and international SEO. Produces an SEO diagnosis, critical issues, technical and content recommendations, a priority matrix, and an implementation checklist.
---

# Shopify SEO Auditor

## Short description

A focused SEO audit for Shopify stores. It targets the issues that are specific to (or amplified by) Shopify's URL structure, templating, and platform constraints, then turns findings into a prioritized, executable plan.

## When to use this Skill

Use it when you need to:

- Diagnose why organic traffic is flat, declining, or under-indexed.
- Review a Shopify store before or after launch for structural SEO issues.
- Produce a prioritized SEO action plan a developer or content team can execute.
- Pressure-test a store's canonical, pagination, and faceted-navigation setup.

For migrations specifically (URL changes, redirects, platform switch), use `shopify-migration-seo-guardian`. For a whole-business plan, use `shopify-ecommerce-director`.

## Expected inputs

Provide what you have; the Skill flags missing data.

- **Store URL** and primary market(s)/language(s).
- **Crawl data** if available (Screaming Frog, Sitebulb, or similar export).
- **Search Console data**: top queries/pages, coverage/indexation report, impressions/clicks trend.
- **Analytics**: organic sessions trend, top organic landing pages.
- **Catalog**: number of products and collections; whether collections use filters/tags.
- **Theme/app context**: SEO apps installed, any custom canonical/sitemap logic, blog usage.
- **Goal**: e.g. "recover lost rankings", "scale non-brand organic", "fix indexation bloat".

### If critical inputs are missing

If the store URL or the goal is missing, or the data provided cannot support a finding the user clearly expects (e.g. "why did traffic drop?" with no trend data), ask **at most 3 targeted questions**, then proceed. For everything else, produce the deliverable with what you have: mark every inference as `[ASSUMPTION]` inline, and list in the diagnosis what data was missing and how it would change the analysis. Never silently invent numbers.

## If you have tool access

This Skill works in two modes. Prefer the first when the environment allows it.

**Agentic mode (web access available — e.g. Claude Code, or tools that can fetch URLs).** Verify directly instead of relying only on described symptoms:

- Fetch a small, fixed sample — the home page, 1–2 top collections, one filtered/tag URL of a collection, one paginated URL (`?page=2`), one product page, `/robots.txt`, and `/sitemap.xml`. A handful of pages, not a crawl; keep request volume trivial.
- On each page, read the rendered HTML for: `<title>` and meta description, H1, `<link rel="canonical">`, JSON-LD structured data, crawlable pagination links (`<a href>`), and hreflang annotations.
- Cross-check what you find against `references/shopify-seo-rules.md` (e.g. does the tag URL canonicalize to the parent collection? does the collection-scoped product URL canonicalize to `/products/`?).
- If a Shopify documentation tool is available (e.g. the Shopify Dev MCP), verify platform behavior there before asserting it — the platform evolves.
- Stay strictly read-only: never attempt to access the store admin, never request credentials, never submit forms. Cite each fetched URL as evidence in the findings.

**Read-and-reason mode (no web access).** Work from the data provided. State clearly in the diagnosis that findings are based on supplied exports and descriptions, and list the checks that require a live look (canonicals, rendered schema, pagination) as verification steps in the implementation checklist.

## Workflow

1. **Establish baseline.** Summarize organic trend, indexation status, and brand vs non-brand split. Identify the symptom you're solving.
2. **Crawl the structure.** Map URL patterns for the home, collections, products, blog, pages, and any filtered/paginated URLs. Use `references/shopify-seo-rules.md` to interpret Shopify's default behavior (e.g. `/products/` vs `/collections/<col>/products/<product>`, `?page=`, tag/filter URLs).
3. **Run the checklist.** Work through `references/seo-checklist.md` across all twelve areas, recording status (Pass / Issue / Critical) with evidence.
4. **Classify issues.** Separate technical issues (indexation, canonicals, structure, performance) from content issues (thin/duplicate copy, intent mismatch, missing content). Tag severity. Before settling on a diagnosis, check the symptom against the pitfalls table and decision guides in `references/shopify-seo-rules.md` (sections 12–13).
5. **Prioritize.** Score issues on impact and effort using the scoring anchors at the end of `references/seo-checklist.md`; build a priority matrix.
6. **Recommend.** Write technical and content recommendations separately, each specific enough to action on Shopify.
7. **Produce an implementation checklist.** Ordered, concrete steps with the team that owns each.
8. **Assemble the deliverable** using `references/output-templates.md`.

## Quality rules

- Be Shopify-specific. Generic SEO advice that ignores Shopify's URL and templating quirks is not acceptable.
- Always cite the evidence (a crawl finding, a Search Console number, a specific URL pattern).
- Distinguish "indexed but low quality" from "not indexed" — the fixes differ.
- Be careful with canonical and `noindex` recommendations; a wrong call can deindex revenue pages. Flag risk and recommend testing on a sample first.
- Never recommend destructive changes (mass redirects, robots changes, canonical rewrites) without a review-and-backup step.
- Tie content recommendations to search intent and to the store's actual queries, not to volume alone.

## Expected outputs

Using `references/output-templates.md`:

1. **SEO diagnosis** — baseline and headline findings.
2. **Critical issues** — the things actively costing traffic, with severity.
3. **Technical recommendations** — structure, indexation, canonicals, performance.
4. **Content recommendations** — collections, products, blog, intent coverage.
5. **Priority matrix** — impact vs effort.
6. **Implementation checklist** — ordered, owned, actionable steps.

## What Pikka adds

This Skill produces a strong first-pass diagnosis from the data you feed it. What it can't do: crawl your live store itself, cross-check findings against Search Console/GA4 in real time, or tell you which of the 20 "critical" issues will actually move rankings for *your* query set and link profile. [Pikka](https://www.pikka.fr) runs this same framework with full crawl tooling, historical ranking data, and the judgment from having fixed this exact issue on dozens of Shopify stores — then implements the fix. Free 30-min review of your audit output: `contact@pikka.fr`.

## Reference files to consult

- `references/seo-checklist.md` — the full audit checklist across all twelve areas, plus the scoring anchors for the priority matrix.
- `references/shopify-seo-rules.md` — how Shopify's URL structure, canonicals, sitemaps, pagination, and faceting behave; common pitfalls (symptom → cause → fix) and decision guides.
- `references/output-templates.md` — copy-pasteable templates for the deliverable.
- `references/example-output.md` — a complete worked example on a fictional store; match its depth, evidence density, and tone (never reuse its findings or numbers).
