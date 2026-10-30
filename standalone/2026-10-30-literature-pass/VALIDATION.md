# Validation and review scope

Date: **30 October 2026**. This is a documentation-only literature contribution. The checks below assess bibliographic consistency, provenance and the accuracy of the annotations; they do not certify external mathematics.

## Source and editorial review

Three independent research lanes reviewed the final draft against their primary-source notes: zero-free/arithmetic results, analytic moments/density, and spectral/positivity/formalization. The review retained exact family, hypothesis and verification qualifications.

The final corrections include:

- Correcting the verified author name to **Alexandre de Faveri**.
- Stating the bounded-coefficient normalization and parameter range of L04.
- Identifying the function and real-zero interval in L10, and the real-valued character/nonunit-conductor restrictions in L11.
- Preserving multiplicity and the **OR** in L16's proportion statement.
- Describing L14's inspected assembly/type checks without claiming inspection of an exported proof closure.
- Restricting the proposed height-100/Sra comparison to conclusions using that height, not PF256's much larger input height.
- Describing L27's 34.1-to-34.4 change as an improvement, not a correction of a false theorem.
- Separating author-site, Hexagon, arXiv, journal and repository version identities.

For L01, the compact JSON extraction was checked against the original protected admission record and live PR metadata. Its source head, exact rational, merge time, kernel names, canonical target, allowed axioms, preflight fields and receipt hash agree with those upstream records. A cached web page's stale open status was resolved using the live API.

## Mechanical checks

The local validation checks require:

1. Both JSON files parse; `SOURCES.json` has 28 unique, consecutive IDs L01–L28.
2. Every ID and title has one matching catalogue heading and BibTeX citation key.
3. Record dates and retrieval dates are valid and do not exceed the stated cutoff; later seminar context is labeled separately in prose.
4. Every relative Markdown link resolves to a file in this packet; external bibliography URLs are syntactically valid HTTPS locators.
5. BibTeX entry delimiters and fields balance, authors/titles agree with the structured bibliography, and Hexagon identifiers are not encoded as arXiv eprints.
6. The exact rational `43670599/50000000` equals `0.87341198`; its difference from the inspected repository candidate `0.8738694` is `0.00045742`.
7. The packet contains only the eight intended text files, with no vendored manuscripts, credentials, build outputs or proof dependencies.

The publication step also compares Git blob hashes for the uploaded files, checks the branch head and the remote diff, and records the resulting commit and PR. These remote publication checks are reported with the PR rather than represented as an external proof run.

## Deliberate limits

No repository theorem, formal proof, dependency closure or numerical computation was changed. No Lean, NanoDa, con-ron, interval-arithmetic census, Schur certificate or external analytic proof was rerun. Accordingly, a full repository proof/test suite was not invoked for these eight text files.

“Inspected” refers to the source depth stated per entry. Abstract-only leads remain abstract-only. Author-reported checker acceptance remains distinct from an inspected protected admission receipt. The bibliography does not turn an unresolved source interface into a discharged hypothesis.

The exact repository baseline and inspected draft heads are in [REPO_MAP.md](REPO_MAP.md); search and access limits are in [SEARCH_LOG.md](SEARCH_LOG.md). The proposed follow-up tasks have explicit acceptance conditions so that a future import can be reviewed on its own evidence.
