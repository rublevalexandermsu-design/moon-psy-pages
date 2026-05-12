from __future__ import annotations

import json
import re
from datetime import datetime
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(r"C:\Users\yanta\Downloads\tatiana-moonn-exam-landing-v3-self-contained.html")
OUT = ROOT / "docs" / "tatiana-munn-exam-prep"
HISTORY = ROOT / "docs" / "codex-chat-history.md"
ART_GALLERY_HOME = ROOT / "docs" / "tatiana-munn-art-gallery" / "homepage-t123-combined-2026-05-12.html"

TILDA_PROJECT_ID = "8326812"
TILDA_HOMEPAGE_ID = "42678538"
TILDA_HOMEPAGE_T123_RECORD_ID = "2251351151"
TILDA_PAGE_ALIAS = "psihologicheskaya-podgotovka-k-ekzamenam"
TILDA_PAGE_URL = f"https://moonn.ru/{TILDA_PAGE_ALIAS}"
TILDA_PAGE_TITLE = "Психологическая подготовка к ОГЭ и ЕГЭ — Татьяна Мунн"
TILDA_PAGE_DESCRIPTION = (
    "Индивидуальные консультации психолога для школьников и студентов перед ОГЭ, "
    "ЕГЭ, сессией и экзаменами: тревога, ступор, страх ошибки и поддержка родителей."
)


def read_source() -> str:
    if not SOURCE.exists():
        raise FileNotFoundError(f"Source landing file is missing: {SOURCE}")
    return SOURCE.read_text(encoding="utf-8")


def first_match(text: str, pattern: str, *, default: str = "") -> str:
    match = re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else default


def extract_body(html: str) -> str:
    body = first_match(html, r"<body[^>]*>(.*)</body>")
    if not body:
        raise ValueError("Source landing does not contain a body tag.")
    return body


def extract_head_assets(html: str) -> str:
    head = first_match(html, r"<head[^>]*>(.*)</head>")
    if not head:
        return ""
    styles = re.findall(r"<style\b[^>]*>.*?</style>", head, flags=re.IGNORECASE | re.DOTALL)
    schemas = re.findall(
        r"<script\b[^>]*type=[\"']application/ld\+json[\"'][^>]*>.*?</script>",
        head,
        flags=re.IGNORECASE | re.DOTALL,
    )
    return "\n".join([*schemas, *styles]).strip()


def normalize_for_tilda(html: str) -> str:
    html = html.replace("https://moonn.ru/psihologicheskaya-podgotovka-k-ekzamenam", TILDA_PAGE_URL)
    html = re.sub(r"\s+data-moonn-exam-prep-tilda=[\"'][^\"']*[\"']", "", html)
    html = html.replace(
        'id="tm-exam-page"',
        'id="tm-exam-page" data-moonn-exam-prep-tilda="true"',
        1,
    )
    return html


def strip_data_images(text: str) -> str:
    return re.sub(r"data:image/[^\"']+", "data:image/...", text)


def assert_public_text_is_clean(html: str) -> None:
    visible_scan = strip_data_images(html)
    forbidden = [
        "не дубль",
        "контур",
        "выглядит как",
        "зачем этот раздел",
        "для старта",
        "будущая автоматическая",
        "карточка для заявки",
        "статус будет обновлён",
        "технический",
        "MVP",
        "прототип",
        "раздел нужен",
    ]
    hits = [word for word in forbidden if word.lower() in visible_scan.lower()]
    if hits:
        raise ValueError(f"Public HTML contains internal wording: {hits}")


def extract_image(html: str, preferred_alt: str) -> tuple[str, str]:
    for tag in re.findall(r"<img\b[^>]*>", html, flags=re.IGNORECASE | re.DOTALL):
        alt = first_match(tag, r"alt=[\"']([^\"']*)[\"']")
        src = first_match(tag, r"src=[\"']([^\"']*)[\"']")
        if preferred_alt.lower() in alt.lower() and src.startswith("data:image/"):
            return src, alt
    for tag in re.findall(r"<img\b[^>]*>", html, flags=re.IGNORECASE | re.DOTALL):
        alt = first_match(tag, r"alt=[\"']([^\"']*)[\"']")
        src = first_match(tag, r"src=[\"']([^\"']*)[\"']")
        if src.startswith("data:image/"):
            return src, alt
    raise ValueError("No inline image found for homepage banner.")


def build_tilda_page_block(source_html: str) -> str:
    head_assets = extract_head_assets(source_html)
    body = normalize_for_tilda(extract_body(source_html))
    block = f"""<section id="moonn-exam-prep-tilda-page" aria-label="Психологическая подготовка к экзаменам Татьяны Мунн">
{head_assets}
{body}
</section>
"""
    assert_public_text_is_clean(block)
    return block


