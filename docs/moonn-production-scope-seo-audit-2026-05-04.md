# Moonn Final SEO Audit — 2026-05-04

Mode: read-only live audit from `output/production-73-rollout-pages.json + output/build-production-83-scope.log`.

## Summary

- Checked URLs: 83
- HTTP 200: 83
- `strengthen_seo`: 77
- `keep_out_of_index_or_remove_from_sitemap`: 1
- `fix_robots_then_strengthen`: 3
- `review_noindex_or_rename_slug`: 2

## Top Issues

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
- `duplicate_title`: 2
- `opaque_or_test_slug`: 2
- `short_title`: 1
- `meta_noindex`: 1
- `missing_description`: 1

## Decision Table

| Decision | URL | Issues |
| --- | --- | --- |
| `review_noindex_or_rename_slug` | `https://moonn.ru/st1` | duplicate_description, images_missing_alt, missing_h1, missing_jsonld, opaque_or_test_slug |
| `review_noindex_or_rename_slug` | `https://moonn.ru/st2` | duplicate_description, images_missing_alt, long_title, missing_h1, missing_jsonld, opaque_or_test_slug |
| `keep_out_of_index_or_remove_from_sitemap` | `https://moonn.ru/psiholog` | images_missing_alt, meta_noindex, missing_h1, missing_jsonld, robots_txt_blocked |
| `strengthen_seo` | `https://moonn.ru/` | images_missing_alt, long_title, missing_jsonld, multiple_h1 |
| `strengthen_seo` | `https://moonn.ru/abuse_gaslight` | images_missing_alt, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/aromatherapy` | images_missing_alt, long_title, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/article_diary_of_emotions` | duplicate_description, images_missing_alt, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/article_femininity` | images_missing_alt, long_title, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/article_gadget_addiction` | images_missing_alt, long_title, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/article_toxic_job` | images_missing_alt, long_title, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/articles/eq-dlya-rukovoditeley` | canonical_mismatch, images_missing_alt, long_title, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/baza-znaniy-emocionalnyy-intellekt-psihologiya` | images_missing_alt, long_description, long_title, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/eintellect` | images_missing_alt, long_title, missing_jsonld, short_description |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/` | canonical_mismatch, images_missing_alt, missing_h1, missing_jsonld, short_title |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/articles` | images_missing_alt, long_title, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/articles/benefits-of-ei` | images_missing_alt, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/articles/emotional-intelligence-skills` | images_missing_alt, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/articles/what-is-emotional-intelligence` | canonical_mismatch, images_missing_alt, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/articles/why-ei-matters` | images_missing_alt, long_title, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/diagnostoka-ei` | images_missing_alt, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/ei-leader-12` | images_missing_alt, long_description, long_title, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base` | images_missing_alt, long_title, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/active-listening` | images_missing_alt, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/burnout` | images_missing_alt, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/emotional-contagion` | images_missing_alt, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/emotional-intelligence` | images_missing_alt, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/emotional-literacy` | images_missing_alt, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/emotional-maturity` | images_missing_alt, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/empathy` | images_missing_alt, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/intrinsic-motivation` | images_missing_alt, long_title, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/male-loneliness-russia` | canonical_mismatch, images_missing_alt, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/nonviolent-communication` | images_missing_alt, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/personal-boundaries` | images_missing_alt, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/psychological-safety` | images_missing_alt, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/self-awareness` | images_missing_alt, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/self-regulation` | images_missing_alt, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/social-intelligence` | images_missing_alt, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/events` | images_missing_alt, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/events_tp` | images_missing_alt, missing_h1, missing_jsonld, short_description |
| `strengthen_seo` | `https://moonn.ru/geshtalt` | images_missing_alt, long_title, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/kpt` | images_missing_alt, long_title, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/kurs-ei` | duplicate_description, duplicate_title, images_missing_alt |
| `strengthen_seo` | `https://moonn.ru/lectures1` | images_missing_alt, long_description, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/microbiom` | images_missing_alt, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/novosti` | canonical_mismatch, images_missing_alt, long_title, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/otzivi` | images_missing_alt, missing_jsonld, multiple_h1 |
| `strengthen_seo` | `https://moonn.ru/panicheskie_ataki` | images_missing_alt, long_description, long_title, missing_jsonld, multiple_h1 |
| `strengthen_seo` | `https://moonn.ru/phytotherapy` | images_missing_alt, missing_h1, missing_jsonld, short_description |
| `strengthen_seo` | `https://moonn.ru/platnye-treningi-seminary-programmy-tatiana-moonn` | images_missing_alt, long_description, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/programmakursa` | duplicate_description, duplicate_title, images_missing_alt, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/psy4psy` | images_missing_alt, long_description, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/psychoanalys` | images_missing_alt, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/psypodgotovka1` | images_missing_alt, long_title, missing_jsonld, multiple_h1 |
| `strengthen_seo` | `https://moonn.ru/recomend` | images_missing_alt, long_title, missing_description, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/salt` | images_missing_alt, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/schematherapy` | images_missing_alt, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/selfharm` | images_missing_alt, long_description, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/semeynie_konflikti_article` | duplicate_description, images_missing_alt, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/semeyniy_psiholog` | images_missing_alt, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/seminar555` | images_missing_alt, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/shppp333` | canonical_mismatch, images_missing_alt, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/speaker` | images_missing_alt, long_description, long_title, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/trauma` | images_missing_alt, long_title, missing_jsonld, short_description |
| `strengthen_seo` | `https://moonn.ru/uslugi_aerofobia` | images_missing_alt, long_title, missing_jsonld, multiple_h1 |
| `strengthen_seo` | `https://moonn.ru/uslugi_depression` | duplicate_description, images_missing_alt, long_title, missing_jsonld, multiple_h1 |
| `strengthen_seo` | `https://moonn.ru/uslugi_fin_blocks` | duplicate_description, images_missing_alt, long_title, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/uslugi_gtr` | duplicate_description, images_missing_alt, long_title, missing_jsonld, multiple_h1 |
| `strengthen_seo` | `https://moonn.ru/uslugi_konflikti_na_rabote` | duplicate_description, images_missing_alt, long_title, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/uslugi_lubovnaya_zavisimost` | duplicate_description, images_missing_alt, long_title, missing_jsonld, multiple_h1 |
| `strengthen_seo` | `https://moonn.ru/uslugi_obida_na_roditelei` | duplicate_description, images_missing_alt, long_title, missing_jsonld, multiple_h1 |
| `strengthen_seo` | `https://moonn.ru/uslugi_otnosheniya_v_kollektive` | duplicate_description, images_missing_alt, long_title, missing_jsonld, multiple_h1 |
| `strengthen_seo` | `https://moonn.ru/uslugi_podrostki` | duplicate_description, images_missing_alt, long_title, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/uslugi_procrastination` | duplicate_description, images_missing_alt, long_title, missing_jsonld, multiple_h1 |
| `strengthen_seo` | `https://moonn.ru/uslugi_razvod` | duplicate_description, images_missing_alt, long_title, missing_jsonld, multiple_h1 |
| `strengthen_seo` | `https://moonn.ru/uslugi_sohranit_brak` | duplicate_description, images_missing_alt, long_title, missing_jsonld, multiple_h1 |
| `strengthen_seo` | `https://moonn.ru/vacuum_cups` | images_missing_alt, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/vigoranie_article` | images_missing_alt, long_title, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/vospitanie_article` | images_missing_alt, missing_h1, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/vystupleniya-lekcii-treningi-psiholog-tatiana-moonn` | images_missing_alt, long_description, missing_jsonld |
| `strengthen_seo` | `https://moonn.ru/water` | images_missing_alt, long_title, missing_jsonld, short_description |
| `fix_robots_then_strengthen` | `https://moonn.ru/psiholog-konsultacii-moskva` | images_missing_alt, missing_jsonld, multiple_h1, robots_txt_blocked |
| `fix_robots_then_strengthen` | `https://moonn.ru/psiholog_moskva` | images_missing_alt, long_title, missing_h1, missing_jsonld, robots_txt_blocked |
| `fix_robots_then_strengthen` | `https://moonn.ru/psihology` | images_missing_alt, missing_h1, missing_jsonld, robots_txt_blocked, short_description |

## Next Action Rules

- `ok_index`: leave indexed, only monitor.
- `strengthen_seo`: improve metadata/H1/schema/image alt, then request reindexing.
- `review_noindex_or_rename_slug`: decide whether the page is real; if real, rename to semantic slug and strengthen SEO; if not, noindex/remove from sitemap.
- `keep_out_of_index_or_remove_from_sitemap`: keep blocked intentionally or remove from sitemap if it should not appear in search tools.
- `fix_http_or_remove_from_sitemap`: fix response or remove from sitemap.
