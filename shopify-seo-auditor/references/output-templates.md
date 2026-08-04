# Output Templates — Shopify SEO Auditor

Copy-pasteable deliverable structure. Fill brackets; **delete every row, table, and section you could not actually measure** — an empty placeholder in a client deliverable is worse than its absence.

---

## 0. Coverage

Goes first, before any finding. The reader must know what this audit does and does not cover before they read a single recommendation.

> **Mode.** [1 scripted / 2 agentic / 3 read-and-reason] — [n] URLs sampled across [n] template classes.
>
> **Data provided.** [GSC export (queries only / queries + pages), analytics, crawl, authority data — list what was actually supplied.]
>
> **Not assessed.** [Areas skipped, in one line each. If everything was covered, say so.]

---

## 1. SEO diagnosis

> **Headline.** [The 1-2 findings that explain most of the problem.]
>
> **Binding constraint.** [Technical / content / authority — which one actually caps growth. If authority, say so plainly.]
>
> **Scope & data used.** [Which tooling mode was used, how many URLs were sampled, which exports were provided — and what was missing.]

### Baseline snapshot

Recorded before any change, so impact is provable later. **Keep only the rows you measured.** A blank or estimated baseline is useless — it cannot prove anything three months from now.

| Metric | Value | Source | Date |
| --- | --- | --- | --- |
| Organic sessions (last 28d) | [ ] | Analytics | [ ] |
| Organic clicks / impressions | [ ] | GSC | [ ] |
| Brand vs non-brand click split | [ ]% / [ ]% | `gsc_report.py` | [ ] |
| Indexed URLs vs catalogue size | [ ] / [ ] | GSC coverage | [ ] |
| LCP p75 — home / collection / PDP | [ ] / [ ] / [ ] | `psi_report.py` | [ ] |
| Referring domains | [ ] | [tool] | [ ] |

### Verification tally

| Status | Count |
| --- | --- |
| Confirmed | [ ] |
| Refuted (dropped) | [ ] |
| Unverifiable (moved to checklist) | [ ] |

---

## 2. Critical issues

Issues actively costing traffic or revenue. Severity: Critical / High / Medium. Only `CONFIRMED` findings appear at Critical or High.

| # | Issue | Area | Track | Severity | Status | Evidence | Impact if unfixed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [ ] | [ ] | A/B/C | Critical | CONFIRMED | [URL + observed value] | [ ] |
| 2 | [ ] | [ ] | [ ] | High | CONFIRMED | [ ] | [ ] |

**Arbitration notes.** [Conflicts resolved between tracks, which decision guide was applied, and any finding downgraded by the authority gate.]

---

## 3. Technical recommendations

| # | Recommendation | Area | Why | How (Shopify-specific) | Owner |
| --- | --- | --- | --- | --- | --- |
| T1 | [ ] | Canonicals | [ ] | [ ] | Dev |
| T2 | [ ] | Indexation | [ ] | [ ] | Dev |
| T3 | [ ] | Faceted nav | [ ] | [ ] | Dev |

---

## 4. Content recommendations

| # | Recommendation | Target (collection/product/blog) | Search intent | Action | Owner |
| --- | --- | --- | --- | --- | --- |
| C1 | [ ] | [ ] | [ ] | [ ] | Content |
| C2 | [ ] | [ ] | [ ] | [ ] | Content |

---

## 5. Priority matrix (impact vs effort)

| | Low effort | High effort |
| --- | --- | --- |
| **High impact** | [Quick wins] | [Big projects] |
| **Low impact** | [Fill-ins] | [Defer] |

Ranked shortlist:

| Rank | Item | Impact (1-5) | Effort (1-5) | Type (Tech/Content) |
| --- | --- | --- | --- | --- |
| 1 | [ ] | [ ] | [ ] | [ ] |

---

## 6. Implementation checklist

Ordered so dependencies come first (e.g. fix canonicals/indexation before scaling content).

- [ ] [Step 1 — owner — what "done" looks like]
- [ ] [Step 2 — owner — verification]
- [ ] [Step 3 — owner — verification]

### Checks that could not be verified remotely

Findings marked `UNVERIFIABLE` become tasks here rather than assertions above.

- [ ] [What to check — why it could not be confirmed remotely — who has the access]

### Measurement plan

Re-run against the baseline snapshot so impact is provable, not asserted.

| When | What to re-measure | How | Expected direction |
| --- | --- | --- | --- |
| Week 0 | Baseline above | scripts + GSC | — |
| Week 2 | Indexation, canonicals, redirects | `seo_fetch.py`, GSC coverage | [ ] |
| Week 4-8 | Non-brand clicks, striking-distance positions | `gsc_report.py` | [ ] |
| Week 8-12 | CWV, organic sessions | `psi_report.py`, analytics | [ ] |

**Validation after changes:** re-crawl, recheck GSC coverage, confirm canonicals/sitemaps, monitor index and organic trend for 2-4 weeks. Attribute cautiously — seasonality and algorithm updates move these numbers too.

---

## 7. Not assessed

Every checklist area that could not be evaluated, and what would unlock it. This section exists so the reader never mistakes silence for a clean bill of health.

**These areas were not audited. That is not the same as finding no problem in them.**

| Area | Why not assessed | What would unlock it |
| --- | --- | --- |
| 13. Performance / Core Web Vitals | No PageSpeed API key available | A free key (`scripts/README.md`), or a PageSpeed Insights run on home, top collection, top PDP |
| 14. Cannibalisation | GSC export carried queries only | Re-export Search Console with **both** Query and Page dimensions |
| 15. Authority | No backlink or competitive data provided | Referring-domain count from any SEO tool, plus the 3-5 sites ranking for your priority queries |
| [ ] | [ ] | [ ] |

Delete the rows that do not apply. If every area was assessed, replace this section with a single line saying so.
