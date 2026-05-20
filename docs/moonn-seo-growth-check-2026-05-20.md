# Moonn SEO Growth Check — 2026-05-20

## Scope

- Project: Moonn / Tatyana Munn site.
- Branch: `codex/moonn-seo-audit`.
- Mode: manual immediate run of the `moonn-seo-privacy-supervisor` checklist.
- Period under review: roughly three weeks after the May 2026 SEO rollout, with the main reindexing packet submitted on 2026-05-08.

## Strategic Read

- Platform value: high. This check is the feedback loop for whether the SEO/AEO work created measurable traffic, not only technical artifacts.
- Staleness risk: high if analytics access remains manual or unavailable. Without Yandex.Metrika/GSC exports, the automation can only verify site readiness, not business effect.
- Stronger architecture: connect Yandex.Metrika, Yandex Webmaster and Google Search Console through official API/export artifacts and write each run to a dated report.
- Reuse: high. The same pattern should become the analytics supervisor for Timepad, MIIIIPS, course pages and future landing experiments.
- 3-12 month risk if unchanged: the team will keep doing SEO by effort, not by measured visits, search queries, click paths and conversion goals.

## Verified Technical Facts

- `83/83` Moonn production-scope URLs return HTTP `200`.
- Rendered H1 layer is live on `83/83` pages.
- Rendered H1 result: `83/83` pages have exactly one H1; `0` missing H1; `0` multiple H1.
- Rendered H1 target checks: `50/52` matched; `2` H2 target checks failed on `https://moonn.ru/psypodgotovka1`.
- Rendered schema layer is live on `83/83` pages.
- Rendered schema result: `83/83` pages have JSON-LD, `Person`, `WebSite`, `WebPage`, `BreadcrumbList`; `0` JSON errors.
- Raw HTML SEO audit still flags source-level issues: `images_missing_alt: 83`, `missing_h1: 43`, `multiple_h1: 13`, `robots_txt_blocked: 12`, `meta_noindex: 9`.
- Compared with 2026-05-08 raw audit:
  - duplicate descriptions improved from `4` to `2`;
  - duplicate titles improved from `2` to `0`;
  - canonical mismatch improved from `1` to `0`;
  - multiple H1 raw signal improved from `14` to `13`;
  - the 2026-05-20 audit now separates `9` intentionally out-of-index pages and `3` robots-blocked pages that need decision/action.

## Analytics Access Result

- API access is still blocked:
  - Yandex.Metrika API for counter `96397286` returned `403 access_denied`.
  - Yandex Webmaster API returned `403 INVALID_OAUTH_TOKEN`.
  - Google Search Console API returned `401 Login Required`.
- GUI access through Google Chrome Rublev profile was available and used for a bounded manual verification.
- Source screenshots were kept as local working evidence and intentionally not committed, because they include analytics cabinet/account UI.

## GUI-Verified Business Metrics

### SEO Rollout Dates And Baseline

The rollout was not a single moment; it happened in phases:

- `2026-05-01`: pre-rollout analytics baseline was recorded. Canonical Metrika counter `96397286` showed `1` visit / `1` view / `1` visitor for `2026-04-25 - 2026-05-01`. GSC last 3 months showed `221` clicks, `12.4K` impressions, CTR `1.8%`, average position `6.9`.
- `2026-05-03`: live Moonn SEO metadata audit and Tilda SEO patch packets were prepared.
- `2026-05-04`: production SEO settings were applied through Tilda UI to `77` ready pages plus `3` formerly robots-blocked production pages; final `80/80` matched title, description and canonical packets.
- `2026-05-06 - 2026-05-07`: H1/H2 cleanup and scoped publishing follow-up were performed.
- `2026-05-08`: JSON-LD schema layer and reindex submission packet were recorded for Google Search Console and Yandex.

Important measurement caveat: the project history also records that before the final May 7-8 publication work, the live global HEAD still had a broken Yandex.Metrika JavaScript snippet. Therefore the Metrika before/after jump is a combined signal: increased traffic plus corrected measurement. Google Search Console is the cleaner source for SEO visibility because it measures search impressions/clicks outside the site script.

### Yandex.Metrika

Period: `21 Apr 2026 - 20 May 2026`.

- Traffic report: `316` visits.
- Sources report: `313` visits, `265` visitors, bounce rate `34.50%`, depth `2.87`.
- Traffic sources:
  - Direct visits: `205` visits / `182` visitors / `65.50%` of visits / bounce `46.83%` / depth `3.58`.
  - Search engines: `81` visits / `63` visitors / `25.88%` of visits / bounce `12.35%` / depth `1.47`.
  - Referral links: `24` visits / `20` visitors / `7.67%` of visits / bounce `4.17%` / depth `1.71`.
  - Social networks: `2` visits / `2` visitors.
  - Internal transitions: `1` visit.
