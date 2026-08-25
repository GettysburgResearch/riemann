# Reviewer B exact-head audit

## Verdict

Reviewer B at `072b4dbd0e4e407728a59110eb4f7214e23f8f8d` is **not an exact-head build pass**. The dependency and toolchain freeze is sound, and the registry, source-lock, blueprint, and source trust-boundary checks pass, but the trusted `lake build` fails on source compilation. Both bare comparator target pairs also fail, and neither B-owned axiom-print module can execute at the unmodified head.

Classification: `LEAN_COMPILE_FAILURE`, with consequential `COMPARATOR_FAILURE` and `AXIOM_AUDIT_FAILURE` results. The identified source corrections are statement-preserving mechanical/proof repairs; no theorem statement needs to be weakened or strengthened.

Reviewer B component verdict: `NOT_READY_FOR_FORMAL_V0_1_RECONCILIATION`.

## Frozen source and locks

| Item | Frozen value |
|---|---|
| Source branch | `formal/020-arithmetic-mellin` |
| Detached/source HEAD | `072b4dbd0e4e407728a59110eb4f7214e23f8f8d` |
| Origin branch HEAD | `072b4dbd0e4e407728a59110eb4f7214e23f8f8d` |
| Tree | `1c32466dd7928a24e0115268a6a330216f26ed3b` |
| First parent | `9bb802ebd97a00e01ef14789417f4c2a53031af3` |
| Bootstrap merge base | `573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f` |
| Initial/final status | clean, detached |
| `formal/lean-toolchain` | `leanprover/lean4:v4.33.0-rc2` |
| Toolchain Git blob | `c084c7fbe586b0276863b66f16d2955a43bc3fc6` |
| Toolchain committed-byte SHA-256 | `0d3c76ccd8772d8bcbe207241421a760312b71a6aa82f84194391fdf5cb026d6` |
| `formal/lake-manifest.json` Git blob | `f9c02d809750cf37e2ae9e19ac635f017e9efe82` |
| Manifest committed-byte SHA-256 | `6be307e0de2294f99ce68e80903cd4cc88e77b6797c853c67be5cd9f6a1db453` |

The working-tree SHA-256 values differ from committed-byte SHA-256 values only because this Windows checkout materializes line endings; `git diff --quiet` and the Git blob IDs confirm that both committed locks remained unmodified. No `lake update` was run.

Elan `4.2.1`, Lean `4.33.0-rc2` (`d8b1897`), Lake `5.0.0-src+d8b1897`, Python `3.12.10`, and GNU bash `5.2.15` were used through the requested PATH prefix.

All ten direct/inherited package checkouts match the committed manifest exactly:

| Package | Inherited | Revision |
|---|---:|---|
| plausible | yes | `123d15766ba49356c02ebad2a4462dfe12d79899` |
| LeanSearchClient | yes | `f5c090429dff3cf66cb65562526c9ea6e8edfbcb` |
| importGraph | yes | `bb3469a87774349fe01898d8bf2fc6a1ce6411ca` |
| proofwidgets | yes | `222c58dad7706a6e7cae46c0edd65ea881d3ee27` |
| aesop | yes | `7db8190085343afde2f5d2cdcc9bac719b6ec02c` |
| Qq | yes | `ef42f8944eaf5b6cbfbe75d1917d824c7dd6cf33` |
| batteries | yes | `76e1c118b0700b4ceafe99532e887d6431625e1a` |
| Cli | yes | `1319485273bf87833fa472afbcefdedecb16b45f` |
| mathlib | no | `51e6992efd06126df61a496bebf8f49482a4e129` |
| Zeta23 | no | `cec57f919ccf34e5fa5372b4ba332f7c848bbb6e` |

## Common exact-head suite

| Command | Exit | Classification | Result |
|---|---:|---|---|
| `lake exe cache get` | 0 | `PASS` | Locked cache retrieval completed; 8,654 files downloaded/decompressed. |
| `lake build` | 1 | `LEAN_COMPILE_FAILURE` | Three independent B source modules fail. |
| `python3 scripts/generate_registry.py` | 0 | `PASS` | 139 claims, 15 delta rows. |
| `python3 scripts/validate_registry.py` | 0 | `PASS` | 139 claims; conservative statuses validate. |
| `python3 scripts/verify_source_locks.py` | 0 | `PASS` | Locked mathlib and Zeta23 revisions validate. |
| `python3 scripts/validate_blueprint.py` | 0 | `PASS` | Three fragments validate. |
| `bash scripts/check_no_sorry.sh` | 0 | `PASS` | No trusted sorry/admit/custom axiom/opaque declaration. |
| `bash scripts/check_axioms.sh` | 1 | `AXIOM_AUDIT_FAILURE` | Cascades from absent `RiemannFormal.olean` after the failed trusted build. |

The first emitted causal compilation error is `RiemannFormal/Arithmetic/FixedRows.lean:24:23`: the intermediate calculation tries to prove an algebraic equality that only follows after using `h2`, leaving an unsolved goal. Two other modules started in parallel and have independent root errors:

