# Output Templates — Migration SEO Guardian

Copy-pasteable deliverable structure. Fill brackets; delete what doesn't apply.

---

## 1. Migration risk assessment

> **Migration summary.** [From <platform> to Shopify; catalog size; markets; timeline.]

| Risk factor | Level | Notes |
| --- | --- | --- |
| URL change scope | [Low/Med/High] | [ ] |
| Traffic concentration | [ ] | [ ] |
| Backlink exposure | [ ] | [ ] |
| Catalog size | [ ] | [ ] |
| International | [ ] | [ ] |
| Content parity | [ ] | [ ] |
| Timeline | [ ] | [ ] |

> **Highest-exposure areas.** [The 2-3 things most likely to cause traffic loss, and how the plan mitigates them.]

---

## 2. Redirect mapping framework

> **Rules.** [Pattern-based rules used + where explicit one-to-one mapping applies.]

| old_url | type | clicks | backlinks | new_url | redirect_type | status |
| --- | --- | --- | --- | --- | --- | --- |
| [ ] | product | [ ] | [ ] | [ ] | 301 | validated |
| [ ] | category | [ ] | [ ] | [ ] | 301 | pending |
| [ ] | retired | [ ] | [ ] | — | 410 | n/a |

> **Coverage.** [X% of valued URLs mapped; list any unresolved high-value URLs.]

---

## 3. Pre-launch checklist (staging)

- [ ] URL inventory consolidated from crawl + sitemaps + GSC + backlinks + logs
- [ ] Redirect map built and validated on a sample (single-hop 301 -> 200)
- [ ] Metadata, headings, structured data migrated
- [ ] Products, variants, images mapped; no silent drops
- [ ] hreflang clusters mapped (if international)
- [ ] Analytics/tracking configured and verified
- [ ] Canonicals, sitemaps, robots correct; staging not indexable
- [ ] Performance parity check on key templates

---

## 4. Go-live checklist (launch day)

- [ ] Remove indexing block on new site
- [ ] Point DNS / publish (confirmation gate + rollback ready)
- [ ] Verify home + key templates (HTTPS, canonical host)
- [ ] Test priority redirects live
- [ ] Crawl live site for 404s / chains
- [ ] Submit sitemap; request indexing for top pages
- [ ] Verify tracking on a live session
- [ ] Validation gate passed (or rollback executed)

---

## 5. Post-launch SEO monitoring plan

| When | What to check | Tool | Threshold that triggers action |
| --- | --- | --- | --- |
| Day 0-2 | 404 spikes, redirect errors, tracking | Logs, GSC, GA4 | Any priority URL 404 -> patch immediately |
| Daily, week 1 | Coverage/indexation, crawl stats | Search Console | Indexed pages dropping -> investigate |
| Weekly, weeks 1-4 | Rankings & organic traffic vs baseline | GSC, analytics | >15-20% sustained drop -> escalate |
| Weeks 4-8 | Recovery curve, new URL indexation | GSC | Not recovering by week 6-8 -> deep review |
| Ongoing | New 404s, lost redirects | Logs / crawl | Add missing redirects as found |

> **Baseline snapshot (pre-launch):** organic sessions [ ], indexed pages [ ], top queries [ ]. Compare against this throughout.
