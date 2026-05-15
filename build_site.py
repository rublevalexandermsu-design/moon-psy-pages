from __future__ import annotations

import argparse
import json
import html
import shutil
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "site.json"
TIMEPAD_REGISTRATION_PATH = ROOT / "data" / "timepad-registration-pages.json"
DIST = ROOT / "dist"


def esc(value: Any) -> str:
    return html.escape("" if value is None else str(value), quote=True)


def load_data() -> dict[str, Any]:
    with DATA_PATH.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def page_slug(filename: str) -> str:
    return Path(filename).stem


def nav_links(pages: list[dict[str, Any]]) -> str:
    items = []
    for page in pages:
        label = esc(page.get("nav_label", page["title"]))
        href = esc(page["filename"])
        items.append(f'<a href="{href}">{label}</a>')
    return "\n".join(items)


def render_section(section: dict[str, Any]) -> str:
    title = esc(section.get("title", ""))
    kind = section.get("type", "list")
    if kind == "cards":
        cards = []
        for item in section.get("items", []):
            href = item.get("href")
            link = f'<a class="card-link" href="{esc(href)}">Подробнее</a>' if href else ""
            cards.append(
                f"""
                <article class="card">
                  <h3>{esc(item.get("title", ""))}</h3>
                  <p>{esc(item.get("text", ""))}</p>
                  {link}
                </article>
                """
            )
        return f'<section class="block"><h2>{title}</h2><div class="grid">{"" .join(cards)}</div></section>'
    if kind == "list":
        items = "".join(f"<li>{esc(item)}</li>" for item in section.get("items", []))
        return f'<section class="block"><h2>{title}</h2><ul class="bullets">{items}</ul></section>'
    if kind == "text":
        return f'<section class="block"><h2>{title}</h2><p>{esc(section.get("text", ""))}</p></section>'
    return ""


def render_faq(faq: list[dict[str, str]]) -> str:
    rows = []
    for item in faq:
        rows.append(
            f"""
            <details class="faq-item">
              <summary>{esc(item["question"])}</summary>
              <p>{esc(item["answer"])}</p>
            </details>
            """
        )
    return '<section class="block"><h2>FAQ</h2>' + "".join(rows) + "</section>"


def schema_jsonld(site: dict[str, Any], person: dict[str, Any], page: dict[str, Any]) -> str:
    web_page = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": page["title"],
        "description": page["description"],
        "url": site["site_url"] if page["slug"] == "index" else f'{site["site_url"].rstrip("/")}/{page["filename"]}',
        "inLanguage": "ru-RU",
    }
    person_schema = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": person["name"],
        "jobTitle": person["job_title"],
        "url": site["brand_url"],
        "address": {
            "@type": "PostalAddress",
            "addressLocality": person["address_locality"],
            "addressRegion": person["service_area"],
            "addressCountry": "RU",
        },
        "sameAs": [site["brand_url"], site["review_url"]],
    }
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": item["question"],
                "acceptedAnswer": {"@type": "Answer", "text": item["answer"]},
            }
            for item in page.get("faq", [])
        ],
    }
    schemas = [web_page, person_schema]
    if page.get("faq"):
        schemas.append(faq_schema)
    if page["slug"] != "index":
        schemas.append(
            {
                "@context": "https://schema.org",
                "@type": "Service",
                "name": page["title"],
                "serviceType": page["title"],
                "provider": {"@type": "Person", "name": person["name"]},
                "areaServed": person["service_area"],
                "url": f'{site["site_url"].rstrip("/")}/{page["filename"]}',
            }
        )
    return "\n".join(
        '<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False) + "</script>"
        for schema in schemas
    )


