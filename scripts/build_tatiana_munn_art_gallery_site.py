from __future__ import annotations

import json
import os
import re
import shutil
import urllib.request
import zipfile
from dataclasses import dataclass
from html import escape
from pathlib import Path

from PIL import Image, ImageEnhance, ImageOps


ROOT = Path(__file__).resolve().parents[1]
DOWNLOADS = Path(r"C:\Users\yanta\Downloads")
OUT = ROOT / "docs" / "tatiana-munn-art-gallery"
ASSETS = OUT / "assets"
ART_DIR = ASSETS / "art"
SCENE_DIR = ASSETS / "scene"
VENDOR_DIR = ASSETS / "vendor"
DATA_DIR = OUT / "data"
ZIP_OUT = ROOT / "output" / "tatiana-munn-art-gallery-site.zip"
THREE_URL = "https://unpkg.com/three@0.164.1/build/three.module.min.js"
GITHUB_REPO = "rublevalexandermsu-design/moonn-psy-pages"
TILDA_PAGE_ALIAS = "kartiny-tatiany-munn"
TILDA_PAGE_URL = f"https://moonn.ru/{TILDA_PAGE_ALIAS}"
TILDA_CDN_REF = os.environ.get("MOONN_ART_GALLERY_CDN_REF", "__MOONN_ART_GALLERY_CDN_REF__")
TILDA_CDN_BASE = f"https://cdn.jsdelivr.net/gh/{GITHUB_REPO}@{TILDA_CDN_REF}/docs/tatiana-munn-art-gallery"
TILDA_PROJECT_ID = "8326812"
TILDA_HOMEPAGE_ID = "42678538"
TILDA_PAGE_TITLE = "Картины Татьяны Мунн | 3D-галерея и персональный код"
TILDA_PAGE_DESCRIPTION = "3D-галерея энергетических картин Татьяны Мунн: каталог работ, персональный код, заявка и онлайн-оплата через защищенную корзину сайта."

SCENE_ASSETS = {
    "gallery-floor-parquet.webp": "ChatGPT Image 10 мая 2026 г., 22_26_33 (1).png",
    "gallery-bench-blue-tufted.webp": "ChatGPT Image 10 мая 2026 г., 22_26_39 (8).png",
    "gallery-door-ornate.webp": "ChatGPT Image 10 мая 2026 г., 22_26_35 (5).png",
    "gallery-door-ornate-alt.webp": "ChatGPT Image 10 мая 2026 г., 22_26_35 (6).png",
    "gallery-wall-panel-source.webp": "ChatGPT Image 10 мая 2026 г., 22_26_34 (4).png",
    "gallery-wall-panel-corner-source.webp": "ChatGPT Image 10 мая 2026 г., 22_26_34 (4).png",
    "gallery-ceiling-coffered.webp": "ChatGPT Image 10 мая 2026 г., 22_26_35 (7).png",
}


@dataclass(frozen=True)
class Artwork:
    slug: str
    title: str
    subtitle: str
    source: str
    shape: str
    price: str
    placement: str
    x: float
    y: float
    z: float
    ry: float
    width: float
    height: float
    note: str
    intent: str


ARTWORKS = [
    Artwork(
        slug="blue-flower-harmony",
        title="Гармония и чувственность",
        subtitle="Круглая центральная работа",
        source="ChatGPT Image 11 мая 2026 г., 00_08_10 (10).png",
        shape="round",
        price="700 000 ₽",
        placement="pedestal",
        x=0,
        y=0.72,
        z=-8,
        ry=0,
        width=4.0,
        height=4.0,
        note="Центральная работа с глубоким синим цветком и золотым ядром.",
        intent="Гармония, чувственность, восстановление личного ресурса.",
    ),
    Artwork(
        slug="turquoise-protection",
        title="Ясность и защита",
        subtitle="Бирюзовая мандала с оком",
        source="ChatGPT Image 11 мая 2026 г., 00_08_06 (6).png",
        shape="square",
        price="420 000 ₽",
        placement="left",
        x=-8.6,
        y=0.45,
        z=-14,
        ry=70,
        width=3.4,
        height=3.4,
        note="Бирюзовая работа с жемчужной фактурой и центральным оком.",
        intent="Ясность, защита, ощущение внутренней опоры.",
    ),
    Artwork(
        slug="lotus-balance",
        title="Баланс и восстановление",
        subtitle="Бирюзовая геометрия с лотосами",
        source="ChatGPT Image 11 мая 2026 г., 00_08_03 (2).png",
        shape="square",
        price="280 000 ₽",
        placement="right",
        x=8.6,
        y=0.45,
        z=-18,
        ry=-70,
        width=3.5,
        height=3.5,
        note="Лотосы и мягкая геометрия собирают композицию в спокойный ритм.",
        intent="Баланс, мягкое восстановление, спокойная настройка пространства.",
    ),
    Artwork(
        slug="violet-galaxy",
        title="Энергия и ресурс",
        subtitle="Фиолетовая галактика со стразами",
        source="ChatGPT Image 11 мая 2026 г., 00_08_06 (7).png",
        shape="square",
        price="360 000 ₽",
        placement="left",
        x=-8.6,
        y=0.45,
        z=-24,
        ry=70,
        width=3.35,
        height=3.35,
        note="Темная основа, фиолетовые круги, золотые акценты и световые блики.",
        intent="Ресурс, энергия, собранность, внутренняя концентрация.",
    ),
    Artwork(
        slug="orchid-rings",
        title="Тонкая настройка",
        subtitle="Орхидея и пересекающиеся круги",
        source="ChatGPT Image 11 мая 2026 г., 00_08_08 (8).png",
        shape="square",
        price="190 000 ₽",
        placement="right",
        x=8.6,
        y=0.45,
        z=-28,
        ry=-70,
        width=3.35,
        height=3.35,
        note="Фиолетовые поля и цветок в центре делают работу камерной и мягкой.",
        intent="Тонкая настройка, эстетика, спокойная эмоциональная фокусировка.",
    ),
    Artwork(
        slug="personal-code-speed",
        title="Скорость восстановления",
        subtitle="Персональный код на голубом поле",
        source="ChatGPT Image 11 мая 2026 г., 00_08_03 (1).png",
        shape="square",
        price="320 000 ₽",
        placement="center",
        x=0,
        y=0.72,
        z=-36,
        ry=0,
        width=3.7,
        height=3.7,
        note="Работа с числовым рядом и мягкими лотосами по краям.",
        intent="Скорость, ясный ритм, персональная формула под запрос.",
    ),
    Artwork(
        slug="finance-realization",
        title="Финансовая реализация",
        subtitle="Фиолетовая спираль",
        source="ChatGPT Image 11 мая 2026 г., 00_08_03 (3).png",
        shape="square",
        price="310 000 ₽",
        placement="left",
        x=-8.6,
        y=0.45,
        z=-42,
        ry=70,
        width=3.35,
        height=3.35,
        note="Лаконичная спираль и числовой ряд на мягком фиолетовом поле.",
        intent="Реализация, структура цели, фокус на финансовом запросе.",
    ),
    Artwork(
        slug="sensitivity-purple",
        title="Чувственность",
        subtitle="Симметрия шести лепестков",
        source="ChatGPT Image 11 мая 2026 г., 00_08_06 (4).png",
        shape="square",
        price="170 000 ₽",
        placement="right",
        x=8.6,
        y=0.45,
        z=-46,
        ry=-70,
        width=3.35,
        height=3.35,
        note="Нежная светлая работа с фиолетовым лепестковым знаком.",
        intent="Чувственность, мягкость, принятие себя и своего состояния.",
    ),
    Artwork(
        slug="eye-vortex",
        title="Око потока",
        subtitle="Цветовой вихрь",
        source="ChatGPT Image 11 мая 2026 г., 00_08_06 (5).png",
        shape="square",
        price="260 000 ₽",
        placement="center",
        x=0,
        y=0.72,
        z=-54,
        ry=0,
        width=3.8,
        height=3.8,
        note="Цветовые поля сходятся к глазу как к центру наблюдения.",
        intent="Внимание, видение, переход от хаоса к ясной картине.",
    ),
    Artwork(
        slug="gold-blue-gate",
        title="Кодовые врата",
        subtitle="Золотые линии и синий центр",
        source="ChatGPT Image 11 мая 2026 г., 00_08_08 (9).png",
        shape="wide",
        price="380 000 ₽",
        placement="right",
        x=8.6,
        y=0.2,
        z=-60,
        ry=-70,
        width=4.6,
        height=2.9,
        note="Широкая работа с золотой фактурой, синим центром и декоративным знаком.",
        intent="Порог, переход, настройка пространства под новый этап.",
    ),
]


def ensure_dirs() -> None:
    for path in (OUT, ART_DIR, SCENE_DIR, VENDOR_DIR, DATA_DIR, ROOT / "output"):
        path.mkdir(parents=True, exist_ok=True)


def enhance_and_save(src: Path, dst: Path, max_size: int, quality: int) -> None:
    with Image.open(src) as img:
        img = ImageOps.exif_transpose(img).convert("RGB")
        img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
        img = ImageEnhance.Contrast(img).enhance(1.04)
        img = ImageEnhance.Sharpness(img).enhance(1.08)
        img.save(dst, "WEBP", quality=quality, method=6)


def save_scene_asset(src: Path, dst: Path, max_size: int, quality: int, crop: tuple[float, float, float, float] | None = None) -> None:
    with Image.open(src) as img:
        img = ImageOps.exif_transpose(img).convert("RGB")
        if crop:
            w, h = img.size
            left, top, right, bottom = crop
            img = img.crop((int(w * left), int(h * top), int(w * right), int(h * bottom)))
        img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
        img = ImageEnhance.Contrast(img).enhance(1.05)
        img = ImageEnhance.Sharpness(img).enhance(1.05)
        img.save(dst, "WEBP", quality=quality, method=6)


def build_assets() -> None:
    concept_src = DOWNLOADS / "ChatGPT Image 10 мая 2026 г., 15_28_29.png"
    enhance_and_save(concept_src, ASSETS / "tatiana_munn_gallery_concept.webp", 1800, 84)
    for output_name, source_name in SCENE_ASSETS.items():
        save_scene_asset(DOWNLOADS / source_name, SCENE_DIR / output_name, 2200, 86)
    with Image.open(SCENE_DIR / "gallery-door-ornate.webp") as img:
        ImageOps.mirror(img).save(SCENE_DIR / "gallery-door-ornate-mirror.webp", "WEBP", quality=86, method=6)
    save_scene_asset(
        DOWNLOADS / "ChatGPT Image 10 мая 2026 г., 22_26_34 (4).png",
        SCENE_DIR / "gallery-wall-panel-texture.webp",
        1400,
        86,
        crop=(0.02, 0.08, 0.98, 0.88),
    )
    for index, art in enumerate(ARTWORKS, start=1):
        src = DOWNLOADS / art.source
        full = ART_DIR / f"{index:02d}-{art.slug}.webp"
        thumb = ART_DIR / f"{index:02d}-{art.slug}-thumb.webp"
        enhance_and_save(src, full, 1600, 84)
        enhance_and_save(src, thumb, 520, 78)


def price_to_int(price: str) -> int:
    value = re.sub(r"\D+", "", price)
    if not value:
        raise ValueError(f"Cannot parse artwork price: {price!r}")
    return int(value)


def cdn_url(path: str) -> str:
    return f"{TILDA_CDN_BASE.rstrip('/')}/{path.lstrip('/')}"


def tilda_asset_html(html: str) -> str:
    html = html.replace('href="index.html"', f'href="{TILDA_PAGE_URL}"')
    html = html.replace('href="catalog.html"', 'href="#catalog"')
    html = html.replace('href="code.html"', 'href="#personal-code"')
    html = html.replace('href="about.html"', 'href="#gallery-about"')
    html = html.replace('href="contacts.html"', 'href="#gallery-contacts"')
    html = re.sub(r'href="artwork-[^"]+\.html"', 'href="#catalog"', html)
    html = html.replace('src="assets/', f'src="{cdn_url("assets/")}')
    html = html.replace('href="favicon.svg"', f'href="{cdn_url("favicon.svg")}"')
    return html


def ensure_three_vendor() -> None:
    target = VENDOR_DIR / "three.module.min.js"
    if target.exists() and target.stat().st_size > 100_000:
        return
    try:
        urllib.request.urlretrieve(THREE_URL, target)
    except Exception:
        target.write_text(
            "export * from 'https://unpkg.com/three@0.164.1/build/three.module.min.js';\n",
            encoding="utf-8",
        )


