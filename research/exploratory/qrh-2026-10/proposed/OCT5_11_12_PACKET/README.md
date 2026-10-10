# PROPOSED packet draft: zero-free half-plane Re s > 11/12 (OpenAI, 5 October 2026)

```text
Status: PROPOSED integration packet draft. This is NOT an integrated packet and assigns no verdict.
  The theorem is an IMPORTED external claim. Bounded agent reviews at one exact source SHA found no
  wrong step in any proof line. No independent exact-SHA review has been done, no human
  mathematician has reviewed the argument, and no human integrator has acted on it.
Scope: Theorem thm:main of the external manuscript "The Quasi-Riemann Hypothesis" (OpenAI, dated
  5 October 2026): no zero of any finite-order Hecke L-function over K = Q(sqrt(-3)) in Re s > 11/12,
  and hence none of any Dirichlet L-function, zeta included. This is a fixed zero-free half-plane.
  It is not RH and says nothing about the critical line.
Exact sources or dependencies: manuscript paper2.tex at ref pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6,
  SHA-256 d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d (3988 lines). Review
  record at commit c2050a5dd8c251f25e5fc285c0845b9f4a42487b on branch claude/peaceful-faraday-ki4ewu.
  Imported external theorems are listed in Section 4.
What was actually run: for this draft, the manuscript was re-extracted and re-hashed, all review
  files and scripts were re-hashed, and the four check scripts were rerun (see CHECKS.md). Line
  ranges were either checked against the source for this draft or taken from the reviews, which
  cite the same hash. No new mathematics was reviewed.
Smallest remaining gap: an independent exact-SHA review of Prop. prop:R (paper2.tex 1317-1333,
  proof 1632-2214 and 2874-3479), and a human integrator's decision. See Sections 8 and 9.
```

RH remains unsolved. This draft does not claim it is proved or disproved. It is about a fixed
half-plane `Re s > 11/12`. That half-plane is far from the critical line `Re s = 1/2`.

## 0. What this draft is and is not

* It is a **separately labelled proposed object**, as [AGENTS.md](../../../../../AGENTS.md) asks
  for under "Before extending an integrated packet". It collects what an integrator and an
  independent reviewer would need: the frozen source, the exact statement, the imported theorems,
  the dependency chain, the review record, scope boundaries and known misreadings.
* It is **not** under `research/integrated/` and it does not change the accepted record.
  [AGENTS.md](../../../../../AGENTS.md) requires the following for integration, and none of it
  exists yet:
  * one exact frozen source commit;
  * an exact-SHA independent review;
  * readable mathematics physically resident under `research/integrated/`;
  * a human integrator.
* The reviews summarised in Section 6 are **bounded agent reviews**. AI agents working on this
  branch wrote them, and they are not independent of one another. [docs/REVIEWING.md](../../../../../docs/REVIEWING.md)
  warns that "different chats using the same model can repeat the same mistake". They can be cited
  as preparation for review. They are not a substitute for it.
* No statement here is stronger than the manuscript's statement. Where this draft simplifies an
  argument (in [PROOF_OUTLINE.md](PROOF_OUTLINE.md)), the simplification is marked.

Files in this draft:

| File | Content |
|---|---|
| README.md (this file) | source, statement, scope, imports, dependency chain, review record, misreadings, smallest failure point, next steps |
| [PROOF_OUTLINE.md](PROOF_OUTLINE.md) | condensed proof, with every step tied to manuscript lines and to the review that covered it |
| [CHECKS.md](CHECKS.md) | how to rerun each check script, expected output, hashes, and what each script does and does not authenticate |

## 1. Frozen source

**The manuscript.** The upstream source is `openai/math` at commit
`adc7f1241b42e322a6451854ab7e4b4c146bf78a` (6 October 2026). It is imported unmodified into this
repository at PR 908.

| Object | Location | SHA-256 | Git blob | Size |
|---|---|---|---|---|
| Manuscript source (load-bearing) | `pr908:standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex` | `d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d` | `2000faddbbebac5de0ecfe0b962534ea61a852d5` | 169,005 bytes, 3988 lines |
| Manuscript PDF (not compared with the TeX) | same directory, `paper2.pdf` | `f919b57829b178c8e60e7c17b018cf773e7907cf642ef5a3347d8a826e8dbf18` | `3ea94d87ffdee8db02c6ef1e563e6d166021ad2f` | 784,503 bytes |
| Citation README | same directory, `README.md` | `35c877a13fd9208ac0d4fb82a21560d9d7c79679982387760c73da9f82220026` | `ab74e085f6b1aaa0ea1ec03095ae77bb65322b15` | 537 bytes |

* `pr908` resolves to `31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6`. The hashes above were recomputed for
  this draft and agree with PR 908's `UPSTREAM_FILES.json`.
* The citation README says "This paper was written with human assistance".
* The upstream licence is Apache-2.0, retained at PR 908 `upstream/LICENSE`. An integrator who makes
  the mathematics resident under `research/integrated/` must keep the attribution and licence
  notices (PR 908 `THIRD_PARTY_NOTICES.md`).
