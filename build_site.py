from __future__ import annotations

import argparse
import json
import html
import shutil
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "site.json"
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


def render_palmistry_embed(page: dict[str, Any], asset_prefix: str = "") -> str:
    quiz = page["quiz"]
    images = {item["id"]: item for item in quiz["images"]}
    options = []
    for step in quiz["steps"]:
        radios = []
        for item in step["options"]:
            radios.append(
                f"""
                <label class="np-option">
                  <input type="radio" name="{esc(step["id"])}" value="{esc(item["value"])}" data-archetype="{esc(item["archetype"])}" />
                  <span>
                    <strong>{esc(item["label"])}</strong>
                    <em>{esc(item["text"])}</em>
                  </span>
                </label>
                """
            )
        options.append(
            f"""
            <fieldset class="np-step">
              <legend>{esc(step["title"])}</legend>
              <div class="np-options">{"".join(radios)}</div>
            </fieldset>
            """
        )
    archetypes_json = html.escape(json.dumps(quiz["archetypes"], ensure_ascii=False), quote=False)
    image_cards = []
    for item in quiz["images"]:
        image_cards.append(
            f"""
            <figure class="np-image-card">
              <img src="{esc(asset_prefix + item["src"])}" alt="{esc(item["alt"])}" loading="lazy" />
              <figcaption>{esc(item["caption"])}</figcaption>
            </figure>
            """
        )
    return f"""
<section class="neuro-palmistry" data-neuro-palmistry>
  <style>
    .neuro-palmistry {{
      --np-bg: #fffaf4;
      --np-ink: #1f2630;
      --np-muted: #65707d;
      --np-line: rgba(31, 38, 48, 0.14);
      --np-accent: #008778;
      --np-accent-2: #b64c72;
      --np-gold: #c28b2c;
      max-width: 1120px;
      margin: 0 auto;
      padding: clamp(18px, 3vw, 34px);
      color: var(--np-ink);
      background: linear-gradient(180deg, #fffdf9 0%, var(--np-bg) 100%);
      border: 1px solid var(--np-line);
      border-radius: 18px;
      font-family: Inter, "IBM Plex Sans", "Segoe UI", Arial, sans-serif;
    }}
    .neuro-palmistry * {{ box-sizing: border-box; }}
    .np-hero {{
      display: grid;
      grid-template-columns: minmax(0, 1.1fr) minmax(260px, 0.9fr);
      gap: clamp(18px, 4vw, 42px);
      align-items: center;
      margin-bottom: 28px;
    }}
    .np-kicker {{
      display: inline-flex;
      margin: 0 0 12px;
      padding: 6px 10px;
      border-radius: 999px;
      background: rgba(0, 135, 120, 0.1);
      color: var(--np-accent);
      font-size: 13px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}
    .np-hero h2 {{
      margin: 0;
      max-width: 760px;
      font-family: Georgia, "Times New Roman", serif;
      font-size: clamp(34px, 5vw, 64px);
      line-height: 1.02;
      letter-spacing: 0;
    }}
    .np-lead {{
      max-width: 680px;
      margin: 16px 0 0;
      color: var(--np-muted);
      font-size: clamp(17px, 2vw, 21px);
      line-height: 1.55;
    }}
    .np-note {{
      margin: 18px 0 0;
      padding: 12px 14px;
      border-left: 4px solid var(--np-accent);
      background: rgba(0, 135, 120, 0.08);
      color: #2f4045;
      line-height: 1.55;
    }}
    .np-hero-visual {{
      margin: 0;
      overflow: hidden;
      border-radius: 14px;
      border: 1px solid var(--np-line);
      background: #fff;
    }}
    .np-hero-visual img, .np-image-card img {{
      display: block;
      width: 100%;
      height: auto;
    }}
    .np-hero-visual figcaption, .np-image-card figcaption {{
      padding: 10px 12px;
      color: var(--np-muted);
      font-size: 13px;
      line-height: 1.4;
    }}
    .np-layout {{
      display: grid;
      grid-template-columns: minmax(0, 0.92fr) minmax(320px, 1.08fr);
      gap: 18px;
      align-items: start;
    }}
    .np-panel {{
      border: 1px solid var(--np-line);
      border-radius: 14px;
      background: rgba(255, 255, 255, 0.76);
      padding: clamp(14px, 2.4vw, 22px);
    }}
    .np-panel h3 {{
      margin: 0 0 12px;
      font-size: 22px;
      line-height: 1.18;
    }}
    .np-step {{
      margin: 0 0 16px;
      padding: 0;
      border: 0;
    }}
    .np-step legend {{
      margin-bottom: 10px;
      font-weight: 800;
      font-size: 16px;
    }}
    .np-options {{
      display: grid;
      gap: 10px;
    }}
    .np-option {{
      display: grid;
      grid-template-columns: 22px minmax(0, 1fr);
      gap: 10px;
      align-items: start;
      min-height: 70px;
      padding: 12px;
      border: 1px solid var(--np-line);
      border-radius: 12px;
      background: #fff;
      cursor: pointer;
    }}
    .np-option:has(input:checked) {{
      border-color: var(--np-accent);
      box-shadow: 0 0 0 3px rgba(0, 135, 120, 0.12);
    }}
    .np-option input {{
      width: 18px;
      height: 18px;
      margin-top: 2px;
      accent-color: var(--np-accent);
    }}
    .np-option strong, .np-option em {{
      display: block;
      line-height: 1.35;
    }}
    .np-option em {{
      margin-top: 4px;
      color: var(--np-muted);
      font-style: normal;
      font-size: 14px;
    }}
    .np-hand {{
      display: grid;
      place-items: center;
      min-height: 280px;
      border-radius: 14px;
      background:
        linear-gradient(145deg, rgba(0, 135, 120, 0.12), rgba(182, 76, 114, 0.1)),
        #fff;
      border: 1px solid var(--np-line);
    }}
    .np-hand svg {{
      width: min(100%, 360px);
      height: auto;
    }}
    .np-line-draw {{
      fill: none;
      stroke: var(--np-accent-2);
      stroke-width: 5;
      stroke-linecap: round;
      stroke-dasharray: 520;
      animation: np-draw 2.4s ease forwards;
    }}
    .np-line-draw:nth-child(2) {{ stroke: var(--np-accent); animation-delay: 0.2s; }}
    .np-line-draw:nth-child(3) {{ stroke: var(--np-gold); animation-delay: 0.4s; }}
    @keyframes np-draw {{
      from {{ stroke-dashoffset: 520; opacity: 0.4; }}
      to {{ stroke-dashoffset: 0; opacity: 1; }}
    }}
    .np-button-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 16px;
    }}
    .np-button {{
      border: 0;
      border-radius: 999px;
      padding: 12px 18px;
      background: var(--np-accent);
      color: #fff;
      font-weight: 800;
      cursor: pointer;
    }}
    .np-button.secondary {{
      background: #fff;
      color: var(--np-ink);
      border: 1px solid var(--np-line);
    }}
    .np-result {{
      margin-top: 16px;
      padding: 16px;
      border-radius: 14px;
      border: 1px solid rgba(0, 135, 120, 0.28);
      background: rgba(0, 135, 120, 0.08);
    }}
    .np-result[hidden] {{ display: none; }}
    .np-result h4 {{
      margin: 0 0 8px;
      font-size: 22px;
    }}
    .np-result p {{
      margin: 8px 0;
      line-height: 1.6;
    }}
    .np-result ul {{
      margin: 10px 0 0;
      padding-left: 20px;
      line-height: 1.6;
    }}
    .np-gallery {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 12px;
      margin-top: 18px;
    }}
    .np-image-card {{
      margin: 0;
      overflow: hidden;
      border: 1px solid var(--np-line);
      border-radius: 12px;
      background: #fff;
    }}
    .np-attribution {{
      margin-top: 16px;
      color: var(--np-muted);
      font-size: 12px;
      line-height: 1.5;
    }}
    .np-attribution a {{ color: var(--np-accent); }}
    @media (max-width: 860px) {{
      .np-hero, .np-layout, .np-gallery {{ grid-template-columns: 1fr; }}
      .neuro-palmistry {{ border-radius: 0; border-left: 0; border-right: 0; }}
    }}
  </style>
  <div class="np-hero">
    <div>
      <p class="np-kicker">{esc(page.get("hero_kicker", ""))}</p>
      <h2>{esc(page.get("hero_heading", page["title"]))}</h2>
      <p class="np-lead">{esc(page.get("hero_subheading", page["description"]))}</p>
      <p class="np-note">{esc(quiz["public_disclaimer"])}</p>
    </div>
    <figure class="np-hero-visual">
      <img src="{esc(asset_prefix + images["right-hand-chart"]["src"])}" alt="{esc(images["right-hand-chart"]["alt"])}" loading="lazy" />
      <figcaption>{esc(images["right-hand-chart"]["caption"])}</figcaption>
    </figure>
  </div>
  <div class="np-layout">
    <div class="np-panel">
      <h3>Схема руки</h3>
      <div class="np-hand" aria-hidden="true">
        <svg viewBox="0 0 260 320" role="img">
          <path d="M126 291 C91 271 70 243 66 203 L55 118 C53 102 75 98 80 113 L93 155 L94 66 C95 48 119 48 120 66 L124 147 L132 45 C134 27 158 30 157 49 L151 149 L166 67 C169 50 192 55 188 74 L174 157 L198 105 C205 90 226 101 219 118 L194 184 C184 212 179 246 167 265 C157 280 144 288 126 291 Z" fill="#ffe1c4" stroke="#8e5940" stroke-width="4" />
          <path class="np-line-draw" d="M82 181 C111 164 143 164 178 184" />
          <path class="np-line-draw" d="M86 214 C117 201 149 203 183 219" />
          <path class="np-line-draw" d="M111 250 C94 222 91 191 105 160" />
          <path class="np-line-draw" d="M143 255 C145 219 142 190 134 160" />
        </svg>
      </div>
      <p class="np-note">Результат строится по выбранным вариантам, а не по загрузке фотографии. Так страница не собирает биометрию и персональные данные.</p>
      <div class="np-gallery">{"".join(image_cards)}</div>
      <p class="np-attribution">
        Изображения: Wikimedia Commons, public domain/CC0. Источники: Chief Lines of the Hand, Plate XXII Palmistry chart of right hand, Chart of the Hand.
      </p>
    </div>
    <div class="np-panel">
      <h3>{esc(quiz["title"])}</h3>
      <form class="np-form">
        {"".join(options)}
        <div class="np-button-row">
          <button class="np-button" type="button" data-np-result>Показать разбор</button>
          <button class="np-button secondary" type="reset" data-np-reset>Сбросить</button>
        </div>
      </form>
      <div class="np-result" hidden aria-live="polite">
        <h4></h4>
        <p data-np-summary></p>
        <ul data-np-points></ul>
        <p data-np-footer></p>
      </div>
    </div>
  </div>
  <script type="application/json" data-np-archetypes>{archetypes_json}</script>
  <script>
    (() => {{
      const root = document.currentScript.closest('[data-neuro-palmistry]');
      const archetypes = JSON.parse(root.querySelector('[data-np-archetypes]').textContent);
      const result = root.querySelector('.np-result');
      const button = root.querySelector('[data-np-result]');
      const reset = root.querySelector('[data-np-reset]');
      const form = root.querySelector('.np-form');
      const choose = () => {{
        const checked = [...root.querySelectorAll('input[type="radio"]:checked')];
        const required = new Set([...root.querySelectorAll('fieldset')].map((item) => item.querySelector('input').name));
        if (checked.length < required.size) {{
          result.hidden = false;
          result.querySelector('h4').textContent = 'Нужно выбрать все варианты';
          result.querySelector('[data-np-summary]').textContent = 'Пройдите четыре коротких шага, чтобы получить аккуратный развлекательный разбор.';
          result.querySelector('[data-np-points]').innerHTML = '';
          result.querySelector('[data-np-footer]').textContent = '';
          return;
        }}
        const score = {{}};
        checked.forEach((item) => {{
          const key = item.dataset.archetype;
          score[key] = (score[key] || 0) + 1;
        }});
        const winner = Object.keys(archetypes).sort((a, b) => (score[b] || 0) - (score[a] || 0))[0];
        const data = archetypes[winner];
        result.hidden = false;
        result.querySelector('h4').textContent = data.title;
        result.querySelector('[data-np-summary]').textContent = data.summary;
        result.querySelector('[data-np-points]').innerHTML = data.points.map((point) => `<li>${{point}}</li>`).join('');
        result.querySelector('[data-np-footer]').textContent = data.footer;
      }};
      button.addEventListener('click', choose);
      reset.addEventListener('click', () => {{
        window.setTimeout(() => {{
          result.hidden = true;
          form.querySelectorAll('input').forEach((item) => item.checked = false);
        }}, 0);
      }});
    }})();
  </script>
</section>
"""


