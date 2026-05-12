from __future__ import annotations

import csv
import json
import re
from html import escape
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUT = DOCS / "moonn-seo-repositioning-2026-05-12"
TODAY = "2026-05-12"

AUDIT_PATH = DOCS / "moonn-final-seo-audit-2026-05-12.json"
POSITIONING_PATH = DOCS / "moonn-public-positioning-map-2026-05-12.json"
INVENTORY_PATH = DOCS / "moonn-tilda-page-governance-inventory-2026-05-07.json"
PRODUCTION_SCOPE_PATH = ROOT / "output" / "production-73-rollout-pages.json"
PRODUCTION_SCOPE_LOG_PATH = ROOT / "output" / "build-production-83-scope.log"

REGISTER_JSON = OUT / "url-decision-register.json"
REGISTER_CSV = OUT / "url-decision-register.csv"
PACKETS_JSON = OUT / "seo-aeo-tilda-apply-packets.json"
PACKETS_MD = OUT / "seo-aeo-tilda-apply-packets.md"
REINDEX_JSON = OUT / "search-reindex-packet.json"
HOMEPAGE_GATEWAY_HTML = OUT / "homepage-strategic-gateway-tilda-block.html"
SUMMARY_MD = OUT / "implementation-report.md"


ENTITY = {
    "name": "Татьяна Мунн",
    "jobTitle": "Психолог МГУ и эксперт по эмоциональному интеллекту",
    "primaryPositioning": (
        "Татьяна Мунн — психолог МГУ и эксперт по эмоциональному интеллекту: "
        "консультации в Москве и онлайн, работа с тревогой, выгоранием, отношениями, "
        "подростками и экзаменационным стрессом; лекции и программы по эмоциональному интеллекту."
    ),
    "sameAs": [
        "https://moonn.ru/",
        "https://moonn.timepad.ru/events/",
        "https://uslugi.yandex.ru/profile/TatyanaKumskovamunn-948629",
        "https://istina.msu.ru/workers/816305440/",
        "https://psyjournals.ru/authors/15337",
    ],
}

TILDA_API_READONLY_VERIFICATION = {
    "checkedDate": TODAY,
    "projectId": "8326812",
    "projectTitle": "Moonn.ru",
    "pageCountFromApi": 166,
    "verifiedAliases": ["psiholog", "speaker", "psypodgotovka1", "otzivi", "kartiny-tatiany-munn"],
    "officialApiDocs": "https://help.tilda.cc/api",
    "supportedUseInThisPipeline": "read_export_verification",
    "writePathStatus": "blocked_until_supported_nonvisual_write_method_is_verified",
}

PILLARS = {
    "private_practice": "https://moonn.ru/psiholog",
    "emotional_intelligence": "https://moonn.ru/speaker",
    "teen_exam_family": "https://moonn.ru/psypodgotovka1",
    "reviews_trust": "https://moonn.ru/otzivi",
    "secondary": "https://moonn.ru/",
    "archive": "",
}

CLUSTER_TITLES = {
    "private_practice": "Консультации психолога",
    "emotional_intelligence": "Эмоциональный интеллект и выступления",
    "teen_exam_family": "Подростки и экзамены",
    "reviews_trust": "Отзывы и доверие",
    "secondary": "Вторичные публичные страницы",
    "archive": "Архив и исключение из SEO-ядра",
}

