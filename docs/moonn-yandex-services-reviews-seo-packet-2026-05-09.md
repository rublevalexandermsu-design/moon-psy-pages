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

Before reporting completion on live site:

1. Commit and push the prepared Git artifacts.
2. Replace `REPLACE_WITH_COMMIT_SHA` in the global HEAD packet with the pushed commit hash.
3. Apply the updated global HEAD in Tilda project `8326812`.
4. Publish only the required scope; do not use publish-all unless explicitly approved.
5. Verify:
   - raw `https://moonn.ru/otzivi` returns `200`;
   - rendered page includes `moonn-yandex-reviews-quality-layer`;
   - rendered page does not show `дублирую информацию` or `поиска информации в интернете`;
   - rendered JSON-LD includes `ProfilePage` and `verified-yandex-review-summaries`;
   - Yandex Services profile link opens `TatyanaKumskovamunn-948629`.

## Follow-up Rule

For future review-source pages, avoid public wording that explains internal SEO mechanics. Use user-facing trust language, source links, provenance records, and structured data instead.