def render_palmistry_quiz_page(site: dict[str, Any], pages: list[dict[str, Any]], page: dict[str, Any]) -> str:
    nav = nav_links(pages)
    title = page["title"]
    description = page["description"]
    canonical = f'{site["site_url"].rstrip("/")}/{page["filename"]}'
    schema = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": title,
        "description": description,
        "url": canonical,
        "inLanguage": "ru-RU",
        "isAccessibleForFree": True,
        "audience": {"@type": "Audience", "audienceType": "16+"},
    }
    return f"""<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}" />
  <link rel="canonical" href="{esc(canonical)}" />
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml" />
  <link rel="stylesheet" href="assets/site.css" />
  <meta name="robots" content="index,follow" />
  <meta property="og:title" content="{esc(title)}" />
  <meta property="og:description" content="{esc(description)}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{esc(canonical)}" />
  <meta property="og:site_name" content="{esc(site["name"])}" />
  <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
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
    {render_palmistry_embed(page)}
  </main>
  <footer class="footer">
    <p>Основной брендовый сайт: <a href="{esc(site["brand_url"])}">{esc(site["brand_domain"])}</a>.</p>
  </footer>
</body>
</html>
"""


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
    if page.get("template") == "palmistry_quiz":
        return render_palmistry_quiz_page(site, pages, page)
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
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml" />
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
        image_entries = []
        for image in page.get("quiz", {}).get("images", []):
            image_url = site["site_url"].rstrip("/") + "/" + image["src"]
            image_entries.append(
                "    <image:image>"
                f"<image:loc>{esc(image_url)}</image:loc>"
                f"<image:caption>{esc(image['caption'])}</image:caption>"
                "</image:image>"
            )
        if image_entries:
            items.append(f"  <url><loc>{esc(url)}</loc>\n" + "\n".join(image_entries) + "\n  </url>")
        else:
            items.append(f"  <url><loc>{esc(url)}</loc></url>")
    return (
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
        "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\" xmlns:image=\"http://www.google.com/schemas/sitemap-image/1.1\">\n"
        + "\n".join(items)
        + "\n</urlset>\n"
    )