PATH_TO_CLUSTER = {
    "/": "secondary",
    "/otzivi": "reviews_trust",
    "/events": "reviews_trust",
    "/events_tp": "reviews_trust",
    "/lectures1": "reviews_trust",
    "/novosti": "reviews_trust",
    "/recomend": "reviews_trust",
    "/20251201": "reviews_trust",
    "/20251213": "reviews_trust",
    "/20251216": "reviews_trust",
    "/novosti20251113": "reviews_trust",
    "/novosti20251118": "reviews_trust",
    "/psiholog": "private_practice",
    "/psiholog-konsultacii-moskva": "private_practice",
    "/psiholog-moskva-online": "private_practice",
    "/psiholog-tatiana-moonn": "private_practice",
    "/trevozhnost": "private_practice",
    "/emotsionalnoe-vygoranie": "private_practice",
    "/otnosheniya-i-granitsy": "private_practice",
    "/samoocenka-i-uverennost": "private_practice",
    "/depressivnoe-sostoyanie": "private_practice",
    "/panicheskie_ataki": "private_practice",
    "/odinochestvo": "private_practice",
    "/abuse_gaslight": "private_practice",
    "/trauma": "private_practice",
    "/semeyniy_psiholog": "private_practice",
    "/semeynie_konflikti_article": "private_practice",
    "/vigoranie_article": "private_practice",
    "/uslugi_aerofobia": "private_practice",
    "/uslugi_depression": "private_practice",
    "/uslugi_fin_blocks": "private_practice",
    "/uslugi_gtr": "private_practice",
    "/uslugi_konflikti_na_rabote": "private_practice",
    "/uslugi_lubovnaya_zavisimost": "private_practice",
    "/uslugi_obida_na_roditelei": "private_practice",
    "/uslugi_otnosheniya_v_kollektive": "private_practice",
    "/uslugi_procrastination": "private_practice",
    "/uslugi_razvod": "private_practice",
    "/uslugi_sohranit_brak": "private_practice",
    "/speaker": "emotional_intelligence",
    "/emotional-intelligence": "emotional_intelligence",
    "/emotional-intelligence/": "emotional_intelligence",
    "/emotional-intelligence/articles": "emotional_intelligence",
    "/emotional-intelligence/articles/benefits-of-ei": "emotional_intelligence",
    "/emotional-intelligence/articles/emotional-intelligence-skills": "emotional_intelligence",
    "/emotional-intelligence/articles/what-is-emotional-intelligence": "emotional_intelligence",
    "/emotional-intelligence/articles/why-ei-matters": "emotional_intelligence",
    "/emotional-intelligence/diagnostoka-ei": "emotional_intelligence",
    "/emotional-intelligence/ei-leader-12": "emotional_intelligence",
    "/emotional-intelligence/knowledge-base": "emotional_intelligence",
    "/emotional-intelligence/knowledge-base/active-listening": "emotional_intelligence",
    "/emotional-intelligence/knowledge-base/assertiveness": "emotional_intelligence",
    "/emotional-intelligence/knowledge-base/burnout": "emotional_intelligence",
    "/emotional-intelligence/knowledge-base/emotional-contagion": "emotional_intelligence",
    "/emotional-intelligence/knowledge-base/emotional-intelligence": "emotional_intelligence",
    "/emotional-intelligence/knowledge-base/emotional-literacy": "emotional_intelligence",
    "/emotional-intelligence/knowledge-base/emotional-maturity": "emotional_intelligence",
    "/emotional-intelligence/knowledge-base/empathy": "emotional_intelligence",
    "/emotional-intelligence/knowledge-base/feedback": "emotional_intelligence",
    "/emotional-intelligence/knowledge-base/intrinsic-motivation": "emotional_intelligence",
    "/emotional-intelligence/knowledge-base/male-loneliness-russia": "emotional_intelligence",
    "/emotional-intelligence/knowledge-base/nonviolent-communication": "emotional_intelligence",
    "/emotional-intelligence/knowledge-base/personal-boundaries": "emotional_intelligence",
    "/emotional-intelligence/knowledge-base/psychological-safety": "emotional_intelligence",
    "/emotional-intelligence/knowledge-base/self-awareness": "emotional_intelligence",
    "/emotional-intelligence/knowledge-base/self-regulation": "emotional_intelligence",
    "/emotional-intelligence/knowledge-base/social-intelligence": "emotional_intelligence",
    "/articles/eq-dlya-rukovoditeley": "emotional_intelligence",
    "/kurs-ei": "emotional_intelligence",
    "/programmakursa": "emotional_intelligence",
    "/platnye-treningi-seminary-programmy-tatiana-moonn": "emotional_intelligence",
    "/vystupleniya-lekcii-treningi-psiholog-tatiana-moonn": "emotional_intelligence",
    "/baza-znaniy-emocionalnyy-intellekt-psihologiya": "emotional_intelligence",
    "/eintellect": "emotional_intelligence",
    "/article_gadget_addiction": "teen_exam_family",
    "/exam-preparation-psychology": "teen_exam_family",
    "/podrostkovyy-lager-psihologiya": "teen_exam_family",
    "/psypodgotovka1": "teen_exam_family",
    "/uslugi_podrostki": "teen_exam_family",
    "/vospitanie_article": "teen_exam_family",
    "/shppp333": "teen_exam_family",
    "/kartiny-tatiany-munn": "secondary",
    "/call": "secondary",
    "/offer": "secondary",
    "/pay-good-moon": "secondary",
    "/politic": "secondary",
}

REDIRECT_TARGETS = {
    "/eintellect": "https://moonn.ru/emotional-intelligence/",
    "/baza-znaniy-emocionalnyy-intellekt-psihologiya": "https://moonn.ru/emotional-intelligence/knowledge-base",
    "/programmakursa": "https://moonn.ru/kurs-ei",
    "/psiholog_moskva": "https://moonn.ru/psiholog",
    "/psihology": "https://moonn.ru/psiholog",
    "/tatiana_moonn369": "https://moonn.ru/psiholog",
    "/seminar555": "https://moonn.ru/events",
    "/vecherinka369": "https://moonn.ru/events",
    "/page44456533.html": "https://moonn.ru/uslugi_podrostki",
    "/page44458639.html": "https://moonn.ru/uslugi_podrostki",
    "/page44459247.html": "https://moonn.ru/psiholog",
    "/page44551635.html": "https://moonn.ru/psypodgotovka1",
    "/page44681917.html": "https://moonn.ru/psiholog",
    "/page45296765.html": "https://moonn.ru/podrostkovyy-lager-psihologiya",
    "/page45326465.html": "https://moonn.ru/podrostkovyy-lager-psihologiya",
    "/page62970147.html": "https://moonn.ru/article_diary_of_emotions",
    "/st1": "https://moonn.ru/events",
    "/st2": "https://moonn.ru/events",
}

