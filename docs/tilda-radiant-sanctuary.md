# Tilda Radiant Sanctuary Redesign

## Source

- Design packet: `C:\Users\yanta\Downloads\stitch_moonn.ru_modern_tilda_redesign (1).zip`
- Extracted source file: `DESIGN.md`
- Creative direction: `The Radiant Sanctuary`

## Scope

First implementation target is the staging homepage only:

- Staging project: `Moonn Staging`, project id `25075076`
- Staging homepage page id: `138660066`
- Public URL: `https://carry-pacific-flatfish.tilda.ws/`

Production `moonn.ru` must not be changed until the staging page is reviewed and explicitly approved.

## Implementation Strategy

Use a Tilda-compatible CSS theme layer instead of rebuilding Tilda blocks manually.

Reasons:

- The staging homepage is already a large Tilda page with many blocks.
- A CSS theme keeps content, forms, links, Tilda block logic, and future page transfer behavior intact.
- The same theme can later be reused across consultation, lecture, product, and knowledge-base pages.
- Page-by-page rollout lets us catch layout collisions before applying the style globally.

## Canonical Theme File

- `assets/tilda-radiant-sanctuary.css`

The CSS adds:

- Plus Jakarta Sans typography.
- Light radiant surface background.
- Glass-style buttons and navigation.
- Soft card surfaces.
- Tilda button normalization.
- Tilda card/container normalization.
- Focus states for forms.
- Reduced-motion safety.

The CSS intentionally avoids destructive layout changes. It does not reorder blocks, remove content, alter links, or change payment/form behavior.

## Tilda Insertion Contract

For a page-level pilot, insert the CSS into the page head or page custom HTML as:

```html
<script>
document.documentElement.classList.add('moonn-radiant-sanctuary');
</script>
<style>
/* paste assets/tilda-radiant-sanctuary.css here */
</style>
```

If Tilda strips `@import` inside a page-level style block, move the Google Fonts import to the page head or site head and leave the rest inside the style block.

## QA Gate

The page is not considered ready until these checks pass:

- Public staging URL opens with HTTP 200.
- Browser Use opens the page visually.
- No obvious overlapping text or CTA collisions on desktop viewport.
- Mobile viewport spot-check passes.
- Buttons remain clickable.
- Main forms remain visible.
- No production project publishing happened.

## Deployment Log

### 2026-05-01

- Inserted the theme snippet into the staging homepage HEAD code.
- Published only `Moonn Staging`.
- Confirmed the live homepage HTML contains:
  - `moonn-radiant-sanctuary`
  - `moonn-radiant-sanctuary-theme`
- Opened the live staging homepage in Browser Use.
- First-screen visual check passed: primary hero, menu, CTA buttons, and portrait area remain visible.
- Production `moonn.ru` was not changed.

## Tilda Editor Note

The page HEAD code editor has both a visible code editor textarea and a hidden `textarea[name="headcode"]`.

Do not fill only the hidden `headcode` textarea. It does not reliably persist through Tilda's save action.

Use the visible code editor field, save, reload the editor, and confirm the saved code appears in `headcode` before publishing.

## Follow-Up Workstreams

The user's broader request splits into three workstreams:

1. `staging-design-system`: unify visual style across copied staging pages.
2. `paid-video-membership`: identify paid lecture/video pages and design payment plus protected viewing through Tilda-compatible mechanisms.
3. `seo-aeo-retrofit`: after design and paid access are stable, run SEO/AEO improvements page by page with metadata, schema, canonical, image alt, and content QA gates.

The paid video/membership workstream must be handled separately because it affects payments, access control, and user entitlements.
