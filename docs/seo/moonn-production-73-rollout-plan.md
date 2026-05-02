# Moonn Production 73 Rollout Plan

Generated: 2026-05-02T13:25:00+03:00

## Scope

- Production site: `https://moonn.ru`.
- Protected staging source: `Moonn Staging` / `https://carry-pacific-flatfish.tilda.ws`.
- Production Tilda project: original `Moonn.ru`.
- Page set: the same `73` `copied_verified` pages from `registry/tilda/moonn-staging-page-map.json`.
- Production rollout registry: `registry/tilda/moonn-production-73-rollout.json`.
- Production SEO audit: `registry/seo/moonn-production-73-seo-audit.json`.

## Operational Decision

Stop working on staging pages except as a reference and verification sandbox.

From this point, production work targets only the original pages that correspond to the copied `73` staging pages.

## Tilda API Constraint

Official Tilda API remains read/export/webhook oriented for this use case. It is suitable for:

- page list snapshots;
- live/export HTML checks;
- SEO/link audits;
- verification after publication.

It is not suitable for directly editing Tilda blocks, page HEAD, native SEO settings, image alt text, or publishing pages through the documented public API. Production changes must therefore be applied through the Tilda UI, but can be driven in batch with a registry and automated verification.

## Baseline Production Audit

Command:

```powershell
python scripts\seo_audit_production_73.py
```

Result:

- Pages in scope: `73`.
- Live `200 OK`: `72`.
- Live errors: `1`.
- Design theme missing: `73`.
- Pages with link issues: `44`.
- Link issue totals:
  - `http://wa.me/79777770303`: `69`.
  - `http://twa.me/79777770303`: `4`.
  - `http://.moonn.ru`: `26`.
  - `http://wa.me/+79777770303`: `0`.
  - `/http://wa.me/+79777770303`: `0`.
- Duplicate title groups: `1`.
- Duplicate description groups: `4`.
- Heading issue pages: `53`.
- Image alt issue pages: `72`.

Current live error:

- `https://moonn.ru/emotional-intelligence` returns `404`.

## Rollout Order

1. Apply the verified `Radiant Sanctuary` design snippet to the production page HEAD of the `73` original pages.
2. Publish and verify live HTML for all `73` pages:
   - exactly one `moonn-radiant-sanctuary-theme` marker;
   - pinned CSS `@102fb3d`;
   - no regression of known card/substrate/button rules.
3. Fix P1 production source-link defects on the `44` affected pages:
   - `http://wa.me/79777770303` -> `https://wa.me/79777770303`;
   - `http://twa.me/79777770303` -> `https://wa.me/79777770303`;
   - `http://.moonn.ru` -> `https://moonn.ru`.
4. Resolve `https://moonn.ru/emotional-intelligence`:
   - either restore/open the original page alias;
   - or add the correct production redirect/canonical target if it should not be public.
5. Build page-specific SEO/AEO manifests by cluster:
   - consultation pages;
   - lectures/events;
   - paid products/courses;
   - knowledge base/articles.
6. Apply native Tilda SEO settings and page-level JSON-LD where needed:
   - title;
   - description;
   - canonical;
   - schema.org;
   - image alt plan;
   - internal linking plan.

## Safety Gates

- Do not edit pages outside the `73` production rollout registry.
- Before each save/publish, verify production project context and source page id.
- Do not rely on project-level HEAD for this rollout; staging showed it does not reliably propagate to already published pages.
- Prefer page-level marked snippets and verify live HTML after publication.
- Production page is not complete until live HTML and the registry agree.
