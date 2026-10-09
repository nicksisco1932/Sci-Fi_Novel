"""Build and verify a private beta edition from a versioned source manifest.

Usage: python beta_readers/build_beta.py {check,build,verify} manifest.json
All manifest paths are relative to the repository, never the current shell.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import subprocess
from pathlib import Path
from xml.sax.saxutils import escape

from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, Image, PageBreak, PageTemplate, Paragraph, Spacer,
)
from reportlab.platypus.tableofcontents import TableOfContents


ROOT = Path(__file__).resolve().parents[1]
CHAPTER_NUMBERS = [1, *range(4, 31)]
APPENDIX_TITLES = [
    "Figures of the Turning Time", "The Voss Conquest", "Gor of Almelah",
]
HEADER = "HIVE EARTH  |  PRIVATE BETA"
HASH_PATTERN = re.compile(r"[0-9a-f]{64}\Z")


class EditionError(ValueError):
    """A release input or verification requirement was not satisfied."""


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalized_text(data: bytes) -> str:
    """Ignore checkout BOM/newline differences, without changing prose."""
    return data.decode("utf-8-sig").replace("\r\n", "\n").replace("\r", "\n")


def text_sha256(data: bytes) -> str:
    return sha256(normalized_text(data).encode("utf-8"))


def repository_path(root: Path, value: object) -> Path:
    if not isinstance(value, str) or not value or "\\" in value:
        raise EditionError("Paths must be nonempty repository-relative POSIX paths.")
    relative = Path(value)
    if relative.is_absolute() or ":" in value or ".." in relative.parts:
        raise EditionError(f"Unsafe repository path: {value}")
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()):
        raise EditionError(f"Path escapes the repository: {value}")
    return path


def _required_text(record: dict, key: str) -> str:
    value = record.get(key)
    if not isinstance(value, str) or not value.strip():
        raise EditionError(f"Missing or empty {key}.")
    return value


def _required_hash(record: dict, key: str) -> str:
    value = _required_text(record, key)
    if not HASH_PATTERN.fullmatch(value):
        raise EditionError(f"Invalid {key}.")
    return value


def _git(root: Path, *arguments: str) -> bytes:
    result = subprocess.run(
        ["git", "-C", str(root), *arguments], capture_output=True, check=False,
    )
    if result.returncode:
        raise EditionError("Source checkpoint is unavailable or lacks a source file.")
    return result.stdout


def check_manifest(manifest_path: Path, *, root: Path = ROOT,
                   allow_output: bool = False) -> dict:
    """Validate all inputs and return their already-read content."""
    root = root.resolve()
    manifest_path = manifest_path.resolve()
    if not manifest_path.is_relative_to(root):
        raise EditionError("The edition manifest must be inside the repository.")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
    if not isinstance(manifest, dict):
        raise EditionError("The edition manifest must be a JSON object.")
    for key in ("edition_id", "title", "author", "edition_date"):
        _required_text(manifest, key)
    commit = _required_text(manifest, "source_commit")
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise EditionError("source_commit must be a full Git commit hash.")
    _git(root, "cat-file", "-e", f"{commit}^{{commit}}")
    reader_note = manifest.get("reader_note")
    if (not isinstance(reader_note, list) or not reader_note
            or any(not isinstance(item, str) or not item.strip() for item in reader_note)):
        raise EditionError("reader_note must contain nonempty paragraphs.")
    sources = manifest.get("sources")
    if not isinstance(sources, list) or len(sources) != 31:
        raise EditionError("An edition requires exactly 28 chapters and three appendices.")
    seen = set()
    texts = []
    starting_hashes = {}
    newline_differences = []
    for index, source in enumerate(sources):
        if not isinstance(source, dict):
            raise EditionError("Each source must be an object.")
        title = _required_text(source, "title")
        if index < 28:
            match = re.match(r"Chapter (\d+)\b", title)
            if (source.get("role") != "chapter" or not match
                    or int(match.group(1)) != CHAPTER_NUMBERS[index]):
                raise EditionError("Chapter order must be Chapter 1, then Chapters 4–30.")
            prefix = "docs/canonical_md/"
        else:
            if source.get("role") != "appendix" or title != APPENDIX_TITLES[index - 28]:
                raise EditionError("Appendices must be Figures, Voss Conquest, then Gor.")
            prefix = "docs/appendices/"
        relative = _required_text(source, "path")
        if not relative.startswith(prefix) or not relative.endswith(".md"):
            raise EditionError(f"Unexpected source location: {relative}")
        path = repository_path(root, relative)
        if path in seen:
            raise EditionError(f"Duplicate source: {relative}")
        seen.add(path)
        if not path.is_file():
            raise EditionError(f"Missing source: {relative}")
        data = path.read_bytes()
        raw_hash = _required_hash(source, "raw_sha256")
        expected_text_hash = _required_hash(source, "text_sha256")
        if text_sha256(data) != expected_text_hash:
            raise EditionError(f"Source text changed: {relative}")
        if sha256(data) != raw_hash:
            newline_differences.append(relative)
        committed = _git(root, "show", f"{commit}:{relative}")
        if text_sha256(committed) != expected_text_hash:
            raise EditionError(f"Source differs from checkpoint: {relative}")
        starting_hashes[relative] = sha256(data)
        texts.append(normalized_text(data))
    cover = manifest.get("cover")
    if not isinstance(cover, dict):
        raise EditionError("A cover record is required.")
    cover_path = repository_path(root, cover.get("path"))
    if not cover_path.is_file() or sha256(cover_path.read_bytes()) != _required_hash(cover, "sha256"):
        raise EditionError("Cover is missing or changed.")
    ImageReader(str(cover_path)).getSize()
    starting_hashes[cover["path"]] = cover["sha256"]
    superseded = manifest.get("superseded", [])
    if not isinstance(superseded, list):
        raise EditionError("superseded must be a list.")
    for old in superseded:
        if not isinstance(old, dict):
            raise EditionError("Invalid superseded record.")
        old_path = repository_path(root, old.get("path"))
        expected = _required_hash(old, "sha256")
        if not old_path.is_file() or sha256(old_path.read_bytes()) != expected:
            raise EditionError(f"Superseded artifact is missing or changed: {old.get('path')}")
        starting_hashes[old["path"]] = expected
    output = manifest.get("output")
    if not isinstance(output, dict):
        raise EditionError("An output record is required.")
    output_path = repository_path(root, output.get("path"))
    # Existing frozen releases remain at output/pdf/. New beta editions may use
    # the stage-specific editions/beta/ tree, without moving old release bytes.
    if (not output["path"].startswith(("output/pdf/", "editions/beta/"))
            or output_path.suffix.lower() != ".pdf"):
        raise EditionError("A beta PDF must be beneath output/pdf/ or editions/beta/.")
    sidecar_path = manifest_path.with_suffix(".verification.json")
    if not allow_output and (output_path.exists() or sidecar_path.exists()):
        raise EditionError("An edition output or verification record already exists; create a new edition.")
    return {
        "manifest": manifest, "manifest_path": manifest_path, "root": root,
        "texts": texts, "cover_path": cover_path, "output_path": output_path,
        "sidecar_path": sidecar_path, "starting_hashes": starting_hashes,
        "checkout_byte_differences": newline_differences,
    }


def visible_inline(text: str) -> str:
    """Resolve human-visible Markdown text; never normalize punctuation."""
    text = re.sub(
        r"\[\[([^\[\]]+)\]\]",
        lambda match: match[1].split("|", 1)[1] if "|" in match[1]
        else match[1].split("#")[-1], text,
    )
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"\1", text)
    return text


def inline_markup(text: str) -> str:
    text = re.sub(
        r"\[\[([^\[\]]+)\]\]",
        lambda match: match[1].split("|", 1)[1] if "|" in match[1]
        else match[1].split("#")[-1], text,
    )
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    return re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<i>\1</i>", text)


def markdown_blocks(text: str) -> list[tuple[str, str]]:
    """The manuscript's paragraphs, headings, quotations and scene breaks."""
    blocks = []
    for block in re.split(r"\n\s*\n", text.strip()):
        lines = block.splitlines()
        if re.fullmatch(r"\s*(?:-{3,}|\*\s*\*\s*\*)\s*", block):
            blocks.append(("scene", "* * *"))
        elif len(lines) == 1 and (match := re.match(r"^(#{1,6})\s+(.+)$", block)):
            blocks.append((f"heading{min(len(match[1]), 3)}", match[2]))
        elif all(line.startswith(">") for line in lines):
            blocks.append(("quote", " ".join(re.sub(r"^>\s?", "", line) for line in lines)))
        else:
            if any(line.startswith("```") or re.match(r"^\|.*\|$", line) for line in lines):
                raise EditionError("Code blocks and Markdown tables need an explicit export treatment.")
            blocks.append(("body", " ".join(lines)))
    return blocks


