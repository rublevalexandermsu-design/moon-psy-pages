from __future__ import annotations

import json
from datetime import date, datetime
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "moonn-timepad-registration-bridge.json"
OUT = ROOT / "docs" / "moonn-timepad-registration-bridge"
HISTORY = ROOT / "docs" / "codex-chat-history.md"

TILDA_PROJECT_ID = "8326812"
TILDA_TARGET_ALIAS = "timepad-registration"
TILDA_TARGET_URL = "https://moonn.ru/timepad-registration"

MONTHS_RU = {
    1: "января",
    2: "февраля",
    3: "марта",
    4: "апреля",
    5: "мая",
    6: "июня",
    7: "июля",
    8: "августа",
    9: "сентября",
    10: "октября",
    11: "ноября",
    12: "декабря",
}

WEEKDAYS_RU = {
    0: "понедельник",
    1: "вторник",
    2: "среда",
    3: "четверг",
    4: "пятница",
    5: "суббота",
    6: "воскресенье",
}


def load_manifest() -> dict:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    required_root = ["canonical_url", "timepad_master_event_id", "lectures"]
    missing = [field for field in required_root if field not in data]
    if missing:
        raise ValueError(f"Bridge manifest misses required fields: {missing}")
    if not data["lectures"]:
        raise ValueError("Bridge manifest has no lectures")
    for lecture in data["lectures"]:
        for field in ("lecture_no", "date", "time", "title", "recurring_event_id", "poster_url"):
            if field not in lecture:
                raise ValueError(f"Lecture {lecture!r} misses {field}")
    return data


def ru_date(value: str) -> str:
    parsed = date.fromisoformat(value)
    return f"{parsed.day} {MONTHS_RU[parsed.month]} 2026, {WEEKDAYS_RU[parsed.weekday()]}"


