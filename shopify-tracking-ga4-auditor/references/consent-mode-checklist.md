# Consent Mode & Privacy Compliance Checklist

For stores with traffic in the EEA/UK (and increasingly elsewhere), consent is both a legal requirement and a data-quality factor. This is operational guidance, not legal advice — confirm specifics with a qualified advisor for the store's jurisdiction.

## 1. Do you need consent management?

- [ ] Store serves the EEA / UK / Switzerland (GDPR / UK GDPR / ePrivacy) -> yes, consent required before non-essential cookies/tracking.
- [ ] Store uses Google Ads / GA4 with EEA users -> **Consent Mode v2** is effectively required for Google to use the data and to model conversions.
- [ ] Other regions with privacy laws (e.g. certain US states) -> check applicable rules.

## 2. Consent Management Platform (CMP)

- [ ] A CMP / cookie banner is present and blocks non-essential tags **before** consent.
- [ ] The CMP is integrated with Shopify's **Customer Privacy API** (so Shopify's pixels respect consent).
- [ ] Banner offers genuine choice (accept / reject / manage), not consent-or-nothing where the law requires a real reject option.
- [ ] Consent choice persists and is re-collected appropriately.
- [ ] A Google-certified CMP is used where relevant (for Consent Mode v2 + ad features).

## 3. Consent Mode v2 signals

Verify the four signals are implemented and behave correctly:

- [ ] `ad_storage`
- [ ] `analytics_storage`
- [ ] `ad_user_data`
- [ ] `ad_personalization`

Checks:
- [ ] **Default state is denied** before the user interacts (for EEA traffic).
- [ ] Signals **update to granted** only after explicit consent.
- [ ] Tags (GA4, Ads) load in a consent-aware way (Advanced consent mode sends cookieless pings when denied; Basic mode withholds tags until consent). Know which mode is configured.
- [ ] Consent state is passed correctly whether tags load via the Google app, GTM, or custom pixels.

## 4. Shopify-specific consent integration

- [ ] Shopify **Customer Privacy / Consent API** is wired to the CMP so first-party pixels and the Google & YouTube app honor consent.
- [ ] Custom pixels read consent state and gate accordingly.
- [ ] Checkout/thank-you tracking respects consent.
- [ ] Region detection is correct (don't apply EEA defaults globally if not intended, and do apply them for EEA visitors).

## 5. Data minimization & PII

- [ ] No PII (emails, names, phone, full address) sent to GA4 or ad platforms in parameters or URLs.
- [ ] Hashing used where platforms support it (e.g. enhanced conversions) and consent allows.
- [ ] IP anonymization / data retention settings reviewed.

## 6. Consent-related risks to flag

| Risk | Effect |
| --- | --- |
| No CMP / tags fire before consent | Legal exposure; possible fines |
| Consent Mode not implemented | Google can't model EEA conversions; data loss; Ads features degraded |
| Default granted in EEA | Non-compliant; tracking without consent |
| CMP not linked to Shopify privacy API | Shopify pixels ignore consent |
| Consent gaps blamed as "low conversions" | Misreads data loss as performance drop |

## 7. Validation

- [ ] Test as an EEA visitor: confirm tags are gated pre-consent and fire post-consent (Tag Assistant / DevTools network).
- [ ] Confirm Consent Mode signals in GA4 DebugView / Tag Assistant.
- [ ] Confirm reject path actually suppresses non-essential tags.
- [ ] Document the consent architecture so it can be maintained.
