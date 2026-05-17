# Moonn Paid Video Lectures Tilda Plan

Date: 2026-05-03
Workstream: Moonn paid video lectures
Branch: `codex/moonn-paid-video-lectures`

## 5-Point Strategic Check

1. Platform value: high. Paid recordings turn existing lectures/events into reusable products.
2. Obsolescence risk: medium. A one-off Tilda edit will break as soon as prices, videos, or access rules change.
3. Stronger architecture: use a canonical product/access manifest, then configure Tilda pages from that manifest.
4. Reuse: high. The same model can support paid lectures, courses, master classes, bundles, QR pages, and Timepad follow-up offers.
5. 3-12 month risk if done only manually: mismatched prices, orphaned YouTube links, broken buttons, support requests after payment, and no clear audit of who bought what.

## Verified Inputs

- Read-only Tilda API audit found 39 published page candidates with lecture/course/video/payment signals.
- Strongest candidates:
  - `https://moonn.ru/events_tp`, Tilda page `66814657`: user-confirmed canonical lecture page; audit found 10 unique Timepad event URLs plus the Timepad loader.
  - `https://moonn.ru/lectures1`, Tilda page `68295899`: secondary lecture page, not the current paid-lecture pilot.
  - `https://moonn.ru/events`, Tilda page `53668815`: public events page.
  - `https://moonn.ru/psypodgotovka1`, Tilda page `62652841`: already contains "purchase recording" signals.
  - `https://moonn.ru/seminar555`, Tilda page `57927493`: contains YouTube links and paid/seminar signals.
- Default requested price: `1300 RUB` per lecture.

## Tilda Architecture

Recommended model:

1. Product/storefront page:
   - Use `events_tp` as the first pilot storefront.
   - Each lecture card becomes a Tilda product with price `1300`.
   - Button text changes from `Записаться` / `Зарегистрироваться` to `Купить запись` or `Приобрести лекцию`.

2. Payment:
   - Use Tilda cart/payment stack already configured in the project.
   - Tilda read-only API exposes the `userpayment` field but did not expose an active provider value in the current API response.
   - Current assumption from the user: T-Bank/Tinkoff for IP Kumskova.
   - For live rollout, visually verify which payment provider is active and whether test payments are possible.
   - Do not change production payment settings blindly.

3. Access after payment:
   - Use Tilda Members / Courses access groups.
   - Buyer is added to the correct group only after successful payment.
   - Each lecture can map to either one group per lecture or one group for the full recordings library.

4. Video viewing:
   - Create protected watch pages inside Tilda Members/Courses.
   - Place the video only on protected watch pages, not on the public sales page.
   - If videos stay on YouTube, unlisted links are not strong copy protection. Treat them as convenience, not real DRM.
   - Stronger option: use a host that supports domain restrictions, signed/private embeds, or platform-level access controls.

5. QR layer:
   - Generate QR to the canonical storefront URL, not to raw videos.
   - Put the QR image and plain URL on the storefront page.
   - Keep QR file name SEO-safe, e.g. `tatyana-munn-paid-lectures-qr.png`.

## Product Manifest

Canonical files created:

- `registry/products/paid-video-lectures.schema.json`
- `registry/products/paid-video-lectures.manifest.json`
- `registry/products/paid-video-lectures-audit-2026-05-03.json`
- `assets/qr/tatyana-munn-paid-lectures-events-tp-qr.png`

These files separate public page text from machine data:

- lecture title;
- source page;
- price;
- Timepad source if any;
- video URL;
- Tilda product SKU;
- Members group;
- protected watch page;
- QR target;
- current status and required user input.

## Safe Rollout Plan

1. Pilot one lecture in staging:
   - choose one lecture card on `events_tp`;
   - create a test product at `1300 RUB`;
   - create one protected watch page/group;
   - connect payment and post-payment group access;
   - test payment flow in safe/test mode or with an agreed live test payment;
   - verify buyer sees the video only after payment.

2. Scale to all selected lectures:
   - fill manifest with final video URLs;
   - create products/groups/pages in batches;
   - update buttons;
   - publish staging;
   - run visual and purchase-flow QA.

3. Production rollout:
   - only after staging proof;
   - preserve existing SEO/title/schema;
   - update `Product`, `VideoObject`, and `Course` schema;
   - request indexing after the page stabilizes.

## High-Risk Gates

Do not proceed to production until these are confirmed:

- payment provider in Tilda is active and legal for this seller;
- checkout shows correct seller/payment information;
- refund/offer/privacy documents are present and linked;
- video access after payment was tested;
- raw YouTube/private video links are not exposed on the public sales page;
- user approved live publication and live payment path.

## `events_tp` Lecture Candidates

The manifest now contains 10 lecture candidates extracted from the live `events_tp` Timepad links:

- `3334362` — БЕСПЛАТНЫЕ лекции по ПСИХОЛОГИИ.
- `3796319` — ДУХОВНАЯ Психология.
- `3796462` — Психология ЛЮБВИ к СЕБЕ.
- `3796469` — Психология ГОЛОДА.
- `3796473` — Психология МУЖЧИНЫ.
- `3808776` — Психология Искусственного и Эмоционального ИНТЕЛЛЕКТА.
- `3808782` — Психология ЖЕНЩИНЫ.
- `3808783` — ЦИФРОВАЯ Психология.
- `3808788` — БЫСТРАЯ Психология.
- `3808803` — Психология ЗНАКОМСТВА.

Each candidate has a planned:

- SKU: `moonn-video-lecture-{timepad_event_id}`;
- Members group: `moonn-video-lecture-{timepad_event_id}`;
- price: `1300 RUB`;
- QR target: `https://moonn.ru/events_tp`;
- status: `needs_video`.

## Test Scenario Approved By User

User approved one test scenario. Safe interpretation:

- one selected `events_tp` lecture only;
- staging or Tilda-safe test mode first;
- if only a live payment is available, run one explicit low-blast-radius test purchase after visual confirmation of seller/payment details;
- do not create a new live T-Bank/Tinkoff integration unless existing provider is absent and legal/payment requisites are confirmed.

## User Input Needed

- Video URL for each lecture.
- If videos are private/hidden in YouTube Studio, provide browser login access to the channel owner account or export the video list with title, video id, visibility and URL.
- Decision: one purchase per lecture or bundle/library access.
- Visual confirmation of current Tilda payment provider, because read-only API did not expose active payment details.
- Confirmation whether the group lecture `3334362` should be sold as a recording or treated only as an archive/series entry.

## YouTube Matching Gate

The YouTube channel is `https://www.youtube.com/@moonn_tatiana`, but the relevant recordings are private/hidden. Public channel scanning is not enough to match videos reliably.

Safe matching process:

1. Open YouTube Studio through the already logged-in Chrome profile or have the owner log in visually.
2. Export or inspect the private video list.
3. Match by lecture title and date against `registry/products/paid-video-lectures-youtube-map.template.csv`.
4. Store only video id / Studio URL / visibility in the internal manifest. Do not expose raw private links on public pages.
5. After Tilda protected access exists, embed the selected video only inside the protected watch page/course lesson.

Required matching fields:

- `lecture_id`;
- `timepad_event_id`;
- `lecture_title`;
- `youtube_candidate_title`;
- `youtube_studio_url_or_video_id`;
- `youtube_visibility`;
- `match_confidence`;
- `approved_for_paid_access`.

## YouTube Studio Matching Result

YouTube Studio owner view was used to inspect the private channel content without committing private video ids or Studio URLs.

Safe results:

- Five `events_tp` lectures have unique private recording matches and can move to protected Tilda product/watch-page setup after payment-provider verification.
- Four `events_tp` lectures have multiple plausible recording candidates and need owner selection before paid setup.
- The recurring Timepad event `3334362` is not a single sellable recording yet.

Committed artifact:

- `registry/products/paid-video-lectures-youtube-match-status-2026-05-03.json`

Local-only artifact:

- `output/youtube-private-map/private-youtube-video-map.local.json`

Do not expose private YouTube links on public Tilda pages. The public sales page should link only to the Tilda checkout/product flow; the selected video belongs inside a protected Members/Courses watch page after successful payment.

## Official Tilda References Checked

- Tilda customer accounts for online store: `https://help-ru.tilda.cc/online-store/customer-accounts`
- Tilda Members access after payment: `https://help-ru.tilda.cc/membership`
- Tilda courses and paid course access: `https://help-ru.tilda.cc/courses`

## 2026-05-17 Price And Bundle Update

User updated the commercial model:

- single lecture recording: `2000 RUB`;
- package: `5000 RUB` for five lecture recordings on choice;
- public button: `Получить запись`;
- bundle button: `Выбрать пакет`;
- support contact should include Tatyana Munn's Telegram and/or WhatsApp after payment.

Applied registry changes:

- `registry/products/paid-video-lectures.manifest.json` now stores `default_price_rub: 2000`, `bundle_price_rub: 5000`, and `bundle_selection_count: 5`.
- `registry/products/paid-video-lectures.schema.json` now supports bundle and support fields.
- `scripts/prepare_paid_video_lecture_products.py` regenerates the manifest price contract and Tilda import CSV.
- `registry/products/paid-video-lectures-tilda-catalog-2026-05-17.csv` contains 10 single lecture products plus the five-recording bundle product.
- `docs/paid-video-lectures-checkout-2026-05-17.md` records the checkout/access implementation packet.

Important constraint:

- Do not send raw YouTube links as the fulfillment mechanism. YouTube unlisted links can be shared by anyone with the link; use Tilda Members/Courses protected pages for the viewer experience.
