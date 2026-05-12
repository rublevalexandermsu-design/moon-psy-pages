from __future__ import annotations

import csv
import json
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-05-12"
AUDIT_PATH = ROOT / "docs" / f"moonn-final-seo-audit-{TODAY}.json"
MAP_JSON = ROOT / "docs" / f"moonn-public-positioning-map-{TODAY}.json"
MAP_CSV = ROOT / "docs" / f"moonn-public-positioning-map-{TODAY}.csv"
STRATEGY_MD = ROOT / "docs" / f"moonn-positioning-architecture-{TODAY}.md"


CORE_PRIVATE_PRACTICE = {
    "/psiholog",
    "/psiholog-moskva-online",
    "/psiholog-konsultacii-moskva",
    "/psiholog-tatiana-moonn",
    "/trevozhnost",
    "/emotsionalnoe-vygoranie",
    "/otnosheniya-i-granitsy",
    "/samoocenka-i-uverennost",
    "/depressivnoe-sostoyanie",
    "/panicheskie_ataki",
}

PRIVATE_SUPPORT = {
    "/uslugi_gtr",
    "/uslugi_depression",
    "/uslugi_lubovnaya_zavisimost",
    "/uslugi_razvod",
    "/uslugi_sohranit_brak",
    "/uslugi_procrastination",
    "/uslugi_obida_na_roditelei",
    "/uslugi_konflikti_na_rabote",
    "/uslugi_otnosheniya_v_kollektive",
    "/uslugi_fin_blocks",
    "/uslugi_aerofobia",
    "/abuse_gaslight",
    "/trauma",
    "/semeyniy_psiholog",
    "/semeynie_konflikti_article",
    "/vigoranie_article",
}

EI_CORE = {
    "/speaker",
    "/emotional-intelligence",
    "/emotional-intelligence/",
    "/kurs-ei",
    "/articles/eq-dlya-rukovoditeley",
    "/vystupleniya-lekcii-treningi-psiholog-tatiana-moonn",
    "/platnye-treningi-seminary-programmy-tatiana-moonn",
}

TEEN_EXAM_CORE = {
    "/podrostkovyy-lager-psihologiya",
    "/psypodgotovka1",
    "/exam-preparation-psychology",
    "/uslugi_podrostki",
    "/article_gadget_addiction",
    "/vospitanie_article",
}

TRUST_ENTITY = {
    "/",
    "/otzivi",
    "/events",
    "/events_tp",
    "/lectures1",
    "/novosti",
    "/shkolapsihologii",
}

NON_CORE_PUBLIC = {
    "/kartiny-tatiany-munn",
    "/call",
    "/pay-good-moon",
    "/offer",
    "/politic",
}

FRINGE_OR_OFFTOPIC = {
    "/aromatherapy",
    "/microbiom",
    "/phytotherapy",
    "/salt",
    "/water",
    "/vacuum_cups",
    "/geshtalt",
    "/kpt",
    "/schematherapy",
    "/psychoanalys",
    "/psy4psy",
}


def normalize_path(url: str) -> str:
    path = urlparse(url).path or "/"
    if len(path) > 1 and path.endswith("/"):
        return path[:-1]
    return path


