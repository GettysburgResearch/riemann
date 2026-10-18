# Arithmetic transfers, finite theta approximants, and obstruction estimates for zeta functions

**Author draft — 19 October 2026.** This is an additive manuscript, not a merge or approval of the underlying research branches. It covers selected recent contributions through the immutable sources in PRs #1003 and #1004, including their predecessors. No RH proof or new global ordinary-zeta zero-free region is claimed.

## Read and build

`main.tex` is the manuscript entry point. `sections/` contains its ten source chapters; `main.bbl` is the pre-generated bibliography and `references.bib` is the corresponding editable bibliographic data. The PDF can be built without BibTeX, shell escape, external downloads, or a checkout of the research packets:

```sh
python -I -S -B verify_paper.py
python build.py
```

The build requires a standard TeX installation with pdfLaTeX, AMS packages, Latin Modern, geometry, microtype, hyperref, and booktabs. It runs pdfLaTeX three times, checks references and overfull boxes, and writes `main.pdf`. The mathematical checker uses only Python's standard library. On a system without Python, run `pdflatex -no-shell-escape main.tex` three times.

Create a clean, source-only arXiv upload archive with:

```sh
python build.py --arxiv recent-zeta-contributions-arxiv.zip
```

The archive contains `main.tex`, all local section files, `main.bbl`, and `references.bib`; it excludes the generated PDF, logs, auxiliary files, and fonts. The repository contribution preserves editable source and build instructions. The compiled PDF is also delivered in the accompanying conversation. No arXiv upload or submission has been performed.

## Mathematical contents

The main text gives detailed proofs of the uniform primitive quadratic-field coefficient comparison, actual quadratic-family residual transfer and optimal auxiliary-variance removal, the elementary two-mollifier theorem, complete native denominator/core and frequency-sector estimates, weighted canonical and strip compactness statements, controlled negative Ising couplings, paired scale filters, and primitive positive-determinant regularization.

It presents the five source-certified real-zero approximants matching theta Taylor orders 22, 24, and 26, with the exact normalization, parameter-cube mechanism, and complete-source remainder formulas. These are finite certificates, not an unbounded-order theorem. The original order-26 certification campaigns were not rerun for this editorial compilation.

The proposed all-field `271/300` composition and real-zero prime-bias consequence are explicitly source-qualified. The failed `0.87` comparison is an exact obstruction within its specified estimate system, not an actual zeta-zero assertion or a general impossibility theorem.

## Provenance and review

- `SOURCE_LOCK.json`: thirteen immutable research heads, principal file paths, recorded blob identities, and exact reading/replay scopes.
- `CLAIM_LEDGER.md`: classification of the paper's principal results, source contracts, and missing conclusions.
- `PAPER_CHECKS.json`: output of the 921-predicate finite arithmetic/editorial check. This is not an analytic proof certificate.
- `VALIDATION.md`: actual fresh replays, compile and visual-inspection scope, and limitations.
- `AUTHOR_REVIEW.md`: author, attribution, mathematical-review, and submission decisions that remain with the human author.

Some original packets contain historical `remote_publication: false` literals. Those are frozen source-report fields, not current GitHub queries; their separate publication notices supersede publication status only. The manuscript does not edit any source packet or its historical report.

Substantial AI assistance is disclosed in the paper. A clean build and finite checks do not establish novelty, certify every imported analytic contract, or replace human author approval or independent mathematical review.
