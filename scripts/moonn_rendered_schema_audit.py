import asyncio
import csv
import json
from datetime import datetime, timezone
from pathlib import Path

from playwright.async_api import async_playwright


ROOT = Path(__file__).resolve().parents[1]
PRODUCTION_AUDIT_PATH = ROOT / "docs" / "moonn-production-scope-seo-audit-2026-05-08.json"
JSON_OUT = ROOT / "docs" / "moonn-rendered-schema-audit-2026-05-08.json"
CSV_OUT = ROOT / "docs" / "moonn-rendered-schema-audit-2026-05-08.csv"
MD_OUT = ROOT / "docs" / "moonn-rendered-schema-audit-2026-05-08.md"


def load_urls():
    audit = json.loads(PRODUCTION_AUDIT_PATH.read_text(encoding="utf-8"))
    urls = []
    for item in audit.get("pages", []):
        url = item.get("url")
        if url and url not in urls:
            urls.append(url)
    return urls


async def audit_page(context, url):
    page = await context.new_page()
    result = {
        "url": url,
        "status": None,
        "loaded": False,
        "hasSchemaLayerScript": False,
        "hasGlobalEntitySchema": False,
        "jsonLdScriptCount": 0,
        "schemaTypes": [],
        "hasPerson": False,
        "hasWebSite": False,
        "hasWebPage": False,
        "hasBreadcrumbList": False,
        "hasArticle": False,
        "hasProfessionalService": False,
        "hasItemList": False,
        "jsonErrors": [],
        "error": None,
    }
    try:
        await page.route(
            "**/*",
            lambda route: route.abort()
            if route.request.resource_type in {"image", "media", "font", "stylesheet"}
            else route.continue_(),
        )
        response = await page.goto(url, wait_until="domcontentloaded", timeout=45000)
        result["status"] = response.status if response else None
        await page.wait_for_timeout(1800)
        result["loaded"] = True
        rendered = await page.evaluate(
            """() => {
                const scripts = Array.from(document.querySelectorAll('script[type="application/ld+json"]'));
                const parsed = [];
                const errors = [];
                for (const script of scripts) {
                    try {
                        const data = JSON.parse(script.textContent || '{}');
                        parsed.push({id: script.id || '', data});
                    } catch (error) {
                        errors.push({id: script.id || '', error: String(error)});
                    }
                }
                const nodes = [];
                const collect = (value) => {
                    if (!value || typeof value !== 'object') return;
                    if (Array.isArray(value)) {
                        value.forEach(collect);
                        return;
                    }
                    nodes.push(value);
                    if (Array.isArray(value['@graph'])) value['@graph'].forEach(collect);
                };
                parsed.forEach((entry) => collect(entry.data));
                const typeSet = new Set();
                for (const node of nodes) {
                    const type = node['@type'];
                    if (Array.isArray(type)) type.forEach((item) => typeSet.add(String(item)));
                    else if (type) typeSet.add(String(type));
                }
                const hasType = (name) => typeSet.has(name);
                return {
                    hasSchemaLayerScript: !!document.querySelector('script[src*="moonn-schema-layer.js"]'),
                    hasGlobalEntitySchema: !!document.querySelector('#moonn-global-entity-schema'),
                    jsonLdScriptCount: scripts.length,
                    schemaTypes: Array.from(typeSet).sort(),
                    hasPerson: hasType('Person'),
                    hasWebSite: hasType('WebSite'),
                    hasWebPage: hasType('WebPage'),
                    hasBreadcrumbList: hasType('BreadcrumbList'),
                    hasArticle: hasType('Article'),
                    hasProfessionalService: hasType('ProfessionalService'),
                    hasItemList: hasType('ItemList'),
                    jsonErrors: errors
                };
            }"""
        )
        result.update(rendered)
    except Exception as exc:
        result["error"] = repr(exc)
    finally:
        await page.close()
    return result


async def main():
    urls = load_urls()
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 1366, "height": 1200},
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36 MoonnRenderedSchemaAudit/1.0"
            ),
        )
        results = []
        for url in urls:
            results.append(await audit_page(context, url))
        await browser.close()

    summary = {
        "createdAt": datetime.now(timezone.utc).isoformat(),
        "checkedUrls": len(results),
        "http200": sum(1 for item in results if item["status"] == 200),
        "withSchemaLayerScript": sum(1 for item in results if item["hasSchemaLayerScript"]),
        "withGlobalEntitySchema": sum(1 for item in results if item["hasGlobalEntitySchema"]),
        "withJsonLd": sum(1 for item in results if item["jsonLdScriptCount"] > 0),
        "withPerson": sum(1 for item in results if item["hasPerson"]),
        "withWebSite": sum(1 for item in results if item["hasWebSite"]),
        "withWebPage": sum(1 for item in results if item["hasWebPage"]),
        "withBreadcrumbList": sum(1 for item in results if item["hasBreadcrumbList"]),
        "withJsonErrors": sum(1 for item in results if item["jsonErrors"]),
        "errors": sum(1 for item in results if item["error"]),
    }
    output = {"summary": summary, "pages": results}
    JSON_OUT.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    with CSV_OUT.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "url",
                "status",
                "hasSchemaLayerScript",
                "hasGlobalEntitySchema",
                "jsonLdScriptCount",
                "schemaTypes",
                "jsonErrors",
                "error",
            ],
        )
        writer.writeheader()
        for item in results:
            writer.writerow(
                {
                    "url": item["url"],
                    "status": item["status"],
                    "hasSchemaLayerScript": item["hasSchemaLayerScript"],
                    "hasGlobalEntitySchema": item["hasGlobalEntitySchema"],
                    "jsonLdScriptCount": item["jsonLdScriptCount"],
                    "schemaTypes": ", ".join(item["schemaTypes"]),
                    "jsonErrors": json.dumps(item["jsonErrors"], ensure_ascii=False),
                    "error": item["error"] or "",
                }
            )

    failures = [
        item
        for item in results
        if item["status"] != 200
        or not item["hasSchemaLayerScript"]
        or not item["hasGlobalEntitySchema"]
        or not item["hasPerson"]
        or not item["hasWebSite"]
        or not item["hasWebPage"]
        or item["jsonErrors"]
        or item["error"]
    ]
    lines = [
        "# Moonn Rendered Schema Audit — 2026-05-08",
        "",
        "## Summary",
        "",
    ]
    for key, value in summary.items():
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(["", "## Failures", ""])
    if failures:
        for item in failures:
            lines.append(f"- `{item['url']}` — status `{item['status']}`, error `{item['error']}`")
    else:
        lines.append("- None.")
    MD_OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
