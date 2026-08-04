# Shopify Tracking & GA4 Auditor

> Bad tracking quietly corrupts every decision downstream — conversion rate, ROAS, attribution.

This Skill verifies that the right events fire once, with the right data, under the right consent, and turns the gaps into a clean tracking plan.

## What it's for

- Trusting your numbers before optimizing conversion, scaling paid, or judging a channel.
- Diagnosing mismatches between GA4, Shopify, and ad platforms — duplicate conversions, missing events.
- Validating consent mode and privacy compliance.
- Producing a tracking plan and QA checklist your developer can implement.

**Run this first.** It's usually a prerequisite for [`shopify-cro-auditor`](../shopify-cro-auditor/), [`shopify-ecommerce-director`](../shopify-ecommerce-director/), and any paid-media decision — optimizing against numbers you can't trust wastes the effort.

## What you give it

| | |
|---|---|
| **Store** | URL and Shopify plan |
| **Current setup** | GA4 measurement ID, how GA4 is installed (Google & YouTube app, Shopify custom pixel, GTM, hardcoded), GTM container, ad platform tags, other tools |
| **Consent setup** | Cookie banner / CMP in use, regions, whether Consent Mode v2 is configured |
| **Symptoms** | e.g. "GA4 purchases don't match Shopify orders", "Ads conversions look doubled", "EU traffic shows no data" |
| **Evidence** | GA4 DebugView or Realtime output, tag setup screenshots, pixel or GTM config |
| **Goal** | e.g. "trustworthy GA4 e-commerce", "fix double-counting", "make tracking consent-compliant" |

**Never paste credentials or tokens.** The Skill works from configuration and debug output, and will not ask for access.

## What you get back

1. **Measurement diagnosis** — current stack, how far you can trust it, headline problems.
2. **Event coverage table** — for each event: present? fires correctly? parameters OK? which source.
3. **Duplicate tracking risks** — where double-counting happens and how to fix it.
4. **Consent risks** — CMP and Consent Mode gaps, and the compliance exposure.
5. **Recommended tracking plan** — target state, which tool owns which event, required parameters.
6. **QA checklist** — how to validate the implementation in DebugView, Realtime, and Tag Assistant.

The governing rule is **one event, one source.** Most Shopify tracking problems come from overlapping mechanisms — GA4 loaded via both the Google & YouTube app *and* a custom pixel, for instance — and every path that can double-count gets flagged.

## Example prompt

> Use the Shopify tracking GA4 auditor Skill. Store is `[yourstore.com]` on `[Shopify plan]`. GA4 is installed via `[Google & YouTube app / custom pixel / GTM / hardcoded]`, and we also run `[Meta pixel, Google Ads tag, etc.]`. Our CMP is `[name]` and we sell into `[regions]`. The problem: `[e.g. GA4 shows 15% more purchases than Shopify]`. Audit our measurement and give me a tracking plan.

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
  <img src="[SCREENSHOT URL]" alt="Claude Code Shopify GA4 tracking audit comparison: without the Skill versus with the Skill" width="100%">
</p>

### At a glance

| | Without the Skill | With the Tracking Auditor Skill |
|---|---|---|
| **Output structure** | [...] | [...] |
| **Event coverage** | [...] | [...] |
| **Duplicate detection** | [...] | [...] |
| **Consent handling** | [...] | [...] |
| **Shopify specificity** | [...] | [...] |
| **Operational use** | [...] | [...] |

### Same finding, different level of usefulness

<table>
<tr>
<th width="50%">Without the Skill</th>
<th width="50%">With the Tracking Auditor Skill</th>
</tr>
<tr>
<td valign="top">

**Observation**

> [quote the baseline output]

[why it falls short]

</td>
<td valign="top">

**Diagnosed cause**

> [quote the Skill output]

- Source: [...]
- Fix: [...]
- Validation: [...]

</td>
</tr>
</table>

### Full, unedited outputs

- [Tracking audit generated with the Tracking Auditor Skill](examples/audit-with-tracking-skill.md)

<details>
<summary><strong>Comparison methodology</strong></summary>

- Store audited: `[URL]`
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

This Skill maps your stack and flags where events are missing, duplicated, or consent-non-compliant, from the configuration you describe. What it can't do: open GA4 DebugView itself, watch a live purchase fire through your actual checkout, or implement the fixes in GTM and your pixel setup. [Pikka](https://www.pikka.fr) does the hands-on validation and implementation, then keeps monitoring so a broken tag doesn't quietly corrupt three months of decisions.

**Free 30-minute review of your audit:** `contact@pikka.fr`
