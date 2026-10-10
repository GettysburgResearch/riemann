# PROPOSED packet draft: formal zero-free half-plane Re s > 7/8 for ζ and Dirichlet L-functions

```text
Status: PROPOSED integration packet draft. This is NOT an integrated packet and assigns no verdict.
  The subject is an IMPORTED FORMAL theorem: a Lean proof imported unmodified from an external
  repository and kernel-checked here under stated trust assumptions. No human has reviewed the
  Lean development, the statement or the trust base, and no human integrator has acted on it.
Scope: Re s > 7/8 implies zeta(s) != 0, and L(s, chi) != 0 for every Dirichlet character chi of
  every modulus q >= 1 (principal chi at s = 1 excluded), for Mathlib's riemannZeta and
  DirichletCharacter.LFunction. This is a fixed open half-plane. It is not RH and says nothing
  about Re s <= 7/8. The Hecke-family theorem, the wave's corollaries and the Sep 30 manuscript's
  own proof are recorded as context only (Sections 2.3 and 5).
Exact sources or dependencies: import ref pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6, Lean
  tree ef5d0c6c35578aacaa83cca392c6752fcc8b1784 (byte-exact import of
  openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a lean/); Lean v4.34.1; Mathlib d13f23b7
  (oleans from its binary cache); 23 shipped third-party patches. Review record read at this
  wave's working-branch commit 995eb31fd05f3372cbe0a85dcedf100974ebe089 (Section 1).
What was actually run for this draft: reading; sha256 of the challenge files, lakefile and manifest
  from git objects at the import ref; re-hash of the review files and logs; a claim-ID collision
  grep; a few Mathlib source lines read in the build's source copy. No Lean, Lake, comparator or
  nanoda process was started. The build, axiom and comparator runs consolidated here are those of
  reviews/LEAN_BUILD_ATTEMPT.md.
Smallest remaining gap: an independent exact-SHA review of statement fidelity and of the trust
  base, and a human decision on comparator assumption 2 (precompiled solution; Mathlib oleans
  from cache, not rebuilt). See Sections 7 and 8.
```

RH remains unsolved. This draft does not claim that RH is proved or disproved. The half-plane
`Re s > 7/8` is far from the critical line `Re s = 1/2`.

## 0. What this draft is and is not

* It is a **separately labelled proposed object**, as [AGENTS.md](../../../../../AGENTS.md) asks.
  It is not under `research/integrated/` and changes no accepted record.
* Integration needs one frozen source commit, an exact-SHA independent review, resident readable
  material under `research/integrated/`, and a human integrator. Only the first exists.
* All reviews cited here are **bounded agent reviews** written on one branch. They are not
  independent of one another ([docs/REVIEWING.md](../../../../../docs/REVIEWING.md)).
* Formal and scientific integration are separate gates ([FORMALIZATION.md](../../../../../FORMALIZATION.md)).
  This packet is about an imported formal theorem. It does not touch the project's own
  formal-v0.1 release or [FORMAL_STATUS.md](../../../../../FORMAL_STATUS.md).
* The model was [OCT5_11_12_PACKET](../OCT5_11_12_PACKET/README.md). Nothing here is stronger
  than its sources.

## 1. Frozen sources and pins

| Item | Pin | Check for this draft |
|---|---|---|
| Import ref (draft PR 908) | `31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6` | `git cat-file -t` = commit |
| Lean tree | `standalone/2026-10-07-openai-quasi-riemann-import/upstream/lean` = tree `ef5d0c6c35578aacaa83cca392c6752fcc8b1784` | `git rev-parse` agrees |
| Upstream | `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a` `lean/`, imported byte-exactly | from the build record; not re-fetched |
| Lean | `leanprover/lean4:v4.34.1`, commit `5045d0056413266e57c625dcd7c365b10e377c52` | `lean-toolchain` at the ref reads v4.34.1 |
| Mathlib | `d13f23b723b8a846827a245b89c10fc7d3f11612`; sources git-clean; oleans from `cache.mathlib.org`, **not rebuilt** | build record §3, Addendum B |
| `lakefile.lean` | sha256 `4cca977ebece444b6c999d99755c1ad3c93119bafc127ea761f7f703c7279e74` | recomputed |
| `lake-manifest.json` | sha256 `cf6105a25d9dca2f166b241d9191bd12c7e13305890dc9c4d0952351cccc0794`; 42 packages at manifest revisions | hash recomputed; revisions from §3 |
| Patches (23) | 11 applied by the lakefile `run_cmd`: iut, tate-curves-theta, genl, heights, pi1, orbicurve-cores, oka, tempered-fundamental-groups, elliptic-curves, formal-schemes, belyi. 12 from the `post_update` hook, replicated by a script: fixed-point-theorems, PrimeNumberTheoremAnd, Zeta3Irrational, rellich-kondrachov, carleson, StrongPNT, AbsorptionCutoff, AINTLIB, ClassFieldTheory, schoenflies-lean, SphereEversion, gromov | from §3 |
| Comparator tools | comparator `d03acab154d269c06e60e4de7e4cc85deebff94b` (toolchain overridden locally to v4.34.1); lean4export `076e8e57707e813375e8f9da8bf989799ace9680`; landrun `811cfff51ceaf3d9843708aa6d22e9b84ccac8b4` (v0.1.18) | from §5 |
| Second kernel | nanoda_lib 0.4.19, `ammkrn/nanoda_lib@3a24072` (queued at drafting; since run: accepts the zeta challenge) | Addendum C |

