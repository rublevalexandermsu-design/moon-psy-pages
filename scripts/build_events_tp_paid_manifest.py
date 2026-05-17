import json
import re
from html import unescape
from pathlib import Path
from urllib.request import Request, urlopen

import qrcode


AUDIT_PATH = Path("registry/products/paid-video-lectures-audit-2026-05-03.json")
MANIFEST_PATH = Path("registry/products/paid-video-lectures.manifest.json")
QR_PATH = Path("assets/qr/tatyana-munn-paid-lectures-events-tp-qr.png")
STORE_URL = "https://moonn.ru/events_tp"
STORE_PAGE_ID = "66814657"


def clean_title(raw: str) -> str:
    title = raw.replace("/ События на TimePad.ru", "")
    title = re.sub(r"\s+", " ", title)
    return unescape(title).strip()


def fetch_timepad_title(event_id: str) -> str:
    url = f"https://moonn.timepad.ru/event/{event_id}/"
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    html = urlopen(request, timeout=20).read().decode("utf-8", "ignore")
    match = re.search(r'<meta property="og:title" content="([^"]+)"', html)
    if not match:
        match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    if not match:
        return f"Timepad event {event_id}"
    return clean_title(match.group(1))


def extract_event_ids() -> list[str]:
    audit = json.loads(AUDIT_PATH.read_text(encoding="utf-8"))
    events_tp = next(item for item in audit["candidates"] if item.get("alias") == "events_tp")
    event_ids: set[str] = set()
    for link in events_tp.get("timepad_links", []):
        event_ids.update(re.findall(r"/event/(\d+)/", link))
    return sorted(event_ids, key=int)


def make_lecture(event_id: str) -> dict:
    title = fetch_timepad_title(event_id)
    slug_title = re.sub(r"[^a-z0-9]+", "-", f"timepad-{event_id}".lower()).strip("-")
    return {
        "lecture_id": slug_title,
        "title": title,
        "price_rub": 1300,
        "source_page_url": STORE_URL,
        "source_tilda_page_id": STORE_PAGE_ID,
        "timepad_event_id": event_id,
        "timepad_source_url": f"https://moonn.timepad.ru/event/{event_id}/",
        "video_source_url": None,
        "tilda_product_sku": f"moonn-video-lecture-{event_id}",
        "tilda_member_group": f"moonn-video-lecture-{event_id}",
        "protected_watch_page_url": None,
        "qr_image_file": QR_PATH.as_posix(),
        "qr_target_url": STORE_URL,
        "status": "needs_video",
        "required_user_input": [
            "matching video URL",
            "confirm whether this Timepad event should be sold as a recording",
        ],
        "notes": "Generated from the live events_tp Timepad link list. Product/access records are planned, not yet created in Tilda.",
    }


def write_qr() -> None:
    QR_PATH.parent.mkdir(parents=True, exist_ok=True)
    image = qrcode.make(STORE_URL)
    image.save(QR_PATH)


def main() -> int:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    manifest["updated_at"] = "2026-05-03"
    manifest["canonical_store_page"] = {
        "url": STORE_URL,
        "tilda_page_id": STORE_PAGE_ID,
        "alias": "events_tp",
        "role": "storefront",
    }
    manifest["access_model"]["payment_receiver"] = "Tilda cart ST100 + configured T-Bank/Tinkoff or existing project payment provider after visual verification"
    manifest["access_model"]["delivery_rule"] = "For one pilot, sell access to a protected Members/Courses page after successful payment; then scale to one group per lecture or one recordings library group."
    manifest["lectures"] = [make_lecture(event_id) for event_id in extract_event_ids()]
    MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_qr()
    print(json.dumps({"lectures": len(manifest["lectures"]), "qr": QR_PATH.as_posix()}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
