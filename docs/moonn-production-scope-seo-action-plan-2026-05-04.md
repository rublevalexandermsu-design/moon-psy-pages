# Moonn Production Scope SEO Action Plan — 2026-05-04

Source audit: `docs/moonn-production-scope-seo-audit-2026-05-04.json`  
Scope source: `output/production-73-rollout-pages.json` + `output/build-production-83-scope.log`  
Mode: read-only live audit of the actual production pages we worked with earlier.

## Correction

The previous full-sitemap audit remains useful for sitemap hygiene, but it was too broad for the user's request because it included all `148` URLs exposed by Tilda sitemap. The correct working scope is the saved production rollout set:

- 73 original copied/rolled-out pages;
- 10 production alias additions;
- total: `83` real production URLs.

## Summary

- Checked URLs: `83`
- HTTP 200: `83`
- `strengthen_seo`: `77`
- `fix_robots_then_strengthen`: `3`
- `review_noindex_or_rename_slug`: `2`
- `keep_out_of_index_or_remove_from_sitemap`: `1`

Top issues:

- `images_missing_alt`: 83
- `missing_jsonld`: 82
- `missing_h1`: 44
- `long_title`: 37
- `duplicate_description`: 17
- `multiple_h1`: 14
- `long_description`: 9
- `canonical_mismatch`: 6
- `short_description`: 6
- `robots_txt_blocked`: 4

## P0: Fix Robots For Real Working Pages

These are real working pages but are blocked by broad `robots.txt` prefix rules:

- `https://moonn.ru/psiholog-konsultacii-moskva`
- `https://moonn.ru/psiholog_moskva`
- `https://moonn.ru/psihology`

Action:

- Replace broad `Disallow: /psiholog` behavior with exact blocking for old/closed pages only.
- Keep `https://moonn.ru/psiholog` out of index if it is still a legacy/noindex page.
- Recheck robots after Tilda publish.

## P0: Review `st1` And `st2`

These are real live pages from the production scope, but their slugs are not semantic:

- `https://moonn.ru/st1`
- `https://moonn.ru/st2`

Action:

- If these are active public pages: rename to semantic slugs and set unique title/description/H1/schema.
- If these are legacy/test pages: set noindex and remove from sitemap or redirect to the canonical training/course page.

## P1: Apply SEO/AEO To 77 Strengthen Pages

Most pages should stay live but need strengthening:

- unique title/description;
- exactly one H1;
- page-specific JSON-LD;
- fixed canonical where mismatch exists;
- alt text for content images.

Start with these clusters:

1. Consultation/service pages.
2. Lecture/events/product pages.
3. Emotional-intelligence knowledge base.
4. Articles.
5. Legacy helpful pages that are still intentionally public.

## P1: Canonical Mismatches

Six scoped pages need canonical decisions:

- `https://moonn.ru/articles/eq-dlya-rukoviteley` equivalent in report: `https://moonn.ru/articles/eq-dlya-rukovoditeley`
- `https://moonn.ru/emotional-intelligence/`
- `https://moonn.ru/emotional-intelligence/articles/what-is-emotional-intelligence`
- `https://moonn.ru/emotional-intelligence/knowledge-base/male-loneliness-russia`
- `https://moonn.ru/novosti`
- `https://moonn.ru/shppp333`

Action:

- If unique page: set full self-canonical with `https://`.
- If duplicate: remove duplicate from sitemap or redirect/canonical intentionally.

## P1: JSON-LD

`82` of `83` scoped pages have no detected JSON-LD. The first priority is to apply already prepared JSON-LD patterns to the 9 priority pages, then generate cluster-based JSON-LD for the rest.

No `Review` or `AggregateRating` until the Yandex Services review gate is approved.

## P2: Images

All scoped pages contain images without alt. This likely includes Tilda/service images, but content/hero images still need SEO alt.

Action:

- First fix hero and article images.
- Avoid trying to replace every generated Tilda image blindly.
- Full file replacement remains a visual/supported Tilda workflow.

## Next Execution Order

1. Fix robots for real `/psiholog...` pages.
2. Decide `st1`/`st2`: semantic rename or noindex/redirect.
3. Apply prepared SEO/JSON-LD/H1 changes to the 9 priority pages.
4. Generate cluster-level SEO patch packets for the remaining 74 scoped pages.
5. Fix canonical mismatches.
6. Add alt to priority images.
7. Re-run `python scripts/moonn_final_seo_audit.py --production-scope`.
