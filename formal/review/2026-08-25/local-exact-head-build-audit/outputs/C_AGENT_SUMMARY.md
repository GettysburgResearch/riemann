# Reviewer C exact-head audit

Verdict: `NOT_READY_FOR_FORMAL_V0_1_RECONCILIATION`

Reviewer C's frozen exact head does not build under its committed Lean toolchain and manifest. The failure persists after a serialized, successful cache verification, so it is not attributable to the initial shared-cache race. The trusted aggregate, every requested bare comparator target, the declaration environment audit, and every C-owned axiom-print module fail.

## Frozen source and dependency state

| Item | Recorded value |
|---|---|
| Source branch | `formal/030-xi-operator-qa` |
| HEAD | `b20ee9b3678e5d8fa32b04b156bc02cec782a97b` |
| Tree | `ed817c346294758ae1db773edba78d4527bace54` |
| Parent | `4863c31dd497ffe69ea400fe29275decf4cb5d29` |
| Bootstrap merge base | `573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f` |
| Toolchain | `leanprover/lean4:v4.33.0-rc2` |
| Lean | `4.33.0-rc2`, commit `d8b18978322de05a8f3dba51ef03cf5461676c17` |
| Lake | `5.0.0-src+d8b1897` |
| `lean-toolchain` blob / committed SHA-256 | `c084c7fbe586b0276863b66f16d2955a43bc3fc6` / `0d3c76ccd8772d8bcbe207241421a760312b71a6aa82f84194391fdf5cb026d6` |
| `lake-manifest.json` blob / committed SHA-256 | `f9c02d809750cf37e2ae9e19ac635f017e9efe82` / `6be307e0de2294f99ce68e80903cd4cc88e77b6797c853c67be5cd9f6a1db453` |
| Dependency checkouts | All 10 exact manifest revisions, all tracked-clean |
| Initial/final source status | Clean / clean |

No `lake update` was run. The manifest and toolchain remained unchanged.

## Authoritative command results

| Check | Exit | Classification | Result |
|---|---:|---|---|
| First `bash scripts/run_c_repair_validation.sh` | 1 | `DEPENDENCY_FAILURE` | Windows sharing error 32 during the concurrent global cache fetch. |
| Serialized recovery validation | 1 | `DEPENDENCY_FAILURE` | Cache passed; its immediate build first saw transient unreadable Mathlib artifacts and then persistent C failures. |
| `lake exe cache get` | 0 | `PASS` | Serialized no-op: all 8681 files already decompressed. |
| `lake build` | 1 | `LEAN_COMPILE_FAILURE` | Persistent Lake package collision and independent local Lean source failures. |
| Registry generation/validation | 0 / 0 | `PASS` | 139 claims, 12 delta rows; registry content validates. |
| Generic `verify_source_locks.py` | 0 | `PASS` | Committed project/toolchain/dependency locks validate. |
| Blueprint validation | 0 | `PASS` | Three fragments validate. |
| `check_no_sorry.sh` | 1 | `LEAN_COMPILE_FAILURE` | Static trust scans passed; its embedded comparator build failed. This is not a placeholder violation. |
| `check_axioms.sh` | 1 | `AXIOM_AUDIT_FAILURE` | Generated 17-declaration audit, then could not import absent `RiemannFormal.olean`. |
| Six requested bare Challenge/Solution targets | all 1 | `COMPARATOR_FAILURE` | All fail; exact per-target causes are in `C_COMMANDS.tsv`. |
| `verify_declaration_map.py` | 1 | `LEAN_COMPILE_FAILURE` | Static checks reach the Lean environment audit, which cannot import absent `RiemannFormal.olean`. |
| `check_statement_sources.py` | 1 | `SOURCE_LOCK_FAILURE` | CRLF worktree bytes do not match the normalized LF lock. |
| Three C-owned PrintAxioms files | all 1 | `AXIOM_AUDIT_FAILURE` | `Solution` objects were not produced. |
| `RiemannFormal/AxiomAudit.lean` | 1 | `AXIOM_AUDIT_FAILURE` | Trusted aggregate object was not produced. |

