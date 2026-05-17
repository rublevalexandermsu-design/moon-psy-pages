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

## Tilda UI Execution - 2026-05-17

Verified in the Tilda UI:

- site payment settings use `Russian Ruble (RUB)`;
- `Visa, MIR, Mastercard via T-Bank` is active;
- `T-Bank installments` is active;
- existing Tilda catalog was exported before import and saved as `registry/products/tilda-catalog-backup-before-paid-lectures-2026-05-17.csv`;
- `registry/products/paid-video-lectures-tilda-catalog-2026-05-17.csv` was imported into Tilda Product Catalog;
- import result: 11 processed products;
- Tilda catalog now contains category `Записи лекций` with single lecture products at `2000 RUB`;
- Tilda catalog now contains category `Пакеты записей` with product `moonn-video-bundle-5-choice` at `5000 RUB`.

Draft editor changes on Tilda page `66814657`:

- added store cart block `ST100`;
- added catalog block `ST315N`;
- connected `ST315N` to category `Записи лекций`;
- preview opened the product page for SKU `moonn-video-lecture-3808783`;
- preview showed product price `2 000 р.`;
- preview showed the imported access/support description and no raw YouTube URL.

Not published:

- Tilda API `getpagefull` still returns the published page without `ST100`/`ST315N`, so the public page has not been changed yet.

Current blockers before publication:

- product page button text is still `BUY NOW`; change it to `Получить запись`;
- bundle product `moonn-video-bundle-5-choice` is imported but not yet exposed in the checked storefront block;
- the buyer access path after successful payment is not yet tested end to end;
- protected watch pages/Members groups are still needed before real paid rollout;
- Telegram URL is still not confirmed.

## Correction - Existing Card Conversion - 2026-05-17

User correction:

- The added `ST315N` product catalog block duplicated lectures and was not the requested interaction model.
- The correct model is one canonical lecture page:
  - lectures with dates before the current Moscow date become paid recordings;
  - future lectures keep the existing `Регистрация` CTA;
  - existing `T774` lecture cards must be reused instead of creating a second catalog grid.

Root cause:

- The previous implementation interpreted "connect payment" as "add a new catalog storefront".
- That created a duplicate visual layer and left the canonical lecture cards unchanged.

Fix applied in Tilda:

- Removed the visible `ST315N` catalog/store block from page `66814657`.
- Kept the cart/payment layer available for `#order:` links.
- Added a `T123` HTML block using canonical code saved in `registry/products/events-tp-recording-switcher-t123.html`.
- The `T123` code:
  - reads each existing `.t774__wrapper` lecture card;
  - parses the lecture date from the card text;
  - uses Moscow date boundaries;
  - converts only past cards to `Получить запись`;
  - adds `Запись лекции - 2 000 ₽`;
  - routes the existing card button to `#order:Запись лекции: <title> =2000`;
  - leaves future cards as `Регистрация`;
  - inserts one compact bundle CTA: `Пакет из 5 записей лекций` for `5000 RUB`.

Validation before publication:

- Playwright smoke-check against current live HTML with injected T123 code:
  - total existing `T774` cards: `43`;
  - converted recording buttons: `19`;
  - future registration buttons: `6`;
  - price notes added: `19`;
  - first April and early May cards converted;
  - 18.05.2026 and later checked samples stayed as `Регистрация`.

Published live validation:

- Published `https://moonn.ru/events_tp` from Tilda after removing the duplicate store block.
- Playwright live check after publication:
  - total existing `T774` cards: `43`;
  - converted recording buttons: `19`;
  - future registration buttons: `6`;
  - price notes added: `19`;
  - visible store/catalog duplicate cards: `0`;
  - T123 service text is not visible on the public page;
  - bundle CTA is visible;
  - click on the first converted `Получить запись` button opens cart with product `Запись лекции: "Психология ОТНОШЕНИЙ. ВВЕДЕНИЕ"` and price `2 000р.`.

Residual risks:

- Buyer delivery is still an interim operational process until protected watch pages/Members groups are created.
- The cart form still contains some default English labels such as `Your Name`, `Your Email`, `Your Phone`, `Checkout`; this should be localized in a follow-up Tilda cart settings pass.
- The `#order:` method creates dynamic order items and is suitable for the current fast correction, but the stronger long-term architecture is still manifest -> product/access registry -> protected watch pages -> verified payment receiver.

New rule:

- For existing canonical content pages, do not add a parallel payment catalog until the user explicitly asks for a separate storefront. First try to convert the existing canonical cards and record the transformation code in the repository.

## Sources Checked

- Tilda Members: paid access after payment through cart/payment and "Личный кабинет".
- Tilda payment systems: payment providers are configured in site settings; Tilda supports T-Bank and other providers; test payments are recommended in a controlled amount.
- Tilda catalog import: CSV/YML import is supported; CSV examples use semicolon separators.
- YouTube Help: unlisted videos can be viewed and shared by anyone with the link.

## Next Actions

1. Localize the Tilda cart form labels that still appear in English (`Your Name`, `Your Email`, `Your Phone`, `Checkout`).
2. Create protected watch pages/groups for the five uniquely matched recordings first.
3. Get owner decision for the four ambiguous YouTube matches and the `3334362` recurring series entry.
4. Configure the post-payment delivery path so buyers receive controlled access instead of manual support-only fulfillment.
5. Run one controlled checkout/access test before scaling paid traffic.
6. Replace the interim `#order:` bridge with manifest-driven Tilda products/access groups when protected watch pages are ready.
