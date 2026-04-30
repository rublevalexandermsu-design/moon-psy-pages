# Codex Chat History

Canonical append-only chat history for `moon-psy-site`.

## 2026-04-30T22:19:51+03:00 — Neuro Palmistry Entertainment Test

- Project: `moon-psy-site`
- Workstream: `site-entertainment-prototypes`
- Branch: `codex/palmistry-test-page`
- Request: create an HTML test page/block for `moonn.ru` about neuro-palmistry with palm images from the internet and selectable palm variants.
- Decisions:
  - Use the existing `moon-psy-site` repository, not the parent AНО repository.
  - Create a separate branch for the independent prototype.
  - Build from `data/site.json` instead of placing an orphan HTML file beside the canonical generator.
  - Use Wikimedia Commons public-domain style historical palm diagrams and store local copies with Latin filenames.
  - Keep the result as entertainment only, with no photo upload and no personal-data collection.
  - Expose quiz images in `sitemap.xml` through the image sitemap namespace after build.
- Created or changed files:
  - `.gitignore`
  - `build_site.py`
  - `data/site.json`
  - `data/media-sources.json`
  - `data/publication-compliance.json`
  - `assets/favicon.svg`
  - `assets/images/palm-lines-chief.jpg`
  - `assets/images/palm-chart-right-hand.jpg`
  - `assets/images/palm-chart-classic.png`
  - `snippets/neuro-palmistry-test.html`
  - `docs/codex-chat-history.md`
- Open questions:
  - Whether the final block should be embedded into the live Tilda root `moonn.ru` or published on `tatyana-psy.moonn.ru` first.
  - Whether future entertainment tests should become a reusable `quiz` template family in the generator.
- Risks and incidents:
  - Wikimedia returned HTTP 429 while downloading extra hand-photo assets; the prototype avoids dependency on those failed images and uses the three successfully saved public-domain diagrams.
  - Esoteric wording can be interpreted as prediction, so the page uses a visible entertainment disclaimer and avoids deterministic future claims.
- QA:
  - `python -m json.tool` passed for `data/site.json`, `data/media-sources.json`, and `data/publication-compliance.json`.
  - `python -m py_compile build_site.py` passed.
  - `python build_site.py` produced `dist/neuro-palmistry-test.html` and `dist/snippets/neuro-palmistry-test.html`.
  - Playwright opened `http://127.0.0.1:8765/neuro-palmistry-test.html`, selected four answers, showed the result card, and reported zero console errors after favicon fix.
  - Public text scan passed for internal markers: `не дубль`, `контур`, `выглядит как`, `зачем этот раздел`, `для старта`, `будущая автоматическая`, `карточка для заявки`, `статус будет обновлён`, `технический`, `MVP`, `прототип`, `раздел нужен`.
- Commit: `f1953c2`
