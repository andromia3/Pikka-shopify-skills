# Theme Architecture Rules (Online Store 2.0)

How a healthy modern Shopify theme is structured, and what to flag.

## 1. Online Store 2.0 baseline

A modern theme should use OS 2.0 patterns:

- **JSON templates** (`templates/*.json`) that compose **sections**, rather than monolithic `.liquid` templates with hardcoded layout.
- **Sections everywhere**: sections usable on any page, with **blocks** for repeatable, merchant-configurable content.
- **App blocks** support so merchants can add app content without code.
- **Theme settings** (`config/settings_schema.json`) for global configuration.

**Flag** legacy patterns: hardcoded layout in templates, content that should be editable but is baked into Liquid, no section/block structure.

## 2. Sections and blocks

- A section should represent one coherent piece of UI with a clear `{% schema %}`.
- Use **blocks** for repeatable items (slides, columns, FAQ items) so merchants can add/remove/reorder.
- Respect block `type`, `limit`, and `max_blocks`. Render blocks with `{{ block.shopify_attributes }}` for editor support.
- Avoid "god sections" that try to be everything; split by responsibility.
- Section settings should have sensible defaults and clear labels (these surface in the theme editor).

## 3. Schema settings design

- Every setting needs a clear `id`, `label`, and `type`; group with `header` settings; provide `default` values.
- Use the right input type (`range`, `select`, `color`, `image_picker`, `richtext`, `url`, `product`, `collection`).
- Don't over-expose: too many settings overwhelm merchants; too few make the section rigid. Aim for the settings a merchant actually needs.
- Validate that `settings_schema.json` (global) and section schemas are valid JSON and load in the editor.
- Locale-aware labels via `t:` translation keys where the theme supports it.

## 4. Snippets boundaries

- Snippets = reusable, parameterized partials (product card, price, rating, icon). One responsibility each.
- Pass explicit parameters via `render`; document expected inputs at the top with a comment.
- Don't let snippets reach for global/ambient variables — that creates hidden coupling.

## 5. Metafields and metaobjects

- **Metafields** extend products/collections/etc. with structured data (specs, badges, care instructions). Prefer them over hardcoding or abusing tags/product descriptions.
- **Metaobjects** model custom content types (e.g. ingredients, designers, size guides) reused across the store.
- **Rules to check:**
  - Are metafields referenced with the correct namespace/key and type-aware rendering (e.g. `metafield.value`, handling `list.` types and references)?
  - Is there graceful fallback when a metafield is empty?
  - Is tag-hacking used where metafields/metaobjects would be cleaner? Flag it.
  - Are metaobject references resolved correctly (not rendering raw GIDs)?

## 6. Layout and theme.liquid

- `theme.liquid` should contain the document shell, critical `<head>` tags (canonical, meta, preloads), and app embed region — not page-specific logic.
- Verify `{{ content_for_header }}` and `{{ content_for_layout }}` are present and correct.
- Critical CSS/preloads in `<head>`; defer non-critical JS.

## 7. Configuration vs code

- Content a merchant should control (text, images, order, toggles) belongs in **settings/blocks**, not hardcoded Liquid.
- Conversely, structural logic shouldn't be exposed as fragile merchant settings.
- Flag mismatches in both directions.

## 8. Architecture smells to flag

- Monolithic legacy templates with no sections.
- Duplicated section variants that should be one configurable section.
- Business logic in `theme.liquid` or templates instead of snippets.
- Tag-based hacks substituting for metafields/metaobjects.
- Hardcoded content that merchants need to edit.
- Inconsistent structure across similar sections (sign of accreted, unplanned growth).