def build_full_preview(block: str) -> str:
    return f"""<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(TILDA_PAGE_TITLE)}</title>
  <meta name="description" content="{escape(TILDA_PAGE_DESCRIPTION)}">
  <link rel="canonical" href="{TILDA_PAGE_URL}">
</head>
<body>
{block}
</body>
</html>
"""


def build_homepage_banner(source_html: str) -> str:
    image_src, image_alt = extract_image(source_html, "Татьяна Мунн")
    return f"""<section id="moonn-exam-prep-home-banner" class="moonn-exam-prep-home-banner" aria-label="Психологическая подготовка к экзаменам">
  <style>
    #moonn-exam-prep-home-banner{{margin:0;padding:48px 20px 56px;background:linear-gradient(135deg,#fff 0%,#f6efff 44%,#edf9ff 100%);font-family:Arial,sans-serif;color:#231b33}}
    #moonn-exam-prep-home-banner *{{box-sizing:border-box}}
    #moonn-exam-prep-home-banner .wrap{{max-width:1160px;margin:0 auto;display:grid;grid-template-columns:minmax(0,1.08fr) minmax(300px,.92fr);gap:28px;align-items:center;border:1px solid rgba(133,75,210,.18);border-radius:30px;background:rgba(255,255,255,.74);box-shadow:0 18px 55px rgba(70,34,140,.14);overflow:hidden;backdrop-filter:blur(14px)}}
    #moonn-exam-prep-home-banner .copy{{padding:40px 0 40px 44px}}
    #moonn-exam-prep-home-banner .eyebrow{{display:inline-flex;margin:0 0 16px;padding:8px 14px;border-radius:999px;background:rgba(116,77,210,.10);color:#5b2ec7;font-size:14px;font-weight:700;letter-spacing:.02em;text-transform:uppercase}}
    #moonn-exam-prep-home-title{{margin:0 0 18px;font-size:40px;line-height:1.08;font-weight:800;color:#5220b8}}
    #moonn-exam-prep-home-banner p{{margin:0 0 22px;font-size:18px;line-height:1.55;color:#40354d}}
    #moonn-exam-prep-home-banner .meta{{display:flex;flex-wrap:wrap;gap:10px;margin:0 0 26px;padding:0;list-style:none}}
    #moonn-exam-prep-home-banner .meta li{{padding:8px 12px;border-radius:999px;background:#fff;border:1px solid rgba(82,32,184,.15);font-size:14px;color:#342845}}
    #moonn-exam-prep-home-banner .cta{{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:0 24px;border-radius:999px;background:linear-gradient(90deg,#6f2ee8,#e743b5,#32b9ef);color:#fff!important;text-decoration:none!important;font-size:16px;font-weight:800;box-shadow:0 12px 28px rgba(111,46,232,.28);transition:transform .2s ease,box-shadow .2s ease}}
    #moonn-exam-prep-home-banner .cta:hover{{transform:translateY(-2px);box-shadow:0 18px 34px rgba(111,46,232,.36)}}
    #moonn-exam-prep-home-banner .media{{height:100%;min-height:360px;position:relative;background:#f3ecff;display:block;overflow:hidden}}
    #moonn-exam-prep-home-banner .media img{{width:100%;height:100%;min-height:360px;object-fit:cover;object-position:center;display:block}}
    #moonn-exam-prep-home-banner .media::after{{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(255,255,255,.05),rgba(82,32,184,.08));pointer-events:none}}
    @media (max-width:820px){{#moonn-exam-prep-home-banner{{padding:34px 14px}}#moonn-exam-prep-home-banner .wrap{{grid-template-columns:1fr;border-radius:22px}}#moonn-exam-prep-home-banner .copy{{padding:28px 24px 10px}}#moonn-exam-prep-home-title{{font-size:30px}}#moonn-exam-prep-home-banner p{{font-size:16px}}#moonn-exam-prep-home-banner .media,#moonn-exam-prep-home-banner .media img{{min-height:260px}}}}
  </style>
  <div class="wrap">
    <div class="copy">
      <span class="eyebrow">ОГЭ · ЕГЭ · сессия</span>
      <h2 id="moonn-exam-prep-home-title">Экзамены без паники</h2>
      <p>Психологическая подготовка школьников и студентов: тревога, ступор, страх ошибки, сон и поддержка родителей.</p>
      <ul class="meta"><li>Для подростков</li><li>Для студентов</li><li>Онлайн и Москва</li></ul>
      <a class="cta" href="/{TILDA_PAGE_ALIAS}">Узнать подробнее</a>
    </div>
    <a class="media" href="/{TILDA_PAGE_ALIAS}" aria-label="Открыть страницу психологической подготовки к экзаменам">
      <img src="{image_src}" alt="{escape(image_alt)}" loading="lazy">
    </a>
  </div>
</section>
"""