def artwork_records() -> list[dict[str, object]]:
    records = []
    for index, art in enumerate(ARTWORKS, start=1):
        image_path = f"assets/art/{index:02d}-{art.slug}.webp"
        thumb_path = f"assets/art/{index:02d}-{art.slug}-thumb.webp"
        price_value = price_to_int(art.price)
        checkout_name = f"{art.title} — картина Татьяны Мунн"
        records.append(
            {
                "id": f"tm-art-{index:02d}",
                "slug": art.slug,
                "title": art.title,
                "subtitle": art.subtitle,
                "shape": art.shape,
                "price": art.price,
                "priceValue": price_value,
                "priceCurrency": "RUB",
                "sku": f"moonn-art-gallery-{index:02d}-{art.slug}",
                "checkoutName": checkout_name,
                "checkoutImage": cdn_url(image_path),
                "tildaProductHref": f"#order:{checkout_name} ={price_value}:::image={cdn_url(image_path)}",
                "placement": art.placement,
                "image": image_path,
                "thumb": thumb_path,
                "detailUrl": f"artwork-{art.slug}.html",
                "scene": {
                    "x": art.x,
                    "y": art.y,
                    "z": art.z,
                    "ry": art.ry,
                    "width": art.width,
                    "height": art.height,
                },
                "note": art.note,
                "intent": art.intent,
            }
        )
    return records


def nav(active: str = "") -> str:
    items = [
        ("index.html", "Галерея"),
        ("catalog.html", "Каталог"),
        ("code.html", "Индивидуальный код"),
        ("about.html", "О Татьяне"),
        ("contacts.html", "Контакты"),
    ]
    links = "\n".join(
        f'<a class="{"is-active" if label == active else ""}" href="{href}">{label}</a>'
        for href, label in items
    )
    return f"""
<header class="site-header">
  <a class="brand" href="index.html" aria-label="Галерея Татьяны Мунн">
    <span class="brand-mark">TM</span>
    <span><b>Татьяна Мунн</b><small>галерея энергетических картин</small></span>
  </a>
  <nav class="site-nav" aria-label="Основная навигация">{links}</nav>
  <button class="gold-button compact" data-open-purchase>Купить картину</button>
</header>"""


def html_shell(
    title: str,
    description: str,
    body: str,
    active: str = "",
    extra_head: str = "",
    canonical_path: str = "art-gallery",
) -> str:
    canonical_url = f"https://moonn.ru/{canonical_path.strip('/')}"
    schema = {
        "@context": "https://schema.org",
        "@type": "ArtGallery",
        "name": "Галерея энергетических картин Татьяны Мунн",
        "url": canonical_url,
        "founder": {"@type": "Person", "name": "Татьяна Мунн"},
        "description": description,
    }
    return f"""<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(description)}">
  <meta name="robots" content="index,follow">
  <link rel="canonical" href="{canonical_url}">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:title" content="{escape(title)}">
  <meta property="og:description" content="{escape(description)}">
  <meta property="og:image" content="assets/tatiana_munn_gallery_concept.webp">
  <link rel="stylesheet" href="style.css">
  <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
  {extra_head}
</head>
<body>
{nav(active)}
{body}
{purchase_drawer()}
<script src="app.js"></script>
</body>
</html>
"""


def purchase_drawer() -> str:
    return """
<aside class="purchase-drawer" id="purchaseDrawer" aria-hidden="true" aria-label="Заявка на покупку картины">
  <div class="purchase-drawer__shade" data-close-purchase></div>
  <form class="purchase-drawer__panel">
    <button class="icon-close" type="button" data-close-purchase aria-label="Закрыть">×</button>
    <span class="eyebrow">Запрос на покупку</span>
    <h2>Забронировать картину</h2>
    <p>Оставьте контакты, чтобы согласовать наличие, формат, персональный код, доставку и способ оплаты.</p>
    <label>Картина<input name="artwork" id="purchaseArtwork" value="Гармония и чувственность"></label>
    <label>Имя<input name="name" placeholder="Ваше имя"></label>
    <label>Телефон или Telegram<input name="contact" placeholder="+7 ... / @username"></label>
    <label>Комментарий<textarea name="message" rows="4" placeholder="Какая работа интересна и какой запрос хотите заложить в код"></textarea></label>
    <button class="gold-button" type="button" data-copy-request>Сформировать текст заявки</button>
    <small>После заявки с вами согласуют наличие работы, персональную настройку, доставку и удобный способ оплаты.</small>
  </form>
</aside>
"""


def build_index(records: list[dict[str, object]]) -> None:
    gallery_cards = "\n".join(
        f"""
      <article class="art-market-card">
        <a href="{record['detailUrl']}" aria-label="{escape(str(record['title']))}">
          <img src="{record['thumb']}" alt="{escape(str(record['title']))} — картина Татьяны Мунн">
        </a>
        <div>
          <span>{escape(str(record['subtitle']))}</span>
          <h3>{escape(str(record['title']))}</h3>
          <p>{escape(str(record['intent']))}</p>
          <b>{escape(str(record['price']))}</b>
          <button class="gold-button compact" type="button" data-open-purchase data-art-id="{escape(str(record['id']))}">Купить картину</button>
        </div>
      </article>"""
        for record in records
    )
    body = f"""
<main class="immersive-page" id="gallery">
  <canvas id="galleryCanvas" aria-label="3D-зал энергетических картин Татьяны Мунн"></canvas>
  <div class="scroll-meter"><span id="scrollMeter"></span></div>
  <div class="entry-doors" aria-hidden="true">
    <div class="entry-doors__hall"></div>
    <div class="entry-door entry-door--left"><span></span></div>
    <div class="entry-door entry-door--right"><span></span></div>
  </div>
  <section class="story-section hero-section">
    <div class="hero-copy">
      <span class="eyebrow">Премиальная 3D-галерея</span>
      <h1>Галерея энергетических картин<br><strong>Татьяна Мунн</strong></h1>
      <p>Прокручивайте страницу: камера входит в зал, проходит вдоль стен, подходит к работам на пьедесталах и подсвечивает каждую картину как в частной выставке.</p>
      <div class="hero-actions">
        <a class="gold-button" href="#walk">Войти в зал</a>
        <a class="ghost-button" href="#catalog">Открыть каталог</a>
      </div>
    </div>
  </section>
  <section class="story-section side-copy" id="walk">
    <div class="glass-text right">
      <span class="eyebrow">Экспозиция</span>
      <h2>Стены, пьедесталы и личные таблички</h2>
      <p>Работы расположены как в камерном выставочном зале: крупные полотна на стенах, круглая картина в центре, рядом подписи с назначением и запросом.</p>
    </div>
  </section>
  <section class="story-section side-copy">
    <div class="glass-text right">
      <span class="eyebrow">Выбор картины</span>
      <h2>Кликните по полотну</h2>
      <p>Любую работу можно открыть крупно, перевернуть и увидеть оборот с персональным кодом владельца.</p>
      <button class="ghost-button" data-preview-art>Показать просмотр</button>
    </div>
  </section>
  <section class="story-section side-copy">
    <div class="glass-text right">
      <span class="eyebrow">Индивидуальный код</span>
      <h2>Формула под человека</h2>
      <p>Покупатель вводит данные и запрос. Код связывается с выбранной работой, оборотом картины и сертификатом владельца.</p>
      <a class="gold-button" href="#personal-code">Составить код</a>
    </div>
  </section>
  <section class="story-section side-copy">
    <div class="glass-text right">
      <span class="eyebrow">Фактура</span>
      <h2>Золото, жемчуг, стразы и свет</h2>
      <p>Объёмные линии, жемчужные детали, стеклянные блики и золотые акценты создают ощущение живой поверхности и частной коллекции.</p>
    </div>
  </section>
  <section class="story-section final-section">
    <div class="glass-text center">
      <span class="eyebrow">Частная покупка</span>
      <h2>Выберите работу для себя или в подарок</h2>
      <p>Посмотрите работы в 3D-зале, откройте выбранную картину крупно, добавьте персональный код и оформите покупку через безопасную оплату на сайте.</p>
      <div class="hero-actions">
        <a class="gold-button" href="#catalog">Перейти в каталог</a>
        <button class="ghost-button" data-open-purchase data-art-id="tm-art-01">Купить картину</button>
      </div>
    </div>
  </section>
  <section class="art-market-section" id="catalog" aria-label="Каталог картин Татьяны Мунн">
    <div class="art-market-heading">
      <span class="eyebrow">Каталог</span>
      <h2>Купить картину Татьяны Мунн</h2>
      <p>Каждая работа продаётся как авторский арт-объект. После выбора картины можно добавить индивидуальный код, согласовать детали и оформить оплату.</p>
    </div>
    <div class="art-market-grid">
{gallery_cards}
    </div>
  </section>
  <section class="personal-code-section" id="personal-code" aria-label="Индивидуальный код для картины">
    <div class="code-intro">
      <span class="eyebrow">Персональная настройка</span>
      <h2>Каждая картина может быть настроена под вас лично</h2>
      <p>ФИО, дата рождения, время рождения и запрос используются для расчёта персонального числового кода. Код можно связать с оборотом картины и сертификатом владельца.</p>
      <div class="code-steps" aria-label="Данные для составления кода">
        <div><span>1</span><b>ФИО</b></div>
        <div><span>2</span><b>Дата рождения</b></div>
        <div><span>3</span><b>Время рождения</b></div>
        <div><span>4</span><b>Ваш запрос</b></div>
      </div>
    </div>
    <form class="premium-form code-inline-form" id="codeForm">
      <label>Фамилия, имя, отчество<input id="fio" value="Иванов Иван Иванович"></label>
      <label>Дата рождения<input id="birth" type="date" value="1985-05-12"></label>
      <label>Время рождения<input id="birthTime" type="time" value="14:30"></label>
      <label>Запрос<textarea id="request" rows="4">гармония, ресурс, реализация</textarea></label>
      <button class="gold-button" type="submit">Составить код</button>
      <strong class="inline-code-result js-code">516 108 369</strong>
    </form>
  </section>
  <section class="gallery-features" aria-label="Почему картины особенные">
    <span class="eyebrow">Почему мои картины особенные</span>
    <div class="feature-grid">
      <article><b>Энергетический инструмент</b><span>Картина работает как акцент пространства и состояния.</span></article>
      <article><b>Индивидуальная настройка</b><span>Работа может быть связана с персональным кодом владельца.</span></article>
      <article><b>Авторская техника</b><span>Фактура, цвет, символы и ручная детализация.</span></article>
      <article><b>Премиальные материалы</b><span>Холсты, объёмные линии, жемчуг, стразы и золото.</span></article>
      <article><b>Подлинность</b><span>Работа согласуется как личный арт-объект.</span></article>
      <article><b>Создано с любовью</b><span>Каждая картина собирается для человека и пространства.</span></article>
    </div>
  </section>
</main>
<div class="art-modal" id="artModal" aria-hidden="true">
  <div class="art-modal__shade" data-close-art></div>
  <article class="art-modal__panel">
    <button class="icon-close" type="button" data-close-art aria-label="Закрыть">×</button>
    <div class="flip-card" id="flipCard">
      <div class="flip-card__inner">
        <div class="flip-face front"><img id="modalImage" alt=""></div>
        <div class="flip-face back">
          <span>Персональный код</span>
          <strong class="js-code">516 108 369</strong>
          <small>ФИО, дата рождения и запрос владельца наносятся на оборот или сертификат по согласованию.</small>
        </div>
      </div>
    </div>
    <div class="modal-copy">
      <span class="eyebrow">Выбранная работа</span>
      <h2 id="modalTitle">Гармония и чувственность</h2>
      <p id="modalText"></p>
      <div class="modal-actions">
        <button class="gold-button" id="flipButton" type="button">Перевернуть</button>
        <button class="ghost-button" type="button" data-open-purchase>Забронировать</button>
        <a class="ghost-button" id="modalDetail" href="catalog.html">Страница картины</a>
      </div>
    </div>
  </article>
</div>
<script type="application/json" id="artworksData">__ARTWORKS__</script>
<script type="module" src="gallery-3d.js"></script>
""".replace("__ARTWORKS__", json.dumps(records, ensure_ascii=False))
    (OUT / "index.html").write_text(
        html_shell(
            "Галерея энергетических картин Татьяны Мунн | 3D-прогулка и индивидуальный код",
            "Премиальная 3D-галерея картин Татьяны Мунн: прогулка по залу, каталог работ, индивидуальный код и покупка картин онлайн.",
            body,
            "Галерея",
            canonical_path=TILDA_PAGE_ALIAS,
        ),
        encoding="utf-8",
    )


