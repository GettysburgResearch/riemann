# Integration handoff

## Frozen objects

```text
bootstrap: 573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f
Reviewer A PR: #734
Reviewer A head: 92f70a3b49b9295b5efb88491107670065b03317
Reviewer C review PR: #747
review branch: formal/review/2026-08-24/c-cross-a
```

Do not modify or merge PR #734 from this review branch.

## Safe salvage

The following can be reconciled after a clean build:

* Mathlib RH/zeta/completed-zeta adapters;
* Zeta23 zero, multiplicity, finite-window, centered-coordinate and reflection adapters;
* standard Mellin dilation/two-term linearity/compact power-kernel/strip holomorphy;
* generic fixed holomorphic-defect and nonvanishing-multiplier singularity transfer;
* reciprocal meromorphic-order inversion;
* conditional reflection closure;
* the upstream reuse ledger's positive matches and its rejection of name-only Landau matching.

## Blocking repairs

1. Restore/fix `zeta23_bridge_preserves_RH` audit compatibility.
2. Replace both open analytic propositions with exact tail-transform statements.
3. Add the complete `PROVED_CONDITIONAL` consumer ending in `RiemannFormal.RH`.
4. Complete the analytic-order-to-meromorphic-multiplicity bridge.
5. Integrate A declarations into the canonical axiom audit.
6. Machine-lock exact source paths and rerun the complete command suite.

## Reconciliation rule

Do not merge the current `A.tsv` rows for `CONSUMER.MELLIN.SPECIALIZED_LANDAU` or `API.MELLIN.SUBPOWER_NEGATIVE_MASS` as statement-faithful formalizations. They may be retained only after the proposition repairs and a fresh cross-review.

## Final classification

```text
upstream reuse:       mostly INTEGRATION_READY after local build repair
generic analytic API: salvageable
Landau propositions: STATEMENT_TOO_STRONG
final consumer:       INCOMPLETE_PUBLICATION
whole PR #734:        NOT_INTEGRATION_READY
RH:                   UNPROVED
```