- Search phrases report: `38` visits / `33` visitors / bounce `7.89%` / depth `1.55`.
- Visible Yandex search phrases include:
  - `татьяна мунн`
  - `татьяна мунн крутой психолог на чем ...`
  - `татьяна мунн сколько стоит`
  - `татьяна муун`
  - `татьянка мунн лекции`
  - `телесная терапия подростки лагерь г...`
  - `что такое самоосознанность`
  - `подростковый психологический инт...`
- Popular content report: `901` views / `268` visitors, but the table collapses all visible page data to `https://moonn.ru/`.

Before/after Metrika check:

- Before core SEO application, `2026-04-20 - 2026-05-03`: traffic report showed `4` visits; sources report showed `1` attributed visit.
- After core SEO/schema/reindex work, `2026-05-07 - 2026-05-20`: traffic report showed `312` visits; sources report showed `312` visits / `264` visitors.
- After-window sources: direct `204`, search engines `81`, referral links `24`, social networks `2`, internal `1`.
- Therefore the earlier `316` figure is not nine months. It is the Metrika `month` preset visible as `21 Apr - 20 May`; almost all tracked visits in that month came in the last two weeks (`312` visits on `7 May - 20 May`).

### Google Search Console

Property: `https://moonn.ru/`.

Last visible update: about `3.5` hours before the check.

- Last `3 months`: `224` clicks, `14.1K` impressions, CTR `1.6%`, average position `7.1`.
- Last `28 days`: `64` clicks, `4.41K` impressions, CTR `1.5%`, average position `8.7`.
- Comparable pre-rollout `28 days` (`2026-04-06 - 2026-05-03`): `89` clicks, `5.87K` impressions, CTR `1.5%`, average position `6.8`.
- Comparable pre/post `15 days`:
  - Before core SEO rollout (`2026-04-19 - 2026-05-03`): `39` clicks, `2.88K` impressions, CTR `1.4%`, average position `8.1`.
  - After core SEO rollout (`2026-05-04 - 2026-05-18`): `30` clicks, `2.1K` impressions, CTR `1.4%`, average position `8.7`.
- Top visible queries for last `28 days`:
  - `татьяна мунн`: `9` clicks / `17` impressions.
  - `дневник эмоций`: `4` clicks / `266` impressions.
  - `как вести дневник эмоций`: `2` clicks / `174` impressions.
  - `социальный интеллект`: `1` click / `82` impressions.
  - `что такое дневник эмоций`: `1` click / `22` impressions.
  - `лекции по психологии му...`: `1` click / `9` impressions.
  - Additional zero-click impression queries include `социальный интеллект это`, `муна`, `дневник эмоций как вести`, `дневник эмоций пример`.
- Top visible pages for last `28 days`:
  - `https://moonn.ru/article_diary_of_emotions`: `15` clicks / `2,025` impressions.
  - `https://moonn.ru/`: `15` clicks / `283` impressions.
  - `https://moonn.ru/article_femininity`: `9` clicks / `549` impressions.
  - `https://moonn.ru/lectures1`: `7` clicks / `132` impressions.
  - `https://moonn.ru/page485296765.html`: `4` clicks / `83` impressions.
  - `https://moonn.ru/emotional-intelligence/knowledge-base/social-intelligence`: `2` clicks / `595` impressions.
  - `https://moonn.ru/schematherapy`: `2` clicks / `218` impressions.
  - `https://moonn.ru/uslugi_konflikti_na_rabote`: `2` clicks / `115` impressions.
  - `https://moonn.ru/emotional-intelligence/lesson-12`: `2` clicks / `32` impressions.
  - `https://moonn.ru/physiotherapy`: `2` clicks / `11` impressions.
- Top visible pages by impressions for last `28 days`:
  - `https://moonn.ru/article_diary_of_emotions`: `15` clicks / `2,025` impressions.
  - `https://moonn.ru/emotional-intelligence/knowledge-base/social-intelligence`: `2` clicks / `595` impressions.
  - `https://moonn.ru/article_femininity`: `9` clicks / `549` impressions.
  - `https://moonn.ru/`: `15` clicks / `283` impressions.
  - `https://moonn.ru/uslugi_sohranit_brak`: `0` clicks / `258` impressions.
  - `https://moonn.ru/schematherapy`: `2` clicks / `218` impressions.
  - `https://moonn.ru/lectures1`: `7` clicks / `132` impressions.
  - `https://moonn.ru/uslugi_konflikti_na_rabote`: `2` clicks / `115` impressions.
  - `https://moonn.ru/emotional-intelligence/diagnostika-ei`: `1` click / `107` impressions.
  - `https://moonn.ru/uslugi_procrastination`: `0` clicks / `106` impressions.

### Yandex Webmaster

Property: `https://moonn.ru`.

- Dashboard is accessible through Chrome.
- Site diagnostics show: `0` errors and `1` recommendation.
- Webmaster highlights duplicate metadata:
  - `9` duplicate titles.
  - `22` duplicate descriptions.
- Search-query statistics page is accessible for `18 Apr 2026 - 18 May 2026`, but a readable table/export was not captured in this bounded pass.

## Current Interpretation

The SEO implementation was not wasted technically, but the current GSC data does not yet prove search-growth uplift.

