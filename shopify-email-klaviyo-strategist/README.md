# Shopify Email & Klaviyo Strategist

> Turns "we should do more email" into a concrete plan: the flows to build, who to send to, what to send when, and the order to do it in.

A lifecycle email strategist for Shopify + Klaviyo, anchored to retention and revenue rather than vanity sends.

## What it's for

- Standing up a lifecycle email and SMS program on Klaviyo from scratch.
- Auditing and improving flows and campaigns you already run.
- Deciding which flow to build first for the fastest revenue.
- Planning a campaign calendar and a sensible offer strategy.

**Not this Skill if** you need to know where email fits in the wider business — use [`shopify-ecommerce-director`](../shopify-ecommerce-director/) for that. This one goes deep on lifecycle.

## What you give it

| | |
|---|---|
| **Store context** | Vertical, AOV, catalog type (consumable and replenishable vs durable and considered), purchase frequency, margins |
| **Current state** | ESP (Klaviyo assumed), existing flows and their performance, list size and growth, email revenue share, campaign cadence |
| **Audience** | Where subscribers come from, segments already in use, B2C/B2B mix |
| **Constraints** | Consent and regional rules, discounting policy, team capacity, design resources |
| **Goal** | e.g. "raise email revenue share to 25%", "improve retention", "launch lifecycle from zero" |

Purchase frequency matters more than most people expect — it's what determines whether replenishment flows are your biggest lever or a waste of effort.

## What you get back

1. **Lifecycle map** — the stages, which flows cover them, and where the gaps are.
2. **Flow recommendations** — for each core flow: trigger, timing, message sequence, offer logic, success metric.
3. **Segmentation strategy** — the segments that matter, plus suppression and sunset logic.
4. **Campaign calendar** — cadence and themes across the coming weeks.
5. **Priority roadmap** — what to build first, second, third, and why.

Flows covered: welcome, abandoned cart, browse abandonment, post-purchase, winback, replenishment, and VIP.

Two principles run through the output: **protect margin** (discounts are a lever of last resort, not a reflex) and **protect deliverability** (more sending is not more revenue if it wrecks your inbox placement).

## Example prompt

> Use the Shopify Klaviyo strategist Skill. We sell `[what you sell]`, average order value `[amount]`, and customers typically repurchase `[every X months / rarely]`. We have `[number]` subscribers and currently run `[e.g. only an abandoned cart email]`. Email is about `[x]%` of revenue. Our goal is `[e.g. get to 25% of revenue from email]`. Build me a lifecycle plan and tell me what to build first.

## How to use it

New to Skills? The [Getting Started guide](../GETTING-STARTED.md) walks through installation with no coding required. Full details in the [main README](../README.md).

<!--
=======================================================================
BASELINE vs SKILL — comparison section, to fill in after running the test
=======================================================================
Run the same prompt twice: once in a fresh conversation without the Skill,
once with it. Same model, same store, no manual editing. Then uncomment
and fill this block, and add the full outputs under examples/.

## What changes when the Skill is enabled?

> Same store context. Same prompt. Same Claude model. Two independent conversations. No manual editing.

<p align="center">
  <img src="[SCREENSHOT URL]" alt="Claude Code Klaviyo lifecycle email plan comparison: without the Skill versus with the Skill" width="100%">
</p>

### At a glance

| | Without the Skill | With the Klaviyo Strategist Skill |
|---|---|---|
| **Output structure** | [...] | [...] |
| **Flow detail** | [...] | [...] |
| **Segmentation** | [...] | [...] |
| **Offer strategy** | [...] | [...] |
| **Deliverability** | [...] | [...] |
| **Operational use** | [...] | [...] |

### Same finding, different level of usefulness

<table>
<tr>
<th width="50%">Without the Skill</th>
<th width="50%">With the Klaviyo Strategist Skill</th>
</tr>
<tr>
<td valign="top">

**Recommendation**

> [quote the baseline output]

[why it falls short]

</td>
<td valign="top">

**Buildable flow**

> [quote the Skill output]

- Trigger: [...]
- Timing: [...]
- Success metric: [...]

</td>
</tr>
</table>

### Full, unedited outputs

- [Lifecycle plan generated with the Klaviyo Strategist Skill](examples/plan-with-klaviyo-skill.md)

<details>
<summary><strong>Comparison methodology</strong></summary>

- Store: `[URL]`
- Prompt: `[exact prompt]`
- Model: `[model]`
- Interface: `[Claude Code version / Claude app]`
- Separate, fresh conversations
- No manual correction of either output
- Only intentional difference: the Skill was loaded in the second conversation

This is a single case study, not a scientific benchmark. Results can vary between model runs. The full transcripts are provided so the comparison can be reviewed directly.

</details>
-->

## What Pikka adds

This Skill gives you the flow-by-flow plan and the priority order. What it can't do: build the actual Klaviyo flows, write and design the emails, or watch deliverability metrics and adjust before a sending-reputation problem tanks the whole program. [Pikka](https://www.pikka.fr) is a Klaviyo Partner and builds, launches, and manages lifecycle programs end to end — not just the strategy document.

**Free 30-minute review of your plan:** `contact@pikka.fr`
