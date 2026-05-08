# Moonn GSC/Yandex Reindex Report — 2026-05-08

## Scope

- 83 Moonn production URLs after JSON-LD/schema rollout.
- Live sitemap: `https://moonn.ru/sitemap.xml`.
- Sitemap URL count: `149`.
- Scope URLs present in sitemap: `83/83`.

## Google Search Console

- Submitted `sitemap.xml` in GSC Sitemaps for property `https://moonn.ru/`.
- UI result: `Sitemap submitted successfully`.
- Google bulk path used: sitemap, because Google documentation recommends sitemap for multiple URLs and quota-limits individual URL Inspection requests.
- Manual URL Inspection was also used for the first priority URLs:
  - `https://moonn.ru/` — observed as indexed, request indexing result: `Indexing requested`.
  - `https://moonn.ru/events_tp` — observed as `Discovered - currently not indexed`, request indexing result: `Indexing requested`.
  - `https://moonn.ru/lectures1` — observed as indexed, request indexing result: `Indexing requested`.
  - `https://moonn.ru/psiholog-konsultacii-moskva` — observed as indexed, request indexing result: `Indexing requested`.
- Stop rule: do not manually submit all `83` URLs through URL Inspection. Use sitemap-level monitoring first, then inspect/request only stale priority URLs.

## Yandex Webmaster

- Submitted all `83` URLs in `Индексирование -> Переобход страниц`.
- Daily limit before submit: `470`.
- Daily remaining after submit: `387`.
- UI result: submitted-pages section appeared and textarea cleared.

## Next Check

- Yandex: check statuses after 3 days; repeat only failed URLs.
- Google: check sitemap last read, Pages indexing, and URL Inspection statuses for the four manually requested priority URLs after several days; use URL Inspection again only for stale or failed priority URLs.
