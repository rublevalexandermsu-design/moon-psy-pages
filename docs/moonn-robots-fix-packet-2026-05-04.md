# Moonn Robots Fix Packet — 2026-05-04

## Problem

The live `robots.txt` contains broad prefix rules such as `Disallow: /psiholog`, which block real published pages that should be indexable.

Pages to unblock before SEO strengthening:

- `https://moonn.ru/psiholog-konsultacii-moskva`
- `https://moonn.ru/psiholog_moskva`
- `https://moonn.ru/psihology`

## Safe Change

Replace broad prefix blocking with exact legacy/test URL blocking only. Keep intentionally closed pages blocked, but do not block semantic service URLs by prefix.

Current risky rule:

```txt
Disallow: /psiholog
```

Recommended direction:

```txt
# Keep only confirmed legacy/noindex pages closed.
Disallow: /psiholog$

# Do not block live semantic service pages:
# https://moonn.ru/psiholog-konsultacii-moskva
# https://moonn.ru/psiholog_moskva
# https://moonn.ru/psihology
```

If Tilda does not support `$` exact matching in its robots editor, remove `Disallow: /psiholog` and keep the legacy page closed via page-level noindex or redirect instead.

## Validation

1. Publish robots changes in Tilda.
2. Fetch `https://moonn.ru/robots.txt`.
3. Re-run `python scripts/moonn_final_seo_audit.py --production-scope`.
4. Confirm the three URLs move from `fix_robots_then_strengthen` to `strengthen_seo` or `ok_index`.
