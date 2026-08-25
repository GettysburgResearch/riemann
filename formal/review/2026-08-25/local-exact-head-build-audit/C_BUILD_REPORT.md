# Reviewer C exact-head build report

Verdict: `LEAN_COMPILE_FAILURE`; consequential comparator, declaration-map, source-statement, no-sorry-wrapper, and axiom-audit failures.

## Frozen source

- branch: `formal/030-xi-operator-qa`
- commit: `b20ee9b3678e5d8fa32b04b156bc02cec782a97b`
- tree: `ed817c346294758ae1db773edba78d4527bace54`
- parent: `4863c31dd497ffe69ea400fe29275decf4cb5d29`
- merge base: `573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f`
- initial/final source status: clean, detached
- toolchain: `leanprover/lean4:v4.33.0-rc2`
- manifest blob: `f9c02d809750cf37e2ae9e19ac635f017e9efe82`
- manifest content SHA-256: `6be307e0de2294f99ce68e80903cd4cc88e77b6797c853c67be5cd9f6a1db453`

No dependency revision or committed lock changed, and `lake update` was not run.

## Required first validation and common suite

| Command | Exit | Classification | First result |
|---|---:|---|---|
| `bash scripts/run_c_repair_validation.sh` | 1 | `DEPENDENCY_FAILURE` | The first concurrent cache attempt hit a Windows sharing violation renaming a global Mathlib `.ltar.part` file. A serialized cache recovery subsequently completed without changing locks. |
| `lake exe cache get` | 0 | `PASS` | Locked cache was fully present and decompressed. |
| `lake build` | 1 | `LEAN_COMPILE_FAILURE` | Duplicate root/Zeta23 comparator libraries cause an absent dependency topic lookup; independent local errors occur in `FiniteMatrix.lean`, `ReciprocalConcavity.lean`, and `XiPickOrderThreeConditional.lean`. |
| `python3 scripts/generate_registry.py` | 0 | `PASS` | 139 claims and 12 delta rows generated. |
| `python3 scripts/validate_registry.py` | 0 | `PASS` | Generated registry validated. |
| `python3 scripts/verify_source_locks.py` | 0 | `PASS` | Locked Mathlib and Zeta23 revisions validated. |
| `python3 scripts/validate_blueprint.py` | 0 | `PASS` | Three fragments validated. |
| `bash scripts/check_no_sorry.sh` | 1 | `LEAN_COMPILE_FAILURE` | The wrapper's prerequisite target compilation fails; its nonzero exit is not a placeholder finding. The independent exact-source no-sorry verdict below passes. |
| `bash scripts/check_axioms.sh` | 1 | `AXIOM_AUDIT_FAILURE` | `RiemannFormal.olean` is absent after the failed trusted build. |

The settled `lake build` isolates source/package errors from the earlier transient cache event. Its first package-graph error is the attempted pinned-Zeta23 path `comparator/ChallengeDeps/XiPickOrderThreeConditional.lean`. Local roots include unsolved finite-matrix algebra, an unsafe derived real `Repr` plus computability/tactic issues in reciprocal concavity, and missing computability/import support in the order-three comparator dependency.

## Comparator and QA targets

| Command | Exit | Classification | First result |
|---|---:|---|---|
| `lake build Challenge.XiPickThreeNode` | 1 | `COMPARATOR_FAILURE` | Dependency-topic collision; local noncomputable-definition errors. |
| `lake build Solution.XiPickThreeNode` | 1 | `COMPARATOR_FAILURE` | Same collision/local errors; trusted finite-matrix failure also reached. |
| `lake build Challenge.OperatorPositiveSchurRescue` | 1 | `COMPARATOR_FAILURE` | Local ChallengeDeps module builds, but the duplicate dependency target is absent. |
| `lake build Solution.OperatorPositiveSchurRescue` | 1 | `COMPARATOR_FAILURE` | Collision plus trusted finite-matrix failure. |
| `lake build Challenge.XiPickOrderThreeConditional` | 1 | `COMPARATOR_FAILURE` | Collision plus local computability/parser errors. |
| `lake build Solution.XiPickOrderThreeConditional` | 1 | `COMPARATOR_FAILURE` | Collision plus trusted reciprocal-concavity/finite-matrix and local comparator errors. |
| `python3 scripts/verify_declaration_map.py` | 1 | `LEAN_COMPILE_FAILURE` | The Lean environment audit cannot import missing `RiemannFormal.olean`. |
| `python3 scripts/check_statement_sources.py` | 1 | `SOURCE_LOCK_FAILURE` | Checked-out CRLF bytes hash to `17de622f...`, not the committed normalized LF hash `2eb547a3...`. |

The line-ending defect is cross-platform and does not change the committed statement. `patches/C_source_statement_eol.patch` scopes an LF checkout rule to the locked external statement records and passes `git apply --check`; it must be present before materializing the statement file, or the file must be checked out again afterward.

## No-sorry, statement, and axiom results

- Exactly three C-owned Challenge placeholders exist: one in each requested Challenge topic.
- There is no `sorry` or `admit` in `RiemannFormal/**`, `comparator/ChallengeDeps/**`, or `comparator/Solution/**`.
- Static exact-source no-sorry verdict: `PASS`.
- The repaired order-three comparator contains all three repeated-node branches (`12`, `13`, `23`) and concludes PSD only. It contains no RH conclusion or stronger order-four/positive-definite result.
- Each of the three C-owned print modules was executed explicitly and exited 1 because the failed comparator builds produced no `Solution` module:
  `XiPickThreeNode.lean`, `OperatorPositiveSchurRescue.lean`, and `XiPickOrderThreeConditional.lean`.
- `RiemannFormal/AxiomAudit.lean` also exited 1 because the trusted aggregate did not build. Therefore no headline theorem has retained successful exact-head `#print axioms` output.

RH remains unproved.
