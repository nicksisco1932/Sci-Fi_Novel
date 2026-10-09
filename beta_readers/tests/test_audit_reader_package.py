"""Synthetic full-edition checks for the independent reader-PDF auditor."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

from reportlab.pdfgen.canvas import Canvas


REPO = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("audit_reader_package", REPO / "tools/audit_reader_package.py")
auditor = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(auditor)


class ReaderPackageAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "docs/canonical_md").mkdir(parents=True)
        (self.root / "docs/appendices").mkdir()
        (self.root / "docs/developmental").mkdir()
        (self.root / "docs/reader_package").mkdir()
        (self.root / "packages/edition").mkdir(parents=True)
        self.order = [1, *range(4, 31)]
        self.support_specs = [
            ("foreword", "foreword", "Author’s Foreword", "", False),
            ("figures", "appendix", "Figures of Time", "Appendix I", False),
            ("voss", "appendix", "Voss History", "Appendix II", False),
            ("gor", "appendix", "Gor of Almelah", "Appendix III", True),
        ]
        chapter_hashes = []
        for number in self.order:
            title = f"Chapter {number} – Test {number}"
            body = "First paragraph.\n\nSecond paragraph.\n"
            if number == 1:
                body = "First paragraph.\n\nParagraph that must survive.\n\nSecond paragraph.\n"
            (self.root / "docs/canonical_md" / f"{title}.md").write_text(body, encoding="utf-8")
            chapter_hashes.append((title, body.encode("utf-8")))
        (self.root / "docs/reader_package/chapter_hashes.txt").write_text(
            "".join(f"{self._sha(data)}  {name}.md\n" for name, data in chapter_hashes), encoding="utf-8")
        support = []
        for key, kind, title, label, developmental in self.support_specs:
            path = ("docs/developmental/foreword.md" if kind == "foreword"
                    else f"docs/appendices/{key}.md")
            text = f"# {title}\n\nOpening {key}.\n\nClosing {key}.\n"
            if key == "foreword":
                text += "\n> **Status:** internal drafting note\n"
            source = self.root / path
            source.write_text(text, encoding="utf-8")
            support.append({"key": key, "kind": kind, "title": title, "label": label,
                            "developmental": developmental, "path": path,
                            "sha256": self._sha(source.read_bytes()),
                            "original_source": f"source/{key}.md",
                            "omit_development_status": key == "foreword"})
        self.config = {
            "title": "Hive: Earth", "author": "Nicholas J. Sisco", "version": "v0.2",
            "date": "2026-10-09", "date_label": "October 9, 2026",
            "manuscript_folder": "docs/canonical_md",
            "manuscript_hashes": "docs/reader_package/chapter_hashes.txt",
            "chapter_order": self.order,
            "supporting_sections": support,
            "output_directory": "packages/edition",
        }
        self.config_path = self.root / "docs/reader_package/package.json"
        self.config_path.write_text(json.dumps(self.config, ensure_ascii=False), encoding="utf-8")
        baseline = {"working_folder": "docs/canonical_md", "chapter_order": self.order}
        (self.root / "docs/working_baseline.json").write_text(json.dumps(baseline), encoding="utf-8")
        self.manifest_path = self.root / "packages/edition/package_manifest.json"
        self.pdf_path = self.root / "packages/edition/Hive_Earth_Beta_Reader_Package.pdf"
        self._write_pdf(include_omitted_paragraph=True)
        source_records, expected, _ = auditor._source_selection(self.root, self.config)
        self.manifest = {"config_sha256": self._sha(self.config_path.read_bytes()),
                         "sources": source_records, "order": [item["key"] for item in expected],
                         "pdf_sha256": self._sha(self.pdf_path.read_bytes())}
        self._save_manifest()

    @staticmethod
    def _sha(data: bytes) -> str:
        return hashlib.sha256(data).hexdigest()

    def _save_manifest(self) -> None:
        self.manifest_path.write_text(json.dumps(self.manifest), encoding="utf-8")

    def _write_pdf(self, *, include_omitted_paragraph: bool) -> None:
        _, sections, _ = auditor._source_selection(self.root, self.config)
        canvas = Canvas(str(self.pdf_path), pagesize=(432, 648), invariant=1)
        for number, section in enumerate(sections):
            title = section["toc"]
            destination = f"section-{number}"
            canvas.bookmarkPage(destination)
            canvas.addOutlineEntry(title, destination, 0, False)
            y = 610
            lines = [value for value in (section["label"], section["title"]) if value]
            body = section["expected"]
            if section["key"] == "chapter-1" and not include_omitted_paragraph:
                body = body.replace("\n\nParagraph that must survive.\n\n", "\n\n")
            lines.extend(line for line in body.splitlines() if line.strip())
            for line in lines:
                canvas.drawString(36, y, line)
                y -= 17
            canvas.showPage()
        canvas.save()

    def test_complete_synthetic_edition_passes_with_source_provenance(self) -> None:
        before = {path: self._sha(path.read_bytes()) for path in self.root.rglob("*.md")}
        result = auditor.audit(self.root, Path("docs/reader_package/package.json"))
        self.assertEqual(result["status"], "accepted")
        self.assertEqual(len(result["sections"]), 32)
        self.assertEqual(result["checks"]["section_order_and_text_fidelity"], "pass")
        self.assertEqual(result["visual_review"], "not performed by this text audit")
        after = {path: self._sha(path.read_bytes()) for path in self.root.rglob("*.md")}
        self.assertEqual(before, after)

    def test_omitted_body_text_fails_even_when_manifest_is_resealed(self) -> None:
        self._write_pdf(include_omitted_paragraph=False)
        self.manifest["pdf_sha256"] = self._sha(self.pdf_path.read_bytes())
        self._save_manifest()
        with self.assertRaisesRegex(auditor.AuditError, "Text mismatch in chapter-1"):
            auditor.audit(self.root, Path("docs/reader_package/package.json"))

    def test_chapter_gap_in_configured_inventory_is_rejected(self) -> None:
        source = self.root / "docs/canonical_md/Chapter 16 – Test 16.md"
        source.unlink()
        with self.assertRaisesRegex(auditor.AuditError, "Chapter inventory differs"):
            auditor.audit(self.root, Path("docs/reader_package/package.json"))

    def test_pdf_byte_change_is_rejected_before_text_check(self) -> None:
        self.pdf_path.write_bytes(self.pdf_path.read_bytes() + b"tampered")
        with self.assertRaisesRegex(auditor.AuditError, "PDF bytes differ"):
            auditor.audit(self.root, Path("docs/reader_package/package.json"))


if __name__ == "__main__":
    unittest.main()
