# GA4 E-commerce Event Taxonomy

The standard GA4 recommended e-commerce events, when they should fire on a Shopify store, and the parameters that must be present. Use this to verify coverage and correctness.

## Shared rules

- Use GA4's **recommended event names** exactly (`view_item`, `add_to_cart`, `purchase`, etc.). Custom names break standard reports.
- Monetary events must include `currency` (ISO 4217, e.g. `EUR`) and `value` (number). If `value` is present, `currency` is required.
- Item-scoped events include an `items` array. Keep `item_id` consistent everywhere (and aligned with your product feed / Merchant Center).
- Send numbers as numbers, not strings.

## The `items` array

Each item object should include:

| Field | Required | Notes |
| --- | --- | --- |
| `item_id` | Yes | SKU or product/variant ID; consistent across events & feed |
| `item_name` | Yes | Product name |
| `price` | Recommended | Unit price (number) |
| `quantity` | Recommended | Integer |
| `item_brand` | Optional | Brand |
| `item_category` | Optional | Category / collection |
| `item_variant` | Optional | Variant (size/color) |
| `index` | Optional | Position in a list |
| `item_list_name` / `item_list_id` | Optional | For list events |

## Events and when they fire

### `view_item_list`
- **When:** a collection/search/listing page renders products.
- **Params:** `items` (with `item_list_name`/`item_list_id`), and list context.
- **Use:** measures merchandising/list performance.

### `select_item`
- **When:** a user clicks a product in a list.
- **Params:** the clicked `items` entry, list context.

### `view_item`
- **When:** a product detail page is viewed.
- **Params:** `currency`, `value` (item price), `items` (the product).

### `add_to_cart`
- **When:** a product is added to cart (button click / AJAX add).
- **Params:** `currency`, `value` (added value), `items` (with `quantity`).
- **Watch:** don't fire on page load; fire on the actual add.

### `remove_from_cart`
- **When:** an item is removed from cart.
- **Params:** `currency`, `value`, `items`.

### `view_cart`
- **When:** the cart page/drawer is viewed.
- **Params:** `currency`, `value`, `items`.

### `begin_checkout`
- **When:** the customer enters checkout.
- **Params:** `currency`, `value`, `items`, optional `coupon`.

### `add_shipping_info`
- **When:** shipping option selected.
- **Params:** `currency`, `value`, `items`, `shipping_tier`.

### `add_payment_info`
- **When:** payment info added.
- **Params:** `currency`, `value`, `items`, `payment_type`.

### `purchase`  (the critical one)
- **When:** order completed (thank-you / order status), **once per order**.
- **Required params:** `transaction_id` (Shopify order id/number), `currency`, `value`, `items`.
- **Recommended:** `tax`, `shipping`, `coupon`.
- **Rules:** dedupe on `transaction_id`; ensure `value` definition (with/without tax & shipping) is consistent with your reporting; reconcile against Shopify orders.

### `refund` (if needed)
- **When:** an order is refunded (often server-side).
- **Params:** `transaction_id`, `currency`, `value`, `items` (for partial refunds).

## Coverage matrix (use in the audit)

| Event | Expected page/trigger | Present? | Fires once / correct time? | `items` correct? | `currency`+`value`? | Source |
| --- | --- | --- | --- | --- | --- | --- |
| view_item_list | Collection/list | | | | | |
| view_item | PDP | | | | | |
| add_to_cart | Add action | | | | | |
| view_cart | Cart | | | | | |
| begin_checkout | Checkout start | | | | | |
| add_shipping_info | Shipping step | | | | | |
| add_payment_info | Payment step | | | | | |
| purchase | Order complete | | | | | |

## Common Shopify pitfalls

- `purchase` firing on every thank-you-page load (refresh double counts) — dedupe on `transaction_id`.
- Missing `currency` on multi-currency / Markets stores.
- `item_id` mismatch between storefront events and feed/Merchant Center (breaks product-level analysis and Ads).
- Events implemented via deprecated checkout additional scripts instead of Web Pixels / Customer Events.
- Two GA4 sources sending the same event (app + custom pixel/GTM).
