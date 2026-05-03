# Moonn Production Image SEO Audit

Date: 2026-05-03
Scope: 83 original production pages on `moonn.ru`.

## Result

The image SEO layer was audited across all 83 production pages.

- Pages checked: `83`
- Pages with errors: `0`
- Visual objects found: `1490`
- Regular `<img>` images: `446`
- Tilda background/cover images: `1044`
- Pages without images: `0`
- Images/backgrounds needing real filename reupload: `1445`
- Images/backgrounds missing source-level title: `1490`
- Background/cover images without native alt channel: `1044`

Machine-readable outputs:

- `registry/seo/moonn-production-83-image-seo-audit.json`
- `registry/seo/moonn-production-83-image-seo-audit.csv`

## What Was Improved In Code

`assets/moonn-seo-aeo-enhancer.js` now includes page-specific image SEO for regular `<img>` images:

- contextual `alt`;
- contextual `title`;
- `data-moonn-recommended-filename` with the future SEO filename for reupload;
- existing lazy loading and async decoding support are preserved.

The generator source is `scripts/build_moonn_seo_enhancer.py`.

## Important Boundary

The actual Tilda CDN filename cannot be changed by editing HTML attributes. If the current URL is something like `photo.png`, `Rectangle_...`, or `____.jpg`, true file-name SEO requires:

1. Download/export the current image.
2. Rename it using the proposed filename from the audit CSV.
3. Reupload the file to Tilda/media.
4. Replace the image in the source Tilda block.
5. Publish and verify the live image URL.

Until that migration is done, the rendered SEO layer improves `alt/title/schema` signals, but the CDN URL itself remains the old Tilda filename.

## Recommended Rollout Order

1. First replace hero/OG images and above-the-fold covers on the homepage, consultations, lectures, paid products, and knowledge-base hub.
2. Then replace repeated profile photos and major course/event covers.
3. Leave decorative gradients/orbs as background assets unless they appear as actual content images.
4. After media reupload, run the image audit again and compare `images_needing_filename_reupload`.
5. Only then request image reindexing through Google Search Console and Yandex Webmaster.

## Local Migration Package

Prepared a local, non-Git media package:

- Folder: `output/moonn-image-seo-migration`
- Manifest: `output/moonn-image-seo-migration/manifest.csv`
- Downloaded SEO-named files: `1362`
- Download errors: `0`
- Total media size: `484012169` bytes

The package is intentionally stored under `output/`, which is ignored by Git. It is the working source for Tilda media replacement, not a repository artifact.

The replacement manifest includes:

- production page URL;
- Tilda source page id;
- original image URL;
- canonical download URL;
- current filename;
- SEO filename;
- local file path;
- proposed alt/title;
- file hash and content type.

## Full-Fidelity Replacement Options

1. Best long-term: use the package as a Tilda media migration checklist and replace images in source blocks, starting with hero/OG/above-the-fold assets.
2. Faster but still source-level: batch replace only the highest-impact pages first, then rerun the audit to measure reduction in technical filenames.
3. Rendered-only fallback: keep the current enhancer for contextual `alt/title`, but this does not change the CDN filename and should not be treated as full image SEO.

Official Tilda API remains export/sync oriented in this project context; a documented API method for uploading a file to Tilda media library and replacing block assets was not available. Therefore the replacement step requires Tilda UI/DevTools automation or manual media replacement against the manifest.

## Validation

- `python scripts/seo_image_audit_production.py` completed with `error_count=0`.
- `python scripts/build_moonn_seo_enhancer.py` regenerated the enhancer.
- `node --check assets/moonn-seo-aeo-enhancer.js` passed.
- A mock DOM check confirmed that contextual `alt`, `title`, and `data-moonn-recommended-filename` are applied to matched images.

## Deployment Note

Production Tilda currently loads the older enhancer pinned to commit `8dd2572`. The image SEO code and manifests are ready in GitHub, but the live Tilda pages will only receive these new image rules after the Tilda head snippets are updated to the new asset URL or to a stable loader.
