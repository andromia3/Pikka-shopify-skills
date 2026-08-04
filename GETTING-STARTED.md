# Getting started (no coding required)

This guide is for Shopify merchants, marketers, SEOs, and agency people who are **not developers**.

You do not need to install anything, use a terminal, or know how to code. If you can download a file and drag it into a browser, you can do this. It takes about 5 minutes the first time, and about 10 seconds every time after that.

---

## What these Skills actually are

A "Skill" is a set of expert instructions you give to Claude once. After that, Claude follows a professional audit process instead of improvising a generic answer.

Concretely:

- **Without a Skill:** you ask "how's my Shopify SEO?" and get generic advice you could have found in any blog post.
- **With a Skill:** Claude runs the same structured audit a specialized Shopify agency runs — checks the issues specific to Shopify, ranks them by impact vs. effort, and hands you a prioritized action list your team can execute.

You install a Skill once. It stays in your account and Claude uses it automatically whenever it's relevant.

---

## Which Skill do I need?

Pick one to start. You can install the others later.

| If you want to... | Use this Skill |
| --- | --- |
| Know where to focus next quarter to grow the store | `shopify-ecommerce-director` |
| Understand why you don't get enough traffic from Google | `shopify-seo-auditor` |
| Move to Shopify without losing your Google rankings | `shopify-migration-seo-guardian` |
| Find out why visitors don't buy | `shopify-cro-auditor` |
| Have your theme's code checked for bugs and slowness | `shopify-liquid-reviewer` |
| Check whether your Google Analytics numbers can be trusted | `shopify-tracking-ga4-auditor` |
| Build or fix your Klaviyo emails and automations | `shopify-email-klaviyo-strategist` |
| Plan selling to businesses (wholesale) on Shopify | `shopify-b2b-advisor` |

Not sure? Start with **`shopify-ecommerce-director`**. It looks at the whole business and tells you which area to dig into first.

---

## Before you start

- **A Claude account** — free, Pro, Max, Team, or Enterprise. Go to [claude.ai](https://claude.ai).
- **Code execution turned on** in Claude. Check **Settings → Capabilities** and make sure it's enabled. (Skills won't appear without it.)
- On **Team** or **Enterprise** plans, an admin may need to enable Skills first in the organization settings.

---

## Step 1 — Download the Skills

1. Go to the repository: **https://github.com/Pikka-Shopify/Pikka-shopify-skills**
2. Click the green **`Code`** button near the top right.
3. Click **`Download ZIP`**.
4. Open the downloaded file — `Pikka-shopify-skills-main.zip` — to unzip it.
   - **Windows:** right-click the file → *Extract All* → *Extract*.
   - **Mac:** double-click the file.

You now have a folder called `Pikka-shopify-skills-main`. Open it — you'll see one folder per Skill, each named after the Skill (`shopify-seo-auditor`, `shopify-cro-auditor`, and so on).

---

## Step 2 — Make a ZIP of the one Skill you want

Claude expects **one Skill per ZIP file** — not the whole collection at once.

Find the folder for the Skill you picked in the table above (for example `shopify-seo-auditor`), then:

- **Windows:** right-click the folder → *Send to* → *Compressed (zipped) folder*.
- **Mac:** right-click the folder → *Compress "shopify-seo-auditor"*.

You now have a file called `shopify-seo-auditor.zip`. That's what you'll upload.

> **Important:** compress the **folder**, not the `SKILL.md` file that's inside it. The ZIP has to contain the folder.

Want more than one Skill? Repeat this step for each one and upload them one at a time.

---

## Step 3 — Upload it to Claude

