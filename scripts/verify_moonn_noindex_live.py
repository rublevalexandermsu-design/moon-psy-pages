from __future__ import annotations

import argparse
import json
import time
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKETS_PATH = ROOT / "docs" / "moonn-seo-repositioning-2026-05-12" / "seo-aeo-tilda-apply-packets.json"
DEFAULT_OUT = ROOT / "docs" / "moonn-seo-repositioning-2026-05-12" / "noindex-live-verification-2026-05-12.json"


def fetch_html(url: str) -> tuple[int, str]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 MoonnNoindexVerifier/2026-05-12",
            "Cache-Control": "no-cache",
        },
    )
    with urllib.request.urlopen(request, timeout=25) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.status, response.read().decode(charset, errors="replace")


def verify_url(item: dict[str, object]) -> dict[str, object]:
    try:
        status, html = fetch_html(str(item["url"]))
        lower_html = html.lower()
        return {
            "path": item["path"],
            "url": item["url"],
            "page_id": item.get("page_id"),
            "status": status,
            "robots_noindex": "noindex" in lower_html,
            "canonical_present": 'rel="canonical"' in lower_html or "rel='canonical'" in lower_html,
            "h1_count": lower_html.count("<h1"),
        }
    except Exception as exc:  # noqa: BLE001
        return {
            "path": item["path"],
            "url": item["url"],
            "page_id": item.get("page_id"),
            "status": "error",
            "error": repr(exc),
            "robots_noindex": False,
        }


def load_noindex_items() -> list[dict[str, object]]:
    packets = json.loads(PACKETS_PATH.read_text(encoding="utf-8"))
    return list(packets["tildaApplyQueue"]["noindexPages"])


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify live noindex markers for the Moonn repositioning noindex queue.")
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    parser.add_argument("--delay", type=float, default=0.15)
    args = parser.parse_args()

    items = load_noindex_items()
    results = []
    for index, item in enumerate(items, start=1):
        result = verify_url(item)
        results.append(result)
        print(f"{index:02d}/{len(items)} {result['path']} noindex={result['robots_noindex']} status={result['status']}")
        if args.delay:
            time.sleep(args.delay)

    payload = {
        "createdDate": "2026-05-12",
        "sourcePackets": str(PACKETS_PATH.relative_to(ROOT)),
        "total": len(results),
        "noindexCount": sum(1 for result in results if result.get("robots_noindex")),
        "missingNoindex": [result["path"] for result in results if not result.get("robots_noindex")],
        "results": results,
    }
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"out": str(out), "noindexCount": payload["noindexCount"], "total": payload["total"]}, ensure_ascii=False))
    return 0 if payload["noindexCount"] == payload["total"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
