from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
ASSETS = ROOT / "assets"
AUDIT_PATH = DOCS / "moonn-production-scope-seo-audit-2026-05-07.json"
OUT_JSON = DOCS / "moonn-schema-layer-packet-2026-05-08.json"
OUT_MD = DOCS / "moonn-schema-layer-packet-2026-05-08.md"
OUT_JS = ASSETS / "moonn-schema-layer.js"


PERSON_ID = "https://moonn.ru/#tatiana-munn"
WEBSITE_ID = "https://moonn.ru/#website"
YANDEX_SERVICES_PROFILE_URL = "https://uslugi.yandex.ru/profile/TatyanaKumskovamunn-948629"
YANDEX_SERVICES_REVIEW_URL = YANDEX_SERVICES_PROFILE_URL + "?action=addReview"

PERSON = {
    "@type": "Person",
    "@id": PERSON_ID,
    "name": "Татьяна Мунн",
    "alternateName": [
        "Кумскова Татьяна Михайловна",
        "Татьяна Мунн (Кумскова)",
        "Tatiana Moonn",
        "Tatiana Kumskova",
    ],
    "jobTitle": "Психолог МГУ, эксперт по эмоциональному интеллекту",
    "url": "https://moonn.ru/",
    "sameAs": [
        "https://moonn.ru/",
        "https://moonn.timepad.ru/events/",
        "https://miiiips.ru/author-tatyana-munn-kumskova.html",
        YANDEX_SERVICES_PROFILE_URL,
        "https://istina.msu.ru/workers/816305440/",
        "https://psyjournals.ru/authors/15337",
    ],
    "knowsAbout": [
        "эмоциональный интеллект",
        "психология эмоций",
        "стресс",
        "выгорание",
        "отношения",
        "психология подростков",
        "soft skills",
    ],
}

YANDEX_REVIEW_SUMMARIES = [
    {
        "name": "Отзыв Натальи о консультации",
        "datePublished": "2025-09-10",
        "summary": "Клиентка отмечает, что консультация помогла быстро разобраться с проблемой.",
    },
    {
        "name": "Отзыв Гаянэ о работе с подростком",
        "datePublished": "2025-08-24",
        "summary": "В отзыве описан прогресс подростка после двух встреч и снижение экзаменационного напряжения.",
    },
    {
        "name": "Отзыв Ирины о психологической работе",
        "datePublished": "2025-01-27",
        "summary": "Клиентка отмечает профессионализм, бережную работу с установками и позитивные изменения.",
    },
    {
        "name": "Отзыв Биназир о работе с паническими атаками",
        "datePublished": "2024-10-07",
        "summary": "В отзыве говорится о снижении страха и облегчении после начала работы с паническими атаками.",
    },
    {
        "name": "Отзыв Анны о самооценке и уверенности",
        "datePublished": "2024-09-04",
        "summary": "Клиентка описывает улучшение уверенности, снижение сомнений и более спокойное отношение к себе.",
    },
]

