# A: second-pass omissions report

Read `REPORT.md`, `CLAIMS.tsv`, `EDGES.tsv`, and `FIXES_AND_EXTRACTION.md`.
These four follow-up deliverables supplement the parent review at
`e44b6d072ac82d014717454635df96da9c0e115f`; they do not erase its history.

There are 30 new scoped dispositions, 20 new exact source records and 15 new
implication records. Join this `SOURCES.tsv` to the parent source table, then
join both claim/edge ledgers. The combined inventory has **158 dispositions,
112 source records and 73 edges**. Counts are not acceptance counts.
`OMISSIONS_RECONCILIATION.tsv` supplies explicit precedence for the 18 former
coverage/hold categories. An old statement that a computation was not run is
historical; the supplement execution receipt records only the fresh runs.

Run `python reviews/A/supplement/validate_supplement.py` from the repository
root to validate the composite inventory and receipts. The full kernel
certificate is reproducible with
`python reviews/A/supplement/replay/seven_independent_cached.py OUTPUT.json`.
It is an exhaustive finite proof computation, not a routine metadata check.
The parent final validator still checks the complete current file manifest.
No RH proof, unperformed Lean build or non-author acceptance is asserted.
