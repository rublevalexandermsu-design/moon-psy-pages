# Moonn Tilda 404 Remediation B1

Created: 2026-05-01  
Project: `moon-psy-site`  
Workstream: `seo-aeo-retrofit`

## What This Batch Does

This is the first executable remediation batch from the GSC URL decision table. It focuses on URLs that Google reports as `Not found (404)` and one additional crawled old EI slug that also returns 404.

The production Tilda redirect settings were changed on 2026-05-01 after explicit user approval in the Codex thread.

## Tilda 301 Entries

Tilda path: `Site Settings -> SEO -> 301 redirects`.

Official constraints checked from Tilda Help:

- enter paths without domain, starting with `/`;
- 301 redirects work inside the same domain;
- Tilda 301 works from non-existent pages;
- existing pages require page/canonical edits or a redirect block, not a 301 rule.

Paste/add these rows:

| Old path | New path | Priority |
| --- | --- | --- |
| `/http://wa.me/+79777770303` | `/psiholog-konsultacii-moskva` | P0 |
| `/emotionalnaya-vygoranie` | `/emotional-intelligence/knowledge-base/burnout` | P1 |
| `/zaprocy` | `/page120952796.html` | P1 |
| `/zaprocy.html` | `/page120952796.html` | P1 |
| `/bystraya-psihologiya.html` | `/page120899276.html` | P1 |
| `/leksii.html` | `/lectures1` | P1 |
| `/kurs-duhovnoy-psihologii.html` | `/platnye-treningi-seminary-programmy-tatiana-moonn` | P2 |
| `/podrostki.html` | `/uslugi_podrostki` | P1 |
| `/emotional-intelligence/articles/why-it-matters` | `/emotional-intelligence/articles/why-ei-matters` | P1 |

CSV source: `registry/seo/moonn-tilda-301-redirects-b1.csv`.

Additional fallback rule added in Tilda UI:

| Old path | New path | Status |
| --- | --- | --- |
| `/http:*` | `/psiholog-konsultacii-moskva` | Attempted fallback for malformed internalized external URLs; not verified for the WhatsApp 404 as of the first live check. |

## Source Link Fixes

Redirects are not enough for the WhatsApp issue. The source Tilda links also need cleanup:

| Pattern | Replacement | Matches in snapshot | Priority |
| --- | --- | ---: | --- |
| `http://wa.me/+79777770303` | `https://wa.me/79777770303` | 1 | P0 |
| `http://wa.me/79777770303` | `https://wa.me/79777770303` | 88 | P1 |
| `http://.moonn.ru` | `https://moonn.ru` | 39 | P1 |

Snapshot search did not find a current source reference for `https://moonn.ru/static.tildacdn.com` or bare `src="static.tildacdn.com`, so `/static.tildacdn.com/` should not receive an SEO redirect unless a live crawl finds an active source link.

## After Applying In Tilda

Applied in Tilda UI: 2026-05-01T21:44:00+03:00.

Live verification batch: 2026-05-01T21:50:00+03:00, `curl -I`, 8 attempts per old path, recording `x-tilda-server`.

| Old path | Result |
| --- | --- |
| `/emotionalnaya-vygoranie` | Propagating: some Tilda servers return 301 to `/emotional-intelligence/knowledge-base/burnout`, some still return 404. |
| `/zaprocy` | Propagating: some Tilda servers return 301 to `/page120952796.html`, some still return 404. |
| `/zaprocy.html` | Propagating: some Tilda servers return 301 to `/page120952796.html`, some still return 404. |
| `/bystraya-psihologiya.html` | Propagating: some Tilda servers return 301 to `/page120899276.html`, some still return 404. |
| `/leksii.html` | Propagating: some Tilda servers return 301 to `/lectures1`, some still return 404. |
| `/kurs-duhovnoy-psihologii.html` | Propagating: some Tilda servers return 301 to `/platnye-treningi-seminary-programmy-tatiana-moonn`, some still return 404. |
| `/podrostki.html` | Propagating: most sampled Tilda servers return 301 to `/uslugi_podrostki`; one sampled server still returned 404. |
| `/emotional-intelligence/articles/why-it-matters` | Propagating: most sampled Tilda servers return 301 to `/emotional-intelligence/articles/why-ei-matters`; one sampled server still returned 404. |
| `/http://wa.me/+79777770303` | Not verified: still returns 404. Tilda exact and wildcard redirect rules did not fix this malformed URL class; source links must be fixed in Tilda content blocks. |

Next gates:

1. Re-check this batch after Tilda cache propagation.
2. Fix source links in Tilda blocks: `http://wa.me/+79777770303`, `http://wa.me/79777770303`, and `http://.moonn.ru`.
3. Crawl for `moonn.ru/http://wa.me`, `http://wa.me/`, `http://.moonn.ru`, and `moonn.ru/static.tildacdn.com`.
4. Only after stable live checks pass, validate the GSC 404 group.