**Challenge files** at the import ref, path `.../upstream/lean/ComparatorChallenges/` (sha256 recomputed for this draft):

| File | sha256 | git blob | Role |
|---|---|---|---|
| `QuasiRiemannHypothesis.json` | `46ebb7edc11f69536210f502b4bcbd36bbaf3f0872c16748b6c8ce43991bf320` | `acf55246` | zeta challenge |
| `QuasiRiemannHypothesis.lean` | `065f8c9a01d28db78c8b1bfc5083b535082a2d2aac2230d563f98b8caa812cc5` | `e7d1caf6` | zeta statement |
| `DirichletSevenEighths.json` | `cfc8d85d49ec5f180e75990d95c59c45f9bd5b9f453a101308870b9c4df9e1d9` | `a946bfcf` | Dirichlet challenge |
| `DirichletSevenEighths.lean` | `8fb13ad977bca104591fcbc6ef01a58496e7385053c9b1445f95749afc0eff54` | `baa55beb` | Dirichlet statement |
| `HeckeSevenEighths.lean` | `cb5e404fa65a502c0a9006b9ad45c28914feb79e4b7b1ffcf05e4af82ed0cfc2` | `dbeb6414` | context only (Section 2.3) |

Both statement files import only Mathlib. Both JSON files name the solution module
`OAI.NumberTheory.DirichletL.Nonvanishing`, `permitted_axioms` [propext, Quot.sound,
Classical.choice] and `enable_nanoda: false`.

**Review record** (paths relative to `research/exploratory/qrh-2026-10/`; read at `995eb31fd`):

| File | sha256 prefix | Last changed in |
|---|---|---|
| `reviews/LEAN_BUILD_ATTEMPT.md` (build, axioms, comparator; Addenda A-C) | `c341a02db311b516` | `995eb31fd` |
| `reviews/HECKE_LEAN_FIDELITY.md` (context: Hecke definitions) | `465c09f6f6363078` | `995eb31fd` |
| `reviews/SEP30_LEAN_CORRESPONDENCE.md` | `d2af9e19afe66312` | `32e92e932` |
| `reviews/PART1_FREE_ROUTE.md` | `a079e16b13560772` | `752c7451b` |
| `reviews/SEP30_VERIFICATION_MAP_V2.md` (incl. §10, v2.1) | `ebe25fdad7f7e2c6` | `752c7451b` |
| `reviews/END_WAVE_REDTEAM.md` | `d1b1bc863dd3b05e` | `d99030d91` |
| `lean/README.md` | `97d54de1cb9f73fb` | `32e92e932` |
| `lean/checks/Axioms.lean`, `Statement.lean` | `48e33961c938d3e0`, `fba45b7b103ba76e` | |
| `reviews/results/lean_axioms.log`, `lean_statement.log` | `249a8a4247191809`, `bc0d488ac336aea4` | |
| `reviews/results/comparator_QuasiRiemannHypothesis.log` | `59bf9c0417f609c1` | `6ce53ccb4` |
| `reviews/results/comparator_DirichletSevenEighths.log` | `9b08d6a1b461cabb` | `32e92e932` |
| `reviews/results/lean_build_resume4_tail.log` | `b1fd647deb3e1a2a` | |

The branch moves while other agents commit. Cite commits, not the branch.

## 2. Statement

### 2.1 Lean, verbatim (`reviews/results/lean_axioms.log`)

