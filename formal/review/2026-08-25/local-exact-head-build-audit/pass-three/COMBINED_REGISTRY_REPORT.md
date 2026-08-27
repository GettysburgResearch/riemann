# Combined registry report

The normal generator and validator pass on combined tree
`bd621c02db310fc318ee287eefeb6e2c76c8b48a`.

- Canonical claims: 139
- Unique canonical IDs: 139
- Combined delta rows: 31
- `STATED`: 2
- `PROVED`: 10
- `PROVED_CONDITIONAL`: 8
- Blueprint fragments: 3
- Analysis locks: 6
- Upstream locks: 5

The first normal generation attempt correctly failed on a duplicate canonical
ID: A and B both carried a row for
`API.MELLIN.SUBPOWER_NEGATIVE_MASS`. A's row is nonempty,
`PROVED_CONDITIONAL`, and names
`fixedDetector_negativeMass_implies_RH`; B's row was a blank/deferred
reservation. The rehearsal removed only B's blank duplicate and left A's row
byte-for-byte unchanged. All other A and B rows remain unchanged, and B retains
11 nonempty declaration rows.

No post-#707 research was imported and no status was promoted to make the
registry pass.

Verdict: `PASS`.
