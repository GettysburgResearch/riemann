# Lean build attempt: OpenAI 7/8 comparator challenge (family 003)

```text
Status: VERIFICATION (formal build COMPLETED, Addendum A; comparator ACCEPTS the 7/8 zeta challenge,
  Addendum B);
  no mathematical claim beyond what the build shows. Sections 1-8 are the original partial
  attempt and are kept unchanged as the record of that attempt
Scope: Kernel build of the import closure of OAI.NumberTheory.DirichletL.Nonvanishing, the solution
  module named in ComparatorChallenges/QuasiRiemannHypothesis.json and DirichletSevenEighths.json.
  The theorem in question is the quasi-RH zero-free half-plane Re s > 7/8. It is NOT RH.
  Hecke: module built and `#print axioms` standard (Addendum C). The upstream SiegelZeros
  solution: see Addendum C. The wave's own Siegel corollary is in ../lean/.
Exact sources or dependencies: repo ref pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6
  (draft PR 908); tree standalone/2026-10-07-openai-quasi-riemann-import/upstream/lean =
  git tree ef5d0c6c35578aacaa83cca392c6752fcc8b1784; this is a byte-exact import of
  openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a lean/. Lean leanprover/lean4:v4.34.1
  (commit 5045d0056413266e57c625dcd7c365b10e377c52); Mathlib d13f23b723b8a846827a245b89c10fc7d3f11612;
  lake-manifest.json unchanged (sha256 cf6105a25d9dca2f...). All 42 packages are at their manifest revisions.
What was actually run: the original attempt (below), then three bounded resumptions of the same
  incremental build (one stopped by the background time limit, one by a full disk while writing an
  .olean, one completing): "Build completed successfully (7061 jobs)", 0 errors, 0 `sorry`
  warnings in the final log. Then `#print axioms` and a statement-pinning check (Addendum A),
  and comparator (Addendum B).
Smallest remaining gap: the kernel check checks the Lean statement against Lean + Mathlib (from
  its binary cache) + the 23 patched third-party packages, under comparator's trust assumptions
  (Addendum B). It does not check the manuscript's text, and no human has reviewed the Lean
  development.
```

## Addendum A (10 Oct 2026, later the same day): build completed; axioms are standard

The incremental build was resumed three times from the scratch state of Section 7:
* The first resumption hit the 2-hour background limit.
* The second failed only because the disk filled while writing an `.olean` ("failed to write");
  that is an environment error, not a Lean error. About 1.2 GB of caches were freed.
* The third finished (scratch log `step3_build_resume4.log`, because the first resumption was
  numbered 2; its tail is `results/lean_build_resume4_tail.log`): `✔ [7061/7061] Built OAI.NumberTheory.DirichletL.Nonvanishing`,
  "Build completed successfully (7061 jobs)". Its log has 0 errors and 0
  `declaration uses 'sorry'` warnings.

`lake env lean scripts/Axioms.lean` (committed as `../lean/checks/Axioms.lean`; output in
`results/lean_axioms.log`) then printed:

```text
@OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re : ∀ {s : ℂ}, 7 / 8 < s.re → riemannZeta s ≠ 0
@OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re : ∀ {q : ℕ} [inst : NeZero q]
  (χ : DirichletCharacter ℂ q) {s : ℂ}, 7 / 8 < s.re → ¬(χ = 1 ∧ s = 1) → DirichletCharacter.LFunction χ s ≠ 0
'OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re' depends on axioms: [propext, Classical.choice, Quot.sound]
'OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re' depends on axioms: [propext, Classical.choice, Quot.sound]
'OAI.SevenEighths.ProbeFinalAssemblyUnconditional.detector_certified_bands' depends on axioms: [propext, Classical.choice, Quot.sound]
```

So there is no `sorryAx`, no `Lean.ofReduceBool` (`native_decide`), no `Lean.trustCompiler` and no
project-declared axiom behind either theorem.

A second check file (`scripts/Statement.lean`, committed as `../lean/checks/Statement.lean`;
output in `results/lean_statement.log`) pins the statements:
* it elaborates both theorems against the explicit types written with `_root_.riemannZeta` and
  `_root_.DirichletCharacter.LFunction`;
* it reports the defining modules: `riemannZeta` from `Mathlib.NumberTheory.LSeries.RiemannZeta`,
  `DirichletCharacter.LFunction` from `Mathlib.NumberTheory.LSeries.DirichletContinuation`.

The theorem is therefore about Mathlib's own zeta and Dirichlet `L`-functions, not about a
project redefinition. Mathlib itself is unmodified at d13f23b7 (`git status` clean).

The "has local changes" warnings that lake prints are the 23 shipped third-party patches of
Section 3. They are part of the trusted input, and they were not reviewed beyond Section 3's checks.

What this does and does not establish:
* It establishes that Lean's kernel accepted a proof of `∀ s, 7/8 < Re s → ζ(s) ≠ 0` (and the
  Dirichlet analogue), built on this machine from the pinned sources (Mathlib from its binary
  cache, not rebuilt), using only the three
  standard axioms.
* It is not a review of the 30 Sep manuscript, and it is not RH. The half-plane `Re s > 7/8` says
  nothing about the critical line.
* `#print axioms` trusts the elaborated environment. Comparator's export-and-replay is the
  stronger check (Addendum B).

## Addendum B (10 Oct 2026): comparator accepts the 7/8 zeta challenge

Comparator was run on the upstream challenge `ComparatorChallenges/QuasiRiemannHypothesis.json`
with the toolchain-matched tools of Section 5:
* comparator d03acab, lean4export 076e8e57, landrun 0.1.18 with `--best-effort`;
* challenge JSON sha256 `46ebb7ed…f320`; challenge Lean file sha256 `065f8c9a…12cc5`;
* permitted axioms `propext`, `Quot.sound`, `Classical.choice`; `enable_nanoda: false`.

```text
Building ComparatorChallenges.QuasiRiemannHypothesis            (sandboxed; no-op, already built)
Exporting #[…, OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re, …] from ComparatorChallenges.QuasiRiemannHypothesis
Building OAI.NumberTheory.DirichletL.Nonvanishing               (sandboxed; no-op, already built)
Exporting #[…] from OAI.NumberTheory.DirichletL.Nonvanishing
Running Lean default kernel on solution.
Lean default kernel accepts the solution
Your solution is okay!
```

The run took 1094 s wall time, exited 0, and peaked at about 7 GB RSS in lean4export. The full
log is [results/comparator_QuasiRiemannHypothesis.log](results/comparator_QuasiRiemannHypothesis.log).

What comparator adds over `#print axioms`:
* It exports the challenge statement from a module that imports only Mathlib, and checks that
  the solution's theorem has the identical statement over identical constants. So
  `riemannZeta`, `Complex.re` and the rest are Mathlib's.
* It re-checks the exported proof with a fresh Lean kernel (`Environment.replay`), outside the
  elaborator, and checks that only the permitted axioms occur.

For the zeta theorem, the patched third-party packages cannot change the meaning of the
statement: comparator compared it against an export from a module that imports only Mathlib,
and Mathlib is unpatched. The patched packages' proofs are among the replayed constants. This
argument applies to the comparator-checked zeta theorem only. For the Dirichlet theorem,
`Statement.lean` elaborated the type in an environment that also loads the patched packages.

