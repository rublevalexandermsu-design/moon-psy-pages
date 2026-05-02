import argparse
import json
import re
import time
from pathlib import Path

import pyperclip
from pywinauto import Desktop
from pywinauto.keyboard import send_keys


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_MANIFEST = ROOT / "registry" / "seo" / "moonn-production-73-schema-snippets.json"


def chrome_window():
    candidates = []
    for window in Desktop(backend="uia").windows():
        title = window.window_text()
        if title.endswith(" - Google Chrome") and "0.0.0.5" not in title and "about:blank" not in title:
            candidates.append(window)
    if not candidates:
        raise RuntimeError("No authenticated regular Chrome window found")
    for window in candidates:
        if "Tilda" in window.window_text():
            return window
    return candidates[0]


def navigate(window, url: str, wait_seconds: float = 6.0) -> None:
    window.set_focus()
    address = window.descendants(control_type="Edit")[0]
    address.set_focus()
    address.set_edit_text(url)
    time.sleep(0.2)
    send_keys("{ENTER}")
    time.sleep(wait_seconds)


def click_control(window, control_type: str, text: str, wait_seconds: float = 2.0, top_limit: int | None = None) -> None:
    matches = []
    for control in window.descendants(control_type=control_type):
        if control.window_text() == text:
            if top_limit is None or control.rectangle().top < top_limit:
                matches.append(control)
    if not matches:
        raise RuntimeError(f"{control_type} not found: {text}")
    matches[0].click_input()
    time.sleep(wait_seconds)


def copy_focused_text() -> str:
    send_keys("^a")
    time.sleep(0.2)
    send_keys("^c")
    time.sleep(0.3)
    return pyperclip.paste()


def paste_text(value: str) -> str:
    pyperclip.copy(value)
    send_keys("^a")
    time.sleep(0.2)
    send_keys("^v")
    time.sleep(0.8)
    send_keys("{END}")
    time.sleep(0.1)
    send_keys(" ")
    time.sleep(0.1)
    send_keys("{BACKSPACE}")
    time.sleep(0.3)
    return copy_focused_text()


def remove_old_schema(existing: str) -> str:
    pattern = re.compile(
        r"\n?\s*<!-- moonn-seo-schema:\d+:start -->.*?<!-- moonn-seo-schema:\d+:end -->",
        re.DOTALL,
    )
    return pattern.sub("", existing.replace("\ufeff", "").strip()).strip()


def page_head_editor(window):
    candidates = []
    for edit in window.descendants(control_type="Edit"):
        rect = edit.rectangle()
        if 650 < rect.top < 900 and rect.left > 350 and rect.right > 850:
            candidates.append((rect.width() * rect.height(), edit))
    if not candidates:
        raise RuntimeError("Page-specific HEAD editor not found")
    return sorted(candidates, key=lambda item: item[0], reverse=True)[0][1]


def open_page_head_settings(window, page_id: str, project_id: str) -> None:
    navigate(window, "about:blank", wait_seconds=1.5)
    navigate(window, f"https://tilda.ru/page/?pageid={page_id}&projectid={project_id}", wait_seconds=7.0)
    click_control(window, "Button", "Настройки", wait_seconds=3.0, top_limit=220)
    click_control(window, "Hyperlink", "Дополнительно", wait_seconds=2.5)
    send_keys("{PGDN 4}")
    time.sleep(1.5)
    click_control(window, "Hyperlink", "Редактировать код", wait_seconds=2.0)


def apply_page_schema(window, page: dict, project_id: str) -> dict:
    page_id = str(page["source_page_id"])
    open_page_head_settings(window, page_id, project_id)
    editor = page_head_editor(window)
    editor.click_input()
    time.sleep(0.2)
    existing = copy_focused_text()
    cleaned = remove_old_schema(existing)
    next_value = f"{cleaned}\n\n{page['snippet']}".strip() if cleaned else page["snippet"].strip()
    saved_text = paste_text(next_value)
    if page["marker"] not in saved_text or "application/ld+json" not in saved_text:
        raise RuntimeError(f"Schema did not appear in page-specific HEAD editor for page {page_id}")
    click_control(window, "Button", "Сохранить изменения", wait_seconds=3.5)
    return {"page_id": page_id, "status": "saved_page_head"}


def publish_page(window, page_id: str, project_id: str) -> None:
    navigate(window, f"https://tilda.ru/page/?pageid={page_id}&projectid={project_id}", wait_seconds=7.0)
    click_control(window, "Button", "Опубликовать", wait_seconds=5.5, top_limit=220)


def main() -> int:
    parser = argparse.ArgumentParser(description="Apply page-specific Moonn JSON-LD schema through Tilda page settings.")
    parser.add_argument("--project-id", default="8326812")
    parser.add_argument("--limit", type=int, default=3)
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--out", default="output/tilda-production-page-schema-rollout-ui.json")
    args = parser.parse_args()

    manifest = json.loads(SCHEMA_MANIFEST.read_text(encoding="utf-8"))
    selected = manifest["snippets"][args.offset : args.offset + args.limit]
    window = chrome_window()
    results = []
    for page in selected:
        page_id = str(page["source_page_id"])
        item = {
            "alias": page["alias"],
            "page_id": page_id,
            "production_url": page["url"],
            "cluster": page["cluster"],
        }
        try:
            item.update(apply_page_schema(window, page, args.project_id))
            publish_page(window, page_id, args.project_id)
            item["published"] = True
        except Exception as exc:
            item["status"] = "error"
            item["error"] = str(exc)
        results.append(item)
        out = ROOT / args.out
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"out": args.out, "processed": len(results), "errors": sum(1 for item in results if item.get("status") == "error")}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
