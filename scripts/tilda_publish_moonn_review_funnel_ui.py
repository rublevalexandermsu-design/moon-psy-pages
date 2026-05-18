from __future__ import annotations

import argparse
import base64
import time
import urllib.request
from pathlib import Path

from pywinauto import Desktop
from pywinauto.keyboard import send_keys


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ID = "8326812"
PAGE_ID = "81167556"
RECORD_ID = "1353112591"
COMBINED_PATH = ROOT / "docs" / "tatiana-munn-review-funnel" / "otzivi-t123-combined-final.html"
LIVE_URL = "https://moonn.ru/otzivi"
MARKER = "moonn-review-funnel"
BACKEND_MARKER = "AKfycbx62eyhvrBVb3rt21le1iHfUrvJwhdcAJoAht_Chu0AL_PZjIR6I3r1FxKvI7pr-tz8"
YCLIENTS_MARKER = "w461584.yclients.com/widgetJS"


def address_bar(window):
    for edit in window.descendants(control_type="Edit"):
        try:
            if edit.element_info.automation_id == "view_1012":
                return edit
        except Exception:
            continue
    edits = window.descendants(control_type="Edit")
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
        candidates.append((window, address, window.window_text()))

    for window, address, title in candidates:
        if "tilda.ru/page/" in address or "Tilda" in title or "tilda.ru/projects" in address:
            window.restore()
            window.set_focus()
            return window

    if candidates:
        window = candidates[0][0]
        window.restore()
        window.set_focus()
        return window

    raise RuntimeError(f"Authenticated Tilda Chrome window not found: {[(a, t) for _, a, t in candidates]}")


def run_javascript_url(window, code: str, expected_prefix: str, timeout: float = 8.0) -> str:
    bar = address_bar(window)
    bar.set_focus()
    bar.set_edit_text(f"javascript:{code};void 0")
    send_keys("{ENTER}")

    deadline = time.time() + timeout
    while time.time() < deadline:
        title = window.window_text()
        if title.startswith(expected_prefix):
            return title
        time.sleep(0.25)
    return window.window_text()


def navigate_to_editor(window) -> None:
    bar = address_bar(window)
    bar.set_focus()
    bar.set_edit_text(f"https://tilda.ru/page/?pageid={PAGE_ID}&projectid={PROJECT_ID}#rec{RECORD_ID}")
    send_keys("{ENTER}")
    time.sleep(5)


def save_record_code(window, html: str) -> str:
    payload = base64.b64encode(html.encode("utf-8")).decode("ascii")
    reset_title = run_javascript_url(
        window,
        "(()=>{window.__MOONN_CODE_B64='';document.title='CHUNK_RESET_0'})()",
        "CHUNK_RESET_",
    )
    if not reset_title.startswith("CHUNK_RESET_"):
        raise RuntimeError(f"Could not reset page buffer: {reset_title}")

    chunk_size = 4000
    for index, start in enumerate(range(0, len(payload), chunk_size), 1):
        part = payload[start : start + chunk_size]
        title = run_javascript_url(
            window,
            f"(()=>{{window.__MOONN_CODE_B64=(window.__MOONN_CODE_B64||'')+'{part}';"
            f"document.title='CHUNK_{index}_{start + len(part)}'}})()",
            f"CHUNK_{index}_",
        )
        if not title.startswith(f"CHUNK_{index}_"):
            raise RuntimeError(f"Could not load chunk {index}: {title}")

    save_code = (
        "(async()=>{try{"
        "const b64=window.__MOONN_CODE_B64||'';"
        "const bin=atob(b64);"
        "const arr=new Uint8Array(bin.length);"
        "for(let i=0;i<bin.length;i++)arr[i]=bin.charCodeAt(i);"
        "const code=new TextDecoder().decode(arr);"
        "const body={comm:'saverecord',pageid:window.pageid,"
        "recordid:'"
        + RECORD_ID
        + "',onlythisfield:'code',code:code};"
        "const r=window.tp__fetch"
        "?await tp__fetch({url:'/page/submit/',body:body,explanation:'saving Moonn review funnel',timeout:90})"
        ":await fetch('/page/submit/',{method:'POST',credentials:'same-origin',headers:{'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'},body:new URLSearchParams(body)}).then(x=>x.text());"
        "if(r===''||r==='OK'){if(window.tp__updateRecord){await tp__updateRecord('"
        + RECORD_ID
        + "')};document.title='SAVE_OK_'+code.length}else{document.title='SAVE_BAD_'+String(r).slice(0,80)}}"
        "catch(e){document.title='SAVE_ERR_'+e.name+'_'+String(e.message).slice(0,100)}})()"
    )
    return run_javascript_url(window, save_code, "SAVE_", timeout=140)


def publish_page(window) -> str:
    publish_code = (
        "(async()=>{try{document.title='PUBLISH_START';"
        "const r=tp__pagePublish();if(r&&r.then){await r};document.title='PUBLISH_CALLED'}"
        "catch(e){document.title='PUBLISH_ERR_'+e.name+'_'+String(e.message).slice(0,80)}})()"
    )
    return run_javascript_url(window, publish_code, "PUBLISH_", timeout=60)


def live_contains_markers() -> bool:
    url = f"{LIVE_URL}?review-funnel-check={int(time.time())}"
    request = urllib.request.Request(url, headers={"Cache-Control": "no-cache", "Pragma": "no-cache"})
    with urllib.request.urlopen(request, timeout=30) as response:
        html = response.read().decode("utf-8", errors="replace")
    return MARKER in html and BACKEND_MARKER in html and YCLIENTS_MARKER in html


def main() -> int:
    parser = argparse.ArgumentParser(description="Save and publish Moonn /otzivi review funnel through an authenticated Tilda Chrome tab.")
    parser.add_argument("--skip-publish", action="store_true", help="Save the T123 code field but do not publish the page.")
    args = parser.parse_args()

    html = COMBINED_PATH.read_text(encoding="utf-8")
    for marker in (MARKER, BACKEND_MARKER, YCLIENTS_MARKER):
        if marker not in html:
            raise RuntimeError(f"Combined /otzivi T123 HTML is missing marker: {marker}")

    window = chrome_window()
    navigate_to_editor(window)
    save_title = save_record_code(window, html)
    print(save_title)
    if not save_title.startswith("SAVE_OK_"):
        raise RuntimeError(f"Tilda save failed: {save_title}")

    if not args.skip_publish:
        publish_title = publish_page(window)
        print(publish_title)
        if not publish_title.startswith("PUBLISH_CALLED"):
            raise RuntimeError(f"Tilda publish was not confirmed: {publish_title}")
        if not live_contains_markers():
            raise RuntimeError("Live /otzivi does not contain review funnel markers after publish.")
        print("LIVE_OK")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