## First causal compile failures

There are two independent failure families.

1. Lake target/library collision. The root and pinned Zeta23 dependency both export `ChallengeDeps`, `Challenge`, and `Solution` libraries. Bare targets try to run paths such as `.lake/packages/Zeta23/comparator/ChallengeDeps/XiPickOrderThreeConditional.lean`, which do not exist. Even `lake build @/+Challenge.XiPickOrderThreeConditional` still inherits the duplicate `ChallengeDeps` resolution.

2. Local sources independently fail when selected directly:
   - `comparator/ChallengeDeps/XiPickThreeNode.lean` uses real division in computable `def`s without a noncomputable boundary.
   - `comparator/ChallengeDeps/XiPickOrderThreeConditional.lean` first fails at line 131 for the same reason, and later has missing BigOperators parsing (`unexpected token 'in'`) with cascading unknown declarations.
   - `RiemannFormal/Operator/ReciprocalConcavity.lean` derives a safe declaration through unsafe `Real.instRepr`, contains noncomputable-definition failures, and leaves algebraic goals unsolved.
   - `RiemannFormal/Operator/FiniteMatrix.lean` leaves several `ring`/`ring_nf` algebraic goals unsolved.

The direct local check confirms these are not merely Lake target-selection diagnostics. A compile patch was not attempted: repair spans target configuration, declaration computability, generated instances, notation scope, and several proofs. Treating all of that as safely mechanical without validation would exceed the no-mathematical-adjudication boundary. No theorem statement was changed.

## Trust-boundary and comparator findings

- The three C-owned challenge files selected by the branch checker each contain exactly one statement-only placeholder: `XiPickThreeNode`, `OperatorPositiveSchurRescue`, and `XiPickOrderThreeConditional`.
- The inherited `comparator/Challenge/RH.lean` smoke challenge contains one additional non-C placeholder, so the full Challenge directory has four. This is reported separately rather than hidden.
- `RiemannFormal/**`, `comparator/ChallengeDeps/**`, and `comparator/Solution/**` contain zero `sorry`/`admit`, zero declaration-leading `axiom`/`opaque`/`unsafe`, and zero unresolved tactic suggestions.
- Static source inspection confirms explicit repeated-node branches for pairs 12, 13, and 23.
- The shared order-three statement concludes `ActualXiPickPSDThroughThree`; it asserts PSD through sizes one, two, and three only, with no positive-definite, order-four, or RH conclusion.
- All 18 C.tsv/C_API.tsv declarations have textual source locations. Their Lean existence cannot be certified because the aggregate does not compile.
- No usable `#print axioms` output was obtained. The axiom verdict is therefore failure/unverified, not an assertion that extra axioms were found.

## Source-lock EOL defect and advisory patch

The committed normalized statement is 526 LF bytes with SHA-256:

`2eb547a373c49f56fa4da97284534bc06ee9a71548121a2b15d337cb79832c73`

The clean Windows checkout under system `core.autocrlf=true` is 537 bytes with 11 CRLF sequences and SHA-256:

`17de622ff254ac81be5e4cf783cd9eafb8a52659b22ba89705ed79d5ee4305ee`

The narrow advisory patch `patches/C_source_statement_eol.patch` adds only:

`registry/deltas/C_EXTERNAL_SOURCE_STATEMENTS/*.txt text eol=lf`

Patch SHA-256: `13bccaae99b551dcdc87f134c14787f13932fb857032766a72c4e09c6c46811a`.

It was not applied to the exact-head worktree. Apply the attribute before materializing the C statement file, or re-check it out afterward, in the combined rehearsal.

## Evidence

- Exact ledger: `C_COMMANDS.tsv`
- Full raw logs: `raw/C/`
- Raw-log checksum manifest: `raw/C/SHA256SUMS` (90 entries; manifest SHA-256 `6da4f33308a92723bfaeaf3ebd86ff6d5d916fa99038116e251eac858dd226ad`)
- Advisory patch: `patches/C_source_statement_eol.patch`

The Reviewer C source worktree remains detached, exact-head, and clean.
