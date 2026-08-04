# Shopify E-commerce Director

> A senior e-commerce director in a box. Thirty things to fix, and you need the ten that matter.

This Skill synthesizes everything known about a Shopify store into one coherent, prioritized growth plan. It does not go deep on a single channel — it connects the dots across the whole business and tells you where to focus first.

## What it's for

- Making sense of scattered data, audits, and opinions, and turning them into a single plan.
- Prioritizing when everything looks urgent.
- Building a 30/60/90-day roadmap for a store, a quarter, or a new client.
- Briefing a team, a founder, or a board on where the growth is and what's blocking it.

**Not this Skill if** you need a deep single-channel audit. Run [`shopify-seo-auditor`](../shopify-seo-auditor/), [`shopify-cro-auditor`](../shopify-cro-auditor/), or [`shopify-tracking-ga4-auditor`](../shopify-tracking-ga4-auditor/) first, then feed their output into this one.

## What you give it

| | |
|---|---|
| **Store basics** | URL, vertical, catalog size, AOV, main markets, B2C/B2B, Shopify plan |
| **Performance** | Sessions, conversion rate, revenue, AOV, returning customer rate, channel mix — 12 months and YoY if you have it |
| **Margin** | Blended gross margin, target CAC, shipping and return economics |
| **Channel detail** | Paid spend and ROAS, email revenue share, SEO traffic trend |
| **Existing audits** | Any SEO, CRO, tracking, or tech review already done |
| **Constraints** | Budget, team size, stack, timeline, what you already tried |
| **Goal** | The business objective, e.g. "+30% revenue in 6 months at stable margin" |

Provide what you have. The Skill works with partial data, marks what it assumed, and states what would change the plan.

## What you get back

1. **Executive summary** — the situation, the single biggest opportunity, the headline plan.
2. **Diagnostic** — a metric tree showing where the business leaks, lever by lever.
3. **Top 10 issues** — ranked, each with impact, effort, and root cause.
4. **30/60/90-day roadmap** — sequenced initiatives, respecting dependencies.
5. **Quick wins** — high-impact, low-effort actions to start now.
6. **Risks** — execution, data, and assumption risks.
7. **KPIs to monitor** — the scoreboard, with baselines and targets.

The analysis runs across 12 levers: traffic, conversion, AOV, retention, margin, SEO, paid acquisition, email/lifecycle, UX, merchandising, tracking, and technical debt.

## Example prompt

> Use the Shopify e-commerce director Skill. We sell `[what you sell]` at `[AOV]` average order value. Monthly revenue is around `[amount]`, traffic `[sessions/month]`, conversion rate `[x]%`, returning customer rate `[x]%`. Channel mix is roughly `[organic/paid/email/direct split]`. Gross margin is `[x]%`. Team and budget: `[describe]`. What should we do over the next 90 days?

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

> Same Shopify store. Same prompt. Same Claude model. Two independent conversations. No manual editing.

<p align="center">
  <img src="[SCREENSHOT URL]" alt="Claude Code Shopify growth roadmap comparison: without the Skill versus with the Skill" width="100%">
</p>

### At a glance

| | Without the Skill | With the E-commerce Director Skill |
|---|---|---|
| **Output structure** | [...] | [...] |
| **Evidence chain** | [...] | [...] |
| **Prioritization** | [...] | [...] |
| **Sequencing** | [...] | [...] |
| **Method discipline** | [...] | [...] |
| **Operational use** | [...] | [...] |

### Same finding, different level of usefulness

<table>
<tr>
<th width="50%">Without the Skill</th>
<th width="50%">With the E-commerce Director Skill</th>
</tr>
<tr>
<td valign="top">

**Recommendation**

> [quote the baseline output]

[why it falls short]

</td>
<td valign="top">

**Prioritized initiative**

> [quote the Skill output]

- [impact / effort / dependency detail]

</td>
</tr>
</table>

### Full, unedited outputs

- [Roadmap generated with the E-commerce Director Skill](examples/roadmap-with-director-skill.md)

<details>
<summary><strong>Comparison methodology</strong></summary>

- Store analyzed: `[URL]`
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

This Skill gives you a coherent 30/60/90 roadmap from whatever data you provide. What it can't do: pressure-test the plan against a live team's actual capacity, negotiate trade-offs with your stakeholders, or adjust the sequencing week-to-week as results come in. [Pikka](https://www.pikka.fr) uses this same metric-tree approach as the starting point for client roadmaps, then runs the plan — with the specialists (SEO, CRO, tracking, email, dev) to execute each lever and the accountability of owning the outcome.

**Free 30-minute review of your roadmap:** `contact@pikka.fr`
