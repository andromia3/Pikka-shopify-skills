# Contributing to Pikka Shopify Skills

Thanks for your interest in improving this collection. Contributions of all sizes are welcome: a typo fix, a sharper checklist item, a new example, or a whole new Skill.

## Ways to contribute

- **New Skills** — propose a new Shopify-focused Skill (e.g. accessibility, international expansion, subscriptions).
- **Improvements** — sharpen an existing checklist, framework, or output template; add a missing edge case.
- **Corrections** — fix outdated Shopify behavior, broken links, wrong terminology, or typos.
- **Examples** — add realistic (anonymized) usage examples that show a Skill in action.
- **Issue reports** — flag something confusing, incorrect, or unsafe.

## Before you start

- Open an issue first for anything non-trivial (a new Skill or a structural change) so we can align on scope.
- For small fixes (typos, link fixes, a clearer sentence), a pull request directly is fine.

## Quality bar

Everything in this repo should be **concrete and immediately usable**. When contributing:

- Write in clear, professional English, oriented toward action.
- Prefer real working methods over generic advice. Checklists must be specific to Shopify where relevant.
- Output templates must be copy-pasteable (use markdown tables and headings).
- Do not make unrealistic promises or guarantee specific business results.
- Never include secrets, tokens, credentials, or personal data — not even as examples.
- Keep the tone professional and useful, not marketing fluff.

## Authoring or editing a Skill

Each Skill lives in `<skill-name>/` at the repository root and follows these conventions:

- **Folder names use kebab-case** and start with `shopify-` (e.g. `shopify-cro-auditor`).
- Each Skill has a `SKILL.md` and a `references/` folder.
- `SKILL.md` starts with YAML frontmatter (`name`, `description`) and contains, in order:
  1. Title
  2. Short description
  3. When to use this Skill
  4. Expected inputs
  5. Workflow
  6. Quality rules
  7. Expected outputs
  8. Reference files to consult
- The `description` in the frontmatter should clearly state what the Skill does and when to use it, so Claude can select it automatically.
- Reference files should contain the actual methods, checklists, rules, and templates — not summaries that point elsewhere.
- Reference filenames listed in `SKILL.md` must exactly match the files in `references/`.

## Pull request checklist

- [ ] Folder and file names follow the conventions above (kebab-case, `shopify-` prefix).
- [ ] `SKILL.md` includes all required sections and valid frontmatter.
- [ ] Every reference file mentioned in `SKILL.md` exists, and vice versa.
- [ ] Content is concrete, accurate, and free of secrets or personal data.
- [ ] No destructive or unsafe instructions were introduced.
- [ ] Links work and markdown renders cleanly.

## Reporting issues

Open a GitHub issue describing:

- The Skill or file affected.
- What you expected vs. what you found.
- Steps to reproduce (for usage problems) or a suggested fix.

For security concerns, follow [SECURITY.md](SECURITY.md) instead of opening a public issue.

## License of contributions

By contributing, you agree that your contributions are licensed under the [MIT License](LICENSE) that covers this project.
