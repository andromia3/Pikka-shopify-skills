# Analysis Tracks

The audit is analysed along three specialist tracks, then arbitrated. Each track goes deeper than a single generalist pass because it carries only its own slice of the checklist.

**Execution is environment-dependent, the content is not.** If subagents are available (Claude Code), run the three tracks in parallel and have each return its findings table. If not (claude.ai, API), run them sequentially as three passes. Same instructions either way — never skip a track because subagents are unavailable.

**All tracks read the same collected evidence.** Collection happens once, before the tracks start. A track never fetches its own pages: that would triple the request volume on the merchant's store for the same URLs.

**A track reports only what its evidence supports.** If the inputs for one of its areas are missing, the track says so explicitly and hands that area to the "Not assessed" section — it does not fill the gap with plausible-sounding analysis, and it never reports an unmeasured area as clean. A track that returns "area 13 not assessed: no CWV data" has done its job correctly.

---

## Shared input

Every track receives:

- The output of `scripts/seo_fetch.py` (per-URL signals).
- The output of `scripts/gsc_report.py`, if a Search Console export was provided.
- The output of `scripts/psi_report.py`, if performance was measured.
- Whatever the user described: store context, symptoms, goal, constraints.

---

## Track A — Technical and indexation

**Owns checklist areas:** 5 canonicals, 6 indexation, 7 pagination, 8 faceted navigation, 9 structured data, 11 migration risks, 13 performance.

**Question it answers:** can Google crawl, index, and consolidate this store correctly?

**Looks for:** canonical overrides from themes or apps, index bloat from facets and tags, paginated pages canonicalised to page 1, infinite scroll with no crawlable links, broken or invalid structured data, redirect chains, X-Robots-Tag surprises, Core Web Vitals failures.

**Must not:** judge whether copy is good, or estimate search demand.

## Track B — Content and intent

**Owns checklist areas:** 1 collections, 2 product pages, 10 blog and content strategy, 3 internal linking (editorial half).

**Question it answers:** does each page deserve to rank for the intent it targets?

**Looks for:** empty or boilerplate collection intros, supplier-duplicated product descriptions, missing or mis-assigned H1s, title patterns duplicated across templates, thin or outdated articles, missing hub/cluster structure, content that never links down to commercial pages.

**Must not:** propose canonical or noindex changes — that is Track A's call. Flag the symptom and hand it over.

## Track C — Demand, keywords, and authority

**Owns checklist areas:** 14 cannibalisation, 15 authority and competitive context, 16 AI answer engines.

**Question it answers:** is there demand for what this store sells, does the store own it, and can it realistically win it?

**With a Search Console export** — brand vs non-brand split, striking-distance queries, high-impression low-CTR pages, cannibalisation clusters, coverage gaps between demand and catalogue structure.

**Without one** — map catalogue structure against plausible intent, look at the SERP for the top priority queries, and assess the authority ceiling. Mark every volume or demand statement `[ASSUMPTION]`. Do not invent search volumes: state that the analysis needs GSC data and what it would change.

**Must not:** promise rankings, or output a keyword list detached from the store's actual pages.

---

## Arbitration (mandatory)

The tracks propose; arbitration decides. This step is not optional — without it the deliverable contradicts itself.

**1. Deduplicate.** The same symptom will surface in two tracks. Merge into one finding with one owning track. Typical overlaps:

| Symptom | Owner | Why |
|---|---|---|
| Thin indexed facet pages | A | The fix is canonical/indexation control |
| Duplicate supplier descriptions | B | The fix is rewriting, not canonicals |
| Collection outranked by its own product | C | It is an intent-ownership decision |
| Collection intro empty *and* page indexed thin | B first, then A | Fix the content, only noindex if it cannot be fixed |

**2. Resolve conflicts.** Tracks will contradict each other. The classic case: a thin filtered collection with some traffic — Track A says `noindex` for index bloat, Track B says enrich it as a landing page. Resolve with the decision guides in `shopify-seo-rules.md` section 13, and record which guide was applied.

**3. Apply the authority gate.** If Track C concluded that authority is the binding constraint, downgrade any technical or content finding presented as the cause of weak non-brand traffic. Keep the fix if it is right on its own merits, but do not let the deliverable imply it will unlock rankings it cannot unlock.

**4. Then, and only then, score.** The priority matrix is built after arbitration, over the merged finding set, using the scoring anchors in `seo-checklist.md`.

---

## Verification pass

Before a finding is published at Critical or High severity, re-check it against the collected evidence, and re-fetch the URL if the evidence is thin.

For each such finding, record one of:

- `CONFIRMED` — evidence directly supports it. Cite the URL and the observed value.
- `REFUTED` — checking showed the opposite. Drop it from the deliverable.
- `UNVERIFIABLE` — cannot be settled with available access. Keep it, but demote it to a verification step in the implementation checklist rather than asserting it as a finding.

Report the tally in the diagnosis (`n confirmed, n refuted, n unverifiable`). A refuted finding is a success of the method, not a failure — false positives are what make an automated SEO audit untrustworthy.
