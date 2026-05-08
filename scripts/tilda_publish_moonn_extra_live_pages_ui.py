import json
import time
from pathlib import Path

from pywinauto import Desktop
from pywinauto.keyboard import send_keys


PROJECT_ID = "8326812"
ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "docs" / "moonn-extra-live-pages-publish-report-2026-05-07.json"


def address_bar(win):
    for edit in win.descendants(control_type="Edit"):
        try:
            if edit.element_info.automation_id == "view_1012":
                return edit
        except Exception:
            continue
    edits = win.descendants(control_type="Edit")
    if edits:
        return edits[0]
    raise RuntimeError("Chrome address bar edit control not found")


def chrome_window():
    candidates = []
    for window in Desktop(backend="uia").windows(title_re=".*Google Chrome.*"):
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
            time.sleep(0.5)
            return window
    for window, address in candidates:
        if "tilda.ru" in address:
            window.restore()
            window.set_focus()
            time.sleep(0.5)
            return window
    raise RuntimeError("Authenticated Google Chrome Tilda window not found")


def find_button(win, name, predicate):
    matches = []
    for button in win.descendants(control_type="Button"):
        try:
            text = button.window_text() or ""
            rect = button.rectangle()
        except Exception:
            continue
        if name in text and predicate(rect):
            matches.append(button)
    if not matches:
        return None
    return sorted(matches, key=lambda item: (item.rectangle().top, item.rectangle().left))[0]


def navigate_to_page(win, page_id):
    bar = address_bar(win)
    bar.set_focus()
    bar.set_edit_text(f"https://tilda.ru/page/?pageid={page_id}&projectid={PROJECT_ID}")
    send_keys("{ENTER}")
    time.sleep(5.0)


def close_publish_popup(win):
    close_button = find_button(
        win,
        "Закрыть",
        lambda rect: 900 < rect.left < 1600 and 150 < rect.top < 550,
    )
    if close_button:
        close_button.click_input()
        time.sleep(0.8)
        return True
    return False


def publish_current_page(win):
    for _ in range(4):
        button = find_button(
            win,
            "Опубликовать",
            lambda rect: rect.left > 850 and rect.top < 260,
        )
        if button:
            button.click_input()
            time.sleep(6.0)
            close_publish_popup(win)
            return True
        time.sleep(1.0)
    return False


def main():
    report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    win = chrome_window()
    for item in report["pages"]:
        print(f"publish extra {item['index']} pageid={item['pageId']} {item['url']}")
        try:
            navigate_to_page(win, item["pageId"])
            item["status"] = "published" if publish_current_page(win) else "failed"
            if item["status"] == "failed":
                item["error"] = "publish_button_not_found"
        except Exception as error:
            item["status"] = "failed"
            item["error"] = repr(error)
        print(json.dumps(item, ensure_ascii=False))
        REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        if item["status"] != "published":
            break


if __name__ == "__main__":
    main()
