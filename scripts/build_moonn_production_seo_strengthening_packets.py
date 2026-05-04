from __future__ import annotations

import csv
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
AUDIT_PATH = DOCS / "moonn-production-scope-seo-audit-2026-05-04.json"
PRODUCTION_73_PATH = ROOT / "output" / "production-73-rollout-pages.json"
PRODUCTION_83_LOG_PATH = ROOT / "output" / "build-production-83-scope.log"
TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")
JSON_OUT = DOCS / f"moonn-production-seo-strengthening-packets-{TODAY}.json"
MD_OUT = DOCS / f"moonn-production-seo-strengthening-packets-{TODAY}.md"
CSV_OUT = DOCS / f"moonn-production-seo-strengthening-packets-{TODAY}.csv"
ROBOTS_OUT = DOCS / f"moonn-robots-fix-packet-{TODAY}.md"


ENTITY = {
    "@type": "Person",
    "@id": "https://moonn.ru/#tatiana-munn",
    "name": "Татьяна Мунн",
    "alternateName": [
        "Кумскова Татьяна Михайловна",
        "Татьяна Мунн (Кумскова)",
    ],
    "jobTitle": "Психолог МГУ, эксперт по эмоциональному интеллекту",
    "url": "https://moonn.ru/",
    "sameAs": [
        "https://moonn.timepad.ru/events/",
        "https://miiiips.ru/author-tatyana-munn-kumskova.html",
        "https://uslugi.yandex.ru/profile/TatyanaKumskovatatyanamunn-948629",
        "https://istina.msu.ru/workers/816305440/",
        "https://psyjournals.ru/authors/15337",
    ],
}


MANUAL_SUBJECTS = {
    "": "Психолог МГУ Татьяна Мунн",
    "events_tp": "Лекции Татьяны Мунн по психологии",
    "events": "Мероприятия Татьяны Мунн",
    "lectures1": "Архив лекций Татьяны Мунн",
    "speaker": "Татьяна Мунн как спикер",
    "otzivi": "Отзывы о психологе Татьяне Мунн",
    "recomend": "Рекомендации и материалы Татьяны Мунн",
    "kurs-ei": "Курс по эмоциональному интеллекту",
    "programmakursa": "Программа курса по эмоциональному интеллекту",
    "platnye-treningi-seminary-programmy-tatiana-moonn": "Платные тренинги и лекции Татьяны Мунн",
    "vystupleniya-lekcii-treningi-psiholog-tatiana-moonn": "Выступления, лекции и тренинги Татьяны Мунн",
    "baza-znaniy-emocionalnyy-intellekt-psihologiya": "База знаний по психологии и эмоциональному интеллекту",
    "emotional-intelligence/": "Эмоциональный интеллект",
    "emotional-intelligence/articles": "Статьи по эмоциональному интеллекту",
    "emotional-intelligence/knowledge-base": "База знаний по эмоциональному интеллекту",
    "psiholog-konsultacii-moskva": "Консультации психолога в Москве и онлайн",
    "psiholog_moskva": "Психолог в Москве",
    "psihology": "Психологическая помощь в Москве и онлайн",
    "articles/eq-dlya-rukovoditeley": "Эмоциональный интеллект руководителя",
    "emotional-intelligence/ei-leader-12": "Эмоциональный интеллект лидера",
}