def build_catalog(records: list[dict[str, object]]) -> None:
    cards = "\n".join(
        f"""
<article class="catalog-card">
  <a href="{record['detailUrl']}"><img src="{record['thumb']}" alt="{escape(str(record['title']))}"></a>
  <div>
    <span>{escape(str(record['subtitle']))}</span>
    <h2>{escape(str(record['title']))}</h2>
    <p>{escape(str(record['intent']))}</p>
    <b>{escape(str(record['price']))}</b>
    <div class="card-actions">
      <a class="ghost-button" href="{record['detailUrl']}">Подробнее</a>
      <button class="gold-button compact" data-open-purchase data-art-title="{escape(str(record['title']))}">Купить</button>
    </div>
  </div>
</article>"""
        for record in records
    )
    body = f"""
<main class="page-shell catalog-page">
  <section class="page-hero split-hero">
    <div>
      <span class="eyebrow">Каталог работ</span>
      <h1>Картины Татьяны Мунн</h1>
      <p>Камерная подборка работ с персональным кодом, фактурными материалами и возможностью индивидуальной настройки под запрос владельца.</p>
    </div>
    <img src="assets/tatiana_munn_gallery_concept.webp" alt="Постер галереи Татьяны Мунн">
  </section>
  <section class="catalog-grid">{cards}</section>
</main>
"""
    (OUT / "catalog.html").write_text(
        html_shell(
            "Каталог картин Татьяны Мунн | энергетические картины с персональным кодом",
            "Каталог картин Татьяны Мунн: оригинальные работы, фактура, персональный код, заявка на покупку.",
            body,
            "Каталог",
            canonical_path="art-gallery/catalog",
        ),
        encoding="utf-8",
    )


def build_artwork_pages(records: list[dict[str, object]]) -> None:
    for record in records:
        related = "\n".join(
            f'<a href="{other["detailUrl"]}"><img src="{other["thumb"]}" alt="{escape(str(other["title"]))}"><span>{escape(str(other["title"]))}</span></a>'
            for other in records[:4]
            if other["slug"] != record["slug"]
        )
        body = f"""
<main class="page-shell artwork-page">
  <section class="artwork-detail">
    <div class="artwork-detail__image"><img src="{record['image']}" alt="{escape(str(record['title']))}"></div>
    <article class="artwork-detail__copy">
      <span class="eyebrow">{escape(str(record['subtitle']))}</span>
      <h1>{escape(str(record['title']))}</h1>
      <p>{escape(str(record['note']))}</p>
      <p>{escape(str(record['intent']))}</p>
      <dl class="spec-list">
        <div><dt>Формат</dt><dd>{escape(str(record['shape']))}</dd></div>
        <div><dt>Стоимость</dt><dd>{escape(str(record['price']))}</dd></div>
        <div><dt>Персональный код</dt><dd>добавляется по запросу</dd></div>
      </dl>
      <div class="hero-actions">
        <button class="gold-button" data-open-purchase data-art-title="{escape(str(record['title']))}">Забронировать работу</button>
        <a class="ghost-button" href="code.html">Составить код</a>
      </div>
    </article>
  </section>
  <section class="related-strip">
    <h2>Ещё работы</h2>
    <div>{related}</div>
  </section>
</main>
"""
        (OUT / f"artwork-{record['slug']}.html").write_text(
            html_shell(
                f"{record['title']} | картина Татьяны Мунн",
                f"{record['title']} — работа Татьяны Мунн с персональным кодом и заявкой на покупку.",
                body,
                "Каталог",
                canonical_path=f"art-gallery/{record['slug']}",
            ),
            encoding="utf-8",
        )


def build_code_page() -> None:
    body = """
<main class="page-shell code-page">
  <section class="page-hero code-hero">
    <span class="eyebrow">Персональная формула</span>
    <h1>Индивидуальный код для картины</h1>
    <p>Введите данные и запрос, чтобы получить персональный числовой код для выбранной картины.</p>
  </section>
  <section class="code-layout">
    <article class="code-intro">
      <div>
        <span class="eyebrow">Каждая картина может быть настроена под вас лично</span>
        <h2>Персональный код соединяет работу с вашим запросом</h2>
        <p>Данные владельца и запрос помогают подготовить числовой ряд для оборота картины и сертификата.</p>
      </div>
      <div class="code-steps" aria-label="Данные для составления кода">
        <div><span>1</span><b>ФИО</b></div>
        <div><span>2</span><b>Дата рождения</b></div>
        <div><span>3</span><b>Время рождения</b></div>
        <div><span>4</span><b>Ваш запрос</b></div>
      </div>
      <p class="code-note">Искусство, написанное для вашей души</p>
    </article>
    <form class="premium-form" id="codeForm">
      <label>Фамилия, имя, отчество<input id="fio" value="Иванов Иван Иванович"></label>
      <label>Дата рождения<input id="birth" type="date" value="1985-05-12"></label>
      <label>Время рождения<input id="birthTime" type="time" value="14:30"></label>
      <label>Запрос<textarea id="request" rows="4">гармония, ресурс, реализация</textarea></label>
      <button class="gold-button" type="submit">Составить код</button>
    </form>
    <article class="code-result-card">
      <span class="eyebrow">Ваш код</span>
      <strong id="codeValue" class="js-code">516 108 369</strong>
      <p>Этот блок связан с оборотом картины и сертификатом владельца.</p>
    </article>
  </section>
</main>
"""
    (OUT / "code.html").write_text(
        html_shell(
            "Индивидуальный код для картины Татьяны Мунн",
            "Форма индивидуального кода для картины Татьяны Мунн: ФИО, дата рождения, время рождения и запрос.",
            body,
            "Индивидуальный код",
            canonical_path="art-gallery/code",
        ),
        encoding="utf-8",
    )


def build_about_contacts() -> None:
    about = """
<main class="page-shell">
  <section class="page-hero">
    <span class="eyebrow">О художнике</span>
    <h1>Татьяна Мунн</h1>
    <p>Татьяна Мунн создаёт фактурные картины, где цвет, символ, число и ручная работа собираются в персональный арт-объект для пространства владельца.</p>
  </section>
  <section class="content-grid">
    <article><h2>Подход</h2><p>Работы строятся вокруг запроса, визуального ритма, фактуры и индивидуального кода. Сайт показывает этот путь как частную прогулку по галерее.</p></article>
    <article><h2>Формат</h2><p>Картины могут быть выбраны из готовой коллекции или настроены под человека. Детали согласуются перед покупкой.</p></article>
  </section>
</main>
"""
    contacts = """
<main class="page-shell">
  <section class="page-hero">
    <span class="eyebrow">Контакты</span>
    <h1>Запрос на покупку картины</h1>
    <p>Выберите работу в каталоге или оставьте общий запрос. После подтверждения наличия и условий с вами согласуют удобный способ оплаты.</p>
    <button class="gold-button" data-open-purchase>Оставить заявку</button>
  </section>
</main>
"""
    (OUT / "about.html").write_text(
        html_shell(
            "О Татьяне Мунн | галерея энергетических картин",
            "О Татьяне Мунн и авторском подходе к фактурным картинам с персональным кодом.",
            about,
            "О Татьяне",
            canonical_path="art-gallery/about",
        ),
        encoding="utf-8",
    )
    (OUT / "contacts.html").write_text(
        html_shell(
            "Контакты галереи Татьяны Мунн | купить картину",
            "Контакты и заявка на покупку картины Татьяны Мунн.",
            contacts,
            "Контакты",
            canonical_path="art-gallery/contacts",
        ),
        encoding="utf-8",
    )