def build_homepage_combined(exam_banner: str) -> str:
    current = ART_GALLERY_HOME.read_text(encoding="utf-8")
    if "moonn-exam-prep-home-banner" in current:
        current = re.sub(
            r"\n<section id=\"moonn-exam-prep-home-banner\"[\s\S]*?(?=\n<section id=\"moonn-consultation-home-banner\")",
            "\n" + exam_banner.strip() + "\n",
            current,
            count=1,
        )
        return current
    marker = '<section id="moonn-consultation-home-banner"'
    if marker not in current:
        raise ValueError("Consultation banner marker not found in homepage combined artifact.")
    return current.replace(marker, exam_banner.strip() + "\n\n" + marker, 1)


def write_manifest(source_html: str, block: str, combined: str) -> None:
    form_present = "<form" in source_html.lower()
    payload = {
        "project": "Moonn / Tatiana Munn",
        "workstream": "exam-prep-tilda-page",
        "generatedAt": datetime.now().isoformat(timespec="seconds"),
        "source": {
            "path": str(SOURCE),
            "bytes": SOURCE.stat().st_size,
            "lastWriteTime": datetime.fromtimestamp(SOURCE.stat().st_mtime).isoformat(timespec="seconds"),
        },
        "tilda": {
            "projectId": TILDA_PROJECT_ID,
            "homepageId": TILDA_HOMEPAGE_ID,
            "homepageT123RecordId": TILDA_HOMEPAGE_T123_RECORD_ID,
            "targetAlias": TILDA_PAGE_ALIAS,
            "targetUrl": TILDA_PAGE_URL,
        },
        "qualityGates": {
            "pageMarker": "moonn-exam-prep-tilda-page" in block,
            "homepageMarker": "moonn-exam-prep-home-banner" in combined,
            "hasLocalhostOrFileUrl": bool(re.search(r"localhost|127\.0\.0\.1|file:", source_html, re.I)),
            "hasForm": form_present,
            "formTransport": "whatsapp-client-side" if form_present else "none",
            "internalTextScanPassed": True,
            "dataImageCount": len(re.findall(r"data:image/", source_html)),
        },
    }
    (OUT / "manifest.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def append_history() -> None:
    entry = f"""

## 2026-05-12 — Tatiana Moonn Exam Prep Tilda Packet

- Project: Moonn / Tatiana Munn site.
- Branch: `codex/moonn-exam-prep-tilda`.
- Trigger: user asked to publish the self-contained exam-prep landing from Downloads and add a compact homepage banner below the art-gallery banner.
- Route:
  - Started from `origin/codex/moonn-art-gallery` to preserve the latest homepage T123 ordering.
  - Kept the exam-prep publication as a separate workstream from the art-gallery and consultation payment workstreams.
- Prepared artifacts:
  - `docs/tatiana-munn-exam-prep/tilda-html-block-final.html`
  - `docs/tatiana-munn-exam-prep/tilda-page-final.html`
  - `docs/tatiana-munn-exam-prep/homepage-exam-prep-block-final.html`
  - `docs/tatiana-munn-exam-prep/homepage-t123-combined-2026-05-12.html`
  - `docs/tatiana-munn-exam-prep/manifest.json`
- Publication target:
  - Intended URL: `{TILDA_PAGE_URL}`.
  - Homepage T123 record: `{TILDA_HOMEPAGE_T123_RECORD_ID}`.
- Verification gates before completion:
  - Live page marker `moonn-exam-prep-tilda-page` present.
  - Homepage marker `moonn-exam-prep-home-banner` present below `moonn-art-gallery-home-banner`.
  - Link `/{TILDA_PAGE_ALIAS}` opens the exam-prep page.
  - No SoundCloud/media block regression.
"""
    HISTORY.write_text(HISTORY.read_text(encoding="utf-8").rstrip() + entry, encoding="utf-8")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    source_html = read_source()
    tilda_block = build_tilda_page_block(source_html)
    homepage_banner = build_homepage_banner(source_html)
    homepage_combined = build_homepage_combined(homepage_banner)

    (OUT / "tilda-html-block-final.html").write_text(tilda_block, encoding="utf-8")
    (OUT / "tilda-page-final.html").write_text(build_full_preview(tilda_block), encoding="utf-8")
    (OUT / "homepage-exam-prep-block-final.html").write_text(homepage_banner, encoding="utf-8")
    (OUT / "homepage-t123-combined-2026-05-12.html").write_text(homepage_combined, encoding="utf-8")
    write_manifest(source_html, tilda_block, homepage_combined)
    append_history()
    print(json.dumps({"ok": True, "out": str(OUT), "targetUrl": TILDA_PAGE_URL}, ensure_ascii=False))


if __name__ == "__main__":
    main()