Trust assumptions, stated as comparator's README asks:
* **Assumption 2 is not met.** The solution was compiled outside the sandbox before the check,
  so a malicious build could in principle have altered files the check reads. This is a
  non-adversarial reproduction.
  * As a partial guard, none of the 8,548 Mathlib `.olean` files has a modification time later
    than the cache unpack (12:48–12:51 UTC); `find -newermt "2026-10-10 13:00"` finds 0.
  * Mathlib's git tree is clean at d13f23b7. That checks the sources, not the `.olean` files:
    **Mathlib was not rebuilt from source.** Its oleans came from Mathlib's binary cache
    (`lake exe cache get`), and the exported definition of `riemannZeta` is whatever the cached
    olean contains.
  * The mtime window (12:48–12:51) overlaps the unsandboxed lakefile `run_cmd` clone-and-patch
    step of `lake exe cache get` (12:43–12:51). So the guard does not cover code run at
    configuration time.
* The landrun sandbox ran in `--best-effort` mode on Landlock ABI v7, and the systemd
  `AF_UNIX` wrapper was not used (Section 5).
* Only the Lean kernel was used. No second kernel, such as nanoda, was run.

**What is established:** under these assumptions, Lean's kernel accepts a proof, from the
three standard axioms, of

    ∀ s : ℂ, 7/8 < Re s → riemannZeta s ≠ 0

for Mathlib's `riemannZeta`.

**What is not established:**
* This is not a review of the 30 Sep manuscript's text, and not a human review of the Lean
  development.
* It is not RH. The half-plane `Re s > 7/8` says nothing about the critical line.

Corollaries proved in this wave on top of this theorem (strip, Dirichlet strip, Siegel challenge)
are in [../lean/](../lean/README.md). The Hecke build and the comparator runs on the Dirichlet,
Hecke and corollary challenges are recorded in Addendum C.

## Addendum C (10 Oct 2026): Hecke build, corollaries, and further comparator runs

**Hecke 7/8.** `lake build OAI.NumberTheory.DirichletL.Hecke.Nonvanishing` added the 2 missing
modules (68 lines) to the completed closure: "Build completed successfully (7062 jobs)", in 21 s.
`../lean/checks/HeckeAxioms.lean` then printed (`results/lean_hecke_axioms.log`):

```text
OAI.SevenEighths.HeckeFamily.LFunction_ne_zero_of_seven_eighths_lt_re : ∀ (χ : OAI.SevenEighths.HeckeFamily.Character)
  {s : ℂ}, 7 / 8 < s.re → ¬(χ.residue = 1 ∧ s = 1) → OAI.SevenEighths.HeckeFamily.LFunction χ s ≠ 0
'…LFunction_ne_zero_of_seven_eighths_lt_re' depends on axioms: [propext, Classical.choice, Quot.sound]
```

The Hecke statement uses project-defined objects (`HeckeFamily.Character` and an `LFunction`
built from a lattice theta construction), written into the challenge file itself. They are not
Mathlib objects. Nobody has checked that they match the manuscript's finite-order Hecke
`L`-functions of `Q(√−3)`.

**Corollaries of this wave** ([../lean/](../lean/README.md)):
* clean build log: `results/lean_corollary_build.log`;
* axioms: `results/lean_corollary_axioms.log`, all `[propext, Classical.choice, Quot.sound]`.

**Comparator runs after Addendum B.** These are run sequentially with the same tools and settings
as in Addendum B, and their outcomes are recorded here as they complete:

| challenge JSON | solution module | outcome |
|---|---|---|
| upstream `DirichletSevenEighths.json` | `OAI.NumberTheory.DirichletL.Nonvanishing` | **accepted**: "Lean default kernel accepts the solution", 1108 s, exit 0 ([results/comparator_DirichletSevenEighths.log](results/comparator_DirichletSevenEighths.log)). Like the zeta challenge, the challenge module imports only Mathlib, so `DirichletCharacter.LFunction` is Mathlib's and the Addendum B statement-meaning argument now covers this theorem too |
| upstream `HeckeSevenEighths.json` | `OAI.NumberTheory.DirichletL.Hecke.Nonvanishing` | pending |
| wave `SiegelFromSevenEighths.json` (upstream `SiegelZeros` challenge module) | `OAI.QRHWave.SiegelFromSevenEighths` | pending |
| wave `QRHWaveStrip.json` (challenge written in this wave) | `OAI.QRHWave.ZetaZeroStrip` | pending |

