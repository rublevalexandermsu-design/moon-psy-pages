# Moonn Paid Video Lectures Checkout Update - 2026-05-17

## Scope

- Project: Moonn / Tatyana Munn site and paid lecture products.
- Workstream: paid recordings on the canonical lecture page.
- Branch: `codex/moonn-paid-video-lectures`.
- Storefront page: `https://moonn.ru/events_tp`.
- Tilda page id: `66814657`.

## Strategic Check

1. Platform value: high. This turns existing lecture recordings into reusable digital products.
2. Obsolescence risk: high if edited only by hand in Tilda. Prices, YouTube ids, access groups and bundle rules will drift.
3. Stronger architecture: manifest-first product registry, then Tilda catalog/cart, then protected watch pages.
4. Reuse: high. The same product/access pattern can support future courses, lecture bundles, Timepad follow-up offers and QR campaigns.
5. 3-12 month risk if weak: wrong videos sold, raw private links leaked, buyer receives no access after payment, support workload grows, and bundle purchases cannot be audited.

## Verified Facts

- Existing canonical paid-lecture workstream already exists on branch `codex/moonn-paid-video-lectures`.
- Existing canonical page is `events_tp`, Tilda page `66814657`.
- The manifest previously contained 10 lecture candidates extracted from the live `events_tp` Timepad links.
- Previous default lecture price was `1300 RUB`; the new user decision is `2000 RUB` per recording.
- New bundle decision: `5000 RUB` for a package of five lecture recordings.
- Five `events_tp` lectures already have unique private YouTube match status in the sanitized registry; four need owner selection; the recurring `3334362` entry is not a single recording yet.
- Tilda documentation says paid access can be granted through cart/payment plus the "Личный кабинет" receiver only after successful payment.
- Tilda catalog supports CSV import/export; the CSV separator in Tilda's example is semicolon.
- YouTube unlisted video is not access protection because anyone with the link can view/share it.

## Applied Registry Changes

- Updated `registry/products/paid-video-lectures.manifest.json`:
  - `default_price_rub`: `2000`;
  - `bundle_price_rub`: `5000`;
  - `bundle_selection_count`: `5`;
  - all 10 lecture candidates now have `price_rub: 2000`;
  - added bundle product `moonn-video-bundle-5-choice`;
  - added support metadata with WhatsApp phone and pending Telegram URL;
  - strengthened fulfillment rule: do not send raw YouTube links; embed videos only inside protected Tilda Members/Courses pages.
- Updated `registry/products/paid-video-lectures.schema.json` with bundle/support fields.
- Added `scripts/prepare_paid_video_lecture_products.py` to regenerate the manifest and Tilda catalog draft deterministically.
- Generated `registry/products/paid-video-lectures-tilda-catalog-2026-05-17.csv`:
  - 10 single lecture products;
  - 1 bundle product;
  - public buttons: `Получить запись` and `Выбрать пакет`;
  - no raw YouTube URLs.

## Public Storefront Copy

Use this block on `events_tp` near the lecture cards:

```text
Записи лекций Татьяны Мунн
Каждую запись можно приобрести отдельно за 2 000 ₽. Доступ открывается после оплаты в закрытом разделе сайта.

Пакет из 5 записей на выбор — 5 000 ₽
Выберите пять тем после оплаты. Если возник вопрос по доступу, напишите Татьяне Мунн в Telegram или WhatsApp.
```

Per lecture button:

```text
Получить запись
```

Bundle button:

```text
Выбрать пакет
```

## Access Model

Recommended implementation:

1. Create/import Tilda catalog products from the generated CSV.
2. Use the existing configured payment provider only after visual verification of seller/payment settings.
3. Connect successful payment to Tilda Members/Courses access groups.
4. For a single lecture, grant access to the matching protected watch page.
5. For the five-lecture bundle, grant access to a protected selection page/form and write the final five selected lectures to the order/access registry.
6. Embed YouTube videos only inside protected pages; do not email raw YouTube links as the main fulfillment method.

## High-Risk Gates

Do not publish live payment/access until these are verified:

- Tilda payment provider and seller details are correct.
- Checkout displays the correct product, price and seller/payment info.
- Payment settings send data to receivers only after successful payment.
- Refund/offer/privacy/legal pages are available and linked.
- Each sold lecture has a final protected watch page or a controlled "pending access" operational process.
- Telegram support URL is confirmed.
- One test purchase is completed and the buyer sees the correct protected content.

## Validation

Local validation completed:

- manifest price contract: single `2000`, bundle `5000`, bundle size `5`;
- 10 lecture products and 1 bundle product in the generated Tilda CSV;
- generated manifest/CSV do not contain raw `youtube.com/watch`, `youtu.be/` or `youtube.com/embed/` URLs.

## Sources Checked

- Tilda Members: paid access after payment through cart/payment and "Личный кабинет".
- Tilda payment systems: payment providers are configured in site settings; Tilda supports T-Bank and other providers; test payments are recommended in a controlled amount.
- Tilda catalog import: CSV/YML import is supported; CSV examples use semicolon separators.
- YouTube Help: unlisted videos can be viewed and shared by anyone with the link.

## Next Actions

1. Open Tilda UI and visually verify payment provider/seller settings.
2. Import or create catalog products from `registry/products/paid-video-lectures-tilda-catalog-2026-05-17.csv`.
3. Add storefront block and replace lecture card buttons with product/cart actions.
4. Create protected watch pages/groups for the five uniquely matched recordings first.
5. Get owner decision for the four ambiguous YouTube matches and the `3334362` recurring series entry.
6. Run one controlled checkout/access test before public rollout.