```text
@OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re : ∀ {s : ℂ}, 7 / 8 < s.re → riemannZeta s ≠ 0
@OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re : ∀ {q : ℕ} [inst : NeZero q]
  (χ : DirichletCharacter ℂ q) {s : ℂ}, 7 / 8 < s.re → ¬(χ = 1 ∧ s = 1) → DirichletCharacter.LFunction χ s ≠ 0
'OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re' depends on axioms: [propext, Classical.choice, Quot.sound]
'OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re' depends on axioms: [propext,
 Classical.choice,
 Quot.sound]
'OAI.SevenEighths.ProbeFinalAssemblyUnconditional.detector_certified_bands' depends on axioms: [propext,
 Classical.choice,
 Quot.sound]
```

The source text of both challenge statements is in LEAN_BUILD_ATTEMPT §2.

### 2.2 In plain mathematics

**Theorem (imported, formal; proposed for integration at this scope).**

1. **Zeta.** `ζ(s) ≠ 0` for every complex `s ≠ 1` with `Re s > 7/8`.
2. **Dirichlet L-functions.** Let `q ≥ 1` and let `χ` be any Dirichlet character mod `q`, primitive
   or not, principal included. Then `L(s, χ) ≠ 0` for every `s` with `Re s > 7/8`, except when `χ`
   is the principal character mod `q` and `s = 1`, the pole.

How to read the Lean text:

* **`s = 1` for zeta.** Mathlib's `riemannZeta` is a total function (`hurwitzZetaEven 0`). At the
  pole it takes a junk value. Mathlib proves `riemannZeta 1 = (γ − log(4π))/2` and
  `riemannZeta_one_ne_zero` (`Mathlib/NumberTheory/Harmonic/ZetaAsymp.lean`, lines 421 and 444 at
  d13f23b7). So the Lean statement at `s = 1` is true by convention and says nothing about the
  pole. That is why item 1 says `s ≠ 1`.
* **The pole for Dirichlet.** In Lean, `χ = 1` is the trivial character mod `q`, i.e. the
  principal character. The hypothesis `¬(χ = 1 ∧ s = 1)` removes exactly the pole. For `q = 1`,
  Mathlib's `LFunction_modOne_eq` gives `LFunction χ = riemannZeta`.
* **Imprimitive characters.** Mathlib's `LFunction χ` is the L-function of `χ` as a character mod
  `q`, so it lacks the Euler factors at primes dividing `q` but not the conductor. Such finite
  factors vanish only on `Re s = 0` (standard), so this changes nothing in `Re s > 7/8`.
* **`7 / 8` is real.** The challenge writes `(7 / 8 : ℝ) < s.re`; it is not natural-number
  division.
* **Not vacuous.** The hypotheses are satisfiable (for example `s = 2`), and the objects are
  Mathlib's own. FORMAL_STATUS.md warns that a clean axiom list for a theorem with impossible
  hypotheses proves nothing. That failure mode does not apply here.
* **Pinned to Mathlib.** `Statement.lean` elaborates both theorems against `_root_.riemannZeta`
  and `_root_.DirichletCharacter.LFunction`, which are defined in
  `Mathlib.NumberTheory.LSeries.RiemannZeta` and `...LSeries.DirichletContinuation`
  (`lean_statement.log`). Comparator also compares each statement with an export from a module
  that imports only Mathlib.
* **Open half-plane.** Nothing about `Re s = 7/8`, about `1/2 < Re s ≤ 7/8`, or about zero counts.

### 2.3 Outside the proposed statement

| Object | Status at `995eb31fd` | Why it is outside |
|---|---|---|
| Hecke-family theorem `OAI.SevenEighths.HeckeFamily.LFunction_ne_zero_of_seven_eighths_lt_re` | built; `#print axioms` standard (`lean_hecke_axioms.log`); comparator **pending** at drafting, **accepted** since (1096 s; LEAN_BUILD_ATTEMPT Addendum C) | Stated over project-defined `HeckeFamily.Character` (a multiplicative character of `O/m`, `O = Z[ω]`, trivial on units) and `LFunction` (one sixth of a continued lattice-theta Mellin transform), written into the challenge file. Mathlib has no Hecke L-function to compare with. [HECKE_LEAN_FIDELITY.md](../../reviews/HECKE_LEAN_FIDELITY.md) (EXPLORATORY; reading, paper-level argument and EMPIRICAL float checks; one bounded agent pass) finds the family "exactly the finite-order Hecke L-functions of K = Q(√−3) as the Sep 30 paper defines them", with the same pole exception, neither narrower nor broader. Its stated gaps: the solution's bridge lemmas are not comparator targets and had no `#print axioms` run of their own, and "finite-order Hecke character = ray class character" is a textbook step, not formalized. Not independently reviewed. |
| Wave corollaries in `lean/`: zeta strip `1/8 ≤ Re s ≤ 7/8`, Dirichlet strip (primitive `χ ≠ 1`, off the Gamma-factor poles), Siegel challenge with `c = (log 3)/8` | built; axioms standard; comparator **pending** at drafting; since then the Siegel corollary (1082 s), the zeta strip (1104 s) and the Dirichlet strip (1130 s, against a wave-written Mathlib-only challenge) are **accepted** (Addendum C) | Separate objects. They rest on this theorem. |
| Oct 1 Siegel-zero development | built (9242 jobs); axioms standard; loads no `DirichletL` module | Independent of the 7/8 development. |
| Manuscript Thm 1.1's proof, Part I (Thm 3.1, 11/12), Cor 1.2 | paper-level record in Section 5 | The formal theorem does not depend on them. |
| Explicit consequences (`EXPLICIT_PNT_7_8.md`) | PROPOSED, conditional, unreviewed | Use imported explicit results; not formal. |