FORCE_NOINDEX = {
    "/selfharm",
    "/aromatherapy",
    "/microbiom",
    "/water",
    "/salt",
    "/vacuum_cups",
    "/phytotherapy",
    "/geshtalt",
    "/kpt",
    "/schematherapy",
    "/psychoanalys",
    "/psy4psy",
    "/test77",
}

PAGE_TITLES = {
    "/": "Татьяна Мунн — психолог МГУ и эксперт по эмоциональному интеллекту",
    "/psiholog": "Психолог в Москве и онлайн — Татьяна Мунн",
    "/speaker": "Спикер по эмоциональному интеллекту — Татьяна Мунн",
    "/emotional-intelligence": "Эмоциональный интеллект — Татьяна Мунн",
    "/emotional-intelligence/": "Эмоциональный интеллект — Татьяна Мунн",
    "/psypodgotovka1": "Психологическая подготовка к ОГЭ и ЕГЭ — Татьяна Мунн",
    "/otzivi": "Отзывы о психологе Татьяне Мунн — проверяемые источники",
    "/kartiny-tatiany-munn": "Картины Татьяны Мунн — 3D-галерея и персональный код",
}

PAGE_H1 = {
    "/": "Татьяна Мунн — психолог МГУ и эксперт по эмоциональному интеллекту",
    "/psiholog": "Психолог в Москве и онлайн: консультации Татьяны Мунн",
    "/speaker": "Эмоциональный интеллект, лекции и выступления Татьяны Мунн",
    "/emotional-intelligence": "Эмоциональный интеллект: статьи, практики и обучение",
    "/emotional-intelligence/": "Эмоциональный интеллект: статьи, практики и обучение",
    "/psypodgotovka1": "Психологическая подготовка к экзаменам без паники",
    "/otzivi": "Отзывы о психологе Татьяне Мунн из проверяемых источников",
    "/kartiny-tatiany-munn": "Картины Татьяны Мунн: 3D-галерея и персональный код",
}

KNOWN_TILDA_PAGE_IDS = {
    "/": "42678538",
    "/kartiny-tatiany-munn": "140864526",
    "/otzivi": "81167556",
    "/podrostkovyy-lager-psihologiya": "140348786",
    "/psiholog": "114846506",
    "/psypodgotovka1": "62652841",
    "/speaker": "87231366",
}


def load_json(path: Path) -> dict | list:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_path(url_or_path: str) -> str:
    if url_or_path.startswith("http"):
        path = urlparse(url_or_path).path or "/"
    else:
        path = url_or_path or "/"
    if path != "/" and path.endswith("/"):
        path = path.rstrip("/")
    return path


def alias_from_path(path: str) -> str:
    return "" if path == "/" else path.lstrip("/")


def page_id_from_path(path: str) -> str:
    match = re.fullmatch(r"/page(\d+)\.html", path)
    if match:
        return match.group(1)
    return ""


def trim_words(value: str, limit: int) -> str:
    value = re.sub(r"\s+", " ", value or "").strip()
    if len(value) <= limit:
        return value
    parts = value.split()
    out: list[str] = []
    for part in parts:
        candidate = " ".join(out + [part])
        if len(candidate) > limit - 1:
            break
        out.append(part)
    return (" ".join(out) or value[: limit - 1]).rstrip(" ,.;:")


def sentence(value: str, limit: int = 158) -> str:
    value = trim_words(value, limit).rstrip(" ,.;:")
    if value and value[-1] not in ".!?":
        value += "."
    return value


def title_from_slug(path: str, fallback: str) -> str:
    if path in PAGE_TITLES:
        return PAGE_TITLES[path]
    cleaned = re.sub(r"\s+", " ", fallback or "").strip()
    for pattern in [
        r"\|\s*Татьяна\s+Мунн.*$",
        r"\s*[-—]\s*Татьяна\s+Мунн.*$",
        r"\s*Психолог\s+Татьяна\s+Мунн.*$",
        r"\s*психолог\s+Татьяна\s+Мунн.*$",
        r"\s*Психолог\s+МГУ.*$",
        r"\s*\(высокий рейтинг.*$",
    ]:
        cleaned = re.sub(pattern, "", cleaned, flags=re.I).strip()
    if not cleaned:
        cleaned = alias_from_path(path).replace("-", " ").replace("_", " ").capitalize()
    suffix = " — Татьяна Мунн"
    return trim_words(cleaned + suffix, 68)


def h1_for(path: str, title: str) -> str:
    if path in PAGE_H1:
        return PAGE_H1[path]
    return trim_words(re.sub(r"\s+[|—-]\s*Татьяна\s+Мунн.*$", "", title).strip(), 82)


