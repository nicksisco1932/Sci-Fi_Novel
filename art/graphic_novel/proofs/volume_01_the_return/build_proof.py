from __future__ import annotations

import hashlib
import shutil
from dataclasses import dataclass
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[4]
PROOF = Path(__file__).resolve().parent
SEQUENCE = PROOF / "sequence"
PAGE_SIZE = (1024, 1536)
PDF_SIZE = (6 * 72, 9 * 72)

ARIAL = Path(r"C:\Windows\Fonts\arial.ttf")
ARIAL_BOLD = Path(r"C:\Windows\Fonts\arialbd.ttf")
ARIAL_NARROW_BOLD = Path(r"C:\Windows\Fonts\ARIALNB.TTF")


@dataclass(frozen=True)
class Page:
    number: int
    kind: str
    title: str
    source: str | None = None
    background: str | None = None


STORY_PAGES = [
    ("The Return", "art/graphic_novel/chapter_01_wakeup/page-01.png"),
    ("The Return", "art/graphic_novel/chapter_01_wakeup/page-02.png"),
    ("The Return", "art/graphic_novel/chapter_01_wakeup/page-03.png"),
    ("The Return", "art/graphic_novel/scenes/chapter_01_launch_anomaly/page-01.png"),
    ("The Return", "art/graphic_novel/scenes/chapter_01_launch_anomaly/page-02.png"),
    ("The Return", "art/graphic_novel/scenes/chapter_01_korin_office/page-01.png"),
    ("The Return", "art/graphic_novel/experiments/korin-office-meditation/assets/variant-03-the-rain.png"),
    ("Controlled Variables", "art/graphic_novel/scenes/chapter_04_the_walk/page-01.png"),
    ("Controlled Variables", "art/graphic_novel/scenes/chapter_05_opening_move/page-01.png"),
    ("Controlled Variables", "art/graphic_novel/scenes/chapter_05_opening_move/page-02.png"),
    ("Controlled Variables", "art/graphic_novel/scenes/chapter_06_controlled_variables/page-01.png"),
    ("Controlled Variables", "art/graphic_novel/scenes/chapter_07_the_seam/page-01.png"),
    ("Controlled Variables", "art/graphic_novel/scenes/chapter_07_the_seam/page-02.png"),
    ("Lanes Between Signals", "art/graphic_novel/scenes/chapter_08_the_drop/page-01.png"),
    ("Lanes Between Signals", "art/graphic_novel/scenes/chapter_08_the_drop/page-02.png"),
    ("Lanes Between Signals", "art/graphic_novel/scenes/chapter_09_fractures_in_the_core/page-01.png"),
    ("Lanes Between Signals", "art/graphic_novel/scenes/chapter_10_signal_to_noise/page-01.png"),
    ("Lanes Between Signals", "art/graphic_novel/scenes/chapter_10_signal_to_noise/page-02.png"),
    ("Lanes Between Signals", "art/graphic_novel/scenes/chapter_11_contingencies/page-01.png"),
    ("Lanes Between Signals", "art/graphic_novel/scenes/chapter_11_contingencies/page-02.png"),
    ("Lanes Between Signals", "art/graphic_novel/scenes/chapter_11_contingencies/page-03.png"),
    ("Lanes Between Signals", "art/graphic_novel/scenes/chapter_12_lanes_between_signals/page-01.png"),
    ("Lanes Between Signals", "art/graphic_novel/scenes/chapter_12_lanes_between_signals/page-02.png"),
    ("Lanes Between Signals", "art/graphic_novel/scenes/chapter_12_lanes_between_signals/page-03.png"),
    ("The Night the Oath Broke", "art/graphic_novel/scenes/chapter_13_soft_edge/page-01.png"),
    ("The Night the Oath Broke", "art/graphic_novel/scenes/chapter_13_soft_edge/page-02.png"),
    ("The Night the Oath Broke", "art/graphic_novel/scenes/chapter_13_soft_edge/page-03.png"),
    ("The Night the Oath Broke", "art/graphic_novel/scenes/chapter_14_broken_clinic/page-01.png"),
    ("The Night the Oath Broke", "art/graphic_novel/scenes/chapter_14_broken_clinic/page-02.png"),
    ("The Night the Oath Broke", "art/graphic_novel/scenes/chapter_14_broken_clinic/page-03.png"),
    ("The Night the Oath Broke", "art/graphic_novel/scenes/chapter_15_safehouse_recognition/page-01.png"),
    ("The Night the Oath Broke", "art/graphic_novel/scenes/chapter_15_almelah_dojo/page-01.png"),
    ("The Night the Oath Broke", "art/graphic_novel/scenes/chapter_15_almelah_dojo/page-02.png"),
    ("The Night the Oath Broke", "art/graphic_novel/scenes/chapter_15_almelah_dojo/page-03.png"),
    ("The Night the Oath Broke", "art/graphic_novel/scenes/chapter_15_augmentation_offer/page-01.png"),
    ("The Night the Oath Broke", "art/graphic_novel/scenes/chapter_15_augmentation_offer/page-02.png"),
    ("The Night the Oath Broke", "art/graphic_novel/scenes/chapter_15_almelah_fall/page-01.png"),
    ("The Night the Oath Broke", "art/graphic_novel/scenes/chapter_15_almelah_fall/page-02.png"),
    ("The Night the Oath Broke", "art/graphic_novel/scenes/chapter_15_almelah_fall/page-03.png"),
    ("The Night the Oath Broke", "art/graphic_novel/scenes/chapter_15_safehouse_conclusion/page-01.png"),
    ("The Night the Oath Broke", "art/graphic_novel/scenes/chapter_15_safehouse_conclusion/page-02.png"),
    ("The Night the Oath Broke", "art/graphic_novel/scenes/chapter_15_gor_in_rain/page-01.png"),
]