STYLE_CSS = r"""
:root{--bg:#07080d;--panel:#11131b;--ink:#f8edda;--muted:#c7bdc8;--gold:#d8aa5d;--gold2:#ffe7aa;--aqua:#5fd6df;--violet:#8e55ff;--line:rgba(255,226,172,.24);--glass:rgba(12,15,24,.70)}
*{box-sizing:border-box}html{scroll-behavior:smooth;background:var(--bg);color:var(--ink)}body{margin:0;font-family:Inter,Segoe UI,Arial,sans-serif;background:radial-gradient(circle at 20% 0%,rgba(63,44,97,.38),transparent 34%),linear-gradient(180deg,#06070b,#0b1118 55%,#07080d);color:var(--ink)}a{color:inherit;text-decoration:none}img{max-width:100%;display:block}.site-header{position:fixed;inset:0 0 auto 0;height:78px;z-index:50;display:flex;align-items:center;gap:28px;padding:0 clamp(18px,4vw,64px);background:rgba(4,6,10,.72);border-bottom:1px solid var(--line);backdrop-filter:blur(18px)}.brand{display:flex;align-items:center;gap:12px;min-width:240px}.brand-mark{display:grid;place-items:center;width:40px;height:40px;border-radius:12px;background:linear-gradient(135deg,#402d6a,#42c7d2);box-shadow:0 0 28px rgba(95,214,223,.24)}.brand b{display:block;font-family:Georgia,serif;font-size:22px;color:var(--gold2);font-weight:400}.brand small{display:block;color:#c8c1cc;font-size:12px}.site-nav{display:flex;justify-content:center;gap:22px;flex:1}.site-nav a{color:#dcd5df;font-size:13px}.site-nav a.is-active,.site-nav a:hover{color:var(--gold2)}button{font:inherit}.gold-button,.ghost-button{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:0 22px;border-radius:999px;border:1px solid rgba(255,226,172,.42);cursor:pointer}.gold-button{background:linear-gradient(135deg,#a06b27,#f3cf82 52%,#8a5f25);color:#171014;font-weight:700;box-shadow:0 12px 34px rgba(216,170,93,.22)}.ghost-button{background:rgba(255,255,255,.06);color:#f5ead9}.compact{min-height:40px;padding-inline:16px;font-size:13px}.immersive-page{min-height:620vh}.immersive-page canvas{position:fixed;inset:0;width:100vw;height:100vh;z-index:1;background:#05070b}.scroll-meter{position:fixed;left:0;right:0;top:0;height:2px;z-index:80;background:rgba(255,255,255,.08)}.scroll-meter span{display:block;height:100%;width:0;background:linear-gradient(90deg,var(--aqua),var(--gold),var(--violet));box-shadow:0 0 18px var(--gold)}.story-section{position:relative;z-index:10;min-height:100vh;padding:120px clamp(18px,6vw,92px);display:flex;align-items:center;pointer-events:none}.hero-section{justify-content:center;text-align:center;align-items:flex-start;padding-top:20vh}.hero-copy,.glass-text{pointer-events:auto}.hero-copy{max-width:980px}.eyebrow{display:inline-flex;align-items:center;gap:10px;margin-bottom:16px;color:var(--gold2);font-size:12px;text-transform:uppercase;letter-spacing:.22em}.eyebrow:before{content:"";width:34px;height:1px;background:linear-gradient(90deg,var(--gold),transparent)}h1,h2{font-family:Georgia,serif;font-weight:400;line-height:1;margin:0;color:#fff2d8;text-wrap:balance}h1{font-size:clamp(48px,7vw,112px)}h1 strong{color:var(--gold2);font-weight:400}h2{font-size:clamp(34px,4vw,68px)}p{color:var(--muted);line-height:1.72;font-size:clamp(15px,1.3vw,18px)}.hero-copy p{max-width:760px;margin:24px auto}.hero-actions,.modal-actions,.card-actions{display:flex;gap:14px;flex-wrap:wrap}.hero-actions{justify-content:center}.glass-text{max-width:560px;padding:30px;border:1px solid var(--line);border-radius:22px;background:linear-gradient(135deg,rgba(9,12,19,.76),rgba(24,19,34,.58));box-shadow:0 24px 70px rgba(0,0,0,.42),inset 0 1px 0 rgba(255,255,255,.05);backdrop-filter:blur(14px)}.glass-text.left{margin-right:auto}.glass-text.right{margin-left:auto}.glass-text.center{margin:auto;text-align:center}.final-section{min-height:120vh}.page-shell{padding:120px clamp(18px,6vw,88px) 70px;min-height:100vh}.page-hero{max-width:960px;margin:0 auto 44px}.split-hero{display:grid;grid-template-columns:1fr minmax(280px,460px);gap:34px;align-items:center;max-width:1180px}.split-hero img,.artwork-detail__image img,.catalog-card img{border-radius:18px;border:1px solid var(--line);box-shadow:0 24px 70px rgba(0,0,0,.44)}.catalog-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:22px;max-width:1220px;margin:auto}.catalog-card{display:grid;grid-template-columns:220px 1fr;gap:20px;padding:18px;border:1px solid var(--line);border-radius:20px;background:var(--glass)}.catalog-card img{aspect-ratio:1;object-fit:cover}.catalog-card span{color:var(--gold2);font-size:12px;letter-spacing:.12em;text-transform:uppercase}.catalog-card h2{font-size:28px;margin:8px 0}.catalog-card b{display:block;margin:12px 0 16px;color:var(--gold2);font-size:20px}.artwork-detail{display:grid;grid-template-columns:minmax(320px,580px) 1fr;gap:42px;align-items:center;max-width:1180px;margin:auto}.artwork-detail__image img{max-height:72vh;object-fit:contain;background:#0b0e14}.spec-list{display:grid;gap:12px;margin:24px 0}.spec-list div{display:flex;justify-content:space-between;gap:18px;border-bottom:1px solid rgba(255,226,172,.14);padding-bottom:10px}.spec-list dt{color:#b8afbd}.spec-list dd{margin:0;color:var(--gold2)}.related-strip{max-width:1180px;margin:70px auto 0}.related-strip>div{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.related-strip a{display:grid;gap:10px;color:#eee}.related-strip img{aspect-ratio:1;object-fit:cover;border-radius:16px}.code-layout,.content-grid{display:grid;grid-template-columns:1fr 1fr;gap:28px;max-width:1080px;margin:auto}.premium-form,.code-result-card,.content-grid article{padding:28px;border:1px solid var(--line);border-radius:22px;background:var(--glass)}label{display:block;margin:0 0 14px;color:#d7cddc;font-size:13px;letter-spacing:.08em;text-transform:uppercase}input,textarea{width:100%;margin-top:8px;padding:13px 14px;border-radius:12px;border:1px solid rgba(255,226,172,.2);background:rgba(0,0,0,.28);color:#fff;font:inherit;text-transform:none;letter-spacing:0}.code-result-card strong{display:block;font-family:Georgia,serif;font-size:64px;color:var(--gold2);text-shadow:0 0 28px rgba(216,170,93,.35)}.purchase-drawer,.art-modal{position:fixed;inset:0;z-index:100;display:none}.purchase-drawer[aria-hidden=false],.art-modal[aria-hidden=false]{display:block}.purchase-drawer__shade,.art-modal__shade{position:absolute;inset:0;background:rgba(1,2,5,.76);backdrop-filter:blur(10px)}.purchase-drawer__panel{position:absolute;right:0;top:0;bottom:0;width:min(480px,94vw);overflow:auto;padding:36px;border-left:1px solid var(--line);background:#0c1018}.icon-close{position:absolute;right:18px;top:18px;width:42px;height:42px;border-radius:50%;border:1px solid var(--line);background:rgba(255,255,255,.06);color:#fff;font-size:28px;cursor:pointer}.art-modal__panel{position:relative;z-index:1;width:min(1060px,94vw);min-height:620px;margin:7vh auto;display:grid;grid-template-columns:minmax(320px,520px) 1fr;gap:28px;align-items:center;padding:28px;border:1px solid var(--line);border-radius:28px;background:linear-gradient(135deg,#0b0f18,#15111d);box-shadow:0 40px 120px rgba(0,0,0,.65)}.flip-card{aspect-ratio:1;perspective:1200px}.flip-card__inner{position:relative;width:100%;height:100%;transform-style:preserve-3d;transition:transform .7s}.flip-card.is-flipped .flip-card__inner{transform:rotateY(180deg)}.flip-face{position:absolute;inset:0;backface-visibility:hidden;overflow:hidden;border-radius:22px;border:1px solid var(--line);display:grid;place-items:center}.flip-face.front img{width:100%;height:100%;object-fit:cover}.flip-face.back{transform:rotateY(180deg);padding:32px;text-align:center;background:radial-gradient(circle at 50% 35%,#fff6df,#d9c5ef);color:#33243c}.flip-face.back strong{font-family:Georgia,serif;font-size:44px;color:#7b541d}.modal-copy h2{margin-bottom:16px}.copy-toast{position:fixed;left:50%;bottom:28px;z-index:200;transform:translateX(-50%);padding:14px 18px;border-radius:999px;background:#121722;border:1px solid var(--line);box-shadow:0 20px 50px rgba(0,0,0,.45)}@media (max-width:900px){.site-nav{display:none}.site-header{height:68px}.brand{min-width:0}.brand small{display:none}.story-section{padding:92px 18px}.hero-actions,.modal-actions{justify-content:center}.catalog-grid,.catalog-card,.artwork-detail,.code-layout,.content-grid,.split-hero,.art-modal__panel{grid-template-columns:1fr}.catalog-card{display:block}.catalog-card img{margin-bottom:16px}.glass-text.left,.glass-text.right{margin:auto}.art-modal__panel{margin:3vh auto;overflow:auto;max-height:94vh}.code-result-card strong{font-size:42px}}@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}.immersive-page canvas{opacity:.35}.story-section{background:rgba(7,8,13,.45)}}
/* art-gallery refinements */
:root{--entry-open:0}.entry-doors{position:fixed;inset:78px 0 0;z-index:3;overflow:hidden;pointer-events:none;perspective:1800px;opacity:calc(1 - var(--entry-open));background:radial-gradient(circle at 50% 42%,rgba(255,216,144,.16),transparent 32%)}.entry-doors__hall{position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.62),rgba(4,7,12,.06),rgba(0,0,0,.62));opacity:.8}.entry-door{position:absolute;top:0;bottom:0;width:50.5vw;max-width:none;background:linear-gradient(90deg,rgba(5,5,6,.18),rgba(8,9,13,.10)),#0a0a0b;background-position:center;background-size:cover;background-repeat:no-repeat;border:1px solid rgba(216,170,93,.48);box-shadow:inset 0 0 0 8px rgba(216,170,93,.08),inset 0 0 0 18px rgba(0,0,0,.30),inset 0 0 70px rgba(216,170,93,.08),0 0 70px rgba(0,0,0,.82);transition:transform .12s linear;transform-style:preserve-3d}.entry-door:before{content:"";position:absolute;inset:5% 7%;border:1px solid rgba(216,170,93,.18);box-shadow:inset 0 0 0 16px rgba(0,0,0,.10),inset 0 0 44px rgba(216,170,93,.08)}.entry-door:after{display:none}.entry-door--left{background-image:linear-gradient(90deg,rgba(5,5,6,.18),rgba(8,9,13,.10)),url("assets/scene/gallery-door-ornate-mirror.webp")}.entry-door--right{background-image:linear-gradient(90deg,rgba(5,5,6,.18),rgba(8,9,13,.10)),url("assets/scene/gallery-door-ornate.webp")}.entry-door span{position:absolute;inset:14% 17%;border:2px solid rgba(216,170,93,.15);border-radius:50%;opacity:.35}.entry-door span:after{content:"";position:absolute;inset:23%;border-radius:50%;border:2px solid rgba(255,226,172,.18);box-shadow:0 0 0 28px rgba(216,170,93,.04),0 0 0 54px rgba(216,170,93,.03)}.entry-door--left{left:0;transform-origin:left center;transform:translateX(calc(var(--entry-open)*-4%)) rotateY(calc(var(--entry-open)*-74deg))}.entry-door--right{right:0;transform-origin:right center;transform:translateX(calc(var(--entry-open)*4%)) rotateY(calc(var(--entry-open)*74deg))}.hero-section{transition:opacity .18s ease}.side-copy{transition:opacity .18s ease}.side-copy .glass-text{max-width:520px}.art-market-section,.personal-code-section{position:relative;z-index:12;padding:86px clamp(18px,6vw,88px);background:linear-gradient(180deg,rgba(8,10,16,.96),rgba(11,15,22,.98));border-top:1px solid var(--line)}.art-market-heading{max-width:940px;margin:0 auto 34px;text-align:center}.art-market-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px;max-width:1240px;margin:auto}.art-market-card{display:grid;grid-template-columns:170px 1fr;gap:18px;align-items:center;padding:16px;border:1px solid rgba(255,226,172,.20);border-radius:18px;background:rgba(12,15,24,.78);box-shadow:0 20px 52px rgba(0,0,0,.26)}.art-market-card img{aspect-ratio:1;object-fit:cover;border-radius:14px;border:1px solid rgba(255,226,172,.18)}.art-market-card span{color:var(--gold2);font-size:11px;letter-spacing:.16em;text-transform:uppercase}.art-market-card h3{margin:6px 0 8px;font-family:Georgia,serif;font-size:25px;font-weight:400;color:#fff2d8}.art-market-card p{margin:0 0 10px;font-size:14px;line-height:1.5}.art-market-card b{display:block;margin:0 0 12px;color:var(--gold2);font-size:18px}.personal-code-section{display:grid;grid-template-columns:1fr minmax(320px,480px);gap:34px;align-items:center}.code-inline-form{border-color:rgba(216,170,93,.42)}.inline-code-result{display:block;margin-top:18px;font-family:Georgia,serif;font-size:42px;line-height:1;color:var(--gold2)}.gallery-features{position:relative;z-index:12;padding:72px clamp(18px,6vw,88px) 88px;border-top:1px solid var(--line);background:linear-gradient(180deg,rgba(11,15,22,.92),rgba(7,8,13,.98));text-align:center}.gallery-features>.eyebrow{justify-content:center}.feature-grid{display:grid;grid-template-columns:repeat(6,1fr);gap:0;max-width:1280px;margin:30px auto 0;border-top:1px solid rgba(255,226,172,.16);border-bottom:1px solid rgba(255,226,172,.16)}.feature-grid article{min-height:150px;padding:24px 18px;border-right:1px solid rgba(255,226,172,.12)}.feature-grid article:last-child{border-right:0}.feature-grid b{display:block;margin-bottom:12px;color:var(--gold2);font-family:Georgia,serif;font-size:18px;font-weight:400;text-transform:uppercase}.feature-grid span{color:#c8c0cc;font-size:14px;line-height:1.55}.code-page{background:radial-gradient(circle at 18% 15%,rgba(65,46,100,.38),transparent 36%),linear-gradient(135deg,#0b0f18,#071019 60%,#0c1018)}.code-page h1{font-size:clamp(46px,6vw,92px)}.code-layout{grid-template-columns:1.08fr .92fr;max-width:1180px;align-items:stretch}.code-intro{display:grid;align-content:center;gap:24px;padding:28px}.code-steps{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}.code-steps span{display:grid;place-items:center;width:68px;height:68px;margin:0 auto 12px;border:1px solid rgba(216,170,93,.55);border-radius:50%;color:var(--gold2);font-family:Georgia,serif;font-size:26px}.code-steps b{display:block;text-align:center;color:#efe6d8;font-size:14px}.code-note{color:var(--gold2);font-family:Georgia,serif;font-size:18px}.code-layout .premium-form{border-color:rgba(216,170,93,.45);box-shadow:0 30px 80px rgba(0,0,0,.32)}.code-result-card{position:relative;overflow:hidden}.code-result-card:after{content:"";position:absolute;right:-50px;bottom:-40px;width:220px;height:220px;background:radial-gradient(circle,rgba(216,170,93,.16),transparent 65%)}@media (max-width:1100px){.feature-grid{grid-template-columns:repeat(3,1fr)}.feature-grid article:nth-child(3n){border-right:0}.art-market-grid,.personal-code-section{grid-template-columns:1fr}}@media (max-width:900px){.entry-doors{inset:68px 0 0}.entry-door{width:51vw}.gallery-features,.art-market-section,.personal-code-section{padding-inline:18px}.feature-grid{grid-template-columns:1fr 1fr}.code-layout,.code-steps{grid-template-columns:1fr}.code-intro{padding:0}.hero-section{padding-top:12vh}.hero-section h1{font-size:clamp(36px,10.6vw,46px);line-height:1.05}.hero-copy p{font-size:14px;line-height:1.55}.hero-actions{gap:10px}.hero-actions .gold-button,.hero-actions .ghost-button{min-height:46px;padding-inline:14px}.side-copy .glass-text{max-width:100%}}@media (max-width:650px){.art-market-card{grid-template-columns:1fr}.art-market-card img{width:100%}}@media (max-width:560px){.feature-grid{grid-template-columns:1fr}.feature-grid article{border-right:0;border-bottom:1px solid rgba(255,226,172,.12)}}
"""


