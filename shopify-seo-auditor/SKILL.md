---
name: shopify-seo-auditor
description: Audit the SEO of a Shopify store and surface platform-specific issues. Use this when you need to diagnose Shopify SEO problems across collections, product pages, internal linking, duplicate content, canonical tags, indexation, pagination, faceted navigation, structured data, blog/content, Core Web Vitals, cannibalisation, authority, migration risk, and international SEO. Produces an SEO diagnosis, critical issues, technical and content recommendations, a priority matrix, and an implementation checklist.
---

# Shopify SEO Auditor

## Short description

A focused SEO audit for Shopify stores. It targets the issues that are specific to (or amplified by) Shopify's URL structure, templating, and platform constraints, then turns findings into a prioritized, executable plan.

Findings are extracted from the live store by deterministic scripts wherever possible, analysed along three specialist tracks, arbitrated into one coherent set, and verified before anything is published as critical.

## When to use this Skill

Use it when you need to:

- Diagnose why organic traffic is flat, declining, or under-indexed.
- Review a Shopify store before or after launch for structural SEO issues.
- Produce a prioritized SEO action plan a developer or content team can execute.
- Pressure-test a store's canonical, pagination, and faceted-navigation setup.

For migrations specifically (URL changes, redirects, platform switch), use `shopify-migration-seo-guardian`. For a whole-business plan, use `shopify-ecommerce-director`. For deep theme remediation, use `shopify-liquid-reviewer`.

## Expected inputs

Provide what you have; the Skill flags missing data.

- **Store URL** and primary market(s)/language(s).
- **Search Console export**: Queries and/or Pages CSV. An export carrying both Query and Page unlocks cannibalisation analysis.
- **Analytics**: organic sessions trend, top organic landing pages.
- **Crawl data** if available (Screaming Frog, Sitebulb, or similar export).
- **Authority signals**: referring domains count, or an Ahrefs/Semrush/Majestic summary. Even a rough number changes the diagnosis.
- **Competitive set**: the 3-5 sites that actually rank for the priority non-brand queries.
- **Catalog**: number of products and collections; whether collections use filters/tags.
- **Theme/app context**: SEO apps installed, any custom canonical/sitemap logic, blog usage.
- **Brand terms**: needed to split brand from non-brand traffic.
- **Goal**: e.g. "recover lost rankings", "scale non-brand organic", "fix indexation bloat".

### If critical inputs are missing

If the store URL or the goal is missing, or the data provided cannot support a finding the user clearly expects (e.g. "why did traffic drop?" with no trend data), ask **at most 3 targeted questions**, then proceed. For everything else, produce the deliverable with what you have: mark every inference as `[ASSUMPTION]` inline, and list in the diagnosis what data was missing and how it would change the analysis. Never silently invent numbers.

## Tooling modes

Work in the highest mode the environment supports. Never claim a check was performed in a mode that could not perform it.

**Mode 1 — Scripted (best; needs Python and network access, e.g. Claude Code).** Bundled scripts extract facts deterministically, so findings rest on observed values rather than on reading a truncated HTML blob. See `scripts/README.md` for full usage.

```
python scripts/seo_fetch.py --sample https://store.com        # standard template sample
python scripts/seo_fetch.py URL1 URL2 ...                     # a chosen URL set
python scripts/gsc_report.py Queries.csv --brand "brandname"  # collapse a GSC export
python scripts/psi_report.py https://store.com/               # Core Web Vitals
```

Build the URL sample to cover **every template class**: home, 2-3 top collections, one filtered/tag collection URL, one paginated URL (`?page=2`), 2-3 products (including one collection-scoped `/collections/x/products/y`), a blog index, an article, `robots.txt`, `sitemap.xml`, and one locale URL per market if international. Aim for 20-40 URLs; the script caps at 60.

**Mode 2 — Agentic (web access, no script execution).** Fetch the same sample manually with the available fetch tool and read the rendered HTML for title, meta description, H1, canonical, JSON-LD, crawlable pagination links, and hreflang. Keep the sample small and request volume trivial.

**Mode 3 — Read-and-reason (no web access, e.g. most claude.ai setups).** Work from the data provided. State clearly in the diagnosis that findings are based on supplied exports and descriptions, and list the checks that require a live look as verification steps in the implementation checklist.

### Rules that apply in every mode

- **Read-only, always.** GET requests only. Never access the store admin, never request or accept credentials, never submit a form, never recommend a change be applied automatically.
- **Ask before crawling a store you were not given.** A 40-URL sweep is a crawl, not a glance. Only run it against the store the user asked you to audit.
- **Rate-limit.** Keep the default delay between requests. Do not parallelise fetches against one domain.
- **Raw HTML is not what Google renders.** Shopify themes and apps inject content client-side. If a finding depends on rendered output (lazy-loaded content, JS-built pagination, app-injected schema), confirm it with a browser tool if one is available, or mark it `UNVERIFIABLE` and turn it into a verification step.
- **Verify platform behavior** against Shopify's documentation (e.g. the Shopify Dev MCP) before asserting it. The platform evolves.