## 3. Trust base

| # | Trusted item | What was checked | What was not |
|---|---|---|---|
| T1 | Lean 4 kernel, v4.34.1 | It accepted both proofs at build time. Comparator re-checked the exported proofs with a fresh kernel (`Environment.replay`) outside the elaborator. | Kernel soundness itself. Only one kernel was used. |
| T2 | The three standard axioms | `#print axioms` gives only `propext`, `Classical.choice`, `Quot.sound`: no `sorryAx`, no `Lean.ofReduceBool`, no `Lean.trustCompiler`, no project axiom. Comparator enforced the permitted list. | — |
| T3 | Mathlib d13f23b7 definitions | The git tree is clean. `riemannZeta` and `LFunction` resolve to Mathlib modules. 0 of 8,548 Mathlib oleans are newer than the cache unpack (12:48-12:51 UTC). | **The oleans came from Mathlib's binary cache and were not rebuilt.** The exported definitions are whatever the cached oleans contain. The mtime window overlaps the unsandboxed `run_cmd` clone-and-patch step (12:43-12:51). |
| T4 | 23 patched third-party packages | All apply cleanly at their pinned commits; the 12 hook patches were also reverse-checked. The PNT+ patch removes 2 `sorry` lines and adds none. Only patched PNT+ `Wiener` (with 3 local imports) and 15 Rellich-Kondrachov modules enter the closure. Their proofs are among the replayed constants. They cannot change the statement's meaning, because comparator compares against a Mathlib-only export (zeta and Dirichlet). | The patches were not reviewed. Patching ran unsandboxed at configuration time. |
| T5 | OAI closure (2,924 modules, 486,490 lines) | All files are byte-identical to the git blobs at the ref. The build had 0 errors and 0 `sorry` warnings. A lexical scan found 0 `axiom`, 0 `sorry`/`admit`, 0 `native_decide`/`ofReduceBool`, 0 `set_option`, 0 `unsafe`/`extern`/`implemented_by`; it found 4 kernel-checked `decide +kernel` (SEP30_LEAN_CORRESPONDENCE §5). | No human has read it. Soundness does not need that, but correspondence with the paper does. |
| T6 | Comparator and lean4export | 4/4 self-tests passed. The toolchain was matched to v4.34.1. | Their own correctness; the local toolchain override. |
| T7 | Comparator assumption 2 (solution not precompiled) | **Not met.** The solution was compiled outside the sandbox first. This is a non-adversarial reproduction. | — |
| T8 | landrun sandbox | v0.1.18 `--best-effort` on Landlock ABI v7 (strict mode wants v9). A write outside the allowed paths was denied in a test. | The systemd `AF_UNIX` wrapper was not used. |
| T9 | Second kernel | At drafting none had run. Since then the **nanoda kernel accepts the zeta challenge** (`QuasiRiemannHypothesisNanoda.json`, 1238 s, together with the Lean kernel; Addendum C). Later the Dirichlet and Hecke challenges were also accepted by both kernels (Addendum C). | — |
| T10 | Human review | **None**, of the Lean development, the statement or the trust base. | — |

## 4. Formal run record

