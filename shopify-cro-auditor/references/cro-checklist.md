# Shopify CRO Checklist

For each item, record: **Status** (Good / Issue / Critical), **Evidence**, **Fix / hypothesis**.

## Trust signals (site-wide)
- [ ] Clear brand identity; the store looks legitimate and cared-for.
- [ ] Visible contact information and a real support channel.
- [ ] Trust badges that are genuine (secure payment, real guarantees) — not fake seals.
- [ ] Transparent shipping, returns, and refund policies, easy to find.
- [ ] Social proof present (reviews, ratings, UGC, press, customer count) and credible.
- [ ] HTTPS, no broken assets, no console errors that scare users.

## Product reassurance
- [ ] Shipping cost and delivery time visible early (ideally before checkout).
- [ ] Returns/exchange policy stated near the buy button.
- [ ] Stock/availability and restock clarity.
- [ ] Guarantees / warranty / satisfaction promises where relevant.
- [ ] Sizing/fit guidance for apparel; specs/compatibility for technical products.
- [ ] Payment options shown (incl. installments where used).

## Objection handling
- [ ] "Is it worth the price?" — value framing, comparisons, bundles.
- [ ] "Will it fit / work for me?" — size guides, specs, use cases.
- [ ] "Can I trust this store?" — reviews, policies, contact, brand.
- [ ] "What if it's wrong?" — returns, guarantees, support.
- [ ] "When will I get it?" — delivery estimate, shipping speed.
- [ ] "Why this vs alternatives?" — differentiation, USPs.

## Reviews
- [ ] Reviews present on PDPs, with count and distribution (not only 5-star).
- [ ] Reviews are credible (verified, photos, dates, responses).
- [ ] Negative reviews handled visibly and gracefully.
- [ ] Review schema implemented honestly (only real reviews).
- [ ] Aggregate rating visible on collection/PDP where it helps.

## Merchandising
- [ ] Collection sort defaults surface best-sellers / high-margin / in-stock items.
- [ ] Filtering and faceting work and match how customers shop.
- [ ] Out-of-stock items are demoted or clearly handled.
- [ ] Cross-sell / upsell / "complete the look" present where it adds value.
- [ ] Promotions and bundles are clear, not confusing.

## Speed perception
- [ ] Fast first paint and quick perceived load (hero image optimized, no layout shift).
- [ ] Skeletons/placeholders rather than blank screens during load.
- [ ] No janky scrolling or slow interactions (INP) on mobile.
- [ ] Images responsive and lazy-loaded below the fold.
- [ ] Heavy apps/scripts not blocking the critical path. (Cross-check `shopify-liquid-reviewer`.)

## Mobile UX
- [ ] Tap targets large enough; no accidental taps.
- [ ] Sticky add-to-cart on PDP for long pages.
- [ ] Mobile navigation and search are easy.
- [ ] Forms are mobile-friendly (correct keyboards, autofill, minimal fields).
- [ ] Express/accelerated checkout (Shop Pay, Apple Pay, Google Pay) enabled.
- [ ] No horizontal scroll, no tiny text, no cut-off content.

## Cart
- [ ] Cart is reachable and clear; line items, quantities, and totals obvious.
- [ ] Shipping cost / free-shipping threshold communicated in cart.
- [ ] Reassurance in cart (returns, secure payment, delivery estimate).
- [ ] Easy quantity edit and remove; no surprise costs later.
- [ ] Clear, prominent path to checkout; express checkout available.

## Checkout (limitations-aware)
- [ ] Accelerated/express checkout enabled (Shop Pay et al.).
- [ ] Guest checkout available (don't force account creation).
- [ ] Only necessary fields; address autocomplete on.
- [ ] Payment methods match the market (incl. local methods).
- [ ] Note: on non-Plus plans, deep checkout customization is limited — focus on settings, payment options, and pre-checkout. On Plus, checkout extensibility allows more.

## A/B test readiness
- [ ] Enough traffic/conversions to detect an effect in reasonable time.
- [ ] Reliable measurement in place (see `shopify-tracking-ga4-auditor`).
- [ ] One primary metric per test; guardrail metrics defined.
