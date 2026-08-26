# Reviewer C pass-two exact-head build report

**Verdict: LEAN_COMPILE_FAILURE / NOT READY** from frozen source head
`b20ee9b3678e5d8fa32b04b156bc02cec782a97b` on
`formal/030-xi-operator-qa`.

Several statement-preserving repairs build in isolation, including FiniteMatrix,
ReciprocalConcavity, PickAlgebra, and both repaired order-three ChallengeDeps
modules. The full trusted library is nevertheless not green. Two inherited
declarations place the data type `ActualXiReserveAllocation ... : Type` directly
inside a proposition conjunction. Compiling either declaration requires a
theorem-type change, so the frozen-statement stop rule controls. No attempted
`Nonempty` wrapper is resident, and no C source repair was committed or pushed
after the stop.

## Frozen identity and dependency locks

| Field | Authoritative value |
|---|---|
| Branch | `formal/030-xi-operator-qa` |
| Frozen source commit | `b20ee9b3678e5d8fa32b04b156bc02cec782a97b` |
| Frozen source tree | `ed817c346294758ae1db773edba78d4527bace54` |
| Frozen source parent | `4863c31dd497ffe69ea400fe29275decf4cb5d29` |
| Initial status | clean |
| Diagnostic worktree | `C:\riemann-pass2\c` (detached, off OneDrive) |
| Local diagnostic head | `560f3548bcabd42a56830da5f18b4332fc996518` (not pushed) |
| Diagnostic status at stop | dirty: seven statement-preserving source files |
| Toolchain | `leanprover/lean4:v4.33.0-rc2` |
| Committed `lean-toolchain` SHA-256 | `0d3c76ccd8772d8bcbe207241421a760312b71a6aa82f84194391fdf5cb026d6` |
| Committed `lake-manifest.json` SHA-256 | `6be307e0de2294f99ce68e80903cd4cc88e77b6797c853c67be5cd9f6a1db453` |
| Locked external statement | LF, 526 bytes, SHA-256 `2eb547a373c49f56fa4da97284534bc06ee9a71548121a2b15d337cb79832c73` |

`lake -Kjobs=1 exe cache get` exited 0 with 8,489 pinned artifacts. No
`lake update` was run, and neither Mathlib nor Zeta23 was silently advanced.

## Controlling theorem-type blockers

1. `RiemannFormal.Operator.actualXiInputs_have_concrete_dependencies`,
   `formal/RiemannFormal/Operator/XiExternalInputs.lean`.

   The retained full-build diagnostic is at line 37, column 6; after the
   proof-only extensionality edit in the advisory working tree, the same frozen
   type is at line 40. Its conclusion contains:

   ```lean
   ... ∧ ActualXiReserveAllocation inputs.grouped ∧ ...
   ```

   `ActualXiReserveAllocation inputs.grouped` has type `Type` (sort `Type 1`),
   but `And` requires a `Prop`. A minimal compiling formulation would need a
   proposition wrapper such as `Nonempty (...)`; that is a theorem-type change
   and was reverted.

2. `RiemannFormal.Operator.buildLockedActualXiReserveAllocation`,
   `formal/RiemannFormal/Operator/XiSourceSpecific.lean:568` in the current
   advisory tree. Its frozen conclusion contains:

   ```lean
   SourceLockExact verified.sourceLock ∧ ActualXiReserveAllocation grouped
   ```

   This has the same `Type`-under-`And` defect. It was identified independently
   after the earlier XiExternalInputs blocker stopped the aggregate build. Its
   signature remains unchanged and no compile repair was attempted.

These are statement-sort defects, not proof-body elaboration failures. Reviewer
authorization is required before either theorem type can change.

## Targeted command evidence