| Run | Outcome | Evidence |
|---|---|---|
| Build of `OAI.NumberTheory.DirichletL.Nonvanishing` | "Build completed successfully (7061 jobs)"; 0 errors; 0 `sorry` warnings | `lean_build_resume4_tail.log` (the third resumption) |
| `#print axioms` | standard (Section 2.1) | `lean_axioms.log`, `lean/checks/Axioms.lean` |
| Statement pinning | Mathlib modules (Section 2.2) | `lean_statement.log`, `lean/checks/Statement.lean` |
| Comparator, `QuasiRiemannHypothesis.json` (zeta) | **accepted**: "Lean default kernel accepts the solution"; 1094 s; exit 0; peak about 7 GB RSS in lean4export | `comparator_QuasiRiemannHypothesis.log`; Addendum B |
| Comparator, `DirichletSevenEighths.json` | **accepted**; 1108 s; exit 0 | `comparator_DirichletSevenEighths.log`; Addendum C |

**Further comparator runs**, quoted exactly from LEAN_BUILD_ATTEMPT.md Addendum C at
`995eb31fd`. That file records outcomes as they complete, so **these rows may be updated**.
Read the file, not this table, for the current status.

| challenge JSON | solution module | outcome |
|---|---|---|
| upstream `HeckeSevenEighths.json` | `OAI.NumberTheory.DirichletL.Hecke.Nonvanishing` | pending at drafting; **accepted** since (1096 s) |
| wave `SiegelFromSevenEighths.json` (upstream `SiegelZeros` challenge module) | `OAI.QRHWave.SiegelFromSevenEighths` | pending at drafting; **accepted** since (1082 s) |
| wave `QRHWaveStrip.json` (challenge written in this wave) | `OAI.QRHWave.ZetaZeroStrip` | pending |
| upstream `SiegelZeros.json` | `OAI.NumberTheory.SiegelZeros.Main` (Oct 1 route) | pending at drafting; **accepted** since (900 s) |
| `QuasiRiemannHypothesisNanoda.json` (upstream zeta challenge with `enable_nanoda: true`) | `OAI.NumberTheory.DirichletL.Nonvanishing` | queued at drafting; since **accepted by both kernels** (nanoda and Lean, 1238 s; Addendum C). nanoda_lib 0.4.19 (ammkrn/nanoda_lib@3a24072) was built here with cargo 1.97.0 (`cargo build --release`, 32 s) and is passed to comparator through `COMPARATOR_NANODA` |

## 5. Paper-level record (context; not load-bearing for the formal statement)

The formal theorem stands or falls with its trust base, not with the manuscript. The paper
record below neither strengthens the formal check nor is verified by it.

**5.1 Verification map v2.1** (SEP30_VERIFICATION_MAP_V2.md §10; bounded agent reviews of the
Sep 30 manuscript, `paper.tex` sha256 `42a5ee0f…a6a3`):

| | R | Rp | I | A | U | L | total |
|---|---|---|---|---|---|---|---|
| as written | 49 | 6 | 2 | 3 | 5 | – | 65 |
| with the Oct 5 substitution | 49 | 6 | 2 | 0 | 0 | 8 | 57 + [O5] thm:main |

With the substitution, owned lines are R 67.1%, Rp 31.7% and I 1.2%. As written, the 8
Part-I-only nodes (3 A, 5 U) are unreviewed. No bounded review reported a wrong step.

**5.2 Lean correspondence** (SEP30_LEAN_CORRESPONDENCE.md). Of the 65 load-bearing nodes:

| F | Fv | C (name-level only) | B (bypassed) | N (not found) |
|---|---|---|---|---|
| 6 | 8 | 37 | 8 | 6 |

* **No Part I.** Lean uses only `β ≤ 1` (`beta_le_one`), not `β* ≤ 11/12`. There is no 11/12
  bound and no sextic large sieve in the closure.
* **The same 7/8 bookkeeping.** `σ0 = 7/8`, `C(s) = s − 11/16`, low exponent `3/16`,
  `κ = 3/4 + 2Δ`, the Lemma 20.2 margin `49/440640`, and so on, constant for constant.
* **Native instances of the cited theorems.** Lean proves its own cubic theta, cubic and quadratic
  large sieves, and Chebotarev via Wiener-Ikehara, only in the instances it uses. They were not
  compared with the published theorems.