def description_for(path: str, cluster: str, h1: str) -> str:
    if path == "/":
        return "Татьяна Мунн, психолог МГУ: консультации в Москве и онлайн, эмоциональный интеллект, подростки, экзамены, отзывы и запись."
    if cluster == "private_practice":
        return sentence(f"{h1}: консультации психолога Татьяны Мунн в Москве и онлайн без медицинских обещаний, с фокусом на эмоции, тревогу, отношения и устойчивость.")
    if cluster == "emotional_intelligence":
        return sentence(f"{h1}: лекции, статьи и программы Татьяны Мунн по эмоциональному интеллекту, саморегуляции, soft skills и устойчивости команд.")
    if cluster == "teen_exam_family":
        return sentence(f"{h1}: психологическая поддержка подростков, студентов и родителей при тревоге, экзаменах, общении и учебной нагрузке.")
    if cluster == "reviews_trust":
        return sentence(f"{h1}: подтверждения опыта Татьяны Мунн, отзывы, мероприятия, лекции и внешние источники для проверки.")
    if cluster == "secondary":
        return sentence(f"{h1}: публичная сервисная страница проекта Татьяны Мунн без статуса основного SEO-направления.")
    return sentence(f"{h1}: архивная страница проекта Татьяны Мунн, не используемая как основное SEO-направление.")


def load_tilda_ids() -> dict[str, dict[str, str]]:
    mapping: dict[str, dict[str, str]] = {}
    if INVENTORY_PATH.exists():
        inventory = load_json(INVENTORY_PATH)
        for item in inventory.get("items", []):
            path = normalize_path(item.get("url") or ("/" + str(item.get("alias") or "")))
            mapping[path] = {
                "page_id": str(item.get("id") or ""),
                "alias": str(item.get("alias") or ""),
                "published": str(bool(item.get("published"))).lower(),
                "inventory_decision": str(item.get("decision") or ""),
            }
    for path in (PRODUCTION_SCOPE_PATH, PRODUCTION_SCOPE_LOG_PATH):
        if not path.exists():
            continue
        data = load_json(path)
        items = data.get("additions", []) if isinstance(data, dict) else data
        for item in items:
            alias = str(item.get("alias") or "")
            production_url = str(item.get("production_url") or "")
            url_path = normalize_path(production_url or ("/" + alias))
            mapping.setdefault(url_path, {})
            mapping[url_path].update(
                {
                    "page_id": str(item.get("source_page_id") or mapping[url_path].get("page_id", "")),
                    "alias": alias,
                    "published": str(bool(item.get("published", True))).lower(),
                    "inventory_decision": str(item.get("scope_source") or mapping[url_path].get("inventory_decision", "")),
                }
            )
    return mapping


def schema_types_for(cluster: str, action: str, path: str, kind: str) -> list[str]:
    if action in {"noindex", "remove_from_sitemap"}:
        return []
    base = ["Person", "WebSite", "WebPage", "BreadcrumbList"]
    if cluster == "private_practice" or path == "/psiholog":
        base.append("ProfessionalService")
    if cluster == "reviews_trust" and path == "/otzivi":
        base.extend(["ProfilePage", "ItemList"])
    if cluster == "reviews_trust" and kind == "lecture_or_events":
        base.append("Event")
    if kind in {"article", "knowledge_base"} or path.startswith("/emotional-intelligence/knowledge-base"):
        base.append("Article")
    return sorted(set(base), key=base.index)


def risk_flags_for(path: str, cluster: str, issues: list[str], action: str) -> list[str]:
    flags: list[str] = []
    if path in FORCE_NOINDEX:
        flags.append("deindex_until_rewritten")
    if path == "/selfharm":
        flags.append("safety_legal_rewrite_required")
    if path in {"/aromatherapy", "/microbiom", "/water", "/salt", "/vacuum_cups", "/phytotherapy"}:
        flags.append("offtopic_entity_dilution")
    if cluster == "private_practice" and path in {"/panicheskie_ataki", "/depressivnoe-sostoyanie", "/uslugi_depression", "/selfharm"}:
        flags.append("medical_adjacent_claims")
    if "multiple_h1" in issues:
        flags.append("multiple_h1")
    if "missing_h1" in issues:
        flags.append("missing_h1")
    if "opaque_or_test_slug" in issues:
        flags.append("opaque_or_test_slug")
    if action == "redirect":
        flags.append("canonical_consolidation")
    return flags


def action_for(path: str, positioning_action: str, issues: list[str]) -> str:
    if path in REDIRECT_TARGETS:
        return "redirect"
    if path in FORCE_NOINDEX:
        return "noindex"
    if positioning_action == "redirect_or_deindex":
        return "noindex"
    if positioning_action == "deindex_or_archive":
        return "noindex"
    if "opaque_or_test_slug" in issues:
        return "noindex"
    if positioning_action in {"public_core", "public_support", "review"}:
        return "rewrite"
    if positioning_action == "public_keep_no_seo":
        return "keep_indexed"
    return "rewrite"


