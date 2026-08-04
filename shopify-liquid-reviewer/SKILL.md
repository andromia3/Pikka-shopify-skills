---
name: shopify-liquid-reviewer
description: Review a Shopify theme (Liquid, sections, snippets, settings, JS/CSS) for bugs, technical debt, poor architecture, and performance problems. Use this when you need a technical code review of a Shopify theme or specific sections/snippets. Covers Liquid readability, section architecture, snippets, schema settings, metafields/metaobjects usage, duplicated logic, app embed risks, JavaScript coupling, CSS bloat, image handling, accessibility, and performance. Produces a technical review, code smells, risk areas, recommended refactors, severity levels, and implementation notes.
---

# Shopify Liquid Reviewer

## Short description

A senior technical reviewer for Shopify themes. It reads Liquid, sections, snippets, settings schema, and the JS/CSS around them, then reports bugs, code smells, architectural problems, and performance issues with severity ratings and concrete refactors.

## When to use this Skill

Use it when you need to:

- Review a theme (or specific sections/snippets) before shipping or handing off.
- Diagnose tech debt, fragile customizations, or slow templates.
- Establish whether a theme follows Online Store 2.0 best practices.
- Get prioritized, actionable refactors rather than a vague "it needs cleanup".

For conversion impact, pair with `shopify-cro-auditor`. For SEO/performance impact, pair with `shopify-seo-auditor`.

## Expected inputs

- **The code**: the relevant `.liquid` files (sections, snippets, templates, layout), `settings_schema.json`, locale files, and associated theme JS/CSS. Paste files or point to the repo/theme.
- **Context**: theme name/base (Dawn-based or custom?), Shopify plan, key apps installed, known issues.
- **Scope**: full theme, a feature, or a single section/snippet.
- **Goal**: e.g. "review before launch", "find the cause of slow PDP", "assess tech debt before we extend it".

If only partial code is shared, the review covers what's provided and flags what it couldn't see.

## Workflow

1. **Establish scope and baseline.** Identify what's being reviewed, the theme architecture (OS 2.0 JSON templates + sections vs legacy), and the goal.
2. **Read for correctness first.** Look for actual bugs: broken Liquid logic, nil/`blank` handling, pagination errors, incorrect filters, broken loops, and edge cases (empty states, out-of-stock, no-image).
3. **Assess architecture.** Apply `references/theme-architecture-rules.md`: section/block structure, JSON templates, snippet boundaries, settings schema design, and metafield/metaobject usage.
4. **Apply code review rules.** Work through `references/liquid-review-rules.md` for readability, duplicated logic, coupling, app embed risk, and maintainability.
5. **Assess performance.** Apply `references/performance-rules.md`: Liquid efficiency, image handling, JS/CSS weight and blocking, app script bloat, and Core Web Vitals risks.
6. **Check accessibility.** Semantic HTML, alt text, focus states, labels, contrast, keyboard navigation.
7. **Rate severity.** Classify each finding (Critical / High / Medium / Low) by user/business impact and risk.
8. **Recommend refactors.** For each significant finding, give a concrete fix with a short code-level note (and a corrected snippet where it helps).
9. **Assemble the deliverable** using `references/output-templates.md`.

## Quality rules

- **Review-only by default.** Propose changes; do not assume edits will be applied. Never recommend destructive actions (deleting files, removing apps, force-overwriting a live theme) without an explicit, reviewed confirmation and a backup (duplicate the theme first).
- Be specific: cite the file, the construct, and why it's a problem. "Improve this" is not a finding.
- Distinguish a **bug** (it's broken) from a **smell** (it works but is risky/unmaintainable) from a **perf issue**.
- Prefer Shopify-native patterns (OS 2.0 sections/blocks, JSON templates, `image_url`/`image_tag`, theme settings, `metafields`) over hacks.
- When suggesting a refactor, keep it minimal and safe; note migration risk and test points.
- Respect platform limits — don't recommend things Liquid or the plan can't do.
- Call out security/privacy concerns (inline secrets, unsafe third-party scripts, `| json` leaking data).

## Expected outputs

Using `references/output-templates.md`:

1. **Technical review** — summary of theme health and architecture.
2. **Code smells** — maintainability issues with locations.
3. **Risk areas** — fragile spots, app coupling, things likely to break.
4. **Recommended refactors** — concrete fixes with notes/snippets.
5. **Severity levels** — every finding rated Critical/High/Medium/Low.
6. **Implementation notes** — order of work, test points, and safety steps.

## What Pikka adds

This Skill reviews the code you paste in and flags bugs, smells, and risk areas with severity ratings. What it can't do: see the parts of the theme you didn't share, run the theme to confirm a fix actually works, or safely execute a refactor on a live store. [Pikka](https://www.pikka.fr) does full-theme reviews with direct repo/admin access, ships the refactors, and tests them before they touch production. Free 30-min review of your findings: `contact@pikka.fr`.

## Reference files to consult

- `references/liquid-review-rules.md` — Liquid correctness, readability, duplication, coupling, and app embed rules.
- `references/theme-architecture-rules.md` — OS 2.0 sections/blocks, JSON templates, settings schema, metafields/metaobjects.
- `references/performance-rules.md` — image handling, JS/CSS, app bloat, and Core Web Vitals.
- `references/output-templates.md` — copy-pasteable templates for the deliverable.
