import csv
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLAN_PATH = ROOT / "docs" / "moonn-tilda-folder-governance-plan-2026-05-08.json"
JSON_OUT = ROOT / "docs" / "moonn-tilda-archive-execution-packet-2026-05-08.json"
CSV_OUT = ROOT / "docs" / "moonn-tilda-archive-execution-packet-2026-05-08.csv"
MD_OUT = ROOT / "docs" / "moonn-tilda-archive-execution-packet-2026-05-08.md"


def main():
    plan = json.loads(PLAN_PATH.read_text(encoding="utf-8"))
    candidates = [
        row
        for row in plan["rows"]
        if row.get("governanceBucket") == "clear_archive_candidate"
        and row.get("recommendedAction") == "move_to_archive_folder_after_ui_gate"
    ]
    packet = {
        "version": 1,
        "createdAt": datetime.now(timezone.utc).isoformat(),
        "sourcePlan": str(PLAN_PATH.relative_to(ROOT)),
        "targetFolderPolicy": {
            "folderName": "ARCHIVE / DRAFT / TEST",
            "mustBeArchiveFolder": True,
            "officialTildaSource": "https://help.tilda.cc/folders",
            "executionGate": (
                "Move only these clear candidates after confirming in Tilda UI that the "
                "destination folder has Archive Folder enabled. Do not delete pages."
            ),
        },
        "notAllowed": [
            "Do not move protected 83-page SEO production scope.",
            "Do not move legal, payment, reviews, media-holder, news/event or ambiguous pages.",
            "Do not use Publish all pages as a cleanup substitute.",
            "Do not delete pages.",
        ],
        "candidates": candidates,
        "status": "prepared_not_executed",
        "reason": (
            "The archive list is ready, but live Tilda movement needs a UI gate: "
            "confirm an archived folder first, then move exactly these 8 candidates."
        ),
    }
    JSON_OUT.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    with CSV_OUT.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["pageId", "url", "alias", "title", "published", "recommendedAction"],
        )
        writer.writeheader()
        for row in candidates:
            writer.writerow(
                {
                    "pageId": row["pageId"],
                    "url": row["url"],
                    "alias": row["alias"],
                    "title": row["title"],
                    "published": row["published"],
                    "recommendedAction": row["recommendedAction"],
                }
            )

    lines = [
        "# Moonn Tilda Archive Execution Packet — 2026-05-08",
        "",
        "## Status",
        "",
        "- Prepared, not executed.",
        "- Official Tilda folder rule checked: an Archive Folder is excluded from Publish all pages.",
        "- Source: https://help.tilda.cc/folders",
        "",
        "## Execution Gate",
        "",
        "Move pages only after the destination folder is confirmed in Tilda UI as an Archive Folder.",
        "No deletion. No movement of legal, payment, reviews, news/event, media-holder or ambiguous pages.",
        "",
        "## Clear Candidates",
        "",
    ]
    for row in candidates:
        url = row["url"] or "(no public alias)"
        lines.append(f"- `{row['pageId']}` — `{url}` — {row['title']}")
    MD_OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"candidates": len(candidates), "json": str(JSON_OUT)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
