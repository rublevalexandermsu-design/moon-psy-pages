import argparse
import json
import os
import re
from html import unescape
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen


API_BASE_URL = "https://api.tildacdn.info/v1"
LECTURE_PATTERNS = re.compile(
    r"(лекц|меропр|вебинар|курс|семинар|тренинг|timepad|youtube|запис|купить|оплат|приобр)",
    re.IGNORECASE,
)


def load_env(path: Path) -> dict[str, str]:
    values = {}
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
    missing = [key for key in ("TILDA_PUBLIC_KEY", "TILDA_SECRET_KEY", "TILDA_PROJECT_ID") if not values.get(key)]
    if missing:
        raise RuntimeError("Missing Tilda env values: " + ", ".join(missing))
    return {
        "publickey": values["TILDA_PUBLIC_KEY"],
        "secretkey": values["TILDA_SECRET_KEY"],
        "projectid": values["TILDA_PROJECT_ID"],
    }


def call_tilda(method: str, params: dict[str, str]) -> dict:
    url = f"{API_BASE_URL}/{method}/?{urlencode(params)}"
    with urlopen(url, timeout=30) as response:
        data = json.loads(response.read().decode("utf-8"))
    if data.get("status") == "ERROR":
        raise RuntimeError(f"Tilda API {method} failed: {data.get('message') or data.get('error')}")
    return data["result"]


def page_url(page: dict) -> str:
    alias = (page.get("alias") or "").strip("/")
    return "https://moonn.ru/" + alias if alias else "https://moonn.ru/"


def strip_tags(html: str) -> str:
    text = re.sub(r"<script\b[^>]*>.*?</script>", " ", html, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<style\b[^>]*>.*?</style>", " ", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", unescape(text)).strip()


def find_links(html: str) -> list[str]:
    links = re.findall(r"https?://[^\"'\s<>]+", html)
    return sorted(set(link.rstrip("),.;") for link in links if any(host in link for host in ("timepad", "youtube", "youtu.be"))))


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only audit for Moonn paid lecture candidates in Tilda.")
    parser.add_argument("--env", default=".env")
    parser.add_argument("--out", default="registry/products/paid-video-lectures-audit-2026-05-03.json")
    args = parser.parse_args()

    config = require_config(load_env(Path(args.env)))
    pages = call_tilda("getpageslist", config)
    published = [page for page in pages if page.get("published")]

    candidates = []
    for page in published:
        haystack = " ".join(str(page.get(key, "")) for key in ("title", "descr", "alias", "filename"))
        if not LECTURE_PATTERNS.search(haystack):
            continue
        page_data = call_tilda(
            "getpagefull",
            {
                "publickey": config["publickey"],
                "secretkey": config["secretkey"],
                "pageid": str(page["id"]),
            },
        )
        html = page_data.get("html", "")
        text = strip_tags(html)
        candidates.append(
            {
                "page_id": str(page.get("id")),
                "alias": page.get("alias"),
                "title": page.get("title"),
                "url": page_url(page),
                "timepad_links": [link for link in find_links(html) if "timepad" in link],
                "youtube_links": [link for link in find_links(html) if "youtube" in link or "youtu.be" in link],
                "signals": sorted(set(match.group(0).lower() for match in LECTURE_PATTERNS.finditer(text[:50000]))),
                "text_sample": text[:900],
            }
        )

    report = {
        "schema_version": "1.0",
        "generated_at": "2026-05-03",
        "scope": "read_only_tilda_paid_lecture_candidates",
        "candidate_count": len(candidates),
        "candidates": candidates,
    }
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"out": str(out), "candidate_count": len(candidates)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
