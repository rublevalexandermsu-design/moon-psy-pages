from __future__ import annotations

import json
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
VENDOR_DIR = ASSETS / "vendor"
DATA_DIR = OUT / "data"
ZIP_OUT = ROOT / "output" / "tatiana-munn-art-gallery-site.zip"
THREE_URL = "https://unpkg.com/three@0.164.1/build/three.module.min.js"


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
        source="ChatGPT Image 10 мая 2026 г., 15_36_09 (1).png",
        shape="round",
        price="700 000 ₽",
        placement="pedestal",
        x=0,
        y=0.25,
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
        source="ChatGPT Image 10 мая 2026 г., 15_36_11 (5).png",
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
        source="ChatGPT Image 10 мая 2026 г., 15_36_13 (9).png",
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
        source="ChatGPT Image 10 мая 2026 г., 15_36_11 (4).png",
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
        source="ChatGPT Image 10 мая 2026 г., 15_36_10 (3).png",
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
        source="ChatGPT Image 10 мая 2026 г., 15_36_17 (10).png",
        shape="square",
        price="320 000 ₽",
        placement="center",
        x=0,
        y=0.2,
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
        source="ChatGPT Image 10 мая 2026 г., 15_36_12 (8).png",
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
        source="ChatGPT Image 10 мая 2026 г., 15_36_12 (7).png",
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
        source="ChatGPT Image 10 мая 2026 г., 15_36_11 (6).png",
        shape="square",
        price="260 000 ₽",
        placement="center",
        x=0,
        y=0.2,
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
        source="ChatGPT Image 10 мая 2026 г., 15_36_10 (2).png",
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
    for path in (OUT, ART_DIR, VENDOR_DIR, DATA_DIR, ROOT / "output"):
        path.mkdir(parents=True, exist_ok=True)


def enhance_and_save(src: Path, dst: Path, max_size: int, quality: int) -> None:
    with Image.open(src) as img:
        img = ImageOps.exif_transpose(img).convert("RGB")
        img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
        img = ImageEnhance.Contrast(img).enhance(1.04)
        img = ImageEnhance.Sharpness(img).enhance(1.08)
        img.save(dst, "WEBP", quality=quality, method=6)


