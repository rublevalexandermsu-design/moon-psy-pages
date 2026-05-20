# Moonn Final SEO Audit — 2026-05-20

Mode: read-only live audit from `output/production-73-rollout-pages.json + output/build-production-83-scope.log`.

## Summary

- Checked URLs: 83
- HTTP 200: 83
- `strengthen_seo`: 69
- `keep_out_of_index_or_remove_from_sitemap`: 9
- `fix_robots_then_strengthen`: 3
- `review_noindex_or_rename_slug`: 2

## Top Issues

- `images_missing_alt`: 83
- `missing_h1`: 43
- `multiple_h1`: 13
- `robots_txt_blocked`: 12
- `meta_noindex`: 9
- `long_title`: 5
- `short_description`: 2
- `duplicate_description`: 2
- `opaque_or_test_slug`: 2

## Decision Table

| Decision | URL | Issues |
| --- | --- | --- |
| `review_noindex_or_rename_slug` | `https://moonn.ru/st1` | duplicate_description, images_missing_alt, missing_h1, opaque_or_test_slug |
| `review_noindex_or_rename_slug` | `https://moonn.ru/st2` | duplicate_description, images_missing_alt, long_title, missing_h1, opaque_or_test_slug |
| `keep_out_of_index_or_remove_from_sitemap` | `https://moonn.ru/aromatherapy` | images_missing_alt, long_title, meta_noindex, robots_txt_blocked |
| `keep_out_of_index_or_remove_from_sitemap` | `https://moonn.ru/geshtalt` | images_missing_alt, long_title, meta_noindex, robots_txt_blocked |
| `keep_out_of_index_or_remove_from_sitemap` | `https://moonn.ru/kpt` | images_missing_alt, long_title, meta_noindex, robots_txt_blocked |
| `keep_out_of_index_or_remove_from_sitemap` | `https://moonn.ru/microbiom` | images_missing_alt, meta_noindex, missing_h1, robots_txt_blocked |
| `keep_out_of_index_or_remove_from_sitemap` | `https://moonn.ru/phytotherapy` | images_missing_alt, meta_noindex, missing_h1, robots_txt_blocked, short_description |
| `keep_out_of_index_or_remove_from_sitemap` | `https://moonn.ru/psychoanalys` | images_missing_alt, meta_noindex, robots_txt_blocked |
| `keep_out_of_index_or_remove_from_sitemap` | `https://moonn.ru/salt` | images_missing_alt, meta_noindex, missing_h1, robots_txt_blocked |
| `keep_out_of_index_or_remove_from_sitemap` | `https://moonn.ru/vacuum_cups` | images_missing_alt, meta_noindex, missing_h1, robots_txt_blocked |
| `keep_out_of_index_or_remove_from_sitemap` | `https://moonn.ru/water` | images_missing_alt, long_title, meta_noindex, robots_txt_blocked, short_description |
| `strengthen_seo` | `https://moonn.ru/` | images_missing_alt, multiple_h1 |
| `strengthen_seo` | `https://moonn.ru/abuse_gaslight` | images_missing_alt |
| `strengthen_seo` | `https://moonn.ru/article_diary_of_emotions` | images_missing_alt |
| `strengthen_seo` | `https://moonn.ru/article_femininity` | images_missing_alt |
| `strengthen_seo` | `https://moonn.ru/article_gadget_addiction` | images_missing_alt |
| `strengthen_seo` | `https://moonn.ru/article_toxic_job` | images_missing_alt |
| `strengthen_seo` | `https://moonn.ru/articles/eq-dlya-rukovoditeley` | images_missing_alt |
| `strengthen_seo` | `https://moonn.ru/baza-znaniy-emocionalnyy-intellekt-psihologiya` | images_missing_alt |
| `strengthen_seo` | `https://moonn.ru/eintellect` | images_missing_alt |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/articles` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/articles/benefits-of-ei` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/articles/emotional-intelligence-skills` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/articles/what-is-emotional-intelligence` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/articles/why-ei-matters` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/diagnostoka-ei` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/ei-leader-12` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/active-listening` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/burnout` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/emotional-contagion` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/emotional-intelligence` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/emotional-literacy` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/emotional-maturity` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/empathy` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/intrinsic-motivation` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/male-loneliness-russia` | images_missing_alt |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/nonviolent-communication` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/personal-boundaries` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/psychological-safety` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/self-awareness` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/self-regulation` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/emotional-intelligence/knowledge-base/social-intelligence` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/events` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/events_tp` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/kurs-ei` | images_missing_alt |
| `strengthen_seo` | `https://moonn.ru/lectures1` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/novosti` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/otzivi` | images_missing_alt, multiple_h1 |
| `strengthen_seo` | `https://moonn.ru/panicheskie_ataki` | images_missing_alt, multiple_h1 |
| `strengthen_seo` | `https://moonn.ru/platnye-treningi-seminary-programmy-tatiana-moonn` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/programmakursa` | images_missing_alt |
| `strengthen_seo` | `https://moonn.ru/psiholog` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/psiholog-konsultacii-moskva` | images_missing_alt, multiple_h1 |
| `strengthen_seo` | `https://moonn.ru/psiholog_moskva` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/psihology` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/psypodgotovka1` | images_missing_alt |
| `strengthen_seo` | `https://moonn.ru/recomend` | images_missing_alt |
| `strengthen_seo` | `https://moonn.ru/semeynie_konflikti_article` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/semeyniy_psiholog` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/seminar555` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/shppp333` | images_missing_alt |
| `strengthen_seo` | `https://moonn.ru/speaker` | images_missing_alt |
| `strengthen_seo` | `https://moonn.ru/trauma` | images_missing_alt |
| `strengthen_seo` | `https://moonn.ru/uslugi_aerofobia` | images_missing_alt, multiple_h1 |
| `strengthen_seo` | `https://moonn.ru/uslugi_depression` | images_missing_alt, multiple_h1 |
| `strengthen_seo` | `https://moonn.ru/uslugi_fin_blocks` | images_missing_alt |
| `strengthen_seo` | `https://moonn.ru/uslugi_gtr` | images_missing_alt, multiple_h1 |
| `strengthen_seo` | `https://moonn.ru/uslugi_konflikti_na_rabote` | images_missing_alt |
| `strengthen_seo` | `https://moonn.ru/uslugi_lubovnaya_zavisimost` | images_missing_alt, multiple_h1 |
| `strengthen_seo` | `https://moonn.ru/uslugi_obida_na_roditelei` | images_missing_alt, multiple_h1 |
| `strengthen_seo` | `https://moonn.ru/uslugi_otnosheniya_v_kollektive` | images_missing_alt, multiple_h1 |
| `strengthen_seo` | `https://moonn.ru/uslugi_podrostki` | images_missing_alt |
| `strengthen_seo` | `https://moonn.ru/uslugi_procrastination` | images_missing_alt, multiple_h1 |
| `strengthen_seo` | `https://moonn.ru/uslugi_razvod` | images_missing_alt, multiple_h1 |
| `strengthen_seo` | `https://moonn.ru/uslugi_sohranit_brak` | images_missing_alt, multiple_h1 |
| `strengthen_seo` | `https://moonn.ru/vigoranie_article` | images_missing_alt |
| `strengthen_seo` | `https://moonn.ru/vospitanie_article` | images_missing_alt, missing_h1 |
| `strengthen_seo` | `https://moonn.ru/vystupleniya-lekcii-treningi-psiholog-tatiana-moonn` | images_missing_alt |
| `fix_robots_then_strengthen` | `https://moonn.ru/psy4psy` | images_missing_alt, robots_txt_blocked |
| `fix_robots_then_strengthen` | `https://moonn.ru/schematherapy` | images_missing_alt, missing_h1, robots_txt_blocked |
| `fix_robots_then_strengthen` | `https://moonn.ru/selfharm` | images_missing_alt, missing_h1, robots_txt_blocked |

## Next Action Rules

- `ok_index`: leave indexed, only monitor.
- `strengthen_seo`: improve metadata/H1/schema/image alt, then request reindexing.
- `review_noindex_or_rename_slug`: decide whether the page is real; if real, rename to semantic slug and strengthen SEO; if not, noindex/remove from sitemap.
- `keep_out_of_index_or_remove_from_sitemap`: keep blocked intentionally or remove from sitemap if it should not appear in search tools.
- `fix_http_or_remove_from_sitemap`: fix response or remove from sitemap.
