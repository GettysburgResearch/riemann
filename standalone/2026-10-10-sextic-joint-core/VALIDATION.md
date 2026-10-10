# Validation and proof boundaries

Date: 2026-10-10. This is a proposed standalone research packet. Validation of files and a scoped mathematical review do not establish the full inverse moment conjecture, an improved zero-free boundary, or RH.

## Written mathematics and independent review

| Claim | Proof or audit | Independent review scope |
| --- | --- | --- |
| Combined one-sided incidence and global-conductor residual reduction | DOUBLE_RESIDUAL_REDUCTION.md | DOUBLE_RESIDUAL_REVIEW.md, author and reviewer distinct; exact polynomial selection, positivity order, subset accounting, uniform constants, and strictness witnesses |
| Finite A2-to-mixed-theta composition, logarithmic norm transfer, uniform classical envelope | INTERFACE_COMPARISON.md | INTERFACE_REVIEW.md, author and reviewer distinct; exact coefficients, scale normalization, zeros, moving auxiliary overlap, cube inversion, and all-row sieve application |
| Exact signed first-Poisson diagonal and its relation to the large-value Gram diagonal | SIGNED_DIAGONAL_INTERACTION.md | Independent audit of the pinned PR #914 source against its imported Poisson identity; bounded to the signed-diagonal theorem and the distinct Gram objects |
| Overview and conditional boundary implications | README.md | README_REVIEW.md; theorem scope, normalization, moment quantifiers and the distinction between original and transformed row ranges |

The new author/reviewer roles are AI research agents. Their reports bind the reviewed proof bytes with SHA-256 hashes. The root agent also read the complete new mathematical notes and checked the main normalizations independently. This is not human peer review, integration approval, or a Lean proof.

The double residual argument retains the imported native second moment as an analytic input. Its optional pointwise exponent below one must be uniform in the moving row and smaller column scale. The mixed-family baseline uses PR #913's all-row squarefree-column sieve. Its exact finite projection requires the arithmetic identities recorded in SOURCE_LOCK.json, rather than a new analytic continuation theorem.

## File and source verification

The publishing pass checks all of the following against the frozen packet:

- Every manifest entry matches its file's byte length and SHA-256 hash.
- Both adjacent source snapshots match their original Git objects byte-for-byte.
- Every SOURCE_LOCK.json entry matches its exact source commit, path, Git blob identity, byte length and SHA-256 hash.
- The proof hashes stated in the independent reports match the actual copied proof files.
- Authored Markdown has paired inline and display math delimiters, no unexpected control bytes, and valid relative file links. Verbatim source copies are excluded from relative-link rewriting; their original directory context is documented in sources/README.md.
- JSON parses, authored text ends in a newline, and the staged patch passes git diff --check.
- The publication changes only this new packet and the root README navigation. All previous source and proof packets retain their exact bytes.
- The remote commit's parent and tree are compared with the intended parent and locally staged tree. Every changed file is compared byte-for-byte with the staged payload, and the manifest is checked again at the remote commit before completion is reported.

MANIFEST.json binds every packet file except itself. The two-file source manifest has its own source metadata and is also covered by the packet manifest. SOURCE_LOCK.json is a dependency lock, not a claim to have independently rebuilt every imported theorem.

The first complete byte scan located one existing form-feed in the verbatim A2 source, at zero-based offset 13449. Its exact location and the independently rederived scale formula are recorded in sources/README.md. The source copy remains byte-identical; this known source-formatting defect is explicitly distinguished from the clean authored files.

## Computation not claimed

No new numerical asymptotic experiment, zero census, finite-field theorem test, certified interval calculation, or Lean build was used for these two combinations. The mathematical checks here are complete written derivations and independent proof review. The separate exact local checks published with PR #915 keep their original scope; they were not rerun or relabeled as validation of the new global reductions.

The signed residual is not bounded by the new reduction. The uniform classical mixed-family envelope is proved, while the stronger reflected or centered estimate remains open. The auxiliary Möbius cancellation in the signed Poisson diagonal does not remove the different positive character-row diagonal in the existing high-value argument. No finite check or file verification is presented as resolving those gaps.