def register_fonts() -> None:
    font_dir = Path("C:/Windows/Fonts")
    for name, filename in (
        ("Georgia", "georgia.ttf"), ("Georgia-Bold", "georgiab.ttf"),
        ("Georgia-Italic", "georgiai.ttf"), ("Georgia-BoldItalic", "georgiaz.ttf"),
    ):
        if name not in pdfmetrics.getRegisteredFontNames():
            pdfmetrics.registerFont(TTFont(name, str(font_dir / filename)))
    pdfmetrics.registerFontFamily(
        "Georgia", normal="Georgia", bold="Georgia-Bold",
        italic="Georgia-Italic", boldItalic="Georgia-BoldItalic",
    )


def _styles() -> dict[str, ParagraphStyle]:
    base = ParagraphStyle(
        "Body", fontName="Georgia", fontSize=11, leading=15.5, spaceAfter=8,
        textColor=colors.HexColor("#222222"), allowWidows=0, allowOrphans=0,
    )
    return {
        "body": base,
        "quote": ParagraphStyle("Quote", parent=base, leftIndent=16, rightIndent=16),
        "scene": ParagraphStyle("Scene", parent=base, alignment=TA_CENTER, spaceBefore=6, spaceAfter=12, keepWithNext=True),
        "heading1": ParagraphStyle("Heading1", parent=base, fontName="Georgia-Bold", fontSize=16, leading=21, spaceBefore=8, spaceAfter=14, keepWithNext=True),
        "heading2": ParagraphStyle("Heading2", parent=base, fontName="Georgia-Bold", fontSize=13, leading=18, spaceBefore=12, spaceAfter=8, keepWithNext=True),
        "heading3": ParagraphStyle("Heading3", parent=base, fontName="Georgia-Bold", fontSize=11, leading=15.5, spaceBefore=10, spaceAfter=8, keepWithNext=True),
        "title": ParagraphStyle("BookTitle", parent=base, fontName="Georgia-Bold", fontSize=25, leading=30, alignment=TA_CENTER, spaceAfter=18),
        "subtitle": ParagraphStyle("Subtitle", parent=base, alignment=TA_CENTER, fontSize=11, leading=16, spaceAfter=5),
    }


