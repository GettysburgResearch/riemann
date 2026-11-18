# Equivalence track checkpoint — 2026-11-17

Completed: full source texts downloaded and read for three works, with original metadata and hashes in papers/equivalence_records.jsonl. Stable IDs PAPER-E001 (Báez-Duarte math/0205003v1), PAPER-E002 (Burnol math/0103058v2), PAPER-E003 (Bettin–Conrey–Farmer1211.5191v1). Six theorem/exercise records and one cross-paper connection record. Complete-paper audit counts: L0 metadata verified=3; L1 substantive reading=3; L2=0; L3=0. Local finite polynomial derivations have proofs and exact rational experimental checks, awaiting independent parent review.

Source PDFs/text are private working copies for reading. Packaging should exclude the entire sources directory unless independently licensed for redistribution. Source URLs and SHA256 remain in paper records. An unrelated probe PDF was downloaded as nb_probe.pdf before identity verification; it is not counted, selected, or read. Remove before packaging.

Methods: web primary-source search then urllib download; pdftotext -layout for complete reading; arXiv abstract pages for exact versions and dates. Shell requests module absent, urllib successful. Bombieri–Lagarias author PDF returned403 in shell; web extraction was unusably garbled; no substantive Li audit is claimed by this track.

Reproduction: from archive root run `python experiments/code/multiple_root_smoothing.py`. Standard library only; uses exact fractions and Parseval coefficients. Proof is in proposals/independent_campaigns/multiplicity_adapted_smoothing.md.

Additional accessed source: Werner Ehm2405.06349v2, partial inspection of p.1 and §8 only; not counted as substantive whole-work reading. Potential quantifier issue in p.1 fixed-coefficient convergence statement remains unresolved, with external result search incomplete. No author-error assertion permitted.

Search coverage: 2024–2026 NB searches found many unreviewed recent claims. They are not treated as established mathematics. arXiv2405.06349 was accessed from primary repository. No claim of current comprehensive frontier coverage.

Continuation: (1) independent verification of elementary double-root proof; (2) exact clustered simple-root transition; (3) verify fixed Selberg-sequence convergence literature before interpreting Ehm p.1; (4) read journal versions/corrections; (5) obtain accessible Bombieri–Lagarias original if Li theorem audit needed.

Update: PAPER-E004 partial record added (not L1). Eight theorem/exercise records, two connection records. Cluster campaign derives exact2x2 Gram expression, c/N transition F(c), and noncommuting limits. Exact rational-complex checks executed for25 finite parameter choices, validating unit modulus, both interpolation constraints, every normal equation, and squared norm. Float profile columns are explicitly unvalidated exploratory numbers. See clustered_root_transition.md.

Update: THM-E009 supplies an exact failure of uniform triangular smoothing for moving simple roots. Twenty finite rational-circle cases checked (four each at N=0,1,2,5,20); optimal equations all exact, window equations checked at the sixteen cases with N>=1. Earlier mention of25 cases was a counting typo; actual total is20.

Uniform remainder campaign completed: THM-E010 proves sup_|c|<=C |L E_N(c/L)-F(c)|<=38(12+C²)²/L for allN>=0, includingc0 and actual double-root aliases. Stable divided-difference Gram basis, uniform determinant bound1/(12+c²), and explicit endpoint quadrature. Advocate and parent independently agree; advocate obtained a sharper18B² constant, but campaign retains38.887 exploratory double-precision cases pass; these are unvalidated stress tests and not proof. No additional paper reading claimed.