WEBSITE = {
    "@type": "WebSite",
    "@id": WEBSITE_ID,
    "url": "https://moonn.ru/",
    "name": "Татьяна Мунн",
    "alternateName": "Moonn.ru",
    "publisher": {"@id": PERSON_ID},
    "inLanguage": "ru-RU",
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
    "psiholog": "Психолог Татьяна Мунн",
    "psiholog-konsultacii-moskva": "Консультации психолога в Москве и онлайн",
    "psiholog_moskva": "Психолог в Москве",
    "psihology": "Психологическая помощь в Москве и онлайн",
    "articles/eq-dlya-rukovoditeley": "Эмоциональный интеллект руководителя",
    "emotional-intelligence/ei-leader-12": "Эмоциональный интеллект лидера",
    "st1": "Онлайн-тренинг Среда Трансформации",
    "st2": "Онлайн-тренинг Среда Трансформации",
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


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def alias_from_url(url: str) -> str:
    path = urlparse(url).path.lstrip("/")
    if url.endswith("/") and path:
        return path + "/"
    return path


def normalized_path(url: str) -> str:
    path = urlparse(url).path or "/"
    if path != "/" and path.endswith("/"):
        path = path.rstrip("/")
    return path


def compact(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def cleanup_subject(page: dict) -> str:
    alias = alias_from_url(page["url"])
    if alias in MANUAL_SUBJECTS:
        return MANUAL_SUBJECTS[alias]
    if alias in SLUG_WORDS:
        return SLUG_WORDS[alias]
    value = compact(page.get("title") or "")
    for pattern in [
        r"^Статья\s*[-—]\s*",
        r"\|\s*Татьяна\s+Мунн$",
        r"\.\s*Психолог\s+Татьяна\s+Мунн.*$",
        r"\s*Психолог\s+Татьяна\s+Мунн.*$",
        r"\s*Психолог\s+МГУ.*$",
        r"\s*Быстрая\s+Психология.*$",
    ]:
        value = re.sub(pattern, "", value, flags=re.I).strip()
    return value.strip(" .—-") or alias.replace("-", " ").replace("_", " ").strip().capitalize()


def trim(value: str, limit: int) -> str:
    value = compact(value)
    if len(value) <= limit:
        return value
    out: list[str] = []
    for part in value.split():
        candidate = " ".join(out + [part])
        if len(candidate) > limit - 1:
            break
        out.append(part)
    return (" ".join(out) or value[: limit - 1]).rstrip(" ,.;:")


def description(page: dict, subject: str) -> str:
    current = compact(page.get("description") or "")
    if 70 <= len(current) <= 180:
        return current
    kind = page.get("kind")
    short = trim(subject, 72)
    if kind == "service":
        text = f"{short}: консультации Татьяны Мунн, психолога МГУ, в Москве и онлайн."
    elif kind == "lecture_or_events":
        text = f"{short}: лекции и практические материалы Татьяны Мунн по психологии и эмоциональному интеллекту."
    elif kind in {"article", "knowledge_base"}:
        text = f"{short}: материал Татьяны Мунн о психологии эмоций, отношениях, коммуникации и саморегуляции."
    else:
        text = f"{short}: материал Татьяны Мунн, психолога МГУ, о практической психологии и эмоциональном интеллекте."
    return trim(text, 170).rstrip(" ,.;:") + "."


def breadcrumbs(url: str, subject: str) -> dict:
    items = [{"@type": "ListItem", "position": 1, "name": "Главная", "item": "https://moonn.ru/"}]
    if url.rstrip("/") != "https://moonn.ru":
        items.append({"@type": "ListItem", "position": 2, "name": subject, "item": url})
    return {"@type": "BreadcrumbList", "@id": f"{url.rstrip('/')}#breadcrumbs", "itemListElement": items}


def page_graph(page: dict) -> dict:
    url = page["url"].rstrip("/") if page["url"] != "https://moonn.ru/" else page["url"]
    subject = cleanup_subject(page)
    title = compact(page.get("title") or subject)
    desc = description(page, subject)
    kind = page.get("kind")
    graph: list[dict] = [PERSON, WEBSITE]
    web_page = {
        "@type": "WebPage",
        "@id": f"{url.rstrip('/')}#webpage",
        "url": page["url"],
        "name": title,
        "description": desc,
        "isPartOf": {"@id": WEBSITE_ID},
        "about": {"@id": PERSON_ID},
        "author": {"@id": PERSON_ID},
        "inLanguage": "ru-RU",
    }
    graph.append(web_page)
    if kind == "service" or alias_from_url(page["url"]) in {"", "psiholog", "psiholog-konsultacii-moskva", "psiholog_moskva", "psihology"}:
        graph.append(
            {
                "@type": "ProfessionalService",
                "@id": f"{url.rstrip('/')}#service",
                "name": subject,
                "url": page["url"],
                "provider": {"@id": PERSON_ID},
                "areaServed": ["Москва", "Онлайн"],
                "description": desc,
            }
        )
    elif kind in {"article", "knowledge_base"}:
        graph.append(
            {
                "@type": "Article",
                "@id": f"{url.rstrip('/')}#article",
                "headline": title,
                "url": page["url"],
                "description": desc,
                "author": {"@id": PERSON_ID},
                "publisher": {"@id": PERSON_ID},
                "mainEntityOfPage": {"@id": f"{url.rstrip('/')}#webpage"},
                "inLanguage": "ru-RU",
            }
        )
    elif kind == "lecture_or_events":
        graph.append(
            {
                "@type": "ItemList",
                "@id": f"{url.rstrip('/')}#lecture-list",
                "name": subject,
                "url": page["url"],
                "description": desc,
                "itemListElement": [],
            }
        )
    if alias_from_url(page["url"]) == "otzivi":
        web_page["citation"] = [YANDEX_SERVICES_PROFILE_URL]
        graph.append(
            {
                "@type": "ProfilePage",
                "@id": "https://moonn.ru/otzivi#yandex-services-profile",
                "url": YANDEX_SERVICES_PROFILE_URL,
                "name": "Профиль Татьяны Кумсковой (Мунн) на Яндекс Услугах",
                "about": {"@id": PERSON_ID},
                "isPartOf": {
                    "@type": "WebSite",
                    "name": "Яндекс Услуги",
                    "url": "https://uslugi.yandex.ru/",
                },
                "inLanguage": "ru-RU",
            }
        )
        graph.append(
            {
                "@type": "ItemList",
                "@id": "https://moonn.ru/otzivi#verified-yandex-review-summaries",
                "name": "Проверяемые отзывы о Татьяне Мунн с источником на Яндекс Услугах",
                "url": page["url"],
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": index,
                        "url": YANDEX_SERVICES_PROFILE_URL,
                        "item": {
                            "@type": "CreativeWork",
                            "name": item["name"],
                            "datePublished": item["datePublished"],
                            "abstract": item["summary"],
                            "isBasedOn": YANDEX_SERVICES_PROFILE_URL,
                            "about": {"@id": PERSON_ID},
                            "inLanguage": "ru-RU",
                        },
                    }
                    for index, item in enumerate(YANDEX_REVIEW_SUMMARIES, start=1)
                ],
            }
        )
    graph.append(breadcrumbs(page["url"], subject))
    return {"@context": "https://schema.org", "@graph": graph}


