# Go-Live Runbook

Launch-day steps, in order. Assign an owner to each. Do not skip the validation gates. Treat anything irreversible (DNS, taking down the old site) as requiring explicit confirmation and a rollback plan.

## T-1 day: final pre-flight

- [ ] Redirect map finalized, imported to Shopify, and validated on a sample.
- [ ] Final content/metadata spot-check on key templates.
- [ ] Sitemaps and `robots.txt` reviewed for production (will allow indexing once live).
- [ ] Analytics/tracking verified on the new site (events firing).
- [ ] Rollback plan written: how to revert DNS / restore the old site if something breaks.
- [ ] Freeze: no further structural changes until after launch is confirmed stable.

## Launch window (in order)

1. [ ] **Remove indexing block** on the new Shopify site (disable password / `noindex` on the storefront). Confirm the storefront is publicly reachable.
2. [ ] **Point DNS** to Shopify (or publish the new theme). *Confirmation gate — irreversible-ish; ensure rollback is ready.*
3. [ ] **Verify the home page and key templates** load with HTTPS and correct canonical host.
4. [ ] **Test redirects live**: run the priority old-URL list through and confirm single-hop 301 -> 200.
5. [ ] **Crawl the live site** quickly: check for 404s, broken internal links, redirect chains.
6. [ ] **Confirm canonicals** render correctly on product, collection, page, blog templates.
7. [ ] **Submit the new sitemap** in Search Console; request indexing for the top pages.
8. [ ] **Verify tracking** fires on a real session (purchase/begin_checkout/view_item).
9. [ ] **Check structured data** on a sample with the Rich Results Test.

## Validation gate (before declaring success)

- [ ] Priority URLs all redirect correctly (single hop, correct destination).
- [ ] No spike of 404s in the live crawl.
- [ ] Home, top collections, and top products render and convert (test transaction if possible).
- [ ] Tracking confirmed.

If any gate fails and can't be fixed quickly, execute the rollback plan rather than leaving a broken state live.

## Immediately after launch (T+0 to T+48h)

- [ ] Keep the old site reachable (if architecture allows) until redirects are confirmed, in case of a rollback.
- [ ] Monitor Search Console Coverage and Crawl Stats for errors.
- [ ] Monitor real-time analytics for traffic collapse or tracking gaps.
- [ ] Watch server/redirect logs for 404 spikes; patch missing redirects fast.
- [ ] Annotate the launch in analytics and Search Console.

## Do NOT

- Do not bulk-delete the old redirects later.
- Do not take down the old site or change DNS without confirmation and a rollback path.
- Do not redesign content/IA further during the stabilization window.
