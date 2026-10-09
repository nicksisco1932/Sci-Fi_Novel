"""Independently check a Hive reader-package PDF against its selected sources.

This command reads repository sources and package artifacts. It writes only an
optional audit report when --report is supplied; it never rebuilds a package.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = "docs/reader_package/package.json"
DEFAULT_BASELINE = "docs/working_baseline.json"
PDF_NAME = "Hive_Earth_Beta_Reader_Package.pdf"
MANIFEST_NAME = "package_manifest.json"
WIKI_LINK = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
EMPHASIS = re.compile(r"\*\*(.+?)\*\*|\*(.+?)\*")
TOKENS = re.compile(r"\w+|[^\w\s]", re.UNICODE)


class AuditError(ValueError):
    """Raised when source selection, provenance, or PDF content fails audit."""


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def repo_file(root: Path, relative: str) -> Path:
    candidate = (root / relative).resolve(strict=True)
    if not candidate.is_relative_to(root.resolve()):
        raise AuditError(f"Repository path leaves the workspace: {relative}")
    return candidate


def tokens(text: str) -> list[str]:
    return TOKENS.findall(text.replace("\u00a0", " "))


def source_body(raw: bytes, *, omit_status: bool = False, remove_title: bool = False) -> str:
    text = raw.decode("utf-8").strip()
    text = WIKI_LINK.sub(lambda match: match.group(2) or match.group(1).split("#", 1)[0], text)
    lines = text.splitlines()
    if remove_title and lines and lines[0].startswith("# "):
        lines = lines[1:]
    if omit_status:
        lines = [line for line in lines if not line.startswith("> **Status:**")]
    text = "\n".join(lines).strip()
    rendered: list[str] = []
    for paragraph in re.split(r"\n\s*\n", text):
        paragraph = paragraph.strip()
        if not paragraph:
            continue
        if paragraph == "---":
            rendered.append("* * *")
            continue
        if paragraph.startswith("#"):
            heading = re.match(r"^#{1,6}\s+(.+)$", paragraph, re.S)
            if not heading:
                raise AuditError(f"Unsupported Markdown heading: {paragraph[:60]}")
            paragraph = heading.group(1)
        else:
            paragraph = " ".join(re.sub(r"^>\s?", "", line).strip() for line in paragraph.splitlines())
        paragraph = EMPHASIS.sub(lambda match: match.group(1) or match.group(2), paragraph)
        rendered.append(paragraph)
    return "\n\n".join(rendered)


def _chapter_records(root: Path, config: dict) -> tuple[list[dict], list[dict]]:
    folder = repo_file(root, config["manuscript_folder"])
    expected_order = config["chapter_order"]
    if not isinstance(expected_order, list) or not expected_order or any(type(n) is not int for n in expected_order):
        raise AuditError("Package chapter_order must be a nonempty list of integer chapter numbers")
    if expected_order != sorted(set(expected_order)):
        raise AuditError("Package chapter_order contains duplicates or is out of order")

    hash_path = repo_file(root, config["manuscript_hashes"])
    pinned = {}
    for line in hash_path.read_text(encoding="utf-8").splitlines():
        try:
            digest, name = line.split("  ", 1)
        except ValueError as exc:
            raise AuditError("Malformed chapter hash manifest") from exc
        if name in pinned:
            raise AuditError(f"Duplicate chapter hash entry: {name}")
        pinned[name] = digest.lower()

    actual: dict[int, Path] = {}
    for path in folder.glob("Chapter *.md"):
        match = re.fullmatch(r"Chapter (\d+)\s+[–-]\s+(.+)", path.stem)
        if not match:
            raise AuditError(f"Unrecognized chapter filename: {path.name}")
        number = int(match.group(1))
        if number in actual:
            raise AuditError(f"Duplicate chapter number: {number}")
        actual[number] = path
    if sorted(actual) != expected_order:
        raise AuditError(f"Chapter inventory differs from package order: expected {expected_order}, found {sorted(actual)}")
    if set(pinned) != {path.name for path in actual.values()}:
        raise AuditError("Chapter hash manifest does not cover exactly the selected chapter files")

    records: list[dict] = []
    sections: list[dict] = []
    for number in expected_order:
        path = repo_file(root, actual[number].relative_to(root).as_posix())
        raw = path.read_bytes()
        digest = sha256(raw)
        if pinned[path.name] != digest:
            raise AuditError(f"Chapter hash mismatch: {path.name}")
        title_match = re.fullmatch(r"Chapter \d+\s+[–-]\s+(.+)", path.stem)
        title = title_match.group(1)
        key = f"chapter-{number}"
        records.append({"path": path.relative_to(root).as_posix(), "sha256": digest})
        sections.append({"key": key, "title": title, "label": f"Chapter {number}",
                         "toc": f"Chapter {number} — {title}", "expected": source_body(raw)})
    return records, sections


def _source_selection(root: Path, config: dict) -> tuple[list[dict], list[dict], str]:
    baseline_path = repo_file(root, DEFAULT_BASELINE)
    baseline_bytes = baseline_path.read_bytes()
    baseline = json.loads(baseline_bytes)
    if baseline.get("working_folder") != config.get("manuscript_folder"):
        raise AuditError("Package manuscript folder differs from the approved working baseline")
    if baseline.get("chapter_order") != config.get("chapter_order"):
        raise AuditError("Package chapter order differs from the approved working baseline")

    chapter_records, chapters = _chapter_records(root, config)
    supporting_records: list[dict] = []
    support: list[dict] = []
    seen_keys: set[str] = set()
    for spec in config.get("supporting_sections", []):
        key = spec.get("key")
        if not key or key in seen_keys:
            raise AuditError(f"Missing or duplicate supporting-section key: {key}")
        seen_keys.add(key)
        path = repo_file(root, spec["path"])
        raw = path.read_bytes()
        digest = sha256(raw)
        if digest != spec.get("sha256", "").lower():
            raise AuditError(f"Supporting-source hash mismatch: {path.relative_to(root)}")
        body = source_body(raw, omit_status=bool(spec.get("omit_development_status")), remove_title=True)
        support.append({"key": key, "title": spec["title"], "label": spec.get("label", ""),
                        "toc": spec["title"], "expected": body, "kind": spec["kind"]})
        supporting_records.append({"path": spec["path"], "sha256": digest,
                                  "original_source": spec["original_source"],
                                  "developmental": spec.get("developmental", False),
                                  "presentation_omissions": ["foreword development-status line"]
                                  if spec.get("omit_development_status") else []})
    forewords = [item for item in support if item["kind"] == "foreword"]
    appendices = [item for item in support if item["kind"] == "appendix"]
    if len(forewords) != 1 or len(appendices) != 3 or len(support) != 4:
        raise AuditError("Expected one foreword and three appendices in the selected package")

    cover = config.get("cover")
    cover_records = []
    if cover:
        cover_path = repo_file(root, cover["path"])
        cover_digest = sha256(cover_path.read_bytes())
        if cover_digest != cover.get("sha256", "").lower() or cover.get("fit") != "contain":
            raise AuditError("Pinned cover hash or full-image presentation rule failed")
        cover_records.append({"path": cover["path"], "sha256": cover_digest,
                              "role": "front-cover", "original_source": cover["original_source"]})
    records = cover_records + chapter_records + supporting_records
    sections = forewords + chapters + appendices
    return records, sections, sha256(baseline_bytes)


def _audit_pdf(pdf_path: Path, expected: list[dict]) -> tuple[int, list[dict]]:
    try:
        reader = PdfReader(pdf_path, strict=True)
        if reader.is_encrypted:
            raise AuditError("Encrypted PDFs are not supported by the text audit")
        outlines = reader.outline
    except AuditError:
        raise
    except Exception as exc:
        raise AuditError(f"PDF could not be read: {type(exc).__name__}: {exc}") from exc

    destinations = []
    for item in outlines:
        if isinstance(item, list):
            continue
        destinations.append(item)
    expected_toc = [section["toc"] for section in expected]
    found_toc = [getattr(item, "title", None) for item in destinations]
    if found_toc != expected_toc:
        raise AuditError(f"PDF bookmark order differs from selected sections: {found_toc}")
    starts = [reader.get_destination_page_number(item) for item in destinations]
    if starts != sorted(set(starts)):
        raise AuditError("PDF section bookmarks are not in strictly increasing page order")

    findings = []
    for index, section in enumerate(expected):
        start = starts[index]
        stop = starts[index + 1] if index + 1 < len(starts) else len(reader.pages)
        extracted = []
        for page_number in range(start, stop):
            try:
                page_text = reader.pages[page_number].extract_text()
            except Exception as exc:
                raise AuditError(f"Text extraction failed on PDF page {page_number + 1}: {exc}") from exc
            if page_text is None:
                raise AuditError(f"Text extraction returned no result on PDF page {page_number + 1}")
            for line in page_text.splitlines():
                stripped = line.strip()
                if stripped not in ("Hive: Earth · Beta Reader Edition", str(page_number + 1)):
                    extracted.append(line)
        rendered_expected = "\n".join(value for value in
                                       (section["label"], section["title"], section["expected"]) if value)
        actual_text = "\n".join(extracted)
        expected_tokens = tokens(rendered_expected)
        actual_tokens = tokens(actual_text)
        if expected_tokens != actual_tokens:
            limit = min(len(expected_tokens), len(actual_tokens))
            mismatch = next((position for position in range(limit)
                             if expected_tokens[position] != actual_tokens[position]), limit)
            left = max(0, mismatch - 5)
            right_expected = " ".join(expected_tokens[left:mismatch + 5])
            right_actual = " ".join(actual_tokens[left:mismatch + 5])
            raise AuditError(
                f"Text mismatch in {section['key']} at token {mismatch}; "
                f"expected {len(expected_tokens)} tokens, extracted {len(actual_tokens)}; "
                f"expected near: {right_expected!r}; extracted near: {right_actual!r}"
            )
        findings.append({"section": section["key"], "first_page": start + 1,
                         "last_page": stop, "text_fidelity": "pass",
                         "tokens": len(expected_tokens)})
    return len(reader.pages), findings


def audit(root: Path, config_path: Path, baseline_path: Path | None = None) -> dict:
    """Validate the pinned package configuration, source files, manifest, and PDF."""
    root = root.resolve(strict=True)
    config_path = config_path if config_path.is_absolute() else root / config_path
    config_path = config_path.resolve(strict=True)
    if not config_path.is_relative_to(root):
        raise AuditError("Configuration path leaves the repository")
    config_bytes = config_path.read_bytes()
    try:
        config = json.loads(config_bytes)
    except Exception as exc:
        raise AuditError(f"Package configuration is invalid JSON: {exc}") from exc

    if baseline_path is not None and baseline_path != root / DEFAULT_BASELINE:
        raise AuditError("The approved baseline path is fixed by repository policy")
    source_records, expected_sections, baseline_digest = _source_selection(root, config)
    manifest_path = repo_file(root, f"{config['output_directory']}/{MANIFEST_NAME}")
    pdf_path = repo_file(root, f"{config['output_directory']}/{PDF_NAME}")
    try:
        manifest_bytes = manifest_path.read_bytes()
        manifest = json.loads(manifest_bytes)
    except Exception as exc:
        raise AuditError(f"Package manifest is missing or invalid: {exc}") from exc
    if manifest.get("config_sha256") != sha256(config_bytes):
        raise AuditError("Saved package manifest belongs to a different package configuration")
    if manifest.get("sources") != source_records:
        raise AuditError("Saved package manifest source list differs from independently checked inputs")
    if manifest.get("order") != [section["key"] for section in expected_sections]:
        raise AuditError("Saved package manifest section order differs from current selection")
    pdf_bytes = pdf_path.read_bytes()
    pdf_digest = sha256(pdf_bytes)
    if manifest.get("pdf_sha256") != pdf_digest:
        raise AuditError("PDF bytes differ from the saved package manifest")

    pages, findings = _audit_pdf(pdf_path, expected_sections)
    return {
        "schema_version": 1,
        "status": "accepted",
        "checks": {"working_baseline_selection": "pass", "source_hashes": "pass",
                   "package_manifest_binding": "pass", "pdf_hash": "pass",
                   "section_order_and_text_fidelity": "pass"},
        "provenance": {"git_head": _git_head(root),
                       "package_config_sha256": sha256(config_bytes),
                       "working_baseline_sha256": baseline_digest,
                       "package_manifest_sha256": sha256(manifest_bytes),
                       "pdf_sha256": pdf_digest},
        "pdf": {"path": pdf_path.relative_to(root).as_posix(), "pages": pages},
        "sections": findings,
        "visual_review": "not performed by this text audit",
        "author_acceptance": "not assessed",
    }


def _git_head(root: Path) -> str | None:
    try:
        result = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"],
                                check=True, capture_output=True, text=True, timeout=3)
        return result.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default=DEFAULT_CONFIG, help="Repository-relative package configuration")
    parser.add_argument("--report", help="Optional new repository-relative JSON report path; existing files are not overwritten")
    args = parser.parse_args(argv)
    try:
        result = audit(ROOT, Path(args.config))
        if args.report:
            report_path = (ROOT / args.report).resolve()
            if not report_path.is_relative_to(ROOT.resolve()):
                raise AuditError("Report path leaves the repository")
            if report_path.exists():
                raise AuditError("Report file already exists; choose a new path")
            report_path.parent.mkdir(parents=True, exist_ok=True)
            report_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (AuditError, OSError, KeyError, TypeError, ValueError) as exc:
        print(json.dumps({"schema_version": 1, "status": "rejected", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