SECTION_BACKGROUNDS = {
    "The Return": "art/graphic_novel/scenes/chapter_01_korin_office/page-01.png",
    "Controlled Variables": "art/graphic_novel/scenes/chapter_05_opening_move/page-01.png",
    "Lanes Between Signals": "art/graphic_novel/locations/lower-grid-market/landscape-reference.png",
    "The Night the Oath Broke": "art/graphic_novel/scenes/chapter_15_gor_in_rain/page-01.png",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def fit_page(image: Image.Image) -> Image.Image:
    image = image.convert("RGB")
    if image.size == PAGE_SIZE:
        return image
    target_ratio = PAGE_SIZE[0] / PAGE_SIZE[1]
    source_ratio = image.width / image.height
    if source_ratio > target_ratio:
        width = round(image.height * target_ratio)
        left = (image.width - width) // 2
        image = image.crop((left, 0, left + width, image.height))
    else:
        height = round(image.width / target_ratio)
        top = (image.height - height) // 2
        image = image.crop((0, top, image.width, top + height))
    return image.resize(PAGE_SIZE, Image.Resampling.LANCZOS)


def draw_centered(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, y: int, fill: str) -> None:
    box = draw.textbbox((0, 0), text, font=font)
    x = (PAGE_SIZE[0] - (box[2] - box[0])) // 2
    draw.text((x, y), text, font=font, fill=fill)


def title_page(background: Path, title: str, subtitle: str | None, output: Path, darken: float = 0.28) -> None:
    image = fit_page(Image.open(background))
    image = ImageEnhance.Brightness(image).enhance(darken)
    overlay = Image.new("RGBA", PAGE_SIZE, (0, 0, 0, 35))
    image = Image.alpha_composite(image.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(image)
    title_font = ImageFont.truetype(str(ARIAL_NARROW_BOLD), 72)
    subtitle_font = ImageFont.truetype(str(ARIAL), 28)
    draw_centered(draw, title.upper(), title_font, 655, "#F2F0EA")
    if subtitle:
        draw_centered(draw, subtitle, subtitle_font, 750, "#C7C6C2")
    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output, quality=95)


def colophon_page(output: Path) -> None:
    image = Image.new("RGB", PAGE_SIZE, "#111416")
    draw = ImageDraw.Draw(image)
    heading = ImageFont.truetype(str(ARIAL_NARROW_BOLD), 48)
    body = ImageFont.truetype(str(ARIAL), 26)
    small = ImageFont.truetype(str(ARIAL), 21)
    draw.text((96, 140), "GRAPHIC NOVEL PROOF OF CONCEPT", font=heading, fill="#ECE9E1")
    lines = [
        "Adapted from the active canonical manuscript through Chapter 15.",
        "Continuous section titles are used because canonical Chapters 2 and 3 are absent.",
        "Generated faces, costumes, architecture, props, and staging remain adaptation designs.",
        "The Korin meditation coda and its five captions are adaptation-only additions.",
        "This volume is a digital review proof, not a publication or print-production master.",
    ]
    y = 300
    for line in lines:
        words = line.split()
        current = ""
        for word in words:
            trial = f"{current} {word}".strip()
            if draw.textlength(trial, font=body) > 820:
                draw.text((96, y), current, font=body, fill="#C6C4BE")
                y += 42
                current = word
            else:
                current = trial
        if current:
            draw.text((96, y), current, font=body, fill="#C6C4BE")
            y += 58
    draw.text((96, 1290), "Source: docs/canonical_md/", font=small, fill="#8F918E")
    draw.text((96, 1330), "Volume endpoint: The Night the Oath Broke", font=small, fill="#8F918E")
    draw.text((96, 1370), "Status: proof for continuity, lettering, and visual-language review", font=small, fill="#8F918E")
    image.save(output, quality=95)


def build_page_plan() -> list[Page]:
    pages: list[Page] = []
    number = 1
    pages.append(Page(number, "cover", "Cassian Rho: The Return", background="art/graphic_novel/locations/hive-spindle-city/landscape-reference.png"))
    number += 1
    story_index = 0
    for section in SECTION_BACKGROUNDS:
        pages.append(Page(number, "divider", section, background=SECTION_BACKGROUNDS[section]))
        number += 1
        while story_index < len(STORY_PAGES) and STORY_PAGES[story_index][0] == section:
            _, source = STORY_PAGES[story_index]
            pages.append(Page(number, "story", Path(source).stem, source=source))
            story_index += 1
            number += 1
    pages.append(Page(number, "colophon", "Colophon"))
    if len(pages) != 48 or number != 48 or story_index != 42:
        raise RuntimeError(f"Invalid proof plan: {len(pages)} pages, {story_index} story pages")
    return pages


def build_sequence(pages: list[Page]) -> None:
    SEQUENCE.mkdir(parents=True, exist_ok=True)
    for old in SEQUENCE.glob("*.png"):
        old.unlink()
    for page in pages:
        output = SEQUENCE / f"{page.number:03d}-{page.kind}.png"
        if page.kind == "cover":
            title_page(ROOT / page.background, "Cassian Rho: The Return", "Graphic Novel Proof of Concept - Provisional", output, 0.34)
        elif page.kind == "divider":
            title_page(ROOT / page.background, page.title, None, output, 0.20)
        elif page.kind == "colophon":
            colophon_page(output)
        else:
            source = ROOT / page.source
            with Image.open(source) as image:
                fit_page(image).save(output, quality=95)


def write_manifest(pages: list[Page]) -> None:
    lines = [
        "# Volume One Proof Manifest",
        "",
        "Working title: `Cassian Rho: The Return`",
        "",
        "Format: 48 pages, 6x9-inch digital review PDF, continuous titled sections.",
        "",
        "Status: complete visual proof; not dialogue-final or publication-ready.",
        "",
        "Lettering gate: Chapters 1 and 4-10 retain generated lettering pending the one-page correction workflow. New art-only pages use controlled lettering specifications.",
        "",
        "| PDF page | Type | Section / title | Source |",
        "|---:|---|---|---|",
    ]
    section = ""
    for page in pages:
        if page.kind == "divider":
            section = page.title
        source = f"`{page.source}`" if page.source else "Generated deterministically by `build_proof.py`"
        title = section if page.kind == "story" else page.title
        lines.append(f"| {page.number} | {page.kind} | {title} | {source} |")
    (PROOF / "manifest.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_hashes() -> None:
    output = PROOF / "source-hashes-before.sha256"
    if output.exists():
        return
    paths = sorted({ROOT / source for _, source in STORY_PAGES})
    source_studies = [
        ROOT / "art/graphic_novel/experiments/korin-office-meditation/assets/study-01-architectural-isolation.png",
        ROOT / "art/graphic_novel/experiments/korin-office-meditation/assets/study-02-partial-face.png",
        ROOT / "art/graphic_novel/experiments/korin-office-meditation/assets/study-03-rain-reflection.png",
    ]
    paths.extend(source_studies)
    lines = [f"{sha256(path)}  {path.relative_to(ROOT).as_posix()}" for path in paths]
    output.write_text("\n".join(lines) + "\n", encoding="ascii")


def build_pdf(pages: list[Page]) -> Path:
    output = PROOF / "cassian-rho-the-return-proof.pdf"
    pdfmetrics.registerFont(TTFont("ProofArial", str(ARIAL)))
    pdfmetrics.registerFont(TTFont("ProofArialNarrowBold", str(ARIAL_NARROW_BOLD)))
    pdf = canvas.Canvas(str(output), pagesize=PDF_SIZE, pageCompression=1)
    pdf.setTitle("Cassian Rho: The Return - Graphic Novel Proof of Concept")
    pdf.setAuthor("Nick S.")
    pdf.setSubject("Provisional graphic novel proof adapted from the Sci-Fi Novel manuscript")
    pdf.setKeywords("graphic novel, proof of concept, Cassian Rho, The Return")

    def draw_background(path: Path, darken: float) -> None:
        with Image.open(path) as source:
            image = ImageEnhance.Brightness(fit_page(source)).enhance(darken)
            overlay = Image.new("RGBA", PAGE_SIZE, (0, 0, 0, 35))
            image = Image.alpha_composite(image.convert("RGBA"), overlay).convert("RGB")
            stream = BytesIO()
            image.save(stream, format="JPEG", quality=95)
            stream.seek(0)
            pdf.drawImage(ImageReader(stream), 0, 0, width=PDF_SIZE[0], height=PDF_SIZE[1])

    def draw_centered_pdf(text: str, font: str, size: float, y: float, color: tuple[float, float, float]) -> None:
        pdf.setFont(font, size)
        pdf.setFillColorRGB(*color)
        pdf.drawCentredString(PDF_SIZE[0] / 2, y, text)

    def draw_colophon_pdf() -> None:
        pdf.setFillColorRGB(17 / 255, 20 / 255, 22 / 255)
        pdf.rect(0, 0, PDF_SIZE[0], PDF_SIZE[1], fill=1, stroke=0)
        pdf.setFillColorRGB(236 / 255, 233 / 255, 225 / 255)
        pdf.setFont("ProofArialNarrowBold", 20)
        pdf.drawString(40.5, 570, "GRAPHIC NOVEL PROOF OF CONCEPT")
        body_lines = [
            "Adapted from the active canonical manuscript through Chapter 15.",
            "Continuous section titles are used because canonical Chapters 2 and 3 are absent.",
            "Generated faces, costumes, architecture, props, and staging remain adaptation designs.",
            "The Korin meditation coda and its five captions are adaptation-only additions.",
            "This volume is a digital review proof, not a publication or print-production master.",
        ]
        pdf.setFillColorRGB(198 / 255, 196 / 255, 190 / 255)
        pdf.setFont("ProofArial", 10.8)
        y = 500
        for line in body_lines:
            words = line.split()
            current = ""
            for word in words:
                trial = f"{current} {word}".strip()
                if pdf.stringWidth(trial, "ProofArial", 10.8) > 350:
                    pdf.drawString(40.5, y, current)
                    y -= 17
                    current = word
                else:
                    current = trial
            if current:
                pdf.drawString(40.5, y, current)
                y -= 25
        pdf.setFillColorRGB(143 / 255, 145 / 255, 142 / 255)
        pdf.setFont("ProofArial", 8.8)
        pdf.drawString(40.5, 101, "Source: docs/canonical_md/")
        pdf.drawString(40.5, 84, "Volume endpoint: The Night the Oath Broke")
        pdf.drawString(40.5, 67, "Status: proof for continuity, lettering, and visual-language review")

    for page in pages:
        if page.kind == "cover":
            draw_background(ROOT / page.background, 0.34)
            draw_centered_pdf("CASSIAN RHO: THE RETURN", "ProofArialNarrowBold", 30, 356, (242 / 255, 240 / 255, 234 / 255))
            draw_centered_pdf("Graphic Novel Proof of Concept - Provisional", "ProofArial", 11.8, 319, (199 / 255, 198 / 255, 194 / 255))
        elif page.kind == "divider":
            draw_background(ROOT / page.background, 0.20)
            draw_centered_pdf(page.title.upper(), "ProofArialNarrowBold", 30, 356, (242 / 255, 240 / 255, 234 / 255))
        elif page.kind == "colophon":
            draw_colophon_pdf()
        else:
            source = SEQUENCE / f"{page.number:03d}-{page.kind}.png"
            pdf.drawImage(ImageReader(str(source)), 0, 0, width=PDF_SIZE[0], height=PDF_SIZE[1], preserveAspectRatio=False)
        pdf.showPage()
    pdf.save()
    return output


def build_contact_sheet(pages: list[Page]) -> None:
    thumb = (192, 288)
    columns = 6
    rows = 8
    gutter = 16
    label_height = 28
    sheet = Image.new("RGB", (columns * (thumb[0] + gutter) + gutter, rows * (thumb[1] + label_height + gutter) + gutter), "#202326")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.truetype(str(ARIAL), 18)
    for index, page in enumerate(pages):
        row, column = divmod(index, columns)
        x = gutter + column * (thumb[0] + gutter)
        y = gutter + row * (thumb[1] + label_height + gutter)
        source = SEQUENCE / f"{page.number:03d}-{page.kind}.png"
        with Image.open(source) as image:
            image = fit_page(image).resize(thumb, Image.Resampling.LANCZOS)
            sheet.paste(image, (x, y))
        draw.text((x, y + thumb[1] + 4), f"{page.number:02d} {page.kind}", font=font, fill="#ECE9E1")
    sheet.save(PROOF / "contact-sheet-48-pages.png", quality=95)


def main() -> None:
    pages = build_page_plan()
    PROOF.mkdir(parents=True, exist_ok=True)
    build_sequence(pages)
    write_manifest(pages)
    write_hashes()
    build_pdf(pages)
    build_contact_sheet(pages)
    print(f"Built {len(pages)} pages in {SEQUENCE}")


if __name__ == "__main__":
    main()