**5.3 Part-I-free paper route** (PART1_FREE_ROUTE.md). **Verdict (A), PROPOSED** (bounded
review): Part II as written, plus an endpoint row count extended from `δ = 5/6` to all
`δ ∈ [5/6, 1]`, would prove 7/8 from `β* ≤ 1` alone (PROPOSED; bounded same-family review only).
* 32/32 exact gates pass and 10/10 failing controls fire.
* Remark 19.3 becomes load-bearing, and two short lemmas (P1F.1-P1F.2) are new.
* This is a new composition and needs its own independent review.
* **Second review** (added after drafting): [../../reviews/PART1_FREE_ROUTE_REVIEW2.md](../../reviews/PART1_FREE_ROUTE_REVIEW2.md),
  verdict **"(A) with corrections"**, no obstruction found. It is another bounded agent pass of
  the same model family, so it is not independent in the AGENTS.md sense. Its corrections:
  * P1F.2 needs the loss bound `λ ≤ 527/300`;
  * gate T2 checks only line ranges;
  * Lemma 17.6 stays in the node set (balanced bins);
  * Remark 19.3 should be rated no better than Rp.

**5.4 The Lean route and the paper routes differ.**

| | Paper as written | Part-I-free paper route | Lean route |
|---|---|---|---|
| bootstrap | Thm 3.1, `β* ≤ 11/12` | `β* ≤ 1` (386-387) | `beta_le_one` |
| ceilings `Δ, κ, δ` | `1/24, 5/6, 5/6` | `1/8, 1, 1` | `1/8, 1, 1` |
| high bins `δ > 5/6` | none | P1F.1-P1F.2 | `CountParameters.high`, `high_mixed_margin` |
| slot lengths | `K` equal lengths `ℓ/K` | equal, unchanged | pairwise **distinct** (`slots_injective`), `t < Δ/4` |
| Lemmas 17.1, 18.1 | general statements | general statements | **instances** only, as interface fields |
| cited theorems | imported (DR, Heath-Brown, GL, Thorner-Zaman) | imported | proved natively, as instances |
| `O(ε)` bookkeeping | asymptotic | asymptotic | explicit linear budgets |

So the formal proof shows that a closely related argument works. It does not check the
manuscript's text, and it does not check the Part-I-free paper route.

## 6. Scope

| Dimension | Scope of the proposed statement |
|---|---|
| Finite / global | **global**: every height, every modulus, every character |
| Conditional | unconditional within Lean + Mathlib + the trust base of Section 3 |
| Native / imported | **imported**: external Lean proof, checked here, not written here |
| Effectivity | none claimed: a pure non-vanishing statement with no constants |
| Family | `ζ` and Dirichlet L-functions only. The Hecke clause is outside (Section 2.3) |
| Relation to RH | none directly. RH needs `Re ρ = 1/2`; this excludes only `Re s > 7/8` |

## 7. Proposed claim row (for the integrator; no verdict assigned)

**Collision check (run for this draft at `995eb31fd`).** `grep -i -E 'QRH|SEVEN_EIGHTHS|7_8|SEP30|ZERO_FREE|FORMAL'`
over `canonical/` and every `research/integrated/**/CLAIMS.tsv` (22 files) finds two hits:
`COMP.FORMAL.LEAN` in `canonical/2026-08-22/computations.tsv`, a row about the project's own
formal backlog, and a prose link to FORMAL_STATUS.md in `canonical/README.md`. Neither is a QRH
claim ID. A grep for the proposed ID itself finds nothing. No `IMPORTED.` ID exists in `canonical/` or
`research/integrated/`. The proposed ID also differs from the sibling proposals
`IMPORTED.QRH.OCT5.ZERO_FREE_11_12` and `IMPORTED.QRH.SEP30.SEXTIC_FOURTH_MOMENT_CASE1`.

| Field | Proposed value |
|---|---|
| semantic_id | `IMPORTED.QRH.SEP30.FORMAL_ZERO_FREE_7_8` (**a proposal**; the integrator allocates) |
| label | **IMPORTED-FORMAL** |
| statement_short | For Mathlib's `riemannZeta` and `DirichletCharacter.LFunction`: no zero in `Re s > 7/8`, for every modulus and character (principal pole excluded; `ζ(1)` is a junk value). |
| source | PR 908 `31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6`, tree `ef5d0c6c…`; challenges `QuasiRiemannHypothesis.json`, `DirichletSevenEighths.json` (Section 1) |
| check evidence | build, `#print axioms`, statement pin, comparator ×2 (LEAN_BUILD_ATTEMPT Addenda A-C, at `995eb31fd`) |
| quantifier_scope | global; open half-plane |
| proof_kind | imported formal proof (Lean 4 kernel; three standard axioms) |
| trust_assumptions | Mathlib oleans from cache; 23 unreviewed patches; comparator assumption 2 not met; landrun best-effort; two kernels (Lean, nanoda) for every comparator challenge of the wave |
| rh_relationship | none directly |
| final_verdict | **not assigned**: awaits an independent exact-SHA review and the decision of Section 8 |
| first_broken_arrow | none known; smallest failure point in Section 9 |

