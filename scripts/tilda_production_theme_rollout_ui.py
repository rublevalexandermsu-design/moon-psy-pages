import argparse
import json
import time
from pathlib import Path

import pyperclip
from pywinauto import Desktop
from pywinauto.keyboard import send_keys


ROOT = Path(__file__).resolve().parents[1]
ROLLOUT = ROOT / "registry" / "tilda" / "moonn-production-73-rollout.json"
SNIPPET = ROOT / "output" / "moonn-radiant-production-snippet.html"


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


def navigate(window, url: str, wait_seconds: float = 5.0) -> None:
    window.set_focus()
    edits = window.descendants(control_type="Edit")
    if not edits:
        raise RuntimeError("Chrome address bar edit control not found")
    address = edits[0]
    address.set_focus()
    address.set_edit_text(url)
    send_keys("{ENTER}")
    time.sleep(wait_seconds)


def editor_control(window):
    edits = window.descendants(control_type="Edit")
    candidates = []
    for edit in edits:
        rect = edit.rectangle()
        if rect.top > 300 and rect.left < 140:
            candidates.append((max(0, rect.width()) * max(0, rect.height()), len(edit.window_text()), edit))
    if not candidates:
        raise RuntimeError("Tilda HEAD code editor control not found")
    return sorted(candidates, key=lambda item: (item[0], item[1]), reverse=True)[0][2]


def click_button(window, label: str, wait_seconds: float = 2.0) -> None:
    for button in window.descendants(control_type="Button"):
        if button.window_text() == label:
            button.click_input()
            time.sleep(wait_seconds)
            return
    raise RuntimeError(f"Button not found: {label}")


def normalize_existing(value: str) -> str:
    value = value.replace("\ufeff", "").strip()
    return "" if not value else value


def copy_editor_text() -> str:
    send_keys("^a")
    time.sleep(0.2)
    send_keys("^c")
    time.sleep(0.3)
    return pyperclip.paste()


def remove_existing_theme(existing: str) -> str:
    start = "<!-- moonn-radiant-sanctuary-theme:start -->"
    end = "<!-- moonn-radiant-sanctuary-theme:end -->"
    if start not in existing or end not in existing:
        return existing
    before, rest = existing.split(start, 1)
    _, after = rest.split(end, 1)
    return f"{before.rstrip()}\n{after.lstrip()}".strip()


def apply_head_snippet(window, page_id: str, project_id: str, snippet: str) -> dict:
    edit_url = f"https://tilda.ru/projects/editheadcode/?projectid={project_id}&pageid={page_id}"
    navigate(window, edit_url, wait_seconds=5.5)
    editor = editor_control(window)
    editor.click_input()
    time.sleep(0.2)
    existing = normalize_existing(copy_editor_text())
    already_present = "moonn-radiant-sanctuary-theme" in existing and "moonn-seo-aeo-enhancer.js" in existing
    if already_present:
        return {"page_id": page_id, "status": "already_present"}
    cleaned = remove_existing_theme(existing)
    next_value = f"{cleaned}\n\n{snippet}".strip() if cleaned else snippet.strip()
    editor.set_focus()
    pyperclip.copy(next_value)
    send_keys("^a")
    time.sleep(0.2)
    send_keys("^v")
    time.sleep(0.7)
    saved_text = copy_editor_text()
    if "moonn-radiant-sanctuary-theme" not in saved_text or "moonn-seo-aeo-enhancer.js" not in saved_text:
        raise RuntimeError(f"Snippet did not appear in editor for page {page_id}")
    click_button(window, "Сохранить", wait_seconds=2.5)
    return {"page_id": page_id, "status": "saved_head"}


def publish_page(window, page_id: str, project_id: str) -> None:
    page_url = f"https://tilda.ru/page/?pageid={page_id}&projectid={project_id}"
    navigate(window, page_url, wait_seconds=7.0)
    click_button(window, "Опубликовать", wait_seconds=5.0)


def main() -> int:
    parser = argparse.ArgumentParser(description="Apply the verified Moonn theme snippet to production Tilda pages through authenticated Chrome UI.")
    parser.add_argument("--project-id", default="8326812")
    parser.add_argument("--limit", type=int, default=3)
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--out", default="output/tilda-production-theme-rollout-ui.json")
    parser.add_argument("--rollout", default=str(ROLLOUT.relative_to(ROOT)))
    args = parser.parse_args()

    pages = json.loads((ROOT / args.rollout).read_text(encoding="utf-8"))
    selected = pages[args.offset : args.offset + args.limit]
    snippet = SNIPPET.read_text(encoding="utf-8-sig")
    window = chrome_window()
    results = []
    for page in selected:
        page_id = str(page["source_page_id"])
        item = {
            "alias": page["alias"],
            "page_id": page_id,
            "production_url": page["production_url"],
        }
        try:
            item.update(apply_head_snippet(window, page_id, args.project_id, snippet))
            publish_page(window, page_id, args.project_id)
            item["published"] = True
        except Exception as exc:
            item["status"] = "error"
            item["error"] = str(exc)
        results.append(item)
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"out": args.out, "processed": len(results), "errors": sum(1 for item in results if item.get("status") == "error")}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
