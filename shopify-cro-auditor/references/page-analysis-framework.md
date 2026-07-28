# Page Analysis Framework

How to audit each stage of the Shopify buying journey. For every page, ask the three core questions, then apply the page-specific checks.

## The three core questions (every page)

1. **Clarity** — Within 5 seconds, does the visitor understand what this is, who it's for, and what to do next?
2. **Motivation** — Does the page build desire and answer "why buy this, here, now"?
3. **Friction & anxiety** — What slows the visitor down or creates doubt (cost surprises, missing info, unanswered objections, UX hurdles)?

Good CRO = increase clarity and motivation, reduce friction and anxiety.

## Home page

Purpose: orient, build trust, and route visitors to the right products fast.

- Value proposition clear above the fold (what you sell, for whom, why you).
- Primary navigation and search are obvious.
- Clear paths into top collections / best-sellers / new arrivals.
- Trust established early (social proof, guarantees, brand cues).
- Not a dead-end: every section routes deeper.
- Mobile: hero loads fast, CTA visible, nav usable.

Common friction: vague hero, no clear entry point, slow hero image, too many competing CTAs.

## Collection pages

Purpose: help the visitor find and compare products quickly.

- Useful sort defaults (best-sellers/relevance, not arbitrary).
- Filters that match how people shop (size, price, category, attributes).
- Product cards show what matters (price, rating, key attribute, quick add).
- In-stock items prioritized; out-of-stock demoted.
- Pagination/load-more works smoothly.
- Intro/category context where it helps (also good for SEO).

Common friction: poor sort default, weak/absent filters, cluttered cards, out-of-stock noise.

## Product pages (PDP)

Purpose: answer every objection and make adding to cart effortless.

- Strong gallery (multiple angles, zoom, video, in-context shots).
- Clear title, price, and variant selection (no confusing variant logic).
- Add-to-cart prominent; sticky on mobile.
- Reassurance near the button: shipping, returns, guarantees, stock.
- Objection-answering content: specs, sizing, FAQs, use cases.
- Reviews visible with count and distribution.
- Cross-sell / "complete the look" where relevant.
- Fast load and no layout shift when images/variants load.

Common friction: weak imagery, hidden shipping/returns, buried add-to-cart on mobile, unanswered fit/spec questions, no reviews.

## Cart

Purpose: reassure and move to checkout without surprises.

- Clear line items, quantities, totals.
- Shipping cost / free-shipping progress shown here, not as a checkout surprise.
- Reassurance present (returns, secure payment, delivery estimate).
- Easy edit/remove; obvious, prominent checkout CTA.
- Express checkout available.
- Optional, non-pushy upsell — never blocking checkout.

Common friction: surprise shipping cost, forced steps, weak CTA, no reassurance, intrusive upsells.

## Pre-checkout / checkout (limitations-aware)

Purpose: complete the purchase with minimal effort and maximum trust.

- Express/accelerated checkout (Shop Pay, Apple/Google Pay) enabled.
- Guest checkout allowed.
- Minimal fields; address autocomplete; correct mobile keyboards.
- Payment methods fit the market.
- Note platform limits: deep checkout edits need Shopify Plus (checkout extensibility). On standard plans, optimize settings, payment options, and everything before checkout.

Common friction: forced account creation, too many fields, missing payment methods, no express checkout.

## Mobile lens (apply to every page)

Most traffic is mobile and it usually converts worse. For each page, re-check on a real device: tap targets, sticky CTAs, load speed, no horizontal scroll, readable text, working forms, express checkout.

## Turning findings into hypotheses

For each meaningful friction point, write a testable hypothesis:

> **Because** [observation/evidence], **we believe** [change] **will** [expected effect] **for** [segment/page], **measured by** [primary metric].

High-confidence, low-risk fixes ship as quick wins. Uncertain ideas go to the test backlog and get prioritized by impact/effort.
