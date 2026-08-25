# Reviewer A exact-head local audit

## Verdict

`NOT_READY_FOR_FORMAL_V0_1_RECONCILIATION`

Reviewer A's exact head does not compile with its committed toolchain and manifest. The failures reproduce after a healthy serialized cache pass and include trusted-source errors, a comparator source/import error, a Lake library-name collision, and a source-lock ledger omission. Consequently no valid axiom-print output was produced and the repaired tail-Mellin declarations and `fixedDetector_negativeMass_implies_RH` were not compiled.

## Frozen identity

| Field | Exact value |
|---|---|
| Named branch | `formal/010-upstream-analysis` |
| Remote branch resolution | `9ed8988218fd9c3e1da33bde81361262fc0aa747` |
| Detached HEAD | `9ed8988218fd9c3e1da33bde81361262fc0aa747` |
| Tree | `2c6e967344eb373843a018a5415f7dce6ba39b94` |
| Parent | `7f9959088610efb7ee7cd01cfce1ad6cda397d61` |
| Toolchain file | `leanprover/lean4:v4.33.0-rc2` |
| Lean | `4.33.0-rc2`, commit `d8b18978322de05a8f3dba51ef03cf5461676c17` |
| Lake | `5.0.0-src+d8b1897` |
| `lake-manifest.json` SHA-256 | `7290452db11edeab155ffabe5a2b5d6b4cf07ea741449a5934af421dbd53f9b1` |
| `lake-manifest.json` Git blob | `f9c02d809750cf37e2ae9e19ac635f017e9efe82` |
| Initial/final status | Detached and clean; no tracked or untracked source-worktree files |

No `lake update` was run. The initial cache command failed only because concurrent agents contended on a shared Windows cache rename (`error 32`). A serialized retry exited 0, downloaded nothing, and decompressed 8,478 cached files. The retained replay later reported all 8,681 cache files already decompressed, then reproduced the local source failures.

## Common suite

| Command | Exit | Classification | Result |
|---|---:|---|---|
| `lake exe cache get` (initial) | 1 | `DEPENDENCY_FAILURE` | Shared-cache `.ltar.part` rename collision, Windows error 32 |
| `lake exe cache get` (serialized recovery) | 0 | `PASS` | Healthy pinned cache, no download |
| `lake build` | 1 | `LEAN_COMPILE_FAILURE` | Comparator and trusted upstream source failures; initial run also had memory/cache concurrency cascades |
| `python3 scripts/generate_registry.py` | 0 | `PASS` | 139 claims, 5 delta rows; generated tree clean |
| `python3 scripts/validate_registry.py` | 0 | `PASS` | Registry valid |
| `python3 scripts/verify_source_locks.py` | 1 | `SOURCE_LOCK_FAILURE` | `Zeta23.RH_implies_on_line` absent from `A_UPSTREAM_REUSE.tsv` |
| `python3 scripts/validate_blueprint.py` | 0 | `PASS` | Three fragments valid |
| `bash scripts/check_no_sorry.sh` | 0 | `PASS` | No trusted `sorry`/`admit` or custom `axiom`/`opaque` |
| `bash scripts/check_axioms.sh` | 1 | `AXIOM_AUDIT_FAILURE` | `RiemannFormal.olean` absent because the trusted build failed |

The exact command ledger and first causal errors are in `A_COMMANDS.tsv`.

## Deterministic blockers

1. `comparator/ChallengeDeps/MellinAPI.lean` imports `Mathlib.Analysis.Analytic.Constructions` but uses `ℂ`, which is not in scope on the pinned graph. Both bare targets and `lake build @/+ChallengeDeps.MellinAPI` reproduce `Unknown identifier ℂ` at lines 8–14.

2. The package graph contains project and Zeta23 libraries with the same names (`ChallengeDeps`, `Challenge`, and `Solution`). Bare targets emit missing-path facets under `.lake/packages/Zeta23/comparator/...`. Root-qualifying the top module does not prevent its prerequisite facet from colliding.

