# Moonn Final SEO Action Plan — 2026-05-04

Source audit: `docs/moonn-final-seo-audit-2026-05-04.json`  
Mode: read-only live audit, no Tilda edits  
Scope: all URLs currently exposed in `https://moonn.ru/sitemap.xml`

## Executive Summary

The sitemap currently exposes `148` URLs, not only the expected 83-page working set. All checked URLs return HTTP `200`, so the main problem is not availability. The main risks are index quality, duplicate/opaque pages and missing machine-readable structure.

Decision groups:

- `strengthen_seo`: 98 URLs
- `review_noindex_or_rename_slug`: 45 URLs
- `keep_out_of_index_or_remove_from_sitemap`: 5 URLs

Top issues:

- `images_missing_alt`: 148
- `missing_jsonld`: 139
- `missing_h1`: 91
- `long_title`: 55
- `duplicate_description`: 52
- `opaque_or_test_slug`: 45
- `short_description`: 18
- `multiple_h1`: 17
- `short_title`: 15
- `long_description`: 13
- `duplicate_title`: 12
- `canonical_mismatch`: 8

## P0: Robots.txt Blocks Important Psychology Pages

`robots.txt` contains `Disallow: /psiholog`, which blocks any path starting with `/psiholog`, including current important pages:

- `https://moonn.ru/psiholog-konsultacii-moskva`
- `https://moonn.ru/psiholog-moskva-online`
- `https://moonn.ru/psiholog-tatiana-moonn`
- `https://moonn.ru/psiholog_moskva`
- `https://moonn.ru/psihology`

Action:

- In Tilda/robots settings, replace broad legacy blocking with exact legacy URLs only.
- Do not block current canonical psychology pages.
- After publishing robots.txt, recheck with `curl -I https://moonn.ru/robots.txt` and GSC/Yandex robots tester.

## P0: 45 Opaque/Test URLs Are In Sitemap

The sitemap includes `page*.html`, `st1`, `st2`, `test77` and similar pages. These should not stay indexable unless each one is a real public page with a semantic URL and unique SEO.

Action:

- For each URL in `review_noindex_or_rename_slug`:
  - if real public page: rename to semantic slug, set unique title/description/H1/canonical/schema;
  - if draft/test/archive: set noindex and remove from sitemap;
  - if replacement exists: create 301 to the canonical page.

## P1: Missing JSON-LD At Scale

`139` URLs have no detected JSON-LD. The 9 priority pages already have prepared JSON-LD packets in:

- `docs/moonn-tilda-jsonld-blocks-2026-05-04.json`

Action:

- Apply prepared JSON-LD to the 9 priority pages first through supported Tilda head/code fields.
- Generate JSON-LD for the remaining indexable pages only after the page is classified as worth indexing.
- Do not add `Review` or `AggregateRating` until the Yandex Services reviews gate is approved.

## P1: H1 Structure Is Weak

`91` URLs have no detected H1. `17` URLs have multiple H1.

Action:

- Every indexable page should have exactly one visible H1.
- Repeated block titles should be H2/H3.
- Do not spend time fixing H1 on pages that will be noindexed or removed.

## P1: Duplicate/Weak Metadata

The audit found duplicate titles/descriptions and overlong/short metadata.

Examples:

- `https://moonn.ru/novosti` and `https://moonn.ru/20251201` point to the same Tashkent trip theme and canonical cluster.
- Several course/page URLs reuse `Татьяна Мунн - психолог МГУ в Москве | Быстрая психология | Консультации`.
- `https://moonn.ru/events_tp` has a short generic description.

Action:

- Fix duplicates by cluster, not page by page blindly.
- Use canonical pages for real clusters.
- Noindex or redirect duplicates that do not carry unique search intent.

## P1: Canonical Mismatches

`8` URLs have canonical mismatch. Some canonicals are missing protocol, point to old URLs or point to another page.

Action:

- Decide intentionally:
  - if duplicate: keep canonical to target and remove duplicate from sitemap;
  - if unique: set self-canonical with full `https://moonn.ru/...` URL.

## P2: Image ALT

All audited pages contain at least one image without alt. In Tilda this can be partly caused by generated/lazy/service images, but content images and covers still need SEO alt.

Action:

- Prioritize hero/cover images and article images first.
- Use short visible captions and full context in `alt`, `og:image`, image sitemap where available.
- Full source file replacement in Tilda should only be done through supported visual/safe path.

## Execution Order

1. Fix `robots.txt` broad `/psiholog` block.
2. Classify 45 opaque/test URLs: indexable semantic page, noindex/remove, or 301.
3. Apply prepared SEO/JSON-LD to the 9 priority pages.
4. Fix title/description/H1 for indexable pages by cluster.
5. Fix canonical mismatches.
6. Add image alt to priority content images.
7. Re-run `scripts/moonn_final_seo_audit.py`.
8. Submit updated URLs/sitemap to GSC and Yandex Webmaster.

## Files Produced

- `scripts/moonn_final_seo_audit.py`
- `docs/moonn-final-seo-audit-2026-05-04.json`
- `docs/moonn-final-seo-audit-2026-05-04.md`
- `docs/moonn-final-seo-audit-2026-05-04.csv`
- `docs/moonn-final-seo-action-plan-2026-05-04.md`
