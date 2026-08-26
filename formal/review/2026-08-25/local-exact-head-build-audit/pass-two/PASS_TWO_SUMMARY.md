# Pass-two exact-head audit addendum

This directory appends to the pass-one evidence in the parent directory. It does not rewrite, supersede, or remove any pass-one command, failure, patch, or verdict.

## Result

| Scope | Frozen source | Trusted build | Comparator | No-sorry | Axiom output |
|---|---|---|---|---|---|
| Shared bootstrap repair | `db95fa09d9e956807099eb9d140de374f3ceca67` from base `573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f` | PASS | PASS | PASS | PASS, 6/6 declarations |
| Reviewer A | remote `ae0887b8125601c98dc809cffe01c7f1c78bb998` | PASS | PASS | PASS | PASS, 24/24 declarations |
| Reviewer B | remote `6d42bbc31c81e7d6a03909e205b56f30f6f7b49a` | PASS | PASS | PASS | PASS, 34/34 declarations |
| Reviewer C | remote remains `b20ee9b3678e5d8fa32b04b156bc02cec782a97b`; local advisory work is unpushed | FAIL | NOT COMPLETED | PASS by exact-source scan | NOT AVAILABLE |

The shared package correction requires unique Lake library names **and** unique local module prefixes. Renaming only the targets did not disambiguate the identical `ChallengeDeps`, `Challenge`, and `Solution` module roots exported by the pinned Zeta23 dependency. The final bootstrap repair preserves the declaration namespaces and Challenge/ChallengeDeps/Solution trust directories while using the local module prefixes `RiemannComparatorChallengeDeps`, `RiemannComparatorChallenge`, and `RiemannComparatorSolution`.

Reviewer A and Reviewer B are complete linear fast-forwards of their previously audited heads. Their theorem/declaration types and committed toolchain/dependency locks are unchanged. Both repaired remote heads pass the requested exact-head suites.

## Controlling C statement-review gate

Reviewer C reached a non-mechanical type error inherited from its accepted source head. `ActualXiReserveAllocation grouped` is a data structure in `Type`: it contains data projections including `share : ℕ → ℝ` and `leftover : ℕ → ℝ`. It therefore cannot be used directly as an operand of logical conjunction, which requires a `Prop`.

Two exact declarations are affected:

- `RiemannFormal.Operator.actualXiInputs_have_concrete_dependencies` in `RiemannFormal/Operator/XiExternalInputs.lean`, where `ActualXiReserveAllocation inputs.grouped` is a bare conjunct;
- `RiemannFormal.Operator.buildLockedActualXiReserveAllocation` in `RiemannFormal/Operator/XiSourceSpecific.lean`, where `ActualXiReserveAllocation grouped` is a bare conjunct.

Wrapping the allocation in `Nonempty`, replacing it with an existential proposition, returning a Type-valued product/Sigma, or splitting the proof and data outputs would all change the declaration type or public API. Changing the allocation structure itself to `Prop` is not mechanical because downstream code consumes its data projections. In accordance with the audit stop rule, the attempted `Nonempty` experiment was reverted. Both resident signatures remain identical to the original C head, and no C repair commit was pushed.

The local C work established that several proof-only repairs are viable, including the finite-matrix, reciprocal-concavity, Pick-algebra, notation, computability, and LF-lock work. Those changes are retained only in an advisory partial patch. They do not clear the controlling statement-review gate or establish a full trusted/comparator/axiom PASS.

## Combined gate

The combined A+B+C rehearsal requires all three individual trusted libraries to build. C does not meet that prerequisite, so no combined worktree was created and no mathematical or shared-file conflict was adjudicated. The pass-two combined verdict is `NOT_RUN_GATE_FAILED`.

## Verdict

`NOT_READY_FOR_FORMAL_V0_1_RECONCILIATION`

RH remains unproved.