The Hecke clause should be a separate row with its own ID, once an independent review confirms
HECKE_LEAN_FIDELITY.md. Its comparator run has since completed: accepted (Addendum C).

## 8. What an integrator still has to do

1. **Independent exact-SHA review of statement fidelity (low effort).** Read the two statement
   files (9 and 16 lines at the hashes above). Check that `riemannZeta` and `LFunction` are
   Mathlib's, the junk value at `s = 1`, the meaning of `χ = 1`, and that both comparator logs
   name the right theorem and say "accepts".
2. **Independent review of the trust base.** At least: the 23 patches (or their effect on the
   closure: PNT+ `Wiener` and Rellich-Kondrachov), the lakefile's configuration-time `run_cmd`,
   and the tool pins.
3. **A human decision on the precompiled solution.** Options:
   * accept it as a non-adversarial reproduction, with T3, T4, T7 and T8 stated wherever the
     result is cited; or
   * **rerun from a clean checkout** (suggested; not tried here): omit `lake exe cache get` so
     that Mathlib builds from its sources, let comparator build the solution inside its sandbox
     (this meets assumption 2), use strict landrun on a kernel with Landlock ABI v9 plus the
     `AF_UNIX` wrapper, and add the nanoda run.
   * **Time estimate from the logs.** The OAI closure is about 4 CPU-hours (measured rate 33.6
     source lines per CPU-second). LEAN_BUILD_ATTEMPT §7 estimates 1.5-2 h wall on a dedicated
     4-core machine. Each comparator run took about 18 minutes with the solution prebuilt. The
     Mathlib-from-source build was **not measured**; Mathlib has 8,548 `.olean` files against
     the closure's 2,924 modules, so it is likely the largest item. Budget a dedicated machine with at
     least 16 GB RAM (lean4export peaked near 7 GB) and well over 14 GB of disk (the disk filled
     once here).
4. **Decide whether to require the paper-level review.** The formal statement does not need it.
   Requiring it would mean an independent review of PART1_FREE_ROUTE (or of the paper as written,
   with Part I) and statement-level work on the 43 C/N rows. That should be a separate object
   about the manuscript, not a condition hidden inside this one.
5. **Housekeeping.** Keep the Hecke clause and the corollaries as separate objects. If the Lean
   source becomes resident, keep the upstream Apache-2.0 notices (PR 908 `THIRD_PARTY_NOTICES.md`).
   The build helper scripts (`env.sh`, `step2_cache.sh`, `step3_build.sh`,
   `apply_post_update_patches.sh` and others) were copied into the repository after this draft
   was written: [../../lean/build_scripts/](../../lean/build_scripts/README.md).

## 9. The smallest statement whose failure would invalidate the result

The mathematics is kernel-checked, so the smallest failure point is in the trust base:

> **The cached Mathlib d13f23b7 oleans encode the definitions in Mathlib's d13f23b7 sources**,
> in particular `riemannZeta`, `DirichletCharacter.LFunction` and what they depend on.

* If it failed, comparator would still compare like with like, but against a different
  `riemannZeta`.
* Rebuilding Mathlib from source (Section 8.3) closes this point.
* Next in line: kernel soundness (for the zeta statement this is now covered by two independent
  kernels; see T9), then the integrity of the unsandboxed precompiled build (T7).

## 10. Known misreadings

1. **"RH is proved."** No. This is the fixed half-plane `Re s > 7/8`. The wave's strip corollary
   says only `1/8 ≤ Re s ≤ 7/8` for nontrivial zeros; RH needs `Re s = 1/2`.
2. **"The paper is verified."** No. Comparator checks the Lean statement, not the manuscript's
   text. The Lean route differs from the paper (no Part I, distinct slots, instance-level lemmas,
   native proofs of the cited theorems). Only 14 of 65 paper nodes have a spot-checked Lean
   counterpart. The paper's status is the bounded-review record of Section 5.
3. **"The Lean Hecke statement is the paper's Hecke family, formally checked."** Not as an
   integrable fact yet. HECKE_LEAN_FIDELITY.md says the definitions match the paper's family, but
   it is a reading-level, single-pass agent note (with float spot checks), not a Lean comparison:
   Mathlib has no Hecke L-function, and the bridge lemmas are not comparator targets. The Hecke
   comparator run has since been accepted (Addendum C), but no independent review of the
   definitions' fidelity exists. Cite it as that note's reading,
   not as part of this packet's statement.