def build_register() -> list[dict[str, object]]:
    audit = {item["url"]: item for item in load_json(AUDIT_PATH)["pages"]}
    positioning = load_json(POSITIONING_PATH)["pages"]
    tilda_ids = load_tilda_ids()
    rows: list[dict[str, object]] = []
    for item in positioning:
        url = str(item["url"])
        path = normalize_path(url)
        audit_item = audit.get(url, {})
        issues = list(audit_item.get("issues") or [])
        cluster = PATH_TO_CLUSTER.get(path)
        if not cluster:
            old_cluster = str(item.get("cluster") or "")
            cluster = {
                "emotional_intelligence_leadership": "emotional_intelligence",
                "private_practice_support": "private_practice",
                "content_support": "private_practice",
                "teen_exam_family": "teen_exam_family",
                "trust_entity": "reviews_trust",
                "secondary_brand_product": "secondary",
                "legal_or_transactional": "secondary",
                "offtopic_wellness_archive": "archive",
                "closed_or_opaque": "archive",
            }.get(old_cluster, "secondary")
        action = action_for(path, str(item.get("action") or ""), issues)
        canonical_target = REDIRECT_TARGETS.get(path) if action == "redirect" else url
        if action == "noindex":
            canonical_target = ""
        pillar_url = PILLARS.get(cluster, "")
        title = title_from_slug(path, str(audit_item.get("title") or item.get("title") or ""))
        h1 = h1_for(path, title)
        description = description_for(path, cluster, h1)
        schema_types = schema_types_for(cluster, action, path, str(audit_item.get("kind") or item.get("kind") or ""))
        id_info = tilda_ids.get(path, {})
        page_id = id_info.get("page_id", "") or KNOWN_TILDA_PAGE_IDS.get(path, "") or page_id_from_path(path)
        rows.append(
            {
                "url": url,
                "path": path,
                "alias": id_info.get("alias", alias_from_path(path)),
                "page_id": page_id,
                "cluster": cluster,
                "cluster_title": CLUSTER_TITLES.get(cluster, cluster),
                "action": action,
                "canonical_target": canonical_target,
                "pillar_url": pillar_url,
                "title": title,
                "description": description,
                "h1": h1,
                "schema_types": schema_types,
                "risk_flags": risk_flags_for(path, cluster, issues, action),
                "issues": issues,
                "verification_status": "packet_ready",
                "source_kind": audit_item.get("kind") or item.get("kind") or "",
            }
        )
    rows.sort(key=lambda row: str(row["path"]))
    return rows


def jsonld_for(row: dict[str, object]) -> dict[str, object] | None:
    if row["action"] in {"noindex", "remove_from_sitemap"}:
        return None
    url = str(row["url"])
    page_id = url.rstrip("/") if url != "https://moonn.ru/" else "https://moonn.ru"
    person = {
        "@type": "Person",
        "@id": "https://moonn.ru/#tatiana-munn",
        "name": ENTITY["name"],
        "alternateName": ["Кумскова Татьяна Михайловна", "Татьяна Мунн (Кумскова)", "Tatiana Moonn"],
        "jobTitle": ENTITY["jobTitle"],
        "url": "https://moonn.ru/",
        "sameAs": ENTITY["sameAs"],
        "knowsAbout": [
            "эмоциональный интеллект",
            "психология эмоций",
            "тревога",
            "выгорание",
            "отношения",
            "подростковая психология",
            "экзаменационный стресс",
        ],
    }
    graph: list[dict[str, object]] = [
        person,
        {
            "@type": "WebSite",
            "@id": "https://moonn.ru/#website",
            "url": "https://moonn.ru/",
            "name": "Татьяна Мунн",
            "publisher": {"@id": "https://moonn.ru/#tatiana-munn"},
            "inLanguage": "ru-RU",
        },
        {
            "@type": "WebPage",
            "@id": f"{page_id}#webpage",
            "url": url,
            "name": row["title"],
            "description": row["description"],
            "isPartOf": {"@id": "https://moonn.ru/#website"},
            "about": {"@id": "https://moonn.ru/#tatiana-munn"},
            "author": {"@id": "https://moonn.ru/#tatiana-munn"},
            "inLanguage": "ru-RU",
        },
    ]
    if "ProfessionalService" in row["schema_types"]:
        graph.append(
            {
                "@type": "ProfessionalService",
                "@id": f"{page_id}#service",
                "name": row["h1"],
                "url": url,
                "provider": {"@id": "https://moonn.ru/#tatiana-munn"},
                "areaServed": ["Москва", "Онлайн"],
                "description": row["description"],
            }
        )
    if "ProfilePage" in row["schema_types"]:
        graph.append(
            {
                "@type": "ProfilePage",
                "@id": f"{page_id}#profile",
                "url": url,
                "mainEntity": {"@id": "https://moonn.ru/#tatiana-munn"},
                "description": "Отзывы и внешние источники о работе психолога Татьяны Мунн.",
            }
        )
    if "ItemList" in row["schema_types"]:
        graph.append(
            {
                "@type": "ItemList",
                "@id": f"{page_id}#verified-review-sources",
                "name": "Проверяемые источники отзывов о Татьяне Мунн",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Яндекс Услуги",
                        "url": "https://uslugi.yandex.ru/profile/TatyanaKumskovamunn-948629",
                    }
                ],
            }
        )
    if "Article" in row["schema_types"]:
        graph.append(
            {
                "@type": "Article",
                "@id": f"{page_id}#article",
                "headline": row["h1"],
                "url": url,
                "author": {"@id": "https://moonn.ru/#tatiana-munn"},
                "publisher": {"@id": "https://moonn.ru/#tatiana-munn"},
                "mainEntityOfPage": {"@id": f"{page_id}#webpage"},
                "inLanguage": "ru-RU",
            }
        )
    graph.append(
        {
            "@type": "BreadcrumbList",
            "@id": f"{page_id}#breadcrumbs",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Главная", "item": "https://moonn.ru/"},
                {"@type": "ListItem", "position": 2, "name": row["h1"], "item": url},
            ]
            if row["path"] != "/"
            else [{"@type": "ListItem", "position": 1, "name": "Главная", "item": "https://moonn.ru/"}],
        }
    )
    return {"@context": "https://schema.org", "@graph": graph}


