# E-commerce Diagnostic Framework

This is the analytical backbone of the Skill. Work top-down: start from the metric tree, then inspect each of the 12 levers, then convert findings into ranked issues.

## 1. The revenue metric tree

Decompose revenue so every issue maps to a number you can move.

```
Revenue
= Sessions x Conversion Rate x Average Order Value
```

Then layer the dimensions that determine whether that revenue is profitable and repeatable:

```
Customer LTV  = AOV x Purchase Frequency x Gross Margin x Customer Lifespan
Contribution  = Revenue x Gross Margin - Variable Costs (shipping, returns, payment fees) - CAC
Growth        = New Customers + Returning Customers - Churned Customers
```

For each node, capture three things:

- **Current value** (last 12 months, plus YoY and trend).
- **Reference point** — the store's own history and a sensible benchmark for the vertical/AOV.
- **Gap** — where is the biggest, most credible gap between current and potential?

The biggest gap with the highest confidence is usually where the plan should start.

## 2. Benchmark sanity ranges

Use these as rough orientation only. Always weight the store's own trend and vertical over any external number.

| Metric | Typical orientation range | Notes |
| --- | --- | --- |
| Conversion rate (overall) | 1.5%-3.5% | Higher for strong brands/low AOV; lower for high-AOV/considered purchases. |
| Mobile vs desktop CVR | Mobile often 40-60% of desktop | A large gap signals mobile UX/perf issues. |
| Returning customer rate | 20%-35% | Below ~20% suggests weak retention/lifecycle. |
| Email revenue share | 15%-30% | Below ~10% usually means flows are missing or weak. |
| Paid ROAS | Varies widely | Judge against contribution margin, not a fixed target. |
| Add-to-cart rate | 5%-12% | Low ATC points to PDP/merchandising/pricing issues. |
| Checkout completion | 45%-65% | Below ~40% points to shipping cost, trust, or payment options. |

## 3. The 12 levers

For each lever: state current state, cite evidence, name the likely root cause, and note the data you'd want to confirm it.

### 1. Traffic
- Channel mix and trend (organic, paid, email, direct, social, referral).
- Concentration risk (over-reliance on one channel or one campaign).
- Quality of traffic (bounce, engaged sessions, CVR by channel).

### 2. Conversion
- Overall and by device, channel, and landing page type (home, collection, PDP, search).
- Funnel drop-off: session -> product view -> add to cart -> checkout -> purchase.
- The biggest single drop is the first place to look.

### 3. Average Order Value (AOV)
- Distribution of order values, units per order, attach rate.
- Cross-sell/upsell presence, bundles, free-shipping threshold positioning.

### 4. Retention
- Returning customer rate, repeat purchase interval, cohort retention curves.
- First-to-second purchase conversion (the hardest and most valuable step).

### 5. Margin
- Blended gross margin; margin by category; discount depth and frequency.
- Shipping and returns economics; payment fees; the true contribution per order.

### 6. SEO
- Organic traffic trend, indexation health, share of non-brand traffic.
- Structural Shopify issues (collections, canonicals, duplicate content). Hand off depth to `shopify-seo-auditor`.

### 7. Paid acquisition
- Spend, ROAS/CAC vs contribution margin, channel mix, creative fatigue.
- Whether measurement is trustworthy (see lever 11 before trusting ROAS).

### 8. Email / lifecycle
- Core flows present and performing (welcome, abandoned cart, post-purchase, winback).
- Email revenue share, list growth, deliverability signals. Hand off to `shopify-email-klaviyo-strategist`.

### 9. UX
- Clarity of navigation, search, and core flows; mobile experience; speed perception.
- Friction in cart and pre-checkout. Hand off depth to `shopify-cro-auditor`.

### 10. Merchandising
- Collection logic, sort defaults, filtering, hero placement, out-of-stock handling.
- Whether best-sellers and high-margin products are surfaced.

### 11. Tracking
- Are GA4/ads events firing correctly, deduplicated, and consent-compliant?
- If tracking is broken, every downstream number (CVR, ROAS, attribution) is suspect. Treat this as a prerequisite. Hand off to `shopify-tracking-ga4-auditor`.

### 12. Technical debt
- Theme health, app sprawl, performance, fragile customizations, unsupported dependencies.
- Operational debt: manual processes, inventory accuracy, fulfillment bottlenecks. Hand off to `shopify-liquid-reviewer`.

## 4. From levers to issues

For every weakness found, write it as a structured issue before scoring it:

- **Issue**: one clear sentence.
- **Lever**: which of the 12.
- **Evidence**: the data or observation behind it.
- **Root cause**: the underlying driver, not the symptom.
- **Affected metric**: which node of the metric tree it moves.

Carry these issues into `prioritization-model.md` to rank and sequence them.