* All line numbers in this draft refer to `paper2.tex` at the hash above.

**Repository context (read, not load-bearing for the statement).**

| Ref | SHA | What it contributes |
|---|---|---|
| `pr908` | `31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6` | source import; `MATHEMATICAL_AUDIT.md` §2 (selective explicit chain of the 11/12 proof); `FORMALIZATION_AUDIT.md` (the Lean release targets 7/8, not this argument) |
| `pr910` | `670a76c1a3a8f325c43c1755b1cfc24d313a3e3c` | height notes: completed calculation gives no height-uniform closure (§1.1, §3.2 of its notes) |
| `origin/claude/openai-math-riemann-analysis-w5copg` | `bd670c92d15f835021c6579ed273b213d71caff7` | earlier numerics for lem:arithmetic (all `n` with `N(n) ≤ 50000`) |

**The review record.** All ten files below are byte-identical at commit
`c2050a5dd8c251f25e5fc285c0845b9f4a42487b` and at the branch head read for this draft
(`d47a04076f34152bd9d0276a9eaa3f43804120f9`). The branch moves while other agents commit, so cite
the commit, not the branch. Paths are relative to `research/exploratory/qrh-2026-10/`.

| File | SHA-256 | Git blob | Last changed in |
|---|---|---|---|
| `reviews/OCT5_REVIEW_SUMMARY.md` | `5c3ab27a62f3a51a87f8239c51960b0275cbfe72c39935beeb2f81dd02ba9dc5` | `2d0e25f4` | `c2050a5d` |
| `reviews/OCT5_R1_REDUCTION_POISSON.md` | `b7207006db676e000c929b7076647bd0e8de2d6763c1677c07ce1ac95e4aa947` | `27095cf3` | `2f607f55` |
| `reviews/OCT5_R2_ITERATION_TRANSFER.md` | `780f749910d956401c3131e77b9f4b9f80e833dd1202a87b4a8668aee3072223` | `8388f705` | `ae4ac885` |
| `reviews/OCT5_R3_THETA_REFLECTION.md` | `68caa5be3629fb852a2b6c82a17196ede5ad59e512f7e8e70dd6f99c450b8d1a` | `22eb896e` | `fbf86638` |
| `reviews/OCT5_RESIDUAL_ITEMS.md` | `794ae2907b1a536e647909cb5db506c393a5e14208fce72d09dfa3a4310513fb` | `c97dc3b5` | `c2050a5d` |
| `reviews/oct5_r1_checks.py` | `4fc6c5d72aa5533a88c205b7ba8b39783212fed14e83a51e3c1b3c34afc9cd54` | `2e92cbcc` | `2f607f55` |
| `reviews/oct5_r2_iteration_check.py` | `e4017ed5c78c5d067c379e90122105b465e7015764099e19d877e50bb9da4bdd` | `1b7c60f8` | `ae4ac885` |
| `reviews/oct5_r3_theta_checks.py` | `504d84f340b31fd5866c548530d713c25227183c73df21d7f3d0e78669c3b16e` | `2d610471` | `fbf86638` |
| `reviews/oct5_residual_checks.py` | `d175c9736a75c581b0ee314ce013d932ed7c85e9723302b16959cff5acbec9b5` | `136ad58e` | `686ca4b1` (WIP checkpoint) |
| `a2/eis.py` (imported by R1 and R3 checks) | `87ca11d98bf3ee130a6dab613b5f7efe444058320b7c22b005327686f2798e65` | `cd753f57` | `f3788ecf` |

Every script hash equals the hash recorded inside its review. One file is cited for context only.
`RUNG_STRENGTH.md` (SHA-256 `1cd6034a189ad2c98a061caea339a6070be8961ca8db8831285c0b6be72d074e`)
was read at `d47a04076`. It changed after `c2050a5d`.

## 2. Statement

### 2.1 The proposed statement (manuscript Theorem thm:main, lines 73-75)

Let `K = Q(√−3) = Q(ω)`, with `ω = e^{2πi/3}`, and let `O = Z[ω]`.

**Theorem (imported; proposed for integration at this scope).**

1. **Hecke family.** Let `ν` be any finite-order Hecke character of `K`, and let `L_K(s, ν)` be its
   Hecke L-function. Then `L_K(s, ν) ≠ 0` for every `s` with `Re s > 11/12`. When `ν` is
   principal (trivial on the ideals prime to its modulus), the point `s = 1` is a pole and is
   excluded. No uniformity in `ν` is claimed or needed; the abscissa `11/12` is the same for
   every `ν`.
2. **Dirichlet L-functions.** Let `χ` be any Dirichlet character of any modulus `q ≥ 1`, primitive
   or imprimitive, including principal characters. Then `L(s, χ) ≠ 0` for `Re s > 11/12`. When `χ`
   is principal, the pole at `s = 1` is excluded.
3. **Zeta.** In particular `ζ(s) ≠ 0` for `Re s > 11/12`. This is the case `q = 1`.

**Conventions behind the statement.**

