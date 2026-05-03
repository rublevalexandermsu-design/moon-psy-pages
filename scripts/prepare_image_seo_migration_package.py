import argparse
import csv
import hashlib
import json
import mimetypes
import shutil
import sys
import time
from http.client import IncompleteRead
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_AUDIT = ROOT / "registry" / "seo" / "moonn-production-83-image-seo-audit.json"
DEFAULT_OUT = ROOT / "output" / "moonn-image-seo-migration"

SKIP_FILENAMES = {
    "tildacopy.png",
}


def canonical_tilda_image_url(url: str) -> str:
    parsed = urlparse(url)
    if parsed.netloc.lower() != "thb.tildacdn.com":
        return url
    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) >= 4 and parts[1] == "-":
        return f"https://static.tildacdn.com/{parts[0]}/{parts[-1]}"
    return url


def safe_alias(alias: str) -> str:
    value = alias.strip("/") if alias else "home"
    value = value.replace("/", "__")
    if len(value) > 48:
        digest = hashlib.sha1(value.encode("utf-8")).hexdigest()[:8]
        value = f"{value[:39].rstrip('_-')}-{digest}"
    return value or "home"


def safe_filename(filename: str, image_id: str, max_stem: int = 82) -> str:
    path = Path(filename)
    suffix = path.suffix or ".jpg"
    stem = path.stem
    if len(stem) > max_stem:
        stem = stem[:max_stem].rstrip("-")
    if image_id not in stem:
        stem = f"{stem}-{image_id}"
    return f"{stem}{suffix}"


def is_content_candidate(image: dict) -> bool:
    filename = (image.get("current_filename") or "").lower()
    if filename in SKIP_FILENAMES:
        return False
    src = image.get("src") or ""
    if "/img/tildacopy.png" in src:
        return False
    if not image.get("needs_filename_reupload"):
        return False
    return True


def download(url: str, out: Path, timeout: int = 45, retries: int = 3) -> dict:
    out.parent.mkdir(parents=True, exist_ok=True)
    last_error = None
    for attempt in range(1, retries + 1):
        try:
            req = Request(url, headers={"User-Agent": "Mozilla/5.0 MoonnImageSeoMigration/1.0"})
            with urlopen(req, timeout=timeout) as response:
                data = response.read()
                content_type = response.headers.get("Content-Type", "")
            break
        except (IncompleteRead, HTTPError, URLError, TimeoutError, OSError) as exc:
            last_error = exc
            if out.exists():
                out.unlink()
            if attempt == retries:
                raise
            time.sleep(0.8 * attempt)
    else:
        raise RuntimeError(str(last_error))
    out.write_bytes(data)
    return {
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "content_type": content_type or mimetypes.guess_type(str(out))[0] or "",
    }