## 1. Verdict of the original attempt (superseded by Addendum A): PARTIAL

The 7/8 closure was **not** fully built, so this attempt makes **no** kernel-checked claim about the 7/8 theorem. Comparator was not run on it, and no axiom list exists for it.

The build ran for 98.8 minutes of wall time. In that time it produced:

- 350 of 2,924 OAI modules (12.0% of modules, 40.4% of source lines: 196,375 of 486,490);
- all 19 external non-Mathlib modules the closure needs (15 RellichKondrachov and 4 PrimeNumberTheoremAnd, including `PrimeNumberTheoremAnd.Wiener` and `RellichKondrachov...Euclidean.Rellich`);
- **0 errors and 0 warnings**. In particular, no `declaration uses 'sorry'` warnings appeared in any compiled module.

The build was stopped deliberately (SIGTERM, exit 143) at the 2-hour budget. Nothing failed.

Why it did not finish:

- The machine has 4 cores shared with other research jobs (load average 4.5 to 12 throughout).
- The build ran at `nice 19` with 3 parallel Lean processes.
- The build process received 97.2 CPU-minutes in 98.8 wall minutes, which is about one effective core.

Measured compile cost was about 33.6 source lines per CPU-second (196k lines in 97 CPU-min). From that:

| Quantity | Estimate |
|---|---|
| Total closure | about 4 CPU-hours |
| Remaining work | about 2.4 CPU-hours |
| Remaining critical path (longest unbuilt import chain) | about 23k lines, about 18 min single-process |
| Remaining wall time, 3 dedicated cores | about 1 to 1.5 hours |
| Remaining wall time, this shared machine at nice 19 | about 2.5 hours or more |

The import graph is deep (404 modules on the longest chain). For long stretches, only one module can compile at a time.

What *is* established, narrowly:

- The pinned dependency set resolves exactly as the manifest says, with no drift.
- The shipped patches apply cleanly at the pinned commits.
- Mathlib loads from cache with no rebuild.
- The two challenge statements elaborate.
- The first 40% (by lines) of the solution closure, plus its external dependencies, compiles under Lean v4.34.1 without errors or `sorry` warnings.

A compile without warnings is not an axiom audit. A module can rely on a declared `axiom` without any warning. The earlier lexical audits found no `axiom` declarations in the closure, but that was not re-checked here by the kernel.

## 2. What the challenge actually asserts

`ComparatorChallenges/QuasiRiemannHypothesis.lean` (sha256 `065f8c9a01d28db7...`), verbatim:

```lean
import Mathlib

namespace OAI

theorem riemannZeta_ne_zero_of_seven_eighths_lt_re
    {s : ℂ} (hs : (7 / 8 : ℝ) < s.re) : riemannZeta s ≠ 0 := by
  sorry

end OAI
```

`ComparatorChallenges/DirichletSevenEighths.lean` (sha256 `8fb13ad977bca104...`), verbatim:

```lean
theorem LFunction_ne_zero_of_seven_eighths_lt_re
    {q : ℕ} [NeZero q] (χ : DirichletCharacter ℂ q) {s : ℂ}
    (hs : (7 / 8 : ℝ) < s.re) (hpole : ¬ (χ = 1 ∧ s = 1)) :
    _root_.DirichletCharacter.LFunction χ s ≠ 0 := by
  sorry
```

This sits inside `namespace OAI` / `namespace DirichletCharacter`.

`QuasiRiemannHypothesis.json` has these fields:

- `challenge_module` ComparatorChallenges.QuasiRiemannHypothesis
- `solution_module` OAI.NumberTheory.DirichletL.Nonvanishing
- `theorem_names` [OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re]
- `definition_names` []
- `permitted_axioms` [propext, Quot.sound, Classical.choice]
- `enable_nanoda` false

