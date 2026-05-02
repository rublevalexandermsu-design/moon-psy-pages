# Moonn.ru production 73-page SEO/design status

Date: 2026-05-02
Workstream: Moonn production SEO/design rollout
Branch: `codex/tilda-api-sync`

## Verified Done

- Production scope is fixed at `73` original Tilda pages from `registry/tilda/moonn-production-73-rollout.json`.
- Live availability: `73/73` production URLs return `200 OK`.
- Production design rollout: `73/73` pages include the verified `Radiant Sanctuary` theme marker and pinned CSS.
- Design CSS is pinned to the immutable GitHub/jsDelivr asset:
  `https://cdn.jsdelivr.net/gh/rublevalexandermsu-design/moonn-psy-pages@102fb3d/assets/tilda-radiant-sanctuary.css`.
- SEO/AEO schema manifest is generated for all `73` pages:
  `registry/seo/moonn-production-73-schema-snippets.json`.
- Entity bridge is prepared for:
  - `Татьяна Мунн`;
  - `Татьяна Кумскова`;
  - `Кумскова Татьяна Михайловна`;
  - verified Yandex Services profile:
    `https://uslugi.yandex.ru/profile/TatyanaKumskovatatyanamunn-948629`;
  - MSU affiliation as a general organization reference, without an unverified Istina profile URL.
- Production audit script now tracks:
  - live status;
  - design marker;
  - pinned CSS;
  - schema marker;
  - JSON-LD;
  - bad source links;
  - duplicate metadata;
  - heading issues;
  - image alt issues.

## Current Live Audit

Source: `python scripts/seo_audit_production_73.py`

- Pages in scope: `73`.
- `200 OK`: `73`.
- Errors: `0`.
- Theme missing: `0`.
- Schema missing in live HTML: `73`.
- JSON-LD missing in live HTML: `72`.
- Pages with bad source links: `44`.
- Bad link totals:
  - `http://wa.me/79777770303`: `69`;
  - `http://twa.me/79777770303`: `4`;
  - `http://.moonn.ru`: `26`.
- Heading issue pages: `53`.
- Image alt issue pages: `73`.
- Duplicate title groups: `1`.
- Duplicate description groups: `4`.

## Not Done Yet

These items remain because they require source-level Tilda edits and live HTML confirmation:

1. Fix bad source links in Tilda blocks on `44` pages:
   - `http://wa.me/79777770303` -> `https://wa.me/79777770303`;
   - `http://twa.me/79777770303` -> `https://wa.me/79777770303`;
   - `http://.moonn.ru` -> `https://moonn.ru`.
2. Normalize page headings:
   - exactly one context-specific `h1`;
   - meaningful `h2` structure.
3. Add meaningful image alt text on all pages with missing alt.
4. Resolve duplicate title/description groups with context-specific metadata.
5. Publish page-specific schema.org/JSON-LD only after the Tilda save path is verified by both:
   - Tilda API/export;
   - live `moonn.ru` HTML.

## Incident Rule

Do not mark page-specific SEO/AEO schema as complete based only on copied editor text in Tilda UI.

Completion requires:

1. Tilda editor write succeeds.
2. Tilda API/export contains the same page marker.
3. Live `moonn.ru` HTML contains the same page marker.
4. `scripts/seo_audit_production_73.py` shows the page as not missing schema.

## Recommended Next Work

Start with source-link cleanup because it is the clearest technical SEO defect and affects both users and indexing. Use the existing source-link registry as the queue, then verify every batch through live HTML counters before moving to headings and image alt.
