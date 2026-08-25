# Combined reconciliation rehearsal

Status: `NOT_RUN_GATE_FAILED`

The required precondition was: create the combined worktree **only if all three individual trusted libraries build**. That precondition failed at the immutable source heads before any combined worktree was created:

- Reviewer A `9ed8988218fd9c3e1da33bde81361262fc0aa747`: `lake build` exited 1.
- Reviewer B `072b4dbd0e4e407728a59110eb4f7214e23f8f8d`: `lake build` exited 1.
- Reviewer C `b20ee9b3678e5d8fa32b04b156bc02cec782a97b`: `lake build` exited 1.

The failures include deterministic source/package-graph errors, not only later environmental cascades. Consequently no A/B/C reconciliation, conflict resolution, combined registry generation, combined comparator build, combined axiom audit, or advisory integration patch was attempted. This preserves the instruction not to create the fourth worktree when an individual trusted library does not build.

`COMBINED_REHEARSAL.patch` is intentionally absent. The individual statement-preserving mechanical proposals are retained under `patches/`; none was treated as if it changed an exact-head verdict.