SLUG_WORDS = {
    "abuse_gaslight": "Абьюз и газлайтинг",
    "aromatherapy": "Ароматерапия и эмоциональное состояние",
    "article_diary_of_emotions": "Дневник эмоций",
    "article_femininity": "Женственность в отношениях",
    "article_gadget_addiction": "Зависимость подростков от гаджетов",
    "article_toxic_job": "Негативные эмоции на работе",
    "eintellect": "Эмоциональный интеллект",
    "geshtalt": "Гештальт-подход",
    "kpt": "Когнитивно-поведенческая терапия",
    "microbiom": "Микробиом и эмоциональное состояние",
    "panicheskie_ataki": "Панические атаки",
    "phytotherapy": "Фитотерапия и эмоциональное состояние",
    "psy4psy": "Психолог для психолога",
    "psychoanalys": "Психоанализ",
    "psypodgotovka1": "Психологическая подготовка",
    "salt": "Соль и самочувствие",
    "schematherapy": "Схематерапия",
    "selfharm": "Самоповреждение у подростков",
    "semeynie_konflikti_article": "Семейные конфликты",
    "semeyniy_psiholog": "Семейный психолог",
    "seminar555": "Семинар по методу Быстрая психология",
    "shppp333": "Школа практической психологии для подростков",
    "trauma": "Психологическая травма",
    "vacuum_cups": "Вакуумные банки и самочувствие",
    "vigoranie_article": "Выгорание на работе",
    "vospitanie_article": "Воспитание ребенка",
    "water": "Вода и психоэмоциональное состояние",
}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def alias_from_url(url: str) -> str:
    path = urlparse(url).path.lstrip("/")
    if url.endswith("/") and path:
        return path + "/"
    return path


def load_scope_map() -> dict[str, dict[str, str]]:
    items: list[dict[str, object]] = []
    if PRODUCTION_73_PATH.exists():
        items.extend(load_json(PRODUCTION_73_PATH))
    if PRODUCTION_83_LOG_PATH.exists():
        items.extend(load_json(PRODUCTION_83_LOG_PATH).get("additions", []))

    by_url: dict[str, dict[str, str]] = {}
    for item in items:
        alias = str(item.get("alias") or "").lstrip("/")
        url = str(item.get("production_url") or "").strip()
        if not url:
            url = "https://moonn.ru/" + alias if alias else "https://moonn.ru/"
        by_url[url] = {
            "alias": alias,
            "sourcePageId": str(item.get("source_page_id") or ""),
            "stagingPageId": str(item.get("staging_page_id") or ""),
            "scopeSource": str(item.get("scope_source") or "production_73_rollout"),
        }
    return by_url


def cleanup_subject(title: str, alias: str) -> str:
    if alias in MANUAL_SUBJECTS:
        return MANUAL_SUBJECTS[alias]
    if alias in SLUG_WORDS:
        return SLUG_WORDS[alias]

    value = title
    replacements = [
        r"^Статья\s*[-—]\s*",
        r"\|\s*Татьяна\s+Мунн$",
        r"\.\s*Психолог\s+Татьяна\s+Мунн.*$",
        r"\s*Психолог\s+Татьяна\s+Мунн.*$",
        r"\s*Психолог\s+МГУ.*$",
        r"\s*Быстрая\s+Психология.*$",
    ]
    for pattern in replacements:
        value = re.sub(pattern, "", value, flags=re.I).strip()
    value = re.sub(r"\s+", " ", value).strip(" .—-")
    return value or alias.replace("-", " ").replace("_", " ").strip().capitalize()


def trim_words(value: str, max_len: int) -> str:
    value = re.sub(r"\s+", " ", value).strip()
    if len(value) <= max_len:
        return value
    parts = value.split()
    out: list[str] = []
    for part in parts:
        candidate = " ".join(out + [part])
        if len(candidate) > max_len - 1:
            break
        out.append(part)
    return " ".join(out).rstrip(" ,.;:") or value[: max_len - 1].rstrip()


def sentence(value: str, max_len: int) -> str:
    value = trim_words(value, max_len).rstrip(" ,.;:")
    if value and value[-1] not in ".!?":
        value += "."
    return value


def make_title(subject: str, kind: str, alias: str) -> str:
    if alias == "":
        return "Татьяна Мунн — психолог МГУ в Москве и онлайн"
    if kind == "service":
        return trim_words(f"{subject}: психолог МГУ Татьяна Мунн", 68)
    if kind == "lecture_or_events":
        return trim_words(f"{subject} — психология и эмоциональный интеллект", 68)
    if kind in {"article", "knowledge_base"}:
        return trim_words(f"{subject} | Татьяна Мунн", 68)
    return trim_words(f"{subject} | психолог Татьяна Мунн", 68)


