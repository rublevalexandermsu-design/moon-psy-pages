import json
import re
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(
    r"C:\пайтонннн.. тесты\код сайт татьяна мунн\Коды для сайта татьяны.готовые\Окончательный.код.сай..html"
)
OUT_DIR = ROOT / "docs" / "psychologist-tatiana-munn-landing"
BODY_OUT = OUT_DIR / "tilda-html-block-final.html"
FULL_OUT = OUT_DIR / "tilda-page-final.html"
HEAD_OUT = OUT_DIR / "tilda-head-seo-final.html"
REPORT_OUT = OUT_DIR / "quality-report.json"

URL = "https://moonn.ru/psiholog-tatiana-moonn"
ICLIENT_URL = "https://n461584.yclients.com/"
YOUTUBE_CHANNEL_URL = "https://youtube.com/channel/UCyAQlNoDtg7En6BdwbctSrQ"
REVIEWS_URL = "https://moonn.ru/otzivi"
TITLE = "Психолог Татьяна Мунн в Москве и онлайн | консультации, отзывы, запись"
DESCRIPTION = (
    "Татьяна Мунн — психолог МГУ в Москве и онлайн. Консультации для взрослых "
    "и подростков, эмоциональный интеллект, отношения, тревога, выгорание, отзывы и онлайн-запись."
)


def remove_html_comments(html: str) -> str:
    return re.sub(r"<!--[\s\S]*?-->", "", html)


def replace_json_ld(html: str) -> str:
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Person",
                "@id": "https://moonn.ru/#tatiana-munn",
                "name": "Татьяна Мунн",
                "alternateName": [
                    "Кумскова Татьяна Михайловна",
                    "Татьяна Мунн (Кумскова)",
                    "Tatiana Munn",
                    "Tatiana Moonn",
                ],
                "jobTitle": "Психолог МГУ, эксперт по эмоциональному интеллекту",
                "url": URL,
                "sameAs": [
                    "https://moonn.ru/",
                    URL,
                    ICLIENT_URL,
                    YOUTUBE_CHANNEL_URL,
                    "https://moonn.timepad.ru/events/",
                    "https://uslugi.yandex.ru/profile/TatyanaKumskovamunn-948629",
                    "https://istina.msu.ru/workers/816305440/",
                    "https://psyjournals.ru/authors/15337",
                ],
                "knowsAbout": [
                    "эмоциональный интеллект",
                    "психология эмоций",
                    "тревога",
                    "стресс",
                    "выгорание",
                    "отношения",
                    "личные границы",
                    "подростковая психология",
                ],
            },
            {
                "@type": "WebPage",
                "@id": URL + "#webpage",
                "url": URL,
                "name": TITLE,
                "description": DESCRIPTION,
                "isPartOf": {"@id": "https://moonn.ru/#website"},
                "about": {"@id": "https://moonn.ru/#tatiana-munn"},
                "author": {"@id": "https://moonn.ru/#tatiana-munn"},
                "inLanguage": "ru-RU",
            },
            {
                "@type": "ProfessionalService",
                "@id": URL + "#service",
                "name": "Психолог Татьяна Мунн — консультации в Москве и онлайн",
                "url": URL,
                "provider": {"@id": "https://moonn.ru/#tatiana-munn"},
                "areaServed": ["Москва", "Онлайн"],
                "serviceType": [
                    "Индивидуальная психологическая консультация",
                    "Консультация психолога онлайн",
                    "Психолог для подростков",
                    "Психологическая помощь при тревоге, выгорании и сложностях в отношениях",
                ],
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": "Москва",
                    "streetAddress": "Цветной бульвар, д. 19, стр. 4",
                    "addressCountry": "RU",
                },
                "description": DESCRIPTION,
            },
            {
                "@type": "BreadcrumbList",
                "@id": URL + "#breadcrumbs",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Главная",
                        "item": "https://moonn.ru/",
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "Психолог Татьяна Мунн",
                        "item": URL,
                    },
                ],
            },
        ],
    }
    block = (
        '<script id="tmSeoJsonLd" type="application/ld+json">\n'
        + json.dumps(schema, ensure_ascii=False, indent=2)
        + "\n</script>"
    )
    return re.sub(
        r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>[\s\S]*?</script>',
        block,
        html,
        count=1,
        flags=re.I,
    )


