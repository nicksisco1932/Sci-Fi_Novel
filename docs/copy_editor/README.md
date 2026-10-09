# Copy Editor workflow

The Copy Editor is a reusable Codex role defined in `COPY_EDITOR_AGENT.md`. The author selected proposals for review as its first-pass mode. Building this workflow does not start a copyedit or change manuscript prose.

## Start a review

Read the role brief and style sheet. From the repository root:

```powershell
& 'C:/Users/nicks/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe' -B tools/prepare_copy_editor.py --run v0.2_first-review
```

The command checks all pinned package input hashes before writing its run files, records the package configuration and guidance, and initializes the 32-section coverage ledger. Choose a fresh run name for each review. It does not make editorial judgments or apply corrections.

Use this instruction to invoke the role in the existing chat:

> Act as the Copy Editor using COPY_EDITOR_AGENT.md. Review the sources pinned in docs/reader_package/package.json in reading order, including the author's foreword and all appendices. Prepare the v0.2_first-review run if it does not already exist; otherwise validate its hashes before continuing. Produce exact proposed corrections and author queries for my review, with a completed coverage ledger and machine-readable findings. Preserve source prose and the completed v0.2 experiment.

## Run records

Each `docs/copy_editor/runs/RUN_NAME/` contains:

- `inputs.json`: exact configuration, ordered source paths and SHA-256 values, guidance hashes, and status `prepared`.
- `coverage.md`: every selected section starts as pending; fill it during actual review.
- `findings.json`: review status, findings, and author dispositions. An empty prepared list means review has not started.
- `review.md`: summary of actual review work and before/after proposals. Its initial status is explicitly unreviewed.

Each finding uses these fields:

```json
{
  "id": "CE-0001",
  "section": "chapter-1",
  "source_path": "exact path from inputs.json",
  "source_sha256": "exact hash from inputs.json",
  "line": 1,
  "paragraph": 1,
  "anchor": "exact source quotation",
  "category": "spelling|grammar|punctuation|consistency|reference|continuity|formatting",
  "kind": "mechanical|consistency-choice|author-query",
  "confidence": "high|medium|low",
  "before": "exact source wording",
  "after": null,
  "query": "question when a correction is not justified",
  "reason": "specific explanation",
  "evidence": [],
  "meaning_risk": "effect or uncertainty to consider",
  "disposition": "pending"
}
```

For a correction, fill `after` with the minimal proposed replacement and set `query` to null. Line and paragraph numbers are one-based positions in the raw Markdown, not PDF coordinates. Preserve quoted punctuation and Markdown when storing anchors. Do not populate this example as a real finding.

## Later acceptance

Author approval applies to selected findings. Apply those findings to a new version after confirming source integrity; preserve frozen reading versions, review records, and package editions. Pending or rejected findings remain unapplied. Name the author **Nicholas J. Sisco** in new reading copies and metadata.