def make_description(subject: str, kind: str, alias: str) -> str:
    desc_subject = trim_words(subject, 72)
    if alias == "":
        return "Татьяна Мунн (Кумскова Татьяна Михайловна) — психолог МГУ: консультации в Москве и онлайн, эмоциональный интеллект, отношения, стресс и подростки."
    if kind == "service":
        text = f"{desc_subject}: консультации Татьяны Мунн, психолога МГУ, в Москве и онлайн. Стресс, отношения, эмоции и личные состояния."
    elif kind == "lecture_or_events":
        text = f"{desc_subject}: лекции и практические материалы Татьяны Мунн по психологии, эмоциональному интеллекту, отношениям и soft skills."
    elif kind == "article":
        text = f"{desc_subject}: авторская статья Татьяны Мунн, психолога МГУ, о поведении, эмоциях, отношениях и саморегуляции."
    elif kind == "knowledge_base":
        text = f"{desc_subject}: справочный материал Татьяны Мунн по эмоциональному интеллекту, коммуникации, саморегуляции и устойчивости."
    else:
        text = f"{desc_subject}: материал Татьяны Мунн, психолога МГУ, о практической психологии, эмоциях, отношениях и саморегуляции."
    return sentence(text, 158)


def h1_instruction(page: dict, subject: str) -> dict[str, str]:
    count = int(page.get("h1Count") or 0)
    if count == 0:
        action = "add_h1"
        note = "Добавить один видимый H1 в верхний смысловой блок страницы."
    elif count > 1:
        action = "reduce_to_one_h1"
        note = "Оставить один главный H1; остальные крупные заголовки перевести в H2/H3."
    else:
        action = "keep_one_h1"
        note = "Сохранить один H1 и сверить, что он совпадает с темой страницы."
    return {"targetH1": subject, "action": action, "note": note}


def breadcrumbs(url: str, subject: str) -> list[dict[str, object]]:
    parsed = urlparse(url)
    parts = [part for part in parsed.path.strip("/").split("/") if part]
    items = [{"@type": "ListItem", "position": 1, "name": "Главная", "item": "https://moonn.ru/"}]
    if parts:
        items.append({"@type": "ListItem", "position": 2, "name": subject, "item": url})
    return items


def page_schema(page: dict, subject: str, title: str, description: str) -> dict[str, object]:
    url = str(page["url"])
    kind = str(page["kind"])
    graph: list[dict[str, object]] = [ENTITY]
    web_page = {
        "@type": "WebPage",
        "@id": f"{url}#webpage",
        "url": url,
        "name": title,
        "description": description,
        "isPartOf": {"@id": "https://moonn.ru/#website"},
        "about": {"@id": "https://moonn.ru/#tatiana-munn"},
        "author": {"@id": "https://moonn.ru/#tatiana-munn"},
    }
    graph.append(
        {
            "@type": "WebSite",
            "@id": "https://moonn.ru/#website",
            "url": "https://moonn.ru/",
            "name": "Татьяна Мунн",
            "publisher": {"@id": "https://moonn.ru/#tatiana-munn"},
        }
    )
    graph.append(web_page)
    if kind == "service":
        graph.append(
            {
                "@type": "ProfessionalService",
                "@id": f"{url}#service",
                "name": subject,
                "url": url,
                "provider": {"@id": "https://moonn.ru/#tatiana-munn"},
                "areaServed": ["Москва", "Онлайн"],
                "description": description,
            }
        )
    elif kind in {"article", "knowledge_base"}:
        graph.append(
            {
                "@type": "Article",
                "@id": f"{url}#article",
                "headline": title,
                "url": url,
                "description": description,
                "author": {"@id": "https://moonn.ru/#tatiana-munn"},
                "publisher": {"@id": "https://moonn.ru/#tatiana-munn"},
                "mainEntityOfPage": {"@id": f"{url}#webpage"},
            }
        )
    elif kind == "lecture_or_events":
        graph.append(
            {
                "@type": "ItemList",
                "@id": f"{url}#lecture-list",
                "name": subject,
                "url": url,
                "description": description,
                "itemListElement": [],
            }
        )
    graph.append(
        {
            "@type": "BreadcrumbList",
            "@id": f"{url}#breadcrumbs",
            "itemListElement": breadcrumbs(url, subject),
        }
    )
    return {"@context": "https://schema.org", "@graph": graph}