* *Finite-order Hecke characters.* In standard terms, a finite-order Hecke character of the
  imaginary quadratic field `K` is a character of a ray class group of `K`. This gloss is ours, not
  the manuscript's. The manuscript uses `ν` together with a "fixed ray class group" (lines 805-821).
* *Primitive versus imprimitive.* The proof works with `L_K^S(s, ν)`, which is `L_K(s, ν)` with the
  Euler factors at the primes of `S` removed (lines 745-750). Removing or adding finitely many
  Euler factors does not change the zeros in `Re s > 0`. So the conclusion holds whether or not
  `ν` is primitive (R1 §3.2).
* *Dirichlet transfer.* For a Dirichlet character `χ`, `χ ∘ N_{K/Q}` is a ray class character of
  `K`. Quadratic base change gives `L_K(s, χ∘N) = L(s, χ) L(s, χχ_{−3})`, up to Euler factors that
  are nonzero in `Re s > 0` (lines 760-770). The case `s = 1` uses `L(1, χ_{−3}) > 0` (R1 §3.3).
* *Open half-plane.* The statement is about the open half-plane only. It says nothing about zeros
  with `Re s = 11/12` exactly, or with `Re s ≤ 11/12`.

### 2.2 The internal key proposition, with all quantifiers (Prop. thm:ms, lines 679-689)

Fix a finite-order Hecke character `ν` of `K`. Fix a finite set `S` of prime ideals of `O` that
contains every prime above `2` and `3` and every prime dividing the conductor of `ν` (lines 665-667).
Call an element of `O` **primary** if it is `≡ 1 (mod 3)`. Let `χ_n(u) = (u/n)_6` be the sextic
residue symbol, extended by zero when `(u, n) ≠ 1` (lines 249-276). For
`W ∈ C_c^∞((0,∞); C)` define

    A_u(D) = Σ_{(n,S)=1} μ(n) ν(n) χ_n(u) W(N(n)/D),

where `n` runs over the ideals prime to `S`, each represented by its primary generator.

**Prop. thm:ms.** For every fixed `0 < ϑ ≤ 1/10` and `ε > 0`, there is an integer
`k = k(ϑ, ε) ≥ 1` with the following property. For every compact interval `I ⊂ (0,∞)`, every smooth
`W` supported in `I`, and every `D ≥ 2`,

    Σ_{0 < N(u) ≤ D^{1+ϑ}} |A_u(D)|²  ≪_{ν,S,I,ϑ,ε}  (max_{0≤j≤k} ‖W^{(j)}‖_∞)² · D^{2+ϑ+ε}.

Notes on the quantifiers:

* The derivative order `k` depends only on `(ϑ, ε)`. The proof gives `k = 2J(ϑ, ε/4) + 4`
  (line 1234, where R1 §3.4 writes 1232).
* Constants may depend on `(ν, S, I, ϑ, ε)`. The proof of thm:main fixes the putative zero `ϱ`
  first, then `W(y) = y^{−ϱ}φ(y)`, and only then lets `D → ∞` (R1 §3.4).
* thm:ms is an average square-root cancellation bound for these particular Möbius coefficients. It
  is not a sextic large sieve for arbitrary coefficients (PR 908 `MATHEMATICAL_AUDIT.md` §2.1).

**The Möbius saving used for thm:main (eq:mobius-saving, line 723).** For every `ε > 0`,

    A_1(D) ≪_{ν,S,W,ε} D^{11/12+ε}.

### 2.3 What is outside the proposed statement

The following are in the manuscript but outside this draft. No review covered them, and they need
their own objects:

* Corollary cor:primes-ap (lines 84-95): a prime number theorem in progressions with error
  `x^{11/12} log x` and an "absolute and effective" constant.
* The arithmetic consequences in lines 97-125: least quadratic nonresidue, Vinogradov's conjecture,
  deterministic algorithms, the class-number bound and idoneal numbers.
* The abstract's sentence (line 47) that the theorem "rules out the existence of Landau–Siegel
  zeros".
* The phrase "We establish the quasi-Riemann hypothesis" in the abstract (line 47). Here that phrase
  means only the zero-free half-plane of Section 2.1.

## 3. Scope

| Dimension | Scope of the proposed statement |
|---|---|
| Finite / global | **global**: every height, every member of the family |
| Conditional / unconditional | unconditional as written, given the imported theorems of Section 4 (no RH or GRH input; R1, R2, R3) |
| Uniformity | qualitative. The abscissa is uniform; constants are not. The `W`-dependence has derivative order at least `5·4^⌈4/ϑ⌉ − 4` (R2 F3), and `‖W‖_{C^k} ≍ |Im ϱ|^k`, so there is no height-uniform estimate |
| Effectivity | the deduction of thm:main is qualitative, by contradiction at a fixed zero. The "effective" claim in cor:primes-ap is not reviewed |
| Family | finite-order Hecke characters of `Q(√−3)`, hence Dirichlet characters. Nothing about other number fields or higher-degree L-functions |
| Relation to RH | none directly. RH would place every nontrivial zero of `ζ` on `Re s = 1/2`. This statement only excludes `Re s > 11/12`. By the functional equation, primitive L-functions then also have no nontrivial zeros in `Re s < 1/12`; that is a standard consequence, not part of the reviewed statement |

