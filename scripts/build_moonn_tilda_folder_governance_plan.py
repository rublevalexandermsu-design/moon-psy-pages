from __future__ import annotations

import csv
import json
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
INVENTORY_PATH = DOCS / "moonn-tilda-page-governance-inventory-2026-05-07.json"
OUT_JSON = DOCS / "moonn-tilda-folder-governance-plan-2026-05-08.json"
OUT_MD = DOCS / "moonn-tilda-folder-governance-plan-2026-05-08.md"
OUT_CSV = DOCS / "moonn-tilda-folder-governance-plan-2026-05-08.csv"


LEGAL_ALIASES = {"politic", "offer", "pay-good-moon", "call"}
CODE_MEDIA_ALIASES = {"586", "587", "588", "589", "888", "866"}
REVIEW_ALIASES = {"otzivi", "866"}
KNOWN_NEWS_RE = re.compile(r"^(novosti|20\d{6}|20\d{4}|vecherinka)", re.I)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def classify(item: dict) -> tuple[str, str, str]:
    decision = item.get("decision")
    alias = (item.get("alias") or "").strip("/")
    title = (item.get("title") or "").strip()
    title_l = title.lower()

    if decision == "work_scope_keep_publishable":
        return ("protected_work_scope", "keep_publishable", "Protected 83-page SEO work scope.")

    if decision == "archive_candidate_test_or_service":
        return (
            "clear_archive_candidate",
            "move_to_archive_folder_after_ui_gate",
            "Clear test/copy/legacy service candidate from read-only inventory; do not delete.",
        )

    if alias in LEGAL_ALIASES:
        return ("public_infrastructure", "keep_publishable", "Legal/payment/contact infrastructure page.")

    if alias in REVIEW_ALIASES or "отзыв" in title_l:
        return ("reviews_or_social_proof", "keep_publishable_review_later", "Reviews/social proof page; needed for Yandex Services workstream.")

    if alias in CODE_MEDIA_ALIASES or "изображ" in title_l or "коды" in title_l:
        return ("code_media_holder", "review_before_archive", "Likely internal code/media holder; verify dependencies before archiving.")

    if KNOWN_NEWS_RE.search(alias) or "новост" in title_l or "выступ" in title_l or "конференц" in title_l:
        return ("news_event_archive", "keep_or_consolidate_after_review", "Published news/event page; may support entity SEO and should not be archived blindly.")

    if not alias:
        return ("published_no_alias", "review_assign_alias_or_archive", "Published page without alias; classify content before archive or slug cleanup.")

    if decision == "review_published_outside_scope":
        return ("published_outside_scope", "review_keep_rename_or_archive", "Published outside current SEO scope; needs editorial decision.")

    return ("unknown_review", "review_required", "No safe automatic decision.")


def main() -> None:
    inventory = load_json(INVENTORY_PATH)
    rows = []
    for item in inventory["items"]:
        bucket, action, rationale = classify(item)
        rows.append(
            {
                "pageId": item["id"],
                "url": item["url"],
                "alias": item.get("alias") or "",
                "title": item.get("title") or "",
                "published": item.get("published"),
                "inventoryDecision": item.get("decision"),
                "governanceBucket": bucket,
                "recommendedAction": action,
                "rationale": rationale,
            }
        )

    counts: dict[str, int] = {}
    actions: dict[str, int] = {}
    for row in rows:
        counts[row["governanceBucket"]] = counts.get(row["governanceBucket"], 0) + 1
        actions[row["recommendedAction"]] = actions.get(row["recommendedAction"], 0) + 1

    payload = {
        "version": 1,
        "createdAt": datetime.now(timezone.utc).isoformat(),
        "sourceInventory": str(INVENTORY_PATH.relative_to(ROOT)),
        "totalPages": len(rows),
        "countsByBucket": counts,
        "countsByAction": actions,
        "safetyRules": [
            "Do not delete pages.",
            "Do not move protected_work_scope pages.",
            "Do not move legal/payment/contact/review/news pages automatically.",
            "Only clear_archive_candidate pages may be moved after the target Tilda folder is confirmed as archived.",
            "After any folder move, run a scoped publish/live check and update this plan.",
        ],
        "rows": rows,
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        "# Moonn Tilda Folder Governance Plan — 2026-05-08",
        "",
        f"- Source inventory: `{INVENTORY_PATH.relative_to(ROOT)}`",
        f"- Total pages: `{len(rows)}`",
        "",
        "## Counts By Bucket",
        "",
    ]
    for key, value in sorted(counts.items()):
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(["", "## Counts By Recommended Action", ""])
    for key, value in sorted(actions.items()):
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(
        [
            "",
            "## Safe Execution Rule",
            "",
            "Only `clear_archive_candidate` pages are ready for Tilda archive-folder movement, and only after the destination folder is confirmed as an archived folder in Tilda UI. Everything else stays publishable until editorial/legal/payment dependency review.",
            "",
            "## Clear Archive Candidates",
            "",
        ]
    )
    for row in rows:
        if row["governanceBucket"] == "clear_archive_candidate":
            lines.append(f"- `{row['pageId']}` `{row['url']}` — {row['title']}")
    lines.extend(["", "## Review Required Buckets", ""])
    for bucket in sorted(k for k in counts if k not in {"protected_work_scope", "clear_archive_candidate"}):
        lines.append(f"### {bucket}")
        for row in rows:
            if row["governanceBucket"] == bucket:
                lines.append(f"- `{row['pageId']}` `{row['url']}` — {row['recommendedAction']} — {row['title']}")
        lines.append("")
    OUT_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(rows), "countsByBucket": counts, "json": str(OUT_JSON)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
