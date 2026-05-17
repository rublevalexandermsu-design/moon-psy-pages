import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "registry/products/paid-video-lectures.manifest.json"
CATALOG_CSV_PATH = ROOT / "registry/products/paid-video-lectures-tilda-catalog-2026-05-17.csv"

UPDATED_AT = "2026-05-17"
SINGLE_PRICE_RUB = 2000
BUNDLE_PRICE_RUB = 5000
BUNDLE_SELECTION_COUNT = 5
STORE_URL = "https://moonn.ru/events_tp"
SUPPORT_PHONE = "+7-977-777-03-03"


def clean_public_title(title: str) -> str:
    replacements = [
        (" - вход свободный", ""),
        ("БЕСПЛАТНЫЕ ", ""),
        ("бесплатные ", ""),
    ]
    result = title
    for source, target in replacements:
        result = result.replace(source, target)
    return " ".join(result.split())


def product_description(title: str) -> str:
    return f"Запись лекции Татьяны Мунн: {clean_public_title(title)}"


def product_text(title: str) -> str:
    return (
        f"Доступ к записи лекции «{clean_public_title(title)}» после успешной оплаты. "
        "Видео открывается в закрытом разделе сайта. "
        f"Если возник вопрос по доступу, напишите Татьяне Мунн в Telegram или WhatsApp: {SUPPORT_PHONE}."
    )


def bundle_text() -> str:
    return (
        f"Пакет из {BUNDLE_SELECTION_COUNT} записей лекций Татьяны Мунн на выбор. "
        "После оплаты доступ выдается через закрытый раздел сайта; выбранные записи фиксируются в заявке покупателя. "
        f"Если возник вопрос по доступу, напишите Татьяне Мунн в Telegram или WhatsApp: {SUPPORT_PHONE}."
    )


def eligible_for_bundle(lecture: dict) -> bool:
    return lecture.get("video_match_status") != "not_single_recording_series_event"


def update_manifest() -> dict:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    manifest["updated_at"] = UPDATED_AT
    manifest["default_price_rub"] = SINGLE_PRICE_RUB
    manifest["bundle_price_rub"] = BUNDLE_PRICE_RUB
    manifest["bundle_selection_count"] = BUNDLE_SELECTION_COUNT
    manifest.setdefault("access_model", {})
    manifest["access_model"]["payment_receiver"] = (
        "Tilda catalog/cart with the existing configured payment provider after visual verification"
    )
    manifest["access_model"]["delivery_rule"] = (
        "Single lecture purchase grants access to the matching protected Tilda Members/Courses watch page after successful payment."
    )
    manifest["access_model"]["bundle_delivery_rule"] = (
        "Bundle purchase grants access to a protected selection flow for five lecture recordings; the final five selected recordings must be written to the order/access registry."
    )
    manifest["access_model"]["video_protection_rule"] = (
        "Do not send raw YouTube links as fulfillment. Embed selected videos only inside protected Tilda Members/Courses pages. YouTube unlisted links are not copy protection."
    )
    manifest["support"] = {
        "telegram_url": None,
        "whatsapp_phone": SUPPORT_PHONE,
        "public_support_text": "Если возник вопрос по доступу к записи, напишите Татьяне Мунн в Telegram или WhatsApp.",
    }

    for lecture in manifest["lectures"]:
        lecture["price_rub"] = SINGLE_PRICE_RUB
        lecture["tilda_product_sku"] = f"moonn-video-lecture-{lecture['timepad_event_id']}"
        lecture["tilda_member_group"] = f"moonn-video-lecture-{lecture['timepad_event_id']}"
        lecture.setdefault("required_user_input", [])
        for item in [
            "final protected watch page URL",
            "Tilda catalog product creation and visual checkout test",
        ]:
            if item not in lecture["required_user_input"]:
                lecture["required_user_input"].append(item)

    eligible_ids = [lecture["lecture_id"] for lecture in manifest["lectures"] if eligible_for_bundle(lecture)]
    manifest["bundle_products"] = [
        {
            "bundle_id": "moonn-video-bundle-5-choice",
            "title": "Пакет из 5 записей лекций Татьяны Мунн на выбор",
            "price_rub": BUNDLE_PRICE_RUB,
            "selection_count": BUNDLE_SELECTION_COUNT,
            "tilda_product_sku": "moonn-video-bundle-5-choice",
            "tilda_member_group": "moonn-video-bundle-5-choice",
            "eligible_lecture_ids": eligible_ids,
            "status": "draft_pending_video_delivery",
            "notes": (
                "Create as a separate Tilda catalog product. Buyer selects five recordings after payment "
                "through a protected account page or order-linked form; do not rely on five independent cart items."
            ),
        }
    ]

    MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest


def write_tilda_catalog_csv(manifest: dict) -> None:
    rows = []
    for lecture in manifest["lectures"]:
        rows.append(
            {
                "Brand": "Татьяна Мунн",
                "SKU": lecture["tilda_product_sku"],
                "Category": "Записи лекций",
                "Title": clean_public_title(lecture["title"]),
                "Description": product_description(lecture["title"]),
                "Text": product_text(lecture["title"]),
                "Price": str(SINGLE_PRICE_RUB),
                "Quantity": "",
                "External ID": lecture["tilda_product_sku"],
                "URL": STORE_URL,
                "Button": "Получить запись",
            }
        )

    bundle = manifest["bundle_products"][0]
    rows.append(
        {
            "Brand": "Татьяна Мунн",
            "SKU": bundle["tilda_product_sku"],
            "Category": "Пакеты записей",
            "Title": bundle["title"],
            "Description": f"{BUNDLE_SELECTION_COUNT} записей лекций на выбор за {BUNDLE_PRICE_RUB} ₽",
            "Text": bundle_text(),
            "Price": str(BUNDLE_PRICE_RUB),
            "Quantity": "",
            "External ID": bundle["tilda_product_sku"],
            "URL": STORE_URL,
            "Button": "Выбрать пакет",
        }
    )

    CATALOG_CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    with CATALOG_CSV_PATH.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), delimiter=";")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    manifest = update_manifest()
    write_tilda_catalog_csv(manifest)
    print(
        json.dumps(
            {
                "manifest": str(MANIFEST_PATH.relative_to(ROOT)),
                "catalog_csv": str(CATALOG_CSV_PATH.relative_to(ROOT)),
                "single_price_rub": SINGLE_PRICE_RUB,
                "bundle_price_rub": BUNDLE_PRICE_RUB,
                "bundle_selection_count": BUNDLE_SELECTION_COUNT,
                "lectures": len(manifest["lectures"]),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
