import argparse
import json
import re
from pathlib import Path


DEFAULT_PATTERNS = {
    "http_wa": {
        "pattern": "http://wa.me/79777770303",
        "replacement": "https://wa.me/79777770303",
        "priority": "P1",
    },
    "bad_domain": {
        "pattern": "http://.moonn.ru",
        "replacement": "https://moonn.ru",
        "priority": "P1",
    },
    "bad_plus_wa": {
        "pattern": "http://wa.me/+79777770303",
        "replacement": "https://wa.me/79777770303",
        "priority": "P0",
    },
    "internalized_bad_plus_wa": {
        "pattern": "/http://wa.me/+79777770303",
        "replacement": "https://wa.me/79777770303",
        "priority": "P0",
    },
}


def load_page_map(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    by_alias: dict[str, dict] = {}
    for page in data.get("pages", []):
        if page.get("status") != "copied_verified":
            continue
        alias = (page.get("alias") or "").strip("/")
        filename = "index.html" if not alias else f"{alias.replace('/', '__')}.html"
        by_alias[filename] = page
    return by_alias


def record_ids_near(text: str, needle: str) -> list[str]:
    ids: set[str] = set()
    for match in re.finditer(re.escape(needle), text):
        start = max(0, match.start() - 4000)
        end = min(len(text), match.end() + 4000)
        for record_id in re.findall(r"rec(\d+)", text[start:end]):
            ids.add(record_id)
    return sorted(ids)


def audit_pages(pages_dir: Path, page_map: dict[str, dict]) -> dict:
    html_files = sorted(pages_dir.glob("*.html"))
    items = []
    totals = {key: 0 for key in DEFAULT_PATTERNS}

    for html_file in html_files:
        html = html_file.read_text(encoding="utf-8", errors="ignore")
        counts = {}
        records = {}
        for key, config in DEFAULT_PATTERNS.items():
            needle = config["pattern"]
            count = html.count(needle)
            counts[key] = count
            totals[key] += count
            if count:
                records[key] = record_ids_near(html, needle)
        if not any(counts.values()):
            continue

        page = page_map.get(html_file.name, {})
        items.append(
            {
                "filename": html_file.name,
                "source_page_id": page.get("source_page_id"),
                "staging_page_id": page.get("staging_page_id"),
                "alias": page.get("alias"),
                "title": page.get("title"),
                "staging_url": page.get("staging_url"),
                "counts": counts,
                "nearby_record_ids": records,
            }
        )

    return {
        "schema_version": "1.0",
        "patterns": DEFAULT_PATTERNS,
        "pages_checked": len(html_files),
        "pages_with_issues": len(items),
        "totals": totals,
        "items": items,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit exported Tilda HTML for known link issues.")
    parser.add_argument("--pages-dir", required=True)
    parser.add_argument("--page-map", default="registry/tilda/moonn-staging-page-map.json")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    result = audit_pages(Path(args.pages_dir), load_page_map(Path(args.page_map)))
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("pages_checked", "pages_with_issues", "totals")}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
