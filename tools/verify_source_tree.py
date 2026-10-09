#!/usr/bin/env python3
"""Read-only integrity checks for the Hive source tree and frozen beta edition.

Standard library only; safe to run in any checkout without modifying files.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
issues: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        issues.append(message)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    require((ROOT / "docs/canonical_md").is_dir(), "Missing active docs/canonical_md manuscript.")
    require(not (ROOT / "docs/canonical").exists(), "Redundant docs/canonical must not be restored.")
    require((ROOT / "docs/appendices").is_dir(), "Missing active docs/appendices.")
    require(len(list((ROOT / "Legacy").glob("*.docx"))) >= 17,
            "Legacy must retain the original 17 archived DOCX files.")
    for folder in ("beta", "proofs", "published"):
        require((ROOT / "editions" / folder / "README.md").is_file(),
                f"Missing edition stage documentation: editions/{folder}/.")

    chapters = list((ROOT / "docs/canonical_md").glob("Chapter *.md"))
    found = []
    for chapter in chapters:
        match = re.match(r"Chapter (\d+)\s", chapter.name)
        if match:
            found.append(int(match.group(1)))
        else:
            issues.append(f"Unrecognized manuscript chapter filename: {chapter.name}")
    require(sorted(found) == [1, *range(4, 31)],
            "Active chapter inventory is not exactly merged Chapter 1 and Chapters 4–30.")

    base = ROOT / "beta_readers/editions/2026-10-07-v2"
    manifest_path = base.with_suffix(".json")
    verification_path = ROOT / "beta_readers/editions/2026-10-07-v2.verification.json"
    delivery_path = ROOT / "beta_readers/editions/2026-10-07-v2.delivery.json"
    if not all(path.is_file() for path in (manifest_path, verification_path, delivery_path)):
        issues.append("The frozen v2 release manifests or records are missing.")
    else:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        verification = json.loads(verification_path.read_text(encoding="utf-8"))
        delivery = json.loads(delivery_path.read_text(encoding="utf-8"))
        require(manifest.get("edition_id") == "2026-10-07-v2", "Unexpected historical edition ID.")
        require(manifest.get("source_commit") == "c41140b00b9fe348f546ada77a9143413ae5894e",
                "Frozen v2 source checkpoint changed.")
        sources = manifest.get("sources", [])
        require(len(sources) == 31, "Frozen v2 has an incomplete source inventory.")
        require([x.get("role") for x in sources] == ["chapter"] * 28 + ["appendix"] * 3,
                "Frozen v2 source roles/order changed.")
        require(len({x.get("path") for x in sources}) == len(sources),
                "Frozen v2 source inventory contains duplicate paths.")
        for source in sources:
            require((ROOT / str(source.get("path"))).is_file(),
                    f"Frozen v2 source path no longer exists: {source.get('path')}")
        pdf = ROOT / str(manifest.get("output", {}).get("path", ""))
        expected = verification.get("output_sha256")
        require(pdf.is_file(), f"Historical beta PDF missing: {pdf}")
        if pdf.is_file():
            actual = digest(pdf)
            require(actual == expected, "Historical v2 PDF differs from verified SHA-256.")
            require(actual == delivery.get("attachment", {}).get("sha256"),
                    "Historical v2 delivery record and PDF hash disagree.")
        require(verification.get("source_commit") == manifest.get("source_commit"),
                "Historical v2 manifest and verification source commits disagree.")
        require(verification.get("chapter_count") == 28
                and verification.get("appendix_count") == 3,
                "Historical v2 verification inventory is incomplete.")
        for old in manifest.get("superseded", []):
            old_path = ROOT / str(old.get("path", ""))
            require(old_path.is_file(), f"Superseded historical export removed: {old_path}")
            if old_path.is_file():
                require(digest(old_path) == old.get("sha256"),
                        f"Superseded historical export changed: {old_path}")

    if issues:
        print("FAIL — Hive repository integrity:")
        for issue in issues:
            print(f" - {issue}")
        return 1
    print("PASS — one canonical Markdown chapter source (28 chapters).")
    print("PASS — legacy DOCX archive retained; no second canonical folder.")
    print("PASS — immutable beta v2 manifests, existing exports and PDF SHA-256.")
    print("PASS — beta/proofs/published edition stages exist.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