## 4. Native versus imported

### 4.1 Native to the manuscript (proved there; every line read by the reviews)

* The reduction thm:ms ⇒ thm:main (lines 694-771): extraction through sixth-power rows `u = p⁶`,
  a Mellin contradiction, and the Dirichlet transfer.
* The Möbius-absorption identities, Lemma lem:arithmetic (statement 823-857, proof 2691-2872). They
  are derived from classical Gauss-sum and reciprocity facts.
* The Poisson reduction: lem:poisson (875-932), lem:remove-exclusions (962-992) and
  prop:poisson-reduction (1000-1252).
* The canonical descent: prop:canonical (1261-1277, proof 1516-1609), lem:cube-reduction
  (1341-1467), prop:transfer (1487-1509, proof 2217-2683) and sec:completion (1611-1629).
* The fixed-ray-class theta transformation (lem:reflection 1805-1821; lem:reflection-uniformity
  1847-1855; lem:theta-bounds 1859-1877; proofs 2904-3479). The manuscript calls it "a variant" of
  the Dunn–Radziwiłł transformation (lines 387, 2881). It is derived from imported theta data.
* lem:squarefree-completed (1923-2187) and prop:R (1317-1333, proof 2189-2214).
* The smoothing lemmas lem:smooth, lem:smooth-mean-square and lem:recombine (3491-3650).

### 4.2 Imported external theorems (not re-proved here)

| # | Imported theorem | Where used (paper2.tex lines) | How it was checked | Label |
|---|---|---|---|---|
| I1 | **Goldmakher–Louvel** quadratic large sieve over number fields, Thm 1.1 (Math. Proc. Camb. Phil. Soc. 154 (2013) 193-212; arXiv:1112.1642v2). It bounds the mean square by `(MN)^ε(M+N)Σ\|λ\|²`. | lem:quadratic 1886-1913; used at 2129-2141 | Hypotheses (GL Def. 1) checked against the family `ψ_k(x) = (x/k)_2 κ_λ(x)^{e_k}`. The use matches Thm 1.1 exactly, with transposition handled by classes or GL Lemma 4.5. GL's proof was read for its use of the hypotheses, but its estimates were not re-derived. Checks G1-G5 are EXACT. (R3 §6; residual §1) | IMPORTED, refereed |
| I2 | **Dunn–Radziwiłł** (Ann. of Math. 200 (2024) 967-1057; read as arXiv:2109.07463v3). Used: the cubic theta normalization (§5.1, (5.7)-(5.8)), the cusp expansions (5.9), (5.13)-(5.15) and App. A table rows 10 and 19, the Kubota character (5.4)/(5.5)/(5.11), the supplementary law (1.5), and as consistency checks Cor. 5.1 and Props 5.1-5.2. | 1643-1660, 1762-1769, 2932-2936, 3032-3106, 3154-3158, 3405 | Quoted correctly; three equation pointers are off (cosmetic). Automorphy under 12-14 group elements and the cusp expansions were checked to `5e-15` (FLOAT). Only DR's unconditional, Patterson-type material is used, not their GRH-conditional results. The journal version was not compared with v3. (R3 §1) | IMPORTED |
| I3 | **Patterson** 1977, Thm 8.1 and Tables II-III: the coefficients `τ(ℓ)` of the cubic theta function. | 1659, 3032, 3106 (through DR) | Not read. DR's transcription was tested numerically for automorphy instead (R3 §9). | IMPORTED (via DR) |
| I4 | **Kubota** 1969: the cubic theta function is automorphic for `Γ₁(3)` with multiplier `(c/a)_3`. | 1647-1660, 3149-3200 | Through DR. The multiplier convention was discriminated numerically: the conjugate convention fails by `√3` (R3 check A). | IMPORTED, classical |
| I5 | **Landau** prime ideal theorem (Math. Ann. 56 (1903); IK04 Thm 5.33): `≍ Y/log Y` prime ideals with `Y/2 < N𝔭 ≤ Y`. | 705-707 | Standard (R1 §3.1). | IMPORTED, classical |
| I6 | **Hecke**: meromorphic continuation of `L_K(s, ν)` (Hec20; IK04 §5.10). | 751-753 | Standard. The one-line repair N1 excludes `s = 1` for principal `ν` (residual §3). | IMPORTED, classical |
| I7 | **Lattice Poisson summation** (IK04 Thm 4.5) and the primitive Gauss-sum evaluation (IK04 (3.12)). | 916-932, then reused at 2230-2494 | The normalization (self-dual measure, covolume 1) was re-derived. Check C4 replays the formula to `3e-14` (R1 §4.3). | IMPORTED, classical |
| I8 | **Hecke's quadratic Gauss-sum reciprocity**: the closed form `Γ_quad` (eq:quadratic-gaussian). | 2783-2800 (proof sketched through Gaussian-regularized Poisson) | Accepted as classical. Checked numerically by C2 and by the w5copg numerics (R1 §4.1). | IMPORTED, classical (sketch in source) |
| I9 | **Cubic and sextic reciprocity** with the supplementary laws (Eisenstein; DR (1.5)). | 2780, 2847-2851, 2931-2936, 3185-3200 | Used by hand in R1 §4.1 and R3 §3. Sextic reciprocity was checked numerically in the earlier numerics, not in these reviews (R3 §6). | IMPORTED, classical |
| I10 | **Gauss–Jacobi** identity (IK04 (3.18)). | 2709 | Re-derived in R1 §4.1. | IMPORTED, classical |
| I11 | **Dirichlet**: `L(1, χ_{−3}) > 0` (Dav00 Ch. 4 and 6). | 768-770 | Standard (R1 §3.3). | IMPORTED, classical |
| I12 | **Quadratic base change**: `L_K(s, χ∘N) = L(s,χ)L(s,χχ_{−3})` up to finitely many Euler factors. | 760-767 | Euler factors at split, inert and ramified primes checked by hand (R1 §3.3). | classical; locally re-verified |
| I13 | **Analytic standard facts** in app:fixed-ray: the Bessel–Mellin integral (DLMF 10.43.19), Phragmén–Lindelöf (IK04 §5.A.4, Thm 5.53), Stirling. | 3317-3323, 3395-3418, 3452-3478 | Full argument written out (residual §2). FLOAT checks C1, C2 and check H. | IMPORTED, classical |
| I14 | **Elementary tools**: character orthogonality on a finite ray class group (IK04 §3.1), Möbius inversion (IK04 (1.18); DR (8.2)), Fubini/Tonelli, the identity theorem. | 813, 1373-1374, 727-759 | Used as stated. | classical |