3. `RiemannFormal/Upstream/MathlibBridge.lean` deterministically fails:
   - aliases of `riemannZeta`, `completedRiemannZeta`, and `completedRiemannZeta₀` need a noncomputable scope;
   - three proofs call `.analyticAt` on pointwise `DifferentiableAt` results. Lean reports the values as existential derivative witnesses and no `Exists.analyticAt` projection exists.

4. The same pointwise-differentiability-to-analyticity pattern is present in `RiemannFormal/Upstream/Zeta23Bridge.lean:41` and `RiemannFormal/Analysis/MellinAPI.lean:48`. These downstream files were not reached because `MathlibBridge` failed. Repairing these analytic adapters is outside the safely mechanical patch boundary and remains an unpatched compile blocker.

5. `verify_source_locks.py` independently fails because `registry/deltas/A_UPSTREAM_REUSE.tsv` omits the referenced declaration `Zeta23.RH_implies_on_line`.

The branch-retained `RiemannFormal/Analysis/replay/run_validation.sh` exits 1 at its embedded default build and therefore never reaches its later comparator and audit steps.

## Reviewer A target and audit verdicts

| Requirement | Verdict | Evidence |
|---|---|---|
| Root trusted library builds | Fail | Default build exits 1 in trusted upstream code |
| `Challenge.MellinAPI` | Fail | Local comparator contract has unknown `ℂ`; Lake collision also emitted |
| `Solution.MellinAPI` | Fail | Blocked by `ChallengeDeps.MellinAPI` |
| Repaired tail-Mellin declarations compile | Not established / fail-closed | `MellinAPI.olean` is absent; upstream bridge fails first |
| `fixedDetector_negativeMass_implies_RH` compiles | Not established / fail-closed | Consumer prerequisites do not build |
| Branch replay | Fail | Reproduces deterministic source failures |
| Analysis axiom module | Fail | Missing `RiemannFormal.Analysis.MellinAPI.olean` |
| Mellin comparator axiom module | Fail | Missing `Solution` module |
| RH comparator axiom module | Fail | Missing `Solution` module |
| Headline `#print axioms` directives retained in source | Pass (static only) | Analysis audit lists 16 declarations; both comparator print modules include the headline theorem |
| Headline axiom output retained from this build | Fail | No print module reached axiom output |

## Trust-boundary checks

The authoritative no-sorry script passes. An additional static scan found:

- no `sorry` or `admit` in `RiemannFormal`, `comparator/Solution`, or `comparator/ChallengeDeps`;
- no custom `axiom`, `opaque`, or `unsafe` declaration in those paths;
- no import of a `Challenge.*` module from those trusted paths;
- exactly two challenge-side placeholders on this head: `Challenge.MellinAPI` and the pre-existing `Challenge.RH`.

`RiemannFormal.Analysis.ComparatorSmoke` imports `Solution.MellinAPI`, whose only project comparator dependency is `ChallengeDeps.MellinAPI`; it does not import the sorry-bearing challenge module. Thus no Challenge-side sorry enters `Solution` or `RiemannFormal` by source imports, but the trusted aggregate still does not compile.

## Advisory mechanics

`patches/A_MECHANICAL_FIXES.patch` applies cleanly with `git apply --check` and was not applied to the source worktree. It only:

- adds the Complex basic import to the comparator contract;
- opens a noncomputable section for the upstream zeta aliases;
- adds `Zeta23.RH_implies_on_line` to the upstream reuse ledger.

This patch is intentionally partial and was not Lean-validated after application. It does not address the analytic-adapter obligations or the duplicate Lake library names; those remain blockers.

## Evidence

- Full logs: `audit-local-20260825/raw/A/`
- Exact command ledger: `audit-local-20260825/A_COMMANDS.tsv`
- Raw-log checksums: `audit-local-20260825/A_RAW_SHA256SUMS.tsv`
- Advisory patch: `audit-local-20260825/patches/A_MECHANICAL_FIXES.patch`
