# Tilda API staging workflow

## Canon

- Production project in Tilda: `Moonn.ru`, project id `8326812`.
- Editable staging project in Tilda: `Moonn Staging`, project id `25075076`.
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
- Empty Tilda staging project `Moonn Staging` was created with project id `25075076`.
- Local full-page snapshot exported 131 published pages.
- Local homepage opened in browser at `http://127.0.0.1:8787/index.html`.
- Browser reported one JavaScript console error: `Unexpected token 'function'`.

## Next copy gate

Before copying pages into `Moonn Staging`, choose one scope:

- `pilot`: duplicate and move only the production homepage.
- `canonical`: copy the core public pages only after reviewing `published-pages.json`.
- `full`: copy all pages in batches; this is not recommended as the first pass because the source project includes drafts, tests, and archive-style pages.

For production safety, never move an original page. Only move duplicated pages into staging.

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

## Browser Use note

Browser Use is the preferred browser control path for this workstream.

On 2026-05-01, Browser Use was repaired by restoring local `codex.exe` discovery for `node_repl.exe`:

- Expected local path: `C:\Users\yanta\AppData\Local\OpenAI\Codex\bin\codex.exe`.
- Source used for repair: installed Codex WindowsApps `app\resources\codex.exe`.
- Verification: Browser Use opened `https://example.com/`.

If Browser Use can open localhost but fails on external URLs with an app-server path error, refresh that local `codex.exe` copy after checking the currently installed Codex version path.
