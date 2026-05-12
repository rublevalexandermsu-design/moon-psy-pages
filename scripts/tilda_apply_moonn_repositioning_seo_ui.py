from __future__ import annotations

import argparse
import json
import time
import urllib.request
from pathlib import Path

import pyautogui
import pyperclip
from pywinauto import Desktop
from pywinauto.keyboard import send_keys


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ID = "8326812"
REGISTER_PATH = ROOT / "docs" / "moonn-seo-repositioning-2026-05-12" / "url-decision-register.json"
REPORT_PATH = ROOT / "docs" / "moonn-seo-repositioning-2026-05-12" / "tilda-seo-ui-live-apply-report.json"


def address_bar(window):
    for attempt in range(2):
        for edit in window.descendants(control_type="Edit"):
            try:
                if edit.element_info.automation_id == "view_1012":
                    return edit
            except Exception:
                continue
        edits = window.descendants(control_type="Edit")
        if edits:
            return edits[0]
        if attempt == 0:
            window.set_focus()
            pyautogui.press("f12")
            time.sleep(1.0)
    raise RuntimeError("Chrome address bar edit control not found")


def chrome_window():
    candidates = []
    for window in Desktop(backend="uia").windows(title_re=".*(Google Chrome|Chromium|Chromium-Gost).*"):
        try:
            address = address_bar(window).window_text()
        except Exception:
            address = ""
        candidates.append((window, address))
    for window, address in candidates:
        title = window.window_text()
        if "tilda.ru" in address and ("Tilda" in title or "Moonn" in title):
            window.restore()
            window.set_focus()
            return window
    if candidates:
        window, _ = candidates[0]
        window.restore()
        window.set_focus()
        return window
    raise RuntimeError("No Google Chrome window found")


def navigate(window, url: str, wait_seconds: float = 5.0) -> None:
    window.restore()
    window.set_focus()
    bar = address_bar(window)
    bar.set_focus()
    bar.set_edit_text(url)
    send_keys("{ENTER}")
    time.sleep(wait_seconds)


def ensure_project_page(window) -> None:
    current = address_bar(window).window_text()
    if "tilda.ru" not in current or f"projectid={PROJECT_ID}" not in current:
        if "tilda.ru" not in current:
            pyautogui.hotkey("ctrl", "t")
            time.sleep(0.4)
        navigate(window, f"https://tilda.ru/projects/?projectid={PROJECT_ID}", wait_seconds=7.0)


def open_devtools_console(window) -> None:
    window.set_focus()
    has_console = any((tab.window_text() or "") in {"Консоль", "Console"} for tab in window.descendants(control_type="TabItem"))
    if not has_console:
        pyautogui.hotkey("ctrl", "shift", "j")
        time.sleep(2.5)
    for tab in window.descendants(control_type="TabItem"):
        if (tab.window_text() or "") in {"Консоль", "Console"}:
            tab.click_input()
            time.sleep(0.4)
            break


def close_devtools(window) -> None:
    has_console = any((tab.window_text() or "") in {"Консоль", "Console"} for tab in window.descendants(control_type="TabItem"))
    if has_console:
        pyautogui.press("f12")
        time.sleep(1.2)


def run_console(window, code: str, wait_seconds: float = 2.0) -> None:
    open_devtools_console(window)
    rect = window.rectangle()
    pyautogui.click(rect.right - 450, rect.top + 450)
    time.sleep(0.1)
    pyperclip.copy(code)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.2)
    pyautogui.press("enter")
    time.sleep(wait_seconds)


def clipboard_json(window, expression: str, wait_seconds: float = 1.0):
    run_console(window, f"copy(JSON.stringify({expression}))", wait_seconds=wait_seconds)
    return json.loads(pyperclip.paste())


