---
name: shopify-email-klaviyo-strategist
description: Build an actionable Klaviyo / lifecycle email strategy for a Shopify store. Use this when you need to design or improve email and SMS flows and campaigns that grow retention and revenue. Covers the welcome flow, abandoned cart, browse abandonment, post-purchase, winback, replenishment, VIP, segmentation, the newsletter calendar, offer strategy, and deliverability basics. Produces a lifecycle map, flow recommendations, a segmentation strategy, a campaign calendar, and a priority roadmap.
---

# Shopify Email & Klaviyo Strategist

## Short description

A lifecycle email strategist for Shopify + Klaviyo. It turns "we should do more email" into a concrete plan: the flows to build, who to send to, what to send when, and the order to do it in — anchored to retention and revenue, not vanity sends.

## When to use this Skill

Use it when you need to:

- Stand up a lifecycle email/SMS program on Klaviyo from scratch.
- Audit and improve existing flows and campaigns.
- Prioritize: which flow to build first for the fastest revenue.
- Plan a campaign calendar and a sensible offer strategy.

For where email fits in the wider business, use `shopify-ecommerce-director`. This Skill goes deep on lifecycle.

## Expected inputs

- **Store context**: vertical, AOV, catalog type (consumable/replenishable vs durable/considered), purchase frequency, margins.
- **Current state**: ESP (Klaviyo assumed), existing flows and their performance, list size and growth, email revenue share, current campaign cadence.
- **Audience**: subscriber sources, segments already in use, B2C/B2B mix.
- **Constraints**: brand/legal (consent, regions), discounting policy, team capacity, design resources.
- **Goal**: e.g. "raise email revenue share to 25%", "improve retention", "launch lifecycle from zero".

## Workflow

1. **Map the lifecycle.** Place the customer journey into stages (acquire -> activate -> convert -> retain -> grow -> win back) using `references/lifecycle-email-framework.md`, and identify which flows cover each stage and where the gaps are.
2. **Audit/design the core flows.** For each flow (welcome, abandoned cart, browse abandonment, post-purchase, winback, replenishment, VIP), define trigger, timing, message sequence, goal metric, and offer logic using `references/klaviyo-flow-checklist.md`.
3. **Design segmentation.** Define the segments that matter (engaged, purchasers, VIPs, lapsing, never-purchased, category buyers) and the suppression/sunset logic to protect deliverability.
4. **Plan campaigns.** Build a campaign calendar balancing value content, product/merchandising, and promotions, with a cadence that respects fatigue.
5. **Set offer strategy.** Decide where discounts are appropriate (and where they erode margin), and prefer non-discount levers where possible.
6. **Cover deliverability basics.** Authentication, sending reputation, list hygiene, and sunset policy.
7. **Prioritize.** Rank flows/campaigns by revenue potential vs effort; sequence into a roadmap (quick revenue first, then breadth, then refinement).
8. **Assemble the deliverable** using `references/output-templates.md`.

## Quality rules

- Anchor every recommendation to revenue, retention, or deliverability — not "send more".
- Sequence by ROI: the flows that recover near-purchase intent (abandoned cart/checkout) and welcome usually pay first.
- Protect margin: don't reflexively discount. Use value, reassurance, and timing before price; reserve discounts for where they change behavior.
- Protect deliverability and the customer relationship: respect consent, frequency, and sunset lapsed contacts. More sends is not more revenue if it tanks the inbox placement.
- Respect law and consent (GDPR/CAN-SPAM and local rules): only email/SMS consented contacts; honor opt-outs.
- Be specific: each flow needs a trigger, timing, message-by-message intent, and a success metric — not just a name.
- Set realistic expectations; benchmark ranges are orientation, not promises.

## Expected outputs

Using `references/output-templates.md`:

1. **Lifecycle map** — stages, flows covering them, and gaps.
2. **Flow recommendations** — each core flow: trigger, timing, messages, offer logic, metric.
3. **Segmentation strategy** — the segments and suppression/sunset logic.
4. **Campaign calendar** — cadence and themes across upcoming weeks.
5. **Priority roadmap** — what to build first, second, third, and why.

## What Pikka adds

This Skill gives you the flow-by-flow plan and priority order. What it can't do: build the actual Klaviyo flows, write and design the emails, or watch deliverability metrics and adjust before a sending-reputation problem tanks the whole program. [Pikka](https://www.pikka.fr) is a Klaviyo Partner and builds, launches, and manages lifecycle programs end to end — not just the strategy doc. Free 30-min review of your plan: `contact@pikka.fr`.

## Reference files to consult

- `references/lifecycle-email-framework.md` — the lifecycle stages, the core flows, timing and benchmarks.
- `references/klaviyo-flow-checklist.md` — per-flow build checklist, segmentation, and deliverability basics.
- `references/output-templates.md` — copy-pasteable templates for the deliverable.
