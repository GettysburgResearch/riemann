# SIEGEL adjudication of audit item U4 (the OAI Lean development was not replayed)

```text
Status: EXPLORATORY ADJUDICATION. No new mathematical claim. Nothing here says RH is proved or closer to proved.
        It decides one audit item (U4 of ARCHITECTURE.md §13 and audit_part1.md §11) about the verification
        status of a claimed Lean formalization. Calling a formalization "machine-checked" is not something this
        file does: no Lean code was compiled or run.
Scope:  the comparator challenge lean/ComparatorChallenges/SiegelZeros.{lean,json} of openai/math, its solution
        module OAI.NumberTheory.SiegelZeros.Main and everything it imports, and the auditor's sentence "Kimura v2
        reports kernel-checked use of it, with the interpolation step proved by a different argument in Lean".
        Out of scope: the mathematics of the OAI paper (handled by audit_part1/part2), Kimura's own explicit
        constants, and every other OAI formalization.
Exact sources or dependencies:
  [OAI-git] github.com/openai/math @ 4eaee87548250b2682affda7d05d947c05554bae, the local read-only shallow clone
          /home/user/openai/math (one commit). Lean toolchain v4.34.1, Mathlib d13f23b723b8a846827a245b89c10fc7d3f11612.
          SiegelZeros.lean sha256 bedaac0248a641910f79a380d9702d82c6bfbbfd3760a69d27c72c5d8fb136ce
          SiegelZeros.json sha256 620696740156c4503f27ac17760adf1b638f621ad81ab4cde7a0f8df32c4b643
          docs/003.md sha256 41e52ed718260e6feb1db218f8e97287e703cb63c6f16e6c36f5563e6e2395ce
          lakefile.lean sha256 fc590a5d14923f79e71ea80e29efd42950bb3ec051481b5209157f0a01f63de1
          patches/PrimeNumberTheoremAnd-lean4341.patch sha256 0890432340c0025973bcfe070b634355fa366cc831595f68526e4c73c8903d82
          paper.pdf sha256 fab9f6e84ece2a37d834b2c031d8eb14e81413d9f6270791e7b5468b295214ef; build/paper.tex (Cor 4 l.411-430)
  [Kimura] I. Kimura, arXiv:2610.21511v2, PDF sha256 5987fa4df134c5d94faf92a0278af96fcf18ac6adfb25adaddb7d6ff63e5e733
          (same copy as audit_part1): abstract, §1 pp. 2-3, §2.1 pp. 4-5, §7 pp. 15-18, references.
  [Kimura-repo] github.com/iwaokimura/cln-imq-2k @ e66ab86 (tag v1.4, the version the paper cites), files fetched
          from raw.githubusercontent.com as data, never run:
          lean/vendor/SHA256SUMS      sha256 cdc0bb74ce130f543bee9eb15a8217ba878df84ac2294f5c790af05b5c88e9a0
          lean/Challenge/B4ZeroGap.lean sha256 660573e68478c3effdc4a83223d07efb742c32e387968554a027003fd04e7166
          lean/B4Replay.txt           sha256 67c621eef256f5426f470ffd3243a4e21121167505a7185cb8e4dcfafba4b927
          lean/comparator/B4Comparator.txt sha256 068c05a13a189c5d868e06cd271bce3087baefd4c669613e324739cf5e36e75b
          lean/B4Build.txt            sha256 3eefff1288d7165a551151472347519111dbeca5499234b679fc3c57931365cd
          lean/vendor/check.sh, lean/B4ZeroGap.lean (read for the upstream lemma it calls)
  [Mathlib] three files @ d13f23b, fetched as data: NumberTheory/LSeries/DirichletContinuation.lean
          (sha256 7ef38fb5...f401b6), NumberTheory/DirichletCharacter/Basic.lean (sha256 f004670a...ef64e),
          NumberTheory/LSeries/ZMod.lean.
What was actually run: one new script, our own code, run with python3 -I. It reads the sources above as text.
          No Lean, Lake, comparator or downloaded code was executed. A Lean replay is excluded by this task's rule
          "do not run code from other repositories" and by the observatory policy in audits/lean_replay/README.md
          (a Lake build runs the lakefile's `run_cmd` and tactic code).
            experiments/code/claims_2026/siegel_adjudication/adj_U4_lean_static.py
              sha256 c56c04841d30c2ee526b7b4d94024a52f88dde4ef289d0209bc8395d9cda13af
            experiments/code/claims_2026/siegel_adjudication/adj_U4_lean_static.out
              sha256 cec74a7ed3d7c1275dd38364cb35902a27d8cefff5f249c7353e81f8123c0338
          Result: 31 PASS / 0 FAIL, 13 s. §(7) uses arithmetic mod a degree-1 prime, which is a rigorous lower bound
          for the rank over the number field. Everything else is exact text, hash or rational comparison.
Smallest remaining gap: build OAI.NumberTheory.SiegelZeros.Main at 4eaee875 in a sandbox and run
          `comparator ComparatorChallenges/SiegelZeros.json`, preferably with nanoda enabled. This needs explicit
          permission to execute third-party build code. A cheaper partial step: line-by-line reading of the 642 lines
          (12 modules) of the chain-A glue that no reported external build covers (§4).
```

