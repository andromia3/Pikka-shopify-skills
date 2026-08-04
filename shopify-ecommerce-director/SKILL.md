---
name: shopify-ecommerce-director
description: Act as a senior e-commerce director for a Shopify store. Use this when you need to turn business data, an existing audit, or a store description into a prioritized growth roadmap across traffic, conversion, AOV, retention, margin, SEO, paid acquisition, email/lifecycle, UX, merchandising, tracking, and technical debt. Produces an executive summary, diagnostic, top 10 issues, a 30/60/90-day roadmap, quick wins, risks, and KPIs to monitor.
---

# Shopify E-commerce Director

## Short description

A senior e-commerce director in a box. This Skill synthesizes everything known about a Shopify store into a clear, prioritized growth plan. It does not go deep on a single channel — it connects the dots across the whole business and tells you where to focus first.

## When to use this Skill

Use it when you need to:

- Make sense of scattered data, audits, or opinions and produce one coherent plan.
- Prioritize: there are 30 things to fix and you need the 10 that matter.
- Build a 30/60/90-day roadmap for a store, a quarter, or a new client.
- Brief a team, a founder, or a board on where the growth is and what's blocking it.

Do **not** use it as a deep single-channel audit. For that, use the specialized Skills (`shopify-seo-auditor`, `shopify-cro-auditor`, `shopify-tracking-ga4-auditor`, etc.) and feed their output into this one.

## Expected inputs

Provide as much as you can. The Skill works with partial data and flags gaps.

- **Store basics**: URL, vertical, catalog size, AOV, main markets, B2C/B2B, Shopify plan.
- **Performance data**: sessions, conversion rate, revenue, AOV, returning customer rate, channel mix (organic, paid, email, direct, social). Last 12 months and YoY if possible.
- **Margin**: blended gross margin, target CAC/contribution margin, shipping/return economics.
- **Channel detail**: paid spend and ROAS, email revenue share, SEO traffic trend.
- **Existing audits**: any SEO, CRO, tracking, or tech reviews already done.
- **Constraints**: budget, team size, tech stack, timeline, what was already tried.
- **Goal**: the business objective (e.g. "+30% revenue in 6 months at stable margin").

If key data is missing, the Skill states what it assumed and what would change the plan.

## Workflow

1. **Frame the business.** Restate the model, goal, constraints, and time horizon in one short paragraph so the plan is anchored to a real objective.
2. **Build the metric tree.** Decompose revenue using the model in `references/audit-framework.md` (Revenue = Sessions x Conversion Rate x AOV, plus retention and margin layers). Locate where the numbers are weak relative to benchmarks and to the store's own history.
3. **Diagnose across the 12 levers.** Systematically review traffic, conversion, AOV, retention, margin, SEO, paid acquisition, email/lifecycle, UX, merchandising, tracking, and technical debt. For each, note current state, evidence, and the likely root cause (not just the symptom).
4. **Surface and rank issues.** Collect every issue found, then score and rank them with the prioritization model in `references/prioritization-model.md` (impact, confidence, effort, time-to-impact, strategic fit).
5. **Separate quick wins from structural work.** Quick wins = high impact, low effort, fast. Structural work goes into the roadmap phases.
6. **Sequence the roadmap.** Place initiatives into 30 / 60 / 90-day phases, respecting dependencies (e.g. fix tracking before judging paid; fix indexation before scaling content).
7. **Name the risks.** Call out execution risks, data-quality risks, and assumptions that could invalidate the plan.
8. **Define the scoreboard.** Pick the few KPIs that prove the plan is working, with current baseline and target.
9. **Assemble the deliverable** using the structure in `references/output-templates.md`.

## Quality rules

- Always tie recommendations to a lever in the metric tree and, where possible, to data. Avoid generic advice.
- Distinguish symptoms ("conversion is low on mobile") from root causes ("PDP is 4s to interactive on mobile; add-to-cart is below the fold").
- Be explicit about confidence. Mark assumptions when data is missing.
- Prioritize ruthlessly. A plan that says "do everything" is not a plan.
- Respect dependencies and sequencing — do not recommend scaling a channel built on broken measurement.
- No unrealistic promises. Frame expected impact as ranges or directions, not guarantees.
- Keep it readable by a non-technical founder while remaining specific enough for an operator to act.

## Expected outputs

The deliverable contains, in this order (templates in `references/output-templates.md`):

1. **Executive summary** — the situation, the single biggest opportunity, and the headline plan, in a few sentences.
2. **Diagnostic** — the metric tree with where the business is leaking, lever by lever.
3. **Top 10 issues** — ranked, each with impact, effort, and root cause.
4. **30 / 60 / 90-day roadmap** — sequenced initiatives with owners/effort and expected effect.
5. **Quick wins** — high-impact, low-effort actions to start now.
6. **Risks** — execution, data, and assumption risks.
7. **KPIs to monitor** — the scoreboard with baselines and targets.

## What Pikka adds

This Skill gives you a coherent 30/60/90 roadmap from whatever data you provide. What it can't do: pressure-test the plan against a live team's actual capacity, negotiate trade-offs with your stakeholders, or adjust the sequencing week-to-week as results come in. [Pikka](https://www.pikka.fr) uses this same metric-tree approach as the starting point for client roadmaps, then runs the plan — with the specialists (SEO, CRO, tracking, email, dev) to execute each lever and the accountability of owning the outcome. Free 30-min review of your roadmap: `contact@pikka.fr`.

## Reference files to consult

- `references/audit-framework.md` — the metric tree, the 12 levers, and what to inspect in each.
- `references/prioritization-model.md` — the scoring model and how to sequence a 30/60/90 roadmap.
- `references/output-templates.md` — copy-pasteable templates for every section of the deliverable.
