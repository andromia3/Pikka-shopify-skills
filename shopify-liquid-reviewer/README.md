# Shopify Liquid Reviewer

> A senior technical reviewer for Shopify themes — not a vague "it needs cleanup".

This Skill reads Liquid, sections, snippets, settings schema, and the JS/CSS around them, then reports bugs, code smells, architectural problems, and performance issues with severity ratings and concrete refactors.

## What it's for

- Reviewing a theme, or specific sections and snippets, before shipping or handing off.
- Diagnosing tech debt, fragile customizations, or slow templates.
- Establishing whether a theme follows Online Store 2.0 best practices.
- Getting prioritized, actionable refactors instead of a list of complaints.

**Pair it with** [`shopify-cro-auditor`](../shopify-cro-auditor/) for conversion impact, or [`shopify-seo-auditor`](../shopify-seo-auditor/) for SEO and performance impact.

## What you give it

| | |
|---|---|
| **The code** | The relevant `.liquid` files (sections, snippets, templates, layout), `settings_schema.json`, locale files, and the theme JS/CSS. Paste them or point to the repo. |
| **Context** | Theme name and base (Dawn-derived or custom?), Shopify plan, key apps installed, known issues |
| **Scope** | Full theme, one feature, or a single section |
| **Goal** | e.g. "review before launch", "find why the PDP is slow", "assess debt before we extend it" |

If you share only part of the theme, the review covers what's provided and explicitly flags what it couldn't see.

## What you get back

1. **Technical review** — theme health and architecture summary.
2. **Code smells** — maintainability issues, with file locations.
3. **Risk areas** — fragile spots, app coupling, things likely to break.
4. **Recommended refactors** — concrete fixes, with corrected snippets where useful.
5. **Severity levels** — every finding rated Critical / High / Medium / Low.
6. **Implementation notes** — order of work, test points, and safety steps.

Findings are separated by kind: a **bug** (it's broken), a **smell** (it works but is risky), and a **performance issue** are not the same thing and aren't treated as such.

## Safety

The Skill is **review-only by default.** It proposes changes rather than assuming they'll be applied, and never recommends destructive actions — deleting files, removing apps, overwriting a live theme — without explicit confirmation and a backup. Duplicate your theme before acting on any refactor.

## Example prompt

> Use the Shopify Liquid reviewer Skill. Here's our `[section/snippet/template]` from a `[Dawn-based/custom]` theme on `[Shopify plan]`. We're seeing `[symptom, e.g. the PDP takes 4s to become interactive on mobile]`. Review it for bugs, tech debt, and performance, and tell me what to fix first.

## How to use it

New to Skills? The [Getting Started guide](../GETTING-STARTED.md) walks through installation with no coding required. Full details in the [main README](../README.md).

<!--
=======================================================================
BASELINE vs SKILL — comparison section, to fill in after running the test
=======================================================================
Run the same prompt twice: once in a fresh conversation without the Skill,
once with it. Same model, same code, no manual editing. Then uncomment
and fill this block, and add the full outputs under examples/.

## What changes when the Skill is enabled?

> Same theme code. Same prompt. Same Claude model. Two independent conversations. No manual editing.

<p align="center">
  <img src="[SCREENSHOT URL]" alt="Claude Code Shopify theme review comparison: without the Skill versus with the Skill" width="100%">
</p>

### At a glance

| | Without the Skill | With the Liquid Reviewer Skill |
|---|---|---|
| **Output structure** | [...] | [...] |
| **Bug vs smell** | [...] | [...] |
| **Severity rating** | [...] | [...] |
| **Shopify specificity** | [...] | [...] |
| **Refactor detail** | [...] | [...] |
| **Operational use** | [...] | [...] |

### Same finding, different level of usefulness

<table>
<tr>
<th width="50%">Without the Skill</th>
<th width="50%">With the Liquid Reviewer Skill</th>
</tr>
<tr>
<td valign="top">

**Observation**

> [quote the baseline output]

[why it falls short]

</td>
<td valign="top">

**Rated finding**

> [quote the Skill output]

- Severity: [...]
- Fix: [...]
- Test point: [...]

</td>
</tr>
</table>

### Full, unedited outputs

- [Theme review generated with the Liquid Reviewer Skill](examples/review-with-liquid-skill.md)

<details>
<summary><strong>Comparison methodology</strong></summary>

- Theme reviewed: `[theme / files]`
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

This Skill reviews the code you paste in and flags bugs, smells, and risk areas with severity ratings. What it can't do: see the parts of the theme you didn't share, run the theme to confirm a fix actually works, or safely execute a refactor on a live store. [Pikka](https://www.pikka.fr) does full-theme reviews with direct repo and admin access, ships the refactors, and tests them before they touch production.

**Free 30-minute review of your findings:** `contact@pikka.fr`