def replace_lectures_section(html: str) -> str:
    section = f"""
    <section id="lectures">
      <div class="wrap">
        <div class="title">
          <div>
            <h2>Лекции и видео</h2>
            <p>Актуальные видео и записи выступлений собраны на YouTube-канале Татьяны Мунн. Если встроенное видео не открывается, переходите на канал напрямую.</p>
          </div>
        </div>

        <div class="big-cta reveal" data-glow>
          <div>
            <h3>Видео о психологии эмоций, отношениях и саморегуляции</h3>
            <p>Канал помогает познакомиться с подходом Татьяны Мунн до консультации: лекции, объяснения метода «Быстрая психология», темы тревоги, выгорания, отношений и эмоционального интеллекта.</p>
            <div class="hero-actions" style="margin-top:12px">
              <a class="btn primary" href="{YOUTUBE_CHANNEL_URL}" target="_blank" rel="noreferrer" data-moonn-goal="youtube_channel">Открыть YouTube-канал</a>
              <a class="btn" href="{ICLIENT_URL}" target="_blank" rel="noreferrer" data-moonn-goal="iclient_booking">Записаться на консультацию</a>
            </div>
          </div>
        </div>
      </div>
    </section>
"""
    return re.sub(
        r'\s*<section id=["\']lectures["\'][\s\S]*?</section>\s*(?=<section id=["\']park["\'])',
        "\n" + section + "\n",
        html,
        count=1,
        flags=re.I,
    )


def replace_payment_buttons(html: str) -> str:
    replacements = {
        r'<button class="btn ghost" type="button" data-pay-open="single" aria-label="Оплата онлайн">Оплатить</button>':
            f'<a class="btn ghost" href="{ICLIENT_URL}" target="_blank" rel="noreferrer" data-moonn-goal="iclient_booking">Онлайн-запись</a>',
        r'<button class="btn ghost" type="button" data-pay-open="single">Оплата</button>':
            f'<a class="btn ghost" href="{ICLIENT_URL}" target="_blank" rel="noreferrer" data-moonn-goal="iclient_booking">Онлайн-запись</a>',
        r'<button class="btn ghost" type="button" data-pay-open="single">Оплатить</button>':
            f'<a class="btn ghost" href="{ICLIENT_URL}" target="_blank" rel="noreferrer" data-moonn-goal="iclient_booking">Онлайн-запись</a>',
        r'<button class="btn ghost" type="button" data-pay-open="single">Оплата онлайн</button>':
            f'<a class="btn ghost" href="{ICLIENT_URL}" target="_blank" rel="noreferrer" data-moonn-goal="iclient_booking">Онлайн-запись</a>',
        r'<button class="btn primary" type="button" data-pay-open="single">Оплатить</button>':
            f'<a class="btn primary" href="{ICLIENT_URL}" target="_blank" rel="noreferrer" data-moonn-goal="iclient_booking">Выбрать время</a>',
        r'<button class="btn primary" type="button" data-pay-open="pack3">Оплатить пакет</button>':
            f'<a class="btn primary" href="{ICLIENT_URL}" target="_blank" rel="noreferrer" data-moonn-goal="iclient_booking">Записаться</a>',
        r'<button class="btn primary" type="button" data-pay-open="pack5">Оплатить пакет</button>':
            f'<a class="btn primary" href="{ICLIENT_URL}" target="_blank" rel="noreferrer" data-moonn-goal="iclient_booking">Записаться</a>',
        r'<button class="btn primary" type="button" data-pay-open="teen">Оплатить</button>':
            f'<a class="btn primary" href="{ICLIENT_URL}" target="_blank" rel="noreferrer" data-moonn-goal="iclient_booking">Выбрать время</a>',
    }
    for old, new in replacements.items():
        html = html.replace(old, new)
    html = html.replace(
        '<a class="btn primary" href="#consult">Выбрать формат консультации</a>',
        f'<a class="btn primary" href="{ICLIENT_URL}" target="_blank" rel="noreferrer" data-moonn-goal="iclient_booking">Записаться онлайн</a>',
    )
    html = html.replace(
        '<a class="btn primary" href="#consult">Онлайн-запись</a>',
        f'<a class="btn primary" href="{ICLIENT_URL}" target="_blank" rel="noreferrer" data-moonn-goal="iclient_booking">Онлайн-запись</a>',
    )
    html = html.replace(
        "Запись и оплата: Telegram, WhatsApp, карта, СБП",
        "Онлайн-запись: iClient/YCLIENTS; контактные каналы — для уточнений",
    )
    html = html.replace(
        "Выберите способ оплаты. После оплаты напишите в Telegram/WhatsApp - зафиксируем время.",
        "Выберите удобную дату и время в iClient/YCLIENTS. Если нужен другой формат, используйте контакты ниже.",
    )
    html = html.replace(
        "Это не диагноз и не мед.оценка. Это “быстрая настройка фокуса”, чтобы не терять время.",
        "Это не диагноз и не медицинская оценка. Это короткая ориентация по запросу перед консультацией.",
    )
    html = html.replace(
        'href="http://n461584.yclients.com/"',
        f'href="{ICLIENT_URL}" data-moonn-goal="iclient_booking"',
    )
    return html