def answer_block_for(row: dict[str, object]) -> dict[str, str] | None:
    if row["action"] in {"noindex", "remove_from_sitemap", "redirect"}:
        return None
    cluster = row["cluster"]
    if cluster == "private_practice":
        answer = "Консультация помогает разобраться с эмоциональным состоянием, тревогой, выгоранием или отношениями; медицинские вопросы и лекарства обсуждаются с врачом."
    elif cluster == "emotional_intelligence":
        answer = "Эмоциональный интеллект помогает распознавать эмоции, регулировать состояние, общаться яснее и сохранять устойчивость в работе и отношениях."
    elif cluster == "teen_exam_family":
        answer = "Психологическая подготовка помогает подростку или студенту снизить тревогу, вернуть концентрацию и пройти период экзаменов спокойнее."
    elif cluster == "reviews_trust":
        answer = "Отзывы и внешние профили помогают проверить опыт специалиста до записи на консультацию, лекцию или программу."
    else:
        return None
    return {"heading": row["h1"], "answer": answer}


def build_packets(rows: list[dict[str, object]]) -> dict[str, object]:
    seo_packets = []
    noindex_queue = []
    redirect_queue = []
    schema_map = {}
    answer_blocks = {}
    for row in rows:
        action = str(row["action"])
        packet = {
            "url": row["url"],
            "path": row["path"],
            "page_id": row["page_id"],
            "cluster": row["cluster"],
            "action": action,
            "title": row["title"],
            "description": row["description"],
            "canonical": row["canonical_target"],
            "h1": row["h1"],
            "schema_types": row["schema_types"],
            "risk_flags": row["risk_flags"],
        }
        if action in {"rewrite", "keep_indexed"}:
            seo_packets.append(packet)
            schema = jsonld_for(row)
            if schema:
                schema_map[row["path"]] = schema
            answer_block = answer_block_for(row)
            if answer_block:
                answer_blocks[row["path"]] = answer_block
        elif action == "redirect":
            redirect_queue.append({"from": row["url"], "to": row["canonical_target"], "page_id": row["page_id"]})
        elif action == "noindex":
            noindex_queue.append({"url": row["url"], "path": row["path"], "page_id": row["page_id"], "reason": row["risk_flags"]})
    return {
        "createdDate": TODAY,
        "entity": ENTITY,
        "seoPackets": seo_packets,
        "schemaMap": schema_map,
        "answerBlocks": answer_blocks,
        "tildaApplyQueue": {
            "seoSettings": seo_packets,
            "redirects": redirect_queue,
            "noindexPages": noindex_queue,
            "homepageGatewayBlock": HOMEPAGE_GATEWAY_HTML.relative_to(ROOT).as_posix(),
        },
        "verificationGates": [
            "register_has_no_review_action",
            "generators_are_deterministic",
            "no_secret_or_local_path_in_artifacts",
            "live_raw_html_one_h1_for_home_and_pillars",
            "sitemap_excludes_opaque_test_urls",
            "canonical_matches_register",
            "rendered_homepage_routes_visible",
        ],
        "tildaApiReadOnlyVerification": TILDA_API_READONLY_VERIFICATION,
    }


