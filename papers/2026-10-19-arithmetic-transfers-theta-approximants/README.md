# Zero-free regions, character averages, and approximations to the Riemann xi function

**Revised manuscript — 19 October 2026.** Gettysburg Research · Agentic Polymath project.

The revised 49-page paper explains the zero-free proposals and their mathematical context before developing the character-average, Möbius, theta, and determinant arguments. It replaces the original 36-page editorial version in the same manuscript directory. It is not a merger of the research branches or an approval of their analytic claims.

## What changed

The new Section 2 covers the two OpenAI manuscripts, Cureton–Thorner's reported 31/32 all-field result, and the repository proposals 23/24, 25/27, 11/12, 91/100, 109/120, 10/11, 9081/10000, 49/54, the archived 68/75, and the 19/21 and 271/300 comparisons. It explains the gains from zero-density stratification, numerator averaging, shorter support, fourth moments, and the enlarged correction domain. The ordinary-zeta and all-number-field settings are not conflated.

Later work is also included: note #1005's explicitly import-dependent 0.87488666 corollary, the related quartic attempts in #1006, and #1008's finite-jet zero-insertion obstruction. The conditional gain in #1005 is stated at its actual size, 4 × 10⁻⁸ relative to its cited Xu–Sang value. The unproved mixed-mean target in #1006 is not presented as an achieved region.

The introduction and section openings now explain the mathematical questions in ordinary prose. Technical derivations, quantifiers, and the distinction between finite matching and all-order existence are retained. The author appears on the title page only; all later pages have page numbers without author headers. Gettysburg Research and the Agentic Polymath project appear on the title page, and the closing acknowledgment expressly records AI assistance, including GPT 6 Pro.

## Build and download package

`main.tex` is the entry point. The eleven files under `sections/` contain the text, `main.bbl` is the ready-to-use bibliography, and `references.bib` is its editable counterpart.

```sh
python -I -S -B verify_paper.py
python build.py
python build.py --arxiv recent-zeta-contributions-v2-arxiv.zip
```

The build needs a standard pdfLaTeX installation with AMS packages, Latin Modern, geometry, microtype, hyperref, and booktabs. It uses three no-shell-escape passes, needs no network or research-packet checkout, and writes `main.pdf`. The clean arXiv source archive contains 14 source files; it excludes the PDF, build products, and font files. The compiled PDF and complete package are supplied in the accompanying conversation. Repository publication here concerns the editable source and checks; no arXiv submission has been made.

## Evidence and attribution

`SOURCE_LOCK.json` records 26 immutable research versions and the exact reading scopes, plus the external references used for the expanded history. Several historical entries were read at detailed PR-statement scope, not as fresh analytic audits. Fresh primary-body retrieval of the cited Liu and Xu–Sang versions was unsuccessful, so their versions, values, and hypotheses are reported through the pinned repository accounts.

`PAPER_CHECKS.json` is the output of 972 finite arithmetic and editorial checks. They do not verify the infinite analytic proofs. `REPLAY_RECEIPTS.json` preserves the first version's original packet replays; those historical runs are not represented as fresh revision runs. `VALIDATION.md` records this revision's checks, compilation, and PDF inspection. `CLAIM_LEDGER.md` and `AUTHOR_REVIEW.md` distinguish the types of claims and remaining review obligations.

No new zero-free region is proved by this editorial revision. The proposed analytic compositions, finite certificate claims, and open all-order estimates retain their source qualifications. Independent mathematical review and human approval of authorship, attribution, and submission remain necessary.