def build_block(data: dict) -> str:
    lectures = sorted(data["lectures"], key=lambda item: item["lecture_no"])
    default = lectures[0]
    lectures_json = json.dumps(
        {
            str(item["lecture_no"]): {
                "lectureNo": item["lecture_no"],
                "title": item["title"],
                "date": item["date"],
                "dateLabel": ru_date(item["date"]),
                "time": item["time"],
                "recurringEvent": item["recurring_event_id"],
                "posterUrl": item["poster_url"],
            }
            for item in lectures
        },
        ensure_ascii=False,
        separators=(",", ":"),
    )
    fallback_cards = "\n".join(
        f"""<a class="tm-bridge-card" href="?lecture={lecture['lecture_no']}">
          <img src="{escape(lecture['poster_url'])}" alt="{escape(lecture['title'])}" loading="lazy">
          <span>Лекция {lecture['lecture_no']}/13</span>
          <strong>{escape(lecture['title'])}</strong>
          <em>{escape(ru_date(lecture['date']))}, {escape(lecture['time'])}</em>
        </a>"""
        for lecture in lectures
    )
    return f"""<section id="moonn-timepad-registration-bridge" class="tm-bridge" aria-label="Регистрация на лекцию Татьяны Мунн">
  <style>
    #moonn-timepad-registration-bridge{{font-family:Inter,Arial,sans-serif;color:#1d1725;background:linear-gradient(135deg,#fff 0%,#f6efff 46%,#eef8ff 100%);padding:34px 18px 54px;min-height:100vh}}
    #moonn-timepad-registration-bridge *{{box-sizing:border-box}}
    #moonn-timepad-registration-bridge .tm-bridge-wrap{{max-width:1040px;margin:0 auto}}
    #moonn-timepad-registration-bridge .tm-bridge-hero{{display:grid;grid-template-columns:minmax(0,1fr) minmax(260px,380px);gap:26px;align-items:center;background:rgba(255,255,255,.82);border:1px solid rgba(91,50,156,.18);border-radius:26px;box-shadow:0 18px 48px rgba(82,32,184,.14);overflow:hidden}}
    #moonn-timepad-registration-bridge .tm-bridge-copy{{padding:34px 34px 32px}}
    #moonn-timepad-registration-bridge .tm-bridge-kicker{{display:inline-flex;margin:0 0 14px;padding:7px 12px;border-radius:999px;background:rgba(82,32,184,.10);color:#5520b8;font-size:13px;font-weight:800;text-transform:uppercase}}
    #moonn-timepad-registration-bridge h1{{margin:0 0 14px;font-size:clamp(32px,5vw,54px);line-height:1.05;color:#5220b8;font-weight:900;letter-spacing:0}}
    #moonn-timepad-registration-bridge .tm-bridge-lead{{margin:0 0 20px;font-size:18px;line-height:1.55;color:#40354d}}
    #moonn-timepad-registration-bridge .tm-bridge-meta{{display:flex;flex-wrap:wrap;gap:9px;margin:0;padding:0;list-style:none}}
    #moonn-timepad-registration-bridge .tm-bridge-meta li{{padding:8px 11px;border-radius:999px;background:#fff;border:1px solid rgba(82,32,184,.14);font-size:14px;color:#342845}}
    #moonn-timepad-registration-bridge .tm-bridge-poster{{height:100%;min-height:290px;background:linear-gradient(135deg,#f5edff,#eef8ff);overflow:hidden;display:grid;place-items:center;padding:14px}}
    #moonn-timepad-registration-bridge .tm-bridge-poster img{{width:100%;height:100%;object-fit:contain;display:block;border-radius:16px}}
    #moonn-timepad-registration-bridge .tm-bridge-widget{{margin:26px auto 0;background:#fff;border:1px solid rgba(91,50,156,.16);border-radius:22px;padding:18px;box-shadow:0 12px 36px rgba(82,32,184,.10)}}
    #moonn-timepad-registration-bridge .tm-bridge-fallback{{margin:26px 0 0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}}
    #moonn-timepad-registration-bridge .tm-bridge-card{{display:grid;grid-template-columns:118px 1fr;gap:14px;align-items:center;padding:12px;border:1px solid rgba(91,50,156,.14);border-radius:18px;background:rgba(255,255,255,.78);color:#1d1725;text-decoration:none}}
    #moonn-timepad-registration-bridge .tm-bridge-card img{{grid-row:1/4;width:118px;aspect-ratio:16/10;object-fit:contain;border-radius:12px;background:#f7f0ff}}
    #moonn-timepad-registration-bridge .tm-bridge-card span{{font-size:12px;font-weight:800;color:#6a2fca}}
    #moonn-timepad-registration-bridge .tm-bridge-card strong{{font-size:16px;line-height:1.2;color:#241331}}
    #moonn-timepad-registration-bridge .tm-bridge-card em{{font-style:normal;font-size:13px;color:#5e5368}}
    #moonn-timepad-registration-bridge .tm-bridge-note{{margin:16px 0 0;font-size:14px;line-height:1.45;color:#6c6075}}
    @media(max-width:760px){{#moonn-timepad-registration-bridge{{padding:20px 12px 38px}}#moonn-timepad-registration-bridge .tm-bridge-hero{{grid-template-columns:1fr;border-radius:20px}}#moonn-timepad-registration-bridge .tm-bridge-copy{{padding:24px 20px 4px}}#moonn-timepad-registration-bridge .tm-bridge-poster{{min-height:210px}}#moonn-timepad-registration-bridge .tm-bridge-fallback{{grid-template-columns:1fr}}#moonn-timepad-registration-bridge .tm-bridge-card{{grid-template-columns:96px 1fr}}#moonn-timepad-registration-bridge .tm-bridge-card img{{width:96px}}}}
  </style>
  <script>
    (function() {{
      var robots = document.querySelector('meta[name="robots"]');
      if (!robots) {{
        robots = document.createElement('meta');
        robots.name = 'robots';
        document.head.appendChild(robots);
      }}
      robots.content = 'noindex,follow';
    }})();
  </script>
  <div class="tm-bridge-wrap">
    <div class="tm-bridge-hero">
      <div class="tm-bridge-copy">
        <p class="tm-bridge-kicker">Бесплатная лекция · {escape(data["age_limit"])}</p>
        <h1 id="tm-bridge-title">{escape(default["title"])}</h1>
        <p class="tm-bridge-lead" id="tm-bridge-date">{escape(ru_date(default["date"]))}, {escape(default["time"])}. Форма ниже уже открыта на выбранную дату.</p>
        <ul class="tm-bridge-meta">
          <li>{escape(data["venue"])}</li>
          <li>{escape(data["address"])}</li>
          <li>Психолог Татьяна Мунн</li>
        </ul>
      </div>
      <div class="tm-bridge-poster">
        <img id="tm-bridge-poster" src="{escape(default["poster_url"])}" alt="{escape(default["title"])}">
      </div>
    </div>
    <div class="tm-bridge-widget" id="tm-bridge-widget">
      <script async defer charset="UTF-8" src="https://timepad.ru/js/tpwf/loader/min/loader.js?v=355" data-timepad-widget-v2="event_register">
        (function() {{
          var lectures = {lectures_json};
          var params = new URLSearchParams(window.location.search);
          var key = params.get('lecture') || params.get('l') || '{default["lecture_no"]}';
          var item = lectures[key] || lectures['{default["lecture_no"]}'];
          window.__MOONN_TIMEPAD_BRIDGE_SELECTED__ = item;
          return {{
            event: {{ id: {int(data["timepad_master_event_id"])} }},
            prefill: {{ recurringEvent: item.recurringEvent }}
          }};
        }})();
      </script>
    </div>
    <p class="tm-bridge-note">Если форма не открылась автоматически, выберите нужную тему ниже.</p>
    <div class="tm-bridge-fallback" id="tm-bridge-fallback">
      {fallback_cards}
    </div>
  </div>
  <script>
    (function() {{
      var lectures = {lectures_json};
      var params = new URLSearchParams(window.location.search);
      var key = params.get('lecture') || params.get('l') || '{default["lecture_no"]}';
      var item = lectures[key] || lectures['{default["lecture_no"]}'];
      var title = document.getElementById('tm-bridge-title');
      var date = document.getElementById('tm-bridge-date');
      var poster = document.getElementById('tm-bridge-poster');
      if (title) title.textContent = item.title;
      if (date) date.textContent = item.dateLabel + ', ' + item.time + '. Форма ниже уже открыта на выбранную дату.';
      if (poster) {{
        poster.src = item.posterUrl;
        poster.alt = item.title;
      }}
      document.title = item.title + ' — регистрация на лекцию Татьяны Мунн';
    }})();
  </script>
</section>
"""


