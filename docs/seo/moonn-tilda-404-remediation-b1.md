# Moonn Tilda 404 Remediation B1

Created: 2026-05-01  
Project: `moon-psy-site`  
Workstream: `seo-aeo-retrofit`

## What This Batch Does

This is the first executable remediation batch from the GSC URL decision table. It focuses on URLs that Google reports as `Not found (404)` and one additional crawled old EI slug that also returns 404.

No production Tilda settings were changed while preparing this packet.

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

## Source Link Fixes

Redirects are not enough for the WhatsApp issue. The source Tilda links also need cleanup:

| Pattern | Replacement | Matches in snapshot | Priority |
| --- | --- | ---: | --- |
| `http://wa.me/+79777770303` | `https://wa.me/79777770303` | 1 | P0 |
| `http://wa.me/79777770303` | `https://wa.me/79777770303` | 88 | P1 |
| `http://.moonn.ru` | `https://moonn.ru` | 39 | P1 |

Snapshot search did not find a current source reference for `https://moonn.ru/static.tildacdn.com` or bare `src="static.tildacdn.com`, so `/static.tildacdn.com/` should not receive an SEO redirect unless a live crawl finds an active source link.

## After Applying In Tilda

1. Publish the production project.
2. Re-check every old path for redirect behavior.
3. Crawl for `moonn.ru/http://wa.me`, `http://wa.me/`, `http://.moonn.ru`, and `moonn.ru/static.tildacdn.com`.
4. Only after live checks pass, validate the GSC 404 group.