`DirichletSevenEighths.json` is identical except that the theorem name is `OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re`. Both challenges therefore share one solution module, so one build serves both.

Reading of the statement:

- `riemannZeta` is Mathlib's definition at d13f23b: `def riemannZeta := hurwitzZetaEven 0` (`Mathlib/NumberTheory/LSeries/RiemannZeta.lean:121`). This is a total function on ℂ. Its value at the pole s = 1 is a junk value, and Mathlib proves `riemannZeta_one_ne_zero`, so the statement is harmless at s = 1.
- `DirichletCharacter.LFunction` is Mathlib's definition (`Mathlib/NumberTheory/LSeries/DirichletContinuation.lean:61`). It covers every positive modulus, including imprimitive characters. The principal pole is excluded explicitly.
- The statements are **open half-plane** nonvanishing assertions with no extra hypotheses. They say nothing about Re s = 7/8 or about 1/2 < Re s ≤ 7/8, and they do not assert RH or GRH.

The solution-side theorems in `OAI/NumberTheory/DirichletL/Nonvanishing.lean` have the same text. They are proved by `SevenEighths.ProbeFinalAssemblyUnconditional.zeta_nonzero` and `.dirichlet_nonzero` from `Detector/FinalAssemblyUnconditional.lean`. The `Nonvanishing.lean` module itself was **not** reached by this build.

Scope caution:

- A completed build plus comparator would check that the formal statement follows from Mathlib's definitions using the permitted axioms.
- It would **not** check source fidelity, meaning whether the Lean development follows the 7/8 manuscript's argument or whether that argument is right on paper. Those are separate questions; see the repo's MATHEMATICAL_AUDIT and Kintali review.
- For the zeta and Dirichlet statements, the objects are Mathlib's own. So the statement-fidelity risk is low *if* comparator passes.

## 3. Environment and pins

| Item | Value |
|---|---|
| elan | 4.2.4 (227caca13 2026-08-25), installed with `--no-modify-path --default-toolchain none` into scratch `ELAN_HOME` |
| Lean / Lake | 4.34.1, commit 5045d0056413266e57c625dcd7c365b10e377c52; Lake 5.0.0-src+5045d00 |
| Mathlib | d13f23b723b8a846827a245b89c10fc7d3f11612 (cache: 8,908 files from cache.mathlib.org, `mathlib4-master` prefix) |
| lakefile.lean | sha256 4cca977ebece444b... (unchanged) |
| lake-manifest.json | sha256 cf6105a25d9dca2f... (unchanged after all lake commands; `lake update` was never run) |
| Package revisions | all 42 manifest entries checked with `git rev-parse HEAD`: 0 mismatches |
| Environment | `GLIBC_TUNABLES=glibc.malloc.mmap_max=0:glibc.malloc.arena_max=1` (vm.max_map_count is 65530 here); `LEAN_NUM_THREADS=3`, which also limits Lake to 3 concurrent Lean processes; `nice -n 19` |
| Machine | 4 vCPU, 16 GB RAM (about 12 to 13 GB available throughout), Linux 6.18 |

Dependency patches:

- The lakefile's `run_cmd` cloned 11 packages (iut, tate-curves-theta, genl, heights, pi1, orbicurve-cores, oka, tempered-fundamental-groups, elliptic-curves, formal-schemes, belyi) and applied their patches automatically before resolution.
- The other 12 patches are applied only by the lakefile's `post_update` hook, which runs only under `lake update`. These are fixed-point-theorems, PrimeNumberTheoremAnd, Zeta3Irrational, rellich-kondrachov, carleson, StrongPNT, AbsorptionCutoff, AINTLIB, ClassFieldTheory, schoenflies-lean, SphereEversion and gromov.
- To avoid `lake update`, I replicated that hook in a script. For each package it checks HEAD against the manifest revision, then runs `git apply --check`, then `git apply`, then a reverse check to verify. All 12 applied cleanly.
- The PNT+ patch (sha256 0890432340c00259...) removes 2 `sorry` lines and adds none. Among other changes, it rewrites PNT+'s `lakefile.toml` (narrower targets) and its `lean-toolchain` (v4.34.0 to v4.34.1).
- **This patching is part of the trusted input and is not upstream PNT+ or Rellich–Kondrachov.** Only the two patched packages actually imported by the closure (PNT+ `Wiener` and its 3 local imports, and the 15 Rellich modules) were compiled.

