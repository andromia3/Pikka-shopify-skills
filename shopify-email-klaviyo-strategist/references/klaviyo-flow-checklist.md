# Klaviyo Flow, Segmentation & Deliverability Checklist

Practical build/audit checklist. For each item: **Status**, **Note/fix**.

## 1. Per-flow build checklist

For every flow, confirm:

- [ ] **Trigger** is correct and specific (right metric/event, e.g. "Started Checkout" vs "Added to Cart").
- [ ] **Entry filters** prevent the wrong people entering (e.g. exclude recent purchasers from cart flow).
- [ ] **Timing/delays** match intent (see lifecycle framework).
- [ ] **Conditional splits** personalize (purchased vs not, first-time vs returning, has discount vs not).
- [ ] **Message sequence** has a clear job per message (reminder -> reassurance -> incentive), not three identical emails.
- [ ] **Smart sending / quiet hours** respected to avoid over-messaging.
- [ ] **Goal/conversion metric** defined (e.g. placed order) so the flow can be measured and the series stops on conversion.
- [ ] **Offer logic** is deliberate (no discount, or escalating, or last-message-only).
- [ ] **SMS vs email** channel choice per step (if SMS consented).
- [ ] **Exit conditions** (purchased, unsubscribed) so people leave the flow appropriately.

## 2. Flow-specific checks

### Welcome
- [ ] Delivers the sign-up promise immediately.
- [ ] Brand story + bestsellers + reason to buy now.
- [ ] Discount (if used) handled so it can't be stacked/abused.

### Abandoned checkout / cart
- [ ] Separate, prioritized handling for Started Checkout (higher intent).
- [ ] Dynamic cart/product content with images.
- [ ] Reassurance (shipping, returns, security) before any discount.
- [ ] Suppresses customers who completed the purchase.

### Browse abandonment
- [ ] Only fires for identified, consented contacts.
- [ ] Soft tone; shows viewed product + alternatives.
- [ ] Frequency capped so browsers aren't spammed.

### Post-purchase
- [ ] Onboarding/usage content relevant to the product.
- [ ] Review/UGC request timed to product experience.
- [ ] Cross-sell based on what they bought.
- [ ] Different path for first-time vs repeat buyers.

### Winback / sunset
- [ ] Lapse window set to the product's purchase cycle.
- [ ] Escalating value; final "still want to hear from us?" before sunset.
- [ ] Non-responders moved to suppression (protects deliverability).

### Replenishment
- [ ] Only for consumables; timing based on expected run-out.
- [ ] One-click reorder path.

### VIP
- [ ] Clear threshold definition; perks that feel exclusive.
- [ ] Ongoing recognition, not a one-off.

## 3. Segmentation strategy

Define and maintain these segments:

- [ ] **Engaged** (opened/clicked recently) — your healthy sending core.
- [ ] **Purchasers** vs **never-purchased**.
- [ ] **VIPs / high LTV**.
- [ ] **Lapsing / lapsed** (by recency vs purchase cycle).
- [ ] **Category / product affinity** (for relevant cross-sell).
- [ ] **Suppression**: unengaged-for-X-days, hard bounces, unsubscribes, complainers.
- [ ] **Consent-based** segments respecting region and channel (email vs SMS).

Rule: send campaigns primarily to engaged segments; expand reach carefully. Aggressively sunset chronically unengaged contacts.

## 4. Deliverability basics

- [ ] **Authentication**: SPF, DKIM, and a dedicated sending domain (DMARC recommended).
- [ ] **Warmup**: ramp volume on a new domain/account; don't blast a cold list.
- [ ] **List hygiene**: remove hard bounces; sunset unengaged; never buy/scrape lists.
- [ ] **Consent**: only consented contacts; clear opt-in; honor opt-out promptly.
- [ ] **Engagement-based sending**: prioritize engaged segments to keep reputation high.
- [ ] **Monitor**: spam complaint rate, bounce rate, open/click trends, inbox placement.
- [ ] **Frequency**: cap sends to avoid fatigue and complaints.
- [ ] **Compliance**: physical address + unsubscribe in every email; follow GDPR/CAN-SPAM and local rules.