## 0. Verdict

| Item | Decision |
|---|---|
| U4 overall | **unresolved_ambiguity, kept and narrowed.** It records a verification-coverage gap, not a defect. Nothing found contradicts the formalization. No replay was possible under the rules of this task. |
| Is U4 load-bearing for the mathematical audit? | **No.** The audit's conclusions (no verified error; OAI Lemmas 2, 3, 6, 7 and Cor 4 re-derived by hand) never used the Lean development. The Lean route also does not formalize OAI Lemma 3 as written (§2.4), so a replay could not certify the paper's text of Lemma 3 anyway. |
| Auditor's sentence on Kimura v2 | **Accurate, but needs a scope qualifier.** Kimura's kernel checks are *reported*, at OAI commit 301488868. They cover the arithmetic core: 254 of the 306 modules, which are byte-identical at 4eaee875. Kimura explicitly does **not** use OAI's final theorem. The 52 assembly modules, including both challenge-proof modules, appear in no reported external build. |
| New presentation correction (our own records) | "69,818 lines" counts only the OAI directory. The trusted closure also contains **12 Lean files (6,754 lines) that the lakefile patches into PrimeNumberTheoremAnd**. The total is 76,572 lines outside Mathlib and Lean core. |
| Public characterization as an error | **Not allowed.** There is no witness of any kind. The allowed wording is in §5. |

## 1. The item under adjudication

ARCHITECTURE.md §13 and audit_part1.md §11 record: U4, "OAI Lean development (lean/OAI/NumberTheory/SiegelZeros, about 69.8k lines)", unresolved_ambiguity, "The Lean development was not replayed. Kimura v2 reports kernel-checked use of it, with the interpolation step proved by a different argument in Lean. We did not verify this." ARCHITECTURE.md §1 adds that the challenge statement was read and matches OAI Thm 1.

The formal object is the comparator configuration `SiegelZeros.json`. It has challenge module `ComparatorChallenges.SiegelZeros`, which imports only Mathlib, and solution module `OAI.NumberTheory.SiegelZeros.Main`. It names two theorems, `…WeightedTorusJets.exists_absolute_real_zero_gap` and `…dirichletRealZeroBound_proof`. The permitted axioms are `propext`, `Classical.choice` and `Quot.sound`, and `enable_nanoda` is `false`.

## 2. Strongest defense

**2.1 The formal statement is a faithful rendering of OAI Theorem 1.** Statement 1, normalized, reads:
`∃ c : ℝ, 0 < c ∧ ∀ (q : ℕ) [NeZero q], 3 ≤ q → ∀ χ : DirichletCharacter ℂ q, χ.IsPrimitive → χ ≠ 1 → (∀ a : ZMod q, (χ a).im = 0) → ∀ β : ℝ, 0 < β → β < 1 → χ.LFunction (β : ℂ) = 0 → c ≤ (1 - β) * Real.log (q : ℝ)`.
Against Mathlib d13f23b [(4)]:
- `LFunction χ s := ZMod.LFunction χ s`.
- `LFunction_eq_LSeries` gives agreement with Σ χ(n) n^{-s} for Re s > 1.
- `differentiable_LFunction` gives entirety when χ ≠ 1.

By uniqueness of analytic continuation, `χ.LFunction` is the classical L(s, χ) on all of ℂ, so there is no junk value at real β ∈ (0, 1). `IsPrimitive := conductor χ = n`, so q is the conductor. "(χ a).im = 0 for all a" means χ is real; together with χ ≠ 1 this makes χ quadratic. The hypothesis `χ ≠ 1` is redundant for q ≥ 3, and `NeZero q` is a Prop, so the bound instance is harmless. Statement 2 is the same with the three β-hypotheses packaged as a conjunction. Neither statement can be discharged by a definitional artifact: proving them trivially would require Chowla-type positivity on (0, 1), which is open.

