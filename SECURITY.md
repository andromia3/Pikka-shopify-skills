# Security Policy

These Skills are reasoning and documentation tools. They are designed to be safe, transparent, and auditable.

## Security principles

- **No destructive actions by default.** The Skills analyze, plan, and recommend. They never instruct the agent to delete data, drop redirects, overwrite themes, or modify a live store without explicit, informed confirmation from you.
- **No credential collection.** The Skills never ask for passwords, API tokens, Shopify Admin access tokens, payment data, or any secret. If a workflow needs data, it asks for exports or descriptions, not credentials.
- **No secret exposure.** Reference files and output templates contain no real keys, tokens, or personal data. Do not paste secrets into prompts when using these Skills.
- **Human review required.** Every recommendation is a starting point. Review and validate output before applying anything to a production store, theme, or tracking setup.

## Safe usage guidelines

- Run analyses against **exports and copies** (crawl files, anonymized analytics, theme snapshots) rather than granting live admin access.
- Treat redirect maps, tracking changes, and theme refactors as **proposals to review**, not commands to execute.
- Before applying changes on a live store, take a backup (duplicate the theme, export current redirects) so you can roll back.
- Remove personally identifiable information (customer emails, order data) from anything you paste into a prompt.

## Reporting a vulnerability or concern

If you find a security issue in this repository — for example, a Skill that could lead an agent toward an unsafe action, or content that exposes sensitive data — please report it.

- Email: `contact@pikka.fr`
- Please include a clear description, the affected file(s), and steps to reproduce if relevant.

We will acknowledge the report and work on a fix. Please give us reasonable time to address the issue before any public disclosure.