def build_packet(page: dict, scope: dict[str, str], apply_after_robots: bool = False) -> dict[str, object]:
    url = str(page["url"])
    alias = scope.get("alias") or alias_from_url(url)
    subject = cleanup_subject(str(page.get("title") or ""), alias)
    title = make_title(subject, str(page["kind"]), alias)
    description = make_description(subject, str(page["kind"]), alias)
    canonical = url
    return {
        "url": url,
        "alias": alias,
        "sourcePageId": scope.get("sourcePageId", ""),
        "decision": page.get("decision"),
        "applyStatus": "apply_after_robots_fix" if apply_after_robots else "ready_to_apply",
        "kind": page.get("kind"),
        "currentIssues": page.get("issues", []),
        "seo": {
            "title": title,
            "description": description,
            "canonical": canonical,
            "h1": h1_instruction(page, subject),
            "imageAltPattern": f"{subject} — Татьяна Мунн, психолог МГУ",
        },
        "jsonLd": page_schema(page, subject, title, description),
        "tildaPlacement": {
            "metadata": "Page Settings -> SEO -> search preview title/description and canonical",
            "headCode": "Page Settings -> Additional -> HTML code for HEAD section",
            "h1": "Page editor: leave exactly one semantic H1",
            "images": "Image/content settings: add SEO alt/title to hero and content images",
        },
        "validationAfterPublish": [
            "Fetch live HTML and verify title/description/canonical.",
            "Verify exactly one H1 where the page template allows it.",
            "Verify one application/ld+json graph is present and JSON is valid.",
            "Re-run scripts/moonn_final_seo_audit.py --production-scope.",
        ],
    }


def write_markdown(payload: dict[str, object]) -> None:
    ready = payload["readyToApply"]
    after_robots = payload["applyAfterRobotsFix"]
    lines = [
        f"# Moonn Production SEO Strengthening Packets — {TODAY}",
        "",
        "Scope: corrected production pages from the saved Moonn rollout set.",
        "",
        "## Summary",
        "",
        f"- Ready to apply now: {len(ready)}",
        f"- Apply after robots fix: {len(after_robots)}",
        "- Live Tilda edits: not performed by this generator.",
        "- Undocumented Tilda endpoints: not used.",
        "",
        "## Ready To Apply",
        "",
    ]
    for packet in ready:
        seo = packet["seo"]
        lines.extend(
            [
                f"### {packet['url']}",
                "",
                f"- Tilda page id: `{packet.get('sourcePageId') or 'unknown'}`",
                f"- Title: `{seo['title']}`",
                f"- Description: `{seo['description']}`",
                f"- Canonical: `{seo['canonical']}`",
                f"- H1 action: `{seo['h1']['action']}` -> `{seo['h1']['targetH1']}`",
                f"- Image alt pattern: `{seo['imageAltPattern']}`",
                "",
            ]
        )
    lines.extend(["## Apply After Robots Fix", ""])
    for packet in after_robots:
        seo = packet["seo"]
        lines.extend(
            [
                f"### {packet['url']}",
                "",
                f"- Tilda page id: `{packet.get('sourcePageId') or 'unknown'}`",
                f"- First fix robots.txt blocking, then apply this same SEO package.",
                f"- Title: `{seo['title']}`",
                f"- Description: `{seo['description']}`",
                f"- Canonical: `{seo['canonical']}`",
                f"- H1 action: `{seo['h1']['action']}` -> `{seo['h1']['targetH1']}`",
                "",
            ]
        )
    MD_OUT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_csv(packets: list[dict[str, object]]) -> None:
    with CSV_OUT.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "applyStatus",
                "kind",
                "url",
                "sourcePageId",
                "title",
                "description",
                "canonical",
                "h1Action",
                "targetH1",
                "imageAltPattern",
                "issues",
            ],
        )
        writer.writeheader()
        for packet in packets:
            seo = packet["seo"]
            writer.writerow(
                {
                    "applyStatus": packet["applyStatus"],
                    "kind": packet["kind"],
                    "url": packet["url"],
                    "sourcePageId": packet.get("sourcePageId", ""),
                    "title": seo["title"],
                    "description": seo["description"],
                    "canonical": seo["canonical"],
                    "h1Action": seo["h1"]["action"],
                    "targetH1": seo["h1"]["targetH1"],
                    "imageAltPattern": seo["imageAltPattern"],
                    "issues": ";".join(packet["currentIssues"]),
                }
            )


