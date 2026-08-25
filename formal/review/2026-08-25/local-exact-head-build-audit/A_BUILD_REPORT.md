# Reviewer A exact-head build report

Verdict: `LEAN_COMPILE_FAILURE`; independent comparator and source-lock failures, with consequential axiom-audit failure.

## Frozen source

- branch: `formal/010-upstream-analysis`
- commit: `9ed8988218fd9c3e1da33bde81361262fc0aa747`
- tree: `2c6e967344eb373843a018a5415f7dce6ba39b94`
- parent: `7f9959088610efb7ee7cd01cfce1ad6cda397d61`
- merge base: `573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f`
- initial/final source status: clean, detached
- toolchain: `leanprover/lean4:v4.33.0-rc2`
- manifest blob: `f9c02d809750cf37e2ae9e19ac635f017e9efe82`
- manifest content SHA-256: `6be307e0de2294f99ce68e80903cd4cc88e77b6797c853c67be5cd9f6a1db453`

No dependency revision or committed lock changed, and `lake update` was not run.

## Common suite

| Command | Exit | Classification | First result |
|---|---:|---|---|
| initial `lake exe cache get` | 1 | `DEPENDENCY_FAILURE` | Concurrent global-cache finalization hit a Windows sharing violation. |
| serialized `lake exe cache get` retry | 0 | `PASS` | Locked cache completed without a manifest change. |
| `lake build` | 1 | `LEAN_COMPILE_FAILURE` | Duplicate root/Zeta23 comparator resolution and independent local source failures. |
| `python3 scripts/generate_registry.py` | 0 | `PASS` | 139 claims and 5 delta rows generated. |
| `python3 scripts/validate_registry.py` | 0 | `PASS` | Generated registry validated. |
| `python3 scripts/verify_source_locks.py` | 1 | `SOURCE_LOCK_FAILURE` | `A_UPSTREAM_REUSE.tsv` omits the referenced declaration `Zeta23.RH_implies_on_line`. |
| `python3 scripts/validate_blueprint.py` | 0 | `PASS` | Three fragments validated. |
| `bash scripts/check_no_sorry.sh` | 0 | `PASS` | No trusted sorry/admit/custom axiom/opaque declaration. |
| `bash scripts/check_axioms.sh` | 1 | `AXIOM_AUDIT_FAILURE` | `RiemannFormal.olean` is absent after the failed trusted build. |

The first persistent package-graph error is Lake's attempt to build absent pinned-Zeta23 files `comparator/ChallengeDeps/MellinAPI.lean` and `comparator/Solution/MellinAPI.lean`. The local ChallengeDeps module independently lacks the import that provides complex notation. `RiemannFormal/Upstream/MathlibBridge.lean` independently has three computability errors and uses an unavailable `.analyticAt` projection on differentiability witnesses in the pinned Mathlib API. The same pointwise differentiability-to-analyticity pattern is present downstream in `Zeta23Bridge.lean` and `Analysis/MellinAPI.lean`; it was not reached after the bridge failed.

The initial parallel build also logged memory/unreadable-cache artifacts. The branch-retained replay was run after a successful serialized cache scan and reproduced only the persistent package/local-source failures; the transient artifacts are therefore not classified as causal.

## Required A targets and retained validation

| Command | Exit | Classification |
|---|---:|---|
| `lake build Challenge.MellinAPI` | 1 | `COMPARATOR_FAILURE` |
| `lake build Solution.MellinAPI` | 1 | `COMPARATOR_FAILURE` |
| `bash RiemannFormal/Analysis/replay/run_validation.sh` | 1 | `LEAN_COMPILE_FAILURE` |
| `lake env lean RiemannFormal/Analysis/AxiomAudit.lean` | 1 | `AXIOM_AUDIT_FAILURE` |
| `lake env lean comparator/PrintAxioms/MellinAPI.lean` | 1 | `AXIOM_AUDIT_FAILURE` |
| `lake env lean comparator/PrintAxioms/RH.lean` | 1 | `AXIOM_AUDIT_FAILURE` |

The replay completed its locked cache stage and then stopped at its failing `lake build`, as required by `set -e`. Package-qualified diagnostics confirm that target qualification alone does not repair the local source/API failures.

## Trusted declarations and axioms

- The root trusted library does not build.
- The repaired tail-Mellin declarations and `fixedDetector_negativeMass_implies_RH` are resident at the requested head, but no successful exact-head compilation of them was produced because their import closure is blocked by `MathlibBridge`.
- Static import/token inspection finds no Challenge-side sorry entering `Solution` or `RiemannFormal`. The A-owned Mellin Challenge has its single intended statement placeholder; the inherited RH Challenge has a separate placeholder.
- All requested headline `#print axioms` directives are present in the three audit sources. None produced successful output because the prerequisite objects were absent, so the axiom verdict is failure/unverified—not a finding of extra axioms.
- PR #747 at `ebe287cc85b122cbe3efd57b7c30ce17d150d74c` still has no final acceptance addendum.

No theorem statement was changed. The analytic API adapter is not treated as a safe mechanical fix without an independently compiling proof.

`patches/A_MECHANICAL_FIXES.patch` passes `git apply --check` and only adds the missing Complex import, opens a noncomputable scope for the three upstream aliases, and repairs the missing source-lock ledger entry. It is intentionally partial and un-applied; it does not claim to solve the analytic adapters or duplicate Lake library names.

RH remains unproved.
