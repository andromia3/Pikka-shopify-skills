# Shopify Migration SEO Guardian

> Replatforming is the single most common way for an e-commerce store to lose organic traffic overnight.

This Skill makes a migration to Shopify safe: it inventories what exists, maps everything to the new structure, and enforces the checks that prevent traffic loss before, during, and after go-live.

## What it's for

- Moving a store to Shopify from PrestaShop, WooCommerce, Magento, BigCommerce, or a custom CMS.
- Any replatforming or redesign that changes URLs.
- Producing a migration plan the dev, SEO, and content teams can all follow.
- Diagnosing and recovering from a migration that already caused a traffic drop.

**Not this Skill if** your URLs aren't changing — use [`shopify-seo-auditor`](../shopify-seo-auditor/) for routine SEO work.

## What you give it

| | |
|---|---|
| **Source platform** | Current platform, store URLs, languages and markets |
| **URL inventory** | Crawl export, XML sitemaps, server logs, CMS export — the more complete, the safer |
| **Search Console + analytics** | Top pages by clicks and impressions, top organic landing pages, most-linked pages |
| **New structure** | Planned Shopify collections, products, pages, blog, theme, markets config |
| **Timeline** | Go-live date and freeze windows |
| **Constraints** | Redirect tooling, DNS access, whether the old site can stay up briefly |

The URL inventory is the input that matters most. Every old URL with traffic, backlinks, or conversions must be accounted for.

## What you get back

1. **Migration risk assessment** — risk profile and the highest-exposure areas.
2. **Redirect mapping framework** — rules plus the mapping table (old URL → new URL → type).
3. **Pre-launch checklist** — everything to validate on staging before go-live.
4. **Go-live checklist** — the ordered launch-day runbook.
5. **Post-launch monitoring plan** — what to watch, when, and the thresholds that trigger action.

The Skill enforces a hard rule throughout: **no valued URL is ever lost silently.** Every one is mapped to a 301 or deliberately retired.

## Example prompt

> Use the Shopify migration SEO guardian Skill. We're migrating `[yourstore.com]` from `[PrestaShop/WooCommerce/Magento/other]` to Shopify, going live around `[date]`. We have roughly `[number]` products, `[number]` categories, and `[number]` blog posts, in `[languages/markets]`. Here's our crawl export and our top organic landing pages. What's our risk profile and what's the redirect plan?

## How to use it

New to Skills? The [Getting Started guide](../GETTING-STARTED.md) walks through installation with no coding required. Full details in the [main README](../README.md).

**If you're mid-migration and something already looks wrong, don't wait for a full audit** — the recovery window matters. See below.

<!--
=======================================================================
BASELINE vs SKILL — comparison section, to fill in after running the test
=======================================================================
Run the same prompt twice: once in a fresh conversation without the Skill,
once with it. Same model, same store, no manual editing. Then uncomment
and fill this block, and add the full outputs under examples/.

## What changes when the Skill is enabled?

> Same migration scenario. Same prompt. Same Claude model. Two independent conversations. No manual editing.

<p align="center">
  <img src="[SCREENSHOT URL]" alt="Claude Code Shopify migration plan comparison: without the Skill versus with the Skill" width="100%">
</p>

### At a glance

| | Without the Skill | With the Migration Guardian Skill |
|---|---|---|
| **Output structure** | [...] | [...] |
| **URL coverage** | [...] | [...] |
| **Redirect rules** | [...] | [...] |
| **Launch-day process** | [...] | [...] |
| **Post-launch** | [...] | [...] |
| **Operational use** | [...] | [...] |

### Same finding, different level of usefulness

<table>
<tr>
<th width="50%">Without the Skill</th>
<th width="50%">With the Migration Guardian Skill</th>
</tr>
<tr>
<td valign="top">

**Recommendation**

> [quote the baseline output]

[why it falls short]

</td>
<td valign="top">

**Mapped rule**

> [quote the Skill output]

- [redirect type / edge case / validation step]

</td>
</tr>
</table>

### Full, unedited outputs

- [Migration plan generated with the Migration Guardian Skill](examples/migration-plan-with-skill.md)

<details>
<summary><strong>Comparison methodology</strong></summary>

- Store migrated: `[URL]`
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

This Skill gives you the risk assessment and mapping framework — the part that's easy to get wrong under deadline pressure. What it can't do: execute the redirect map, watch rankings in real time on go-live day, or make the judgment call at 2am when something's off. [Pikka](https://www.pikka.fr) has run this playbook across real Shopify migrations and stays on post-launch monitoring until traffic is confirmed stable.

**If you're mid-migration and something looks wrong, don't wait:** `contact@pikka.fr`