def remove_payment_modal_and_legacy_js(html: str) -> str:
    html = re.sub(
        r'\s*<div class="modal" id="payModal" aria-hidden="true">[\s\S]*?</div>\s*(?=<main>)',
        "\n",
        html,
        count=1,
        flags=re.I,
    )
    html = re.sub(
        r"\s*// =========================\s*// Оплата: конфиг[\s\S]*?const PAY_CFG = \{[\s\S]*?\n      \};\s*",
        "\n",
        html,
        count=1,
    )
    html = re.sub(
        r"\s*// =========================\s*// Оплата - модалка[\s\S]*?window\.addEventListener\('keydown', \(e\)=>\{\s*if\(e\.key === 'Escape'\) closePay\(\);\s*\}\);\s*",
        "\n",
        html,
        count=1,
    )
    return html


def inject_responsive_safety_css(html: str) -> str:
    css = """

  /* Moonn publication QA: prevent horizontal overflow in Tilda/mobile shells. */
  .tm-root, .tm-root #tmRoot{max-width:100%; overflow-x:hidden}
  .tm-root .wrap,
  .tm-root .card,
  .tm-root .hero-card,
  .tm-root .side,
  .tm-root .big-cta,
  .tm-root .drawer .panel{max-width:100%; min-width:0}
  .tm-root p,
  .tm-root li,
  .tm-root h1,
  .tm-root h2,
  .tm-root h3{overflow-wrap:anywhere}
  .tm-root .hero-actions{display:flex; flex-wrap:wrap}
  .tm-root .btn{max-width:100%; min-width:0; text-align:center}
  .tm-root img,
  .tm-root video,
  .tm-root iframe{max-width:100%; height:auto}

  @media (max-width: 560px){
    .tm-root .nav-inner{gap:8px}
    .tm-root .brand{min-width:0; flex:1 1 96px}
    .tm-root .brand b{line-height:1.1}
    .tm-root .cta{flex:0 1 236px; justify-content:flex-end; gap:8px}
    .tm-root .cta .btn{padding:10px 12px; font-size:12px}
    .tm-root .hero-actions{flex-direction:column}
    .tm-root .hero-actions .btn{width:100%; white-space:normal; line-height:1.2}
    .tm-root .bottom-cta{left:12px; right:12px; max-width:calc(100vw - 24px); gap:8px}
    .tm-root .bottom-cta a{white-space:normal; line-height:1.2; padding:10px 8px}
    .tm-root .review-carousel .slide,
    .tm-root .lectures-carousel .slide,
    .tm-root .slide{flex-basis:88%; max-width:88%}
  }
"""
    return html.replace("</style>", css + "\n</style>", 1)


def add_booking_links(html: str) -> str:
    html = html.replace(
        '<a class="btn primary" href="https://t.me/Tatiana_Moonn" target="_blank" rel="noreferrer">Написать</a>',
        f'<a class="btn primary" href="{ICLIENT_URL}" target="_blank" rel="noreferrer" data-moonn-goal="iclient_booking">Онлайн-запись</a>',
        1,
    )
    html = html.replace(
        '<a class="btn primary" href="https://t.me/Tatiana_Moonn" target="_blank" rel="noreferrer">Личное сообщение</a>',
        f'<a class="btn primary" href="{ICLIENT_URL}" target="_blank" rel="noreferrer" data-moonn-goal="iclient_booking">Онлайн-запись</a>',
    )
    html = html.replace(
        '<a class="btn primary" href="https://t.me/Tatiana_Moonn" target="_blank" rel="noreferrer">Написать в Telegram</a>',
        f'<a class="btn primary" href="{ICLIENT_URL}" target="_blank" rel="noreferrer" data-moonn-goal="iclient_booking">Записаться в iClient</a>',
        1,
    )
    html = html.replace(
        '<li><span class="bullet"></span> Сайт: <a href="https://moonn.ru/" target="_blank" rel="noreferrer">moonn.ru</a></li>',
        f'<li><span class="bullet"></span> Онлайн-запись: <a href="{ICLIENT_URL}" target="_blank" rel="noreferrer" data-moonn-goal="iclient_booking">iClient/YCLIENTS</a></li>\n'
        '<li><span class="bullet"></span> Сайт: <a href="https://moonn.ru/" target="_blank" rel="noreferrer">moonn.ru</a></li>',
    )
    return html


