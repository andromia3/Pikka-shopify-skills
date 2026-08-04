# Liquid Code Review Rules

Concrete rules for reviewing Liquid for correctness, readability, duplication, and coupling. Cite the file and construct for every finding.

## 1. Correctness and bugs

- **Nil / blank handling.** Guard against missing data: use `if object != blank`, default filters (`| default:`), and handle empty collections, missing images, and unset metafields. Unhandled `nil` produces blank output or errors.
- **Loops.** Check `for` loops for correct `limit`, `offset`, and `forloop` usage; avoid unbounded loops over large collections that slow rendering.
- **Pagination.** Use `paginate` correctly; don't render all products when paginating; verify `default_pagination`.
- **Filters.** Verify filter chains produce the expected type (e.g. `money` filters on numbers, `date` on dates). Watch for `| money` without a shop currency context, or string/number mismatches.
- **Conditionals.** Watch truthiness: in Liquid, `0`, empty string, and empty array are truthy except `nil`/`false`/`blank` rules. Verify `unless`/`else` logic.
- **Whitespace control.** Use `{%-` / `-%}` to avoid stray whitespace where it matters (especially in JSON/`<script type="application/json">`).
- **Edge states.** Confirm out-of-stock, sold-out, single-variant, no-image, and zero-results states render correctly.

## 2. Readability and maintainability

- **Naming.** Variables (`assign`) and snippet parameters should be descriptive. Avoid `x`, `temp`, cryptic abbreviations.
- **Logic density.** Heavy business logic embedded in templates is a smell. Extract to snippets or compute once and pass down.
- **Comments.** Use `{% comment %}` for non-obvious intent. Don't leave dead/commented-out blocks in production.
- **Consistency.** Consistent indentation, tag style, and filter usage across files.
- **File length.** Very long sections/snippets that do many things should be split by responsibility.

## 3. Duplicated logic (DRY)

- Repeated markup/logic across sections (e.g. product card rendered five different ways) should be a single snippet with parameters.
- Repeated computed values (price formatting, badge logic, savings calc) should be computed once in a snippet, not copy-pasted.
- Repeated settings patterns suggest a shared block or snippet.
- **Rule:** if the same logic appears 3+ times, recommend extracting a snippet. Note the duplication locations.

## 4. Snippets and `render` vs `include`

- Use `{% render %}` (isolated scope) over the deprecated `{% include %}` (leaky scope). Flag any `include` usage.
- Pass explicit parameters to `render`; don't rely on ambient variables.
- A snippet should have one clear responsibility and a documented set of inputs.

## 5. JavaScript coupling

- **Separation.** JS should be in theme assets or `<script>` blocks tied to a section, not scattered inline across Liquid.
- **Section-scoped JS.** For OS 2.0, prefer JS that scopes to the section instance (e.g. via `section.id`) so multiple instances don't collide.
- **Data passing.** Pass Liquid data to JS via a `<script type="application/json">` block (escaped) rather than inlining values into JS string literals.
- **Event re-binding.** In the theme editor, sections re-render; verify JS re-initializes on `shopify:section:load` and cleans up on `shopify:section:unload`.
- **Global leakage.** Watch for globals, duplicate event listeners, and memory leaks.

## 6. App embed and third-party risk

- **App embeds / blocks.** Note app embeds in `theme.liquid` and app blocks in templates; some inject heavy/blocking scripts.
- **Leftover app code.** Removed apps often leave snippets, `<script>` tags, or `{% render 'app-...' %}` calls that 404 or error. Flag orphaned app code.
- **Liquid injected by apps.** Be cautious editing app-managed blocks; document them as risk areas rather than refactoring blindly.
- **Security.** Flag inline third-party scripts loaded without integrity/async, and any secrets or tokens hardcoded in theme files (must never happen).

## 7. Data exposure

- Avoid dumping large objects with `| json` into the page (e.g. entire `cart`, `customer`, or `all_products`) — it bloats the DOM and can leak data.
- Never expose admin/private data, internal IDs that shouldn't be public, or PII in rendered JSON.

## 8. Internationalization

- Use translation keys (`{{ 'general.search.title' | t }}`) and locale files, not hardcoded strings.
- Use `money` filters for prices (respect shop/locale currency), not manual formatting.
- Flag hardcoded user-facing strings as i18n debt.