def write_homepage_gateway() -> None:
    cards = [
        ("Консультации", "Тревога, выгорание, отношения, самооценка и эмоциональные состояния.", "/psiholog"),
        ("Эмоциональный интеллект", "Лекции, выступления и программы для людей, лидеров и команд.", "/speaker"),
        ("Подростки и экзамены", "Поддержка подростков, студентов и родителей в период нагрузки и экзаменов.", "/psypodgotovka1"),
        ("Отзывы и доверие", "Проверяемые отзывы, внешние профили, лекции и публичная активность.", "/otzivi"),
    ]
    card_html = "\n".join(
        f"""    <a class="moonn-route-card" href="{href}">
      <span>{escape(title)}</span>
      <small>{escape(text)}</small>
    </a>"""
        for title, text, href in cards
    )
    html = f"""<section id="moonn-strategic-gateway" data-moonn-seo-repositioning="2026-05-12">
  <style>
    #moonn-strategic-gateway{{font-family:Inter,Arial,sans-serif;background:#fff;padding:56px 20px 48px;color:#231a2f}}
    #moonn-strategic-gateway .wrap{{max-width:1160px;margin:0 auto}}
    #moonn-strategic-gateway h1{{margin:0 0 18px;font-size:clamp(34px,5vw,68px);line-height:1.02;color:#5220b8;letter-spacing:0}}
    #moonn-strategic-gateway p{{margin:0;max-width:780px;font-size:19px;line-height:1.55;color:#4d4258}}
    #moonn-strategic-gateway .routes{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px;margin-top:30px}}
    #moonn-strategic-gateway .moonn-route-card{{display:flex;flex-direction:column;gap:10px;min-height:138px;padding:20px;border:1px solid #e8ddff;border-radius:8px;text-decoration:none;background:#fbf9ff;color:#2e2440;box-shadow:0 12px 28px rgba(82,32,184,.08)}}
    #moonn-strategic-gateway .moonn-route-card span{{font-size:20px;font-weight:850;color:#5220b8}}
    #moonn-strategic-gateway .moonn-route-card small{{font-size:14px;line-height:1.45;color:#5b5268}}
    @media(max-width:860px){{#moonn-strategic-gateway .routes{{grid-template-columns:1fr 1fr}}}}
    @media(max-width:560px){{#moonn-strategic-gateway{{padding:38px 16px}}#moonn-strategic-gateway .routes{{grid-template-columns:1fr}}#moonn-strategic-gateway p{{font-size:17px}}}}
  </style>
  <div class="wrap">
    <h1>{escape(PAGE_H1["/"])}</h1>
    <p>{escape(ENTITY["primaryPositioning"])}</p>
    <div class="routes">
{card_html}
    </div>
  </div>
</section>
"""
    HOMEPAGE_GATEWAY_HTML.write_text(html, encoding="utf-8")