def tilda_save_page_settings(window, row: dict[str, object], noindex: bool) -> dict[str, object]:
    page_id = str(row["page_id"])
    payload = {
        "pageId": page_id,
        "title": "" if noindex else row["title"],
        "description": "" if noindex else row["description"],
        "canonical": "" if noindex else row["canonical_target"],
        "nosearch": bool(noindex),
        "nofollow": bool(noindex),
    }
    code = """
(async function(payload) {
try {
  function wait(ms) { return new Promise(resolve => setTimeout(resolve, ms)); }
  async function waitField(selector, label) {
    const deadline = Date.now() + 7000;
    while (Date.now() < deadline) {
      const field = document.querySelector(selector);
      if (field) return field;
      await wait(250);
    }
    throw new Error(`missing field ${label}`);
  }
  function setField(name, value) {
    const field = document.querySelector(`input[name="${name}"], textarea[name="${name}"]`);
    if (!field) throw new Error(`missing field ${name}`);
    field.value = value || '';
    field.dispatchEvent(new Event('input', { bubbles: true }));
    field.dispatchEvent(new Event('change', { bubbles: true }));
  }
  function setChecked(name, checked) {
    const field = document.querySelector(`input[name="${name}"]`);
    if (!field) throw new Error(`missing checkbox ${name}`);
    field.checked = !!checked;
    field.dispatchEvent(new Event('change', { bubbles: true }));
  }
  if (typeof td__showform__EditPageSettings !== 'function') {
    throw new Error('td__showform__EditPageSettings is not available on this Tilda screen');
  }
  td__showform__EditPageSettings(String(payload.pageId));
  await wait(1400);
  const seoTab = Array.from(document.querySelectorAll('a,button,div')).find(el => (el.textContent || '').trim() === 'SEO');
  if (seoTab) seoTab.click();
  await wait(1200);
  await waitField('input[name="meta_title"]', 'meta_title');
  const before = {
    meta_title: document.querySelector('input[name="meta_title"]')?.value || '',
    meta_descr: document.querySelector('input[name="meta_descr"], textarea[name="meta_descr"]')?.value || '',
    link_canonical: document.querySelector('input[name="link_canonical"]')?.value || '',
    nosearch: !!document.querySelector('input[name="nosearch"]')?.checked,
    meta_nofollow: !!document.querySelector('input[name="meta_nofollow"]')?.checked
  };
  setField('meta_title', payload.title);
  setField('meta_descr', payload.description);
  setField('link_canonical', payload.canonical);
  setChecked('nosearch', payload.nosearch);
  setChecked('meta_nofollow', payload.nofollow);
  const submit = Array.from(document.querySelectorAll('input[type="submit"],button')).find(el => /Сохранить изменения|Save changes/i.test(el.value || el.textContent || ''));
  if (!submit) throw new Error('save button not found');
  submit.click();
  await wait(2600);
  window.__MOONN_REPOSITIONING_SEO_SAVE__ = {
    pageId: payload.pageId,
    before,
    after: {
      meta_title: payload.title,
      meta_descr: payload.description,
      link_canonical: payload.canonical,
      nosearch: payload.nosearch,
      meta_nofollow: payload.nofollow
    }
  };
  document.title = 'MOONN_SEO_UI_SAVED_' + payload.pageId;
} catch (error) {
  window.__MOONN_REPOSITIONING_SEO_SAVE__ = {
    pageId: payload.pageId,
    error: String(error && error.message ? error.message : error)
  };
  document.title = 'MOONN_SEO_UI_ERROR_' + payload.pageId;
}
})(__PAYLOAD__);
""".replace("__PAYLOAD__", json.dumps(payload, ensure_ascii=False))
    run_console(window, code, wait_seconds=3.0)
    deadline = time.time() + 15
    while time.time() < deadline:
        title = window.window_text()
        if f"MOONN_SEO_UI_SAVED_{page_id}" in title or f"MOONN_SEO_UI_ERROR_{page_id}" in title:
            result = clipboard_json(window, "window.__MOONN_REPOSITIONING_SEO_SAVE__ || null")
            if result and result.get("error"):
                raise RuntimeError(f"Tilda SEO UI error for page {page_id}: {result['error']}")
            return result
        time.sleep(0.5)
    raise RuntimeError(f"SEO UI save confirmation missing for page {page_id}")


