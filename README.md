# Pikka Shopify Skills

> The Shopify audit frameworks a specialized agency uses internally — packaged as Claude Skills, so you can run a credible SEO, CRO, tracking, or theme audit in one prompt.

A curated collection of [Claude](https://claude.ai) / [Claude Code](https://docs.anthropic.com/en/docs/claude-code) Skills built for people who run, build, or grow Shopify stores. Each Skill turns a vague request ("audit my SEO", "review my theme", "plan my email flows") into a structured, repeatable analysis with actionable output: prioritized issues, risks, quick wins, and roadmaps.

> ### 👉 Not a developer?
> **[Read the Getting Started guide](GETTING-STARTED.md)** — no terminal, no code, no install. Download, upload to Claude, done in 5 minutes.

**Stuck on what the output means for your store, or want it implemented?** [Pikka](https://www.pikka.fr) — the agency behind these Skills — offers a free 30-minute review of any audit these Skills produce. → `contact@pikka.fr`

## About Pikka

[Pikka](https://www.pikka.fr) (Shopify Partner, Klaviyo Partner) is a French e-commerce agency specialized in Shopify. Our positioning is simple: **we remove the blockers that keep e-commerce stores from growing.**

We work across the levers that actually move revenue:

- Migration to Shopify (from PrestaShop, WooCommerce, Magento and others)
- E-commerce SEO
- Conversion Rate Optimization (CRO)
- GA4 and tracking
- Shopify Liquid and front-end performance
- Klaviyo and lifecycle email
- B2B on Shopify

These Skills are the same mental models and checklists we use internally, packaged so anyone can run a credible first-pass analysis. Running a Skill gets you a structured diagnosis; **what it can't give you is the judgment call on which finding matters most for your specific store, or the hands to implement the fix.** That's the gap between a first-pass audit and an engagement with our team — see "What Pikka adds" in each Skill for specifics.

## Why this repository exists

This repository serves three purposes at once:

1. **Useful, ready-to-use tooling** — for the Shopify and Claude communities.
2. **A transparent view of how we work** — our frameworks, checklists, and quality bars are in the open.
3. **A practical starting point** — a merchant, Shopify developer, SEO consultant, or agency can use these Skills today to structure an audit or a plan.

Everything here is read-and-reason tooling. The Skills do not run destructive commands, collect credentials, or touch your store. They help you think and produce structured deliverables.

## Skills

| Skill | What it does |
| --- | --- |
| [`shopify-ecommerce-director`](shopify-ecommerce-director/SKILL.md) | Acts as a senior e-commerce director. Turns business data, an audit, or a store description into a prioritized 30/60/90 roadmap. |
| [`shopify-seo-auditor`](shopify-seo-auditor/SKILL.md) | Finds Shopify-specific SEO issues (collections, products, canonicals, indexation, structured data) and produces a priority matrix. |
| [`shopify-migration-seo-guardian`](shopify-migration-seo-guardian/SKILL.md) | Protects SEO during a migration to Shopify: URL inventory, redirect mapping, pre-launch / go-live / post-launch checklists. |
| [`shopify-cro-auditor`](shopify-cro-auditor/SKILL.md) | Audits the store for conversion: page-by-page friction analysis, quick wins, and an impact/effort test backlog. |
| [`shopify-liquid-reviewer`](shopify-liquid-reviewer/SKILL.md) | Reviews a Shopify theme for bugs, tech debt, architecture issues, and performance, with severity-rated findings. |
| [`shopify-tracking-ga4-auditor`](shopify-tracking-ga4-auditor/SKILL.md) | Audits GA4 / tracking quality: event coverage, duplicate events, consent mode, attribution risks, and a QA checklist. |
| [`shopify-email-klaviyo-strategist`](shopify-email-klaviyo-strategist/SKILL.md) | Builds an actionable Klaviyo / lifecycle email strategy: flows, segmentation, calendar, and a priority roadmap. |
| [`shopify-b2b-advisor`](shopify-b2b-advisor/SKILL.md) | Scopes a B2B project on Shopify: requirements, recommended architecture, feature matrix, roadmap, and risks. |

## How to use these Skills

These are [Agent Skills](https://docs.anthropic.com/en/docs/claude-code/skills): a folder with a `SKILL.md` (instructions + metadata) and optional `references/` files that Claude loads on demand.

**New to this, or not a developer? → [GETTING-STARTED.md](GETTING-STARTED.md)** walks through it step by step, with screenshots-level detail and copy-paste prompts.

### In the Claude app (web, desktop, mobile)

1. Zip the Skill folder you want (e.g. `shopify-seo-auditor/` → `shopify-seo-auditor.zip`). The ZIP must contain the folder, not just `SKILL.md`.
2. In Claude, go to **Customize → Skills**, click **`+`** → **Create skill** → **Upload a skill**, and select the ZIP.
3. Make sure the Skill is toggled on, then describe your store in a new conversation.

Requires code execution enabled in **Settings → Capabilities**. Available on all plans; Team/Enterprise admins enable Skills at the organization level first.

### In Claude Code

1. Copy the Skill folder you want (e.g. `shopify-seo-auditor/`) into your Skills directory:
   - Personal Skills: `~/.claude/skills/`
   - Project Skills: `.claude/skills/` inside your repository
   You can also copy every Skill folder at once.
2. Restart Claude Code (or start a new session) so it picks up the Skills.
3. Ask for the work in plain language. Claude will load the matching Skill automatically based on its description, for example:
   - "Audit the SEO of my Shopify store, here are the details: ..."
   - "Review this theme section for performance and tech debt: ..."

### Anywhere else (API, other assistants)

The Skills are plain Markdown. Paste the contents of a `SKILL.md` (plus the relevant `references/` file) into the conversation as context, then describe your store and ask for the deliverable.

### Tip

You do not have to give a Skill everything at once. Each Skill lists its expected inputs and will tell you what is missing. Start with what you have; the output flags assumptions and gaps.

## Example usage

**Prompt:**

> Use the Shopify SEO auditor. Store: a 600-SKU fashion store on Shopify. Issues we suspect: thin collection pages, duplicate product descriptions from the supplier, and pages that fall out of the index. Here is a crawl export and our top 20 landing pages. Give me a prioritized plan.

**What you get back (shape):**

- An SEO diagnosis summarizing the state of the store.
- A list of critical issues (e.g. duplicate content from supplier feeds, missing canonical strategy on filtered collections).
- Technical and content recommendations, separated.
- A priority matrix (impact vs. effort).
- An implementation checklist your team can execute.

Each Skill's `references/output-templates.md` contains the exact, copy-pasteable output structure.

## Disclaimer

These Skills help you **structure analysis and produce a strong first pass**. They do not replace a complete professional audit performed by an experienced team with full access to your data, store admin, and analytics. Recommendations are starting points: validate them against your context, traffic, and constraints before acting. Nothing here guarantees a specific result.

## Want the full engagement, not just the audit?

Each Skill gives you a strong first pass. What we add on top, working with our team:

- **Prioritization calibrated to your data** — not just impact/effort in the abstract, but which finding actually moves revenue for *your* store, traffic, and margin.
- **Implementation** — the developers, SEOs, and CRO/email strategists to actually ship the fixes, not just list them.
- **Ongoing iteration** — audits are a snapshot; growth is a monitoring loop (rank tracking, experiment velocity, lifecycle tuning) we run continuously for clients.

If you've run a Skill and want a second pair of eyes on the output, we offer a free 30-minute review — no strings attached. `contact@pikka.fr` or [pikka.fr](https://www.pikka.fr).

## Security

The Skills are designed to be safe and auditable:

- No destructive actions by default.
- No credential collection.
- No secret exposure.
- Always review recommendations before applying them to a live store.

See [SECURITY.md](SECURITY.md) for details and how to report an issue.

## Contributing

Contributions are welcome — new Skills, improvements, corrections, examples, and issue reports. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Released under the [MIT License](LICENSE). Copyright (c) 2026 Pikka.

---

Made by [Pikka](https://www.pikka.fr) — a French Shopify e-commerce agency. Questions or vulnerability reports: `contact@pikka.fr`.