## 4. Commands and timings (UTC, 2026-10-10)

| Time | Step | Result |
|---|---|---|
| 12:40:54 | `git archive pr908 <lean dir> \| tar -x` into scratch | OK |
| 12:41 | `sh elan-init.sh -y --no-modify-path --default-toolchain none`; `elan toolchain install leanprover/lean4:v4.34.1` | OK, 59 s |
| 12:43:14 to 12:51:56 | `nice -n 19 lake exe cache get` (clones all 42 packages; run_cmd patches 11; builds `cache` exe; downloads Mathlib cache) | exit 0, 8 min 42 s |
| 12:52 | post_update patch script (12 packages) | 12/12 OK |
| 12:52:32 to 12:53:21 | `lake build ComparatorChallenges.QuasiRiemannHypothesis ComparatorChallenges.DirichletSevenEighths` | OK, 8,925 jobs (Mathlib replayed from cache, nothing rebuilt); only warnings are the two intended `declaration uses 'sorry'` |
| 12:53:28 to 14:32:14 | `nice -n 19 lake build OAI.NumberTheory.DirichletL.Nonvanishing` | stopped by SIGTERM at budget (exit 143). Lake job counter 4,486 of 7,061. 350/2,924 OAI modules, 19/19 external modules, 0 errors, 0 warnings. real 98m46s, user 97m12s, sys 13m09s |

Further details:

- Per-module wall times averaged 26.3 s.
- The slowest modules took about 100 s each: `CubicSieve.PaddedPassage`, `Mellin.LogProfiles`, `GaussSum.CompletedDyadicRows` and `Eisenstein.MeromorphicResolvent`.
- Disk use at the end was 14 GB in scratch: toolchain 3.0 GB, Mathlib with cache 7.3 GB, other packages, build outputs and tools. A further 0.45 GB of Mathlib `.ltar` files sits in `~/.cache/mathlib`.

Note on earlier repo records: the w5copg branch reported "about 4,400 of 7,061 build jobs". Roughly the first 4,070 jobs of this target are Mathlib and other dependency replays. The job counter therefore greatly overstates OAI progress; module counts are the meaningful measure.

## 5. Comparator tooling (built, self-tested, not run on the 7/8 challenge)

| Tool | Revision / version | Notes |
|---|---|---|
| comparator | leanprover/comparator d03acab154d269c06e60e4de7e4cc85deebff94b ("bump toolchain to v4.34.0"), the last commit before the v4.35 RC bumps | `lean-toolchain` overridden locally from v4.34.0 to v4.34.1 so that it and lean4export match the project's olean format. Binary sha256 afa65e57a1770f59... |
| lean4export | 076e8e57707e813375e8f9da8bf989799ace9680 (pinned by that comparator manifest) | built with v4.34.1; sha256 8c5d64ba68f4d3a6... |
| landrun | Zouuup/landrun 811cfff51ceaf3d9843708aa6d22e9b84ccac8b4, v0.1.18, built with go1.24.7 | sha256 38b0fdcbd2862f8e... |

Build time was 69 s for comparator and lean4export, and 46 s for landrun.

Landlock behaviour on this machine:

- The kernel exposes Landlock ABI v7. In strict mode landrun 0.1.18 refuses to run, because it wants v9.
- Comparator invokes landrun with `--best-effort`. In that mode a write outside the allowed paths was denied ("Permission denied") and an allowed write succeeded, so filesystem sandboxing is enforced.
- Comparator's README notes a landrun weakness that its `systemd-run --property=RestrictAddressFamilies=~AF_UNIX` wrapper guards against. That wrapper was not set up.

