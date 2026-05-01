import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from html import unescape
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
PAGE_MAP = ROOT / "registry" / "tilda" / "moonn-staging-page-map.json"
OUT = ROOT / "registry" / "seo" / "moonn-seo-audit-pages.json"


@dataclass
class PageAudit:
    source_page_id: str
    staging_page_id: str
    alias: str
    url: str
    status: int | None
    title: str
    description: str
    canonical: str
    robots: str
    h1: list[str]
    h2: list[str]
    image_count: int
    images_missing_alt: int
    error: str | None = None


def normalize_text(value: str | None) -> str:
    if not value:
        return ""
    value = re.sub(r"\s+", " ", unescape(value)).strip()
    return value


def attr(html: str, pattern: str) -> str:
    match = re.search(pattern, html, flags=re.IGNORECASE | re.DOTALL)
    return normalize_text(match.group(1) if match else "")


def tags(html: str, tag: str) -> list[str]:
    found = re.findall(fr"<{tag}\b[^>]*>(.*?)</{tag}>", html, flags=re.IGNORECASE | re.DOTALL)
    cleaned = []
    for item in found:
        text = re.sub(r"<[^>]+>", " ", item)
        text = normalize_text(text)
        if text:
            cleaned.append(text)
    return cleaned


def image_alt_counts(html: str) -> tuple[int, int]:
    images = re.findall(r"<img\b[^>]*>", html, flags=re.IGNORECASE | re.DOTALL)
    missing = 0
    for image in images:
        alt_match = re.search(r"\balt=(['\"])(.*?)\1", image, flags=re.IGNORECASE | re.DOTALL)
        if not alt_match or not normalize_text(alt_match.group(2)):
            missing += 1
    return len(images), missing


def fetch(url: str) -> tuple[int | None, str, str | None]:
    request = Request(url, headers={"User-Agent": "Mozilla/5.0 Moonn SEO audit"})
    try:
        with urlopen(request, timeout=25) as response:
            return response.status, response.read().decode("utf-8", errors="replace"), None
    except HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        return exc.code, body, str(exc)
    except (URLError, TimeoutError) as exc:
        return None, "", str(exc)


def audit_page(page: dict) -> PageAudit:
    url = page["staging_url"]
    status, html, error = fetch(url)
    title = attr(html, r"<title[^>]*>(.*?)</title>")
    description = attr(
        html,
        r"<meta\s+[^>]*name=(?:'|\")description(?:'|\")[^>]*content=(?:'|\")(.*?)(?:'|\")[^>]*>",
    )
    if not description:
        description = attr(
            html,
            r"<meta\s+[^>]*content=(?:'|\")(.*?)(?:'|\")[^>]*name=(?:'|\")description(?:'|\")[^>]*>",
        )
    canonical = attr(
        html,
        r"<link\s+[^>]*rel=(?:'|\")canonical(?:'|\")[^>]*href=(?:'|\")(.*?)(?:'|\")[^>]*>",
    )
    robots = attr(
        html,
        r"<meta\s+[^>]*name=(?:'|\")robots(?:'|\")[^>]*content=(?:'|\")(.*?)(?:'|\")[^>]*>",
    )
    image_count, images_missing_alt = image_alt_counts(html)
    return PageAudit(
        source_page_id=str(page.get("source_page_id", "")),
        staging_page_id=str(page.get("staging_page_id", "")),
        alias=str(page.get("alias", "")),
        url=url,
        status=status,
        title=title,
        description=description,
        canonical=canonical,
        robots=robots,
        h1=tags(html, "h1"),
        h2=tags(html, "h2"),
        image_count=image_count,
        images_missing_alt=images_missing_alt,
        error=error,
    )


def group_duplicates(audits: list[PageAudit], field: str) -> list[dict]:
    buckets: dict[str, list[PageAudit]] = defaultdict(list)
    for audit in audits:
        value = getattr(audit, field)
        if value:
            buckets[value].append(audit)
    duplicates = []
    for value, pages in buckets.items():
        if len(pages) > 1:
            duplicates.append(
                {
                    field: value,
                    "count": len(pages),
                    "pages": [
                        {
                            "url": page.url,
                            "alias": page.alias,
                            "source_page_id": page.source_page_id,
                            "staging_page_id": page.staging_page_id,
                        }
                        for page in pages
                    ],
                }
            )
    return sorted(duplicates, key=lambda item: (-item["count"], item[field]))


def main() -> int:
    data = json.loads(PAGE_MAP.read_text(encoding="utf-8"))
    pages = [page for page in data["pages"] if page.get("staging_url")]
    audits = [audit_page(page) for page in pages]
    result = {
        "schema_version": "1.0",
        "source": str(PAGE_MAP.relative_to(ROOT)),
        "page_count": len(audits),
        "ok_count": sum(1 for audit in audits if audit.status == 200),
        "error_count": sum(1 for audit in audits if audit.status != 200 or audit.error),
        "duplicate_titles": group_duplicates(audits, "title"),
        "duplicate_descriptions": group_duplicates(audits, "description"),
        "heading_issues": [
            {
                "url": audit.url,
                "alias": audit.alias,
                "h1_count": len(audit.h1),
                "h1": audit.h1,
                "h2_count": len(audit.h2),
            }
            for audit in audits
            if len(audit.h1) != 1 or not audit.h2
        ],
        "image_alt_issues": [
            {
                "url": audit.url,
                "alias": audit.alias,
                "image_count": audit.image_count,
                "images_missing_alt": audit.images_missing_alt,
            }
            for audit in audits
            if audit.images_missing_alt
        ],
        "pages": [audit.__dict__ for audit in audits],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in ["page_count", "ok_count", "error_count"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