The following are cited in the manuscript but are not load-bearing. Yoshimoto 1987 (line 2882) is
background for the transformation. Petrow–Young 2019 (line 3523) is a "see also". Heath-Brown 1995
supplies the enlargement device but is not invoked as a theorem. Blomer–Goldmakher–Louvel appears
only as a contrast (line 412). Two facts enter only through other routes: GL's own proof uses that
primitive quadratic Hecke characters have root number `1` (residual §1.5), and the repair N2 uses
Whitney's theorem on even functions (residual §3).

## 5. Dependency chain (paper2.tex line ranges)

```text
thm:main (73-75)                                              [deduction 694-771; R1]
 ├─ Landau PIT (I5), Hecke continuation (I6), base change (I12), L(1,chi_-3) > 0 (I11)
 └─ thm:ms (679-689)                                          [proved in sec:completion 1611-1629; R1/R2]
     ├─ prop:poisson-reduction (1000-1022; proof 1024-1252)    [R1; C5, C6]
     │   ├─ lem:arithmetic (823-857; proof 2691-2872)          [R1; C2, C3; R2 E]
     │   ├─ lem:poisson (875-932) ← lattice Poisson (I7)       [R1; C4]
     │   ├─ lem:remove-exclusions (962-992)                    [R1]
     │   ├─ lem:smooth-mean-square (3566-3615)                 [R1, R2]
     │   └─ hypothesis eq:auxiliary-target (1008-1013) ─────────┐
     └─ prop:canonical (1261-1277; proof 1516-1609),           │ supplied with kappa = theta/2, C0 = 2
        induction over ceil(C0/kappa) levels  ◄────────────────┘ [R2; A, C, F]
         ├─ lem:cube-reduction (1341-1356; proof 1358-1467)    [R2]
         │   └─ prop:R (1317-1333), used at 1389-1400 ◄── AUTOMORPHIC CORE
         │       proof 2189-2214                               [R3]
         │       └─ lem:squarefree-completed (1923-1936; proof 1937-2187)   [R3; residual]
         │           ├─ lem:theta-realization (1686-1718)      [R3; G]
         │           ├─ lem:reflection (1805-1821)             ┐
         │           ├─ lem:reflection-uniformity (1847-1855)  ├ proofs 2904-3479 [R3; A-F, H]
         │           ├─ lem:theta-bounds (1859-1877)           ┘ contour shift 3395-3418 [residual; C1, C2]
         │           │   └─ DR / Patterson / Kubota theta data (I2-I4), reciprocity (I9), I13
         │           ├─ lem:quadratic (1886-1913) ← Goldmakher-Louvel Thm 1.1 (I1)   [R3; residual; G1-G5]
         │           ├─ lem:smooth (3491-3524)                 [R1; residual §1.4]
         │           └─ lem:recombine (3621-3650)              [coordinator; residual §1.4]
         └─ prop:transfer (1487-1509; proof 2672-2683)         [R2; B, D, E, F]
             ├─ lem:first-transfer (2263-2349)   ← lem:poisson, eq:convert1/2, eq:quotient
             ├─ lem:arithmetic-poisson (2407-2494)
             └─ lem:second-transfer (2496-2670): regrouping and sign sum, which forces f' | k' (2550-2585)
```

The only load-bearing input to the descent that is not elementary or classical is **prop:R**.
R2 treated it as a black box. R3 and the residual note reviewed it.

## 6. Review record (bounded agent reviews; not independent human review)