def write_register(rows: list[dict[str, object]]) -> None:
    payload = {
        "createdDate": TODAY,
        "source": {
            "audit": AUDIT_PATH.relative_to(ROOT).as_posix(),
            "positioningMap": POSITIONING_PATH.relative_to(ROOT).as_posix(),
            "tildaInventory": INVENTORY_PATH.relative_to(ROOT).as_posix(),
        },
        "allowedActions": ["keep_indexed", "rewrite", "redirect", "noindex", "remove_from_sitemap"],
        "clusters": list(PILLARS),
        "pages": rows,
    }
    REGISTER_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    fields = [
        "url",
        "alias",
        "page_id",
        "cluster",
        "action",
        "canonical_target",
        "pillar_url",
        "title",
        "description",
        "h1",
        "schema_types",
        "risk_flags",
        "verification_status",
    ]
    with REGISTER_CSV.open("w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: "; ".join(row[key]) if isinstance(row.get(key), list) else row.get(key, "") for key in fields})


def write_packets(packets: dict[str, object], rows: list[dict[str, object]]) -> None:
    PACKETS_JSON.write_text(json.dumps(packets, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    reindex = {
        "createdDate": TODAY,
        "submitToSearchConsolesAfterLiveApply": [row["url"] for row in rows if row["action"] in {"rewrite", "keep_indexed"}],
        "removeOrInspect": [row["url"] for row in rows if row["action"] in {"redirect", "noindex", "remove_from_sitemap"}],
        "notes": [
            "Submit only after Tilda live verification passes.",
            "Do not request indexing for noindex/archive/legal transaction pages.",
        ],
    }
    REINDEX_JSON.write_text(json.dumps(reindex, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    summary = {
        "rewrite": sum(1 for row in rows if row["action"] == "rewrite"),
        "keep_indexed": sum(1 for row in rows if row["action"] == "keep_indexed"),
        "redirect": sum(1 for row in rows if row["action"] == "redirect"),
        "noindex": sum(1 for row in rows if row["action"] == "noindex"),
        "remove_from_sitemap": sum(1 for row in rows if row["action"] == "remove_from_sitemap"),
    }
    lines = [
        "# Moonn SEO/AEO/Tilda Apply Packets — 2026-05-12",
        "",
        "## Summary",
        "",
        f"- Rewrite packets: `{summary['rewrite']}`",
        f"- Keep indexed packets: `{summary['keep_indexed']}`",
        f"- Redirects: `{summary['redirect']}`",
        f"- Noindex/archive pages: `{summary['noindex']}`",
        f"- Register: `{REGISTER_JSON.relative_to(ROOT).as_posix()}`",
        f"- Homepage gateway block: `{HOMEPAGE_GATEWAY_HTML.relative_to(ROOT).as_posix()}`",
        "",
        "## Live Apply Gate",
        "",
        "- Tilda API read-only was verified for project `8326812` (`Moonn.ru`) and returned `166` pages.",
        "- Official Tilda API documentation exposes read/export requests used for synchronization; a supported non-visual bulk write/edit method for page SEO or blocks is not proven in this repository.",
        "- Apply order: redirects/noindex, robots/canonical, homepage gateway, core pillars, support pages, schema layer, sitemap/reindex.",
        "- Do not use visible Chrome for bulk work unless explicitly accepted as a temporary high-risk path.",
        "- If non-visual Tilda write access is unavailable, stop after these packets and record the blocker.",
        "",
        "## First Core Pages",
        "",
    ]
    for row in rows:
        if row["path"] in {"/", "/psiholog", "/speaker", "/emotional-intelligence", "/psypodgotovka1", "/otzivi"}:
            lines.append(f"- `{row['path']}` — `{row['action']}` / `{row['cluster']}` / H1: `{row['h1']}`")
    PACKETS_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def validate(rows: list[dict[str, object]], packets: dict[str, object]) -> None:
    bad = [row["url"] for row in rows if row["action"] == "review"]
    if bad:
        raise RuntimeError(f"Register still has review actions: {bad[:10]}")
    allowed = {"keep_indexed", "rewrite", "redirect", "noindex", "remove_from_sitemap"}
    bad_actions = sorted({str(row["action"]) for row in rows if row["action"] not in allowed})
    if bad_actions:
        raise RuntimeError(f"Unknown actions: {bad_actions}")
    for row in rows:
        if row["action"] in {"rewrite", "keep_indexed", "redirect"} and not row["page_id"]:
            raise RuntimeError(f"Missing page_id for actionable page: {row['url']}")
    schema_map = packets["schemaMap"]
    if "/otzivi" in schema_map:
        raw = json.dumps(schema_map["/otzivi"], ensure_ascii=False)
        if "AggregateRating" in raw:
            raise RuntimeError("Reviews schema must not include AggregateRating")


def write_summary(rows: list[dict[str, object]], packets: dict[str, object]) -> None:
    clusters: dict[str, int] = {}
    actions: dict[str, int] = {}
    for row in rows:
        clusters[str(row["cluster"])] = clusters.get(str(row["cluster"]), 0) + 1
        actions[str(row["action"])] = actions.get(str(row["action"]), 0) + 1
    lines = [
        "# Moonn SEO Repositioning Implementation Report — 2026-05-12",
        "",
        "## What Changed",
        "",
        "- Added a canonical URL decision register for all audited public URLs.",
        "- Generated SEO packets, AEO answer blocks, schema map and Tilda apply queue from the register.",
        "- Generated a one-H1 homepage strategic gateway block with four routes.",
        "- Generated a search reindex packet for GSC/Yandex follow-up after live apply.",
        "",
        "## Counts",
        "",
    ]
    for action, count in sorted(actions.items()):
        lines.append(f"- `{action}`: `{count}`")
    lines.extend(["", "## Clusters", ""])
    for cluster, count in sorted(clusters.items()):
        lines.append(f"- `{cluster}`: `{count}`")
    lines.extend(
        [
            "",
            "## Non-Visual Live Apply Status",
            "",
            "Prepared but not applied live in this generator. Read-only Tilda API access was verified for project `8326812` (`Moonn.ru`) and returned `166` pages. Existing project scripts for Tilda bulk writes use visible Google Chrome UI. The official Tilda API documentation currently supports synchronization/export requests; a non-visual write-capable Tilda path still needs verification before mass publication.",
            "",
            "## Artifacts",
            "",
            f"- `{REGISTER_JSON.relative_to(ROOT).as_posix()}`",
            f"- `{PACKETS_JSON.relative_to(ROOT).as_posix()}`",
            f"- `{PACKETS_MD.relative_to(ROOT).as_posix()}`",
            f"- `{REINDEX_JSON.relative_to(ROOT).as_posix()}`",
            f"- `{HOMEPAGE_GATEWAY_HTML.relative_to(ROOT).as_posix()}`",
        ]
    )
    SUMMARY_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = build_register()
    packets = build_packets(rows)
    validate(rows, packets)
    write_homepage_gateway()
    write_register(rows)
    write_packets(packets, rows)
    write_summary(rows, packets)
    print(
        json.dumps(
            {
                "ok": True,
                "out": OUT.relative_to(ROOT).as_posix(),
                "pages": len(rows),
                "rewrite": sum(1 for row in rows if row["action"] == "rewrite"),
                "redirect": sum(1 for row in rows if row["action"] == "redirect"),
                "noindex": sum(1 for row in rows if row["action"] == "noindex"),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
