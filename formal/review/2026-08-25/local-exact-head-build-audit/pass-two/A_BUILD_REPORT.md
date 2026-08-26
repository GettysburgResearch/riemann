# Reviewer A pass-two exact-remote build report

Verdict: `PASS` for the repaired Reviewer A remote head. This report appends to, and does not replace, the immutable pass-one evidence.

## Frozen source and dependency locks

- branch: `formal/010-upstream-analysis`
- original audited head: `9ed8988218fd9c3e1da33bde81361262fc0aa747`
- repaired remote head: `ae0887b8125601c98dc809cffe01c7f1c78bb998`
- tree: `2a0482258f6063d9be314042382203e64cb09fcc`
- parent: `b670dee62fa6eb957186e186c23b1ae7d5595ef8`
- source status: clean, detached audit worktree
- committed toolchain SHA-256: `0d3c76ccd8772d8bcbe207241421a760312b71a6aa82f84194391fdf5cb026d6`
- committed manifest SHA-256: `6be307e0de2294f99ce68e80903cd4cc88e77b6797c853c67be5cd9f6a1db453`
- toolchain: `leanprover/lean4:v4.33.0-rc2`

The repaired head is a linear three-commit fast-forward from the original audited head. The committed `formal/lean-toolchain` and `formal/lake-manifest.json` blobs are unchanged, the checked-out Mathlib and Zeta23 revisions remain pinned, and no `lake update` was run.

The push log and an authoritative `git ls-remote` query both place the remote branch at `ae0887b8125601c98dc809cffe01c7f1c78bb998`.

## Exact-head results

| Command | Exit | Classification | Retained result |
|---|---:|---|---|
| `lake exe cache get` | 0 | `PASS` | Cache already complete; no files downloaded. |
| `lake build` | 0 | `PASS` | Trusted root completed successfully (`3914` jobs). |
| `python3 scripts/generate_registry.py` | 0 | `PASS` | `139` claims, `5` delta rows. |
| `python3 scripts/validate_registry.py` | 0 | `PASS` | `139` claims; `2` stated, `2` proved, `2` conditional. |
| `python3 scripts/verify_source_locks.py` | 0 | `PASS` | `139` claims; `6` analysis locks and `5` upstream locks. |
| `python3 scripts/validate_blueprint.py` | 0 | `PASS` | `3` blueprint fragments. |
| `bash scripts/check_no_sorry.sh` | 0 | `PASS` | No trusted sorry, admit, custom axiom, or opaque declaration. |
| `bash scripts/check_axioms.sh` | 0 | `PASS` | `24/24` declarations across `4/4` manifest modules. |
| `lake build RiemannComparatorChallenge.MellinAPI` | 0 | `PASS` | Unique local Challenge target compiled; its one statement placeholder is intentional and isolated. |
| `lake build RiemannComparatorSolution.MellinAPI` | 0 | `PASS` | Unique local Solution target compiled without sorry. |
| `lake env lean RiemannFormal/Analysis/AxiomAudit.lean` | 0 | `PASS` | All `16` A headline outputs were emitted. |
| `lake env lean comparator/PrintAxioms/MellinAPI.lean` | 0 | `PASS` | Comparator solution and conclusion-facing theorem outputs emitted. |
| `lake env lean comparator/PrintAxioms/RH.lean` | 0 | `PASS` | Baseline RH, Mellin solution, and conclusion-facing outputs emitted. |
| `bash RiemannFormal/Analysis/replay/run_validation.sh` | 0 | `PASS` | Full retained replay passed in `404` seconds. |

The fail-closed axiom manifest exactly covers both committed `AxiomAudit.lean` modules and both committed comparator print modules. Every reported dependency is among the permitted Lean foundations `propext`, `Classical.choice`, and `Quot.sound`; two release metadata equalities depend on no axioms.

## Statement-preserving elaboration repair

The only representation repair in the Landau package changes `NonnegativeTailMellinCore` from a Prop-valued `structure`—which asked Lean to generate an impermissible data-valued projection for `initialAbscissa : ℝ`—to a single-constructor `inductive ... : Prop`.

The constructor retains the exact same nine ordered payloads:

1. `locallyIntegrable`
2. `eventuallyNonnegative`
3. `nonzeroAE`
4. `finiteAbscissa`
5. `initialAbscissa`
6. `boundary_lt_initial`
7. `initialConvergence`
8. `analyticRightOfAbscissa`
9. `analyticPositiveReal`

`NonnegativeTailMellinData` still contains exactly that core proposition plus the unchanged `agreesRight` field. Consumers now eliminate the core proof to recover its witness instead of using the forbidden projection. No theorem type, open analytic proposition, comparator statement, or RH conclusion was strengthened or weakened.

The pinned-Mathlib repairs otherwise change proof terms, imports, notation scope, and computability annotations only. `fixedDetector_negativeMass_implies_RH` compiles with all unresolved analytic and arithmetic premises explicit. RH remains unproved.

## Comparator and trust boundary

The local Lake libraries and module paths now use the unique `RiemannComparatorChallengeDeps`, `RiemannComparatorChallenge`, and `RiemannComparatorSolution` prefixes. No legacy ambiguous comparator import remains. The Challenge-side Mellin placeholder is confined to the Challenge library; neither Solution nor `RiemannFormal` imports it. Solution and the trusted source tree are sorry-free.

The retained evidence proves Lake compilation and the statement-lock/import boundary. No standalone external `leanprover/comparator` binary transcript is present in the A raw-log set.

## Evidence notes

- `raw/A/00_push_fast_forward.log` records the successful remote fast-forward.
- `raw/A/01_cache_get.log` through `raw/A/14_run_validation.log` are the authoritative pass-two command logs.
- Upstream Zeta23 replay emits deprecation and tactic-suggestion diagnostics, including informational text saying a suggested `ring` tactic would fail. These are nonfatal replay diagnostics; every enclosing Lake build ends with `Build completed successfully`.
- The local `refs/remotes/origin/formal/010-upstream-analysis` ref was still stale at the original head during evidence preparation. This does not contradict the remote state: `git ls-remote` and the push transcript both resolve the server branch to the repaired head.

Run `sha256sum -c concise-staging/A/SHA256SUMS` from `audit-local-20260826-pass2/` to verify every retained raw A log.