GALLERY_JS = r"""
import * as THREE from './assets/vendor/three.module.min.js';

const canvas = document.getElementById('galleryCanvas');
const dataNode = document.getElementById('artworksData');
const artworks = JSON.parse(dataNode?.textContent || '[]');
const meter = document.getElementById('scrollMeter');
const modal = document.getElementById('artModal');
const modalImage = document.getElementById('modalImage');
const modalTitle = document.getElementById('modalTitle');
const modalText = document.getElementById('modalText');
const modalDetail = document.getElementById('modalDetail');
const flipCard = document.getElementById('flipCard');
const flipButton = document.getElementById('flipButton');
const assetBase = window.MOONN_ART_GALLERY_BASE_URL || '';
const isTildaMode = Boolean(window.MOONN_ART_GALLERY_TILDA_MODE);

function assetUrl(path) {
  if (!path || /^https?:\/\//i.test(path) || path.startsWith('data:')) return path;
  if (!assetBase) return path;
  return `${assetBase.replace(/\/?$/, '/')}${String(path).replace(/^\.?\//, '')}`;
}

const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: false, powerPreference: 'high-performance' });
renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.5));
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.46;
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x151c26);
scene.fog = new THREE.FogExp2(0x0c121b, 0.0037);

const camera = new THREE.PerspectiveCamera(54, 1, 0.1, 120);
camera.position.set(0, 1.2, 5.5);

scene.add(new THREE.HemisphereLight(0xf3ffff, 0x47291a, 1.58));
scene.add(new THREE.AmbientLight(0xfff0d8, 0.38));
const warm = new THREE.PointLight(0xffcf86, 4.1, 62);
warm.position.set(0, 5, -18);
scene.add(warm);
const cool = new THREE.PointLight(0x8cebff, 1.95, 52);
cool.position.set(-4, 3, -38);
scene.add(cool);

const loader = new THREE.TextureLoader();
const clickable = [];
const frames = [];
const panelLights = [];
const artworkLights = [];

function mat(color, roughness = 0.8, metalness = 0.05) {
  return new THREE.MeshStandardMaterial({ color, roughness, metalness });
}

function makeTexture(size, painter, repeatX = 1, repeatY = 1) {
  const c = document.createElement('canvas');
  c.width = size;
  c.height = size;
  const ctx = c.getContext('2d');
  painter(ctx, size);
  const texture = new THREE.CanvasTexture(c);
  texture.colorSpace = THREE.SRGBColorSpace;
  texture.wrapS = THREE.RepeatWrapping;
  texture.wrapT = THREE.RepeatWrapping;
  texture.repeat.set(repeatX, repeatY);
  texture.anisotropy = Math.min(renderer.capabilities.getMaxAnisotropy?.() || 8, 8);
  return texture;
}

function createParquetTexture() {
  return makeTexture(1024, (ctx, size) => {
    const bg = ctx.createLinearGradient(0, 0, size, size);
    bg.addColorStop(0, '#2a1a10');
    bg.addColorStop(0.5, '#6b4425');
    bg.addColorStop(1, '#23150d');
    ctx.fillStyle = bg;
    ctx.fillRect(0, 0, size, size);
    const plank = 128;
    for (let y = -plank; y < size + plank; y += plank) {
      for (let x = -plank; x < size + plank; x += plank) {
        ctx.save();
        ctx.translate(x + plank / 2, y + plank / 2);
        ctx.rotate(((x + y) / plank) % 2 ? Math.PI / 4 : -Math.PI / 4);
        const g = ctx.createLinearGradient(-plank / 2, 0, plank / 2, 0);
        g.addColorStop(0, '#2d1b0f');
        g.addColorStop(0.45, '#8b5d34');
        g.addColorStop(1, '#3a2313');
        ctx.fillStyle = g;
        ctx.fillRect(-plank / 2, -plank / 5, plank, plank / 2.4);
        ctx.strokeStyle = 'rgba(246,196,118,.20)';
        ctx.lineWidth = 3;
        ctx.strokeRect(-plank / 2, -plank / 5, plank, plank / 2.4);
        for (let i = 0; i < 11; i += 1) {
          ctx.strokeStyle = `rgba(255,221,165,${0.035 + i * 0.004})`;
          ctx.beginPath();
          ctx.moveTo(-plank / 2 + i * 13, -plank / 5);
          ctx.bezierCurveTo(-30 + i * 12, -12, 12 + i * 6, 16, plank / 2, plank / 5 - i);
          ctx.stroke();
        }
        ctx.restore();
      }
    }
    const shine = ctx.createRadialGradient(size * 0.55, size * 0.42, 10, size * 0.55, size * 0.42, size * 0.5);
    shine.addColorStop(0, 'rgba(255,231,174,.34)');
    shine.addColorStop(0.45, 'rgba(255,231,174,.08)');
    shine.addColorStop(1, 'rgba(255,231,174,0)');
    ctx.fillStyle = shine;
    ctx.fillRect(0, 0, size, size);
  }, 5, 22);
}

function createWallTexture() {
  return makeTexture(1024, (ctx, size) => {
    const bg = ctx.createLinearGradient(0, 0, size, size);
    bg.addColorStop(0, '#162636');
    bg.addColorStop(0.55, '#0f1b27');
    bg.addColorStop(1, '#091019');
    ctx.fillStyle = bg;
    ctx.fillRect(0, 0, size, size);
    for (let x = 80; x < size; x += 220) {
      ctx.fillStyle = 'rgba(255,226,172,.045)';
      ctx.fillRect(x, 0, 4, size);
      ctx.fillStyle = 'rgba(0,0,0,.18)';
      ctx.fillRect(x + 6, 0, 8, size);
    }
    for (let y = 130; y < size; y += 230) {
      ctx.fillStyle = 'rgba(255,226,172,.035)';
      ctx.fillRect(0, y, size, 4);
      ctx.fillStyle = 'rgba(0,0,0,.16)';
      ctx.fillRect(0, y + 6, size, 7);
    }
    for (let i = 0; i < 6500; i += 1) {
      const alpha = Math.random() * 0.035;
      ctx.fillStyle = `rgba(255,255,255,${alpha})`;
      ctx.fillRect(Math.random() * size, Math.random() * size, 1, 1);
    }
  }, 1, 8);
}

function createCeilingTexture() {
  return makeTexture(1024, (ctx, size) => {
    ctx.fillStyle = '#0c0d11';
    ctx.fillRect(0, 0, size, size);
    for (let x = 0; x < size; x += 240) {
      for (let y = 0; y < size; y += 240) {
        const g = ctx.createRadialGradient(x + 120, y + 120, 8, x + 120, y + 120, 130);
        g.addColorStop(0, 'rgba(255,218,150,.10)');
        g.addColorStop(1, 'rgba(0,0,0,.10)');
        ctx.fillStyle = g;
        ctx.fillRect(x, y, 240, 240);
        ctx.strokeStyle = 'rgba(216,170,93,.18)';
        ctx.lineWidth = 8;
        ctx.strokeRect(x + 20, y + 20, 200, 200);
        ctx.strokeStyle = 'rgba(0,0,0,.42)';
        ctx.lineWidth = 10;
        ctx.strokeRect(x + 36, y + 36, 168, 168);
      }
    }
  }, 2, 10);
}

function createSheenTexture() {
  return makeTexture(512, (ctx, size) => {
    ctx.clearRect(0, 0, size, size);
    const g = ctx.createLinearGradient(0, 0, size, size);
    g.addColorStop(0, 'rgba(255,255,255,0)');
    g.addColorStop(0.46, 'rgba(255,255,255,.20)');
    g.addColorStop(0.52, 'rgba(255,226,172,.12)');
    g.addColorStop(1, 'rgba(255,255,255,0)');
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, size, size);
  }, 1, 1);
}

function loadSceneTexture(path, repeatX = 1, repeatY = 1) {
  const texture = loader.load(assetUrl(path));
  texture.colorSpace = THREE.SRGBColorSpace;
  texture.wrapS = THREE.RepeatWrapping;
  texture.wrapT = THREE.RepeatWrapping;
  texture.repeat.set(repeatX, repeatY);
  texture.anisotropy = Math.min(renderer.capabilities.getMaxAnisotropy?.() || 8, 8);
  return texture;
}

function makeBox(w, h, d, material, x, y, z) {
  const mesh = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), material);
  mesh.position.set(x, y, z);
  scene.add(mesh);
  return mesh;
}

const parquetTexture = loadSceneTexture('assets/scene/gallery-floor-parquet.webp', 1.8, 11);
const wallTexture = createWallTexture();
const panelTexture = loadSceneTexture('assets/scene/gallery-wall-panel-texture.webp', 1, 1);
const ceilingTexture = loadSceneTexture('assets/scene/gallery-ceiling-coffered.webp', 1.6, 8);
const sheenTexture = createSheenTexture();
const wallMat = new THREE.MeshStandardMaterial({ color: 0x122232, map: wallTexture, bumpMap: wallTexture, bumpScale: 0.018, roughness: 0.76, metalness: 0.04 });
const panelMat = new THREE.MeshStandardMaterial({ color: 0xffffff, map: panelTexture, bumpMap: panelTexture, bumpScale: 0.018, roughness: 0.68, metalness: 0.06 });
const floorMat = new THREE.MeshStandardMaterial({ color: 0xffffff, map: parquetTexture, bumpMap: parquetTexture, bumpScale: 0.055, roughness: 0.38, metalness: 0.18 });
const ceilingMat = new THREE.MeshStandardMaterial({ color: 0xffffff, map: ceilingTexture, bumpMap: ceilingTexture, bumpScale: 0.025, roughness: 0.64, metalness: 0.08 });
const floor = new THREE.Mesh(new THREE.PlaneGeometry(19, 82, 32, 160), floorMat);
floor.rotation.x = -Math.PI / 2;
floor.position.set(0, -2.24, -34);
floor.receiveShadow = true;
scene.add(floor);
makeBox(19, 0.16, 82, mat(0x160e08, 0.7, 0.08), 0, -2.42, -34);
makeBox(19, 0.2, 82, ceilingMat, 0, 5.2, -34);
makeBox(0.25, 7.5, 82, wallMat, -9.5, 1.35, -34);
makeBox(0.25, 7.5, 82, wallMat, 9.5, 1.35, -34);
makeBox(19, 7.5, 0.25, mat(0x111018, 0.75, 0.08), 0, 1.35, -74);

function makeSideWallPanel(side, z) {
  const isLeft = side === 'left';
  const x = isLeft ? -9.31 : 9.31;
  const normalOffset = isLeft ? 0.05 : -0.05;
  const panel = new THREE.Mesh(new THREE.PlaneGeometry(5.15, 5.15), panelMat);
  panel.position.set(x + normalOffset, 1.1, z);
  panel.rotation.y = isLeft ? Math.PI / 2 : -Math.PI / 2;
  scene.add(panel);
  const trim = mat(0xb48138, 0.38, 0.55);
  makeBox(0.055, 5.45, 0.08, trim, x + normalOffset * 1.8, 1.1, z - 2.72);
  makeBox(0.055, 5.45, 0.08, trim, x + normalOffset * 1.8, 1.1, z + 2.72);
  makeBox(0.055, 0.08, 5.45, trim, x + normalOffset * 1.8, 3.82, z);
  makeBox(0.055, 0.08, 5.45, trim, x + normalOffset * 1.8, -1.62, z);
  const lights = [];
  [-1.45, 0, 1.45].forEach((offset) => {
    const lampGlow = new THREE.PointLight(0xffd89a, 0.62, 8.5);
    lampGlow.position.set(x + (isLeft ? 0.72 : -0.72), 3.32, z + offset);
    scene.add(lampGlow);
    lights.push(lampGlow);
    const lamp = new THREE.Mesh(new THREE.CylinderGeometry(0.08, 0.13, 0.16, 18), mat(0xd8aa5d, 0.34, 0.62));
    lamp.rotation.z = Math.PI / 2;
    lamp.position.set(x + (isLeft ? 0.16 : -0.16), 3.38, z + offset);
    scene.add(lamp);
  });
  panelLights.push({ z, lights });
}

artworks.forEach((art) => {
  if (art.scene.x < -1) makeSideWallPanel('left', art.scene.z);
  if (art.scene.x > 1) makeSideWallPanel('right', art.scene.z);
});

for (let z = -8; z > -72; z -= 8) {
  const light = new THREE.PointLight(0xffcf86, 1.85, 25);
  light.position.set(0, 4.3, z);
  scene.add(light);
  makeBox(17.4, 0.08, 0.16, mat(0x5a3e24, 0.45, 0.44), 0, 5.05, z);
  makeBox(0.08, 5.2, 0.12, mat(0x6f4c2a, 0.48, 0.36), -9.28, 1.35, z + 2.4);
  makeBox(0.08, 5.2, 0.12, mat(0x6f4c2a, 0.48, 0.36), 9.28, 1.35, z + 2.4);
  const spot = new THREE.Mesh(new THREE.CylinderGeometry(0.13, 0.2, 0.09, 24), mat(0xf4c878, 0.32, 0.6));
  spot.position.set(0, 5.0, z + 1.8);
  spot.rotation.x = Math.PI / 2;
  scene.add(spot);
}

const doorGroup = new THREE.Group();
const doorMat = mat(0x1b1513, 0.48, 0.24);
const leftDoor = makeBox(4.8, 6.2, 0.28, doorMat, -2.4, 1, 2.2);
const rightDoor = makeBox(4.8, 6.2, 0.28, doorMat, 2.4, 1, 2.2);
doorGroup.add(leftDoor, rightDoor);
scene.add(doorGroup);

function makeBench(x, z) {
  const bench = new THREE.Group();
  const seatMat = new THREE.MeshStandardMaterial({ color: 0x061225, roughness: 0.42, metalness: 0.16 });
  const seat = new THREE.Mesh(new THREE.BoxGeometry(3.2, 0.34, 0.86, 8, 2, 4), seatMat);
  seat.position.set(0, 0, 0);
  seat.castShadow = true;
  bench.add(seat);
  const trimMat = mat(0xb48138, 0.36, 0.58);
  const frontTrim = new THREE.Mesh(new THREE.BoxGeometry(3.28, 0.08, 0.05), trimMat);
  frontTrim.position.set(0, -0.03, 0.46);
  bench.add(frontTrim);
  const backTrim = frontTrim.clone();
  backTrim.position.z = -0.46;
  bench.add(backTrim);
  for (let ix = -1; ix <= 1; ix += 1) {
    for (let iz = -1; iz <= 1; iz += 2) {
      const tuft = new THREE.Mesh(new THREE.SphereGeometry(0.16, 18, 8), mat(0x020814, 0.52, 0.08));
      tuft.scale.set(1.15, 0.13, 0.72);
      tuft.position.set(ix * 0.82, 0.20, iz * 0.22);
      bench.add(tuft);
    }
  }
  [-0.42, 0.42].forEach((lineZ) => {
    const seam = new THREE.Mesh(new THREE.BoxGeometry(3.0, 0.025, 0.025), mat(0x1d2f4b, 0.48, 0.08));
    seam.position.set(0, 0.19, lineZ);
    bench.add(seam);
  });
  const legMat = mat(0x8b642e, 0.42, 0.5);
  [[-1.25, -0.25], [1.25, -0.25], [-1.25, 0.25], [1.25, 0.25]].forEach(([lx, lz]) => {
    const leg = new THREE.Mesh(new THREE.CylinderGeometry(0.055, 0.085, 0.62, 18), legMat);
    leg.position.set(lx, -0.48, lz);
    bench.add(leg);
    const foot = new THREE.Mesh(new THREE.SphereGeometry(0.105, 18, 10), legMat);
    foot.scale.set(0.9, 0.42, 0.9);
    foot.position.set(lx, -0.82, lz);
    bench.add(foot);
  });
  bench.position.set(x, -1.37, z);
  scene.add(bench);
  return bench;
}
makeBench(-4.7, -7.2);
makeBench(4.7, -7.2);

function textTexture(title, subtitle) {
  const c = document.createElement('canvas');
  c.width = 2200; c.height = 820;
  const ctx = c.getContext('2d');
  const bg = ctx.createLinearGradient(0, 0, c.width, c.height);
  bg.addColorStop(0, '#101722');
  bg.addColorStop(0.55, '#07101a');
  bg.addColorStop(1, '#171018');
  ctx.fillStyle = bg;
  ctx.fillRect(0, 0, c.width, c.height);
  ctx.strokeStyle = '#d8aa5d';
  ctx.lineWidth = 10;
  ctx.strokeRect(28, 28, c.width - 56, c.height - 56);
  ctx.strokeStyle = 'rgba(255,235,180,.32)';
  ctx.lineWidth = 3;
  ctx.strokeRect(52, 52, c.width - 104, c.height - 104);
  ctx.fillStyle = '#f4d38a';
  ctx.font = '800 94px Georgia';
  ctx.textAlign = 'center';
  ctx.textBaseline = 'alphabetic';
  wrap(ctx, title, c.width / 2, 220, 1680, 104);
  ctx.fillStyle = '#f0eaf0';
  ctx.font = '600 50px Segoe UI';
  wrap(ctx, subtitle, c.width / 2, 500, 1760, 68);
  const texture = new THREE.CanvasTexture(c);
  texture.colorSpace = THREE.SRGBColorSpace;
  texture.generateMipmaps = false;
  texture.minFilter = THREE.LinearFilter;
  texture.magFilter = THREE.LinearFilter;
  texture.anisotropy = Math.min(renderer.capabilities.getMaxAnisotropy?.() || 8, 16);
  return texture;
}

function wrap(ctx, text, x, y, maxWidth, lineHeight) {
  const words = String(text).split(' ');
  let line = '';
  for (const word of words) {
    const test = line ? line + ' ' + word : word;
    if (ctx.measureText(test).width > maxWidth && line) {
      ctx.fillText(line, x, y);
      line = word; y += lineHeight;
    } else line = test;
  }
  ctx.fillText(line, x, y);
}

function addArtwork(art, index) {
  const group = new THREE.Group();
  const t = loader.load(assetUrl(art.image));
  t.colorSpace = THREE.SRGBColorSpace;
  t.anisotropy = Math.min(renderer.capabilities.getMaxAnisotropy?.() || 8, 8);
  const imageMat = new THREE.MeshStandardMaterial({
    map: t,
    bumpMap: t,
    displacementMap: t,
    emissive: 0xffffff,
    emissiveMap: t,
    emissiveIntensity: 0.16,
    bumpScale: 0.065,
    displacementScale: art.shape === 'round' ? 0.035 : 0.026,
    roughness: 0.46,
    metalness: 0.03,
  });
  const w = art.scene.width;
  const h = art.scene.height;
  const plane = new THREE.Mesh(new THREE.PlaneGeometry(w, h, 72, 72), imageMat);
  plane.position.z = 0.04;
  plane.castShadow = true;
  plane.userData.art = art;
  group.add(plane);
  clickable.push(plane);
  const sheen = new THREE.Mesh(
    new THREE.PlaneGeometry(w, h),
    new THREE.MeshBasicMaterial({ map: sheenTexture, transparent: true, opacity: 0.18, blending: THREE.AdditiveBlending, depthWrite: false }),
  );
  sheen.position.z = 0.072;
  group.add(sheen);

  const frameMat = mat(0x18100c, 0.42, 0.55);
  const frameThickness = 0.12;
  const frameDepth = 0.16;
  const topFrame = new THREE.Mesh(new THREE.BoxGeometry(w + frameThickness * 2, frameThickness, frameDepth), frameMat);
  const bottomFrame = topFrame.clone();
  const leftFrame = new THREE.Mesh(new THREE.BoxGeometry(frameThickness, h + frameThickness * 2, frameDepth), frameMat);
  const rightFrame = leftFrame.clone();
  topFrame.position.set(0, h / 2 + frameThickness / 2, -0.04);
  bottomFrame.position.set(0, -h / 2 - frameThickness / 2, -0.04);
  leftFrame.position.set(-w / 2 - frameThickness / 2, 0, -0.04);
  rightFrame.position.set(w / 2 + frameThickness / 2, 0, -0.04);
  group.add(topFrame, bottomFrame, leftFrame, rightFrame);
  frames.push(group);

  const plaqueTexture = textTexture(art.title, art.intent);
  const plaqueWidth = Math.min(4.35, w + 1.16);
  const isMainPedestal = art.placement === 'pedestal';
  const isCenterWork = art.placement === 'center';
  const plaqueHeight = isMainPedestal ? 0.84 : 0.92;
  const plaqueY = isMainPedestal ? -h / 2 - 0.16 : (isCenterWork ? -h / 2 - 0.58 : -h / 2 - 0.46);
  const plaqueZ = isMainPedestal ? w * 0.58 + 0.28 : (isCenterWork ? 0.26 : 0.16);
  const plaqueBack = new THREE.Mesh(new THREE.BoxGeometry(plaqueWidth + 0.16, plaqueHeight + 0.18, 0.12), mat(0x0f1118, 0.45, 0.38));
  plaqueBack.position.set(0, plaqueY, plaqueZ - 0.05);
  group.add(plaqueBack);
  const plaque = new THREE.Mesh(new THREE.PlaneGeometry(plaqueWidth, plaqueHeight), new THREE.MeshBasicMaterial({ map: plaqueTexture, toneMapped: false }));
  plaque.position.set(0, plaqueY, plaqueZ + 0.03);
  group.add(plaque);

  if (isMainPedestal) {
    const pedestalMat = mat(0x1a1210, 0.36, 0.42);
    const pedestal = new THREE.Mesh(new THREE.CylinderGeometry(w * 0.48, w * 0.56, 0.68, 72), pedestalMat);
    pedestal.scale.z = 0.46;
    pedestal.position.set(0, -h / 2 - 0.82, -0.18);
    pedestal.castShadow = true;
    group.add(pedestal);
    [-0.54, -1.04].forEach((rimY) => {
      const rim = new THREE.Mesh(new THREE.TorusGeometry(w * 0.50, 0.028, 10, 72), mat(0xd8aa5d, 0.32, 0.68));
      rim.rotation.x = Math.PI / 2;
      rim.scale.z = 0.46;
      rim.position.set(0, -h / 2 + rimY, -0.18);
      group.add(rim);
    });
  }

  group.position.set(art.scene.x, art.scene.y, art.scene.z);
  group.rotation.y = THREE.MathUtils.degToRad(art.scene.ry);
  group.userData.baseY = group.position.y;
  group.userData.index = index;
  const focusLight = new THREE.PointLight(0xffddb0, 0.38, 9.5);
  focusLight.position.set(0, h / 2 + 0.78, 1.15);
  group.add(focusLight);
  artworkLights.push({ group, light: focusLight });
  scene.add(group);
}

artworks.forEach(addArtwork);

const raycaster = new THREE.Raycaster();
const pointer = new THREE.Vector2();
canvas.addEventListener('click', event => {
  const rect = canvas.getBoundingClientRect();
  pointer.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
  pointer.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;
  raycaster.setFromCamera(pointer, camera);
  const hit = raycaster.intersectObjects(clickable, false)[0];
  if (hit?.object?.userData?.art) openArt(hit.object.userData.art);
});

document.querySelector('[data-preview-art]')?.addEventListener('click', () => openArt(artworks[0]));
document.querySelectorAll('[data-close-art]').forEach(el => el.addEventListener('click', closeArt));
flipButton?.addEventListener('click', () => {
  flipCard.classList.toggle('is-flipped');
  flipButton.textContent = flipCard.classList.contains('is-flipped') ? 'На лицевую сторону' : 'Перевернуть';
});

function openArt(art) {
  modalImage.src = assetUrl(art.image);
  modalImage.alt = art.title;
  modalTitle.textContent = art.title;
  modalText.textContent = `${art.note} ${art.intent}`;
  modalDetail.href = isTildaMode ? '#catalog' : art.detailUrl;
  document.getElementById('purchaseArtwork').value = art.title;
  flipCard.classList.remove('is-flipped');
  flipButton.textContent = 'Перевернуть';
  modal.setAttribute('aria-hidden', 'false');
}
function closeArt() { modal.setAttribute('aria-hidden', 'true'); }

function resize() {
  const w = window.innerWidth;
  const h = window.innerHeight;
  camera.aspect = w / h;
  camera.updateProjectionMatrix();
  renderer.setSize(w, h, false);
}
window.addEventListener('resize', resize);
resize();

function scrollProgress() {
  const max = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
  return Math.min(1, Math.max(0, window.scrollY / max));
}

let target = 0;
let current = 0;
const heroSection = document.querySelector('.hero-section');
const sideSections = [...document.querySelectorAll('.story-section.side-copy')];

function smooth(t) {
  const v = Math.max(0, Math.min(1, t));
  return v * v * (3 - 2 * v);
}

function viewForArt(art) {
  const isLeft = art.scene.x < -1;
  const isRight = art.scene.x > 1;
  const isCenter = !isLeft && !isRight;
  const cameraX = isLeft ? art.scene.x + 3.85 : isRight ? art.scene.x - 3.85 : 0;
  const cameraZ = art.scene.z + (isCenter ? 6.7 : 4.25);
  const cameraY = isCenter ? 0.74 : 0.92;
  return {
    p: 0,
    pos: new THREE.Vector3(cameraX, cameraY, cameraZ),
    look: new THREE.Vector3(art.scene.x, art.scene.y - 0.86, art.scene.z),
  };
}

const cameraStops = [
  { p: 0.00, pos: new THREE.Vector3(0, 1.15, 5.6), look: new THREE.Vector3(0, 1.0, -8) },
  { p: 0.08, pos: new THREE.Vector3(0, 1.1, 1.6), look: new THREE.Vector3(0, 0.7, -8) },
  ...artworks.map((art, index) => {
    const stop = viewForArt(art);
    stop.p = 0.15 + index * 0.068;
    return stop;
  }),
  { p: 0.88, pos: new THREE.Vector3(0, 1.2, -63), look: new THREE.Vector3(0, 0.4, -72) },
  { p: 1.00, pos: new THREE.Vector3(0, 1.45, -70), look: new THREE.Vector3(0, 0.5, -74) },
];

function cameraSample(progress) {
  for (let i = 0; i < cameraStops.length - 1; i += 1) {
    const a = cameraStops[i];
    const b = cameraStops[i + 1];
    if (progress <= b.p) {
      const t = smooth((progress - a.p) / Math.max(0.001, b.p - a.p));
      return {
        pos: a.pos.clone().lerp(b.pos, t),
        look: a.look.clone().lerp(b.look, t),
      };
    }
  }
  return cameraStops[cameraStops.length - 1];
}

function updateStoryPanels(progress) {
  if (heroSection) {
    const heroOpacity = 1 - smooth((progress - 0.025) / 0.055);
    heroSection.style.opacity = Math.max(0, Math.min(1, heroOpacity)).toFixed(3);
    heroSection.style.pointerEvents = heroOpacity > 0.35 ? 'auto' : 'none';
  }
  const panelWindows = [
    [0.115, 0.185],
    [0.245, 0.315],
    [0.500, 0.570],
    [0.785, 0.855],
  ];
  sideSections.forEach((section, index) => {
    const [start, end] = panelWindows[index] || [1, 1];
    const fadeIn = smooth((progress - start) / 0.02);
    const fadeOut = 1 - smooth((progress - (end - 0.02)) / 0.02);
    const opacity = Math.max(0, Math.min(1, fadeIn, fadeOut));
    section.style.opacity = opacity.toFixed(3);
    section.style.pointerEvents = opacity > 0.45 ? 'auto' : 'none';
  });
}

function animate() {
  requestAnimationFrame(animate);
  target = scrollProgress();
  current += (target - current) * 0.12;
  if (meter) meter.style.width = `${current * 100}%`;
  document.documentElement.style.setProperty('--entry-open', String(Math.min(1, target / 0.075).toFixed(3)));
  updateStoryPanels(current);
  const sample = cameraSample(current);
  sample.pos.y += Math.sin(current * Math.PI * 18) * 0.034 + Math.sin(performance.now() * 0.0013) * 0.006;
  camera.position.copy(sample.pos);
  camera.lookAt(sample.look);
  const door = Math.min(1, current / 0.11);
  leftDoor.rotation.y = -door * 1.25;
  rightDoor.rotation.y = door * 1.25;
  panelLights.forEach(({ z, lights }) => {
    const focus = Math.max(0, 1 - Math.abs(z - camera.position.z) / 8.5);
    lights.forEach((light) => {
      light.intensity = 0.68 + focus * 2.45;
      light.distance = 7.5 + focus * 3.5;
    });
  });
  frames.forEach((group, index) => {
    const distance = Math.abs(group.position.z - camera.position.z);
    const active = distance < 7;
    group.position.y = group.userData.baseY;
    group.scale.setScalar(active ? 1.012 : 1);
  });
  artworkLights.forEach(({ group, light }) => {
    const focus = Math.max(0, 1 - Math.abs(group.position.z - camera.position.z) / 7.2);
    light.intensity = 0.52 + focus * 2.35;
  });
  renderer.render(scene, camera);
}
animate();
"""