def classify_url(item: dict[str, object]) -> tuple[str, str, str]:
    path = normalize_path(str(item["url"]))
    issues = set(item.get("issues") or [])
    kind = str(item.get("kind") or "")

    if kind in {"numeric_page", "test_or_staging"} or re.fullmatch(r"/page\d+\.html", path):
        return "redirect_or_deindex", "closed_or_opaque", "Opaque/test URL; do not use for positioning."
    if path in {"/offer", "/politic", "/pay-good-moon", "/call"}:
        return "public_keep_no_seo", "legal_or_transactional", "Keep accessible, exclude from positioning."
    if path in FRINGE_OR_OFFTOPIC:
        return "deindex_or_archive", "offtopic_wellness_archive", "Weakens psychology/EI entity; move out of main index unless rewritten with evidence and boundaries."
    if path in NON_CORE_PUBLIC:
        return "public_keep_no_seo", "secondary_brand_product", "Can stay public, but should not compete with psychology/EI clusters."
    if path in TRUST_ENTITY:
        return "public_support", "trust_entity", "Supports brand, proof, events, reviews and entity consistency."
    if path in CORE_PRIVATE_PRACTICE:
        return "public_core", "private_practice", "Core commercial search lane for consultations and adult states."
    if path in PRIVATE_SUPPORT:
        return "public_support", "private_practice_support", "Supporting page; should link to the private-practice pillar and avoid medical overclaims."
    if path in EI_CORE or path.startswith("/emotional-intelligence"):
        return "public_core", "emotional_intelligence_leadership", "Core authority lane for EI, leadership, speaking and soft skills."
    if path in TEEN_EXAM_CORE:
        return "public_core", "teen_exam_family", "Core lane for adolescents, exams, parents and study stress."
    if path.startswith("/article") or path.endswith("_article") or "/articles/" in path:
        return "public_support", "content_support", "Article/supporting content; assign to one pillar before strengthening."
    if "robots_txt_blocked" in issues:
        return "technical_fix", "indexing_blocker", "Open public page is blocked by robots; fix before measuring."
    return "review", "unassigned_public", "Open URL needs manual cluster decision."


def build_map() -> dict[str, object]:
    audit = json.loads(AUDIT_PATH.read_text(encoding="utf-8"))
    rows = []
    for item in audit["pages"]:
        path = normalize_path(item["url"])
        action, cluster, rationale = classify_url(item)
        rows.append(
            {
                "url": item["url"],
                "path": path,
                "kind": item.get("kind", ""),
                "action": action,
                "cluster": cluster,
                "issues": ", ".join(item.get("issues") or []),
                "title": item.get("title", ""),
                "h1_count": len(item.get("h1Values") or []),
                "rationale": rationale,
            }
        )
    summary = {}
    for key in ("action", "cluster"):
        counts: dict[str, int] = {}
        for row in rows:
            counts[row[key]] = counts.get(row[key], 0) + 1
        summary[key] = dict(sorted(counts.items()))
    return {
        "createdAt": datetime.now().isoformat(timespec="seconds"),
        "sourceAudit": AUDIT_PATH.relative_to(ROOT).as_posix(),
        "scopeRule": "Only open semantic public pages participate in positioning; opaque/test/legal/transactional/closed URLs are hygiene, not SEO clusters.",
        "summary": summary,
        "pages": rows,
    }