def build_assets() -> None:
    concept_src = DOWNLOADS / "ChatGPT Image 10 мая 2026 г., 15_28_29.png"
    enhance_and_save(concept_src, ASSETS / "tatiana_munn_gallery_concept.webp", 1800, 84)
    for index, art in enumerate(ARTWORKS, start=1):
        src = DOWNLOADS / art.source
        full = ART_DIR / f"{index:02d}-{art.slug}.webp"
        thumb = ART_DIR / f"{index:02d}-{art.slug}-thumb.webp"
        enhance_and_save(src, full, 1600, 84)
        enhance_and_save(src, thumb, 520, 78)


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
        records.append(
            {
                "id": f"tm-art-{index:02d}",
                "slug": art.slug,
                "title": art.title,
                "subtitle": art.subtitle,
                "shape": art.shape,
                "price": art.price,
                "placement": art.placement,
                "image": f"assets/art/{index:02d}-{art.slug}.webp",
                "thumb": f"assets/art/{index:02d}-{art.slug}-thumb.webp",
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
    body = """
<main class="immersive-page">
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
        <a class="ghost-button" href="catalog.html">Открыть каталог</a>
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
      <a class="gold-button" href="code.html">Составить код</a>
    </div>
  </section>
  <section class="story-section side-copy">
    <div class="glass-text right">
      <span class="eyebrow">Фактура</span>
      <h2>Золото, жемчуг, стразы и свет</h2>
      <p>WebP-ассеты подготовлены из новых изображений: усилена резкость и контраст, сохранены блики и фактура, чтобы работы не выглядели плоско.</p>
    </div>
  </section>
  <section class="story-section final-section">
    <div class="glass-text center">
      <span class="eyebrow">Частная покупка</span>
      <h2>Выберите работу для себя или в подарок</h2>
      <p>Финальный путь клиента: просмотр в 3D-зале, открытие карточки, подбор кода, заявка на покупку и подтверждение заказа.</p>
      <div class="hero-actions">
        <a class="gold-button" href="catalog.html">Перейти в каталог</a>
        <button class="ghost-button" data-open-purchase>Оставить заявку</button>
      </div>
    </div>
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
            "Премиальная 3D-галерея картин Татьяны Мунн: прогулка по залу, каталог работ, индивидуальный код, заявка на покупку.",
            body,
            "Галерея",
            canonical_path="art-gallery",
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
:root{--entry-open:0}.entry-doors{position:fixed;inset:78px 0 0;z-index:3;overflow:hidden;pointer-events:none;perspective:1200px;opacity:calc(1 - var(--entry-open));background:radial-gradient(circle at 50% 42%,rgba(255,216,144,.16),transparent 32%)}.entry-doors__hall{position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.52),rgba(4,7,12,.06),rgba(0,0,0,.52));opacity:.75}.entry-door{position:absolute;top:0;bottom:0;width:35vw;max-width:500px;background:radial-gradient(circle at 50% 42%,rgba(216,170,93,.26),transparent 18%),linear-gradient(90deg,#0a0a0b,#211815 18%,#08090d 70%,#2a1d14);border:1px solid rgba(216,170,93,.42);box-shadow:inset 0 0 0 8px rgba(216,170,93,.08),inset 0 0 0 18px rgba(0,0,0,.24),0 0 60px rgba(0,0,0,.78);transition:transform .12s linear}.entry-door span{position:absolute;inset:12% 12%;border:2px solid rgba(216,170,93,.42);border-radius:50%;background:repeating-radial-gradient(circle at 50% 50%,rgba(216,170,93,.35) 0 2px,transparent 2px 18px),conic-gradient(from 0deg,transparent,rgba(216,170,93,.32),transparent 18%,rgba(216,170,93,.26),transparent 42%)}.entry-door--left{left:0;transform-origin:left center;transform:translateX(calc(var(--entry-open)*-90%)) rotateY(calc(var(--entry-open)*-28deg))}.entry-door--right{right:0;transform-origin:right center;transform:translateX(calc(var(--entry-open)*90%)) rotateY(calc(var(--entry-open)*28deg))}.hero-section{transition:opacity .18s ease}.side-copy{transition:opacity .18s ease}.side-copy .glass-text{max-width:520px}.gallery-features{position:relative;z-index:12;padding:72px clamp(18px,6vw,88px) 88px;border-top:1px solid var(--line);background:linear-gradient(180deg,rgba(11,15,22,.92),rgba(7,8,13,.98));text-align:center}.gallery-features>.eyebrow{justify-content:center}.feature-grid{display:grid;grid-template-columns:repeat(6,1fr);gap:0;max-width:1280px;margin:30px auto 0;border-top:1px solid rgba(255,226,172,.16);border-bottom:1px solid rgba(255,226,172,.16)}.feature-grid article{min-height:150px;padding:24px 18px;border-right:1px solid rgba(255,226,172,.12)}.feature-grid article:last-child{border-right:0}.feature-grid b{display:block;margin-bottom:12px;color:var(--gold2);font-family:Georgia,serif;font-size:18px;font-weight:400;text-transform:uppercase}.feature-grid span{color:#c8c0cc;font-size:14px;line-height:1.55}.code-page{background:radial-gradient(circle at 18% 15%,rgba(65,46,100,.38),transparent 36%),linear-gradient(135deg,#0b0f18,#071019 60%,#0c1018)}.code-page h1{font-size:clamp(46px,6vw,92px)}.code-layout{grid-template-columns:1.08fr .92fr;max-width:1180px;align-items:stretch}.code-intro{display:grid;align-content:center;gap:24px;padding:28px}.code-steps{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}.code-steps span{display:grid;place-items:center;width:68px;height:68px;margin:0 auto 12px;border:1px solid rgba(216,170,93,.55);border-radius:50%;color:var(--gold2);font-family:Georgia,serif;font-size:26px}.code-steps b{display:block;text-align:center;color:#efe6d8;font-size:14px}.code-note{color:var(--gold2);font-family:Georgia,serif;font-size:18px}.code-layout .premium-form{border-color:rgba(216,170,93,.45);box-shadow:0 30px 80px rgba(0,0,0,.32)}.code-result-card{position:relative;overflow:hidden}.code-result-card:after{content:"";position:absolute;right:-50px;bottom:-40px;width:220px;height:220px;background:radial-gradient(circle,rgba(216,170,93,.16),transparent 65%)}@media (max-width:1100px){.feature-grid{grid-template-columns:repeat(3,1fr)}.feature-grid article:nth-child(3n){border-right:0}}@media (max-width:900px){.entry-doors{inset:68px 0 0}.entry-door{width:42vw}.gallery-features{padding-inline:18px}.feature-grid{grid-template-columns:1fr 1fr}.code-layout,.code-steps{grid-template-columns:1fr}.code-intro{padding:0}.hero-section{padding-top:12vh}.hero-section h1{font-size:clamp(36px,10.6vw,46px);line-height:1.05}.hero-copy p{font-size:14px;line-height:1.55}.hero-actions{gap:10px}.hero-actions .gold-button,.hero-actions .ghost-button{min-height:46px;padding-inline:14px}.side-copy .glass-text{max-width:100%}}@media (max-width:560px){.feature-grid{grid-template-columns:1fr}.feature-grid article{border-right:0;border-bottom:1px solid rgba(255,226,172,.12)}}
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

const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: false, powerPreference: 'high-performance' });
renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.5));
renderer.outputColorSpace = THREE.SRGBColorSpace;

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x0a0d13);
scene.fog = new THREE.FogExp2(0x080c14, 0.006);

const camera = new THREE.PerspectiveCamera(54, 1, 0.1, 120);
camera.position.set(0, 1.2, 5.5);

scene.add(new THREE.HemisphereLight(0xd7f6ff, 0x24130d, 1.0));
const warm = new THREE.PointLight(0xffc56f, 2.25, 48);
warm.position.set(0, 5, -18);
scene.add(warm);
const cool = new THREE.PointLight(0x5fd6df, 1.45, 40);
cool.position.set(-4, 3, -38);
scene.add(cool);

const loader = new THREE.TextureLoader();
const clickable = [];
const frames = [];

function mat(color, roughness = 0.8, metalness = 0.05) {
  return new THREE.MeshStandardMaterial({ color, roughness, metalness });
}

function makeBox(w, h, d, material, x, y, z) {
  const mesh = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), material);
  mesh.position.set(x, y, z);
  scene.add(mesh);
  return mesh;
}

const wallMat = mat(0x303945, 0.62, 0.08);
const floorMat = mat(0x4a2f1d, 0.42, 0.28);
makeBox(19, 0.2, 82, floorMat, 0, -2.35, -34);
for (let z = 1; z > -73; z -= 4) {
  makeBox(0.035, 0.03, 82, mat(0x7b5330, 0.55, 0.24), -7.2 + ((z + 73) % 16), -2.22, -34);
}
makeBox(19, 0.2, 82, mat(0x10131b, 0.85, 0.03), 0, 5.2, -34);
makeBox(0.25, 7.5, 82, wallMat, -9.5, 1.35, -34);
makeBox(0.25, 7.5, 82, wallMat, 9.5, 1.35, -34);
makeBox(19, 7.5, 0.25, mat(0x111018, 0.75, 0.08), 0, 1.35, -74);

for (let z = -8; z > -72; z -= 8) {
  const light = new THREE.PointLight(0xffcf86, 1.0, 18);
  light.position.set(0, 4.3, z);
  scene.add(light);
  makeBox(17.4, 0.08, 0.16, mat(0x4d3521, 0.5, 0.45), 0, 5.05, z);
}

const doorGroup = new THREE.Group();
const doorMat = mat(0x1b1513, 0.48, 0.24);
const leftDoor = makeBox(4.8, 6.2, 0.28, doorMat, -2.4, 1, 2.2);
const rightDoor = makeBox(4.8, 6.2, 0.28, doorMat, 2.4, 1, 2.2);
doorGroup.add(leftDoor, rightDoor);
scene.add(doorGroup);

function makeBench(x, z) {
  const seat = makeBox(3.1, 0.32, 0.78, mat(0x071326, 0.38, 0.22), x, -1.42, z);
  const legMat = mat(0x8b642e, 0.42, 0.5);
  [[-1.25, -0.25], [1.25, -0.25], [-1.25, 0.25], [1.25, 0.25]].forEach(([lx, lz]) => {
    makeBox(0.12, 0.72, 0.12, legMat, x + lx, -1.88, z + lz);
  });
  return seat;
}
makeBench(-4.7, -7.2);
makeBench(4.7, -7.2);

function textTexture(title, subtitle) {
  const c = document.createElement('canvas');
  c.width = 1024; c.height = 420;
  const ctx = c.getContext('2d');
  ctx.fillStyle = '#11151d';
  ctx.fillRect(0, 0, c.width, c.height);
  ctx.strokeStyle = '#d8aa5d';
  ctx.lineWidth = 6;
  ctx.strokeRect(18, 18, c.width - 36, c.height - 36);
  ctx.fillStyle = '#f4d38a';
  ctx.font = '54px Georgia';
  ctx.textAlign = 'center';
  wrap(ctx, title, c.width / 2, 120, 820, 58);
  ctx.fillStyle = '#d6ccd7';
  ctx.font = '30px Segoe UI';
  wrap(ctx, subtitle, c.width / 2, 270, 860, 38);
  const texture = new THREE.CanvasTexture(c);
  texture.colorSpace = THREE.SRGBColorSpace;
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
  const t = loader.load(art.image);
  t.colorSpace = THREE.SRGBColorSpace;
  const imageMat = new THREE.MeshBasicMaterial({ map: t });
  const w = art.scene.width;
  const h = art.scene.height;
  const plane = new THREE.Mesh(new THREE.PlaneGeometry(w, h), imageMat);
  plane.position.z = 0.04;
  plane.userData.art = art;
  group.add(plane);
  clickable.push(plane);

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
  const plaqueWidth = Math.min(3.9, w + 1.0);
  const plaqueY = (art.placement === 'pedestal' || art.placement === 'center') ? -h / 2 - 0.38 : -h / 2 - 0.76;
  const plaqueZ = (art.placement === 'pedestal' || art.placement === 'center') ? 0.72 : 0.12;
  const plaqueBack = new THREE.Mesh(new THREE.BoxGeometry(plaqueWidth + 0.16, 1.0, 0.1), mat(0x0f1118, 0.52, 0.36));
  plaqueBack.position.set(0, plaqueY, plaqueZ - 0.05);
  group.add(plaqueBack);
  const plaque = new THREE.Mesh(new THREE.PlaneGeometry(plaqueWidth, 0.82), new THREE.MeshBasicMaterial({ map: plaqueTexture }));
  plaque.position.set(0, plaqueY, plaqueZ + 0.03);
  group.add(plaque);

  if (art.placement === 'pedestal' || art.placement === 'center') {
    const pedestal = new THREE.Mesh(new THREE.CylinderGeometry(w * 0.42, w * 0.5, 0.8, 48), mat(0x1a1210, 0.42, 0.38));
    pedestal.position.set(0, -h / 2 - 0.64, -0.28);
    group.add(pedestal);
  }

  group.position.set(art.scene.x, art.scene.y, art.scene.z);
  group.rotation.y = THREE.MathUtils.degToRad(art.scene.ry);
  group.userData.baseY = group.position.y;
  group.userData.index = index;
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
  modalImage.src = art.image;
  modalImage.alt = art.title;
  modalTitle.textContent = art.title;
  modalText.textContent = `${art.note} ${art.intent}`;
  modalDetail.href = art.detailUrl;
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
  sample.pos.y += Math.sin(current * Math.PI * 18) * 0.025;
  camera.position.copy(sample.pos);
  camera.lookAt(sample.look);
  const door = Math.min(1, current / 0.11);
  leftDoor.rotation.y = -door * 1.25;
  rightDoor.rotation.y = door * 1.25;
  frames.forEach((group, index) => {
    const distance = Math.abs(group.position.z - camera.position.z);
    const active = distance < 7;
    group.position.y = group.userData.baseY + Math.sin(performance.now() * 0.001 + index) * (active ? 0.05 : 0.015);
    group.scale.setScalar(active ? 1.04 : 1);
  });
  renderer.render(scene, camera);
}
animate();
"""


APP_JS = r"""
const drawer = document.getElementById('purchaseDrawer');
const purchaseArtwork = document.getElementById('purchaseArtwork');

function openPurchase(title) {
  if (title && purchaseArtwork) purchaseArtwork.value = title;
  drawer?.setAttribute('aria-hidden', 'false');
}
function closePurchase() { drawer?.setAttribute('aria-hidden', 'true'); }

document.querySelectorAll('[data-open-purchase]').forEach((button) => {
  button.addEventListener('click', () => openPurchase(button.dataset.artTitle || purchaseArtwork?.value));
});
document.querySelectorAll('[data-close-purchase]').forEach((button) => button.addEventListener('click', closePurchase));

document.querySelector('[data-copy-request]')?.addEventListener('click', () => {
  const form = drawer?.querySelector('form');
  const data = new FormData(form);
  const text = [
    'Здравствуйте. Хочу обсудить покупку картины Татьяны Мунн.',
    `Картина: ${data.get('artwork') || ''}`,
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
            "singleNVisibleHits": text.count("Татьяна Мун</"),
            "hasThreeJs": (OUT / "gallery-3d.js").read_text(encoding="utf-8").count("THREE.") > 10,
            "hasPurchaseRequestLayer": "purchaseDrawer" in (OUT / "app.js").read_text(encoding="utf-8"),
            "hasArtworkJson": (DATA_DIR / "artworks.json").exists(),
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
    build_report(records)
    build_zip()
    print(json.dumps({"output": str(OUT), "zip": str(ZIP_OUT), "artworks": len(records)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