def _draw_page(canvas, document) -> None:
    canvas.saveState()
    canvas.setFillColor(colors.HexColor("#68727A"))
    canvas.setFont("Georgia", 8)
    if document.page > 1:
        canvas.drawRightString(letter[0] - .85 * inch, letter[1] - .43 * inch, HEADER)
    canvas.drawCentredString(letter[0] / 2, .42 * inch, str(document.page))
    canvas.restoreState()


class EditionDocument(BaseDocTemplate):
    def afterFlowable(self, flowable) -> None:
        if isinstance(flowable, Paragraph) and hasattr(flowable, "section_key"):
            title = flowable.getPlainText()
            self.canv.bookmarkPage(flowable.section_key)
            self.canv.addOutlineEntry(title, flowable.section_key, level=0)
            self.notify("TOCEntry", (0, title, self.page, flowable.section_key))


def _source_paragraphs(text: str, styles: dict, width: float,
                       height: float) -> list[Paragraph]:
    blocks = markdown_blocks(text)
    paragraphs = [Paragraph(inline_markup(value) if kind != "scene" else value, styles[kind])
                  for kind, value in blocks]
    if len(paragraphs) >= 2 and all(kind in ("body", "quote") for kind, _ in blocks[-2:]):
        previous, last = paragraphs[-2:]
        _, previous_height = previous.wrap(width, height)
        _, last_height = last.wrap(width, height)
        # Keep a short closing beat with its short predecessor. Long paragraphs
        # remain independently splittable and every source paragraph stays intact.
        if last_height <= last.style.leading * 1.01 and previous_height <= previous.style.leading * 4.01:
            previous.keepWithNext = True
    return paragraphs


