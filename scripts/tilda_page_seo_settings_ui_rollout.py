import argparse
import json
import time
from pathlib import Path

import pyautogui
import pyperclip
from pywinauto import Desktop
from pywinauto.keyboard import send_keys


ROOT = Path(__file__).resolve().parents[1]
PACKETS = ROOT / "docs" / "moonn-production-seo-strengthening-packets-2026-05-04.json"


def chrome_window():
    candidates = []
    for window in Desktop(backend="uia").windows(title_re=".*Google Chrome.*"):
        try:
            address = next(
                edit.window_text()
                for edit in window.descendants(control_type="Edit")
                if edit.element_info.automation_id == "view_1012"
            )
        except Exception:
            address = ""
        candidates.append((window, address))
    for window, address in candidates:
        title = window.window_text()
        if "tilda.ru" in address and ("Moonn.ru" in title or "Tilda" in title or "ACE_LEN" in title):
            window.restore()
            window.set_focus()
            return window
    for window, address in candidates:
        if "tilda.ru" in address:
            window.restore()
            window.set_focus()
            return window
    raise RuntimeError("No authenticated Google Chrome Tilda window found")


def address_bar(window):
    for edit in window.descendants(control_type="Edit"):
        if edit.element_info.automation_id == "view_1012":
            return edit
    edits = window.descendants(control_type="Edit")
    if edits:
        return edits[0]
    raise RuntimeError("Chrome address bar edit control not found")


def navigate(window, url, wait_seconds=5.0):
    window.restore()
    window.set_focus()
    bar = address_bar(window)
    bar.set_focus()
    bar.set_edit_text(url)
    send_keys("{ENTER}")
    time.sleep(wait_seconds)


def ensure_project_page(window, project_id):
    current = address_bar(window).window_text()
    if f"projectid={project_id}" not in current or "/projects/" not in current:
        navigate(window, f"https://tilda.ru/projects/?projectid={project_id}", wait_seconds=6.0)


def open_devtools_console(window):
    window.set_focus()
    has_console = any((tab.window_text() or "") == "Консоль" for tab in window.descendants(control_type="TabItem"))
    if not has_console:
        pyautogui.press("f12")
        time.sleep(2.5)
    for tab in window.descendants(control_type="TabItem"):
        if (tab.window_text() or "") == "Консоль":
            tab.click_input()
            time.sleep(0.4)
            break


def close_devtools(window):
    has_console = any((tab.window_text() or "") == "Консоль" for tab in window.descendants(control_type="TabItem"))
    if has_console:
        pyautogui.press("f12")
        time.sleep(1.2)


def console_input(window):
    for edit in window.descendants(control_type="Edit"):
        rect = edit.rectangle()
        if rect.left > 850 and rect.top > 330 and rect.width() > 500:
            return edit
    raise RuntimeError("Chrome DevTools console input not found")


def run_console(window, code, wait_seconds=2.0):
    open_devtools_console(window)
    edit = console_input(window)
    edit.set_focus()
    edit.set_edit_text(code)
    time.sleep(0.2)
    edit.type_keys("{ENTER}")
    time.sleep(wait_seconds)


def clipboard_json(window, expression, wait_seconds=1.0):
    run_console(window, f"copy(JSON.stringify({expression}))", wait_seconds=wait_seconds)
    raw = pyperclip.paste()
    return json.loads(raw)


