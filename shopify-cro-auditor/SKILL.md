---
name: shopify-cro-auditor
description: Audit a Shopify store for conversion rate optimization. Use this when you want to find and prioritize the friction that stops visitors from buying. Covers the home page, collection pages, product pages, cart, checkout limitations, mobile UX, trust signals, product reassurance, objections, reviews, merchandising, speed perception, and A/B test ideas. Produces a conversion diagnosis, a page-by-page audit, friction points, quick wins, a test backlog, and an impact/effort prioritization.
---

# Shopify CRO Auditor

## Short description

A structured conversion audit for Shopify stores. It walks the buying journey page by page, identifies the friction and unanswered objections that cost conversions, and turns them into quick wins and a prioritized test backlog.

## When to use this Skill

Use it when you need to:

- Understand why a store converts below its potential.
- Get a page-by-page list of conversion problems with fixes.
- Build a prioritized CRO test backlog (not random "best practices").
- Prepare for a redesign or a conversion sprint.

For measurement reliability (is the conversion number even trustworthy?), pair with `shopify-tracking-ga4-auditor`. For a whole-business view, use `shopify-ecommerce-director`.

## Expected inputs

- **Store URL** and key templates to review (home, top collections, top products).
- **Conversion data** if available: overall CVR, CVR by device, funnel drop-off (view -> ATC -> checkout -> purchase), top landing pages.
- **Qualitative data** if available: session recordings, heatmaps, on-site survey answers, support tickets, common objections.
- **AOV, returns rate, and product type** (considered vs impulse purchase changes the playbook).
- **Constraints**: Shopify plan (affects checkout customization), apps installed, brand guidelines.
- **Goal**: e.g. "lift mobile CVR", "reduce cart abandonment", "improve PDP add-to-cart rate".

## Workflow

1. **Frame the funnel.** Summarize where conversion leaks the most (device, step, page type) using data if provided; if not, state assumptions and reason from the journey.
2. **Audit page by page.** Using `references/page-analysis-framework.md`, evaluate each stage: home, collection, product, cart, and the pre-checkout experience. Note what helps and what blocks conversion.
3. **Run the CRO checklist.** Work through `references/cro-checklist.md` across all areas (trust, reassurance, objections, reviews, merchandising, mobile UX, speed perception).
4. **Identify friction and objections.** For each page, list the specific friction points and the unanswered buyer objections (cost, fit, trust, timing, risk).
5. **Separate quick wins from tests.** Quick wins are near-certain improvements (clear bugs, missing trust elements, broken mobile layouts). Uncertain-but-promising ideas become hypotheses to test.
6. **Build the test backlog.** Write each as a hypothesis with a metric, and prioritize with an impact/effort (or PIE/ICE) score.
7. **Assemble the deliverable** using `references/output-templates.md`.

## Quality rules

- Anchor findings to the buyer's decision, not to generic "best practices". Every recommendation should reduce a real friction or answer a real objection.
- Respect Shopify checkout reality: on non-Plus plans the checkout is largely fixed. Don't propose checkout changes the plan can't support; focus on pre-checkout and cart, and on the levers that are available (Shop Pay, express checkout, accelerated buttons, checkout settings).
- Prefer evidence (recordings, data) over opinion; when reasoning from heuristics, say so.
- Frame test ideas as hypotheses with a measurable metric, not as guaranteed wins.
- Prioritize mobile — it's usually the majority of traffic and the weakest experience.
- Don't recommend dark patterns (fake scarcity, forced urgency, misleading pricing). They harm trust and can breach consumer law.

## Expected outputs

Using `references/output-templates.md`:

1. **Conversion diagnosis** — where and why the funnel leaks.
2. **Page-by-page audit** — home, collection, product, cart, pre-checkout, mobile.
3. **Friction points** — specific blockers and unanswered objections.
4. **Quick wins** — high-confidence, low-effort fixes to ship now.
5. **Test backlog** — prioritized hypotheses with metrics.
6. **Impact / effort prioritization** — the matrix and ranked shortlist.

## What Pikka adds

This Skill turns your inputs into a page-by-page friction list and test backlog. What it can't do: watch real session recordings itself, run the A/B tests it proposes, or know which "quick win" will actually hold up once shipped to your traffic. [Pikka](https://www.pikka.fr) pairs this framework with hands-on session review, test implementation, and statistically sound read-outs — then iterates based on what the data actually shows. Free 30-min review of your audit output: `contact@pikka.fr`.

## Reference files to consult

- `references/cro-checklist.md` — the full conversion checklist across all areas.
- `references/page-analysis-framework.md` — what to evaluate on each page type and how to spot friction.
- `references/output-templates.md` — copy-pasteable templates for the deliverable.