All of these reviews were written by AI agents on this branch, and their commit trailers name
Claude. They read the same frozen source. They overlap in model and context, so they are not
independent of one another in the sense of [docs/REVIEWING.md](../../../../../docs/REVIEWING.md).
The verdict wording below is quoted or closely paraphrased from each file.

| Review | Lines of paper2.tex covered | Method | Script, result | Recorded verdict |
|---|---|---|---|---|
| [R1](../../reviews/OCT5_R1_REDUCTION_POISSON.md) | 206-1252 (206-658 outline: internal arithmetic only); 2689-2872; 3481-3615 as invoked; the interface 1261-1278 / 1611-1630 for parameters only | line-by-line hand re-derivation of every displayed identity in Section 4 | `oct5_r1_checks.py`, groups C1-C6, ALL CHECKS PASSED. C6 replays the exact Poisson identity end to end at `D ≤ 60`, error ≤ `2e-14` | "Both implications are correct as written, apart from three non-load-bearing expository points" (N1-N3) |
| [R2](../../reviews/OCT5_R2_ITERATION_TRANSFER.md) | 1254-1629; 2217-2683 | line-by-line hand check; prop:R treated as a black box by assignment | `oct5_r2_iteration_check.py`, 53/53 pass | "PASS conditional on Prop prop:R, Lemma lem:arithmetic and Lemma lem:smooth-mean-square (the last was checked here). This is not a verdict on Theorem 1.1." Findings F1-F4 are expository or about uniformity |
| [R3](../../reviews/OCT5_R3_THETA_REFLECTION.md) | 1632-2214; 2874-3479 | line-by-line reading; DR v3 citations checked; GL statement checked | `oct5_r3_theta_checks.py`, groups gauss, G, H, C, D, A, B, F, E all within tolerance; D is 700/700 EXACT | "no wrong step was found". The Kubota residue is absent because the `∂_z̄` derivative kills the constant mode. Three residual items are listed |
| [Residual](../../reviews/OCT5_RESIDUAL_ITEMS.md) | 1886-1913 and 2097-2187 (including 2112-2141); 3395-3418 with 3296-3394 and 3426-3478; 752; 1193-1203 | GL read in full from TeX; contour argument written out in full | `oct5_residual_checks.py`: G1-G5 EXACT, G6 and C1-C2 FLOAT, ALL CHECKS PASSED | GL use "matches GL Thm 1.1 exactly"; contour shift "correct and complete"; N1 and N2 "harmless omission" with one-line repairs |
| Coordinator ([summary](../../reviews/OCT5_REVIEW_SUMMARY.md) §1) | 3617-3650 (lem:recombine) | read | none | "correct (one line)" |

**Coverage.** Together these read lines 206-3650, that is, every proof line. The summary writes
"206–3648"; lines 3649-3650 close the proof of lem:recombine. The gaps between scopes (1630-1631,
2215-2216, 2684-2688, 3480, 3616) are blank or heading lines; this was checked for this draft. Lines
1-205 are the introduction. The statement thm:main (73-75) was read by R1. The corollary and the
consequences (84-125) were not read.

**Non-load-bearing findings, with the repairs recorded by the reviews.**

| ID | Lines | Finding | Recorded repair or status |
|---|---|---|---|
| N1 | 752 | The identity theorem for principal `ν` must exclude `s = 1` | one line; `ϱ ≠ 1` because `ϱ` is a zero and `1` is the pole (residual §3) |
| N2 | 1193-1203 | Smoothness of `Φ̂` near `0` is used but not stated | one line; only bounds on `(t∂_t)^j Φ̂` are needed, and they hold (residual §3) |
| N3 | 206-658 | The outline is labelled "rough" | none needed; Sections 3-4 do not use it (R1 §6) |
| F1 | after 1556 | The regime `𝓗 > X` (`H_c < 1`) is handled but not discussed | one sentence; the contraction then comes from `F^{−2}` (R2 §6) |
| F2 | 604-613 | The outline's "ratio stays fixed" | the proof uses only `𝓗'/Σ' ≤ 𝓗/Σ` (R2 §6) |
| F3 | whole descent | derivative order at least `5·4^⌈4/ϑ⌉ − 4` | no height uniformity; harmless for the qualitative theorem (R2 §6) |
| F4 | 1572, 2588 | some slack is discarded | cosmetic (R2 §6) |
| R3-m1 | 362, 1647, 3154 | DR equation pointers are off; "(5.6)" should be the unnumbered expansion, and (5.5) or (5.11) | cosmetic (R3 §8) |
| R3-m2 | 3099 | the wording "translating ... then applying inversion" | the labels are correct (R3 check F) |
| R3-m3 | 1862 | `m ≥ −4` is a superset of the actual support | harmless (R3 §6) |
| Res-e | 1900-1913 | GL citation could name Lemma 4.5 for transposition; Cor. 1.2 (line 412) is not needed | editorial (residual §1.5) |

**What no review did.**

* Patterson 1977 itself was not read.
* There was no end-to-end numerical evaluation of both sides of eq:reflection. R3 estimated that it
  would need about `10⁶` dual terms.