Comparator self-test: `lean --run runtests.lean simple_match simple_mismatch simple_axiom_issue proj_trick`, with the real landrun and the lean4export above, gave 4/4 PASSED. This shows that the toolchain-matched comparator works on this machine.

The intended run, once the build is complete:

```sh
cd <lean dir>
COMPARATOR_LANDRUN=<scratch>/tools/bin/landrun \
COMPARATOR_LEAN4EXPORT=<scratch>/tools/comparator-v4341/.lake/packages/lean4export/.lake/build/bin/lean4export \
  lake env <scratch>/tools/comparator-v4341/.lake/build/bin/comparator ComparatorChallenges/QuasiRiemannHypothesis.json
# same for ComparatorChallenges/DirichletSevenEighths.json
```

Comparator's README states its trust assumptions. Assumption 2 requires that the solution was not compiled beforehand in the checking environment, which would be violated here because this attempt compiles the solution outside the sandbox first. For a non-adversarial reproduction that is acceptable, but it should be stated whenever the result is reported. A completed comparator run with `enable_nanoda: false` uses only the Lean kernel; no second kernel is involved.

## 6. Axioms

**Not obtained.** `#print axioms OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re` needs the solution module's olean, which was not reached.

The prepared check file `<scratch>/scripts/Axioms.lean` contains:

```lean
import OAI.NumberTheory.DirichletL.Nonvanishing
#check @OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re
#check @OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re
#print axioms OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re
#print axioms OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re
#print axioms OAI.SevenEighths.ProbeFinalAssemblyUnconditional.detector_certified_bands
```

Run it from the lean directory with `lake env lean <scratch>/scripts/Axioms.lean`. The expected acceptable output is exactly `[propext, Classical.choice, Quot.sound]`. Any `sorryAx`, `Lean.ofReduceBool`, `Lean.trustCompiler` or project-declared axiom would be critical.

## 7. How to resume

The scratch state is intact at `/tmp/claude-0/-home-user-riemann/0f40aeb7-3b99-59f5-bdd3-8b0e9e4502dc/scratchpad/leanbuild/` (session scratch, so not durable). Lake is incremental, so re-running continues from the 350 built modules:

```sh
. <scratch>/scripts/env.sh   # ELAN_HOME, PATH, P, GLIBC_TUNABLES, LEAN_NUM_THREADS
<scratch>/scripts/step3_build.sh > <scratch>/logs/step3_build_resume.log 2>&1
<scratch>/scripts/progress.sh           # olean counts
```

Then run `lake env lean <scratch>/scripts/Axioms.lean` and the comparator commands in Section 5.

To reproduce from scratch elsewhere, the steps are:

1. Extract the pr908 tree.
2. Run `lake exe cache get`.
3. Run `<scratch>/scripts/apply_post_update_patches.sh`, or run upstream's `lake update` and then confirm the manifest hash is unchanged.
4. Run the build.

On a dedicated 4-core machine the full closure should take about 1.5 to 2 hours. Here, sharing cores at nice 19, it is impractical within 2 hours.

## 8. Not done / not claimed

- No claim that the 7/8 theorem is kernel-checked. Neither comparator nor `#print axioms` was run on it.
- Hecke (`OAI.NumberTheory.DirichletL.Hecke.Nonvanishing`) and SiegelZeros were not attempted.
- No source-fidelity review: does the Lean development follow the September 30 manuscript, and does the manuscript's argument hold?
- No review of the 23 third-party patches beyond confirming that they apply at the pinned commits and that the PNT+ patch adds no `sorry`.
- Nothing here bears on RH itself. The target statement is a zero-free half-plane Re s > 7/8 for ζ and Dirichlet L-functions.
