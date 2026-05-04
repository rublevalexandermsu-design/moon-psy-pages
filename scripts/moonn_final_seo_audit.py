from __future__ import annotations

import csv
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "docs"
SITEMAP_URL = "https://moonn.ru/sitemap.xml"
ROBOTS_URL = "https://moonn.ru/robots.txt"
TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")
JSON_OUT = OUT_DIR / f"moonn-final-seo-audit-{TODAY}.json"
MD_OUT = OUT_DIR / f"moonn-final-seo-audit-{TODAY}.md"
CSV_OUT = OUT_DIR / f"moonn-final-seo-audit-{TODAY}.csv"


REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; MoonnSEOAudit/1.0; +https://moonn.ru/)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


def fetch(url: str, timeout: int = 25) -> tuple[int | str, str, dict[str, str]]:
    req = urllib.request.Request(url, headers=REQUEST_HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            charset = resp.headers.get_content_charset() or "utf-8"
            return resp.status, raw.decode(charset, errors="replace"), dict(resp.headers)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        return exc.code, body, dict(exc.headers)
    except Exception as exc:  # noqa: BLE001
        return "ERROR", str(exc), {}


def get_sitemap_urls() -> list[dict[str, str]]:
    status, body, _ = fetch(SITEMAP_URL, timeout=40)
    if status != 200:
        raise RuntimeError(f"Cannot fetch sitemap: {status} {body[:200]}")
    root = ET.fromstring(body)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    rows: list[dict[str, str]] = []
    for item in root.findall("sm:url", ns):
        loc = item.findtext("sm:loc", default="", namespaces=ns).strip()
        lastmod = item.findtext("sm:lastmod", default="", namespaces=ns).strip()
        if loc:
            rows.append({"url": loc, "lastmod": lastmod})
    return rows


def get_robot_disallows() -> list[str]:
    status, body, _ = fetch(ROBOTS_URL, timeout=25)
    if status != 200:
        return []
    disallows: list[str] = []
    for line in body.splitlines():
        line = line.strip()
        if line.lower().startswith("disallow:"):
            value = line.split(":", 1)[1].strip()
            if value:
                disallows.append(value)
    return disallows


def attr_value(tag: str, attr: str) -> str:
    match = re.search(rf"\b{re.escape(attr)}\s*=\s*(['\"])(.*?)\1", tag, flags=re.I | re.S)
    return html.unescape(match.group(2).strip()) if match else ""


def first_meta(content: str, key_attr: str, key_value: str) -> str:
    for tag in re.findall(r"<meta\b[^>]*>", content, flags=re.I | re.S):
        if attr_value(tag, key_attr).lower() == key_value.lower():
            return attr_value(tag, "content")
    return ""


def first_link(content: str, rel_value: str) -> str:
    for tag in re.findall(r"<link\b[^>]*>", content, flags=re.I | re.S):
        if attr_value(tag, "rel").lower() == rel_value.lower():
            return attr_value(tag, "href")
    return ""


def visible_text(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    value = html.unescape(value)
    return re.sub(r"\s+", " ", value).strip()


def page_kind(url: str) -> str:
    path = urllib.parse.urlparse(url).path.strip("/")
    if not path:
        return "home"
    if path in {"politic", "offer", "pay-good-moon", "call"}:
        return "legal_or_service"
    if path.startswith("emotional-intelligence/knowledge-base"):
        return "knowledge_base"
    if path.startswith("emotional-intelligence/articles") or path.endswith("_article") or "article" in path:
        return "article"
    if path.startswith("uslugi_") or path in {
        "psiholog-konsultacii-moskva",
        "psiholog-moskva-online",
        "psiholog_moskva",
        "semeyniy_psiholog",
    }:
        return "service"
    if path in {"events_tp", "events", "lectures1", "speaker", "vystupleniya-lekcii-treningi-psiholog-tatiana-moonn"}:
        return "lecture_or_events"
    if path.startswith("page") and path.endswith(".html"):
        return "numeric_page"
    if re.fullmatch(r"st\d+", path) or "test" in path.lower():
        return "test_or_staging"
    return "other"


def robots_blocked(url: str, disallows: list[str]) -> bool:
    path = urllib.parse.urlparse(url).path or "/"
    return any(path.startswith(rule.rstrip("*")) for rule in disallows if rule and not rule.endswith("*"))


def audit_one(row: dict[str, str], disallows: list[str]) -> dict[str, object]:
    url = row["url"]
    status, body, headers = fetch(url)
    result: dict[str, object] = {
        "url": url,
        "lastmod": row.get("lastmod", ""),
        "status": status,
        "contentType": headers.get("content-type", ""),
        "kind": page_kind(url),
        "robotsTxtBlocked": robots_blocked(url, disallows),
    }
    if status != 200 or not isinstance(body, str):
        result["decision"] = "fix_http_or_remove_from_sitemap"
        result["issues"] = [f"HTTP status {status}"]
        return result

    title_match = re.search(r"<title[^>]*>(.*?)</title>", body, flags=re.I | re.S)
    title = visible_text(title_match.group(1)) if title_match else ""
    description = first_meta(body, "name", "description")
    robots = first_meta(body, "name", "robots")
    canonical = first_link(body, "canonical")
    og_image = first_meta(body, "property", "og:image")
    h1_values = [visible_text(m) for m in re.findall(r"<h1\b[^>]*>(.*?)</h1>", body, flags=re.I | re.S)]
    jsonld_count = len(re.findall(r'application/ld\+json', body, flags=re.I))
    img_tags = re.findall(r"<img\b[^>]*>", body, flags=re.I | re.S)
    img_count = len(img_tags)
    missing_alt = sum(1 for tag in img_tags if not attr_value(tag, "alt").strip())

    issues: list[str] = []
    if not title:
        issues.append("missing_title")
    elif len(title) < 25:
        issues.append("short_title")
    elif len(title) > 80:
        issues.append("long_title")
    if not description:
        issues.append("missing_description")
    elif len(description) < 70:
        issues.append("short_description")
    elif len(description) > 180:
        issues.append("long_description")
    if not canonical:
        issues.append("missing_canonical")
    elif canonical.rstrip("/") != url.rstrip("/"):
        issues.append("canonical_mismatch")
    if "noindex" in robots.lower():
        issues.append("meta_noindex")
    if not og_image:
        issues.append("missing_og_image")
    if not h1_values:
        issues.append("missing_h1")
    elif len(h1_values) > 1:
        issues.append("multiple_h1")
    if jsonld_count == 0:
        issues.append("missing_jsonld")
    if img_count and missing_alt:
        issues.append("images_missing_alt")
    if result["robotsTxtBlocked"]:
        issues.append("robots_txt_blocked")
    if result["kind"] in {"numeric_page", "test_or_staging"}:
        issues.append("opaque_or_test_slug")

    if status != 200:
        decision = "fix_http_or_remove_from_sitemap"
    elif "meta_noindex" in issues or result["robotsTxtBlocked"]:
        decision = "keep_out_of_index_or_remove_from_sitemap"
    elif result["kind"] in {"numeric_page", "test_or_staging"}:
        decision = "review_noindex_or_rename_slug"
    elif issues:
        decision = "strengthen_seo"
    else:
        decision = "ok_index"

    result.update(
        {
            "title": title,
            "titleLength": len(title),
            "description": description,
            "descriptionLength": len(description),
            "canonical": canonical,
            "robots": robots,
            "ogImagePresent": bool(og_image),
            "h1Count": len(h1_values),
            "h1": h1_values[:3],
            "jsonLdCount": jsonld_count,
            "imageCount": img_count,
            "imagesMissingAlt": missing_alt,
            "issues": issues,
            "decision": decision,
        }
    )
    return result


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    title_counter = Counter(str(r.get("title", "")).strip().lower() for r in rows if r.get("title"))
    desc_counter = Counter(str(r.get("description", "")).strip().lower() for r in rows if r.get("description"))
    duplicate_titles = {k for k, v in title_counter.items() if v > 1}
    duplicate_descs = {k for k, v in desc_counter.items() if v > 1}

    for row in rows:
        title_key = str(row.get("title", "")).strip().lower()
        desc_key = str(row.get("description", "")).strip().lower()
        issues = list(row.get("issues", []))
        if title_key in duplicate_titles:
            issues.append("duplicate_title")
        if desc_key in duplicate_descs:
            issues.append("duplicate_description")
        row["issues"] = sorted(set(issues))
        if row.get("decision") == "ok_index" and issues:
            row["decision"] = "strengthen_seo"

    by_decision = Counter(str(r.get("decision")) for r in rows)
    by_issue = Counter(issue for r in rows for issue in r.get("issues", []))
    by_kind = Counter(str(r.get("kind")) for r in rows)
    grouped: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get("decision"))].append(str(row.get("url")))

    return {
        "checkedUrls": len(rows),
        "http200": sum(1 for r in rows if r.get("status") == 200),
        "byDecision": dict(by_decision),
        "byIssue": dict(by_issue.most_common()),
        "byKind": dict(by_kind),
        "groups": dict(grouped),
    }