def find_button(window, name: str, min_left: int = 0, max_top: int = 1000):
    matches = []
    for button in window.descendants(control_type="Button"):
        try:
            text = button.window_text() or ""
            rect = button.rectangle()
        except Exception:
            continue
        if name in text and rect.left >= min_left and rect.top <= max_top:
            matches.append(button)
    if not matches:
        return None
    return sorted(matches, key=lambda item: (item.rectangle().top, item.rectangle().left))[0]


def close_publish_popup(window) -> None:
    for _ in range(4):
        button = find_button(window, "Закрыть", min_left=650, max_top=600) or find_button(window, "Close", min_left=650, max_top=600)
        if button:
            button.click_input()
            time.sleep(0.8)
            return
        time.sleep(0.5)


def publish_page(window, row: dict[str, object]) -> bool:
    close_devtools(window)
    navigate(window, f"https://tilda.ru/page/?pageid={row['page_id']}&projectid={PROJECT_ID}", wait_seconds=6.0)
    button = find_button(window, "Опубликовать", min_left=700, max_top=360) or find_button(window, "Publish", min_left=700, max_top=360)
    if not button:
        return False
    button.click_input()
    time.sleep(7.0)
    close_publish_popup(window)
    return True


def load_rows(paths: list[str], include_noindex: bool, only_action: str) -> list[dict[str, object]]:
    rows = json.loads(REGISTER_PATH.read_text(encoding="utf-8"))["pages"]
    if paths:
        wanted = set(paths)
        rows = [row for row in rows if row["path"] in wanted]
    elif only_action:
        rows = [row for row in rows if row["action"] == only_action]
    else:
        allowed = {"rewrite", "keep_indexed", "noindex"} if include_noindex else {"rewrite", "keep_indexed"}
        rows = [row for row in rows if row["action"] in allowed]
    return rows


def fetch_live(url: str) -> dict[str, object]:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 MoonnSEOApplyVerifier/1.0"})
    with urllib.request.urlopen(req, timeout=25) as response:
        html = response.read().decode(response.headers.get_content_charset() or "utf-8", errors="replace")
    return {
        "status": response.status,
        "titlePresent": "<title>" in html.lower(),
        "canonicalPresent": 'rel="canonical"' in html.lower() or "rel='canonical'" in html.lower(),
        "robotsNoindexPresent": "noindex" in html.lower(),
        "h1Count": html.lower().count("<h1"),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Apply Moonn repositioning SEO settings through authenticated Tilda UI.")
    parser.add_argument("--paths", nargs="*", default=[])
    parser.add_argument("--include-noindex", action="store_true")
    parser.add_argument("--only-action", choices=["rewrite", "keep_indexed", "noindex"], default="")
    parser.add_argument("--publish", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    rows = load_rows(args.paths, args.include_noindex, args.only_action)
    if args.limit:
        rows = rows[: args.limit]
    if not rows:
        raise RuntimeError("No rows selected")

    window = chrome_window()
    ensure_project_page(window)

    if REPORT_PATH.exists():
        report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    else:
        report = {"createdDate": "2026-05-12", "projectId": PROJECT_ID, "sourceRegister": str(REGISTER_PATH.relative_to(ROOT)), "results": []}

    for row in rows:
        result = {
            "url": row["url"],
            "path": row["path"],
            "pageId": row["page_id"],
            "action": row["action"],
            "cluster": row["cluster"],
            "publishRequested": args.publish,
        }
        try:
            ensure_project_page(window)
            noindex = row["action"] == "noindex"
            result["settingsSave"] = tilda_save_page_settings(window, row, noindex=noindex)
            if args.publish:
                result["published"] = publish_page(window, row)
            if args.publish:
                result["liveAfterPublish"] = fetch_live(str(row["url"]))
            result["status"] = "ok"
        except Exception as exc:  # noqa: BLE001
            result["status"] = "error"
            result["error"] = repr(exc)
        report["results"].append(result)
        REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(result, ensure_ascii=False))
        if result["status"] != "ok":
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