def write_outputs(report: dict[str, object]) -> None:
    MAP_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    fields = ["url", "path", "kind", "action", "cluster", "issues", "title", "h1_count", "rationale"]
    with MAP_CSV.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(report["pages"])

    lines = [
        "# Moonn Positioning Architecture — 2026-05-12",
        "",
        "## Scope",
        "",
        "This is a planning and governance artifact. It does not publish Tilda changes.",
        "",
        "- Branch: `codex/moonn-seo-positioning-architecture`.",
        "- Source live audit: `docs/moonn-final-seo-audit-2026-05-12.json`.",
        "- Public-page rule: analyze open semantic pages only; closed, opaque, test, legal and transactional URLs are cleanup/hygiene, not positioning assets.",
        "- User constraint: avoid visual Tilda/Chrome control while planning; use repository, HTTP checks and headless audits.",
        "",
        "## Verdict On The Submitted Research",
        "",
        "I agree with the core diagnosis. The site has strong brand/entity material, but its public sitemap currently spreads Tatyana Munn across too many equal-looking topics: private psychology, emotional intelligence, teen/exam products, events, gallery, older method pages and off-topic wellness pages. This weakens the site's primary purpose signal.",
        "",
        "The stronger strategy is not to create more pages for every broad keyword. The stronger strategy is to make the homepage a brand/entity gateway and build three search lanes with pillar pages, supporting pages, internal links and clear safety boundaries.",
        "",
        "## Current Live Evidence",
        "",
        "- Live audit checked `151` URLs.",
        "- `45` URLs are opaque/test/numeric and should be renamed, redirected or removed/noindexed.",
        "- `105` URLs need SEO strengthening.",
        "- `1` public psychology URL is blocked by robots and needs a technical fix.",
        "- `92` pages have no detected H1; `16` have multiple H1; `33` duplicate descriptions.",
        "- Homepage raw HTML has `5` H1 elements and mixes lecture headings, education, recommendations and Yandex services into the same semantic level.",
        "- `/panicheskie_ataki` has `7` H1 elements and overpromising medical-adjacent text; it should not remain a core landing in its current form.",
        "- `/psiholog` is cleaner conceptually but currently has no raw H1.",
        "- `/speaker` is the clearest current EI/spiker page: one H1, no fringe/medical risk hits in the sampled text.",
        "",
        "## Strategic Positioning",
        "",
        "Primary entity:",
        "",
        "> Татьяна Мунн — психолог МГУ и эксперт по эмоциональному интеллекту: консультации в Москве и онлайн, работа с тревогой, выгоранием, отношениями, подростками и экзаменационным стрессом; лекции и программы по эмоциональному интеллекту для людей и команд.",
        "",
        "This should be the stable bio/entity wording across homepage, `/psiholog`, `/speaker`, `/otzivi`, schema, Yandex profile links, Timepad descriptions and future page templates.",
        "",
        "## Search Lanes",
        "",
        "### 1. Private Practice",
        "",
        "Goal: convert adults who search for help with anxiety, burnout, relationships and emotional states.",
        "",
        "Pillar: `/psiholog`.",
        "",
        "Support pages to keep/merge/rewrite:",
        "",
        "- `/trevozhnost`",
        "- `/emotsionalnoe-vygoranie`",
        "- `/otnosheniya-i-granitsy`",
        "- `/samoocenka-i-uverennost`",
        "- `/depressivnoe-sostoyanie`",
        "- `/panicheskie_ataki` only after claim cleanup and one-H1 rebuild",
        "",
        "Do not try to win the broad head term `психолог Москва` as the main bet. Use it as a local modifier, not as the positioning core.",
        "",
        "### 2. Emotional Intelligence And Leadership",
        "",
        "Goal: make Tatyana visible as an expert, speaker and educator in emotional intelligence, self-regulation and soft skills.",
        "",
        "Pillars: `/speaker` and `/emotional-intelligence/`.",
        "",
        "Support pages:",
        "",
        "- `/articles/eq-dlya-rukovoditeley`",
        "- `/emotional-intelligence/knowledge-base/*` after H1 fixes",
        "- `/kurs-ei`",
        "- `/events` and `/events_tp` as evidence, not as the main content hub",
        "",
        "This is the most defensible non-brand SEO lane because it matches her public lectures, MSU/education proof, schema `knowsAbout`, and existing content cluster.",
        "",
        "### 3. Teens, Exams And Family Support",
        "",
        "Goal: own narrower high-intent pages around teen communication, exam anxiety and parent support.",
        "",
        "Pillars: `/psypodgotovka1` or a future semantic slug `/psihologicheskaya-podgotovka-k-ekzamenam`, plus `/podrostkovyy-lager-psihologiya` for the seasonal product.",
        "",
        "Support pages:",
        "",
        "- `/uslugi_podrostki`",
        "- `/article_gadget_addiction`",
        "- `/vospitanie_article`",
        "- future pages for `страх ЕГЭ`, `тревога перед экзаменом`, `подросток и гаджеты`, `как родителям поддержать подростка`",
        "",
        "## Homepage Rule",
        "",
        "The homepage should stop being a catalog of everything. It should become a concise brand/entity gateway:",
        "",
        "1. One H1 with name + positioning.",
        "2. Three route cards: consultations, emotional intelligence/speaker, teens/exams.",
        "3. Proof layer: MSU, lectures, reviews, Yandex/B17/Timepad/YouTube links.",
        "4. Current campaigns as compact banners below the strategic routes.",
        "5. Gallery and other secondary products should be lower priority or moved out of the main SEO route.",
        "",
        "## Pages To De-Emphasize Or Archive",
        "",
        "These pages should not be equal homepage/SEO signals unless rewritten with clear evidence, psychological boundaries and a reason to exist:",
        "",
        "- `/aromatherapy`",
        "- `/microbiom`",
        "- `/phytotherapy`",
        "- `/salt`",
        "- `/water`",
        "- `/vacuum_cups`",
        "- `/geshtalt`, `/kpt`, `/schematherapy`, `/psychoanalys` if they are only method labels and not strong unique service pages",
        "- `/kartiny-tatiany-munn` as a public product page, not a psychology SEO lane",
        "",
        "Recommended action: keep accessible where needed, but remove from homepage priority and sitemap/index unless each page is rebuilt as a safe, sourced, user-first article.",
        "",
        "## Technical SEO Gates For Every Open Public Page",
        "",
        "- Exactly one raw H1.",
        "- Self-canonical for unique public pages.",
        "- Unique title and description matched to one intent.",
        "- Visible content must support the structured data.",
        "- No internal SEO/debug wording in public text.",
        "- No medical guarantees or promises of complete/fast cure.",
        "- For medical-adjacent topics: add boundary text that psychological consultation is not emergency or medical care and that medication questions belong to physicians.",
        "- Images: meaningful alt on hero/content images first.",
        "- Pages not assigned to one of the three lanes must not remain in the main sitemap as active SEO targets.",
        "",
        "## AIO / AI Search Rule",
        "",
        "Do not create special `AI SEO` files as the main work. Google says AI features use the same fundamental SEO requirements and no special AI markup/files are needed. Yandex fast answers are generated automatically from indexed, well-structured, well-written pages. So the practical AI plan is: clean indexable pages, clear headings, strong authorship/entity proof, structured data that matches visible content, and concise answer blocks.",
        "",
        "## Implementation Order",
        "",
        "### Phase 1: Stop Dilution",
        "",
        "1. Create a public URL decision register from this map.",
        "2. Remove/redirect/noindex the `45` opaque/test URLs.",
        "3. Fix robots block for `/psiholog-moskva-online` or decide to redirect it.",
        "4. Move off-topic wellness pages out of the main SEO path.",
        "",
        "### Phase 2: Rebuild Core Pages",
        "",
        "1. Homepage: one-H1 brand gateway with three routes.",
        "2. `/psiholog`: main private-practice pillar.",
        "3. `/speaker`: EI/speaker pillar.",
        "4. `/emotional-intelligence/`: content hub without unfinished blocks.",
        "5. `/psypodgotovka1`: either keep alias but strengthen canonical/slug strategy, or redirect to a semantic slug after a migration plan.",
        "",
        "### Phase 3: Cluster Content",
        "",
        "Build 5-8 supporting pages per lane. Each support page must link up to its pillar and sideways only inside its cluster.",
        "",
        "### Phase 4: External Entity Reinforcement",
        "",
        "Align sameAs/profile facts across schema, Yandex Services, Timepad, B17/other profiles, YouTube and site bio. Use verified review summaries and source links, not fake aggregate-rating markup.",
        "",
        "## Machine Map",
        "",
        f"- JSON: `{MAP_JSON.relative_to(ROOT).as_posix()}`",
        f"- CSV: `{MAP_CSV.relative_to(ROOT).as_posix()}`",
        "",
        "## Sources Checked",
        "",
        "- Google Search Central, AI features and your website: https://developers.google.com/search/docs/appearance/ai-features?hl=en",
        "- Google Search Central, helpful reliable people-first content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content",
        "- Google Search Central, URL structure: https://developers.google.com/search/docs/crawling-indexing/url-structure/?hl=en",
        "- Google Search Central, review snippets: https://developers.google.com/search/docs/appearance/structured-data/review-snippet",
        "- Yandex Webmaster, fast answer: https://yandex.ru/support/webmaster/ru/search-appearance/fast",
        "",
        "## Done Criteria For The Next Implementation Branch",
        "",
        "- Public URL register updated after Tilda changes.",
        "- Live raw HTML confirms one H1 on homepage and each rebuilt pillar.",
        "- Sitemap no longer contains closed/opaque/test URLs.",
        "- Homepage no longer gives equal weight to off-topic products and wellness pages.",
        "- A fresh `scripts/moonn_final_seo_audit.py` run shows reduced duplicate descriptions, multiple H1 and opaque slug counts.",
        "- Browser render verifies that the homepage is visually coherent after the SEO restructure.",
        "",
    ]
    STRATEGY_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    report = build_map()
    write_outputs(report)
    print(json.dumps(report["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