4. **"There is an effective constant."** No. The theorem has no constants. The Siegel corollary
   states only `∃ c > 0`; its proof happens to use `c = (log 3)/8`, but the checked statement is
   existential. Comparator has since accepted it (1082 s). The explicit `c` is in the helper
   `gap_of_real_zero`, which is not a comparator target. The explicit bounds of
   EXPLICIT_PNT_7_8.md are PROPOSED derivations from imported explicit results; they are not
   formal and not reviewed.
5. **"Kintali's 47/48 and the Oct 5 11/12 papers are now verified."** No. Their ζ and Dirichlet
   *statements* follow at once from this one, under this trust base, because their half-planes
   lie inside `Re s > 7/8`. Their *arguments* are not checked by it, and their Hecke clauses
   would also need the Hecke theorem (item 3).
6. **"Comparator accepted the corollaries / the Oct 1 Siegel proof."** Not at `995eb31fd`
   (Section 4). The Hecke theorem, the Siegel corollary and the zeta strip were accepted after
   this draft was written. For the Oct 1 route see Addendum C.
7. **"Mathlib's git tree is clean, so its definitions are checked."** The sources were checked;
   the oleans came from cache (T3).
8. **"Two kernels agree."** For the zeta statement, yes: nanoda and the Lean kernel both
   accepted it, and later the Dirichlet and Hecke statements too (added after drafting;
   Addendum C). The corollaries and both Siegel proofs were later accepted by both kernels too.
9. **"The Lean statement at `s = 1` says something about the pole."** It is a fact about Mathlib's
   junk value.
10. **"Agent reviews make this reviewed."** No. Integration needs an independent exact-SHA review.

## 11. Reproduction (copied from LEAN_BUILD_ATTEMPT §4-§5, §7 and Addenda A-C)

`<scratch>` is session scratch and is not durable. Environment used here:
`GLIBC_TUNABLES=glibc.malloc.mmap_max=0:glibc.malloc.arena_max=1`, `LEAN_NUM_THREADS=3`, `nice -n 19`.

```sh
# 1. source and toolchain
git archive pr908 <lean dir> | tar -x                     # into scratch
sh elan-init.sh -y --no-modify-path --default-toolchain none
elan toolchain install leanprover/lean4:v4.34.1
# 2. dependencies (clones 42 packages; run_cmd patches 11; downloads the Mathlib cache)
nice -n 19 lake exe cache get
# 3. the 12 post_update patches: run <scratch>/scripts/apply_post_update_patches.sh
#    (per package: HEAD = manifest rev, git apply --check, git apply, reverse check),
#    or run upstream's `lake update` and confirm the manifest hash is unchanged
# 4. challenges, then the solution closure
lake build ComparatorChallenges.QuasiRiemannHypothesis ComparatorChallenges.DirichletSevenEighths
nice -n 19 lake build OAI.NumberTheory.DirichletL.Nonvanishing
#    resume: . <scratch>/scripts/env.sh; <scratch>/scripts/step3_build.sh > <scratch>/logs/step3_build_resume.log 2>&1
# 5. axioms and statement pin (committed as lean/checks/Axioms.lean, Statement.lean)
lake env lean <scratch>/scripts/Axioms.lean
lake env lean <scratch>/scripts/Statement.lean
# 6. comparator (Addendum B; same for ComparatorChallenges/DirichletSevenEighths.json)
cd <lean dir>
COMPARATOR_LANDRUN=<scratch>/tools/bin/landrun \
COMPARATOR_LEAN4EXPORT=<scratch>/tools/comparator-v4341/.lake/packages/lean4export/.lake/build/bin/lean4export \
  lake env <scratch>/tools/comparator-v4341/.lake/build/bin/comparator ComparatorChallenges/QuasiRiemannHypothesis.json
# 7. context only (Addendum C): Hecke build and axioms; the second kernel via COMPARATOR_NANODA
lake build OAI.NumberTheory.DirichletL.Hecke.Nonvanishing
lake env lean <repo>/research/exploratory/qrh-2026-10/lean/checks/HeckeAxioms.lean
```

Expected: "Build completed successfully"; axioms exactly `[propext, Classical.choice, Quot.sound]`;
comparator ends with "Lean default kernel accepts the solution" and "Your solution is okay!". Any
`sorryAx`, `Lean.ofReduceBool`, `Lean.trustCompiler` or project axiom would be critical. For the
wave corollaries, follow [lean/README.md](../../lean/README.md), "How to check".