| Check | Exit | Classification | Result / retained evidence |
|---|---:|---|---|
| `lake -Kjobs=1 exe cache get` | 0 | `PASS` | Pinned cache materialized; `raw/C/01_cache_get_command_result.log`. |
| `python scripts/verify_source_locks.py` | 0 | `PASS` | 139 locks; Mathlib `51e6992e`, Zeta23 `cec57f91`. |
| `python scripts/verify_c_repair_static.py` | 0 | `PASS` | Nine C semantic/static fixtures, including repaired order-three shape. |
| `python scripts/check_external_input_usage.py` | 0 | `PASS` | 14 headline theorems and 18 concrete fields. |
| `lake -Kjobs=1 build RiemannFormal.Operator.FiniteMatrix` | 0 | `PASS` | 8,697 jobs; raw Lake trace retained. |
| `lake -Kjobs=1 build RiemannFormal.Operator.ReciprocalConcavity` | 0 | `PASS` | 8,697 jobs; unused-variable warning only. |
| `lake -Kjobs=1 build RiemannComparatorChallengeDeps.XiPickThreeNode` | 0 | `PASS` | Unique local target built. |
| `lake -Kjobs=1 build RiemannComparatorChallengeDeps.XiPickOrderThreeConditional` | 0 | `PASS` | Unique local target built; unused-variable warning only. Repeated-node cases and PSD-only conclusion remain unchanged. |
| `lake -Kjobs=1 build RiemannFormal` | 1 | `LEAN_COMPILE_FAILURE` | First failed module `XiExternalInputs`; sort mismatch above. PickAlgebra also failed in this run but was repaired without a type change. |
| `lake -Kjobs=1 build RiemannFormal.Operator.PickAlgebra` | 0 | `PASS` | Proof-only explicit unfolding/normalization repair; 8,698 jobs. |
| `RiemannFormal.Operator.HeatQ4Finite` within aggregate | 0 | `PASS_PARTIAL` | Built successfully before aggregate failure. |
| Full `run_c_repair_validation.sh` and common suite | — | `BLOCKED_BY_LEAN_COMPILE_FAILURE` | Not green-completed after the controlling stop. |
| Complete C Challenge/Solution comparator suite | — | `BLOCKED_BY_LEAN_COMPILE_FAILURE` | Only the two ChallengeDeps targets above are authoritative PASS results. |
| Complete fail-closed `#print axioms` audit | — | `AXIOM_AUDIT_FAILURE` | Not green-completed; no kernel axiom verdict is claimed. |

## Static trust and comparator observations

A direct source scan found zero `sorry`, `admit`, leading `axiom`, `opaque`, or
`unsafe` declarations in `RiemannFormal/**`, nested ChallengeDeps, or nested
Solution. The three C-owned Challenge topics each retain exactly one expected
placeholder. The separate bootstrap RH Challenge topic retains its own expected
placeholder. This static scan does not substitute for the blocked authoritative
runner.

The shared Lake naming collision is mechanically corrected in the advisory
patch: local libraries use `RiemannComparatorChallengeDeps`,
`RiemannComparatorChallenge`, and `RiemannComparatorSolution`; Lean declaration
namespaces remain unchanged. The fail-closed axiom module manifest and LF lock
rule are also included. Only the two C ChallengeDeps targets were compiled after
that relocation, so the overall comparator verdict remains incomplete.

## Advisory patch and release gate

`C_PARTIAL_STATEMENT_PRESERVING_REPAIRS.patch` is the complete diff from frozen
head `b20ee9b...` to the stopped diagnostic working tree. A reverse apply check
against that working tree exits 0. The patch includes the shared Lake isolation,
LF rule, proof-body repairs, current big-operator notation, and QA script path
updates. It deliberately preserves both invalid theorem signatures above.

No source was pushed or merged. The full C suite, axiom audit, combined A+B+C
rehearsal, and formal-v0.1 reconciliation gate are blocked. RH remains unproved
and no RH claim is made.

Raw command excerpts and successful Lake trace JSON files are retained under
`raw/C/`; every retained evidence file and the advisory patch is covered by
this directory's `SHA256SUMS`.

