---
name: shopify-migration-seo-guardian
description: Protect SEO and traffic when migrating an e-commerce store to Shopify from PrestaShop, WooCommerce, Magento, or another CMS. Use this when planning or executing a replatforming to avoid losing rankings, redirects, metadata, and structured content. Covers URL inventory, redirect mapping, metadata preservation, collection/category mapping, product variants, images, hreflang, analytics continuity, pre-launch, go-live, and post-launch monitoring. Produces a risk assessment, redirect mapping framework, pre-launch and go-live checklists, and a post-launch monitoring plan.
---

# Shopify Migration SEO Guardian

## Short description

Replatforming is the single most common way for an e-commerce store to lose organic traffic overnight. This Skill makes a migration to Shopify safe: it inventories what exists, maps everything to the new structure, and enforces the checks that prevent traffic loss before, during, and after go-live.

## When to use this Skill

Use it when:

- A store is moving to Shopify from PrestaShop, WooCommerce, Magento, BigCommerce, a custom CMS, or another platform.
- You're replatforming or redesigning in a way that changes URLs.
- You need a migration plan that the dev, SEO, and content teams can all follow.
- A recent migration caused a traffic drop and you need to diagnose and recover.

For routine SEO audits (no URL change), use `shopify-seo-auditor`.

## Expected inputs

- **Source platform** and store URL(s); languages/markets.
- **Full URL inventory** from the old site: crawl export, XML sitemaps, server logs, and/or CMS export. The more complete, the safer.
- **Search Console + analytics** for the old site: top pages by clicks/impressions, top organic landing pages, top linked pages (backlinks).
- **New Shopify structure**: planned collections, products, pages, blog; theme; markets config.
- **Timeline**: planned go-live date and freeze windows.
- **Constraints**: redirect tooling available, access to DNS, ability to keep the old site briefly.

## Workflow

1. **Assess risk.** Score the migration's risk profile (URL change scope, traffic concentration, backlink exposure, market complexity) using `references/migration-checklist.md`. State what's most at risk.
2. **Build the URL inventory.** Consolidate every old URL from crawl + sitemaps + GSC + logs into one master list. Prioritize by traffic, backlinks, and conversions. No URL with value should be lost silently.
3. **Map old to new.** Using `references/redirect-mapping-framework.md`, map every valued old URL to its best new Shopify equivalent (301). Define rules for products, categories->collections, CMS pages, blog, and parameter/filter URLs. Decide what to redirect, what to retire (410), and what has no equivalent.
4. **Preserve metadata and content.** Plan migration of titles, meta descriptions, headings, structured data, image alt text, and unique product/category copy. Avoid regressing to platform defaults.
5. **Handle products, variants, and images.** Map variants correctly (avoid creating duplicate or orphaned URLs), preserve image quality and alt text, and keep handles clean.
6. **Plan international (if relevant).** Map hreflang clusters from old to new; ensure reciprocal annotations survive.
7. **Ensure analytics continuity.** Plan GA4/tracking setup on Shopify so data doesn't break at launch and pre/post comparison is possible. (Hand depth to `shopify-tracking-ga4-auditor`.)
8. **Run pre-launch checks.** Validate redirects on staging, crawl the new site, verify canonicals/sitemaps/robots, and confirm metadata. Use `references/migration-checklist.md`.
9. **Execute go-live checks.** Follow `references/go-live-checklist.md` in order on launch day.
10. **Monitor post-launch.** Track indexation, redirects, rankings, and traffic on the schedule in the output template; catch and fix regressions fast.
11. **Assemble the deliverable** using `references/output-templates.md`.

## Quality rules

- **Never lose a valued URL silently.** Every old URL with traffic, backlinks, or conversions must be mapped to a 301 or deliberately retired.
- **301, not 302**, for permanent moves. Avoid redirect chains and loops; redirect directly to the final destination.
- **No destructive steps without confirmation.** Do not recommend taking down the old site, changing DNS, or bulk-editing redirects without an explicit, reviewed go/no-go and a rollback plan.
- Keep the old site crawlable until redirects are confirmed working, where feasible.
- Validate everything on staging before launch; re-validate live.
- Set realistic expectations: even a clean migration can see temporary fluctuation while Google reprocesses. The goal is to minimize and recover quickly, not to promise zero movement.

## Expected outputs

Using `references/output-templates.md`:

1. **Migration risk assessment** — risk profile and the highest-exposure areas.
2. **Redirect mapping framework** — rules and the mapping table (old URL -> new URL -> type).
3. **Pre-launch checklist** — everything validated on staging before go-live.
4. **Go-live checklist** — the ordered launch-day runbook.
5. **Post-launch SEO monitoring plan** — what to watch, when, and the thresholds that trigger action.

## What Pikka adds

This Skill gives you the risk assessment and mapping framework — the part that's easy to get wrong under deadline pressure. What it can't do: execute the redirect map, watch rankings in real time on go-live day, or make the judgment call at 2am when something's off. [Pikka](https://www.pikka.fr) has run this playbook across real Shopify migrations and stays on the post-launch monitoring until traffic is confirmed stable. If you're mid-migration and something looks wrong, don't wait: `contact@pikka.fr`.

## Reference files to consult

- `references/migration-checklist.md` — risk scoring, URL inventory method, and the full pre-launch checklist.
- `references/redirect-mapping-framework.md` — how to map old URLs to Shopify, redirect rules, and edge cases.
- `references/go-live-checklist.md` — the launch-day runbook, in order.
- `references/output-templates.md` — copy-pasteable templates for every deliverable.
