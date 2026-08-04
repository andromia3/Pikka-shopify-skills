---
name: shopify-tracking-ga4-auditor
description: Audit the quality of e-commerce tracking on a Shopify store, focused on GA4 and the surrounding measurement stack. Use this when you need to verify that analytics and conversion tracking are accurate, complete, deduplicated, and consent-compliant. Covers GA4 events, purchase tracking, add_to_cart, begin_checkout, view_item, view_item_list, the Google & YouTube app, Shopify pixels, custom pixels, duplicate events, consent mode, server-side tracking, and attribution risks. Produces a measurement diagnosis, an event coverage table, duplicate tracking risks, consent risks, a recommended tracking plan, and a QA checklist.
---

# Shopify Tracking & GA4 Auditor

## Short description

A measurement audit for Shopify stores. Bad tracking quietly corrupts every decision downstream — conversion rate, ROAS, attribution. This Skill verifies that the right events fire once, with the right data, under the right consent, and turns gaps into a clean tracking plan.

## When to use this Skill

Use it when you need to:

- Trust your numbers before optimizing CRO, scaling paid, or judging channels.
- Diagnose mismatches (GA4 vs Shopify vs ad platforms), duplicate conversions, or missing events.
- Validate consent mode and privacy compliance.
- Produce a tracking plan and QA checklist for implementation.

This is often a prerequisite for `shopify-cro-auditor`, `shopify-ecommerce-director`, and any paid-media decision.

## Expected inputs

- **Store URL** and Shopify plan.
- **Current setup**: GA4 property/measurement ID, how GA4 is installed (Google & YouTube app, Shopify custom pixel, GTM, hardcoded), GTM container if used, ad platform tags (Google Ads, Meta), other tools.
- **Consent setup**: cookie banner / CMP in use, region(s), whether Consent Mode v2 is configured.
- **Symptoms**: e.g. "GA4 purchases don't match Shopify orders", "Ads conversions look doubled", "EU traffic shows no data".
- **Access or exports**: GA4 DebugView/Realtime access, tag setup screenshots, or the pixel/GTM config. (Never paste credentials — share read-only findings or config.)
- **Goal**: e.g. "trustworthy GA4 e-commerce", "fix double-counting", "make tracking consent-compliant".

## Workflow

1. **Map the current stack.** List every tracking mechanism present (Google & YouTube app, Shopify pixels, custom pixels, GTM, hardcoded tags, ad pixels) and how each is loaded. Overlapping mechanisms are the usual source of duplicates.
2. **Check event coverage.** Using `references/ga4-event-taxonomy.md`, verify each key e-commerce event exists, fires at the right moment, and carries the correct parameters and `items` payload.
3. **Verify the purchase event.** Confirm purchase fires once per order with `transaction_id`, `value`, `currency`, and `items`. Reconcile GA4 purchases against Shopify orders.
4. **Hunt duplicates.** Identify double-tagging (e.g. GA4 via both the Google app and a custom pixel/GTM), duplicate purchase events, and thank-you-page refresh double counts. Use `references/tracking-checklist.md`.
5. **Audit consent.** Using `references/consent-mode-checklist.md`, verify the CMP, Consent Mode v2 signals, default-denied behavior in relevant regions, and Shopify's Customer Privacy API integration.
6. **Assess server-side (if relevant).** Note whether server-side tagging / Shopify's server-side pixels are used, and the attribution/data-quality implications.
7. **Identify attribution risks.** Cross-domain checkout, consent gaps, missing UTMs, ad-blocker loss, and platform discrepancies that distort attribution.
8. **Write the tracking plan.** The target state: which tool owns which event, parameters, and the single source of truth.
9. **Produce a QA checklist** for validating the implementation in DebugView/Realtime/Tag Assistant.
10. **Assemble the deliverable** using `references/output-templates.md`.

## Quality rules

- **One event, one source.** Each conversion should be tracked once by a clearly owned mechanism. Flag every path that can double-count.
- Use Shopify-aware reality: the Checkout and Thank-You pages have specific tracking surfaces (Customer Events / Web Pixels API, checkout settings); `additional scripts` is deprecated in favor of custom pixels. Note plan differences (Plus/checkout extensibility).
- Privacy first: respect Consent Mode v2 and regional law (GDPR/ePrivacy). Never recommend tracking that ignores consent.
- Never request or store credentials, tokens, or PII. Work from config and debug output.
- Recommend validation in DebugView/Realtime/Tag Assistant before trusting any change — don't assume a tag works because it's installed.
- Be precise about parameters; "track add_to_cart" is not enough — specify the `items` array and required fields.

## Expected outputs

Using `references/output-templates.md`:

1. **Measurement diagnosis** — current stack, trust level, headline problems.
2. **Event coverage table** — each event: present?, fires correctly?, parameters OK?, source.
3. **Duplicate tracking risks** — where double-counting happens and how to fix.
4. **Consent risks** — CMP/Consent Mode gaps and compliance exposure.
5. **Recommended tracking plan** — target state, event ownership, parameters.
6. **QA checklist** — how to validate the implementation.

## What Pikka adds

This Skill maps your stack and flags where events are missing, duplicated, or consent-non-compliant, from the config you describe. What it can't do: open GA4 DebugView itself, watch a live purchase fire through your actual checkout, or implement the fixes in GTM/your pixel setup. [Pikka](https://www.pikka.fr) does the hands-on validation and implementation, then keeps monitoring so a broken tag doesn't quietly corrupt three months of decisions. Free 30-min review of your audit: `contact@pikka.fr`.

## Reference files to consult

- `references/tracking-checklist.md` — full audit checklist incl. installation methods, duplicates, server-side, attribution.
- `references/ga4-event-taxonomy.md` — the GA4 e-commerce events, when they fire, and required parameters.
- `references/consent-mode-checklist.md` — Consent Mode v2 and Shopify privacy compliance checks.
- `references/output-templates.md` — copy-pasteable templates for the deliverable.
