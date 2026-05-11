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
- Current visible Tilda editor session is usable for navigation, but automated code-editor copy/paste did not focus the T123 code editor reliably during this run.
- No live Tilda save or publish was performed from this run.

## Status

- Artifact prepared and locally verified.
- Live Tilda publication and provider-screen verification are still pending.
