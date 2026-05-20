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

- Yandex.Metrika API for counter `96397286` returned `403 access_denied`.
- Yandex Webmaster API returned `403 INVALID_OAUTH_TOKEN`.
- Google Search Console API returned `401 Login Required`.
- Existing Chrome was running, but no Chrome DevTools Protocol port was open on `9222`, so Codex could not attach to the already-authenticated browser session.
- Therefore visits, users, pageviews, search phrases, click maps, Webvisor sessions, GSC clicks/impressions/CTR/queries and GA data are not verified in this run.

## Current Interpretation

The SEO implementation was not wasted technically: the rendered SEO/AEO layer is live and structurally strong on the full 83-page scope. The business question is still open: there is not enough verified analytics access in this run to say whether visits, search impressions, search queries or consultation clicks increased.

The biggest process gap is not the SEO code; it is missing machine-readable analytics export. The supervisor should not be considered complete until it can pull or ingest Yandex.Metrika, Yandex Webmaster and Google Search Console data for a fixed date range.

## Problem Areas

- Analytics evidence is blocked by missing OAuth/API access or exported reports.
- Raw HTML still does not reflect the rendered H1/schema mitigation, so audits must continue to distinguish raw source vs rendered DOM.
- Image alt remains unresolved across `83` pages at source/raw level.
- `robots_txt_blocked` appears on `12` pages; `9` look intentionally out-of-index, but `3` are marked `fix_robots_then_strengthen`: `/psy4psy`, `/schematherapy`, `/selfharm`.
- Privacy/RKN raw audit still sees `404` for `/privacy`, `/personal-data-consent`, `/cookies`, `/data-subject-request`; existing `/politic` may cover part of the policy layer, but canonical endpoint strategy remains unresolved.
- The audit scripts previously wrote to historical filenames. This run fixed the scripts to write dated output files.

## Follow-Up Tasks

1. Connect or export Yandex.Metrika for counter `96397286`: visits, users, pageviews, sources, search phrases, popular pages, click goals and Webvisor/clickmap summary for 2026-04-29 to 2026-05-20.
2. Connect or export Google Search Console for `https://moonn.ru/`: clicks, impressions, CTR, average position, pages, queries and sitemap/indexing status for the same period.
3. Check whether Google Analytics/GA4 is intentionally absent; if absent, keep Yandex.Metrika primary until legal/privacy posture for GA is approved.
4. Resolve the three `fix_robots_then_strengthen` pages: `/psy4psy`, `/schematherapy`, `/selfharm`.
5. Create a source-level image-alt remediation packet for the 83-page scope, with filenames/alt text separated from hidden marketing tokens.
6. Decide privacy endpoint canon: keep `/politic` only with internal redirects/links, or publish canonical `/privacy`, `/cookies`, `/personal-data-consent`, `/data-subject-request` pages after legal approval.
7. Update the supervisor so future runs require analytics export evidence before making a conclusion about SEO success or failure.

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
