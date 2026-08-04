# Output Templates — Shopify SEO Auditor

Copy-pasteable deliverable structure. Fill brackets; delete rows that don't apply.

---

## 1. SEO diagnosis

> **Headline.** [The 1-2 findings that explain most of the problem.]
>
> **Binding constraint.** [Technical / content / authority — which one actually caps growth. If authority, say so plainly.]
>
> **Scope & data used.** [Which tooling mode was used, how many URLs were sampled, which exports were provided — and what was missing.]

### Baseline snapshot

Recorded before any change, so impact is provable later.

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