def set_page_seo(window, page):
    page_id = str(page["sourcePageId"])
    seo = page["seo"]
    title = seo["title"]
    description = seo["description"]
    canonical = seo["canonical"]
    payload = {
        "pageId": page_id,
        "title": title,
        "description": description,
        "canonical": canonical,
    }
    code = """
(async function(payload) {
  function wait(ms) { return new Promise(resolve => setTimeout(resolve, ms)); }
  function setField(name, value) {
    const field = document.querySelector(`input[name="${name}"]`);
    if (!field) throw new Error(`missing field ${name}`);
    field.value = value || '';
    field.dispatchEvent(new Event('input', { bubbles: true }));
    field.dispatchEvent(new Event('change', { bubbles: true }));
  }
  function setChecked(name, checked) {
    const field = document.querySelector(`input[name="${name}"]`);
    if (!field) return;
    field.checked = !!checked;
    field.dispatchEvent(new Event('change', { bubbles: true }));
  }
  td__showform__EditPageSettings(String(payload.pageId));
  await wait(1200);
  const seoTab = Array.from(document.querySelectorAll('a')).find(a => (a.textContent || '').trim() === 'SEO');
  if (seoTab) seoTab.click();
  await wait(500);
  const backup = {
    pageId: payload.pageId,
    before: {
      meta_title: document.querySelector('input[name="meta_title"]')?.value || '',
      meta_descr: document.querySelector('input[name="meta_descr"]')?.value || '',
      link_canonical: document.querySelector('input[name="link_canonical"]')?.value || '',
      nosearch: !!document.querySelector('input[name="nosearch"]')?.checked,
      meta_nofollow: !!document.querySelector('input[name="meta_nofollow"]')?.checked
    }
  };
  setField('meta_title', payload.title);
  setField('meta_descr', payload.description);
  setField('link_canonical', payload.canonical);
  setChecked('nosearch', false);
  setChecked('meta_nofollow', false);
  const submit = Array.from(document.querySelectorAll('input[type="submit"],button')).find(el => /Сохранить изменения/i.test(el.value || el.textContent || ''));
  if (!submit) throw new Error('save button not found');
  submit.click();
  await wait(2500);
  backup.after = {
    meta_title: payload.title,
    meta_descr: payload.description,
    link_canonical: payload.canonical,
    nosearch: false,
    meta_nofollow: false
  };
  window.__MOONN_LAST_SEO_SAVE__ = backup;
  document.title = 'SEO_UI_SAVED_' + payload.pageId;
})(__PAYLOAD__);
""".replace("__PAYLOAD__", json.dumps(payload, ensure_ascii=False))
    run_console(window, code, wait_seconds=2.0)
    title = window.window_text()
    deadline = time.time() + 12
    while f"SEO_UI_SAVED_{page_id}" not in title and time.time() < deadline:
        time.sleep(0.5)
        title = window.window_text()
    if f"SEO_UI_SAVED_{page_id}" not in title:
        raise RuntimeError(f"SEO settings save was not confirmed for page {page_id}: {title}")
    backup = clipboard_json(window, "window.__MOONN_LAST_SEO_SAVE__ || null")
    if not backup:
        raise RuntimeError(f"SEO settings backup missing for page {page_id}")
    return backup


def publish_page(window, project_id, page_id):
    close_devtools(window)
    navigate(window, f"https://tilda.ru/page/?pageid={page_id}&projectid={project_id}", wait_seconds=7.0)
    buttons = [button for button in window.descendants(control_type="Button") if (button.window_text() or "").strip() == "Опубликовать"]
    if not buttons:
        raise RuntimeError(f"Publish button not found for page {page_id}")
    buttons[0].click_input()
    time.sleep(6.0)


def load_pages(mode):
    data = json.loads(PACKETS.read_text(encoding="utf-8"))
    if mode == "ready":
        return data["readyToApply"]
    if mode == "after-robots":
        return data["applyAfterRobotsFix"]
    if mode == "all":
        return data["readyToApply"] + data["applyAfterRobotsFix"]
    raise ValueError(f"Unknown mode: {mode}")


def main():
    parser = argparse.ArgumentParser(description="Apply Moonn page-specific SEO settings through visible Tilda UI in authenticated Google Chrome.")
    parser.add_argument("--project-id", default="8326812")
    parser.add_argument("--mode", choices=["ready", "after-robots", "all"], default="ready")
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--limit", type=int, default=1)
    parser.add_argument("--publish", action="store_true")
    parser.add_argument("--out", default="output/tilda-page-seo-settings-ui-rollout.json")
    args = parser.parse_args()

    pages = load_pages(args.mode)
    selected = pages[args.offset : args.offset + args.limit]
    out_path = ROOT / args.out
    if out_path.exists():
        results = json.loads(out_path.read_text(encoding="utf-8"))
    else:
        results = []
    window = chrome_window()
    ensure_project_page(window, args.project_id)

    for page in selected:
        item = {
            "pageId": str(page["sourcePageId"]),
            "url": page["url"],
            "alias": page.get("alias"),
            "mode": args.mode,
            "publishRequested": args.publish,
        }
        try:
            ensure_project_page(window, args.project_id)
            item["settingsBackup"] = set_page_seo(window, page)
            if args.publish:
                publish_page(window, args.project_id, str(page["sourcePageId"]))
                item["published"] = True
            item["status"] = "saved"
        except Exception as exc:
            item["status"] = "error"
            item["error"] = str(exc)
        results.append(item)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps({
        "out": str(out_path.relative_to(ROOT)),
        "processed": len(selected),
        "errors": sum(1 for item in results[-len(selected):] if item.get("status") == "error"),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