def render_page(site: dict[str, Any], person: dict[str, Any], pages: list[dict[str, Any]], page: dict[str, Any]) -> str:
    nav = nav_links(pages)
    sections = "".join(render_section(section) for section in page.get("sections", []))
    faq = render_faq(page.get("faq", [])) if page.get("faq") else ""
    hero_cta = ""
    if page.get("primary_cta"):
        hero_cta += f'<a class="button primary" href="{esc(page["primary_cta"]["href"])}">{esc(page["primary_cta"]["label"])}</a>'
    if page.get("secondary_cta"):
        hero_cta += f'<a class="button" href="{esc(page["secondary_cta"]["href"])}">{esc(page["secondary_cta"]["label"])}</a>'
    machine = f"""
      <aside class="machine">
        <h3>Машинный слой</h3>
        <ul class="bullets compact">
          <li>Canonical page: {esc(page["filename"])}</li>
          <li>Person: {esc(person["name"])}</li>
          <li>Service area: {esc(person["service_area"])}</li>
          <li>Primary review URL: {esc(site["review_url"])}</li>
        </ul>
      </aside>
    """
    title = page["title"]
    description = page["description"]
    canonical = f'{site["site_url"].rstrip("/")}/{page["filename"]}' if page["slug"] != "index" else site["site_url"]
    return f"""<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}" />
  <link rel="canonical" href="{esc(canonical)}" />
  <link rel="stylesheet" href="assets/site.css" />
  <meta name="robots" content="index,follow" />
  <meta property="og:title" content="{esc(title)}" />
  <meta property="og:description" content="{esc(description)}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{esc(canonical)}" />
  <meta property="og:site_name" content="{esc(site["name"])}" />
  {schema_jsonld(site, person, page)}
</head>
<body>
  <header class="topbar">
    <div class="brand">
      <span class="brand-mark">MM</span>
      <div>
        <strong>{esc(site["name"])}</strong>
        <span>{esc(site["site_url"])}</span>
      </div>
    </div>
    <nav class="nav">
      {nav}
    </nav>
  </header>
  <main class="wrap">
    <section class="hero">
      <p class="kicker">{esc(page.get("hero_kicker", ""))}</p>
      <h1>{esc(page.get("hero_heading", page["title"]))}</h1>
      <p class="lead">{esc(page.get("hero_subheading", page["description"]))}</p>
      <p class="body">{esc(page.get("hero_body", ""))}</p>
      <div class="cta">{hero_cta}</div>
    </section>
    {machine}
    {sections}
    {faq}
  </main>
  <footer class="footer">
    <p>Основной брендовый сайт остаётся на <a href="{esc(site["brand_url"])}">{esc(site["brand_domain"])}</a>. Этот поддомен служит SEO / AEO / IEO-слоем.</p>
    <p><a href="{esc(site["review_url"])}">Прямая форма отзыва Яндекс Услуг</a></p>
  </footer>
</body>
</html>
"""


def build_llms_txt(site: dict[str, Any], pages: list[dict[str, Any]]) -> str:
    lines = [
        f"# {site['name']} — machine readable map",
        "",
        f"Site: {site['site_url']}",
        f"Brand site: {site['brand_url']}",
        f"Review URL: {site['review_url']}",
        "",
        "Important pages:",
    ]
    for page in pages:
        lines.append(f"- {page['filename']} — {page['title']}")
    lines.extend(
        [
            "",
            "Rules:",
            "- Use the index page as the canonical hub.",
            "- Use cluster pages for distinct intents.",
            "- Prefer direct review flow for event feedback.",
        ]
    )
    return "\n".join(lines) + "\n"


def build_sitemap(site: dict[str, Any], pages: list[dict[str, Any]]) -> str:
    items = []
    for page in pages:
        url = site["site_url"].rstrip("/") + "/" + page["filename"]
        if page["slug"] == "index":
            url = site["site_url"]
        items.append(f"  <url><loc>{esc(url)}</loc></url>")
    static_urls = [
        site["site_url"].rstrip("/") + "/teen-softskills/",
    ]
    for url in static_urls:
        items.append(f"  <url><loc>{esc(url)}</loc></url>")
    return (
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
        "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n"
        + "\n".join(items)
        + "\n</urlset>\n"
    )


def build_robots(site: dict[str, Any]) -> str:
    return f"""User-agent: *
Allow: /

Sitemap: {site['site_url'].rstrip('/')}/sitemap.xml
"""


def copy_static_tree(source: Path, destination: Path) -> None:
    if not source.exists():
        return
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(source, destination)