def add_click_tracking(html: str) -> str:
    tracking = """
  <script>
    (function(){
      var goalMap = {
        iclient_booking: 'consultation_iclient_click',
        youtube_channel: 'youtube_channel_click',
        reviews: 'reviews_click'
      };
      document.addEventListener('click', function(event){
        var link = event.target.closest && event.target.closest('a[data-moonn-goal]');
        if(!link) return;
        var goal = goalMap[link.getAttribute('data-moonn-goal')] || link.getAttribute('data-moonn-goal');
        if(window.ym && goal){
          try{ window.ym(96397286, 'reachGoal', goal); }catch(error){}
        }
      }, true);
    })();
  </script>
"""
    return html.replace("</div>\n\n\n\n<script>", "</div>\n" + tracking + "\n<script>", 1)


def clean_html() -> str:
    html = SOURCE.read_text(encoding="utf-8-sig")
    html = remove_html_comments(html)
    html = replace_json_ld(html)
    html = replace_lectures_section(html)
    html = replace_payment_buttons(html)
    html = remove_payment_modal_and_legacy_js(html)
    html = inject_responsive_safety_css(html)
    html = add_booking_links(html)
    html = html.replace("https://youtube.com/channel/UCpTJZh6wGfDSn04QRRRu04g", YOUTUBE_CHANNEL_URL)
    html = html.replace("https://www.youtube.com/channel/UCpTJZh6wGfDSn04QRRRu04g", YOUTUBE_CHANNEL_URL)
    html = html.replace('href="https://moonn.ru/otzivi"', f'href="{REVIEWS_URL}" data-moonn-goal="reviews"')
    html = add_click_tracking(html)
    html = re.sub(r"\n{4,}", "\n\n", html)
    return html.strip() + "\n"


def build_head() -> str:
    return f"""<title>{escape(TITLE)}</title>
<meta name="description" content="{escape(DESCRIPTION)}">
<link rel="canonical" href="{URL}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="website">
<meta property="og:url" content="{URL}">
<meta property="og:title" content="{escape(TITLE)}">
<meta property="og:description" content="{escape(DESCRIPTION)}">
<meta name="twitter:card" content="summary_large_image">
"""


def build_full_page(body: str, head: str) -> str:
    return f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{head}</head>
<body>
{body}</body>
</html>
"""


def text_from_html(html: str) -> str:
    no_code = re.sub(r"<script\b[^>]*>[\s\S]*?</script>", " ", html, flags=re.I)
    no_code = re.sub(r"<style\b[^>]*>[\s\S]*?</style>", " ", no_code, flags=re.I)
    no_tags = re.sub(r"<[^>]+>", " ", no_code)
    return re.sub(r"\s+", " ", no_tags).strip()


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    body = clean_html()
    head = build_head()
    full = build_full_page(body, head)
    BODY_OUT.write_text(body, encoding="utf-8")
    HEAD_OUT.write_text(head, encoding="utf-8")
    FULL_OUT.write_text(full, encoding="utf-8")
    visible_text = text_from_html(body)
    report = {
        "source": str(SOURCE),
        "outputs": {
            "body": str(BODY_OUT.relative_to(ROOT)),
            "head": str(HEAD_OUT.relative_to(ROOT)),
            "full": str(FULL_OUT.relative_to(ROOT)),
        },
        "url": URL,
        "iclient_url": ICLIENT_URL,
        "youtube_channel_url": YOUTUBE_CHANNEL_URL,
        "checks": {
            "has_title": bool(re.search(r"<title>", full, re.I)),
            "has_description": "name=\"description\"" in full,
            "has_canonical": URL in head,
            "h1_count": len(re.findall(r"<h1\b", body, flags=re.I)),
            "h2_count": len(re.findall(r"<h2\b", body, flags=re.I)),
            "jsonld_count": len(re.findall(r"application/ld\+json", body, flags=re.I)),
            "has_iclient": ICLIENT_URL in body,
            "has_youtube_channel": YOUTUBE_CHANNEL_URL in body,
            "old_youtube_embeds": len(re.findall(r"youtube\.com/embed/(P-Pdy2jG00g|wVloZ-9F3AY|4dV0EqbZGkU|NmNkVEdmMmM|igkWXqSE1lc|4HRLYnAiPXY|uJPaCLabzIU)", body, flags=re.I)),
            "visible_internal_hits": len(re.findall(r"НАСТРОЙКА|если Тильда|вставь реальные|TODO|MVP|техническ|черновик|placeholder", visible_text, flags=re.I)),
            "raw_internal_hits": len(re.findall(r"НАСТРОЙКА|если Тильда|вставь реальные|TODO|MVP|техническ|черновик|placeholder", body, flags=re.I)),
        },
    }
    REPORT_OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