* Goldmakher–Louvel's estimates were not re-derived. The journal versions of GL and DR were not
  compared with the arXiv versions.
* No human reviewed any part.
* The upstream Lean release does not formalize this argument (Section 7). Its 7/8 targets were
  built later the same day, with `#print axioms` standard for the zeta, Dirichlet and Hecke
  theorems, and comparator accepted the zeta challenge (../../reviews/LEAN_BUILD_ATTEMPT.md).
  That says nothing about the 11/12 proof.

## 7. Known misreadings

1. **"RH (or GRH) is proved."** No. This is a fixed half-plane `Re s > 11/12`. It gives no
   information about the critical line, the strip `1/12 ≤ Re s ≤ 11/12`, multiplicities, or zero
   counts there.
2. **"This improves 7/8."** No. The Sep 30 manuscript claims the stronger `Re s > 7/8`.
   * The Oct 5 introduction calls 11/12 "a natural intermediate step" toward it (line 81).
   * The later date is not a withdrawal of 7/8 (PR 908 `FORMALIZATION_AUDIT.md`).
   * Integrating 11/12 would not integrate 7/8, which is a different and mostly unreviewed argument
     ([SEP30_VERIFICATION_MAP.md](../../reviews/SEP30_VERIFICATION_MAP.md)).
   * PR 910's `139999/160000` is conditional on the 7/8 machinery, not on this packet.
3. **"The result is height-uniform, explicit, or effective."** No.
   * Constants depend on `‖W‖_{C^k}`, with `k ≥ 5·4^⌈4/ϑ⌉ − 4` (about `6·10^24` at `ϑ = 1/10`),
     and `W` depends on the putative zero `ϱ`.
   * No height-local or shrinking-band statement follows (R2 F3; PR 910 §1.1 and §3.2).
   * The "effective" constant of cor:primes-ap is unreviewed.
4. **"`ϑ = 0` is allowed" or "`A_1(D) ≪ D^{11/12}`".** No.
   * `ϑ > 0` is fixed first, and the number of levels `⌈4/ϑ⌉` blows up as `ϑ → 0`.
   * `11/12 + ε` is reached by choosing `ϑ` small after fixing `ε` (lines 717-725).
5. **"The leverage mechanism could reach 7/8 or below with more moments."** Not by this pipeline.
   [RUNG_STRENGTH.md](../../RUNG_STRENGTH.md) shows the following.
   * The extraction boundary depends only on the row/column ratio `ρ`. It is `1/2 + 5ρ/12`, so
     `ρ = 1` gives `11/12` at every moment order (Observation 1, elementary).
   * The Oct 5 toolbox ends in a row-blind large sieve. RUNG_STRENGTH argues that this caps it at
     `ρ ≥ 1`, i.e. at `11/12`. **That cap is labelled HEURISTIC/PROPOSED there.** It is a barrier for
     the stated pipeline, not a theorem about the true size of the moments.
6. **"Prop. prop:R is a sextic large sieve," or "the theta reflection alone gives it."** No.
   * prop:R needs the angular factor `ᾱ(n)ᾱ(b)³`. Without `ᾱ(n)`, the Mellin transform has the
     Kubota pole at `5/6` (R3 §5).
   * It also needs the conversion of the active exponent `j = 1` into the quadratic `χ_p³`, which
     depends on the multiplier convention `θ(gw) = (c/a)_3 θ(w)` (R3 §3, check A).
7. **"The Lean formalization checks this."** No.
   * The upstream Lean release targets the Sep 30 7/8 theorem and the Oct 1 Siegel-zero theorem.
   * When this packet was drafted it had not been built in this repository (PR 908
     `FORMALIZATION_AUDIT.md`). Its 7/8 targets have since been built, and `#print axioms` is standard for the
     zeta, Dirichlet and Hecke theorems. Comparator has accepted the zeta challenge
     (../../reviews/LEAN_BUILD_ATTEMPT.md, Addendum B); the other comparator runs are recorded
     there. None of this formalizes the 11/12 argument.
8. **"The numerical checks are evidence for the theorem."** No.
   * They are finite and at tiny scales (`D ≤ 60`, norms ≤ a few thousand). They test conventions
     and exact identities.
   * They replay no analytic estimate. The FLOAT checks are not directed or certified (CHECKS.md).
9. **"Agent agreement means it is reviewed."** No. Three agent reviews plus a residual note make
   one bounded, non-independent review record. Integration needs an exact-SHA independent review.
10. **"The corollaries are reviewed."** No. cor:primes-ap, the Landau–Siegel sentence and the
    arithmetic consequences (lines 47, 84-125) are outside this draft.
11. **"A large `A_1(D)` would be visible on the primal side and lost by positivity."** No.
    * The Poisson identity is exact over all `u ∈ O` (C6).
    * The only inequality used before the dual estimate is positivity of `Φ`.
    * The sixth-power rows are ordinary terms (R1 §5).

## 8. The smallest statement whose failure would invalidate the result

