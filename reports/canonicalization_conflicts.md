# Canonicalization Conflicts

Phase 2 gate failed because at least one chapter is `DIVERGENT`.

## Conflicts
- Chapter 1: first mismatch at main.tex:~23 (chapter-block line ~1) vs chapters/ch1.tex:~1.
- Chapter 2: first mismatch at main.tex:~58 (chapter-block line ~1) vs chapters/ch2.tex:~1.
- Chapter 3: first mismatch at main.tex:~91 (chapter-block line ~1) vs chapters/ch3.tex:~1.

## Recommended Resolution Path
1. Choose canonical source per divergent chapter (`main.tex` block or `chapters/chN.tex`).
2. Reconcile text exactly (no prose rewrite), then re-run the audit.
3. Apply include wiring only after all chapters are non-divergent.

Phase 2 halted due to divergence. No manuscript files modified.

