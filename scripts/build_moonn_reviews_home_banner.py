from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs" / "tatiana-munn-reviews-home-banner"
FUNNEL_DIR = ROOT / "docs" / "tatiana-munn-review-funnel"
BLOCK_PATH = DOCS_DIR / "tilda-html-block-final.html"
PREVIEW_PATH = DOCS_DIR / "homepage-reviews-banner-preview.html"
COMBINED_PATH = DOCS_DIR / "homepage-t123-combined-2026-05-17.html"
QR_SVG_PATH = FUNNEL_DIR / "qr-moonn-review-funnel.svg"


READ_URL = "/otzivi"
REVIEW_URL = "/otzivi?source=homepage_reviews_banner#moonn-review-funnel"


def build_block() -> str:
    qr_svg = QR_SVG_PATH.read_text(encoding="utf-8")
    qr_svg = qr_svg.replace("<svg ", '<svg class="qr-svg" aria-hidden="true" ')
    return f"""<section id="moonn-reviews-home-banner" class="moonn-reviews-home-banner" aria-label="Отзывы клиентов Татьяны Мунн">
  <style>
    #moonn-reviews-home-banner{{box-sizing:border-box;width:100%;margin:0;padding:48px 20px 56px;background:linear-gradient(135deg,#fff 0%,#f6efff 44%,#edf9ff 100%);font-family:Arial,sans-serif;color:#231b33;overflow:hidden}}
    #moonn-reviews-home-banner *{{box-sizing:border-box;letter-spacing:0}}
    #moonn-reviews-home-banner .wrap{{width:min(100%,1160px);max-width:1160px;margin:0 auto;display:grid;grid-template-columns:minmax(0,1.04fr) minmax(300px,.96fr);gap:28px;align-items:stretch;border:1px solid rgba(133,75,210,.18);border-radius:30px;background:rgba(255,255,255,.74);box-shadow:0 18px 55px rgba(70,34,140,.14);overflow:hidden;backdrop-filter:blur(14px)}}
    #moonn-reviews-home-banner .copy{{min-width:0;padding:40px 0 40px 44px;display:grid;align-content:center}}
    #moonn-reviews-home-banner .eyebrow{{display:inline-flex;width:fit-content;max-width:100%;margin:0 0 16px;padding:8px 14px;border-radius:999px;background:rgba(116,77,210,.10);color:#5b2ec7;font-size:14px;font-weight:700;text-transform:uppercase}}
    #moonn-reviews-home-title{{margin:0 0 18px;font-size:40px;line-height:1.08;font-weight:800;color:#5220b8}}
    #moonn-reviews-home-banner p{{max-width:650px;margin:0 0 22px;font-size:18px;line-height:1.55;color:#40354d;overflow-wrap:anywhere}}
    #moonn-reviews-home-banner .meta{{display:flex;flex-wrap:wrap;gap:10px;margin:0 0 26px;padding:0;list-style:none}}
    #moonn-reviews-home-banner .meta li{{padding:8px 12px;border-radius:999px;background:#fff;border:1px solid rgba(82,32,184,.15);font-size:14px;color:#342845;white-space:nowrap}}
    #moonn-reviews-home-banner .actions{{display:flex;flex-wrap:wrap;gap:10px;align-items:center}}
    #moonn-reviews-home-banner .cta{{display:inline-flex;align-items:center;justify-content:center;width:fit-content;min-height:48px;padding:0 24px;border-radius:999px;background:linear-gradient(90deg,#6f2ee8,#e743b5,#32b9ef);color:#fff!important;text-decoration:none!important;font-size:16px;font-weight:800;box-shadow:0 12px 28px rgba(111,46,232,.28);transition:transform .2s ease,box-shadow .2s ease}}
    #moonn-reviews-home-banner .cta.secondary{{background:#fff;color:#5220b8!important;border:1px solid rgba(82,32,184,.22);box-shadow:none}}
    #moonn-reviews-home-banner .cta:hover{{transform:translateY(-2px);box-shadow:0 18px 34px rgba(111,46,232,.30)}}
    #moonn-reviews-home-banner .media{{min-width:0;min-height:360px;position:relative;display:grid;align-content:center;gap:14px;padding:34px;background:radial-gradient(circle at 85% 16%,rgba(252,204,0,.28),transparent 33%),linear-gradient(135deg,#fffaf0 0%,#fff 45%,#f4fbff 100%);border-left:1px solid rgba(133,75,210,.14);text-decoration:none!important;overflow:hidden}}
    #moonn-reviews-home-banner .source{{display:flex;align-items:center;gap:12px;margin-bottom:2px;color:#281b36;font-size:18px;font-weight:900}}
    #moonn-reviews-home-banner .source-mark{{display:grid;place-items:center;width:42px;height:42px;border-radius:13px;background:#fc0;color:#111;font-size:25px;font-weight:900;box-shadow:0 12px 24px rgba(132,92,0,.18)}}
    #moonn-reviews-home-banner .review-card{{position:relative;padding:15px 16px 15px 18px;border:1px solid rgba(82,32,184,.12);border-radius:18px;background:rgba(255,255,255,.82);box-shadow:0 12px 30px rgba(67,45,110,.10);color:#3f334e}}
    #moonn-reviews-home-banner .review-card strong{{display:block;margin:0 0 6px;color:#5220b8;font-size:15px;line-height:1.25}}
    #moonn-reviews-home-banner .review-card span{{display:block;font-size:14px;line-height:1.45;color:#5a5063;overflow-wrap:anywhere}}
    #moonn-reviews-home-banner .qr-box{{display:grid;grid-template-columns:104px minmax(0,1fr);gap:14px;align-items:center;padding:14px;border:1px dashed rgba(82,32,184,.22);border-radius:18px;background:rgba(255,255,255,.88)}}
    #moonn-reviews-home-banner .qr-svg{{width:104px;height:104px;display:block;background:#fff;border-radius:8px}}
    #moonn-reviews-home-banner .qr-box b{{display:block;margin:0 0 4px;color:#5220b8;font-size:15px}}
    #moonn-reviews-home-banner .qr-box span{{display:block;color:#5a5063;font-size:13px;line-height:1.4;overflow-wrap:anywhere}}
    @media (max-width:820px){{#moonn-reviews-home-banner{{max-width:100vw;padding:34px 14px}}#moonn-reviews-home-banner .wrap{{width:100%;max-width:calc(100vw - 28px);grid-template-columns:1fr;border-radius:22px}}#moonn-reviews-home-banner .copy{{padding:28px 24px 10px}}#moonn-reviews-home-title{{font-size:30px}}#moonn-reviews-home-banner p{{font-size:16px}}#moonn-reviews-home-banner .media{{min-height:260px;padding:24px;border-left:0;border-top:1px solid rgba(133,75,210,.14)}}}}
    @media (max-width:520px){{#moonn-reviews-home-banner .meta li{{white-space:normal}}#moonn-reviews-home-banner .source{{font-size:16px}}#moonn-reviews-home-banner .source-mark{{width:36px;height:36px;font-size:22px}}#moonn-reviews-home-banner .review-card{{padding:13px 14px}}#moonn-reviews-home-banner .qr-box{{grid-template-columns:1fr}}}}
  </style>
  <div class="wrap">
    <div class="copy">
      <span class="eyebrow">Отзывы · Яндекс Услуги · доверие</span>
      <h2 id="moonn-reviews-home-title">Отзывы о Татьяне Мунн</h2>
      <p>Отзывы клиентов и участников лекций собраны на отдельной странице. Там можно прочитать отзывы, поставить оценку на Яндекс Услугах и оставить текстовый отзыв для сайта Moonn.</p>
      <ul class="meta"><li>Источник указан</li><li>Профиль Яндекс Услуг</li><li>QR для участников</li></ul>
      <div class="actions">
        <a class="cta" href="{READ_URL}">Читать отзывы</a>
        <a class="cta secondary" href="{REVIEW_URL}">Оставить отзыв</a>
      </div>
    </div>
    <div class="media" aria-label="QR-код и переход к отзывам о Татьяне Мунн">
      <div class="source"><span class="source-mark">Я</span><span>Проверяемые отзывы</span></div>
      <div class="review-card"><strong>Оценка на Яндекс Услугах</strong><span>Кнопка открывает официальную форму оценки исполнителя.</span></div>
      <div class="review-card"><strong>Текстовый отзыв для Moonn</strong><span>Комментарий можно оставить на странице отзывов сайта.</span></div>
      <a class="qr-box" href="{REVIEW_URL}" aria-label="Открыть страницу, где можно оставить отзыв о Татьяне Мунн">
        {qr_svg}
        <span><b>Навести камеру</b>QR ведёт на страницу оценки и текстового отзыва.<br>{REVIEW_URL}</span>
      </a>
    </div>
  </div>
</section>"""


