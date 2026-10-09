"""Release-level checks using a complete synthetic edition and a real temp Git repo."""

import importlib.util
import contextlib
import io
import json
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

from PIL import Image
from pypdf import PdfReader, PdfWriter


SPEC = importlib.util.spec_from_file_location("build_beta", Path(__file__).parents[1] / "build_beta.py")
builder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(builder)


class EditionTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / "docs/canonical_md").mkdir(parents=True)
        (self.root / "docs/appendices").mkdir()
        (self.root / "beta_readers").mkdir()
        self.manifest_path = self.root / "beta_readers/test.json"
        sources = []
        for index, number in enumerate(builder.CHAPTER_NUMBERS):
            path = f"docs/canonical_md/Chapter {number} – Test.md"
            text = f"Chapter {number}'s text preserves “curly quotes,” em—dashes, and [[Elias Verran|Elias Verran]].\n\n**Purposeful emphasis** and *quiet thought*.\n\n---\n\n> “The final line remains.”\n"
            if number == 1:
                # Wrapped paragraphs, including page-split paragraphs, must
                # retain every line when PDF text is verified.
                text += "\n" + "Every wrapped line must survive extraction with all words intact. " * 110 + "\n"
            if number == 4:
                text = "\n\n".join([f"Short paragraph {index}." for index in range(26)])
                text += "\n\n---\n\nThe following scene starts here.\n\nA short final beat.\n"
            self._source(sources, path, f"Chapter {number} – Test", "chapter", text)
        for title in builder.APPENDIX_TITLES:
            path = f"docs/appendices/Appendix – {title}.md"
            text = f"## Archive Note\n\nThe complete {title} appendix.\n"
            if title == "Gor of Almelah":
                text += "\n**Developmental Draft — Not Yet Canon**\n\nUnresolved differences remain; nothing is silently canonized.\n"
            self._source(sources, path, title, "appendix", text)
        cover = self.root / "beta_readers/cover.png"
        Image.new("RGB", (64, 96), "#29425a").save(cover)
        self._git("init", "--quiet")
        self._git("add", "docs")
        self._git("-c", "user.name=Test", "-c", "user.email=test@example.invalid", "commit", "--quiet", "-m", "Preserve sources")
        commit = self._git("rev-parse", "HEAD").strip()
        self.manifest = {
            "edition_id": "test-beta-v2", "title": "Hive Earth", "author": "Nicholas Sisco",
            "edition_date": "2026-10-07", "source_commit": commit,
            "reader_note": ["Private review edition. Elias Verran / Verran terminology is preserved."],
            "sources": sources, "cover": {"path": "beta_readers/cover.png", "sha256": builder.sha256(cover.read_bytes())},
            "output": {"path": "output/pdf/test-beta.pdf"}, "superseded": [], "verification": {},
        }
        self._save()

    def _git(self, *arguments):
        return subprocess.check_output(["git", "-c", "core.autocrlf=false", "-C", str(self.root), *arguments]).decode("utf-8")

    def _source(self, records, path, title, role, text):
        data = text.encode("utf-8")
        (self.root / path).write_bytes(data)
        records.append({"role": role, "path": path, "title": title,
                        "raw_sha256": builder.sha256(data), "text_sha256": builder.text_sha256(data)})

    def _save(self):
        self.manifest_path.write_text(json.dumps(self.manifest), encoding="utf-8")

    def test_complete_pdf_preserves_all_text_and_inputs(self):
        hashes = {record["path"]: builder.sha256((self.root / record["path"]).read_bytes()) for record in self.manifest["sources"]}
        report = builder.build_edition(self.manifest_path, root=self.root)
        self.assertEqual((report["chapter_count"], report["appendix_count"], report["bookmark_count"]), (28, 3, 32))
        self.assertTrue(report["text_verified"])
        context = builder.check_manifest(self.manifest_path, root=self.root, allow_output=True)
        self.assertEqual(report, builder.verify_pdf(context))
        for path, digest in hashes.items():
            self.assertEqual(builder.sha256((self.root / path).read_bytes()), digest)
        self.assertTrue(self.manifest_path.with_suffix(".verification.json").exists())
        with self.assertRaisesRegex(builder.EditionError, "already exists"):
            builder.build_edition(self.manifest_path, root=self.root)

    def test_missing_or_changed_sources_stop_before_output(self):
        source = self.root / self.manifest["sources"][0]["path"]
        original = source.read_bytes()
        source.unlink()
        with self.assertRaisesRegex(builder.EditionError, "Missing source"):
            builder.build_edition(self.manifest_path, root=self.root)
        source.write_bytes(original + b"\nNew prose.\n")
        with self.assertRaisesRegex(builder.EditionError, "Source text changed"):
            builder.build_edition(self.manifest_path, root=self.root)
        self.assertFalse((self.root / self.manifest["output"]["path"]).exists())

    def test_duplicate_and_out_of_order_sources_fail(self):
        self.manifest["sources"][1]["path"] = self.manifest["sources"][0]["path"]
        self._save()
        with self.assertRaisesRegex(builder.EditionError, "Duplicate source"):
            builder.check_manifest(self.manifest_path, root=self.root)
        self.manifest["sources"][0]["title"] = "Chapter 2 – Superseded"
        self._save()
        with self.assertRaisesRegex(builder.EditionError, "Chapter order"):
            builder.check_manifest(self.manifest_path, root=self.root)

    def test_checkout_line_endings_are_portable(self):
        source = self.root / self.manifest["sources"][0]["path"]
        source.write_bytes(b"\xef\xbb\xbf" + source.read_bytes().replace(b"\n", b"\r\n"))
        result = builder.check_manifest(self.manifest_path, root=self.root)
        self.assertEqual(result["checkout_byte_differences"], [self.manifest["sources"][0]["path"]])

    def test_output_or_sidecar_collision_preserves_existing_bytes(self):
        output = self.root / self.manifest["output"]["path"]
        output.parent.mkdir(parents=True)
        output.write_bytes(b"Existing edition")
        with self.assertRaisesRegex(builder.EditionError, "already exists"):
            builder.build_edition(self.manifest_path, root=self.root)
        self.assertEqual(output.read_bytes(), b"Existing edition")
        output.unlink()
        sidecar = self.manifest_path.with_suffix(".verification.json")
        sidecar.write_bytes(b"Existing verification")
        with self.assertRaisesRegex(builder.EditionError, "already exists"):
            builder.build_edition(self.manifest_path, root=self.root)
        self.assertEqual(sidecar.read_bytes(), b"Existing verification")

    def test_manifest_hashes_cannot_hide_uncommitted_source_change(self):
        source_record = self.manifest["sources"][0]
        source = self.root / source_record["path"]
        source.write_bytes(source.read_bytes() + b"\nChanged after checkpoint.\n")
        source_record["raw_sha256"] = builder.sha256(source.read_bytes())
        source_record["text_sha256"] = builder.text_sha256(source.read_bytes())
        self._save()
        with self.assertRaisesRegex(builder.EditionError, "differs from checkpoint"):
            builder.check_manifest(self.manifest_path, root=self.root)

    def test_changed_pdf_bytes_rejected_even_when_prose_is_unchanged(self):
        builder.build_edition(self.manifest_path, root=self.root)
        context = builder.check_manifest(self.manifest_path, root=self.root, allow_output=True)
        output = context["output_path"]
        writer = PdfWriter(clone_from=PdfReader(output))
        writer.add_metadata({"/Subject": "Changed after verification"})
        with output.open("wb") as stream:
            writer.write(stream)
        with self.assertRaisesRegex(builder.EditionError, "differs from its saved"):
            builder.verify_pdf(context)

    def test_check_command_accepts_a_completed_edition_without_writing(self):
        builder.build_edition(self.manifest_path, root=self.root)
        output = self.root / self.manifest["output"]["path"]
        sidecar = self.manifest_path.with_suffix(".verification.json")
        starting = {path: path.read_bytes() for path in (output, sidecar, self.manifest_path)}
        captured = io.StringIO()
        with patch.object(builder, "ROOT", self.root), patch("sys.argv", [
            "build_beta.py", "check", "beta_readers/test.json",
        ]), contextlib.redirect_stdout(captured):
            self.assertEqual(builder.main(), 0)
        self.assertTrue(json.loads(captured.getvalue())["check_passed"])
        for path, original in starting.items():
            self.assertEqual(path.read_bytes(), original)

    def test_scene_divider_and_short_closing_beat_are_not_stranded(self):
        context = builder.check_manifest(self.manifest_path, root=self.root)
        reader = PdfReader(io.BytesIO(builder.pdf_bytes(context)))
        start = reader.get_destination_page_number(reader.outline[2])
        end = reader.get_destination_page_number(reader.outline[3])
        for index in range(start, end):
            lines = [line.strip() for line in builder._page_text(reader.pages[index], index + 1).splitlines() if line.strip()]
            self.assertNotEqual(lines[-1], "* * *")
            if "A short final beat." in lines:
                self.assertIn("The following scene starts here.", lines)

    def test_verify_retains_passed_visual_review_for_the_same_pdf(self):
        initial = builder.build_edition(self.manifest_path, root=self.root)
        self.assertEqual(initial["visual_review"], "Pending separate inspection of rendered pages.")
        sidecar = self.manifest_path.with_suffix(".verification.json")
        recorded = json.loads(sidecar.read_text(encoding="utf-8"))
        evidence = {"status": "passed", "pages_inspected": initial["page_count"],
                    "method": "All rendered pages inspected.", "issues_remaining": []}
        recorded["visual_review"] = evidence
        sidecar.write_text(json.dumps(recorded), encoding="utf-8")
        context = builder.check_manifest(self.manifest_path, root=self.root, allow_output=True)
        result = builder.verify_pdf(context)
        self.assertEqual(result["visual_review"], evidence)
        self.assertTrue(result["text_verified"])
        self.assertTrue(result["source_preserved"])


if __name__ == "__main__":
    unittest.main()
