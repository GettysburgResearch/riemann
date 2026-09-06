# Reviewer D — integrated-main re-audit

Status: completed first pass at an explicitly partial coverage boundary.
Scope: already integrated main, not the post-707 scientific review.
Baseline: `8d16f8d9c475db290bc85e53d775b93b9bcdb336`.
Branch: `review/D/20260905-integrated-main-reaudit`.
RH: no proof or disproof; no main/source/canonical/formal changes.

Read [REPORT.md](REPORT.md), then [REPAIRS.md](REPAIRS.md).
[CLAIMS.tsv](CLAIMS.tsv) gives 74 component dispositions;
[EDGES.tsv](EDGES.tsv) separates valid, conditional and broken transfers.
[COVERAGE.tsv](COVERAGE.tsv) accounts for the full 139-row canonical denominator
without pretending that all those rows were independently reviewed.
[SOURCES.tsv](SOURCES.tsv) contains 67 exact inspection pins, including 46
mathematical source files and 21 main metadata/contract files.

Seven concrete findings include a varying-order filter counterexample, a
spectrum/eigenvalue error, a wrong principal-minor sentence, a wavelet energy
mismatch, two lost integration contracts and a missing excursion boundary
term. Three further norm/domain/uniformity contracts are made explicit.

The wavelet criterion is not discarded: a complete separate suffix-field
proof repairs the literal old normalization. Neither energy bound nor RH is
proved. Existing Xi multiplicity, Hardy truncation and Julia-margin repairs
remain binding rather than being relabeled new discoveries.

[VALIDATION.md](VALIDATION.md) records 45 named independent bounded checks,
9,380 fixtures in each Python mode, strict corruption refusals and limitations.
The checker needs Python 3 and SymPy; the tested versions are recorded there.

```sh
python checks.py --check checks.normal.json
python -O checks.py --check checks.optimized.json
python validate.py
sha256sum -c SHA256SUMS
```

All edits are confined to `reviews/D/`. Review recommendations do not themselves
change canonical acceptance. The same assistant's new reviewer designation is
not a claim of an external referee or absence of every authorship overlap.
