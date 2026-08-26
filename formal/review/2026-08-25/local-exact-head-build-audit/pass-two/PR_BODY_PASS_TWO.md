## Pass two — statement-preserving repair audit

Pass one remains immutable in the parent directory and in the original PR body.

The shared root/Zeta23 comparator collision is independently repaired by unique Lake target names and unique local module prefixes. The exact bootstrap suite passes, including the RH comparator smoke target, 139-row registry, source locks, blueprint, no-sorry scan, and fail-closed axiom audit.

Reviewer A now passes at remote `ae0887b8125601c98dc809cffe01c7f1c78bb998`. Reviewer B now passes at remote `6d42bbc31c81e7d6a03909e205b56f30f6f7b49a`. Both retain the committed toolchain and manifest and preserve theorem/declaration types.

Reviewer C was not pushed. Two inherited declarations use the Type-valued data structure `ActualXiReserveAllocation` directly under Prop-valued conjunction:

- `RiemannFormal.Operator.actualXiInputs_have_concrete_dependencies`;
- `RiemannFormal.Operator.buildLockedActualXiReserveAllocation`.

Every viable repair changes a result type or public API. The attempted `Nonempty` experiment was reverted, the original signatures remain resident, and the no-type-change stop rule controls. Local proof-only progress is retained as an advisory patch only.

Because C's individual trusted build is not green, the combined rehearsal remains `NOT_RUN_GATE_FAILED`.

Final pass-two verdict: `NOT_READY_FOR_FORMAL_V0_1_RECONCILIATION`.

RH remains unproved.
