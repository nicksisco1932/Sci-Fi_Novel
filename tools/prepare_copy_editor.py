"""Validate package inputs and prepare a proposal-only copyedit review ledger."""
from __future__ import annotations

import argparse
import json
import re

from build_reader_package import ROOT, digest, local_path, validate_sources


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", required=True, help="Fresh review name, using letters, digits, dots, underscores or hyphens")
    parser.add_argument("--config", default="docs/reader_package/package.json")
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,79}", args.run):
        raise ValueError("Invalid review run name")
    if args.run.split(".", 1)[0].upper() in {"CON", "PRN", "AUX", "NUL", *[f"COM{i}" for i in range(1, 10)], *[f"LPT{i}" for i in range(1, 10)]}:
        raise ValueError("Reserved review run name")
    config_path = local_path(args.config)
    raw = config_path.read_bytes()
    config = json.loads(raw)
    sections, provenance = validate_sources(config)
    guidance = []
    for name in ["AGENTS.md", "COPY_EDITOR_AGENT.md", "docs/copy_editor/README.md",
                 "docs/copy_editor/style_sheet.md",
                 "docs/developmental/manuscript_style_tests/style_guide_v0.2.md"]:
        guidance.append({"path": name, "sha256": digest(local_path(name).read_bytes())})
    ordered = []
    for section in sections:
        if section["kind"] == "chapter":
            number = int(section["key"].split("-")[1])
            candidates = [p for p in local_path(config["manuscript_folder"]).glob("Chapter *.md")
                          if re.match(rf"^Chapter {number}\s+[–-]", p.name)]
            if len(candidates) != 1:
                raise ValueError(f"Source location is ambiguous: {section['key']}")
            source = candidates[0].relative_to(ROOT).as_posix()
        else:
            source = next(s["path"] for s in config["supporting_sections"] if s["key"] == section["key"])
        source_record = next(s for s in provenance if s["path"] == source)
        ordered.append({"section": section["key"], "title": section["toc"],
                        **source_record, "review_status": "pending"})
    out = local_path(f"docs/copy_editor/runs/{args.run}")
    if out.exists():
        raise ValueError("Review run already exists; preserve its findings and choose a fresh name")
    # Complete source and guidance validation above before creating any run output.
    out.mkdir(parents=True)
    inputs = {"status": "prepared", "mode": "proposals-for-author-review", "run": args.run,
              "config_path": config_path.relative_to(ROOT).as_posix(), "config_sha256": digest(raw),
              "config": config, "guidance": guidance, "sources": ordered,
              "source_changes_applied": False}
    records = {
        "inputs.json": json.dumps(inputs, ensure_ascii=False, indent=2) + "\n",
        "findings.json": json.dumps({"status": "not-started", "findings": []}, indent=2) + "\n",
        "review.md": f"# Copy Editor Review — {args.run}\n\nStatus: prepared; no sections reviewed and no findings assessed.\n\nFollow COPY_EDITOR_AGENT.md.\n",
        "coverage.md": "# Copy Editor Coverage\n\nStatus: prepared; every section awaits review.\n\n| Section | Source | Status | Finding IDs / retention notes |\n|---|---|---|---|\n" + "".join(
            f"| {s['title']} | `{s['path']}` | Pending | |\n" for s in ordered),
    }
    for name, text in records.items():
        (out / name).write_text(text, encoding="utf-8", newline="")
    print(json.dumps({"run_directory": str(out), "sections": len(ordered),
                      "status": "prepared", "reviewed_sections": 0, "source_changes_applied": False}))


if __name__ == "__main__":
    main()
