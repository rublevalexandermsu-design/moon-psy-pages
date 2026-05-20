import asyncio
import csv
import json
from datetime import datetime, timezone
from pathlib import Path

from playwright.async_api import async_playwright


ROOT = Path(__file__).resolve().parents[1]
PLAN_PATH = ROOT / "docs" / "moonn-h1-h2-ui-apply-plan-2026-05-06.json"
PRODUCTION_AUDIT_PATH = ROOT / "docs" / "moonn-production-scope-seo-audit-2026-05-06.json"
RUN_DATE = datetime.now(timezone.utc).date().isoformat()
JSON_OUT = ROOT / "docs" / f"moonn-rendered-heading-audit-{RUN_DATE}.json"
CSV_OUT = ROOT / "docs" / f"moonn-rendered-heading-audit-{RUN_DATE}.csv"
MD_OUT = ROOT / "docs" / f"moonn-rendered-heading-audit-{RUN_DATE}.md"


def normalize_heading_text(value: str) -> str:
    return " ".join((value or "").replace(" :", ":").split()).casefold()


async def audit_page(context, url, target_actions):
    page = await context.new_page()
    result = {
        "url": url,
        "status": None,
        "loaded": False,
        "hasSemanticLayerScript": False,
        "h1": [],
        "h2": [],
        "targetChecks": [],
        "error": None,
    }
    navigation_error = None
    try:
        await page.route(
            "**/*",
            lambda route: route.abort()
            if route.request.resource_type in {"image", "media", "font", "stylesheet"}
            else route.continue_(),
        )
        try:
            response = await page.goto(url, wait_until="domcontentloaded", timeout=45000)
            result["status"] = response.status if response else None
        except Exception as exc:
            navigation_error = repr(exc)
        await page.wait_for_timeout(1200)
        result["loaded"] = True
        result["hasSemanticLayerScript"] = await page.evaluate(
            "() => !!document.querySelector('script[src*=\"moonn-semantic-heading-layer.js\"]')"
        )
        headings = await page.evaluate(
            """() => Array.from(document.querySelectorAll('h1,h2')).map((node) => ({
                tag: node.tagName.toLowerCase(),
                text: (node.innerText || node.textContent || '').replace(/\\s+/g, ' ').trim(),
                recId: (node.closest('[id*="rec"]')?.id || '').replace(/\\D+/g, '') || null,
                className: node.className || ''
            }))"""
        )
        result["h1"] = [h for h in headings if h["tag"] == "h1"]
        result["h2"] = [h for h in headings if h["tag"] == "h2"]
        for action in target_actions:
            expected_tag = action["setTag"].lower()
            rec_id = str(action["recId"])
            signal = action["visibleSignal"]
            normalized_signal = normalize_heading_text(signal)
            found = [
                h
                for h in headings
                if h["tag"] == expected_tag
                and h.get("recId") == rec_id
                and normalized_signal in normalize_heading_text(h["text"])
            ]
            result["targetChecks"].append(
                {
                    "recId": rec_id,
                    "expectedTag": expected_tag,
                    "visibleSignal": signal,
                    "matched": bool(found),
                    "matchedText": found[0]["text"] if found else None,
                }
            )
        result["error"] = navigation_error
    except Exception as exc:
        result["error"] = repr(exc)
    finally:
        await page.close()
    return result


def load_urls_and_actions():
    plan = json.loads(PLAN_PATH.read_text(encoding="utf-8"))
    actions_by_url = {}
    for action in plan["actions"]:
        actions_by_url.setdefault(action["url"], []).append(action)

    production = json.loads(PRODUCTION_AUDIT_PATH.read_text(encoding="utf-8"))
    urls = []
    for item in production.get("pages", []):
        url = item.get("url")
        if url and url not in urls:
            urls.append(url)
    for url in actions_by_url:
        if url not in urls:
            urls.append(url)
    return urls, actions_by_url


