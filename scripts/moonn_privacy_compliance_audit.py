from __future__ import annotations

import json
import re
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "docs" / "moonn-gsc-yandex-reindex-packet-2026-05-08.json"
RUN_DATE = datetime.now(timezone.utc).date().isoformat()
OUT_JSON = ROOT / "docs" / f"moonn-privacy-compliance-audit-{RUN_DATE}.json"
OUT_MD = ROOT / "docs" / f"moonn-privacy-compliance-audit-{RUN_DATE}.md"

POLICY_URLS = [
    "https://moonn.ru/privacy",
    "https://moonn.ru/personal-data-consent",
    "https://moonn.ru/cookies",
    "https://moonn.ru/data-subject-request",
]


@dataclass
class PageResult:
    url: str
    status: int | str
    formSignals: int
    consentSignals: int
    checkboxSignals: int
    yandexMetrikaSignals: int
    webvisorSignals: int
    googleAnalyticsSignals: int
    hasPolicyLink: bool
    hasConsentLink: bool
    hasCookieText: bool
    riskFlags: list[str]


def fetch(url: str, timeout: int = 25) -> tuple[int | str, str]:
    req = Request(url, headers={"User-Agent": "MoonnComplianceAudit/1.0"})
    try:
        with urlopen(req, timeout=timeout) as response:
            return response.getcode(), response.read().decode("utf-8", errors="replace")
    except HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", errors="replace")
    except URLError as exc:
        return f"ERROR:{exc.reason}", ""


def count(pattern: str, html: str) -> int:
    return len(re.findall(pattern, html, flags=re.IGNORECASE | re.DOTALL))


def analyze_page(url: str) -> PageResult:
    status, html = fetch(url)
    form_signals = count(r"t-form|js-form-proccess|data-tilda-formskey|formaction|<form\b", html)
    consent_signals = count(r"персональн|согласи|конфиденц|privacy|personal-data|consent", html)
    checkbox_signals = count(r'type=["\']checkbox["\']|t-checkbox|checkbox', html)
    yandex_signals = count(r"mc\.yandex\.ru|ym\(", html)
    webvisor_signals = count(r"webvisor\s*:\s*true", html)
    ga_signals = count(r"google-analytics|googletagmanager|gtag\(", html)
    has_policy_link = bool(re.search(r'href=["\'][^"\']*(privacy|policy|personal-data)', html, re.I))
    has_consent_link = bool(re.search(r'href=["\'][^"\']*(consent|soglas|personal-data)', html, re.I))
    has_cookie_text = bool(re.search(r"cookie|cookies|куки|метрик", html, re.I))

    flags: list[str] = []
    if isinstance(status, int) and status >= 400:
        flags.append("http_error")
    if form_signals and not checkbox_signals:
        flags.append("forms_without_detected_checkbox")
    if form_signals and consent_signals == 0:
        flags.append("forms_without_detected_consent_text")
    if yandex_signals and not has_cookie_text:
        flags.append("metrics_without_detected_cookie_notice_text")
    if ga_signals:
        flags.append("google_analytics_signal_detected")

    return PageResult(
        url=url,
        status=status,
        formSignals=form_signals,
        consentSignals=consent_signals,
        checkboxSignals=checkbox_signals,
        yandexMetrikaSignals=yandex_signals,
        webvisorSignals=webvisor_signals,
        googleAnalyticsSignals=ga_signals,
        hasPolicyLink=has_policy_link,
        hasConsentLink=has_consent_link,
        hasCookieText=has_cookie_text,
        riskFlags=flags,
    )


def load_scope_urls() -> list[str]:
    data = json.loads(PACKET.read_text(encoding="utf-8"))
    urls = [row["url"] for row in data["urls"]]
    return list(dict.fromkeys(urls))


def write_report(payload: dict[str, Any]) -> None:
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    pages = payload["pages"]
    policy = payload["policyEndpoints"]
    high_risk = [p for p in pages if p["riskFlags"]]
    form_pages = [p for p in pages if p["formSignals"]]

    lines = [
        f"# Moonn Privacy Compliance Audit — {RUN_DATE}",
        "",
        "## Summary",
        "",
        f"- Scope URLs checked: `{len(pages)}`.",
        f"- Policy endpoints checked: `{len(policy)}`.",
        f"- Pages with form signals: `{len(form_pages)}`.",
        f"- Pages with risk flags: `{len(high_risk)}`.",
        "",
        "## Policy Endpoints",
        "",
    ]
    for row in policy:
        lines.append(f"- `{row['url']}` — `{row['status']}`")

    lines.extend([
        "",
        "## Required Publication Pages",
        "",
        "- `/privacy` — policy for personal-data processing.",
        "- `/personal-data-consent` — consent text linked from every form checkbox.",
        "- `/cookies` — cookies and Yandex Metrika/Webvisor notice.",
        "- `/data-subject-request` — request/withdrawal/update/deletion procedure, or equivalent section inside `/privacy`.",
        "",
        "## High-Risk Pages",
        "",
    ])
    for row in high_risk[:80]:
        flags = ", ".join(row["riskFlags"])
        lines.append(f"- `{row['url']}` — `{flags}`")

    if len(high_risk) > 80:
        lines.append(f"- ...and `{len(high_risk) - 80}` more. See JSON.")

    lines.extend([
        "",
        "## Gate",
        "",
        "- Do not treat this as legal advice.",
        "- Final publication requires confirmed operator details and legal approval.",
        "- Do not disable Yandex/Google crawling while fixing compliance.",
    ])
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    urls = load_scope_urls()
    policy_results = [asdict(analyze_page(url)) for url in POLICY_URLS]
    page_results = [asdict(analyze_page(url)) for url in urls]
    payload = {
        "version": 1,
        "createdAt": datetime.now(timezone.utc).isoformat(),
        "scope": "Moonn 83 production URLs privacy/form/cookie compliance read-only audit",
        "sourcePacket": str(PACKET.relative_to(ROOT)),
        "policyEndpoints": policy_results,
        "pages": page_results,
        "notes": [
            "This is a technical audit, not legal advice.",
            "Final public legal text requires confirmed operator details and legal approval.",
            "Google Analytics signals are flagged separately because cross-border/legal handling depends on actual configuration.",
        ],
    }
    write_report(payload)
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
