import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "registry" / "seo" / "moonn-production-73-seo-audit.json"
OUT = ROOT / "registry" / "seo" / "moonn-production-73-schema-snippets.json"

YANDEX_PROFILE_URL = "https://uslugi.yandex.ru/profile/TatyanaKumskovatatyanamunn-948629"


def classify(alias: str, title: str) -> str:
    text = f"{alias} {title}".lower()
    if any(token in text for token in ["event", "lecture", "lekcii", "vystupleniya", "speaker", "seminar", "trening", "kurs", "program"]):
        return "lecture_product"
    if (
        "emotional-intelligence" in text
        or "article" in text
        or "knowledge-base" in text
        or "baza-znaniy" in text
        or any(token in text for token in ["vospitanie", "vigoranie", "trauma", "abuse", "emoci"])
    ):
        return "knowledge_base"
    if any(token in text for token in ["uslugi", "psiholog", "konsultac", "depression", "gtr", "aerofobia", "razvod", "semey"]):
        return "consultation"
    return "general"


def keywords_for(cluster: str, alias: str, title: str) -> list[str]:
    base = ["Татьяна Мунн", "Кумскова Татьяна Михайловна", "психолог МГУ", "Быстрая психология"]
    if cluster == "consultation":
        base += ["психолог Москва", "консультация психолога", "психолог онлайн", "психолог для взрослых и подростков"]
    elif cluster == "lecture_product":
        base += ["лекции по психологии", "эмоциональный интеллект", "soft skills", "тренинг по психологии"]
    elif cluster == "knowledge_base":
        base += ["эмоциональный интеллект", "психология эмоций", "психология состояний", "саморегуляция"]
    else:
        base += ["психология эмоций", "психология состояний", "эмоциональный интеллект"]
    topic = re.sub(r"[-_/]+", " ", alias).strip()
    if topic:
        base.append(topic)
    return list(dict.fromkeys(base))


def breadcrumb_items(url: str) -> list[dict]:
    parts = [part for part in url.replace("https://moonn.ru", "").strip("/").split("/") if part]
    items = [{"@type": "ListItem", "position": 1, "name": "Moonn", "item": "https://moonn.ru/"}]
    current = "https://moonn.ru"
    for index, part in enumerate(parts, start=2):
        current += f"/{part}"
        items.append({"@type": "ListItem", "position": index, "name": part.replace("-", " "), "item": current + ("/" if index == len(parts) + 1 and url.endswith("/") else "")})
    return items


def page_schema(page: dict) -> dict:
    url = page["url"]
    cluster = classify(page["alias"], page["title"])
    person_id = "https://moonn.ru/#tatiana-munn"
    website_id = "https://moonn.ru/#website"
    webpage_id = f"{url.rstrip('/')}/#webpage" if url != "https://moonn.ru/" else "https://moonn.ru/#webpage"
    title = page["title"] or "Татьяна Мунн"
    description = page["description"] or f"{title}. Татьяна Мунн, психолог МГУ, эксперт по эмоциональному интеллекту и быстрой психологии."
    graph = [
        {
            "@type": "WebSite",
            "@id": website_id,
            "url": "https://moonn.ru/",
            "name": "Татьяна Мунн",
            "inLanguage": "ru-RU",
            "publisher": {"@id": person_id},
        },
        {
            "@type": "Person",
            "@id": person_id,
            "name": "Татьяна Мунн",
            "alternateName": ["Татьяна Кумскова", "Кумскова Татьяна Михайловна"],
            "jobTitle": ["психолог", "спикер", "лектор", "эксперт по эмоциональному интеллекту"],
            "url": "https://moonn.ru/",
            "sameAs": [YANDEX_PROFILE_URL],
            "alumniOf": {
                "@type": "CollegeOrUniversity",
                "name": "МГУ имени М. В. Ломоносова, факультет психологии",
                "sameAs": "https://www.msu.ru/",
            },
            "knowsAbout": [
                "эмоциональный интеллект",
                "психология эмоций",
                "психология состояний",
                "консультирование взрослых и подростков",
                "стресс",
                "выгорание",
                "тревожные состояния",
            ],
        },
        {
            "@type": "WebPage",
            "@id": webpage_id,
            "url": url,
            "name": title,
            "description": description,
            "inLanguage": "ru-RU",
            "isPartOf": {"@id": website_id},
            "about": {"@id": person_id},
            "keywords": keywords_for(cluster, page["alias"], page["title"]),
            "mainEntity": {"@id": person_id} if cluster in {"general", "consultation"} else None,
        },
        {
            "@type": "BreadcrumbList",
            "@id": f"{webpage_id}-breadcrumb",
            "itemListElement": breadcrumb_items(url),
        },
    ]
    if cluster == "consultation":
        graph.append(
            {
                "@type": "ProfessionalService",
                "@id": f"{url.rstrip('/')}/#service",
                "name": "Консультация психолога Татьяны Мунн",
                "url": url,
                "provider": {"@id": person_id},
                "areaServed": ["Москва", "Россия", "онлайн"],
                "serviceType": "Психологическая консультация",
                "audience": ["взрослые", "подростки от 12 лет", "семьи"],
            }
        )
    if cluster == "lecture_product":
        graph.append(
            {
                "@type": "Course",
                "@id": f"{url.rstrip('/')}/#course-or-event",
                "name": title,
                "description": description,
                "provider": {"@id": person_id},
                "inLanguage": "ru-RU",
            }
        )
    if cluster == "knowledge_base":
        graph.append(
            {
                "@type": "Article",
                "@id": f"{url.rstrip('/')}/#article",
                "headline": title,
                "description": description,
                "author": {"@id": person_id},
                "publisher": {"@id": person_id},
                "mainEntityOfPage": {"@id": webpage_id},
                "inLanguage": "ru-RU",
            }
        )
    for item in graph:
        for key in [key for key, value in item.items() if value is None]:
            item.pop(key)
    return {"@context": "https://schema.org", "@graph": graph}


def main() -> int:
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    snippets = []
    for page in audit["pages"]:
        schema = page_schema(page)
        marker = f"moonn-seo-schema:{page['source_page_id']}"
        snippet = (
            f"<!-- {marker}:start -->\n"
            '<script type="application/ld+json">\n'
            f"{json.dumps(schema, ensure_ascii=False, indent=2)}\n"
            "</script>\n"
            f"<!-- {marker}:end -->"
        )
        snippets.append(
            {
                "alias": page["alias"],
                "source_page_id": page["source_page_id"],
                "url": page["url"],
                "cluster": classify(page["alias"], page["title"]),
                "marker": marker,
                "snippet": snippet,
            }
        )
    OUT.write_text(json.dumps({"schema_version": "1.0", "source": str(AUDIT.relative_to(ROOT)), "count": len(snippets), "snippets": snippets}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"out": str(OUT.relative_to(ROOT)), "count": len(snippets)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
