# Tilda API staging workflow

## Canon

- Production project in Tilda: `Moonn.ru`, project id `8326812`.
- Local API credentials are stored only in `.env`; they must not be committed.
- The Tilda API is read/export-oriented. It is used for local snapshots, registry sync, and audit inputs.
- Editable project cloning inside Tilda is not available through the documented API.

## Official Tilda copy path

Tilda documents the project copy flow through the cabinet UI:

1. Duplicate pages in the source project.
2. Create a new Tilda project.
3. Move duplicated pages into the new project.

Tilda also documents a limit of 100 new pages per day, so a full editable copy of `Moonn.ru` may require more than one day if all published and draft pages are copied.

## Local snapshot path

Use the local snapshot script for safe read-only review:

```powershell
python scripts\tilda_sync_snapshot.py --all-pages
```

Output:

- `output/tilda-snapshot/project.json`
- `output/tilda-snapshot/pages.json`
- `output/tilda-snapshot/published-pages.json`
- `output/tilda-snapshot/pages/*.html`
- `output/tilda-snapshot/snapshot-manifest.json`

Serve locally:

```powershell
python -m http.server 8787 --bind 127.0.0.1
```

from `output/tilda-snapshot/pages`, then open:

```text
http://127.0.0.1:8787/index.html
```

## Current checked result

- API access works.
- Project `Moonn.ru` was found.
- Local full-page snapshot exported 131 published pages.
- Local homepage opened in browser at `http://127.0.0.1:8787/index.html`.
- Browser reported one JavaScript console error: `Unexpected token 'function'`.

## Initial homepage SEO signals

- Title length: 90 characters.
- Description length: 166 characters.
- Canonical: `https://moonn.ru`.
- Open Graph image exists.
- H1 count: 5.
- H2 count: 0.
- Images: 55.
- Images without alt: 55.
- Scripts: 74.

## Analytics boundary

Tilda API does not expose visits, button clicks, or page-view analytics. For traffic and click data, connect one of:

- Yandex Metrica access for `moonn.ru`.
- Google Analytics/Search Console access, if installed.
- Tilda built-in statistics access, if used.
- A future first-party event layer in staging before production rollout.