APP_JS = r"""
const drawer = document.getElementById('purchaseDrawer');
const purchaseArtwork = document.getElementById('purchaseArtwork');
const artworksData = JSON.parse(document.getElementById('artworksData')?.textContent || '[]');
const artworksById = new Map(artworksData.map((art) => [art.id, art]));
const artworksByTitle = new Map(artworksData.map((art) => [art.title, art]));
const assetBase = window.MOONN_ART_GALLERY_BASE_URL || '';

function assetUrl(path) {
  if (!path || /^https?:\/\//i.test(path) || path.startsWith('data:')) return path;
  if (!assetBase) return path;
  return `${assetBase.replace(/\/?$/, '/')}${String(path).replace(/^\.?\//, '')}`;
}

function resolveArtwork(value) {
  if (!value) return artworksData[0] || null;
  return artworksById.get(value) || artworksByTitle.get(value) || artworksData.find((art) => art.title === value) || artworksData[0] || null;
}

function openPurchase(artworkOrTitle) {
  const art = typeof artworkOrTitle === 'object' ? artworkOrTitle : resolveArtwork(artworkOrTitle);
  if (art && purchaseArtwork) purchaseArtwork.value = art.title;
  drawer?.setAttribute('aria-hidden', 'false');
}
function closePurchase() { drawer?.setAttribute('aria-hidden', 'true'); }

function initTildaCart() {
  const cartRecord = document.querySelector('[data-record-type="706"][id]');
  if (!cartRecord || typeof window.t_onFuncLoad !== 'function') return;
  window.t_onFuncLoad('tcart__init', () => {
    try {
      window.tcart__init(cartRecord.id.replace(/^rec/, ''), { cssClassName: '' });
    } catch (error) {
      console.warn('Moonn art cart init skipped', error);
    }
  });
}

function repairTildaOrderFormHandlers() {
  const cartRecord = document.querySelector('[data-record-type="706"][id]');
  const form = document.querySelector('.t706__cartwin form.js-form-proccess');
  if (!cartRecord || !form) return;
  try {
    if (window.initForms && cartRecord.id) delete window.initForms[cartRecord.id];
    if (typeof window.t_forms__initFormFields === 'function') window.t_forms__initFormFields(cartRecord);
    if (typeof window.t_forms__addInputItsGood === 'function') window.t_forms__addInputItsGood(cartRecord);
    if (typeof window.t_forms__addAttrAction === 'function') window.t_forms__addAttrAction(cartRecord);
    if (typeof window.t_forms__onSubmit === 'function') window.t_forms__onSubmit(cartRecord);
    if (typeof window.t_forms__onClick === 'function') window.t_forms__onClick(cartRecord);
    if (typeof window.t_forms__onRender === 'function') window.t_forms__onRender(cartRecord);
    if (typeof window.t_forms__addFocusOnTab === 'function') window.t_forms__addFocusOnTab(cartRecord);
  } catch (error) {
    console.warn('Moonn art order form repair skipped', error);
  }
}

function enhanceTildaPaymentUi() {
  const cart = document.querySelector('.t706__cartwin, .t706');
  if (!cart) return;
  repairTildaOrderFormHandlers();
  cart.querySelectorAll('.t-submit, button[type="submit"], .t-btnflex_type_submit').forEach((submit) => {
    const submitText = submit.querySelector('.t-btnflex__text, span') || submit;
    if ((submitText.textContent || '').trim() !== 'Перейти к оплате') submitText.textContent = 'Перейти к оплате';
    submit.setAttribute('aria-label', 'Перейти к оплате через T-Bank');
  });
}

function openArtworkPayment(art) {
  if (!art) return false;
  initTildaCart();
  if (typeof window.tcart__addProduct !== 'function' || typeof window.tcart__openCart !== 'function') return false;
  const image = art.checkoutImage || assetUrl(art.image);
  const product = {
    name: art.checkoutName || `${art.title} — картина Татьяны Мунн`,
    price: Number(art.priceValue || 0),
    amount: Number(art.priceValue || 0),
    quantity: 1,
    img: image,
    sku: art.sku || art.id,
  };
  try {
    if (window.tcart && Array.isArray(window.tcart.products)) window.tcart.products = [];
    window.tcart__addProduct(product);
    if (typeof window.tcart__reDrawCartIcon === 'function') window.tcart__reDrawCartIcon();
    window.tcart__openCart();
    setTimeout(enhanceTildaPaymentUi, 200);
    setTimeout(enhanceTildaPaymentUi, 900);
    return true;
  } catch (error) {
    console.warn('Moonn art payment open skipped', error);
    return false;
  }
}

initTildaCart();
setTimeout(initTildaCart, 300);
setTimeout(initTildaCart, 1200);
setInterval(enhanceTildaPaymentUi, 1500);

document.querySelectorAll('[data-open-purchase]').forEach((button) => {
  button.addEventListener('click', (event) => {
    event.preventDefault();
    const art = resolveArtwork(button.dataset.artId || button.dataset.artTitle || purchaseArtwork?.value);
    if (!openArtworkPayment(art)) openPurchase(art);
  });
});
document.querySelectorAll('[data-close-purchase]').forEach((button) => button.addEventListener('click', closePurchase));

document.querySelector('[data-copy-request]')?.addEventListener('click', () => {
  const form = drawer?.querySelector('form');
  const data = new FormData(form);
  const text = [
    'Здравствуйте. Хочу обсудить покупку картины Татьяны Мунн.',
    `Картина: ${data.get('artwork') || ''}`,
    `Стоимость: ${(resolveArtwork(data.get('artwork')) || {}).price || ''}`,
    `Имя: ${data.get('name') || ''}`,
    `Контакт: ${data.get('contact') || ''}`,
    `Комментарий: ${data.get('message') || ''}`,
  ].join('\n');
  navigator.clipboard?.writeText(text);
  const toast = document.createElement('div');
  toast.className = 'copy-toast';
  toast.textContent = 'Текст заявки скопирован';
  document.body.appendChild(toast);
  setTimeout(() => toast.remove(), 1800);
});

function calculatePersonalCode(seed) {
  let hash = 2166136261;
  for (let i = 0; i < seed.length; i += 1) {
    hash ^= seed.charCodeAt(i);
    hash = Math.imul(hash, 16777619);
  }
  const n = Math.abs(hash >>> 0);
  const a = String(100 + (n % 900));
  const b = String(100 + (Math.floor(n / 997) % 900));
  const c = String(100 + (Math.floor(n / 7919) % 900));
  return `${a} ${b} ${c}`;
}

const codeForm = document.getElementById('codeForm');
function updateCode() {
  if (!codeForm) return;
  const fio = document.getElementById('fio')?.value || '';
  const birth = document.getElementById('birth')?.value || '';
  const time = document.getElementById('birthTime')?.value || '';
  const request = document.getElementById('request')?.value || '';
  const code = calculatePersonalCode(`${fio}|${birth}|${time}|${request}|TatianaMoonn`);
  document.querySelectorAll('.js-code').forEach((node) => { node.textContent = code; });
}
codeForm?.addEventListener('submit', (event) => { event.preventDefault(); updateCode(); });
codeForm?.addEventListener('input', updateCode);
updateCode();
window.MoonnArtGalleryPayment = { artworks: artworksData, openArtworkPayment, openPurchase };

window.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') {
    closePurchase();
    document.getElementById('artModal')?.setAttribute('aria-hidden', 'true');
  }
});
"""


