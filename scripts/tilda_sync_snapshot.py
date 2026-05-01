import argparse
import json
import os
import sys
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen


API_BASE_URL = "https://api.tildacdn.info"


def load_env(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if path.exists():
        for raw_line in path.read_text(encoding="utf-8-sig").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            values[key.strip()] = value.strip()
    values.update({key: value for key, value in os.environ.items() if key.startswith("TILDA_")})
    return values


def require_config(values: dict[str, str]) -> dict[str, str]:
    required = ["TILDA_PUBLIC_KEY", "TILDA_SECRET_KEY", "TILDA_PROJECT_ID"]
    missing = [key for key in required if not values.get(key)]
    if missing:
        joined = ", ".join(missing)
        raise RuntimeError(f"Missing Tilda config values: {joined}")
    return {
        "publickey": values["TILDA_PUBLIC_KEY"],
        "secretkey": values["TILDA_SECRET_KEY"],
        "projectid": values["TILDA_PROJECT_ID"],
    }


def call_tilda(method: str, params: dict[str, str]) -> dict:
    url = f"{API_BASE_URL}/v1/{method}/?{urlencode(params)}"
    with urlopen(url, timeout=30) as response:
        data = json.loads(response.read().decode("utf-8"))
    if data.get("status") == "ERROR":
        message = data.get("message") or data.get("error") or "Unknown Tilda API error"
        raise RuntimeError(f"Tilda API {method} failed: {message}")
    return data


def page_url(page: dict) -> str:
    alias = (page.get("alias") or "").strip("/")
    if not alias:
        return "https://moonn.ru/"
    return f"https://moonn.ru/{alias}"


def safe_page_filename(page: dict) -> str:
    alias = (page.get("alias") or "").strip("/").replace("/", "__")
    if alias:
        return f"{alias}.html"
    return page.get("filename") or f"page{page['id']}.html"


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_html(path: Path, html: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a local read-only Tilda API snapshot.")
    parser.add_argument("--env", default=".env", help="Path to local env file with Tilda keys.")
    parser.add_argument("--out", default="output/tilda-snapshot", help="Snapshot output directory.")
    parser.add_argument("--all-pages", action="store_true", help="Export all published pages, not only the index page.")
    args = parser.parse_args()

    config = require_config(load_env(Path(args.env)))
    out_dir = Path(args.out)
    pages_dir = out_dir / "pages"

    project = call_tilda("getprojectinfo", config)["result"]
    pages = call_tilda("getpageslist", config)["result"]
    published_pages = [page for page in pages if page.get("published")]
    index_page_id = str(project.get("indexpageid") or "")

    write_json(out_dir / "project.json", project)
    write_json(out_dir / "pages.json", pages)
    write_json(
        out_dir / "published-pages.json",
        [
            {
                "id": page.get("id"),
                "title": page.get("title"),
                "alias": page.get("alias"),
                "filename": page.get("filename"),
                "published": page.get("published"),
                "url": page_url(page),
            }
            for page in published_pages
        ],
    )

    selected_pages = published_pages if args.all_pages else [
        page for page in published_pages if str(page.get("id")) == index_page_id
    ]
    if not selected_pages and published_pages:
        selected_pages = [published_pages[0]]

    exported_pages = []
    for page in selected_pages:
        page_id = str(page["id"])
        page_data = call_tilda(
            "getpagefull",
            {
                "publickey": config["publickey"],
                "secretkey": config["secretkey"],
                "pageid": page_id,
            },
        )["result"]
        html_filename = "index.html" if str(page.get("id")) == index_page_id else safe_page_filename(page)
        html_path = pages_dir / html_filename
        write_html(html_path, page_data.get("html", ""))
        exported_pages.append(
            {
                "id": page_id,
                "title": page.get("title"),
                "source_url": page_url(page),
                "local_path": str(html_path.as_posix()),
            }
        )

    write_json(out_dir / "snapshot-manifest.json", {"project": project.get("title"), "exported_pages": exported_pages})
    print(json.dumps({"out": str(out_dir), "exported_pages": len(exported_pages)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