def write_reports(rows: list[dict[str, object]], summary: dict[str, object]) -> None:
    payload = {
        "version": 1,
        "createdAt": datetime.now(timezone.utc).isoformat(),
        "source": SITEMAP_URL,
        "summary": summary,
        "pages": rows,
    }
    JSON_OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    with CSV_OUT.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "decision",
                "kind",
                "status",
                "url",
                "titleLength",
                "descriptionLength",
                "h1Count",
                "jsonLdCount",
                "imageCount",
                "imagesMissingAlt",
                "issues",
                "canonical",
                "title",
                "description",
            ],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "decision": row.get("decision"),
                    "kind": row.get("kind"),
                    "status": row.get("status"),
                    "url": row.get("url"),
                    "titleLength": row.get("titleLength", ""),
                    "descriptionLength": row.get("descriptionLength", ""),
                    "h1Count": row.get("h1Count", ""),
                    "jsonLdCount": row.get("jsonLdCount", ""),
                    "imageCount": row.get("imageCount", ""),
                    "imagesMissingAlt": row.get("imagesMissingAlt", ""),
                    "issues": ";".join(row.get("issues", [])),
                    "canonical": row.get("canonical", ""),
                    "title": row.get("title", ""),
                    "description": row.get("description", ""),
                }
            )

    lines = [
        f"# Moonn Final SEO Audit — {TODAY}",
        "",
        "Mode: read-only live audit from `https://moonn.ru/sitemap.xml`.",
        "",
        "## Summary",
        "",
        f"- Checked URLs: {summary['checkedUrls']}",
        f"- HTTP 200: {summary['http200']}",
    ]
    for decision, count in summary["byDecision"].items():
        lines.append(f"- `{decision}`: {count}")
    lines += ["", "## Top Issues", ""]
    for issue, count in list(summary["byIssue"].items())[:20]:
        lines.append(f"- `{issue}`: {count}")
    lines += ["", "## Decision Table", "", "| Decision | URL | Issues |", "| --- | --- | --- |"]
    sort_key = {"fix_http_or_remove_from_sitemap": 0, "review_noindex_or_rename_slug": 1, "keep_out_of_index_or_remove_from_sitemap": 2, "strengthen_seo": 3, "ok_index": 4}
    for row in sorted(rows, key=lambda r: (sort_key.get(str(r.get("decision")), 9), str(r.get("url")))):
        issues = ", ".join(row.get("issues", [])) or "none"
        lines.append(f"| `{row.get('decision')}` | `{row.get('url')}` | {issues} |")
    lines += [
        "",
        "## Next Action Rules",
        "",
        "- `ok_index`: leave indexed, only monitor.",
        "- `strengthen_seo`: improve metadata/H1/schema/image alt, then request reindexing.",
        "- `review_noindex_or_rename_slug`: decide whether the page is real; if real, rename to semantic slug and strengthen SEO; if not, noindex/remove from sitemap.",
        "- `keep_out_of_index_or_remove_from_sitemap`: keep blocked intentionally or remove from sitemap if it should not appear in search tools.",
        "- `fix_http_or_remove_from_sitemap`: fix response or remove from sitemap.",
    ]
    MD_OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    started = time.time()
    sitemap_rows = get_sitemap_urls()
    disallows = get_robot_disallows()
    results: list[dict[str, object]] = []
    with ThreadPoolExecutor(max_workers=6) as executor:
        futures = [executor.submit(audit_one, row, disallows) for row in sitemap_rows]
        for future in as_completed(futures):
            results.append(future.result())
    results.sort(key=lambda row: str(row.get("url")))
    summary = summarize(results)
    summary["durationSeconds"] = round(time.time() - started, 2)
    write_reports(results, summary)
    print(json.dumps({"json": str(JSON_OUT), "md": str(MD_OUT), "csv": str(CSV_OUT), "summary": summary}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
