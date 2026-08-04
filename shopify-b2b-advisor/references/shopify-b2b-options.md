# Shopify B2B Options and Capabilities

How to map B2B requirements to what Shopify can actually do. Verify current capabilities and plan boundaries against Shopify's docs, since the platform evolves.

## 1. The key platform fact

Shopify's **native B2B** functionality (company accounts, B2B price lists, payment terms, B2B checkout) is part of **Shopify Plus**. On non-Plus plans you do **not** get native company accounts and location-based price lists; you rely on apps or workarounds.

State this clearly in any recommendation. The plan decision drives the whole architecture.

## 2. Native Shopify B2B (Plus) — what it provides

- **Company accounts:** companies with multiple **locations**, and multiple **buyers** with roles/permissions.
- **Catalogs + price lists:** assign catalogs and price lists per company/location (custom pricing, % adjustments, fixed prices, volume rules depending on current features).
- **Payment terms:** net terms (e.g. Net 30), deposits, and "pay later/by invoice"-style flows.
- **B2B checkout:** buyer-aware checkout with terms and the right pricing.
- **Customer accounts (new):** company-aware login and self-serve portal.
- **Same admin & APIs:** B2B objects accessible via Admin API for integration.
- **B2B + D2C on one store:** run wholesale and retail together, with buyer-aware experiences.

This covers a large share of standard B2B needs natively on Plus, reducing app/custom dependence.

## 3. Non-Plus options (and their tradeoffs)

When Plus isn't available/justified:

- **Wholesale apps:** add gated catalogs, customer-group pricing, quick order, net terms emulation. Tradeoffs: monthly cost, theme coupling, limits, and the app becomes critical infrastructure.
- **Tag-based gating + theme logic:** show/hide pricing and content by customer tag. Cheap but fragile and limited; not true company accounts.
- **Separate / expansion store:** a dedicated B2B store. Cleaner separation but duplicated catalog/ops and another store to maintain.
- **Draft orders + manual quoting:** reps create draft orders/invoices. Works for low volume / high-touch, but doesn't scale to self-serve.

Make the cost/limitation/maintenance tradeoffs explicit; don't present a workaround as equivalent to native B2B.

## 4. Mapping requirements to native / app / custom

| Requirement | Typical solution |
| --- | --- |
| Company accounts, multiple buyers | Native (Plus B2B) |
| Per-company / per-location price lists | Native (Plus B2B); app on non-Plus |
| Gated catalog (login to see prices) | Native B2B (Plus) or app/theme gating |
| Payment terms (Net 30/60) | Native (Plus) or app/manual invoicing |
| Quote workflow | App or custom (often draft orders + flow); some via apps |
| Order approval chains (buyer-side) | App or custom; partial via roles |
| Sales-rep-assisted ordering | Draft orders / apps / custom portal |
| Bulk / quick order, CSV upload | App or custom storefront component |
| Volume/tier pricing | Native price-list rules (varies) / app |
| ERP integration | Connector/iPaaS or custom (Admin API) |
| Tax exemption / VAT IDs | Native tax settings + B2B config / app |

Decision order: **native first, then app, then custom.** Each step up adds cost and maintenance.

## 5. ERP integration patterns

- **Define the source of truth per data type** (products, pricing, inventory, customers, orders). The ERP is usually the source for pricing/inventory; Shopify for storefront/checkout.
- **Integration methods:**
  - **Native/marketplace connectors** for common ERPs (fastest, least flexible).
  - **iPaaS / middleware** (e.g. integration platforms) for mapping and orchestration (good balance).
  - **Custom** via Shopify Admin API + webhooks (most flexible, highest build/maintenance).
- **Sync design:** direction, frequency (real-time webhooks vs batch), idempotency, conflict resolution, and failure handling/alerting. This is where B2B projects most often break — design it deliberately and stage it.

## 6. Plus vs non-Plus decision checklist

Lean **Plus / native B2B** when:
- [ ] You need true company accounts with multiple buyers/locations.
- [ ] You need per-company/location price lists and payment terms at scale.
- [ ] B2B is a core, growing channel justifying the cost.
- [ ] You want to avoid stacking fragile apps for core functionality.

Consider **non-Plus + apps/workarounds** when:
- [ ] B2B is small, experimental, or high-touch/low-volume.
- [ ] Budget can't support Plus yet.
- [ ] Requirements are simple (basic gated pricing, manual quoting).

Always state the migration path (e.g. start lean, move to Plus B2B as volume grows) so the first build doesn't become a dead end.