async def main():
    urls, actions_by_url = load_urls_and_actions()
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 1366, "height": 1200},
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36 MoonnRenderedHeadingAudit/1.0"
            ),
        )
        semaphore = asyncio.Semaphore(6)

        async def guarded_audit(url):
            async with semaphore:
                return await audit_page(context, url, actions_by_url.get(url, []))

        results = await asyncio.gather(*(guarded_audit(url) for url in urls))
        await context.close()
        await browser.close()

    target_checks = [check for page in results for check in page["targetChecks"]]
    summary = {
        "createdAt": datetime.now(timezone.utc).isoformat(),
        "scope": "rendered DOM audit for Moonn production pages after Tilda global semantic heading layer publish",
        "sourcePlan": str(PLAN_PATH.relative_to(ROOT)),
        "sourceProductionAudit": str(PRODUCTION_AUDIT_PATH.relative_to(ROOT)),
        "pagesChecked": len(results),
        "pagesLoaded": sum(1 for r in results if r["loaded"]),
        "pagesWithSemanticLayerScript": sum(1 for r in results if r["hasSemanticLayerScript"]),
        "pagesWithExactlyOneH1": sum(1 for r in results if len(r["h1"]) == 1),
        "pagesWithMissingH1": sum(1 for r in results if len(r["h1"]) == 0),
        "pagesWithMultipleH1": sum(1 for r in results if len(r["h1"]) > 1),
        "targetChecks": len(target_checks),
        "targetChecksMatched": sum(1 for c in target_checks if c["matched"]),
        "targetChecksFailed": sum(1 for c in target_checks if not c["matched"]),
        "errors": sum(1 for r in results if r["error"]),
    }
    payload = {"summary": summary, "pages": results}
    JSON_OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    with CSV_OUT.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "url",
                "status",
                "hasSemanticLayerScript",
                "h1Count",
                "h1Text",
                "h2Count",
                "targetChecks",
                "targetChecksMatched",
                "error",
            ],
        )
        writer.writeheader()
        for item in results:
            writer.writerow(
                {
                    "url": item["url"],
                    "status": item["status"],
                    "hasSemanticLayerScript": item["hasSemanticLayerScript"],
                    "h1Count": len(item["h1"]),
                    "h1Text": " | ".join(h["text"] for h in item["h1"]),
                    "h2Count": len(item["h2"]),
                    "targetChecks": len(item["targetChecks"]),
                    "targetChecksMatched": sum(1 for c in item["targetChecks"] if c["matched"]),
                    "error": item["error"] or "",
                }
            )

    failed_targets = [
        {"url": page["url"], **check}
        for page in results
        for check in page["targetChecks"]
        if not check["matched"]
    ]
    problem_pages = [
        item
        for item in results
        if item["error"] or len(item["h1"]) != 1 or not item["hasSemanticLayerScript"]
    ]
    md = [
        f"# Moonn Rendered Heading Audit — {RUN_DATE}",
        "",
        "Rendered DOM check after publishing the global Tilda HEAD semantic heading layer.",
        "",
        "## Summary",
        "",
    ]
    for key, value in summary.items():
        md.append(f"- `{key}`: {value}")
    md.extend(["", "## Failed Target Checks", ""])
    if failed_targets:
        for item in failed_targets:
            md.append(
                f"- {item['url']} rec `{item['recId']}` expected `{item['expectedTag']}`: {item['visibleSignal']}"
            )
    else:
        md.append("- None.")
    md.extend(["", "## Pages Requiring Review", ""])
    if problem_pages:
        for item in problem_pages:
            h1 = " | ".join(h["text"] for h in item["h1"]) or "NONE"
            md.append(
                f"- {item['url']} status={item['status']} layer={item['hasSemanticLayerScript']} h1={len(item['h1'])}: {h1}"
            )
    else:
        md.append("- None.")
    MD_OUT.write_text("\n".join(md) + "\n", encoding="utf-8")

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if failed_targets:
        print("FAILED_TARGETS")
        print(json.dumps(failed_targets[:20], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
