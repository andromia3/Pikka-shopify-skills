# Prioritization and Sequencing Model

How to turn a list of issues into a ranked plan and a sequenced 30/60/90-day roadmap.

## 1. Scoring model (ICE-TS)

Score each issue/initiative on five factors, 1-5 (5 is best). This extends classic ICE with time-to-impact and strategic fit, which matter for sequencing.

| Factor | Question | 1 | 5 |
| --- | --- | --- | --- |
| Impact (I) | How much revenue/margin could this move? | Marginal | Step-change |
| Confidence (C) | How sure are we it will work? | Speculative | Proven / strong evidence |
| Ease (E) | How easy to ship? (inverse of effort) | Months, cross-team | Hours, one person |
| Time-to-impact (T) | How fast do we see the effect? | Quarters | Days |
| Strategic fit (S) | Does it support the stated goal and compound? | Off-strategy | Directly on-goal |

**Priority score = I x C x E** (the core ICE ranking), with **T** and **S** used as tie-breakers and for sequencing.

Keep the raw factor scores visible in the output so the reasoning is auditable.

## 2. Quick-win filter

An initiative is a **quick win** if: Ease >= 4 AND Time-to-impact >= 4 AND Impact >= 3. Quick wins are pulled out of the roadmap and started immediately — they fund momentum and trust.

## 3. Impact / effort quadrants

Map every initiative for a fast visual read:

| | Low effort | High effort |
| --- | --- | --- |
| **High impact** | Quick wins — do now | Big bets — plan and resource |
| **Low impact** | Fill-ins — batch or defer | Money pits — drop unless strategic |

## 4. Dependencies and sequencing rules

Priority score sets *desirability*; dependencies set *order*. Apply these rules before locking the roadmap:

- **Measurement before scaling.** Fix tracking/attribution before optimizing or scaling paid spend, or you optimize on noise.
- **Foundation before content.** Fix indexation, canonicals, and site structure before investing heavily in new SEO content.
- **Retention before acquisition (when margin is thin).** If repeat rate is weak, fixing lifecycle often beats buying more first-time buyers.
- **Conversion before traffic (often).** Sending more traffic to a leaky funnel wastes spend; lift CVR first when the funnel is clearly broken.
- **Stabilize before refactor.** Fix bugs and broken flows before large theme/architecture work.

## 5. Building the 30 / 60 / 90-day roadmap

Think in three horizons. Each phase should have a theme, not just a task list.

- **Days 0-30 — Stabilize and capture quick wins.**
  Fix what's broken or leaking (tracking, broken flows, obvious funnel drop-offs). Ship the quick wins. Establish the KPI baseline. Goal: stop the bleeding and build momentum.

- **Days 31-60 — Optimize the core.**
  Improve the highest-leverage lever found in the diagnostic (often conversion or lifecycle). Run the first structured tests. Begin foundational SEO/tech work. Goal: measurable lift on the primary metric.

- **Days 61-90 — Scale and compound.**
  Scale what's now measurable and working (paid, content, lifecycle expansion). Tackle larger structural projects. Goal: durable, compounding growth aligned to the business objective.

For each initiative in the roadmap, record: name, lever, expected effect (direction/range), effort, owner/skill, dependencies, and how you'll know it worked.

## 6. Expressing expected impact honestly

- Use **ranges and directions** ("likely +0.2 to +0.5 pts CVR"), never point guarantees.
- State the **mechanism** ("by removing the surprise shipping cost at cart").
- Flag **confidence** explicitly. Low-confidence, high-impact items become **tests**, not commitments.