The strongest positive signal is that Google Search Console now exposes concrete non-brand demand surfaces around `дневник эмоций`, `как вести дневник эмоций`, `социальный интеллект`, and related informational pages. These pages are discoverable. However, comparable GSC windows are weaker after the rollout: `89` clicks / `5.87K` impressions before versus `64` clicks / `4.41K` impressions in the latest 28 days; and `39` clicks / `2.88K` impressions before versus `30` clicks / `2.1K` impressions in the first 15 days after the core rollout.

Metrika confirms that tracked site traffic changed sharply after the rollout window: `4` visits before the core application window versus `312` visits after May 7. Because the Metrika snippet was also fixed during the SEO/RKN workstream, this should be treated as "tracked traffic became visible and active", not as a pure SEO-only uplift.

The strongest limitation is conversion/path analytics: Yandex.Metrika shows traffic and search-source quality, but the visible popular-content report collapses page data to `https://moonn.ru/`. This blocks reliable understanding of what users click and which Moonn pages drive onsite interest inside Metrika. GSC page data partially compensates for SEO pages, but it does not replace onsite behavior and goal tracking.

Current conclusion: SEO produced measurable search visibility and tracked traffic, but not yet measurable GSC growth. The next work should focus on CTR/snippet improvements for high-impression low-click pages, Metrika URL/page tracking, duplicate metadata cleanup, and goals for consultation/contact actions.

## Problem Areas

- Machine-readable API/export evidence is still blocked by missing OAuth/API access.
- Yandex.Metrika page-level content reporting appears too collapsed to evaluate interest by page; this needs URL/pageview tracking correction or a different report/export configuration.
- Google Search Console confirms SEO visibility, but average CTR is still low: `1.5%` over the last 28 days.
- Google Search Console does not yet show before/after growth: the latest comparable windows are lower than pre-rollout windows.
- Google Search Console top SEO page is `article_diary_of_emotions`, which shows `2,025` impressions and `15` clicks; this page should become the first content-to-consultation funnel improvement candidate.
- High-impression low-click pages need snippet/intent work: social-intelligence (`595` impressions / `2` clicks), `uslugi_sohranit_brak` (`258` / `0`), procrastination (`106` / `0`).
- Yandex Webmaster still reports `9` duplicate titles and `22` duplicate descriptions.
- Raw HTML still does not reflect the rendered H1/schema mitigation, so audits must continue to distinguish raw source vs rendered DOM.
- Image alt remains unresolved across `83` pages at source/raw level.
- `robots_txt_blocked` appears on `12` pages; `9` look intentionally out-of-index, but `3` are marked `fix_robots_then_strengthen`: `/psy4psy`, `/schematherapy`, `/selfharm`.
- Privacy/RKN raw audit still sees `404` for `/privacy`, `/personal-data-consent`, `/cookies`, `/data-subject-request`; existing `/politic` may cover part of the policy layer, but canonical endpoint strategy remains unresolved.
- The audit scripts previously wrote to historical filenames. This run fixed the scripts to write dated output files.

## Follow-Up Tasks

1. Fix or document Yandex.Metrika page-level tracking so the content report separates Moonn URLs instead of collapsing visible page data to `https://moonn.ru/`.
2. Create a conversion-goal map for consultation/contact actions and verify that Yandex.Metrika goals capture them without adding new legal/privacy risk.
3. Use GSC top pages to create a focused content-funnel backlog: start with `article_diary_of_emotions`, homepage, `article_femininity`, `lectures1`, and social-intelligence content.
4. Resolve Yandex Webmaster duplicate metadata: `9` duplicate titles and `22` duplicate descriptions.
5. Resolve the three `fix_robots_then_strengthen` pages: `/psy4psy`, `/schematherapy`, `/selfharm`.
6. Create a source-level image-alt remediation packet for the 83-page scope, with filenames/alt text separated from hidden marketing tokens.
7. Decide privacy endpoint canon: keep `/politic` only with internal redirects/links, or publish canonical `/privacy`, `/cookies`, `/personal-data-consent`, `/data-subject-request` pages after legal approval.
8. Update the supervisor so future runs first try official APIs/exports and then explicitly fall back to Chrome GUI capture when APIs are blocked.

## Artifacts

- `docs/moonn-production-scope-seo-audit-2026-05-20.json`
- `docs/moonn-production-scope-seo-audit-2026-05-20.md`
- `docs/moonn-production-scope-seo-audit-2026-05-20.csv`
- `docs/moonn-rendered-heading-audit-2026-05-20.json`
- `docs/moonn-rendered-heading-audit-2026-05-20.md`
- `docs/moonn-rendered-heading-audit-2026-05-20.csv`
- `docs/moonn-rendered-schema-audit-2026-05-20.json`
- `docs/moonn-rendered-schema-audit-2026-05-20.md`
- `docs/moonn-rendered-schema-audit-2026-05-20.csv`
- `docs/moonn-privacy-compliance-audit-2026-05-20.json`
- `docs/moonn-privacy-compliance-audit-2026-05-20.md`