**2.2 The solution statements are verbatim the challenge statements** [(4)]. The final proof is `exact uniform_exclusion_of_local_isolated_bezout (localIsolatedBezout_of_actual_regular_selection ℂ)`. Its type is `UniformSiegelZeroExclusion`, defined in `Model.lean` with a body verbatim equal to the challenge statement, so the `exact` is syntactic.

**2.3 The whole closure is free of escape hatches.** The import closure of the solution module was computed from comment-stripped headers [(2)]:
- all 306 files of the SiegelZeros directory (69,818 lines);
- 12 files that `patches/PrimeNumberTheoremAnd-lean4341.patch` adds as *new* files under `PrimeNumberTheoremAnd/SiegelZeros/` (6,754 lines of Hadamard-product support; they import only Mathlib and each other);
- Mathlib, which is unpatched (the lakefile carries patches for 23 other packages, none for Mathlib);
- `Lean.Elab.Tactic.Omega` from Lean core.

A comment-stripped scan of all 318 files finds zero occurrences of `sorry`, `admit`, `axiom`, `native_decide`, `ofReduceBool`/`trustCompiler`, `implemented_by`, `@[extern`, `unsafe`, `opaque`, `skipKernelTC`, `macro`, `elab`, `syntax`, `run_cmd`/`#eval`, `initialize`, `open Lean`, `Lean.Meta`/`addDecl` or `@[csimp`. There is no `set_option` at all [(3)].

The two challenge theorems are proved by **module-disjoint** chains [(2)]:
- **Chain A** (theorem 1): 201 modules, 37,269 lines, no PrimeNumberTheoremAnd. It uses a local isolated Bézout inequality in A⁴ (`IsolatedBezoutFromRegularSelection.lean:25, :346`).
- **Chain B** (theorem 2): 67 modules, 25,995 lines, plus the 12 patch-added files. It ends in the master inequality `1 ≤ 13/16 + (C + 13/24)·ℓ/log U + …` (`RealZeroUniformMasterBound.lean:30`).
- A further 38 modules are imported by `Main` but needed by neither chain.

**2.4 The auditor's description of Kimura is accurate.**
- Kimura v2, p. 2: the proofs "use the Lean formalization of [SZ] in [Ope26a], which proves the interpolation step by a different argument (Section 7); they have been checked by the Lean kernel, by a replay of all declarations they depend on, and by an independent kernel."
- §7.2, p. 16: "The interpolation step is not formalized as [SZ, Lemma 3] … What is formalized is the conclusion of [SZ, Cor. 4] for our box … by a multiplicity estimate (uniform rectangular multiplicity)."

We confirmed this in the OAI source:
- `actual_biquadratic_rectangle_span` (`Structure/InvariantJetLinearMap.lean:471`) is exactly Cor 4 (paper.tex l.411–420) for the biquadratic map, with thresholds `rectangleThreshold H N j = 32·H^{2/3 or −1/3}·N^{4/3}` (`Structure/RectangleThreshold.lean:14`).
- It is proved through the dual statement `uniform_rectangular_multiplicity` (`Differentials/TorusQuotientDimensionPosCotangentFinrankThree.lean:205`): a nonzero F in the box {0..N−1}⁴ cannot vanish at (1, 1, 1, 1) to these orders along three invariant derivations whose directions span ker(c·), with c Q-independent.
- This is the reading the paper itself gives in its Remark after Cor 4: (D^α xⁿ)(1) = (An)^α. We checked that duality identity exactly [(8)].

**2.5 Kimura's reported checks transfer to the audited files** [(5)].
- Kimura's `lean/vendor/SHA256SUMS` lists 254 OAI files from upstream commit 301488868beec11bfd897168433b0a64f5258559 and the 12 patch-added PrimeNumberTheoremAnd files. **All 266 are byte-identical to 4eaee875.** The same toolchain and Mathlib are pinned, so they elaborate to the same declarations.
- The vendored OAI set is **exactly** the import closure of `Characters.UnconditionalPrimeBias` ∪ `EntireFunctions.RealZeroUniformMasterBound`. This is an independent consistency check on Kimura's description of what he imports.
- Kimura's `B4ZeroGap.lean` calls `source_character_global_greedy_determinant_master_bounds`, which carries the Hadamard upper bound, the divisibility lower bound and the pivot bounds that use `actual_biquadratic_rectangle_span`.

Kimura's logs, read as data, report:
- a full build of these files (18 min, exit 0), in which every declaration passes the kernel;
- a kernel replay of 123,010 constants from an empty environment, with only the three standard axioms ("REPLAY DONE", exit 0);
- Comparator acceptance of `B4.Chi8.zero_gap_all` by both the Lean kernel and nanoda.