def load_audit(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_csv(path: Path, rows: list[dict]) -> None:
    fields = [
        "status",
        "page_url",
        "alias",
        "source_page_id",
        "kind",
        "original_src",
        "download_url",
        "current_filename",
        "seo_filename",
        "local_file",
        "alt",
        "title",
        "bytes",
        "sha256",
        "content_type",
        "error",
    ]
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="Download Moonn image assets into SEO-named local migration package.")
    parser.add_argument("--audit", default=str(DEFAULT_AUDIT.relative_to(ROOT)))
    parser.add_argument("--out", default=str(DEFAULT_OUT.relative_to(ROOT)))
    parser.add_argument("--limit", type=int, default=0, help="Optional limit for smoke tests.")
    parser.add_argument("--sleep", type=float, default=0.04, help="Small delay between downloads.")
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()

    audit = load_audit(ROOT / args.audit)
    out_root = ROOT / args.out
    files_root = out_root / "files_by_page"
    cache_root = out_root / "_download_cache"
    out_root.mkdir(parents=True, exist_ok=True)

    rows = []
    seen_targets = set()
    processed = 0
    for page in audit.get("pages", []):
        page_dir = files_root / safe_alias(page.get("alias") or "")
        for image in page.get("images", []):
            if not is_content_candidate(image):
                continue
            processed += 1
            if args.limit and processed > args.limit:
                break
            original_src = image["src"]
            download_url = canonical_tilda_image_url(original_src)
            seo_filename = safe_filename(image["proposed_filename"], image["image_id"])
            target = page_dir / seo_filename
            if target in seen_targets:
                stem = target.stem
                suffix = target.suffix
                target = target.with_name(f"{stem}-{image['image_id']}{suffix}")
            seen_targets.add(target)
            cache_key = hashlib.sha1(download_url.encode("utf-8")).hexdigest()[:16] + target.suffix
            cache_file = cache_root / cache_key
            rows.append({
                "status": "pending",
                "page_url": page["url"],
                "alias": page.get("alias") or "",
                "source_page_id": page.get("source_page_id") or "",
                "kind": image.get("kind") or "",
                "original_src": original_src,
                "download_url": download_url,
                "current_filename": image.get("current_filename") or "",
                "seo_filename": target.name,
                "local_file": str(target.relative_to(out_root)),
                "alt": image.get("proposed_alt") or "",
                "title": image.get("proposed_title") or "",
                "bytes": "",
                "sha256": "",
                "content_type": "",
                "error": "",
                "_cache_file": str(cache_file),
                "_target": str(target),
            })
        if args.limit and processed > args.limit:
            break

    def materialize(row: dict) -> dict:
        cache_file = Path(row.pop("_cache_file"))
        target = Path(row.pop("_target"))
        try:
            if not cache_file.exists():
                meta = download(row["download_url"], cache_file)
                if args.sleep:
                    time.sleep(args.sleep)
            else:
                data = cache_file.read_bytes()
                meta = {
                    "bytes": len(data),
                    "sha256": hashlib.sha256(data).hexdigest(),
                    "content_type": mimetypes.guess_type(str(cache_file))[0] or "",
                }
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(cache_file, target)
            row.update(
                {
                    "status": "downloaded",
                    "bytes": meta["bytes"],
                    "sha256": meta["sha256"],
                    "content_type": meta["content_type"],
                }
            )
        except (HTTPError, URLError, TimeoutError, OSError) as exc:
            row.update({"status": "error", "error": str(exc)})
        return row

    completed = []
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        future_map = {executor.submit(materialize, row): row for row in rows}
        for future in as_completed(future_map):
            completed.append(future.result())
    rows = sorted(completed, key=lambda row: (row["page_url"], row["seo_filename"], row["original_src"]))

    summary = {
        "generated_at": "2026-05-03",
        "audit": str((ROOT / args.audit).relative_to(ROOT)),
        "out": str(out_root.relative_to(ROOT)),
        "candidate_count": len(rows),
        "downloaded_count": sum(1 for row in rows if row["status"] == "downloaded"),
        "error_count": sum(1 for row in rows if row["status"] == "error"),
        "total_bytes": sum(int(row["bytes"] or 0) for row in rows),
        "note": "Files are local migration artifacts and are intentionally stored under output/, which is ignored by Git.",
    }
    (out_root / "manifest.json").write_text(json.dumps({"summary": summary, "items": rows}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_csv(out_root / "manifest.csv", rows)
    (out_root / "README.md").write_text(
        "# Moonn Image SEO Migration Package\n\n"
        "This folder contains local SEO-named copies of Tilda image assets.\n\n"
        "Use `manifest.csv` as the replacement checklist in Tilda:\n\n"
        "1. Open the target page/block.\n"
        "2. Upload the file from `files_by_page/<alias>/...`.\n"
        "3. Set the image alt/title from the manifest where Tilda exposes those fields.\n"
        "4. Publish the page.\n"
        "5. Re-run `scripts/seo_image_audit_production.py` and compare filename/alt status.\n\n"
        "Do not commit this folder: it is a local migration artifact and may contain large media files.\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False))
    return 0 if summary["error_count"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
