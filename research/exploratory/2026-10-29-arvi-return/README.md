# Candidate scalar return below tracker PR #94

**Status:** The staged `0.8738702` candidate, including its floor-budget changes and final `Candidate.bound`, has compiled in pinned Lean 4.34.1 using cached dependencies. Lean reports only `propext`, `Classical.choice`, and `Quot.sound` as transitive axioms. The build is not tracker admission or a fresh replay of all cached proofs; independent review of the analytic framework and its interpretation remains open. The improvement over PR #94 is small, not a claim of a significant new region. See the completed build and theorem audit below.

**Sources:** QuasiRiemannTracker [PR #94 at head e5a82f72d8ff39a3cc1ad044e6acd727e77a3fc4](https://github.com/GTimG/QuasiRiemannTracker/tree/e5a82f72d8ff39a3cc1ad044e6acd727e77a3fc4/submissions/2026-10-29-arvi-density/src/Submissions/arvi_density), especially `Return/Constants.lean`, `Return/Formulas.lean`, `Return/Windows.lean`, `ReturnD/Schedule.lean`, and `ReturnD/TransportGeometry.lean`. The source head reports the boundary 43693617/50000000 = 0.87387234. For the transcribed inputs at that head, SHA-256 of `Return/Formulas.lean` is `e7dfed2c335372dde5a609ec2b53bf268d6fe7c40807bdb7ee83c5d7f3f3216b` and of `Return/Windows.lean` is `3d436434bf8a76f2246f12bb942840f33e4d8ce3d2155660e4572dccab15a799`. The 31 window bounds in the script are copied from that `Windows.lean` (Apache-2.0; copyright Sil, and subsequent modifications credited to ArviFoxy in that file). The branch formulas are independently transcribed from `Formulas.lean`.

**Candidate:** retain both PR #94 source faces and all count-branch constants and set

```text
theta = 4369351/5000000 = 0.8738702
h = 1007/1250 = 0.8056
numeratorCap = 619/10000 = 0.0619
floor reserve = 1/250
```

The candidate theta is 0.00000214 below PR #94's, a small improvement. The formal Dirichlet nonvanishing theorem is recorded below; the imported analytic sources, their source-to-physical transport, and their interpretation have not received a complete independent mathematical audit.

## Checks performed

Run with Python 3 and SymPy 1.14.0:

```text
$ python research/exploratory/2026-10-29-arvi-return/check_rows.py
edge 0 nodes 1 leaves 1 maxdepth 0 branches {'old': 1}
edge 1 nodes 3 leaves 2 maxdepth 1 branches {'old': 2}
edge 2 nodes 3 leaves 2 maxdepth 1 branches {'old': 2}
edge 3 nodes 59 leaves 30 maxdepth 11 branches {'old': 11, 'capP': 6, 'C': 8, 'weakC7': 2, 'capC': 3}
$ python research/exploratory/2026-10-29-arvi-return/check_geometry.py
parameters True
BoundsN True
schedule True
physical cap restricted True
floor loss constructor True
theta,h,ell,x,y,cap: 4369351/5000000 1007/1250 641947/3750000 1370947/3750000 868553/1875000 619/10000
```

`check_rows.py` uses exact rational arithmetic and Bernstein coefficients on dyadic rectangular subdivisions of the full parameter box `[0,3/4] × [0,1/2]`. It derives each branch's cleared row margin from the source definitions and verifies the fifteen branch admission guards. Every non-old branch leaf must also lie in a source window of that branch. A parent rectangle is replaced by its two closed halves, so the listed leaves cover the entire box, not a sample. All four conductor edges are checked with row reserve `10^-8`. This provides the scalar edge inequalities, conditional on the identification of the source branches and window availability. The source's interpolation in conductor distance is an imported lemma, not checked by this computation.

`check_geometry.py` checks the transcribed `Parameters`, modified `BoundsN` (with the floor reserve changed to `1/250`), the non-row fields of `PhysicalSchedule`, and the physical cap restriction. For the candidate, the exact floor saving is `13825071799/3000000000000`, exceeding `1/250` by `1825071799/3000000000000`. The original `1/200` bound fails; it cannot be used unchanged.

## Historical development checkpoints (29 October 2026)

The following paragraphs record earlier checkpoints and their limitations at the time; the completed build below supersedes their statements about missing compilation.

### Proposed floor patch and initial open gates

`floor-budget-proposal.patch` changes 11 occurrences across eight PR #94 `ReturnD` files, from the floor-only reserve `1/200` to `1/250`. The patch passes `git apply --check` against the pinned head and is **not compiled**. It intentionally leaves unrelated `1/200` quantities, including the minimum conductor scale, unchanged. The constructor bounds its floor loss by `(26/10000+1/100+2+1/8+1/8) t` with `t≤10^-8`, which is below `1/250`; the geometry script checks this rational inequality. Its modified proofs and all callers still need Lean verification.

The patch does not alter the PR constants or regenerate the Lean endpoint certificates. Completing a proof requires at least: reproduce and verify all imported analytic and source interfaces, prove the candidate's window/admission and edge certificates inside the intended proof system, reinstantiate geometry and physical schedule with the candidate constants, check the smaller floor budget through all transport calls, rebuild the dependency graph, and prove the final zero-free assertion. The scripts establish no claim of novelty or improvement beyond this scalar candidate.

A subsequent Lean candidate is recorded as `candidate-lean.patch`: it includes the floor patch, changes the candidate constants and theorem target, and regenerates all 47 existing edge certificate coefficient arrays while retaining the original source windows and cover tree. An exact symbolic replay verified all 47 displayed polynomial identities and nonnegative coefficients. A partial pinned Lean 4.34.1 probe compiled `Constants`, `Formulas` and all six edge modules containing the 47 generated row proofs. `partial-lean-probe.json` records the source and resulting `.olean` hashes; the probe operator reported success but did not retain stdout. The complete return, floor changes and final target have not been built, so this is not a kernel-verified zero-free theorem.

The initial exploratory script incorrectly parsed Lean's `oldCapacity`: Lean divides the whole `min` by `6*kappa`. The current `check_rows.py` uses the corrected expression, and all listed checks were rerun after that correction. The initial version and its hash are invalid.

For the 47 displayed polynomial identities, `python research/exploratory/2026-10-29-arvi-return/verify_generated.py /path/to/patched/tracker` compares each candidate `bsum` expansion with a separately constructed exact rational margin and checks its positive constant and nonnegative coefficients. `regenerate_rows.py` recreates these row files in a supplied isolated tracker checkout; it is a **mutating** script. Re-running it on the candidate checkout produced the same `candidate-lean.patch` SHA-256 `f1dfd0f0c04677e331568ceb038dc0a91b8262110f48260502f4218f6febc2d7`.

Independent review found that an earlier generator emitted nine coefficient arrays at the polynomial's minimal degree while leaving the source's larger `bsum` degree unchanged, making those declarations ill-typed. The generator now elevates the arrays to the declared degrees; the independent checker additionally checks all 47 distinct names, matrix dimensions and bound coefficient names. This repair has not yet been kernel-checked.

Independent source review checked that the 31 window tuples match the pinned source, inspected the transcribed branch and admission formulas, and checked all 47 patched matrix dimensions and coefficient references. A separate inspection traced the floor-budget calls and found no unrelated `1/200` changes or visible unmodified floor call. These are source inspections, not a kernel build or an audit of all external dependencies.

A later isolated pinned Lean probe compiled the modified `ReturnD.TransportGeometry`, `Return.Geometry`, `Return.TransportInstances`, and `ReturnD.Transport.Transport.FloorExponent`, including the revised floor-source margin, as well as their local geometry dependencies. The exact driver and captured warnings/exit codes are in `lean-geometry-probe.py` and `lean-geometry-probe.log`. This does not compile the remaining floor-budget callers or final target.

### Intermediate build trace

The pinned Lean 4.34.1 main run has compiled `Return.Constants` and every changed floor-budget module: `ReturnD.TransportGeometry`, `TransportParameters`, and `Transport.Transport.{FloorExponent,CubeFloorSaving,CubeFloorCollected,NonfloorTransport,SharedNonfloor,HighApproximation}`. The six changed `Return.Rows.Edge_*` modules compiled both in a separate probe and in the main run. The main run has also compiled all 129 individual `ChainF50.Step_*` modules, all 31 window-admission modules, and the candidate `Return.EdgeCertificates`, `Return.FinalRows`, `Return.FinalSchedule` and `Return.EndpointFromNumerator`. The conditional `Return.EndpointFromSources` and `Return.Endpoint` have also compiled. Their theorem still takes the two named global source hypotheses. This was the intermediate checkpoint before the full target compilation recorded below. Individual module completions alone do not imply the final theorem. Main build logs currently reside in `/workspace/scratch/qproject/build_combined.log` and `build_priority.log`.

The pinned Lean `#check` and `#print axioms` output is retained in `lean-endpoint-axioms.log`. It gives the exact conditional statements: if both PR #94 global sources at faces `(96232839/100000000, 3853/2000, 1/10)` and `(49283557/50000000, 4503/2000, 1/10)` are available whenever the Hecke zero supremum beta is at least `51/100`, then beta is at most `4369351/5000000`, and the corresponding Dirichlet functions are nonzero strictly to its right with the principal pole excluded. Lean reports only `propext`, `Classical.choice`, and `Quot.sound` for these declarations. The compiler is Lean 4.34.1, commit `5045d0056413266e57c625dcd7c365b10e377c52`, binary SHA-256 `e8baaa71855a616dc351028f3ad2200051b0671f423a1696a100e809302d5550`; `candidate-manifest.json` binds all changed sources to the pinned tracker revision. The full target was compiled subsequently, as recorded below; the conditional output alone does not discharge these hypotheses or establish a significant new zero-free region.

`package-source-audit.json` inventories the 20 pinned package source trees. All 20 Git HEADs match the tracker Lake manifest. Mathlib and the 17 packages other than PNT/Rellich have no tracked or untracked changes; PNT has 8 modified and 47 untracked files, and Rellich has 15 modified files. We independently created clean worktrees at their pinned commits and applied the tracker's pinned Lean 4.34.1 patches: their complete Git status lists and every changed/untracked file's SHA-256 match the active PNT and Rellich trees exactly. PNT's 47 untracked files are additions from that patch, not unexplained source edits. No ignored Lean source exists outside the package `.lake` directories in the audited trees. `check_package_sources.py` records the per-file hashes; its expected worktrees must first be freshly created at the pinned HEADs and patched, as described. This audits source trees, not the authenticity of compiled package OLeans or independently the content and correctness of the compatibility patches.

## Completed native Lean build and theorem audit

The staged `0.8738702` candidate's pinned native Lean 4.34.1 build has now completed. The final scheduler compiled 1,614 modules after earlier restored or separately compiled dependencies; its full log is [lean-full-build.log](lean-full-build.log). It ended with `all modules compiled successfully 1614`, with no cgroup OOM event. This is an incremental build using the documented official cache and previously compiled dependencies, not a fresh replay of every imported proof.

A separate `lean --stdin` query exited 0 and reports the target and its transitive axioms in [lean-candidate-axioms.log](lean-candidate-axioms.log). Its theorem has no analytic premises: for any positive modulus and Dirichlet character, it states nonvanishing for real part greater than `4369351/5000000`, except the principal pole. `#print axioms` reports exactly `propext`, `Classical.choice`, and `Quot.sound`. [lean-candidate-audit.json](lean-candidate-audit.json) records the exact query hash, compiler hash and Lean path; source-file hashes are in [candidate-manifest.json](candidate-manifest.json). The independently verified package-source provenance is recorded in [package-source-audit.json](package-source-audit.json).

This is native Lean compilation evidence for the staged formal theorem, not a fresh `leanchecker` replay of the entire dependency closure and not tracker admission. Comparator, NanoDa and con-ron have not been run on this candidate, and an independent audit of the imported analytic framework and its interpretation remains outstanding. The arithmetic gain over PR94 is `2.14·10^(−6)`, and no claim of a significant new analytic zero-free region is made on that basis.

## Full target compilation

The active pinned Lean 4.34.1 build subsequently completed `Candidate.Main`: `lean-endpoint-build.log` ends with `all modules compiled successfully 1614`, after reuse of the separately verified tracker build cache and compilation of the remaining modules. `lean-candidate-axioms.log` records `Candidate.bound` at `4369351/5000000` for all mathlib Dirichlet characters with the principal pole excluded, with `[propext, Classical.choice, Quot.sound]` as its reported transitive axioms. This is one Lean kernel build using compiled dependency caches; independent full rechecking of the cache, correspondence with conventional L-functions, the other tracker kernels, and tracker admission remain separate evidence gates. It is an incremental candidate improvement, not an assertion of a significant new region or of external peer review.
