"""Render a reader package for visual review with the existing local runtime."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import pypdfium2 as pdfium
from PIL import Image, ImageDraw
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]


def workspace_path(name: str) -> Path:
    path = (ROOT / name).resolve()
    if not path.is_relative_to(ROOT):
        raise ValueError("Render paths must stay in this workspace")
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", help="Package directory; defaults to package.json selection")
    parser.add_argument("--pages", default="", help="Additional page numbers for full-size inspection, comma separated")
    parser.add_argument("--output", default="tmp/pdfs/reader_package")
    args = parser.parse_args()
    cfg = json.loads((ROOT / "docs/reader_package/package.json").read_text(encoding="utf-8"))
    folder = workspace_path(args.package or cfg["output_directory"])
    manifest = json.loads((folder / "package_manifest.json").read_text(encoding="utf-8"))
    pdf = folder / "Hive_Earth_Beta_Reader_Package.pdf"
    pdf_hash = hashlib.sha256(pdf.read_bytes()).hexdigest()
    if pdf_hash != manifest["pdf_sha256"]:
        raise ValueError("PDF differs from the recorded package manifest")
    out = workspace_path(args.output)
    doc = pdfium.PdfDocument(str(pdf))
    selected = {1, 2, 3, len(doc)}
    selected.update(int(n) for n in args.pages.split(",") if n.strip())
    for sec in manifest["verification"]["sections"]:
        if sec["section"] in {"authors-foreword", "chapter-1", "figures", "voss-conquest", "gor"}:
            selected.add(sec["first_page"])
    # Include the current author-added transition when present.
    for i, page in enumerate(PdfReader(pdf).pages, 1):
        if "Snap. Extreme pain." in (page.extract_text() or ""):
            selected.add(i)
    if any(n < 1 or n > len(doc) for n in selected):
        raise ValueError("Requested page is outside the PDF")
    out.mkdir(parents=True, exist_ok=True)
    for n in sorted(selected):
        page = doc[n - 1]
        page.render(scale=1.6).to_pil().save(out / f"page-{n:03d}.png")
        page.close()
    sheets = []
    for batch in range(0, len(doc), 36):
        sheet = Image.new("RGB", (1116, 1770), "#dddddd")
        draw = ImageDraw.Draw(sheet)
        for offset in range(min(36, len(doc) - batch)):
            n = batch + offset
            page = doc[n]
            image = page.render(scale=.43).to_pil()
            page.close()
            image.thumbnail((174, 262))
            x = (offset % 6) * 186 + 6
            y = (offset // 6) * 295 + 23
            sheet.paste(image, (x, y))
            draw.text((x, y - 17), f"Page {n + 1}", fill="black")
        name = f"contact-{batch // 36 + 1:02d}.png"
        sheet.save(out / name)
        sheets.append(name)
    review = {"pdf_sha256": pdf_hash, "pages": len(doc), "full_size_pages": sorted(selected),
              "contact_sheets": sheets, "visual_review": "pending human/agent inspection"}
    (out / "render_manifest.json").write_text(json.dumps(review, indent=2) + "\n", encoding="utf-8", newline="")
    print(json.dumps(review))


if __name__ == "__main__":
    main()