**2.6 The OAI *statement* has a reported second certificate.** Kimura's challenge `B4.Chi8.zero_gap_all` imports only Mathlib. It has exactly the OAI hypotheses, with conclusion `(5811/10000000 : ℝ) ≤ (1 - β) * Real.log q` [(4)]. It therefore implies OAI statement 1 with c = 5811·10⁻⁷. If Kimura's report is accurate, the formal statement of OAI Thm 1 holds in Lean without using OAI's final assembly.

**2.7 Cross-checks of the Lean constants against the paper are exact** [(6)]:
- H = 86,713,344 = 12·C0/c0 = 9216·97², so (C0/c0)/H = 1/12 exactly (`ParameterChoices.explicit_pivot_weight`).
- 18818 = 2·97².
- The master-bound coefficients follow from (master) at S2/S1 ≤ 1/12: 13/16 = (3/4)(13/12), 13/24 = (1/2)(13/12), 13/12·log 8, and C/(D log U) + 3/(2DU) from S1 ≥ MDU and log M = 3 log U.
- 13/16 + 1/16 = 7/8.
- Cor 4's budget: 4096 N⁴ > (4N−3)⁴.

**2.8 Toy certificates for the formal intermediate statement** [(7)]. For d ∈ {−3, 5}, N ≤ 4 and every 1 ≤ H ≤ N, the Lean-form rectangle rows span over Q(√d, √2). This is certified by full rank modulo a degree-1 prime (p = 1048447 and p = 1048559). The Vandermonde rows α = (a, 0, 0), a < N⁴, also span; Kimura uses this fact to get Δ ≠ 0. The minimal scale κ* that suffices is at most 1.0 in every case, essentially the row-count bound κ_count (ratio ≤ 1.33). The constant 32 therefore has ≥ 32× slack at these sizes.

## 3. Strongest attack

Each route below would yield a real witness or a real downgrade if it succeeded.

1. **Nobody in this audit has compiled anything.**
   - A text scan is not a proof check. It cannot see tactic behaviour, elaboration failures, or code introduced by Mathlib metaprograms.
   - OAI publishes no comparator log for SiegelZeros. Its config has `enable_nanoda: false`.
   - *Outcome:* a coverage gap. It is not evidence of a defect. **No witness.**

2. **Kimura's coverage is narrower than "kernel-checked use of it".**
   - Kimura: "We do not use its final theorem."
   - **52 of the 306 modules (7,270 lines) were not part of Kimura's build.** These include `Main`, `Model`, `Conclusions.Theorem`, both `DirichletRealZeroBound*` modules, `Estimates.GeometricBoundary`, `Intersection.BezoutBoundary`, `Estimates.ContrarySequence` and `Characters.BoundedConductor`.
   - For theorem 1, the uncovered part of chain A is 12 modules, **642 lines**: `BoundedConductor` (46), `Conclusions/Theorem` (27), `ContrarySequence` (51), `GenuineSequence` (73), `GeometricBoundary` (56), `BezoutBoundary` (27), `LocalGap` (45), `ParameterChoices` (76), `SequenceParameters` (49), `Model` (19), `EventualSelection` (112), `EventuallyInputs` (61).
   - We cannot tell statically which of the 254 imported modules' constants lie in Kimura's 123,010-constant replay. They were, however, compiled in his reported build.
   - Kimura also states that Comparator reused build products, so its guarantee against an adversarial proof needs a clean build (his kernel replay is unaffected).
   - Everything Kimura reports is a report: we read his logs, we did not reproduce them.
   - *Outcome:* the auditor's summary needs the qualifier in §0. **No witness against the formalization.**

3. **The trusted closure is bigger than reported.**
   - The lakefile's configuration-time `run_cmd` and `post_update` hook apply `git apply` patches. One patch *adds* 12 Lean files (6,754 lines) to PrimeNumberTheoremAnd, and chain B depends on them.
   - Our record's "69,818 lines" undercounts the closure.
   - These files were scanned (clean) and are byte-identical to Kimura's vendored copies.
   - *Outcome:* a presentation correction to our own record. **No witness.**

4. **Statement drift or trivialization.**
   - We looked for any weakening of the statement: a junk L-value, a non-primitive modulus, a missing reality condition, a different logarithm, or q = 8 dropped.
   - None found (§2.1). q = 8 is excluded only inside the chain-B master bound, and the contrary sequence has q → ∞.
   - The bounded-conductor step is formalized (`bounded_conductor_zero_gap`, via `fixed_level_real_zero_gap`).
   - **No witness.**

