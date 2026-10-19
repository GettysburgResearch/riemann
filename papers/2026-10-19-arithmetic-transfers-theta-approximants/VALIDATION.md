# Revision validation — 19 October 2026

This record applies to the revised 49-page manuscript. It does not reclassify the source research as independently accepted mathematics.

## Checks performed for this revision

- `python -I -S -B verify_paper.py` and `python -I -S -O -B verify_paper.py` pass with byte-identical output. The report contains 972 finite arithmetic/editorial checks, including the inherited 850 rational middle-class comparisons, historical Mellin sums, the selected-density gain, the conditional #1005 boundary and preceding-stage equality, four finite conjugate-node fixtures, local LaTeX inputs, 126 unique labels, 41 bibliography entries, and 26 source pins.
- The bibliography keys in `main.bbl` and `references.bib` agree. All LaTeX citations and cross-references resolve. Every linked research source uses a 40-character immutable commit, not a moving branch.
- Three pdfLaTeX passes with `-no-shell-escape` succeed. There are no overfull boxes or undefined references. The ordinary disabled-shell-escape package warning is expected and does not indicate a build failure.
- A clean 14-file arXiv source ZIP was extracted into a separate directory and compiled in three passes. Every page has the same extracted text as the main build. The archive contains no PDF, font file, or transient build product.
- The 49-page PDF was rendered for layout inspection. Contact sheets cover the full manuscript; title, progression tables, technical tables, and the closing page were also checked separately. After the final table/header refinements, selected affected pages were rendered again, and a full-page text-coordinate check found no horizontal text outside the prescribed text area.
- PDF text inspection confirms that the author's name occurs visibly on page 1 only; the Gettysburg Research and Agentic Polymath project credits appear on the first page; the explicit GPT 6 Pro acknowledgment appears at the end, on page 49. Page numbers replace the old alternating author headers.

The checks cover finite arithmetic, source/editorial consistency, and document production. They are not an independent verification of the infinite analytic estimates, the original theta source integrals, or the five original certificate cubes.

## Source and review limits

The original thirteen source locks and the v1 `REPLAY_RECEIPTS.json` are preserved as historical records. Their recorded runs are not claimed as new executions in this revision. The original #1003 full theta integration and parameter-cube campaigns, #1005's complete originating checker, and #1006's large experiment collection were not rerun.

The expanded historical account reads the detailed live PR statements for #957–974, including overlap and recovery qualifications. The #959 source-identity note, the complete #1005 uniform-boundary argument, and the qualitative finite-jet insertion proof in #1008 were additionally read at the scopes recorded in `SOURCE_LOCK.json`.

The two OpenAI scopes were checked against the pinned primary repository: the September 30 metadata and formalization-scope document, and the October 5 introduction and main theorem. Fresh primary-body retrieval of the Liu and Xu–Sang versions was unsuccessful. Their versioned claims are therefore reported through the pinned research notes, not as fresh primary verification. The Cureton–Thorner formalization is reported by its project; no Lean build or axiom audit was performed here.

No separate research agent, independent human referee, new analytic theorem, repository-wide validator, remote CI execution, arXiv submission, or merge into main is claimed by this revision.

## Reproduce

```sh
python -I -S -B verify_paper.py
python -I -S -O -B verify_paper.py
python build.py
python build.py --arxiv manuscript-v2-arxiv.zip
```

`SHA256SUMS` binds the revised text and data files. `REVISION.json` records the delivered PDF and source-ZIP hashes; PDF metadata may change on a later rebuild. Remote publication is recorded separately after a successful commit and branch readback.