def build_robots(site: dict[str, Any]) -> str:
    return f"""User-agent: *
Allow: /

Sitemap: {site['site_url'].rstrip('/')}/sitemap.xml
"""


def copy_assets(out_dir: Path) -> None:
    css = (ROOT / "assets" / "site.css").read_text(encoding="utf-8")
    (out_dir / "assets" / "site.css").write_text(css, encoding="utf-8")
    favicon = ROOT / "assets" / "favicon.svg"
    if favicon.exists():
        shutil.copy2(favicon, out_dir / "assets" / "favicon.svg")
    image_src = ROOT / "assets" / "images"
    image_dst = out_dir / "assets" / "images"
    if image_src.exists():
        shutil.copytree(image_src, image_dst, dirs_exist_ok=True)


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
    (out_dir / "snippets").mkdir(exist_ok=True)

    copy_assets(out_dir)

    for page in pages:
        content = render_page(site, person, pages, page)
        (out_dir / page["filename"]).write_text(content, encoding="utf-8")
        if page.get("template") == "palmistry_quiz":
            snippet = render_palmistry_embed(page, asset_prefix="https://tatyana-psy.moonn.ru/")
            (out_dir / "snippets" / "neuro-palmistry-test.html").write_text(snippet, encoding="utf-8")

    (out_dir / ".nojekyll").write_text("", encoding="utf-8")
    (out_dir / "CNAME").write_text((ROOT / "CNAME").read_text(encoding="utf-8"), encoding="utf-8")
    (out_dir / "robots.txt").write_text(build_robots(site), encoding="utf-8")
    (out_dir / "llms.txt").write_text(build_llms_txt(site, pages), encoding="utf-8")
    (out_dir / "sitemap.xml").write_text(build_sitemap(site, pages), encoding="utf-8")


if __name__ == "__main__":
    main()