5. **Falsify a formal intermediate statement at toy size.** A counterexample to `actual_biquadratic_rectangle_span` would expose either kernel unsoundness or a misstatement. All 18 toy cases span, with κ* ≈ κ_count [(7)]. **No witness.** This is weak evidence only: the asymptotic regime is far beyond toy size.

6. **"The Lean confirms the paper."** It does not, in one specific place: Lemma 3 (supporting face, Carathéodory, Lagrange) is not formalized; only Cor 4's conclusion is. A successful replay would certify the formal theorem and Cor 4's conclusion, not the paper's text of Lemma 3. Lemma 3 rests on the hand audit (audit_part2) and on Banks's independent Prop 3.4. This is a scope fact, not a defect.

## 4. Coverage map (what is established, and by whom)

| Component | Status |
|---|---|
| Formal statement equals OAI Thm 1 (Mathlib d13f23b definitions) | **Checked here** (text and definitions) |
| Solution statements equal challenge statements; `Model` definition verbatim | **Checked here** |
| No sorry/axiom/native_decide/escape hatch in 306 + 12 files | **Checked here** (static scan only) |
| 254 core modules + 12 patch files compile and pass the kernel; constants in Kimura's closure replayed by Lean and nanoda | **Reported by Kimura v2** (logs read; not reproduced). Files byte-identical to 4eaee875: **checked here** |
| OAI Thm 1 statement holds in Lean (via Kimura's `zero_gap_all`, c = 5811·10⁻⁷) | **Reported by Kimura v2**; implication **checked here** |
| 52 assembly modules (642 lines for theorem 1), and OAI's own two challenge proofs | **Not covered** by any build we know of. Read statically: coherent with paper §6 |
| OAI comparator run for SiegelZeros.json | **Not done** by us; no log published by OAI |
| Paper's Lemma 3 as written | Not formalized. Hand-audited in audit_part2 |

## 5. Decision

- **Classification: unresolved_ambiguity**, kept, narrowed and marked non-load-bearing. "Not replayed" stays true, because we were not allowed to build third-party code. Every static check that could have exposed a problem passed.
  - "not_an_issue" would overstate what we know about the formalization.
  - "suspected_gap" has no supporting evidence.
  - "repaired_minor" does not apply: nothing in the source needed repair.
- **Error characterization: not allowed.** No witness exists.
- **Corrections to our own records.**
  1. Replace "about 69.8k lines" with "69,818 lines in OAI/NumberTheory/SiegelZeros plus 6,754 lines patched into PrimeNumberTheoremAnd by the lakefile (76,572 in total, excluding Mathlib)".
  2. Replace "Kimura v2 reports kernel-checked use of it" with "Kimura v2 reports a build, a kernel replay and a Lean-plus-nanoda comparator check of his own theorems. These import 254 of the 306 SiegelZeros modules unmodified (byte-identical at 4eaee875), including the multiplicity-estimate replacement for Lemma 3, but not OAI's final theorem."
- **Allowed public wording.** "OAI states a Lean formalization of Theorem 1. The comparator statement matches the theorem; the Observatory did not build or replay it. Kimura (arXiv:2610.21511v2) reports independent kernel checks of a proof that uses the formalization's arithmetic core unmodified and implies the formal statement with c = 5.811·10⁻⁴. The formalization replaces the paper's interpolation Lemma 3 by a multiplicity estimate."
- **Known misreadings to avoid.**
  - A Lean certificate here does not certify the paper's Lemma 3 text.
  - "Kernel-checked" in Kimura refers to Kimura's theorems, not to OAI's `exists_absolute_real_zero_gap`.
  - Our static scan is not a proof check.
  - The formal statement is a real-zero gap, not GRH and not a zero-free half-plane.

## 6. Reproduction

```
# data (fetched once, read as text; never executed):
#   raw.githubusercontent.com/iwaokimura/cln-imq-2k/e66ab86/lean/{vendor/SHA256SUMS,Challenge/B4ZeroGap.lean}
#   raw.githubusercontent.com/leanprover-community/mathlib4/d13f23b.../Mathlib/NumberTheory/{LSeries/DirichletContinuation,DirichletCharacter/Basic}.lean
cd research/exploratory/riemann-observatory/experiments/code/claims_2026/siegel_adjudication
python3 -I adj_U4_lean_static.py [OAI_LEAN_ROOT] [KIMURA_SHA256SUMS] [KIMURA_CHALLENGE] [MATHLIB_DIR]
# ~13 s, 31 PASS / 0 FAIL; output in adj_U4_lean_static.out
```
Dependencies: numpy 2.5.3, sympy 1.14.0, Python 3.13. Default paths point to the session scratchpad copies listed in the header.