def write_robots_packet(after_robots: list[dict[str, object]]) -> None:
    blocked_urls = "\n".join(f"- `{packet['url']}`" for packet in after_robots)
    lines = [
        f"# Moonn Robots Fix Packet — {TODAY}",
        "",
        "## Problem",
        "",
        "The live `robots.txt` contains broad prefix rules such as `Disallow: /psiholog`, which block real published pages that should be indexable.",
        "",
        "Pages to unblock before SEO strengthening:",
        "",
        blocked_urls,
        "",
        "## Safe Change",
        "",
        "Replace broad prefix blocking with exact legacy/test URL blocking only. Keep intentionally closed pages blocked, but do not block semantic service URLs by prefix.",
        "",
        "Current risky rule:",
        "",
        "```txt",
        "Disallow: /psiholog",
        "```",
        "",
        "Recommended direction:",
        "",
        "```txt",
        "# Keep only confirmed legacy/noindex pages closed.",
        "Disallow: /psiholog$",
        "",
        "# Do not block live semantic service pages:",
        "# https://moonn.ru/psiholog-konsultacii-moskva",
        "# https://moonn.ru/psiholog_moskva",
        "# https://moonn.ru/psihology",
        "```",
        "",
        "If Tilda does not support `$` exact matching in its robots editor, remove `Disallow: /psiholog` and keep the legacy page closed via page-level noindex or redirect instead.",
        "",
        "## Validation",
        "",
        "1. Publish robots changes in Tilda.",
        "2. Fetch `https://moonn.ru/robots.txt`.",
        "3. Re-run `python scripts/moonn_final_seo_audit.py --production-scope`.",
        "4. Confirm the three URLs move from `fix_robots_then_strengthen` to `strengthen_seo` or `ok_index`.",
    ]
    ROBOTS_OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    audit = load_json(AUDIT_PATH)
    scope_map = load_scope_map()
    ready: list[dict[str, object]] = []
    after_robots: list[dict[str, object]] = []

    for page in audit["pages"]:
        decision = page.get("decision")
        if decision not in {"strengthen_seo", "fix_robots_then_strengthen"}:
            continue
        scope = scope_map.get(page["url"], {"alias": alias_from_url(page["url"])})
        packet = build_packet(page, scope, apply_after_robots=decision == "fix_robots_then_strengthen")
        if decision == "fix_robots_then_strengthen":
            after_robots.append(packet)
        else:
            ready.append(packet)

    payload = {
        "version": 1,
        "createdAt": datetime.now(timezone.utc).isoformat(),
        "project": "Moonn / Tilda site",
        "workstream": "moonn-production-seo-strengthening",
        "sourceAudit": str(AUDIT_PATH.relative_to(ROOT)),
        "applicationBoundary": {
            "liveTildaEdits": "not_performed_by_this_script",
            "undocumentedTildaEndpoints": "not_used",
            "safeUse": "Use these packets to apply page-specific SEO through supported Tilda UI/head-code fields, then re-audit live HTML.",
        },
        "readyToApply": ready,
        "applyAfterRobotsFix": after_robots,
    }

    JSON_OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(payload)
    write_csv(ready + after_robots)
    write_robots_packet(after_robots)
    print(
        json.dumps(
            {
                "json": str(JSON_OUT),
                "md": str(MD_OUT),
                "csv": str(CSV_OUT),
                "robots": str(ROBOTS_OUT),
                "readyToApply": len(ready),
                "applyAfterRobotsFix": len(after_robots),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
