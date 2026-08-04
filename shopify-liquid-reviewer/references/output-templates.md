# Output Templates — Shopify Liquid Reviewer

Copy-pasteable deliverable structure. Fill brackets; delete what doesn't apply.

Severity scale: **Critical** (broken / data or revenue risk) - **High** (serious bug or major debt/perf) - **Medium** (should fix) - **Low** (nice to have).

---

## 1. Technical review (summary)

> **Scope.** [Files/sections reviewed; theme base; plan.]
>
> **Overall health.** [1-2 paragraphs: architecture maturity (OS 2.0?), code quality, performance posture, biggest risks.]
>
> **Not reviewed / unseen.** [What wasn't provided and couldn't be assessed.]

Health snapshot:

| Dimension | Rating | Note |
| --- | --- | --- |
| Correctness | [Good/Watch/Weak] | [ ] |
| Architecture (OS 2.0) | [ ] | [ ] |
| Maintainability | [ ] | [ ] |
| Performance | [ ] | [ ] |
| Accessibility | [ ] | [ ] |

---

## 2. Findings (bugs, smells, risks)

| # | Finding | Type (Bug/Smell/Perf/A11y/Security) | File : location | Severity | Why it matters |
| --- | --- | --- | --- | --- | --- |
| 1 | [ ] | [ ] | `sections/x.liquid : 42` | Critical | [ ] |
| 2 | [ ] | [ ] | [ ] | High | [ ] |

---

## 3. Code smells

| Smell | Where (files) | Impact | Suggested direction |
| --- | --- | --- | --- |
| Duplicated product-card logic | [ ] | Maintenance, drift | Extract `snippets/product-card.liquid` |
| [ ] | [ ] | [ ] | [ ] |

---

## 4. Risk areas

| Risk area | Description | Likelihood | Impact | Note |
| --- | --- | --- | --- | --- |
| App coupling | [orphaned app scripts / heavy embeds] | [ ] | [ ] | Document before changing |
| [ ] | [ ] | [ ] | [ ] | [ ] |

---

## 5. Recommended refactors

For each, give a concrete fix. Include a corrected snippet when it clarifies.

**R1 - [title]** (Severity: [ ])
- **Problem:** [ ]
- **Fix:** [ ]
- **Note:** [migration risk, test points]

```liquid
{# Example corrected pattern #}
{% render 'product-card', product: product, show_rating: true %}
```

**R2 - [title]** (Severity: [ ])
- **Problem:** [ ]
- **Fix:** [ ]

---

## 6. Implementation notes

- **Safety first:** duplicate the theme before edits; never edit the live theme directly. Test in the theme editor and on key templates.
- **Order of work:** [Critical bugs -> high-severity perf/security -> architecture refactors -> low-priority polish.]
- **Test points:** [What to verify after each change — templates, devices, editor re-render, performance re-measure.]
- **Confirmation required for:** [anything destructive — removing apps/files, bulk changes.]