- `SourceIdentities.lean:124:4` and `:202:4`: executable definitions over noncomputable real comparison/division instances lack `noncomputable` markers.
- `HalfDivisor.lean:19:4` first lacks a `noncomputable` marker; later failures are tactic/elaboration mechanics in the coefficient recurrence, antidiagonal sign rearrangement, factorization-product coercion, and prime-power simplification.

The advisory source patch changes proof bodies/tactics and computability markers only. It does not alter any declaration type or theorem statement.

## Comparator and axiom targets

All four required bare targets exit 1:

| Target | First causal result |
|---|---|
| `Challenge.ArithmeticRows23` | Lake also resolves the identically rooted locked-Zeta23 `ChallengeDeps` library and attempts its absent `ArithmeticRows23.lean`. |
| `Solution.ArithmeticRows23` | Same bare-target collision, followed by the trusted `FixedRows` compile error. |
| `Challenge.FixedDetectorFiveThree` | Same locked-Zeta23/local `ChallengeDeps` root collision. |
| `Solution.FixedDetectorFiveThree` | Same collision, followed by the trusted `FixedRows` compile error. |

Both the root package and locked Zeta23 dependency declare libraries named/rooted `ChallengeDeps`, `Challenge`, and `Solution`. The topic files exist only in the root package. Top-level root-package qualification (`@/+Module.Name`) does **not** repair this: all four qualified diagnostics still exit 1 because each target's imported `ChallengeDeps.<topic>` is resolved in both packages and Lake schedules the absent Zeta23 file. This comparator configuration collision remains unresolved and is not included as a claimed fix.

At the unmodified head:

- `lake env lean RiemannFormal/Arithmetic/AxiomAudit.lean` exits 1 because `FixedRows.olean` was not produced.
- `lake env lean comparator/PrintAxioms/ArithmeticFixedRows.lean` exits 1 because the failed comparator builds left no `Solution` module in `LEAN_PATH`.
- `scripts/check_axioms.sh` invokes neither of those B-owned modules. `patches/B_check_axioms.patch` adds both invocations and passes `git apply --check`; it does not modify the B worktree.

In the disposable patched tree, the three targeted trusted modules all build and a full `lake build` passes. Explicit execution of `RiemannFormal/Arithmetic/AxiomAudit.lean` then passes and emits 26 declaration records. A multiline-aware audit finds only `propext`, `Classical.choice`, and `Quot.sound`, with no `sorryAx`. The comparator print module and patched authoritative runner were not run because the persistent comparator collision prevented creation of `Solution.ArithmeticRows23.olean`, `Solution.FixedDetectorFiveThree.olean`, and `Solution.RH.olean`; this is a recorded prerequisite failure, not an axiom pass.

## Static declaration and trust-boundary checks

- Every one of the 11 nonempty `B.tsv` declaration entries is present in its declared module.
- Comment-stripped code in all 17 B-owned Lean files changed from the bootstrap contains no `RH`, `RiemannHypothesis`, or `riemannHypothesis` token. The only two textual RH mentions are comments explicitly saying the assembly does not conclude RH. Thus no B theorem concludes RH.
- A local import-closure traversal from trusted aggregate `RiemannFormal` visits 38 local/external module names and contains zero `Solution` modules.
- The two B challenge topics contain their expected statement-only `sorry` placeholders. Neither B solution imports `Challenge`; no sorry/admit occurs in `RiemannFormal`, `comparator/ChallengeDeps`, or `comparator/Solution`.

## Advisory mechanical fixes

- `patches/B_check_axioms.patch`: verified to apply cleanly; extends authoritative print-module coverage.
- `patches/B_compile_fixes.patch`: verified to apply cleanly against the exact head. It changes only three trusted source files: proof bodies/tactics and required `noncomputable` markers. All three targeted modules and the full trusted library build successfully with it. It changes no declaration type or theorem statement.

The source patch repairs the trusted build only. It does not repair the independent Lake comparator-library collision. The check-axioms coverage patch cannot be accepted as an executed authoritative pass until that collision is fixed and the Solution objects can be built.

The exact-head failures remain the controlling result even if the disposable patched diagnostic succeeds.

## Retained evidence

The command ledger is `B_COMMANDS.tsv`. Full logs are under `raw/B/`; the principal logs are:

- `10_lake_exe_cache_get.log`
- `11_lake_build.log`
- `12_generate_registry.log` through `17_check_axioms.log`
- `20_build_Challenge_ArithmeticRows23.log` through `25_lean_comparator_PrintAxioms_ArithmeticFixedRows.log`
- `30_static_B_declarations_and_closure.log`
- `31_comparator_library_collision.log`
- `33_final_exact_head_git_status.log` and `34_final_exact_head_integrity.log`
- `45_diagnostic_build_FixedRows.log`, `46_diagnostic_build_SourceIdentities.log`, and `48_diagnostic_build_HalfDivisor_refined.log`
- `49_diagnostic_full_lake_build.log`
- `50_diagnostic_build_qualified_Challenge_ArithmeticRows23.log` through `53_diagnostic_build_qualified_Solution_FixedDetectorFiveThree.log`
- `54_diagnostic_lean_RiemannFormal_Arithmetic_AxiomAudit.log` through `57_diagnostic_validate_B_axiom_output.log`

No dependency source, `.lake` tree, build artifact, or generated cache is included in the retained report set.
