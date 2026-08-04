# Full audit output — Shopify CRO Auditor Skill

Unedited transcript of a Claude Code session running the `shopify-cro-auditor` Skill against a live store.

- **Store audited:** `https://www.cocorico.store/`
- **Prompt:** `Can you make a ecommerce audit about the shop "https://www.cocorico.store/" I would like to optimize the CRO`

---

```
❯ Can you make a ecommerce audit about the shop "https://www.cocorico.store/" I 
  would like to optimize the CRO                                                

● I'll run the dedicated Shopify CRO audit skill for this. Let me start by
  invoking it.

● Skill(shopify-cro-auditor)
  ⎿  Successfully loaded skill

● Let me read the reference files and then examine the actual store.

  Read 3 files (ctrl+o to expand)

● Now let me examine the actual store. I'll load the browser tools and navigate
  through the buying journey.

  Called claude-in-chrome 4 times (ctrl+o to expand)

● The hero area rendered blank — let me scroll to check if the hero image is
  slow-loading, then continue through the page.

  Called claude-in-chrome (ctrl+o to expand)

● Hero loaded after a delay (lazy-load — a perceived-speed issue). Let me look
  at the reviews/social proof section and footer.

  Called claude-in-chrome (ctrl+o to expand)

● Images render as empty gray placeholders here — a lazy-load/perceived-speed
  issue. Let me get to the reviews section.

  Called claude-in-chrome (ctrl+o to expand)

● Let me see the reviews section ("Nos clients en parlent") which I scrolled
  past.

  Called claude-in-chrome (ctrl+o to expand)

● Strong social proof — Trustpilot "Excellent" 4.5/5 on 26,619 reviews, verified
  reviews with names/dates. Now let me examine a collection page and a product
  page.

  Called claude-in-chrome 2 times (ctrl+o to expand)

● The /collections/homme handle 404s. Let me read the actual navigation links
  from the homepage.

  Called claude-in-chrome 2 times (ctrl+o to expand)

● Now let me visit the men's collection page and check its layout, filters, and
  sorting.

  Called claude-in-chrome 2 times (ctrl+o to expand)

● Sub-category images and hero render as empty gray boxes again (heavy
  lazy-loading). Let me scroll to the product grid to check cards, filters, and
  sort.

  Called claude-in-chrome (ctrl+o to expand)

● This collection page is a curated landing page (sub-carousels like "T-shirts
  Coton", "T-shirts en Lin") with no visible filter/sort controls. Let me get a
  product link and examine a PDP — the most important CRO page.
  Called claude-in-chrome (ctrl+o to expand)

● Let me examine a best-seller PDP.

  Called claude-in-chrome 3 times (ctrl+o to expand)

● Strong PDP structure. But the main product image is still blank gray — let me
  confirm whether it loads (perceived-speed concern) and then check the cart.

  Called claude-in-chrome (ctrl+o to expand)

● Image loads after a delay — confirming a consistent perceived-speed / LCP
  issue site-wide. Now the cart.

  Called claude-in-chrome 2 times (ctrl+o to expand)

● The cart is solid: free-shipping progress bar ("Plus que 35,20 € pour la
  livraison gratuite"), qty steppers, payment icons, shipping estimator. Notably
  there's no express checkout button (Shop Pay/PayPal/Apple Pay one-click) —
  only the generic "COMMANDER". Let me do a quick mobile check since mobile is
  the priority lens.

  Called claude-in-chrome 3 times (ctrl+o to expand)

● The screenshot capture renders at a fixed desktop resolution, so window-resize
  won't show me a true mobile render — I'll avoid that rabbit hole and reason
  about mobile from the responsive structure, flagging the sticky-ATC point as
  "verify" rather than asserting it. The image reloaded blank-gray again,
  reconfirming the LCP issue.

  I have strong evidence across home, collection, PDP, and cart. Let me restore
  the window and write up the audit.

  Called claude-in-chrome (ctrl+o to expand)

● I've completed the walkthrough. Here's the full CRO audit.

  ---
  CRO Audit — Cocorico (cocorico.store)

  Store profile: Made-in-France apparel, affordable price points (t-shirts
  ~15–25€, packs 30–75€), high review volume, aggressive sitewide discounting.
  Considered-but-low-ticket purchase → volume + AOV game. Audit based on live
  walkthrough of home, collection, PDP (best-seller), and cart on 2026-07-28. No
  analytics/session data was provided, so funnel reads below are heuristic and
  flagged as assumptions.

  ---
  1. Conversion diagnosis

  ▎ Funnel read (assumed). The store already does the hard trust-building work 
  ▎ well (26,619 Trustpilot reviews, MIF story, generous returns). The leak is 
  ▎ most likely perceived speed on entry and PDP→ATC hesitation driven by 
  ▎ slow-loading imagery and a discount-saturated experience that trains 
  ▎ shoppers to distrust prices and wait for the "next" sale.
  ▎
  ▎ Biggest opportunity. Fix image loading (LCP). On every page I loaded, 
  ▎ hero/product/category images rendered as empty gray placeholders for 1–3 
  ▎ seconds before appearing — including the primary PDP image, which is the 
  ▎ single most persuasive element on the page. This silently taxes every 
  ▎ session, and it hits hardest on mobile/3G where most fashion traffic sits.
  ▎
  ▎ Runner-up. The perpetual "SOLDES — Prolongations" countdown + near-universal
  ▎ strikethrough pricing erodes price credibility and urgency (shoppers learn 
  ▎ the "deal" never ends), which delays purchase.
  ▎
  ▎ Data used / assumptions. Live UX walkthrough only. Missing: CVR by device, 
  ▎ funnel drop-off, session recordings, LCP/INP field data, returns rate. 
  ▎ Confirm the speed finding with a Core Web Vitals check (PageSpeed Insights /
  ▎ GA4) before sizing the win.

  ---
  2. Page-by-page audit

  Page: Home
  Clarity: Medium — logo tagline "Fabriqué en France" is the only value prop
    above the fold; hero is 100% a discount banner
  Motivation: Strong sale pull, weak brand pull (why MIF, quality) above fold
  Friction / anxiety: Slow hero/image load; brand story buried at very bottom
  Key issues: Hero sells price, not the reason-to-believe; MIF differentiation
  is
    below everything
  ────────────────────────────────────────
  Page: Collection
  Clarity: Low–Medium
  Motivation: Good curation (Coton / Lin / Oversize sub-carousels)
  Friction / anxiety: No filter or sort on the main collection landing; images
    load as gray blocks; horizontal-scroll category nav hides options
  Key issues: Shoppers who know what they want (size/color/price) can't narrow
    down; real filterable sub-collections are buried one click deeper
  ────────────────────────────────────────
  Page: Product (PDP)
  Clarity: High
  Motivation: High — price+strikethrough, swatches, "Trouver ma taille",
    cross-sell
  Friction / anxiety: Main image slow to render; rating "4.5/5" has no count and
   
    isn't clickable; shipping cost under 60€ not stated
  Key issues: Great structure, but trust/social-proof and shipping clarity
    underplayed at the decision point
  ────────────────────────────────────────
  Page: Cart
  Clarity: High
  Motivation: Good — free-shipping progress bar ("Plus que 35,20 € pour la
    livraison gratuite")
  Friction / anxiety: No express checkout button; only generic "COMMANDER";
    "frais de port calculés au checkout" = late-stage surprise
  Key issues: Missing one-tap checkout (Shop Pay/PayPal/Apple Pay) is a
    measurable mobile leak
  ────────────────────────────────────────
  Page: Pre-checkout
  Clarity: n/a (standard Shopify)
  Motivation: —
  Friction / anxiety: Standard Shopify checkout; payment icons shown (Apple Pay,

    CB, GPay, Maestro, MC, PayPal, Visa)
  Key issues: Ensure accelerated wallets are actually enabled before checkout,
    not just as trust icons
  ────────────────────────────────────────
  Page: Mobile (cross-cutting)
  Clarity: Medium
  Motivation: —
  Friction / anxiety: Same slow images (worse on cellular); sticky ATC not 
    verified
  Key issues: Verify sticky add-to-cart on PDP and express-checkout buttons on
    mobile cart

  ---
  3. Friction points & unanswered objections

  #: 1
  Page: All
  Friction / unanswered objection: Images load as empty gray placeholders, then
    pop in
  Evidence: Observed on home hero, collection tiles, PDP main image, promo
  blocks
  Why it costs conversions: Poor LCP → higher bounce, lower perceived quality,
    worst on mobile
  ────────────────────────────────────────
  #: 2
  Page: All
  Friction / unanswered objection: "SOLDES — Prolongations" countdown never
  truly
    ends; nearly every product has a strikethrough "prix normal"
  Evidence: Persistent top-bar countdown; sitewide -60%
  Why it costs conversions: Price/urgency loses credibility; trains shoppers to
    wait; potential consumer-law risk (reference pricing)
  ────────────────────────────────────────
  #: 3
  Page: PDP
  Friction / unanswered objection: "Will it fit?" partly answered, but rating
    shows "4.5/5" with no review count, not  clickable, and the on-page reviews
    block is a generic Trustpilot carousel, not product-specific reviews with
    photos
  Evidence: PDP header + "Nos clients en parlent" carousel
  Why it costs conversions: Product-level social proof is the top ATC driver for

    apparel; it's underused here
  ────────────────────────────────────────
  #: 4
  Page: PDP / Cart
  Friction / unanswered objection: "When & how much is shipping?" — free over
    60€, but the cost below 60€ is never shown until checkout
  Evidence: PDP reassurance line only says "offerte dès 60€"; cart says
  "calculés
    au checkout"
  Why it costs conversions: Surprise shipping cost is a leading abandonment
  cause
  ────────────────────────────────────────
  #: 5
  Page: Cart
  Friction / unanswered objection: No express/accelerated checkout button
  Evidence: Cart shows only "COMMANDER"; wallets appear only as static icons
  Why it costs conversions: One-tap checkout materially lifts mobile CVR
  ────────────────────────────────────────
  #: 6
  Page: Collection
  Friction / unanswered objection: No filter/sort on main collection pages
  Evidence: /collections/…homme… is a curated carousel page, no facets
  Why it costs conversions: Slows product discovery for high-intent shoppers
  ────────────────────────────────────────
  #: 7
  Page: Home
  Friction / unanswered objection: Value proposition weak above the fold
  Evidence: Hero = sale banner; brand rationale sits at page bottom
  Why it costs conversions: New visitors don't get "why Cocorico" before
    scrolling

  ---
  4. Quick wins (ship now)

  Quick win: Prioritize LCP image: preload the PDP main image + hero, set
    explicit width/height, serve responsive srcset, drop lazy-load on
    above-the-fold images
  Page: All
  Effort: Med
  Expected effect: Faster perceived load, less bounce
  Why high-confidence: Slow LCP is a near-universal CVR drag; images are the LCP

    element here
  ────────────────────────────────────────
  Quick win: Add express checkout buttons (Shop Pay / PayPal / Apple Pay) to
  cart
    and PDP
  Page: Cart/PDP
  Effort: Low
  Expected effect: Fewer steps, higher mobile CVR
  Why high-confidence: Native Shopify feature; well-documented lift
  ────────────────────────────────────────
  Quick win: Make the PDP star rating show the review count and link/scroll to
    reviews
  Page: PDP
  Effort: Low
  Expected effect: Stronger trust at decision point
  Why high-confidence: Count + accessibility of reviews is a proven ATC driver
  ────────────────────────────────────────
  Quick win: State shipping cost explicitly on PDP ("Livraison 4,90 € · offerte
    dès 60 €" — use real figure)
  Page: PDP
  Effort: Low
  Expected effect: Removes a checkout surprise
  Why high-confidence: Transparency reduces abandonment
  ────────────────────────────────────────
  Quick win: Surface filter/sort (size, color, price) on collection landing
    pages, or route the category to the real filterable collection
  Page: Collection
  Effort: Med
  Expected effect: Faster find-to-cart
  Why high-confidence: Standard merchandising expectation
  ────────────────────────────────────────
  Quick win: Add a one-line value prop to the hero ("Le vrai Made in France, au
    prix du made-in-ailleurs") alongside the sale
  Page: Home
  Effort: Low
  Expected effect: Clarity for new visitors
  Why high-confidence: Differentiation is the brand's actual moat

  ▎ ⚠️ Handle with care, not a "quick win": the perpetual countdown + universal 
  ▎ strikethrough. Don't remove urgency blindly, but move to honest scarcity 
  ▎ (real end dates, genuine reference prices). Fake/rolling urgency is a dark 
  ▎ pattern and a legal exposure in France (DGCCRF / Omnibus reference-price 
  ▎ rules) — I won't recommend keeping it as-is.

  ---
  5. Test backlog

  ID: T1
  Hypothesis: Because images are the LCP element and load slowly, we believe
    preloading/optimizing them will reduce bounce and lift CVR, esp. on mobile.
  Page: All
  Primary metric: Mobile CVR / bounce
  Impact: 5
  Effort: 3
  Conf.: 4
  ────────────────────────────────────────
  ID: T2
  Hypothesis: Because one-tap wallets reduce steps, we believe adding express
    checkout to cart+PDP will lift checkout-start→purchase.
  Page: Cart/PDP
  Primary metric: Cart→purchase rate
  Impact: 4
  Effort: 2
  Conf.: 4
  ────────────────────────────────────────
  ID: T3
  Hypothesis: Because apparel buyers rely on peer proof, we believe adding
    product-specific reviews (count, photos, distribution) near the buy box will

    lift ATC.
  Page: PDP
  Primary metric: PDP→ATC rate
  Impact: 4
  Effort: 3
  Conf.: 4
  ────────────────────────────────────────
  ID: T4
  Hypothesis: Because surprise shipping abandons carts, we believe showing
    shipping cost + free-ship threshold on PDP will lift ATC→checkout.
  Page: PDP
  Primary metric: ATC→checkout
  Impact: 3
  Effort: 2
  Conf.: 3
  ────────────────────────────────────────
  ID: T5
  Hypothesis: Because rolling urgency lacks credibility, we believe replacing
  the
    perpetual countdown with an honest, dated offer will lift CVR without
  harming
     trust.
  Page: Site
  Primary metric: Sitewide CVR
  Impact: 3
  Effort: 2
  Conf.: 3
  ────────────────────────────────────────
  ID: T6
  Hypothesis: Because high-intent shoppers want to narrow choices, we believe
    adding size/color/price filters to collections will lift collection→PDP.
  Page: Collection
  Primary metric: Collection→PDP CTR
  Impact: 3
  Effort: 3
  Conf.: 3
  ────────────────────────────────────────
  ID: T7
  Hypothesis: Because a stronger above-fold value prop aids new visitors, we
    believe adding a brand-benefit hero line will lift home→PDP.
  Page: Home
  Primary metric: Home engagement / CVR
  Impact: 2
  Effort: 1
  Conf.: 3

  ---
  6. Impact / effort prioritization

  ┌─────────┬───────────────────────────────────┬──────────────────────────┐
  │         │            Low effort             │       High effort        │
  ├─────────┼───────────────────────────────────┼──────────────────────────┤
  │ High    │ Express checkout (T2), PDP review │ Image/LCP fix (T1),      │
  │ impact  │  count, shipping transparency     │ product reviews revamp   │
  │         │ (T4)                              │ (T3)                     │
  ├─────────┼───────────────────────────────────┼──────────────────────────┤
  │ Low     │ Hero value prop (T7), honest      │ Collection filters (T6)  │
  │ impact  │ urgency (T5)                      │                          │
  └─────────┴───────────────────────────────────┴──────────────────────────┘

  Ranked shortlist (next 5):

  ┌──────┬───────────────────────────────────┬────────────┬────────┬────────┐
  │ Rank │               Item                │    Type    │ Impact │ Effort │
  ├──────┼───────────────────────────────────┼────────────┼────────┼────────┤
  │ 1    │ Image/LCP optimization            │ Win+Test   │ 5      │ 3      │
  │      │                                   │ (T1)       │        │        │
  ├──────┼───────────────────────────────────┼────────────┼────────┼────────┤
  │ 2    │ Express checkout on cart + PDP    │ Win (T2)   │ 4      │ 2      │
  ├──────┼───────────────────────────────────┼────────────┼────────┼────────┤
  │ 3    │ Product-specific reviews +        │ Win+Test   │ 4      │ 3      │
  │      │ visible count on PDP              │ (T3)       │        │        │
  ├──────┼───────────────────────────────────┼────────────┼────────┼────────┤
  │ 4    │ Shipping cost transparency on PDP │ Win (T4)   │ 3      │ 2      │
  ├──────┼───────────────────────────────────┼────────────┼────────┼────────┤
  │ 5    │ Collection filter/sort            │ Test (T6)  │ 3      │ 3      │
  └──────┴───────────────────────────────────┴────────────┴────────┴────────┘

  ---
  Two caveats on method

  - Speed is my #1 finding but I observed it, not measured it. Before you
  invest, run PageSpeed Insights on the home + a PDP and check GA4 for mobile
  bounce/CVR — that turns "slow images" into a sized opportunity.
  - I couldn't verify mobile sticky add-to-cart (the screenshot tool captures at
  desktop resolution). Check on a real phone; if the ATC scrolls out of view on
  the long PDP, add a sticky bar — that's a likely additional quick win.

  ---
  This audit is a framework-driven friction list and test backlog. What it can't
  do: watch your real session recordings, run the A/B tests, or tell you which 
  "quick win" will hold up against your actual traffic. Pikka pairs this with 
  hands-on session review, test implementation, and statistically sound 
  read-outs. Free 30-min review of this output: contact@pikka.fr.

  Want me to go deeper on any single area — e.g., a detailed PDP redesign spec,
  the exact Liquid/theme changes for the image-speed fix, or a mobile-specific
  pass?

✻ Crunched for 4m 31s

※ recap: I audited cocorico.store for conversion optimization and delivered the full report: diagnosis, page-by-page findings, quick wins, and a prioritized test backlog. Next, I can go deeper on any area you pick, like a PDP redesign spec or the image-speed fix. (disable recaps in /config)```
