"""Assemble a pinned manuscript and supporting sources into a shareable PDF.

Uses the bundled Python runtime, reportlab, pypdf and pypdfium2.
No manuscript or supporting source is rewritten by this command.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from html import escape
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageBreak, PageTemplate, Paragraph, Spacer,
)
from reportlab.platypus.tableofcontents import TableOfContents
from pypdf import PdfReader
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = re.compile(r"^Chapter (\d+)\s+[–-]\s+(.+)$")
WIKI = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def visible(text: str) -> str:
    return WIKI.sub(lambda m: m.group(2) or m.group(1).split("#", 1)[0], text)


def inline(text: str) -> str:
    text = escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\*(.+?)\*", r"<i>\1</i>", text)
    return text


def plain_inline(text: str) -> str:
    return re.sub(r"\*\*(.+?)\*\*|\*(.+?)\*", lambda m: m.group(1) or m.group(2), text)


def local_path(name: str) -> Path:
    path = (ROOT / name).resolve()
    if not path.is_relative_to(ROOT):
        raise ValueError(f"Package path leaves the workspace: {name}")
    return path


def validate_sources(config: dict) -> tuple[list[dict], list[dict]]:
    folder = local_path(config["manuscript_folder"])
    hashes = {}
    for line in local_path(config["manuscript_hashes"]).read_text(encoding="utf-8").splitlines():
        h, name = line.split("  ", 1)
        hashes[name] = h.lower()
    files = []
    for path in folder.glob("Chapter *.md"):
        match = CHAPTER.match(path.stem)
        if not match:
            raise ValueError(f"Unrecognized manuscript filename: {path.name}")
        files.append((int(match.group(1)), match.group(2), path))
    files.sort()
    if [n for n, _, _ in files] != config["chapter_order"]:
        raise ValueError("Manuscript chapter order or completeness differs from the package configuration")
    if set(hashes) != {p.name for _, _, p in files}:
        raise ValueError("Manuscript hash manifest does not cover exactly the input chapters")
    sections = []
    provenance = []
    if cover := config.get("cover"):
        path = local_path(cover["path"])
        data = path.read_bytes()
        if digest(data) != cover["sha256"]:
            raise ValueError("Cover artwork hash mismatch")
        if cover.get("fit") != "contain":
            raise ValueError("Cover must preserve the complete image using contain")
        with Image.open(path) as artwork:
            artwork.verify()
        provenance.append({"path": cover["path"], "sha256": digest(data),
                           "role": "front-cover", "original_source": cover["original_source"]})
    for n, title, path in files:
        data = path.read_bytes()
        if digest(data) != hashes[path.name]:
            raise ValueError(f"Manuscript hash mismatch: {path.name}")
        sections.append({"key": f"chapter-{n}", "title": title,
                         "label": f"Chapter {n}", "toc": f"Chapter {n} — {title}",
                         "body": visible(data.decode("utf-8").strip()), "kind": "chapter"})
        provenance.append({"path": path.relative_to(ROOT).as_posix(), "sha256": digest(data)})
    # Verify supporting snapshots and strip only the explicitly configured frontmatter label.
    support = []
    for spec in config["supporting_sections"]:
        path = local_path(spec["path"])
        data = path.read_bytes()
        if digest(data) != spec["sha256"]:
            raise ValueError(f"Supporting-source hash mismatch: {path.name}")
        text = visible(data.decode("utf-8").strip())
        lines = text.splitlines()
        if lines and lines[0].startswith("# "):
            lines = lines[1:]
        if spec.get("omit_development_status"):
            lines = [line for line in lines if not line.startswith("> **Status:**")]
        body = "\n".join(lines).strip()
        support.append({"key": spec["key"], "title": spec["title"], "label": spec.get("label", ""),
                        "toc": spec["title"], "body": body, "kind": spec["kind"]})
        provenance.append({"path": spec["path"], "sha256": digest(data),
                           "original_source": spec["original_source"],
                           "developmental": spec.get("developmental", False),
                           "presentation_omissions": ["foreword development-status line"] if spec.get("omit_development_status") else []})
    ordered = [x for x in support if x["kind"] == "foreword"] + sections + [x for x in support if x["kind"] == "appendix"]
    return ordered, provenance


class ReaderPDF(BaseDocTemplate):
    def __init__(self, path: Path, config: dict, styles: dict):
        self.config = config
        self.styles = styles
        self.section_starts = {}
        self.cover_pages = 2 if config.get("cover") else 1
        BaseDocTemplate.__init__(self, str(path), pagesize=(6 * inch, 9 * inch),
                                 leftMargin=.68 * inch, rightMargin=.68 * inch,
                                 topMargin=.72 * inch, bottomMargin=.66 * inch,
                                 title=config["title"], author=config["author"],
                                 subject=f"Beta reader package — manuscript {config['version']}",
                                 pageCompression=1)
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height,
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id="text")
        self.addPageTemplates(PageTemplate(id="reader", frames=[frame], onPage=self.page_art))

    def beforeDocument(self):
        self.section_starts = {}

    def page_art(self, canvas, doc):
        canvas.saveState()
        if doc.page == 1 and self.config.get("cover"):
            artwork = ImageReader(str(local_path(self.config["cover"]["path"])))
            width, height = artwork.getSize()
            page_width, page_height = self.pagesize
            scale = min(page_width / width, page_height / height)
            draw_width, draw_height = width * scale, height * scale
            canvas.setFillColor(colors.HexColor("#15202b"))
            canvas.rect(0, 0, page_width, page_height, fill=1, stroke=0)
            canvas.drawImage(artwork, (page_width - draw_width) / 2,
                             (page_height - draw_height) / 2,
                             width=draw_width, height=draw_height, mask="auto")
        if doc.page > self.cover_pages:
            canvas.setFont("Georgia", 7.5)
            canvas.setFillColor(colors.HexColor("#666666"))
            canvas.drawCentredString(3 * inch, 8.64 * inch, "Hive: Earth · Beta Reader Edition")
            canvas.drawCentredString(3 * inch, .34 * inch, str(doc.page))
        canvas.restoreState()

    def afterFlowable(self, flowable):
        if hasattr(flowable, "section_key"):
            key = flowable.section_key
            self.section_starts[key] = self.page
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(flowable.toc_title, key, 0, False)
            self.notify("TOCEntry", (0, flowable.toc_title, self.page, key))


def styles() -> dict:
    fonts = Path("C:/Windows/Fonts")
    for name, filename in [("Georgia", "georgia.ttf"), ("Georgia-Bold", "georgiab.ttf"),
                           ("Georgia-Italic", "georgiai.ttf"), ("Georgia-BoldItalic", "georgiaz.ttf")]:
        pdfmetrics.registerFont(TTFont(name, str(fonts / filename)))
    pdfmetrics.registerFontFamily("Georgia", normal="Georgia", bold="Georgia-Bold", italic="Georgia-Italic", boldItalic="Georgia-BoldItalic")
    body = ParagraphStyle("body", fontName="Georgia", fontSize=10.8, leading=15,
                          spaceAfter=6.2, textColor=colors.HexColor("#222222"),
                          allowWidows=0, allowOrphans=0)
    return {
        "body": body,
        "quote": ParagraphStyle("quote", parent=body, leftIndent=12, rightIndent=8),
        "heading": ParagraphStyle("heading", parent=body, fontName="Georgia-Bold", fontSize=19,
                                  leading=25, spaceAfter=24, keepWithNext=True),
        "subheading": ParagraphStyle("subheading", parent=body, fontName="Georgia-Bold", fontSize=13,
                                     leading=18, spaceBefore=12, spaceAfter=8, keepWithNext=True),
        "minor": ParagraphStyle("minor", parent=body, fontName="Georgia-Bold", fontSize=11,
                                leading=16, spaceBefore=10, keepWithNext=True),
        "label": ParagraphStyle("label", parent=body, fontSize=9, leading=14, spaceAfter=8),
        "cover": ParagraphStyle("cover", parent=body, fontSize=31, leading=39, alignment=TA_CENTER),
        "center": ParagraphStyle("center", parent=body, alignment=TA_CENTER, spaceAfter=12),
        "scene": ParagraphStyle("scene", parent=body, alignment=TA_CENTER, spaceBefore=4, spaceAfter=10),
        "toc": ParagraphStyle("toc", parent=body, fontSize=10, leading=15, spaceAfter=5,
                              leftIndent=0, rightIndent=10),
    }


def body_flowables(text: str, st: dict) -> tuple[list, str]:
    flow = []
    plain = []
    for paragraph in re.split(r"\n\s*\n", text):
        paragraph = paragraph.strip()
        if not paragraph:
            continue
        if paragraph == "---":
            flow.append(Paragraph("* * *", st["scene"]))
            plain.append("* * *")
            continue
        if paragraph.startswith("#"):
            match = re.match(r"^(#{1,6})\s+(.+)$", paragraph, re.S)
            if not match:
                raise ValueError(f"Unrecognized heading: {paragraph[:60]}")
            txt = match.group(2)
            flow.append(Paragraph(inline(txt), st["subheading" if len(match.group(1)) <= 2 else "minor"]))
        else:
            quote = paragraph.startswith(">")
            txt = " ".join(re.sub(r"^>\s?", "", line).strip() for line in paragraph.splitlines())
            flow.append(Paragraph(inline(txt), st["quote" if quote else "body"]))
        plain.append(plain_inline(txt))
    return flow, "\n\n".join(plain)


def token_normalize(text: str) -> list[str]:
    return re.findall(r"\w+|[^\w\s]", text.replace("\u00a0", " "), re.UNICODE)


def verify_pdf(pdf: Path, doc: ReaderPDF, sections: list[dict], plain_sections: dict) -> dict:
    reader = PdfReader(pdf)
    starts = doc.section_starts
    if set(starts) != {s["key"] for s in sections}:
        raise ValueError("PDF section/bookmark completeness check failed")
    findings = []
    for i, sec in enumerate(sections):
        start = starts[sec["key"]]
        end = starts[sections[i + 1]["key"]] - 1 if i + 1 < len(sections) else len(reader.pages)
        page_text = []
        for num in range(start, end + 1):
            lines = (reader.pages[num - 1].extract_text() or "").splitlines()
            page_text.extend(line for line in lines if line.strip() not in
                             ("Hive: Earth · Beta Reader Edition", str(num)))
        expected = "\n".join([sec["label"], sec["title"], plain_sections[sec["key"]]])
        actual = "\n".join(page_text)
        if token_normalize(expected) != token_normalize(actual):
            import difflib
            a, b = token_normalize(expected), token_normalize(actual)
            first = next((x for x in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes() if x[0] != "equal"), None)
            raise ValueError(f"Extracted-text mismatch in {sec['key']}: {first}")
        findings.append({"section": sec["key"], "first_page": start, "last_page": end,
                         "text_fidelity": "pass", "words": len(re.findall(r"\b\w+\b", expected))})
    return {"pages": len(reader.pages), "section_order_and_text_fidelity": "pass", "sections": findings}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="docs/reader_package/package.json")
    parser.add_argument("--output", help="New edition directory; preserve earlier editions")
    parser.add_argument("--rebuild", action="store_true", help="Regenerate an unchanged edition instead of reusing its verified artifacts")
    args = parser.parse_args()
    cfg_path = local_path(args.config)
    cfg_bytes = cfg_path.read_bytes()
    cfg = json.loads(cfg_bytes)
    sections, provenance = validate_sources(cfg)  # validate all inputs before output writes
    out = local_path(args.output or cfg["output_directory"])
    old_manifest = out / "package_manifest.json"
    if old_manifest.exists():
        old = json.loads(old_manifest.read_text(encoding="utf-8"))
        if old["config_sha256"] != digest(cfg_bytes) or old["sources"] != provenance:
            raise ValueError("This package edition already exists with different inputs; choose a new output directory")
        for filename, hash_key in [("Hive_Earth_Beta_Reader_Package.pdf", "pdf_sha256"),
                                   ("Hive_Earth_Beta_Reader_Package.md", "markdown_sha256")]:
            existing = out / filename
            if existing.exists() and digest(existing.read_bytes()) != old[hash_key]:
                raise ValueError(f"Existing {filename} was changed after export; preserve it and choose a new output directory")
        if not args.rebuild and all((out / name).exists() for name in
                                    ("Hive_Earth_Beta_Reader_Package.pdf", "Hive_Earth_Beta_Reader_Package.md")):
            print(json.dumps({"pdf": str(out / "Hive_Earth_Beta_Reader_Package.pdf"),
                              "pages": old["verification"]["pages"], "reused": True,
                              "input_and_artifact_hashes": "pass",
                              "text_fidelity": old["verification"]["section_order_and_text_fidelity"]}))
            return
    out.mkdir(parents=True, exist_ok=True)
    st = styles()
    pdf = out / "Hive_Earth_Beta_Reader_Package.pdf"
    doc = ReaderPDF(pdf, cfg, st)
    story = [Spacer(1, 1.3 * inch), Paragraph(escape(cfg["title"]), st["cover"]),
             Spacer(1, .28 * inch), Paragraph(escape(cfg["author"]), st["center"]),
             Spacer(1, 1.0 * inch), Paragraph("Beta Reader Edition", st["center"]),
             Paragraph(f"Manuscript {escape(cfg['version'])}<br/>{escape(cfg['date_label'])}", st["center"]), PageBreak(),
             Paragraph("Contents", st["heading"])]
    if cfg.get("cover"):
        story = [Spacer(1, 1), PageBreak()] + story
    toc = TableOfContents()
    toc.levelStyles = [st["toc"]]
    story.append(toc)
    plain = {}
    markdown = [f"# {cfg['title']}", cfg["author"], f"Beta Reader Edition · Manuscript {cfg['version']} · {cfg['date_label']}"]
    for sec in sections:
        story.append(PageBreak())
        if sec["label"]:
            story.append(Paragraph(escape(sec["label"]), st["label"]))
        heading = Paragraph(escape(sec["title"]), st["heading"])
        heading.section_key = sec["key"]
        heading.toc_title = sec["toc"]
        story.append(heading)
        flow, plain[sec["key"]] = body_flowables(sec["body"], st)
        story.extend(flow)
        markdown.extend((f"# {sec['toc']}", sec["body"]))
    def stable_canvas(*args, **kwargs):
        kwargs["invariant"] = 1
        return Canvas(*args, **kwargs)
    doc.multiBuild(story, canvasmaker=stable_canvas)
    fidelity = verify_pdf(pdf, doc, sections, plain)
    md = out / "Hive_Earth_Beta_Reader_Package.md"
    md.write_text("\n\n".join(markdown) + "\n", encoding="utf-8", newline="")
    manifest = {"title": cfg["title"], "author": cfg["author"], "version": cfg["version"],
                "date": cfg["date"], "config_sha256": digest(cfg_bytes), "sources": provenance,
                "order": [s["key"] for s in sections], "verification": fidelity,
                "pdf_sha256": digest(pdf.read_bytes()), "markdown_sha256": digest(md.read_bytes()),
                "developmental_appendix_notice": "Gor appendix retains its non-canon status and unresolved Chapter 15 conflicts"}
    if cfg.get("cover"):
        manifest["cover"] = {**cfg["cover"], "first_page": 1, "title_page": 2}
    (out / "package_config.json").write_bytes(cfg_bytes)
    old_manifest.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="")
    print(json.dumps({"pdf": str(pdf), "pages": fidelity["pages"], "chapters": len(cfg["chapter_order"]),
                      "frontmatter": 1, "appendices": 3, "text_fidelity": "pass"}, ensure_ascii=True))


if __name__ == "__main__":
    main()