1. Go to [claude.ai](https://claude.ai) and open **Customize → Skills** (via Settings).
2. Click the **`+`** button, then **`Create skill`**.
3. Choose **`Upload a skill`**.
4. Select the ZIP file you just made.

Claude reads the file and shows you the Skill's name and description. Make sure its toggle is **on**.

That's it. The Skill now lives in your account, on web, desktop, and mobile.

---

## Step 4 — Use it

Start a new conversation and just describe your situation in plain English. Claude picks the right Skill on its own.

If you want to be sure, name it explicitly: *"Use the Shopify SEO auditor Skill."*

### Copy-paste starter prompts

Replace the text in `[brackets]` with your own details.

**SEO audit**

> Use the Shopify SEO auditor Skill. My store is `[yourstore.com]`. We sell `[what you sell]` in `[country/language]`. We have roughly `[number]` products and `[number]` collections. My main problem is `[e.g. organic traffic has been flat for 6 months]`. My goal is `[e.g. get more non-brand traffic from Google]`. Give me a prioritized plan.

**Why visitors don't buy (CRO)**

> Use the Shopify CRO auditor Skill. My store is `[yourstore.com]`, we sell `[what you sell]` at an average order value of `[amount]`. My conversion rate is `[x]%` and about `[x]%` of my traffic is mobile. Where is the friction, and what should I fix first?

**Growth priorities**

> Use the Shopify e-commerce director Skill. Here's my store: `[describe it in a few sentences]`. Monthly revenue is around `[amount]`, traffic is around `[sessions/month]`, conversion rate `[x]%`, average order value `[amount]`. My budget and team are `[describe]`. What should I do over the next 90 days?

**Email / Klaviyo**

> Use the Shopify Klaviyo strategist Skill. We sell `[what you sell]`, average order value `[amount]`, repurchase cycle roughly `[e.g. every 3 months]`. We currently have `[e.g. only an abandoned cart email]` set up and a list of `[number]` subscribers. Build me a lifecycle email plan.

### Give it whatever you have

You don't need perfect data. Screenshots, a CSV export from Google Analytics or Search Console, a link to your store, or just a description in your own words — all of it works. If something important is missing, the Skill will tell you what it is and how it would change the analysis, then carry on with what it has.

You can also just paste your store URL and ask. It will ask you a couple of questions to fill the gaps.

---

## What you get back

Not a wall of generic advice. Each Skill produces a structured deliverable — typically:

- A diagnosis of where you stand
- The critical issues, named specifically
- Recommendations split between technical and non-technical
- A priority matrix (what has the most impact for the least effort)
- A checklist your team or agency can actually execute

You can ask Claude to turn any of it into a document, a spreadsheet, or a slide deck.

---

## If something goes wrong

**I don't see "Skills" in my settings.**
Code execution isn't enabled. Go to **Settings → Capabilities** and turn it on. On Team/Enterprise, ask your admin to enable Skills for the organization.

**Claude rejected my ZIP file.**
You most likely zipped the `SKILL.md` file instead of the folder containing it. Go back to Step 2 and compress the folder itself (e.g. `shopify-seo-auditor`).

**Claude isn't using the Skill.**
Two things to check: the Skill's toggle is on in your Skills list, and you're in a **new** conversation. Then say it outright: *"Use the Shopify SEO auditor Skill."*

**The answer feels generic.**
Give it more context — your store URL, what you sell, your numbers, and above all your *goal*. The quality of the output tracks the quality of the input. Also, don't stop at the first answer: push back, ask "why", ask it to go deeper on one issue.

**I use ChatGPT / another AI.**
These Skills are built for Claude, but they're just plain text. Open the `SKILL.md` file of the Skill you want in a text editor, copy everything, paste it into your chat, then describe your store. It works less smoothly, but it works.

---

## Honest expectations

These Skills give you a **strong first pass** — the kind of structured analysis that normally takes an experienced consultant a few days. They're genuinely useful and we use these exact frameworks internally.

What they can't do: see inside your Shopify admin, look at your real analytics unless you paste it in, know your market and your constraints, or decide which of the twenty findings actually matters most for *your* store. And they can't implement anything.

Treat the output as a well-argued starting point. Validate before you act on a live store.

---

## Stuck on what the output means?

We're [Pikka](https://www.pikka.fr), the French Shopify agency that wrote these Skills. If you've run one and want a second pair of eyes on the result, we offer a **free 30-minute review** — no strings attached.

Send the output to **`contact@pikka.fr`** or reach us at [pikka.fr](https://www.pikka.fr).

---

Back to the [main README](README.md) for the full technical details, or [CONTRIBUTING.md](CONTRIBUTING.md) if you want to suggest an improvement.
