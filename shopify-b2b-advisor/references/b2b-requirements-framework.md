# B2B Requirements Framework

A discovery framework to capture B2B needs before recommending architecture. For each area, record the requirement, whether it's a must-have or nice-to-have, and any constraint.

## 1. Accounts and buyers

- **Account model:** Do buyers belong to **companies** (multiple buyers per company, shared catalog/pricing) or are they individual **customer accounts**?
- **Buyer roles & permissions:** Who can browse, order, approve, see pricing, manage users?
- **Multiple locations:** Do companies have multiple ship-to locations with different catalogs/pricing/tax?
- **Self-service vs assisted:** Do buyers self-serve, or do sales reps place orders on their behalf?
- **Onboarding:** How are new companies/buyers vetted and approved?

## 2. Pricing

- **Pricing model:** Per-company price lists, volume/tier pricing, % off retail, fixed negotiated prices, or contract pricing?
- **Currency & markets:** Multiple currencies/regions?
- **MOQs / increments:** Minimum order quantities, case packs, order increments?
- **Visibility:** Are prices hidden until login? Different prices per company?
- **Promotions:** B2B-specific discounts, not the same as D2C.

## 3. Catalog

- **Public vs gated:** Is the catalog public, fully gated behind login, or mixed (D2C public + B2B gated)?
- **Per-company catalog:** Do different companies see different products?
- **Product data:** B2B-specific attributes (spec sheets, case packs, lead times, MOQs).
- **Search & reorder:** Fast reordering, order history, quick order by SKU/CSV upload.

## 4. Payments and terms

- **Payment terms:** Net 15/30/60, deposits, credit limits?
- **Payment methods:** Cards, bank transfer, "pay by invoice", purchase orders?
- **Tax:** B2B tax exemption, VAT handling, tax IDs per company?
- **Credit management:** Who sets and enforces credit limits?

## 5. Workflow

- **Quotes:** Do buyers request quotes? Who approves and converts them to orders?
- **Order approval:** Internal approval chains on the buyer side (e.g. buyer creates, manager approves)?
- **Sales reps:** Rep-assisted ordering, rep visibility into their accounts, commissions?
- **Reordering:** Repeat-order convenience, subscriptions/standing orders?
- **Returns/RMA:** B2B return process.

## 6. ERP / systems integration

- **Source of truth:** Which system owns products, pricing, inventory, customers, orders? (Often the ERP.)
- **Systems in play:** ERP, accounting, CRM, PIM, WMS, shipping.
- **Sync needs:** What syncs, in which direction, how often (real-time vs batch)?
- **Order flow:** Where do B2B orders get fulfilled and invoiced?

## 7. B2B UX

- **Login-first experience:** Gated storefront, company switcher, location switcher.
- **Account portal:** Order history, reorder, invoices, users, addresses, credit/terms visibility.
- **Bulk ordering:** Quick order forms, CSV upload, saved lists.
- **Clarity:** Showing the right price, terms, and availability per buyer.

## 8. Prioritization

Tag each requirement:

- **Must-have (MVP):** Without it, B2B can't launch.
- **Should-have:** Important, can follow shortly after launch.
- **Nice-to-have:** Optimization for later phases.

Resist scope creep: a focused MVP (accounts + pricing + ordering + core integration) that ships beats a perfect spec that never launches.

## Discovery output table

| Area | Requirement | Priority (Must/Should/Nice) | Constraint / note |
| --- | --- | --- | --- |
| Accounts | [ ] | [ ] | [ ] |
| Pricing | [ ] | [ ] | [ ] |
| Catalog | [ ] | [ ] | [ ] |
| Payments/terms | [ ] | [ ] | [ ] |
| Workflow | [ ] | [ ] | [ ] |
| Integration | [ ] | [ ] | [ ] |
| UX | [ ] | [ ] | [ ] |