README = """# Tatiana Moonn Art Gallery

Статический многостраничный сайт галереи картин Татьяны Мунн.

## Что внутри

- `index.html` — 3D-scroll прогулка по выставочному залу на Three.js.
- `catalog.html` — каталог картин.
- `artwork-*.html` — отдельные страницы работ.
- `code.html` — форма индивидуального кода.
- `about.html`, `contacts.html` — служебные страницы многостраничника.
- `assets/art/*.webp` — оптимизированные изображения картин с латинскими именами файлов.
- `data/artworks.json` — machine-first манифест картин, цен, описаний и 3D-позиций.

## Запуск

Из этой папки:

```powershell
python -m http.server 8765
```

Открыть:

```text
локальный адрес, который покажет сервер в терминале
```

## Важно

В интерфейсе есть заявка на покупку. Реальная онлайн-оплата включается отдельным безопасным этапом после утверждения цен, остатков, продавца, доставки и условий возврата.
"""

FAVICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" rx="16" fill="#07080d"/>
<circle cx="32" cy="32" r="22" fill="none" stroke="#d8aa5d" stroke-width="3"/>
<path d="M16 38c10-22 22-22 32 0M22 32c4-12 16-12 20 0" fill="none" stroke="#5fd6df" stroke-width="3" stroke-linecap="round"/>
<circle cx="32" cy="32" r="5" fill="#ffe7aa"/>
</svg>
"""


def build_tilda_artifacts(records: list[dict[str, object]]) -> None:
    index_html = (OUT / "index.html").read_text(encoding="utf-8")
    body_match = re.search(r"<body>(?P<body>[\s\S]*?)</body>", index_html)
    if not body_match:
        raise RuntimeError("Generated index.html does not contain a body section")
    body = body_match.group("body")
    body = re.sub(r'<script src="app\.js"></script>\s*', "", body)
    body = re.sub(r'<script type="module" src="gallery-3d\.js"></script>\s*', "", body)
    body = tilda_asset_html(body)
    body = body.replace('id="gallery"', 'id="gallery" data-moonn-art-gallery-tilda="true"', 1)
    page_schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": f"{TILDA_PAGE_URL}#webpage",
                "url": TILDA_PAGE_URL,
                "name": TILDA_PAGE_TITLE,
                "description": TILDA_PAGE_DESCRIPTION,
                "inLanguage": "ru-RU",
                "isPartOf": {"@type": "WebSite", "@id": "https://moonn.ru/#website", "url": "https://moonn.ru/"},
            },
            {
                "@type": "ItemList",
                "@id": f"{TILDA_PAGE_URL}#artworks",
                "name": "Каталог картин Татьяны Мунн",
                "numberOfItems": len(records),
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": index,
                        "item": {
                            "@type": "Product",
                            "name": record["checkoutName"],
                            "image": record["checkoutImage"],
                            "sku": record["sku"],
                            "offers": {
                                "@type": "Offer",
                                "price": record["priceValue"],
                                "priceCurrency": record["priceCurrency"],
                                "availability": "https://schema.org/InStock",
                                "url": TILDA_PAGE_URL,
                            },
                        },
                    }
                    for index, record in enumerate(records, start=1)
                ],
            },
        ],
    }
    block = f"""<section id="moonn-art-gallery-tilda-page" aria-label="Галерея картин Татьяны Мунн">
  <link rel="stylesheet" href="{cdn_url('style.css')}">
  <script>
    window.MOONN_ART_GALLERY_BASE_URL = "{TILDA_CDN_BASE.rstrip('/')}/";
    window.MOONN_ART_GALLERY_TILDA_MODE = true;
  </script>
  {body}
  <script type="module" src="{cdn_url('gallery-3d.js')}"></script>
  <script src="{cdn_url('app.js')}"></script>
  <script type="application/ld+json">{json.dumps(page_schema, ensure_ascii=False)}</script>
