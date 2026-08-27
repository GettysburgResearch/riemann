# Independent C delta audit

The diff from `b20ee9b3678e5d8fa32b04b156bc02cec782a97b` to
`381a5a98ade7c6bad7122e5182c2fc07332dc747` was inspected independently before
the final exact-head run.

The only mathematical declaration-type changes are the two approved
`Nonempty (ActualXiReserveAllocation ...)` conclusions recorded in
`B_C_STATEMENT_ADJUDICATION.md`. No premise was added. The actual-Xi
order-three comparator type is unchanged, retains all repeated-node cases, and
concludes PSD only.

Other changes are proof bodies, computability/notation support, LF source-lock
materialization, comparator packaging, audit coverage, and parser robustness.
`buildActualXiReserveAllocation` is a `noncomputable def` with the same explicit
data-returning type. Removal of a generated `Repr` derivation from `Jet2` is not
a mathematical theorem-type change.

Scans found no new `sorry`, `admit`, custom `axiom`, `opaque`, or `unsafe`
declaration in trusted, ChallengeDeps, or Solution sources. The final exact C
suite and the later combined suite both passed.

Verdict: `PASS_STATEMENT_BOUNDARY_AUDIT`.
