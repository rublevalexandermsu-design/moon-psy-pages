# Moonn Teen Psychology Camp Payment Report — 2026-05-09

## Scope

Add a real payment entry point to the teen psychology camp page on `moonn.ru` while preserving the existing Tilda/T-Bank payment flow and without entering real card data.

## Live page

- URL: https://moonn.ru/podrostkovyy-lager-psihologiya
- Tilda project: `8326812`
- Tilda page id: `140348786`
- Product: `Подростковый лагерь по психологии`
- SKU: `teen-camp-2026`
- Price: `30000`
- Native order link:
  `#order:Подростковый лагерь по психологии =30000:::image=https://cdn.jsdelivr.net/gh/rublevalexandermsu-design/moonn-psy-pages@b28b5f48939f8f640a218be50ac278ca24969ace/assets/teen-psychology-camp-2026/teen-psychology-camp-tatyana-moonn-poster-2026.jpg`

## Payment settings found on the page

The live Tilda page includes the native Tilda cart block:

- Record id: `rec2251553291`
- Block type: `706`
- Runtime script: `tilda-cart-1.1.min.js`
- Payment options visible in cart:
  - `Visa, МИР, Mastercard через T-Bank`
  - `Рассрочка Т-Банк`

## Changes

- Added/kept a visible price/payment block in the landing page with the `30 000 ₽` participation price.
- Added a direct `Оплатить участие` CTA.
- Preserved the native Tilda cart instead of replacing it with a custom payment implementation.
- Added a runtime repair in `tilda-page-final.html` so the custom rendered page restores the native `.t706` cart structure when the older compact loader has moved cart nodes.
- Bound payment CTA clicks to native Tilda cart functions:
  - `tcart__addProduct`
  - `tcart__reDrawCartIcon`
  - `tcart__openCart`
- Purged the encoded jsDelivr branch URL after the GitHub update so the live Tilda loader received the current page artifact.

## Root causes fixed

1. The first custom Tilda loader used full body replacement, which removed or displaced the native Tilda cart DOM.
2. Tilda timed out when saving a very large page HEAD payload, so the page needed a compact loader plus external page artifact.
3. The jsDelivr branch URL with `/` in the branch name needed encoded purge to refresh reliably.
4. Native `#order` parsing was not enough after custom rendering, so the CTA now calls the native Tilda cart API directly.

## Verification

Live/source checks:

- `https://moonn.ru/podrostkovyy-lager-psihologiya` returns the page with the compact loader.
- The external page artifact contains `openTeenCampPayment` and the cart repair logic.
- The live page keeps the native `.t706` cart record.
- The PDF URL returns `200`, `application/pdf`, size `245793`.

Headless browser check:

- Payment CTA exists.
- Clicking `Оплатить участие` opens the Tilda cart modal.
- The cart contains:
  - `Подростковый лагерь по психологии`
  - `teen-camp-2026`
  - `30 000р.`
  - T-Bank card payment
  - T-Bank installment option
- Screenshot artifact:
  - `docs/teen-psychology-camp-2026/cart-headless-check.png`

Real Chrome check:

- Opened the live page in Google Chrome.
- Verified the payment modal is visible with the order, price and T-Bank payment options.
- Did not enter card data.
- Did not submit a real payment.

## Compliance / risk boundary

This rollout enables the real checkout path but stops before payment submission. A full acquiring test should be a separately approved scenario with a small real payment and refund/check in the T-Bank/Tilda order dashboard.

The page still has a privacy-policy/cookie layer. If a native Tilda payment form stores order/contact data, the broader RKN checklist should keep tracking required consent language and operator details for the site-wide policy.

## Commits

- `641aaab` — Add teen camp payment CTA artifacts
- `ee85b0a` — Preserve Tilda cart on teen camp page
- `edcd706` — Initialize Tilda cart after teen camp render
- `abb9dcb` — Preserve Tilda allrecords for teen camp cart
- `4e40ac1` — Add compact teen camp Tilda loader
- `9ef31b6` — Fix teen camp cart preservation in loader
- `4472b6b` — Repair teen camp Tilda cart runtime
- `95f6853` — Open teen camp payment through Tilda cart

## Follow-up rule

For future paid Moonn/Tilda pages, first verify whether a native Tilda cart/payment block already exists. Reuse it and test the actual cart modal before introducing any custom payment layer. Do not report payment setup as complete unless a browser click opens the real provider-backed checkout form and the no-real-payment boundary is explicitly recorded.