def pdf_bytes(context: dict) -> bytes:
    register_fonts()
    styles = _styles()
    manifest = context["manifest"]
    buffer = io.BytesIO()
    document = EditionDocument(
        buffer, pagesize=letter, leftMargin=.85 * inch, rightMargin=.85 * inch,
        topMargin=.75 * inch, bottomMargin=.75 * inch,
        title=f"{manifest['title']} — {manifest['edition_id']}",
        author=manifest["author"], subject="Private beta manuscript and three appendices",
    )
    frame = Frame(document.leftMargin, document.bottomMargin, document.width, document.height, id="book")
    document.addPageTemplates(PageTemplate(id="book", frames=frame, onPage=_draw_page))
    cover_width, cover_height = ImageReader(str(context["cover_path"])).getSize()
    scale = min(5 * inch / cover_width, 5.5 * inch / cover_height)
    cover = Image(str(context["cover_path"]), width=cover_width * scale, height=cover_height * scale)
    cover.hAlign = "CENTER"
    story = [
        Paragraph(escape(manifest["title"]), styles["title"]), cover, Spacer(1, 12),
        Paragraph(escape(manifest["author"]), styles["subtitle"]),
        Paragraph(escape(f"Private beta edition — {manifest['edition_date']}"), styles["subtitle"]),
        Paragraph(escape(manifest["edition_id"]), styles["subtitle"]), PageBreak(),
    ]
    heading = Paragraph("Reader note", styles["heading1"])
    heading.section_key = "reader-note"
    story.append(heading)
    story.extend(Paragraph(inline_markup(note), styles["body"]) for note in manifest["reader_note"])
    story.extend([PageBreak(), Paragraph("Contents", styles["heading1"])])
    toc = TableOfContents()
    toc.levelStyles = [ParagraphStyle(
        "ContentsEntry", fontName="Georgia", fontSize=9.5, leading=13,
        spaceBefore=2, leftIndent=0, rightIndent=22,
    )]
    story.append(toc)
    for index, (source, text) in enumerate(zip(manifest["sources"], context["texts"])):
        story.append(PageBreak())
        heading = Paragraph(escape(source["title"]), styles["heading1"])
        heading.section_key = f"source-{index:02d}"
        story.append(heading)
        story.extend(_source_paragraphs(text, styles, document.width, document.height))
    # A missing glyph should stop the release rather than silently become a box.
    glyphs = pdfmetrics.getFont("Georgia").face.charToGlyph
    displayed = [manifest["title"], manifest["author"], manifest["edition_id"], manifest["edition_date"]]
    displayed += [visible_inline(note) for note in manifest["reader_note"]]
    displayed += [source["title"] for source in manifest["sources"]]
    displayed += [visible_inline(value) for text in context["texts"] for _, value in markdown_blocks(text)]
    unsupported = sorted({character for value in displayed for character in value if not character.isspace() and ord(character) not in glyphs})
    if unsupported:
        raise EditionError(f"Georgia lacks required glyphs: {unsupported!r}")
    document.multiBuild(story)
    return buffer.getvalue()


def _compact(value: str) -> str:
    return " ".join(value.split())


def _page_text(page, page_number: int) -> str:
    # ReportLab draws this exact furniture before the story. Do not filter by
    # visitor coordinates: some pypdf versions misreport wrapped-line positions.
    text = page.extract_text()
    prefix = (f"{HEADER}\n" if page_number > 1 else "") + f"{page_number}\n"
    if not text.startswith(prefix):
        raise EditionError(f"Unexpected page furniture on page {page_number}.")
    return text[len(prefix):]