def build_preview(block: str, data: dict) -> str:
    return f"""<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Регистрация на лекцию Татьяны Мунн</title>
  <meta name="description" content="Регистрация на выбранную дату бесплатной лекции по психологии с Татьяной Мунн.">
  <meta name="robots" content="{escape(data["robots"])}">
  <link rel="canonical" href="{escape(data["canonical_url"])}">
</head>
<body>
{block}
</body>
</html>
"""


def write_report(data: dict, block: str, preview: str) -> None:
    report = {
        "project": data["project"],
        "workstream": "moonn-timepad-registration-bridge",
        "generatedAt": datetime.now().isoformat(timespec="seconds"),
        "target": {
            "tildaProjectId": TILDA_PROJECT_ID,
            "alias": TILDA_TARGET_ALIAS,
            "url": TILDA_TARGET_URL,
            "robots": data["robots"],
        },
        "qualityGates": {
            "lectureCount": len(data["lectures"]),
            "hasTimepadWidget": "data-timepad-widget-v2" in block,
            "hasRecurringPrefill": "recurringEvent" in block,
            "hasNoindex": "noindex,follow" in preview,
            "hasInternalWords": any(
                token in block.lower()
                for token in ["mvp", "прототип", "технический", "контур", "не дубль"]
            ),
        },
    }
    (OUT / "manifest.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def append_history() -> None:
    marker = "## 2026-05-15 — Moonn Timepad Registration Bridge"
    existing = HISTORY.read_text(encoding="utf-8") if HISTORY.exists() else ""
    if marker in existing:
        return
    entry = f"""

{marker}

- Project: Moonn / Tatyana Munn site.
- Branch: `codex/moonn-timepad-registration-bridge`.
- Trigger: user asked to move the Timepad direct-registration helper from `school.miiiips.ru` to the canonical `moonn.ru` domain.
- Decision:
  - Use one noindex Tilda page with query parameter `?lecture=N` instead of seven duplicate public pages.
  - Keep Timepad as the payment/registration processor; the Moonn page is only a UX bridge to the selected recurring session.
- Prepared artifacts:
  - `data/moonn-timepad-registration-bridge.json`
  - `scripts/build_moonn_timepad_registration_bridge.py`
  - `docs/moonn-timepad-registration-bridge/tilda-html-block-final.html`
  - `docs/moonn-timepad-registration-bridge/tilda-page-final.html`
  - `docs/moonn-timepad-registration-bridge/manifest.json`
- Publication target:
  - `https://moonn.ru/timepad-registration?lecture=7`
- Verification gate:
  - Local and live browser checks must confirm that the selected Timepad registration form opens directly, not the recurring date list.
"""
    HISTORY.write_text(existing.rstrip() + entry, encoding="utf-8")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    data = load_manifest()
    block = build_block(data)
    preview = build_preview(block, data)
    (OUT / "tilda-html-block-final.html").write_text(block, encoding="utf-8")
    (OUT / "tilda-page-final.html").write_text(preview, encoding="utf-8")
    write_report(data, block, preview)
    append_history()
    print(json.dumps({"ok": True, "targetUrl": TILDA_TARGET_URL, "out": str(OUT)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
