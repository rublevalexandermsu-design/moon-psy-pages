# Paid Video Lectures YouTube Matching Status

Date: 2026-05-03
Workstream: Moonn paid video lectures
Branch: `codex/moonn-paid-video-lectures`

## Strategic Check

1. Platform value: high. Matching private recordings now lets the paid lecture catalog become a repeatable product workflow.
2. Obsolescence risk: high if raw YouTube links are pasted manually into public Tilda pages.
3. Stronger architecture: keep private video ids local/internal, sell through Tilda products, and expose videos only through protected watch pages.
4. Reuse: high. The same matching gate can support future courses, bundles, Timepad follow-up offers, and QR lecture catalogs.
5. 3-12 month risk if left manual: wrong recording sold, private links leaked, broken access after payment, and no audit trail for product/video mapping.

## Verified Facts

- YouTube Studio owner view was opened for the channel `Психолог Татьяна Мунн | БЫСТРАЯ ПСИХОЛОГИЯ`.
- The relevant February-March 2026 lecture recordings are present in Studio with `По ссылке` visibility.
- Private video ids and Studio URLs are stored only in local ignored output files and are not committed.
- Sanitized machine report without private ids: `registry/products/paid-video-lectures-youtube-match-status-2026-05-03.json`.
- Manifest updated without raw private video URLs: `registry/products/paid-video-lectures.manifest.json`.

## Match Summary

Confirmed unique candidates:

- `3796462` — `2605 Психология любви к себе`, duration `2:05:03`.
- `3796469` — `2606 Психология голода`, duration `1:59:58`.
- `3808782` — `2609 Психология Женщины`, duration `1:57:58`.
- `3808783` — `2610 Цифровая психология`, duration `2:00:16`.
- `3808803` — `Психология знакомства`, duration `1:54:42`.

Needs owner selection before paid rollout:

- `3796319` — `2604 Духовная психология`: main recording plus duplicate.
- `3796473` — `2607 Психология мужчины`: two matching uploads with the same duration.
- `3808776` — `2608 ИИ и ЭИ`: two matching uploads with different durations.
- `3808788` — `Быстрая психология`: part 1 and part 2 found for 30.03.2026.

Not a single recording yet:

- `3334362` — recurring/free lecture series entry. Keep outside paid rollout until it is mapped to a specific recording or bundle.

## Next Safe Step

Use one unique lecture as the pilot. The strongest first pilot is `3796462` because the match is unique and duration is full-length.

Before creating live paid access:

- visually verify the current Tilda payment provider and seller settings;
- create one protected Tilda watch page or Members/Courses lesson;
- create one product at `1300 RUB`;
- connect successful payment to the protected access group;
- run one approved test purchase;
- verify that the public storefront does not expose raw YouTube links.

## Privacy Rule

Do not commit raw private video ids, Studio edit URLs, owner-account snapshots, passwords, exported cookies, or browser session artifacts. Local matching files under `output/` are ignored by Git.
