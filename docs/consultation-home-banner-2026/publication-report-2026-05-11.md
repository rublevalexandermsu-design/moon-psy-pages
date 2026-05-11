# 2026-05-11 Consultation Homepage Banner

## Scope

- Project: Moonn / Tatiana Moonn.
- Workstream: homepage consultation banner with native Tilda cart payment.
- Branch: `codex/moonn-consultation-home-banner`.
- Homepage page id: `42678538`.

## Source Facts

- Banner reference supplied by user in Codex chat on 2026-05-11.
- Public offer facts extracted into `consultation-products.json`.
- Payment route follows the existing native Tilda cart / T-Bank pattern used for the teen camp workstream.

## Products

- `moonn-consultation-online-1-2026`: `Онлайн-консультация Татьяны Мунн`, 8 000 RUB.
- `moonn-consultation-online-3-summer-2026`: `Пакет 3 онлайн-консультаций Татьяны Мунн`, 19 000 RUB.
- Regular 3-consultation price shown as 21 000 RUB.
- Valid-through text shown as `до 31 августа`.

## Artifacts

- `docs/consultation-home-banner-2026/tilda-html-block-final.html` - native Tilda `T123` HTML block.
- `docs/consultation-home-banner-2026/consultation-products.json` - machine-readable product manifest.
- `docs/consultation-home-banner-2026/local-preview.html` - local QA wrapper with a mocked Tilda cart.

## Publication Gate

- Do not submit a real payment.
- Verify live homepage contains `moonn-consultation-home-banner` after publication.
- Verify both payment CTAs open native Tilda cart with correct amounts.
- Verify T-Bank provider screen is reachable without entering or submitting card data.

## Local Verification

- Local preview served from `docs/consultation-home-banner-2026` on `127.0.0.1:8765`.
- Playwright desktop render check passed: banner is visible and public text is readable.
- Playwright mobile render check passed after removing the noisy old-poster background from the main layout.
- Mock cart check passed for `moonn-consultation-online-1-2026`: product name and `8000 RUB` amount reached the cart.
- Mock cart check passed for `moonn-consultation-online-3-summer-2026`: product name and `19000 RUB` amount reached the cart.

## Tilda Editor Check

- Homepage editor page opened: `pageid=42678538`.
- Existing homepage native T123 banner record found: `rec2251351151`.
- Existing native cart record found through Tilda API: `rec792077353`, block type `706`.
- The existing teen-camp T123 block was preserved and the consultation banner was appended below it in the same native T123 block.
- The homepage was published from Tilda UI after the T123 update.

## Live Verification

- Live URL checked: `https://moonn.ru/?consult-banner-check=20260512-0019`.
- HTTP status: `200`.
- Live raw HTML contains:
  - `moonn-teen-camp-home-banner`
  - `moonn-consultation-home-banner`
  - native cart/Tilda payment markers.
- Live rendered browser contains the consultation banner with:
  - `1 консультация - 8 000 ₽`
  - `3 консультации - 21 000 ₽`
  - `Летняя цена - 19 000 ₽`
- Live cart smoke test:
  - Clicking `Оплатить 1 консультацию` opened the native Tilda cart.
  - Product name: `Онлайн-консультация Татьяны Мунн`.
  - SKU: `moonn-consultation-online-1-2026`.
  - Amount: `8 000р.`.
  - Clicking `Оплатить пакет 3 консультации` opened the native Tilda cart.
  - Product name: `Пакет 3 онлайн-консультаций Татьяны Мунн`.
  - SKU: `moonn-consultation-online-3-summer-2026`.
  - Amount: `19 000р.`.
- No real payment was submitted.

## Status

- Consultation homepage banner is live on `https://moonn.ru/`.
- Native cart opens with the correct one-consultation and three-consultation products and amounts.
- T-Bank provider transition without card submission still remains a separate high-risk payment QA step.