</section>
"""
    (OUT / "tilda-html-block-final.html").write_text(block, encoding="utf-8")
    full_page = f"""<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(TILDA_PAGE_TITLE)}</title>
  <meta name="description" content="{escape(TILDA_PAGE_DESCRIPTION)}">
  <meta name="robots" content="index,follow">
  <link rel="canonical" href="{TILDA_PAGE_URL}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{TILDA_PAGE_URL}">
  <meta property="og:title" content="{escape(TILDA_PAGE_TITLE)}">
  <meta property="og:description" content="{escape(TILDA_PAGE_DESCRIPTION)}">
  <meta property="og:image" content="{cdn_url('assets/tatiana_munn_gallery_concept.webp')}">
</head>
<body>
{block}
</body>
</html>
"""
    (OUT / "tilda-page-final.html").write_text(full_page, encoding="utf-8")
    (OUT / "tilda-head-loader-final.html").write_text(
        "\n".join(
            [
                f'<link rel="canonical" href="{TILDA_PAGE_URL}">',
                f'<meta property="og:image" content="{cdn_url("assets/tatiana_munn_gallery_concept.webp")}">',
                f'<script>window.MOONN_ART_GALLERY_BASE_URL="{TILDA_CDN_BASE.rstrip("/")}/";window.MOONN_ART_GALLERY_TILDA_MODE=true;</script>',
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    (OUT / "tilda-head-seo-final.html").write_text(
        "\n".join(
            [
                f"<title>{escape(TILDA_PAGE_TITLE)}</title>",
                f'<meta name="description" content="{escape(TILDA_PAGE_DESCRIPTION)}">',
                '<meta name="robots" content="index,follow">',
                f'<link rel="canonical" href="{TILDA_PAGE_URL}">',
                '<meta property="og:type" content="website">',
                f'<meta property="og:url" content="{TILDA_PAGE_URL}">',
                f'<meta property="og:title" content="{escape(TILDA_PAGE_TITLE)}">',
                f'<meta property="og:description" content="{escape(TILDA_PAGE_DESCRIPTION)}">',
                f'<meta property="og:image" content="{cdn_url("assets/tatiana_munn_gallery_concept.webp")}">',
                f'<script type="application/ld+json">{json.dumps(page_schema, ensure_ascii=False)}</script>',
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    payment_products = {
        "generatedAt": "2026-05-11",
        "project": "Moonn / Tatiana Moonn art gallery",
        "pageUrl": TILDA_PAGE_URL,
        "paymentProvider": "Tilda native cart / T-Bank",
        "products": [
            {
                "sku": record["sku"],
                "name": record["checkoutName"],
                "price": record["priceValue"],
                "currency": record["priceCurrency"],
                "image": record["checkoutImage"],
                "tildaProductHref": record["tildaProductHref"],
            }
            for record in records
        ],
    }
    (DATA_DIR / "tilda-payment-products.json").write_text(json.dumps(payment_products, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    build_homepage_art_gallery_block(records)
    build_publication_report(records)


def build_homepage_art_gallery_block(records: list[dict[str, object]]) -> None:
    lead = records[0]
    block = f"""<section id="moonn-art-gallery-home-banner" class="moonn-art-gallery-home-banner" aria-label="Галерея картин Татьяны Мунн">
  <style>
    #moonn-art-gallery-home-banner{{font-family:Inter,Arial,sans-serif;max-width:1180px;margin:28px auto;padding:30px;border:1px solid rgba(216,170,93,.25);background:linear-gradient(135deg,#090b12,#17111d 58%,#22152a);color:#fff2d8;box-shadow:0 24px 70px rgba(0,0,0,.22);display:grid;grid-template-columns:minmax(0,1fr) minmax(250px,380px);gap:26px;align-items:center;overflow:hidden;position:relative}}
    #moonn-art-gallery-home-banner *{{box-sizing:border-box}}
    #moonn-art-gallery-home-banner h2{{margin:0 0 14px;font-family:Georgia,serif;font-weight:400;font-size:clamp(34px,4.8vw,64px);line-height:1.02;letter-spacing:0;color:#fff2d8}}
    #moonn-art-gallery-home-banner p{{margin:0 0 20px;max-width:680px;color:#d6ccd8;font-size:17px;line-height:1.58}}
    #moonn-art-gallery-home-banner .eyebrow{{display:inline-flex;margin-bottom:12px;color:#ffe7aa;font-size:12px;text-transform:uppercase;letter-spacing:.18em}}
    #moonn-art-gallery-home-banner .actions{{display:flex;flex-wrap:wrap;gap:12px;align-items:center}}
    #moonn-art-gallery-home-banner a.button{{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:0 20px;border-radius:999px;background:linear-gradient(135deg,#a06b27,#f3cf82 52%,#8a5f25);color:#171014!important;text-decoration:none!important;font-weight:800;box-shadow:0 14px 34px rgba(216,170,93,.22)}}
    #moonn-art-gallery-home-banner .note{{color:#bfb5c5;font-size:14px}}
    #moonn-art-gallery-home-banner .media{{position:relative;display:grid;grid-template-columns:1fr 1fr;gap:12px;align-items:center}}
    #moonn-art-gallery-home-banner .media img{{width:100%;aspect-ratio:1;object-fit:cover;border-radius:16px;border:1px solid rgba(255,226,172,.2);box-shadow:0 18px 44px rgba(0,0,0,.34)}}
    #moonn-art-gallery-home-banner .media img:first-child{{transform:translateY(18px)}}
    @media(max-width:820px){{#moonn-art-gallery-home-banner{{grid-template-columns:1fr;margin:22px 10px;padding:22px}}#moonn-art-gallery-home-banner .media{{order:-1}}#moonn-art-gallery-home-banner a.button{{width:100%}}}}
  </style>
  <div>
    <span class="eyebrow">3D-галерея · картины · персональный код</span>
    <h2>Картины Татьяны Мунн</h2>
    <p>Премиальная онлайн-галерея: прогулка по залу, каталог работ, персональный код владельца и заявка на покупку картины.</p>
    <div class="actions">
      <a class="button" href="/{TILDA_PAGE_ALIAS}">Открыть галерею</a>
      <span class="note">10 авторских работ · от {escape(str(min(record["priceValue"] for record in records)))} ₽</span>
    </div>
  </div>
  <a class="media" href="/{TILDA_PAGE_ALIAS}" aria-label="Открыть галерею картин Татьяны Мунн">
    <img src="{lead['checkoutImage']}" alt="{escape(str(lead['title']))} — картина Татьяны Мунн">
    <img src="{cdn_url('assets/tatiana_munn_gallery_concept.webp')}" alt="3D-галерея картин Татьяны Мунн">
  </a>
</section>
"""
    (OUT / "homepage-art-gallery-block-final.html").write_text(block, encoding="utf-8")


def build_publication_report(records: list[dict[str, object]]) -> None:
    report = f"""# 2026-05-11 Tatiana Moonn Art Gallery Tilda Publication Packet

## Scope

- Project: Moonn / Tatiana Moonn art gallery.
- Branch: `codex/moonn-art-gallery`.
- Intended URL: `{TILDA_PAGE_URL}`.
- Homepage page id: `{TILDA_HOMEPAGE_ID}`.
- Tilda project id: `{TILDA_PROJECT_ID}`.

## Generated Artifacts

- `tilda-html-block-final.html` - native Tilda T123 block for the gallery page.
- `tilda-page-final.html` - standalone preview page using the same Tilda-safe block.
- `tilda-head-loader-final.html` - minimal head/base snippet.
- `tilda-head-seo-final.html` - SEO and schema layer.
- `homepage-art-gallery-block-final.html` - homepage banner linking to `/{TILDA_PAGE_ALIAS}`.
- `data/tilda-payment-products.json` - native Tilda cart product manifest.

## Payment Products

- Products: `{len(records)}` artworks.
- Price range: `{min(record["priceValue"] for record in records)}`-`{max(record["priceValue"] for record in records)}` RUB.
- Payment route: native Tilda cart / T-Bank through `tcart__addProduct`, `tcart__reDrawCartIcon`, `tcart__openCart`.

## Publication Gate

- Do not submit a real payment.
- Create or update the Tilda page with alias `{TILDA_PAGE_ALIAS}`.
- Add a native Tilda cart/payment block (`T706`/`ST100`) on the gallery page before payment QA.
- Publish the gallery page.
- Add `homepage-art-gallery-block-final.html` to the homepage near the existing consultation/camp promo banners.
- Verify live HTML contains `moonn-art-gallery-tilda-page` and `moonn-art-gallery-home-banner`.
- Verify at least one artwork CTA opens the native cart with the correct artwork name and amount.
- Verify T-Bank provider screen is reachable without entering card data.
"""
    (OUT / "publication-report-2026-05-11.md").write_text(report, encoding="utf-8")


def write_static_files(records: list[dict[str, object]]) -> None:
    (OUT / "style.css").write_text(STYLE_CSS, encoding="utf-8")
    (OUT / "gallery-3d.js").write_text(GALLERY_JS, encoding="utf-8")
    (OUT / "app.js").write_text(APP_JS, encoding="utf-8")
    (OUT / "README.md").write_text(README, encoding="utf-8")
    (OUT / "favicon.svg").write_text(FAVICON_SVG, encoding="utf-8")
    (DATA_DIR / "artworks.json").write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    stale_payment_manifest = DATA_DIR / "purchase-manifest.json"
    if stale_payment_manifest.exists():
        stale_payment_manifest.unlink()


def build_zip() -> None:
    if ZIP_OUT.exists():
        ZIP_OUT.unlink()
    with zipfile.ZipFile(ZIP_OUT, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in OUT.rglob("*"):
            if path.is_file():
                zf.write(path, path.relative_to(OUT.parent))


def build_report(records: list[dict[str, object]]) -> None:
    html_files = sorted(p.name for p in OUT.glob("*.html"))
    text = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in OUT.glob("*.html"))
    report = {
        "project": "Moonn / Tatiana Moonn art gallery",
        "branch": "codex/moonn-art-gallery",
        "generatedAt": "2026-05-10",
        "outputDir": str(OUT),
        "zip": str(ZIP_OUT),
        "artworks": len(records),
        "htmlFiles": html_files,
        "checks": {
            "usesTatianaMunnDoubleN": "Татьяна Мунн" in text,
            "singleNVisibleHits": text.count("Татьяна " + "Мун</"),
            "hasThreeJs": (OUT / "gallery-3d.js").read_text(encoding="utf-8").count("THREE.") > 10,
            "hasPurchaseRequestLayer": "purchaseDrawer" in (OUT / "app.js").read_text(encoding="utf-8"),
            "hasArtworkJson": (DATA_DIR / "artworks.json").exists(),
            "hasTildaPage": (OUT / "tilda-html-block-final.html").exists(),
            "hasHomepageBanner": (OUT / "homepage-art-gallery-block-final.html").exists(),
            "hasTildaPaymentProducts": (DATA_DIR / "tilda-payment-products.json").exists(),
            "latinAssetNames": all(all(ord(ch) < 128 for ch in p.name) for p in ART_DIR.glob("*")),
        },
    }
    (OUT / "build-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    ensure_dirs()
    build_assets()
    ensure_three_vendor()
    records = artwork_records()
    write_static_files(records)
    build_index(records)
    build_catalog(records)
    build_artwork_pages(records)
    build_code_page()
    build_about_contacts()
    build_tilda_artifacts(records)
    build_report(records)
    build_zip()
    print(json.dumps({"output": str(OUT), "zip": str(ZIP_OUT), "artworks": len(records)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