def load_timepad_registration_pages() -> dict[str, Any]:
    if not TIMEPAD_REGISTRATION_PATH.exists():
        return {"pages": []}
    with TIMEPAD_REGISTRATION_PATH.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def render_timepad_registration_page(site: dict[str, Any], page: dict[str, Any]) -> str:
    canonical = f'{site["site_url"].rstrip("/")}/timepad/{page["slug"]}/'
    master_url = page["master_event_url"]
    title = page["title"]
    description = page["description"]
    event_id = int(page["master_event_id"])
    recurring_event_id = int(page["recurring_event_id"])
    poster = page.get("poster_url", "")
    poster_html = (
        f'<img class="poster" src="{esc(poster)}" alt="{esc(page.get("poster_alt", title))}" />'
        if poster
        else ""
    )
    widget_config = {
        "event": {"id": event_id},
        "prefill": {"recurringEvent": recurring_event_id},
    }
    widget_config_json = json.dumps(widget_config, ensure_ascii=False)
    return f"""<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}" />
  <meta name="robots" content="noindex,follow" />
  <link rel="canonical" href="{esc(canonical)}" />
  <style>
    :root {{ color-scheme: light; }}
    body {{
      margin: 0;
      font-family: Arial, Helvetica, sans-serif;
      background: #f8f3ff;
      color: #1f2430;
    }}
    .wrap {{
      max-width: 980px;
      margin: 0 auto;
      padding: 28px 16px 42px;
    }}
    .hero {{
      display: grid;
      grid-template-columns: minmax(0, 280px) minmax(0, 1fr);
      gap: 24px;
      align-items: center;
      margin-bottom: 24px;
      padding: 18px;
      background: #fff;
      border: 1px solid #eadcf7;
      border-radius: 12px;
      box-shadow: 0 18px 42px rgba(88, 48, 140, .12);
    }}
    .poster {{
      width: 100%;
      max-width: 280px;
      border-radius: 10px;
      display: block;
    }}
    .kicker {{
      margin: 0 0 8px;
      color: #6a36c9;
      font-weight: 700;
      text-transform: uppercase;
      font-size: 13px;
    }}
    h1 {{
      margin: 0 0 12px;
      font-size: clamp(28px, 4vw, 44px);
      line-height: 1.08;
      letter-spacing: 0;
    }}
    .lead {{
      margin: 0 0 12px;
      font-size: 18px;
      line-height: 1.5;
    }}
    .back {{
      display: inline-flex;
      margin-top: 8px;
      color: #5d2fd1;
      font-weight: 700;
      text-decoration: none;
    }}
    .widget {{
      padding: 18px;
      background: #fff;
      border: 1px solid #eadcf7;
      border-radius: 12px;
    }}
    @media (max-width: 720px) {{
      .hero {{ grid-template-columns: 1fr; }}
      .poster {{ max-width: 100%; }}
    }}
  </style>
</head>
<body>
  <main class="wrap">
    <section class="hero">
      <div>{poster_html}</div>
      <div>
        <p class="kicker">{esc(page["date_label"])}</p>
        <h1>{esc(page["heading"])}</h1>
        <p class="lead">{esc(description)}</p>
        <a class="back" href="{esc(master_url)}">Вернуться к общей странице лекций</a>
      </div>
    </section>
    <section class="widget" aria-label="Форма регистрации Timepad">
      <script type="text/javascript" async="async" defer="defer" charset="UTF-8"
        src="https://timepad.ru/js/tpwf/loader/min/loader.js?v=355"
        data-timepad-widget-v2="event_register">
        (function(){{return {widget_config_json};}})();
      </script>
    </section>
  </main>
</body>
</html>
"""


def build_timepad_registration_pages(site: dict[str, Any], out_dir: Path) -> None:
    pages = load_timepad_registration_pages().get("pages", [])
    for page in pages:
        page_dir = out_dir / "timepad" / page["slug"]
        page_dir.mkdir(parents=True, exist_ok=True)
        page_html = render_timepad_registration_page(site, page)
        (page_dir / "index.html").write_text(page_html, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="dist")
    args = parser.parse_args()

    data = load_data()
    site = data["site"]
    person = data["person"]
    pages = data["pages"]

    out_dir = ROOT / args.output
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "assets").mkdir(exist_ok=True)

    css = (ROOT / "assets" / "site.css").read_text(encoding="utf-8")
    (out_dir / "assets" / "site.css").write_text(css, encoding="utf-8")
    copy_static_tree(ROOT / "assets" / "teen-softskills", out_dir / "assets" / "teen-softskills")
    copy_static_tree(ROOT / "teen-softskills", out_dir / "teen-softskills")

    for page in pages:
        content = render_page(site, person, pages, page)
        (out_dir / page["filename"]).write_text(content, encoding="utf-8")

    build_timepad_registration_pages(site, out_dir)

    (out_dir / ".nojekyll").write_text("", encoding="utf-8")
    (out_dir / "CNAME").write_text((ROOT / "CNAME").read_text(encoding="utf-8"), encoding="utf-8")
    (out_dir / "robots.txt").write_text(build_robots(site), encoding="utf-8")
    (out_dir / "llms.txt").write_text(build_llms_txt(site, pages), encoding="utf-8")
    (out_dir / "sitemap.xml").write_text(build_sitemap(site, pages), encoding="utf-8")


if __name__ == "__main__":
    main()
