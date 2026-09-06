# Reviewer D — third wide-pass supplement

Audited main: `8d16f8d9c475db290bc85e53d775b93b9bcdb336`.
Review parent: `3c1fd241032e87377088a209ff3f008624fad315`, PR #799.
The two older sibling packets `../D/` and `../D-final/` are unchanged.

Start with `REPORT.md`, then `PROOFS_AND_REPAIRS.md`. New finding labels are
D-F12–D-F15 and proof reconstructions R16–R24. Not every qualification is a
new mathematical failure: net-pole cancellation already appears in the
successor, and the gauge correction concerns the unactivated range.

`CLAIMS.tsv` contains 42 scoped dispositions at exact source SHA/path/claim;
`EDGES.tsv` contains 45 dependency/transfer edges. `SOURCES.tsv` has 29
inspection pins. `COVERAGE.tsv` accounts for all 139 canonical rows through
24 family counts plus four legacy/metadata rows, without claiming all rows
proof-reviewed. Eight families receive additional focused primary review.

`checks.py` independently reconstructs bounded exact controls, including the
complete 60-coefficient annular kernel object and the one actual P61 endpoint
X=184. It imports no upstream producer. Analytic proofs are not machine
verified. See `VALIDATION.md` for execution and trust boundaries.

`validate.py` authenticates this directory's manifest and declared inventory;
it does not refetch source blobs or prove their theorems. All source identities
were recorded from GitHub exact-ref reads. See `EXTERNAL_INPUTS.md` for the
background input contracts. The publication receipt is outside the committed
directory so it can name the final commit without self-reference.

Integration is by scoped repair under new identities, not overwriting old
source proofs. No RH-bearing arithmetic sign, global producer, zero census,
large historical campaign or formal build is claimed by this supplement.