def write_js(page_map: dict[str, dict]) -> None:
    payload = json.dumps(page_map, ensure_ascii=False, separators=(",", ":"))
    code = f"""(function(){{
  var MOONN_SCHEMA_MAP = {payload};
  function normalizePath(path) {{
    if (!path) return "/";
    if (path.length > 1 && path.endsWith("/")) return path.slice(0, -1);
    return path;
  }}
  function addJsonLd(data) {{
    if (!data || document.getElementById("moonn-page-schema-jsonld")) return;
    var script = document.createElement("script");
    script.type = "application/ld+json";
    script.id = "moonn-page-schema-jsonld";
    script.text = JSON.stringify(data);
    document.head.appendChild(script);
  }}
  var path = normalizePath(window.location.pathname || "/");
  addJsonLd(MOONN_SCHEMA_MAP[path] || MOONN_SCHEMA_MAP[path + "/"] || MOONN_SCHEMA_MAP["/"]);
}})();
"""
    OUT_JS.write_text(code, encoding="utf-8")


def write_docs(page_map: dict[str, dict], pages: list[dict]) -> None:
    payload = {
        "version": 1,
        "createdAt": datetime.now(timezone.utc).isoformat(),
        "sourceAudit": str(AUDIT_PATH.relative_to(ROOT)),
        "totalPages": len(pages),
        "globalEntitySchema": {"@context": "https://schema.org", "@graph": [PERSON, WEBSITE]},
        "pageSchemaByPath": page_map,
        "applicationBoundary": {
            "liveTildaEdits": "schema layer requires supported global HEAD update and scoped republish",
            "undocumentedTildaEndpoints": "not_used",
            "unsafeContent": "no fake ratings, no private video links, no personal review data",
        },
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Moonn Schema Layer Packet — 2026-05-08",
        "",
        f"- Source audit: `{AUDIT_PATH.relative_to(ROOT)}`",
        f"- Pages covered: `{len(pages)}`",
        "- Schema types: `Person`, `WebSite`, `WebPage`, `ProfilePage`, `ProfessionalService`, `Article`, `ItemList`, `CreativeWork`, `BreadcrumbList`.",
        "- Safety: no fake ratings/prices, no private videos, no payment data; review layer uses source summaries and Yandex profile provenance instead of synthetic aggregate ratings.",
        "",
        "## Paths",
        "",
    ]
    for path, schema in page_map.items():
        graph_types = ", ".join(obj.get("@type", "?") for obj in schema.get("@graph", []))
        lines.append(f"- `{path}`: {graph_types}")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    audit = load_json(AUDIT_PATH)
    pages = [page for page in audit["pages"] if page.get("status") == 200]
    page_map = {normalized_path(page["url"]): page_graph(page) for page in pages}
    write_js(page_map)
    write_docs(page_map, pages)
    print(json.dumps({"pages": len(page_map), "asset": str(OUT_JS), "json": str(OUT_JSON)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
