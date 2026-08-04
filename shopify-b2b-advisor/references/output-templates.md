# Output Templates — Shopify B2B Advisor

Copy-pasteable deliverable structure. Fill brackets; delete what doesn't apply.

---

## 1. Requirements analysis

> **Business model.** [Pure B2B / B2B + D2C / wholesale arm; scale: companies, buyers, geos.]
>
> **Commercial summary.** [Pricing model, catalog visibility, payment terms, key processes.]

| Area | Requirement | Priority | Constraint / note |
| --- | --- | --- | --- |
| Accounts | [ ] | Must/Should/Nice | [ ] |
| Pricing | [ ] | [ ] | [ ] |
| Catalog | [ ] | [ ] | [ ] |
| Payments/terms | [ ] | [ ] | [ ] |
| Workflow | [ ] | [ ] | [ ] |
| Integration | [ ] | [ ] | [ ] |
| UX | [ ] | [ ] | [ ] |

> **MVP scope.** [The must-haves required to launch.]

---

## 2. Recommended architecture

> **Platform tier.** [Plus (native B2B) vs non-Plus + apps/workaround — with the reasoning and tradeoffs.]
>
> **Account model.** [Company accounts vs customer accounts; buyers/roles/locations.]
>
> **Pricing & catalog.** [Price-list structure, gating, currencies.]
>
> **Payments & terms.** [Net terms, methods, tax handling.]
>
> **Integration.** [Source of truth per data type; sync method and direction.]

Architecture overview:

```mermaid
flowchart LR
  buyer[B2B Buyer] --> store[Shopify Storefront / B2B]
  store --> admin[Shopify Admin and Orders]
  erp[ERP / Source of Truth] -->|products, pricing, inventory| store
  admin -->|orders, customers| erp
```

---

## 3. Feature matrix

| Requirement | Native | App | Custom | Not feasible | Notes / dependency |
| --- | --- | --- | --- | --- | --- |
| Company accounts | [ ] | | | | Plus only |
| Per-company price lists | [ ] | [ ] | | | [ ] |
| Gated catalog | [ ] | [ ] | | | [ ] |
| Payment terms (Net 30) | [ ] | [ ] | | | [ ] |
| Quote workflow | | [ ] | [ ] | | [ ] |
| Order approval | | [ ] | [ ] | | [ ] |
| Sales-rep ordering | | [ ] | [ ] | | [ ] |
| Bulk / quick order | | [ ] | [ ] | | [ ] |
| ERP integration | | [ ] | [ ] | | [ ] |

---

## 4. Implementation roadmap

| Phase | Goal | Scope | Depends on |
| --- | --- | --- | --- |
| Phase 1 — Foundation | Plan/setup, accounts, catalog | [account model, plan decision, data model] | [ ] |
| Phase 2 — Core B2B | Pricing, gated catalog, ordering | [price lists, gating, checkout] | Phase 1 |
| Phase 3 — Workflow & integration | Terms, quotes/approval, ERP sync | [terms, integration, rep tools] | Phase 2 |
| Phase 4 — Optimization | UX, reorder, reporting, scale | [quick order, portal polish] | Phase 3 |

---

## 5. Risk assessment

| Risk | Type | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- | --- |
| Platform fit (needs Plus) | Platform | [ ] | [ ] | Confirm plan early; map workarounds |
| ERP sync conflicts/failures | Integration | [ ] | [ ] | Define source of truth; staged sync; alerting |
| Data migration errors | Data | [ ] | [ ] | Stage + validate; reversible; confirm before live |
| Process change resistance | Org | [ ] | [ ] | Train reps/buyers; phased rollout |
| Scope creep / cost overrun | Delivery | [ ] | [ ] | Lock MVP; phase the rest |