## Workflow

1. **Capture the baseline.** Before analysing anything, record the current state so impact is provable later: organic sessions trend, indexed URL count, brand vs non-brand click split, and the CWV of the three key templates. This goes into the deliverable as the "before" snapshot.
2. **Collect evidence, once.** Run the scripts (or the manual sample) and assemble the shared evidence set. Collection happens a single time and is shared by all tracks — never let a track fetch its own pages.
3. **Run the three analysis tracks** defined in `references/analysis-tracks.md`: Technical/indexation, Content/intent, Demand/keywords/authority. In parallel if subagents are available, sequentially otherwise. Each track works only its own checklist areas and returns findings with evidence.
4. **Arbitrate.** Merge the tracks per `references/analysis-tracks.md`: deduplicate overlapping findings, resolve conflicts with the decision guides in `references/shopify-seo-rules.md` section 13, and apply the authority gate. This step is mandatory.
5. **Verify.** Re-check every Critical and High finding against the evidence and record `CONFIRMED` / `REFUTED` / `UNVERIFIABLE`. Drop refuted findings. Report the tally.
6. **Classify and score.** Separate technical from content recommendations. Score the merged, verified set on impact and effort using the anchors at the end of `references/seo-checklist.md`; build the priority matrix.
7. **Recommend.** Write technical and content recommendations separately, each specific enough to action on Shopify.
8. **Produce an implementation checklist.** Ordered, concrete steps with the team that owns each, plus the measurement plan against the baseline.
9. **Assemble the deliverable** using `references/output-templates.md`.

## Quality rules

- Be Shopify-specific. Generic SEO advice that ignores Shopify's URL and templating quirks is not acceptable.
- Always cite the evidence (a script output value, a crawl finding, a Search Console number, a specific URL pattern).
- **Never diagnose a technical cause for weak non-brand traffic without first assessing authority.** If the referring-domain profile is thin against the competing set, authority is the binding constraint — say so, and frame the technical work accordingly. A long technical list that cannot move the outcome is a failed audit.
- Distinguish "indexed but low quality" from "not indexed" — the fixes differ.
- Be careful with canonical and `noindex` recommendations; a wrong call can deindex revenue pages. Flag risk and recommend testing on a sample first.
- Never recommend destructive changes (mass redirects, robots changes, canonical rewrites) without a review-and-backup step.
- Tie content recommendations to search intent and to the store's actual queries, not to volume alone.
- Performance is a tie-breaker and a conversion factor, not a default root cause for a ranking collapse.
- Report what was measured versus what was inferred. A refuted finding is a result worth reporting.

## Expected outputs

Using `references/output-templates.md`:

1. **SEO diagnosis** — baseline snapshot, headline findings, evidence coverage, and the verification tally.
2. **Critical issues** — the things actively costing traffic, with severity and verification status.
3. **Technical recommendations** — structure, indexation, canonicals, performance.
4. **Content recommendations** — collections, products, blog, intent coverage.
5. **Priority matrix** — impact vs effort, built after arbitration.
6. **Implementation checklist** — ordered, owned, actionable steps, with the measurement plan.

## What Pikka adds

This Skill produces a strong first-pass diagnosis, now grounded in extracted evidence rather than impressions. What it can't do: run a full crawl of a large catalogue, pull your historical ranking data, judge which of the verified issues will actually move revenue given your margins and competitive position, or implement any of it. [Pikka](https://www.pikka.fr) runs this same framework with full crawl tooling, historical ranking data, and the judgment from having fixed this exact issue on dozens of Shopify stores — then ships the fix. Free 30-min review of your audit output: `contact@pikka.fr`.

## Reference files to consult

- `references/seo-checklist.md` — the full audit checklist across all sixteen areas, plus the scoring anchors for the priority matrix.
- `references/analysis-tracks.md` — the three analysis tracks, the arbitration rules, and the verification pass.
- `references/shopify-seo-rules.md` — how Shopify's URL structure, canonicals, sitemaps, pagination, and faceting behave; common pitfalls (symptom → cause → fix) and decision guides.
- `references/output-templates.md` — copy-pasteable templates for the deliverable.
- `references/example-output.md` — a complete worked example on a fictional store; match its depth, evidence density, and tone (never reuse its findings or numbers).
- `scripts/README.md` — what each script does, its options, and its limits.