**Prop. prop:R (eq:R, lines 1317-1333), in the form used at lines 1389-1400.** Fix
`ε > 0`, `C₀ ≥ 1` and a ray class character `ξ`. For `1 ≤ 𝓗, X, N(f) ≤ D^{C₀}`, squarefree primary
`f` prime to `S`, and `W ∈ C_c^∞(I)`, it asserts

    Σ_{0<N(k)≪𝓗} |T(X;k,f)|²  ≪_{I,ξ,S,ε,C₀}  D^ε ‖W‖²_{C^J(I)} (𝓗 + 𝓗² N(f)/X),

**with no term that grows with `X` alone** (no Patterson-type `X^{5/6}` main term). Here `𝓗` is a
dual row range, as in the manuscript, not the original `H = D^{1+ϑ}`.

* The rest of the chain is a deduction from prop:R, lem:arithmetic (exact algebra) and classical
  theorems (R1, R2).
* The cube cutoff `H_c³ = min(X, X²/𝓗²)` and the contraction rate are calibrated to this exact
  shape. R2 §6.4 notes that a weaker prop:R, for example one with an extra `X^{2/3}` term, would
  change both.

Inside prop:R, the review record makes three facts load-bearing. Each would invalidate it on its own:

1. **No Kubota residue.** `T(s, Ψ)` is entire, because `∂_z̄` at `z = 0` annihilates the constant mode
   `σv'^{2/3}` at every cusp (lines 3307-3370, 3408; R3 §5; residual §2A).
2. **Active primes become quadratic.** `B_{p,1} = χ_p³` (lines 1735-1745, 3232-3275). The exponent
   is `−j−2` under the multiplier `(c/a)_3`. With the conjugate convention, `j = 1` would give a
   sextic character, and GL would not apply (R3 §3; checks A, C, D, E).
3. **GL Thm 1.1 applies to the family `ψ_k`** (I1). A failure here would mean either an error in
   GL Thm 1.1, which is refereed and published, or a hypothesis mismatch that the residual review
   missed (residual §1).

Outside prop:R, the next-smallest load-bearing statement is the sign-sum regrouping in
lem:second-transfer (lines 2550-2585): `Σ μ(e)μ(w) = τ(r)·1_{f'|k'}` over the preimages of a fixed
`(r, f', k')`, which share one kernel. It is checked exhaustively for up to 6 primes (R2 check D),
and the algebraic argument covers the general case.

## 9. Next-step boundary (what remains before any integration)

1. **Independent exact-SHA review** of prop:R and its proof (1632-2214, 2874-3479). Human scrutiny
   is preferred. Fresh derivations of the three hinge facts in Section 8 should come first. The
   review should be at the commit that contains this draft once frozen, not at a moving branch head.
2. **Read Patterson 1977 Thm 8.1 and Tables II-III** directly, rather than through DR's
   transcription (R3 §9).
3. **Optional, large:** an end-to-end numerical test of eq:reflection with about `10⁶` dual terms
   (R3 §6). This would test the assembled identity, not any estimate.
4. **Integrator decisions.**
   * Allocate a new claim ID. Suggested semantic ID: `IMPORTED.QRH.OCT5.ZERO_FREE_11_12`. No QRH or
     Hecke ID exists in `canonical/` or `research/integrated/*/CLAIMS.tsv` at `d47a04076`; that
     check was run for this draft.
   * Decide whether [PROOF_OUTLINE.md](PROOF_OUTLINE.md) suffices as the resident proof extract, or
     whether the full manuscript text must be resident, with the Apache-2.0 notices.
   * Record N1, N2 and F1 as required editorial fixes, in the style of `VERIFIED_WITH_FIXES`, if an
     independent review concurs. This draft does not assign that verdict.
   * Keep the corollaries (Section 2.3) as separate, unreviewed objects.
5. **Mathematical frontier.** None of this moves RH. RUNG_STRENGTH's (heuristic) analysis puts the
   next step for this architecture at a sub-diagonal (`ρ < 1`) mean square for the sextic family.
   No mechanism for that is known.

### Proposed claim row (for the integrator; no verdict assigned)

| Field | Proposed value |
|---|---|
| semantic_id | `IMPORTED.QRH.OCT5.ZERO_FREE_11_12` (proposed; integrator allocates) |
| statement_short | No finite-order Hecke L-function over Q(√−3), hence no Dirichlet L-function and not ζ, vanishes in Re s > 11/12 (principal poles excluded). |
| source | external manuscript; repository import PR 908 `31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6`, path in §1, SHA-256 `d9a8f15a…0d4d` |
| review evidence | R1, R2, R3, residual items and summary, at `c2050a5dd8c251f25e5fc285c0845b9f4a42487b` (bounded agent reviews) |
| quantifier_scope | global: all heights, all finite-order ν of Q(√−3), all Dirichlet χ; qualitative constants |
| proof_kind | analytic proof using imported theorems I1-I14 |
| rh_relationship | none directly; a fixed zero-free half-plane, not RH |
| required_fix | N1, N2 (one line each); F1 (one sentence); DR equation pointers |
| final_verdict | **not assigned**: awaits an independent exact-SHA review |
| first_broken_arrow | none found by the agent reviews; the smallest failure point is prop:R (§8) |