def build_preview(block: str) -> str:
    return f"""<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Preview: отзывы Татьяны Мунн на главной</title>
  <style>body{{margin:0;background:#f7f4ff}}</style>
</head>
<body>
{block}
</body>
</html>
"""


def update_combined(block: str) -> None:
    if not COMBINED_PATH.exists():
        return
    html = COMBINED_PATH.read_text(encoding="utf-8")
    marker = '<section id="moonn-reviews-home-banner"'
    start = html.find(marker)
    if start == -1:
        raise RuntimeError("Reviews section marker not found in combined homepage T123 file.")
    end = html.find("</section>", start)
    if end == -1:
        raise RuntimeError("Reviews section closing tag not found in combined homepage T123 file.")
    end += len("</section>")
    COMBINED_PATH.write_text(html[:start] + block + html[end:], encoding="utf-8")


def main() -> None:
    block = build_block()
    BLOCK_PATH.write_text(block + "\n", encoding="utf-8")
    PREVIEW_PATH.write_text(build_preview(block), encoding="utf-8")
    update_combined(block)
    print({
        "block": str(BLOCK_PATH),
        "preview": str(PREVIEW_PATH),
        "combined": str(COMBINED_PATH),
        "review_url": REVIEW_URL,
    })


if __name__ == "__main__":
    main()
