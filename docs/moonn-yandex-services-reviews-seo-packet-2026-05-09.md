# Moonn Yandex Services Reviews SEO Packet — 2026-05-09

## Scope

- Project: Moonn / Tatyana Munn site.
- Workstream: Yandex Services entity linking and reviews page quality.
- Branch: `codex/moonn-seo-audit`.
- Canonical live page: `https://moonn.ru/otzivi`.
- Tilda page: `81167556`.
- Verified Yandex Services profile: `https://uslugi.yandex.ru/profile/TatyanaKumskovamunn-948629`.

## Verified Facts

- `https://moonn.ru/otzivi` returned `200` on 2026-05-09.
- The page already exists and already contains client reviews with links to Yandex Services.
- The page currently includes `moonn-semantic-heading-layer` and `moonn-schema-layer`.
- Live HEAD currently pins `moonn-schema-layer.js` to commit `0e5967eaa5d2fcca54900772ff632f91f090f073`.
- The public page still contains weak internal SEO wording:
  - `дублирую информацию`
  - `поиска информации в интернете`
- Yandex profile URL used by the live page redirects to / resolves as `TatyanaKumskovamunn-948629`; local structured data previously used an older `TatyanaKumskovatatyanamunn-948629` variant.

## Decision

Do not create a second reviews page and do not mirror the Yandex Services page one-to-one.

The stronger route is to keep `/otzivi` as the canonical reviews page and improve it as a verified source page:

- visible editorial text should say that reviews are published with source links;
- each source route should point to the real Yandex Services profile;
- structured data should connect `Person`, `WebPage`, Yandex `ProfilePage`, and review-summary `ItemList`;
- no synthetic aggregate ratings, fake review counts, or unsupported medical guarantees.

## Local Changes Prepared

- Updated Yandex Services profile URL in:
  - `data/site.json`
  - `scripts/build_moonn_schema_layer.py`
  - `docs/moonn-global-head-code-with-schema-2026-05-08.html`
- Rebuilt schema artifacts:
  - `assets/moonn-schema-layer.js`
  - `docs/moonn-schema-layer-packet-2026-05-08.json`
  - `docs/moonn-schema-layer-packet-2026-05-08.md`
- Added rendered-page quality patch:
  - `assets/moonn-yandex-reviews-quality-layer.js`

## Safety Notes

- Review text should not be copied as a full external page mirror.
- Review schema is intentionally source-summary based and does not publish fake `aggregateRating`.
- The live native Tilda block still needs a source edit to remove internal SEO wording from raw HTML. The JS quality layer improves rendered output, but raw HTML cleanup remains the stronger final state.

## Live Apply Gate

Status: completed for the rendered page and structured data on 2026-05-09.

- Git commit applied in Tilda page-specific HEAD:
  - `b9930a83da11cdbfaeae98a9f92309fe1d2d4464`
- Tilda page-specific HEAD saved through Ace editor + textarea model.
- Tilda page `81167556` was published.
- Live raw check:
  - `https://moonn.ru/otzivi` returns `200`.
  - `moonn-yandex-reviews-quality-layer` is present.
  - pinned commit `b9930a83da11cdbfaeae98a9f92309fe1d2d4464` is present.
  - typo commit `ba39941e95b8a623a7566ba58d281d34e8a16a13` is absent.
- Rendered browser check:
  - `script#moonn-page-schema-jsonld` has `data-moonn-schema-path="/otzivi"`.
  - JSON-LD includes `ProfilePage` and `ItemList`.
  - JSON-LD includes `https://moonn.ru/otzivi#yandex-services-profile`.
  - JSON-LD includes `https://moonn.ru/otzivi#verified-yandex-review-summaries`.
  - rendered page includes the source panel `Проверяемые отзывы с Яндекс Услуг`.
  - rendered page does not show `дублирую информацию` or `поиска информации в интернете`.

Remaining stronger-state cleanup:

- Raw Tilda HTML still contains the old weak phrases and the older profile URL variant. The runtime layer removes these from the rendered page, but native Tilda block editing remains the stronger SEO/compliance follow-up.

## Follow-up Rule

For future review-source pages, avoid public wording that explains internal SEO mechanics. Use user-facing trust language, source links, provenance records, and structured data instead.

## 2026-05-10 Archive Layer Update

Status: completed for the rendered page.

- Git commit applied in Tilda page-specific HEAD:
  - `9df3edab278d5c27dbc98e2216de692ae247da6f`
- Added runtime layer:
  - `assets/moonn-yandex-all-reviews-layer.js`
- Updated runtime layer:
  - `assets/moonn-yandex-reviews-quality-layer.js`
- Tilda page `81167556` was published only for `/otzivi`.

Live checks:

- Raw live HTML contains `moonn-yandex-reviews-quality-layer`.
- Raw live HTML contains `moonn-yandex-all-reviews-layer`.
- Raw live HTML contains commit `9df3edab278d5c27dbc98e2216de692ae247da6f`.
- Rendered browser check found `123` review summary cards.
- Rendered browser check found 2026 review dates, including `15.04.2026`, `05.04.2026`, and `28.02.2026`.
- Rendered browser check found the Yandex Services source badge and `актуальные отзывы 2026`.
- Rendered browser check confirmed the old dark hero block is hidden.

Publication posture:

- Full verbatim Yandex review text is still behind the legal/platform/personal-data gate.
- Current public page uses source-linked summary cards, not a full text mirror of Yandex Services.