def verify_pdf(context: dict, data: bytes | None = None) -> dict:
    visual_review = "Pending separate inspection of rendered pages."
    if data is None:
        data = context["output_path"].read_bytes()
        sidecar = json.loads(context["sidecar_path"].read_text(encoding="utf-8-sig"))
        if (sidecar.get("edition_id") != context["manifest"]["edition_id"]
                or sidecar.get("output_path") != context["manifest"]["output"]["path"]
                or sidecar.get("output_sha256") != sha256(data)):
            raise EditionError("PDF differs from its saved edition verification record.")
        # Retain recorded page-review evidence only for the exact verified PDF.
        # The text and source checks below still run afresh.
        visual_review = sidecar.get("visual_review", visual_review)
    reader = PdfReader(io.BytesIO(data))
    if reader.is_encrypted:
        raise EditionError("The beta PDF must be directly readable.")
    outlines = [item for item in reader.outline if not isinstance(item, list)]
    expected_titles = ["Reader note", *[item["title"] for item in context["manifest"]["sources"]]]
    if [item.title for item in outlines] != expected_titles:
        raise EditionError("PDF bookmarks do not match the complete source order.")
    page_texts = [_page_text(page, index + 1) for index, page in enumerate(reader.pages)]
    source_results = []
    for index, (source, text) in enumerate(zip(context["manifest"]["sources"], context["texts"])):
        start = reader.get_destination_page_number(outlines[index + 1])
        end = (reader.get_destination_page_number(outlines[index + 2])
               if index + 2 < len(outlines) else len(reader.pages))
        actual = _compact("\n".join(page_texts[start:end]))
        expected = _compact("\n".join([
            source["title"], *[value if kind == "scene" else visible_inline(value)
                               for kind, value in markdown_blocks(text)],
        ]))
        if actual != expected:
            offset = next((position for position, pair in enumerate(zip(actual, expected)) if pair[0] != pair[1]), min(len(actual), len(expected)))
            raise EditionError(f"PDF text differs in {source['title']} near character {offset}: expected {expected[offset:offset+70]!r}; extracted {actual[offset:offset+70]!r}")
        source_results.append({"path": source["path"], "title": source["title"], "start_page": start + 1, "end_page": end, "text_verified": True})
    note_start = reader.get_destination_page_number(outlines[0])
    note_actual = _compact(page_texts[note_start])
    for note in context["manifest"]["reader_note"]:
        if _compact(visible_inline(note)) not in note_actual:
            raise EditionError("Reader note paragraph missing from the PDF.")
    for relative, initial_hash in context["starting_hashes"].items():
        if sha256(repository_path(context["root"], relative).read_bytes()) != initial_hash:
            raise EditionError(f"Input changed during export: {relative}")
    return {
        "edition_id": context["manifest"]["edition_id"],
        "source_commit": context["manifest"]["source_commit"],
        "output_path": context["manifest"]["output"]["path"],
        "output_sha256": sha256(data), "page_count": len(reader.pages),
        "chapter_count": 28, "appendix_count": 3, "bookmark_count": len(outlines),
        "text_verified": True, "source_preserved": True,
        "superseded_preserved": True, "checkout_byte_differences": context["checkout_byte_differences"],
        "sources": source_results,
        "rendering_conversions": "Markdown emphasis becomes font styling; wiki/link labels become visible text; scene separators become * * *; whitespace is collapsed only for text comparison. Unicode punctuation is unchanged.",
        "visual_review": visual_review,
    }


def build_edition(manifest_path: Path, *, root: Path = ROOT) -> dict:
    context = check_manifest(manifest_path, root=root)
    data = pdf_bytes(context)
    verification = verify_pdf(context, data)
    output = context["output_path"]
    sidecar = context["sidecar_path"]
    output.parent.mkdir(parents=True, exist_ok=True)
    created_output = False
    created_sidecar = False
    try:
        with output.open("xb") as stream:
            created_output = True
            stream.write(data)
        with sidecar.open("x", encoding="utf-8", newline="\n") as stream:
            created_sidecar = True
            json.dump(verification, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
    except Exception:
        # Only remove files this invocation created; existing releases are untouched.
        if created_sidecar:
            sidecar.unlink()
        if created_output:
            output.unlink()
        raise
    return verification


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("check", "build", "verify"))
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    path = args.manifest if args.manifest.is_absolute() else ROOT / args.manifest
    try:
        if args.command == "build":
            result = build_edition(path, root=ROOT)
        else:
            # Both read-only commands accept a completed edition. Only build
            # refuses collisions; verify additionally checks the saved PDF hash.
            context = check_manifest(path, root=ROOT, allow_output=True)
            result = (verify_pdf(context) if args.command == "verify" else {
                "edition_id": context["manifest"]["edition_id"], "check_passed": True,
                "chapter_count": 28, "appendix_count": 3,
                "checkout_byte_differences": context["checkout_byte_differences"],
            })
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (EditionError, OSError, UnicodeError, json.JSONDecodeError) as error:
        print(f"Beta edition blocked: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
