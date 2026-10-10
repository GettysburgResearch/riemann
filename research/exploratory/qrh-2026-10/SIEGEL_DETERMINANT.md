# The Oct 1 Landau–Siegel determinant: budget, scaling limits, effectivity

```text
Status: EXPLORATORY. IMPORTED (unreviewed manuscript claims) + PROPOSED (budget algebra, scaling
        analysis, explicit constants) + EMPIRICAL (finite numerics) + HEURISTIC (ideal-bias ceilings).
        No RH claim. RH remains unproved. The manuscript is not reviewed here; nothing below
        validates it.
Scope:  "Uniform exclusion of Landau–Siegel zeros" (OpenAI, dated 1 Oct 2026, 773-line TeX).
        Intake, the budget of its final comparison, how far the mechanism can be pushed,
        effectivity, light numerics, and relevance to the QRH files and this repository.
Exact sources or dependencies:
        pr908:standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
          Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/build/paper.tex (line refs below);
        pr908:.../MATHEMATICAL_AUDIT.md §4 and FORMALIZATION_AUDIT.md;
        pr908:.../upstream/lean/OAI/NumberTheory/SiegelZeros/{Estimates/GeometricBoundary,
          Intersection/BezoutBoundary,Characters/CharacterMaster,Conclusions/Theorem}.lean (read, not built).
        Standard imports: Davenport, Multiplicative Number Theory (ch. 12, 14); Rosser–Schoenfeld
        (1962) explicit Mertens/Chebyshev bounds.
What was actually run:
        scripts/siegel_budget.py   (exact-rational ledger + closed forms; 17/17 checks pass)
        scripts/siegel_numerics.py consts | bias | det N d H | rect N d
          (float prime sums to 2·10^6; exact determinants in Z[√d,√2] for N=2,3, M=16,81)
Smallest remaining gap:
        For the manuscript: an independent, complete review of Lemma 3 (interpolation) and
        Lemma 7 (divisibility). Neither PR 908 nor this file found a defect, and neither is a review.
        For "pushing the method": no version can see zeros farther than O(1/log q) from s = 1
        (§3). The logarithmic scale is intrinsic.
```

## 0. Summary

* **IMPORTED.** The claim is that some absolute `c > 0` has `(1−β) log q ≥ c` for every real zero `β ∈ (0,1)` of every primitive nonprincipal real `L(s,χ)` with `q ≥ 3`.
* **PROPOSED (budget).** The final comparison closes if and only if, for some `λ = log U / log q`,

  ```text
  Γ(ε) := 1 − κ(1+ε)  >  (C1 + c_arch(1+ε))/λ  +  Cδ·δ·λ  +  R_num/(λ log q),
  ```
  where:
  * `κ = log N/log U = 3/4` comes from `U³ = N⁴`;
  * `ε = S2/S1 ≤ 7 226 112/H` is the weight;
  * `c_arch = 1/2` comes from `|√d| ≤ √q`;
  * `C1 = 1 + e/4` and `Cδ = e/2` are the explicit constants of Lemma 2;
  * `R_num ≈ log H + 4.6` collects the finite-size terms.

  The optimum is `δ_max = Γ²/(4Cδ(C1 + c_arch(1+ε)))`. This gives `δ_max ≈ 0.0029` with the paper's `ε = 1/12` and `≈ 0.0053` as `ε → 0`.
* **PROPOSED (structure).** The method is exactly balanced in the generic case. The Frobenius classes that Lemma 7's mechanism can use are `{id, σ, στ}`, with Chebotarev density 3/4, and that equals `κ`. A Siegel zero moves the Frobenius mass into `{σ, στ}` and breaks the balance. The auxiliary `√2` exists to make `κ < 1`.
* **PROPOSED/HEURISTIC (limits).**
  * (a) The scale is logarithmic and intrinsically so. Under ideal bias the paper's version cannot exceed `δ < (1 − ln 2)/2 ≈ 0.153`, and no variant can exceed `δ < 2`.
  * (b) More square roots raise the margin `1 − κ` from 1/4 towards 1/2, never past it. Beyond `n = 4` they need a new interpolation lemma, and they improve the rigorous constant by at most a factor 4.
  * (c) It is blind to the middle strip and to complex zeros beyond a disc of radius `O(1/log q)` at `s = 1`.
  * (d) The proof is effective. Following the manuscript's own constants gives `c ≳ 3·10⁻⁴` for all `q ≥ 3` (conditional on the manuscript).
* **EMPIRICAL.**
  * Exact `N = 2, 3` determinants satisfy Lemma 7's divisibility at every admissible prime. They fail it at the unusable class `τ` (e.g. `v₅ = 32 < 168`).
  * Fields with long inert runs (`D = −163`, `−424708`) show inert shares above 3/4 only for `X ≤ q^{0.75}`. The comparison runs at `X ≈ q^{24}`.

## 1. Intake

### 1.1 Statements (IMPORTED; TeX line numbers)

Notation: `χ` is primitive, real and nonprincipal of conductor `q ≥ 3`. `β ∈ (0,1)` is a real zero, `ℓ = log q` and `δ = (1−β)ℓ`.

| Item | Lines | Exact content and quantifiers |
|---|---|---|
| **Theorem 1** | 66–73 | `∃ c > 0` absolute `∀ q ≥ 3 ∀χ ∀β`: `(1−β) log q ≥ c`. |
| **Lemma 2** (prime bias) | 181–244 | `∀ X ≥ 3`: (2.1) `Σ_{p≤X, χ(p)=1} log p/p ≪ ℓ + δ(log X)²/ℓ`. `∀` integer `H ≥ 2`: (2.2) `Σ_{H<p≤X, p∤2q, χ(p)=−1} log p/p ≥ log X − Cℓ − Cδ(log X)²/ℓ − C_H`, with `C` absolute and `C_H` depending only on `H`. Proof: Hadamard/functional-equation formula (2.3) at `s = 1 + 1/log X`, keeping only the `β` term (2.4), with Mertens. |
| **Lemma 3** (interpolation) | 252–408 | Let `A: ℂ⁴→ℂ³` be surjective with `ker A = ℂc`, where `c` has four ℚ-independent coordinates. Let `N ≥ 1` and let integers `t_j ≥ 3(N−1)` satisfy `∏(t_j − 3(N−1) + 1) > (4N−3)⁴`. Then evaluation `P_t → ℂ^{E_N}` is surjective, where `E_N = {0..N−1}⁴`. There are no constants, and the result is uniform in `A`. |
| **Corollary 4** | 410–432 | `1 ≤ H ≤ N`, `U = N^{4/3}`, `T1 = 32H^{2/3}U`, `T2 = T3 = 32H^{−1/3}U`. The monomial rows with `α_j ≤ T_j` span `ℂ^{E_N}`. |
| Remark 5 | 434–443 | The torus/multiplicity interpretation. |
| Setup | 451–515 | `D` fundamental, `ℚ(√D) = ℚ(√d)`, `d ≠ 1, 2`, `K = ℚ(a,b)` with `a² = d`, `b² = 2`, `R = ℤ[a,b]`. `A` as in (4.1), with `ker A = ℂ(ab, b, −a, −1)`. The rows `R_α` have entries `θ_n^{α1} σ(θ_n)^{α2} στ(θ_n)^{α3}`. Rows are taken greedily over `K` in order of `w(α) = α1 + Hα2 + Hα3`. `Δ ∈ R∖{0}`, `S1 = Σα1`, `S2 = Σ(α2+α3)`. |
| **Lemma 6** | 517–550 | `∀` fixed `H ≥ 1` and `N ≫_H 1`: `S1 ≥ c0 M H^{2/3}U` and `S2 ≤ C0 M H^{−1/3}U`, with `c0 = 1/(4·97²)` and `C0 = 192`. |
| (5.1) Archimedean bound | 562–577 | `¼ log|NΔ| ≤ (M/2) log M + (S1+S2)(log N + ℓ/2 + log 8)`. |
| (5.2) Frobenius relation | 580–596 | For an admissible prime `p` (`p > H`, `p∤2q`, `χ(p) = −1`), `θ^p ≡ g_p(θ) mod pR`, where `g_p = σ` if `(2/p) = 1` and `g_p = στ` otherwise. |
| **Lemma 7** | 598–638 | For admissible `p`, `Δ ∈ p^{E_p} R` with `E_p = Σ_α ⌊α1/p⌋`. |
| (5.6), (5.7) | 640–661 | `¼ log|NΔ| ≥ S1(log U − Cℓ − Cδ(log U)²/ℓ − C_H) − CMU`. |
| §6 | 663–719 | Assume a sequence with `q → ∞` and `δ → 0`. Fix `H` with `(C0/c0)/H ≤ 1/12`, set `N = ⌈q^γ⌉` with `γ` large, and let `q → ∞` in (6.2). This gives `1 ≤ 13/16 + 1/16`. |

**Dependency chain.**
* Theorem 1 ⇐ §6 (6.2) ⇐ the upper bound (5.1) and the lower bound (5.7), with Lemma 6.
* (5.1) uses Hadamard's inequality. It also needs `Δ ≠ 0`, which comes from Corollary 4 ⇐ Lemma 3.
* (5.7) ⇐ Lemma 7 ⇐ (5.2), using the greedy order; plus Lemma 2 (2.2) and Chebyshev.
* Lemma 6 ⇐ the weight bound `96H^{2/3}U` from Corollary 4.

Only two analytic inputs are used: the explicit formula (2.3) and Mertens/Chebyshev. The proof uses no GRH, no Siegel's theorem, no zero density and no second exceptional character.

### 1.2 What PR 908 already established (not repeated here)

* MATHEMATICAL_AUDIT §4 gives a five-step read-through and reports "no defect identified". It notes that the row-operation matrix `L` need not be integral, because the integrality of the replacement entries carries the divisibility.
* That audit's 27 exact checks concern the QRH papers only. None concern this paper.
* FORMALIZATION_AUDIT covers several points:
  * the exported Lean statement: existential `c`, both parities, `q ≥ 3`;
  * the root `SiegelZeros.Main`, with 306 internal imports and a clean token scan;
  * the final step through `Intersection.BezoutBoundary`;
  * the Lean was not compiled.

### 1.3 New intake observations (PROPOSED unless marked)

* I read Lemmas 3, 6 and 7, (5.1) and §6 line by line. No defect found. This agrees with PR 908 and is not a review.
  * Lemma 3 is elementary. The steps are:
    1. Choose a nearest nonvanishing lattice point to `K = 4P`.
    2. A supporting face `G` gives a vertex `u` with `y − u ∈ 3P`.
    3. The off-face points vanish by strict decrease of distance.
    4. Lagrange interpolation on the face finishes. It needs `A|_H` bijective, which needs a **one-dimensional** kernel; this matters in §3(b).
  * In Lemma 7, the lower rows `R_{α−pme1+me_j}` have weight `w(α) − m(p−H) < w(α)`. They therefore lie in the `K`-span of earlier retained rows, so `det` is preserved and each replaced row lies in `p^k R`.
* The Lean final assembly (`Estimates/GeometricBoundary.lean`) hard-codes `H := 86713344` and `18818 ≤ N`. These equal `12·C0/c0` and `2·97²`. `siegel_budget.py` checks them, and they agree with the TeX.
* The Lean spanning hypothesis `ActualCutoffSpanning` (rows of weight `≤ ⌊96 H^{2/3}N^{4/3}⌋` span) is discharged through `localIsolatedBezout_of_actual_regular_selection`, a Bézout/torus-jet multiplicity route, and not through TeX Lemma 3. The TeX and Lean therefore give **different proofs of the spanning input**. This is read from the source and not compiled.
* The case `d = 2` (`q = 8`, `χ₈`) is excluded at TeX 456/675. Lean handles it with `chiEightComplex` in `Characters/ExceptionalConductor.lean`.

## 2. Budget ledger (`scripts/siegel_budget.py`)

### 2.1 Explicit Lemma 2 (PROPOSED derivation; constant sign EMPIRICAL-checked)

On `(1, 2]`, `−ζ'/ζ(s) − 1/(s−1) < 0` (standard). Also `½ψ((s+ε)/2) ≤ ½ψ(3/2) < ½ log π`. So the additive constant in (2.4) can be taken as `0`. The script's `consts` mode finds the maximum of the full constant `c(s)` to be `−0.984` on a 200-point grid. Hence

```text
M₊(X) := Σ_{p≤X, χ(p)=1} log p/p  ≤  (e/2)[ℓ/2 + (1−β)(log X)²]  =  (e/4)ℓ + (e/2)·δ(log X)²/ℓ.
```

Rosser–Schoenfeld give `Σ_{p≤X} log p/p > log X − 1.3326 − 1/(2 log X)`. Combined with the paper's crude bound `Σ_{p|q} log p/p ≤ ℓ`, the admissible share of the mass up to `X = q^λ` is

```text
φ_adm(λ) ≥ 1 − (1 + e/4)/λ − (e/2)·δ·λ − (log H + 1.83 + (log 2)/2)/(λℓ).        (★)
```

### 2.2 The contradiction condition (PROPOSED; arithmetic EXACT)

Divide (5.7) ≥ … ≥ (5.1) by `S1 log U`, put `λ = log U/ℓ` (the paper has `λ = 4γ/3`) and `ε = S2/S1`:

```text
φ_adm(λ)  >  κ(1+ε)  +  c_arch(1+ε)/λ  +  [(1+ε) log 8 + 1.01624/(c0 H^{2/3}) + negligible]/(λℓ)
⟺  Γ(ε) = 1 − κ(1+ε)  >  (C1 + c_arch(1+ε))/λ + Cδ δ λ + R_num/(λℓ).
```

| Source of each term | Quantity | Value |
|---|---|---|
| Full Mertens mass of primes `≤ U` (all admissible under a Siegel bias) | `1` | 1 |
| Dimension count: 3 coordinates, 4-dimensional lattice, `U³ = N⁴` | `κ = log N/log U` | 3/4 |
| Weight `H` (Lemma 6) | `ε = S2/S1 ≤ (C0/c0)/H` | `≤ 7 226 112/H`; 1/12 at `H = 86 713 344` |
| Prime bias forced by the zero (Lemma 2) | `C1/λ + Cδδλ` | `C1 = 1 + e/4 ≈ 1.680`, `Cδ = e/2 ≈ 1.359` |
| `log q` in the Archimedean size: `|√d| ≤ √q` | `c_arch(1+ε)/λ` | `c_arch = 1/2` |
| Finite size: `C_H`, `log 8`, Mertens, `MU/S1` | `R_num` | `≈ log H + 4.6` (22.9 at the paper's `H`) |

The paper's own split (TeX 693–718) is `13/16 + 1/16 = 7/8 < 1`. The script checks it exactly.

In closed form, with `a = C1 + c_arch(1+ε) + R_num/ℓ`, the best `λ` is `2a/Γ` and

```text
δ < δ_M(ℓ) = Γ² / (4 Cδ a),      δ_max = lim_{ℓ→∞} δ_M = Γ² / (4 Cδ (C1 + c_arch(1+ε))).
```

| Constants | Γ | δ_max | λ* (γ* = 3λ*/4) |
|---|---|---|---|
| paper, `ε = 1/12` | 3/16 | 0.00291 | 23.7 (17.8) |
| paper, `ε → 0` | 1/4 | 0.00527 | 17.4 (13.1) |
| `C1 = e/4` (`Σ_{p\|q} = o(ℓ)`), `ε → 0` | 1/4 | 0.00975 | 9.4 (7.1) |

### 2.3 The algebraic half in one line (PROPOSED restatement, conditional on Lemmas 3/6/7)

Drop Lemma 2. Then (5.1) and (5.6) alone give an unconditional statement for every real primitive `χ` with `d ≠ 2`, every `H ≥ 2` and every `N ≥ max(H, 18818^{3/4}H^{−1/2})`, where `U = N^{4/3}`:

```text
Σ_{p≤U, χ(p)=+1} log p/p  ≥  (1/4 − 3ε/4) log U − (3/2 + ε/2) ℓ − log H − O(1).
```

That is, split primes carry at least about a quarter of the log-mass up to any `U ≥ q^{C}`. Lemma 2 says a zero with small `δ` forces `M₊(U) ≤ (e/4)ℓ + (e/2)δλ²ℓ`. The theorem is the collision of the two. Seen this way, the manuscript is a Mertens-level, Chebyshev-style divisibility bound for a Chebotarev class.

### 2.4 Generic balance (PROPOSED observation; consistency check, not evidence of correctness)

The proof of Lemma 7 also works verbatim for split-completely primes, where `Frob = id` and `θ^p ≡ θ`, because the replaced rows drop weight by `m(p−1) > 0`. The usable Frobenius set is therefore `{id, σ, στ} = G∖{τ}`. Its Chebotarev density 3/4 equals `κ` exactly.

For a field without a Siegel zero, the divisibility lower bound and the Hadamard upper bound therefore agree at leading order, `S1·¾ log U`. The method cannot prove a false Chebotarev statement, and the margin it exploits is entirely the zero-induced shift of Frobenius mass from `{id, τ}` to `{σ, στ}`.

This also explains the auxiliary `√2`:
* Over `ℚ(√d)` alone with coordinates `{θ, σθ}`, `κ = 1` and every class is usable, so there is no margin.
* With `{θ}` alone, only split primes are usable.

The finite slack check in §4.2 is consistent with the balance.

## 3. Scaling limits

### (a) Bias versus δ; the logarithmic scale is intrinsic

* **Rigorous share** (PROPOSED, from (★)): at `X = q^A` the inert share is at least `1 − (1+e/4)/A − (e/2)δA − O((log H)/(Aℓ))`. The best value over `A` is `1 − 2√((1+e/4)(e/2)δ)`. The comparison closes iff `δ < δ_M(ℓ)`, which tends to 0.0029–0.0098 depending on the constants (§2.2).
* **Heuristic true share** (HEURISTIC; one real zero, explicit formula, other zeros ignored): `β` contributes `−(1−X^{β−1})/(1−β) = −(ℓ/δ)(1−e^{−x})` to `Σ_{p≤X} χ(p) log p/p`, where `x = δA`. So `φ₋(q^A) ≈ ½ + (1−e^{−δA})/(2δA)`.
  * The paper's inert-only comparison needs `1 − e^{−x} − x/2 > 2c_arch δ`.
  * The supremum is `δ < (1 − ln 2)/(4c_arch)`: **0.153** for the paper's cube box and 0.307 for an anisotropic box. In the cube box `n2` and `n4` range to `N/√|d|`, so the house is about `N q^{1/4}` and `c_arch = 1/4`.
  * The rigorous version loses a factor of about 50 against this. The loss comes from Lemma 2's quadratic `δ(log X)²` (no saturation) and from the crude `C1`.
* **Why `δ` must stay `O(1)`** (PROPOSED):
  * The zero's total bias in log-mass is at most `ℓ/δ`, so the extra usable mass is at most `ℓ/(2δ)`.
  * Every variant must pay an Archimedean `c_arch·ℓ ≥ ℓ/4` per unit of degree. `N⁴` distinct elements of `ℤ[√d,√2]` must have house `≳ N|d|^{1/4}`, since the covolume is `≍ |d|`. That is HEURISTIC as a lower bound for what Hadamard can deliver.
  * Therefore `δ < 2` in every variant (§3(b) table), and the paper's variant is `≤ 0.153` even with ideal bias.
* **Answer.** Excluding `1 − β ≥ (log q)^{−1+η}`, i.e. `δ = ℓ^η → ∞`, is impossible by this mechanism: the bias would be `≤ ℓ^{1−η} = o(ℓ)`. The method is intrinsically logarithmic.
  * The only escape would run the comparison at `U = q^{o(1)}`, i.e. `λ → 0`.
  * Both `log q` costs block that: the conductor term `(e/4)ℓ` of Lemma 2, which reflects genuine low-lying-zero noise, and the Archimedean `ℓ/4`.

### (b) Dimension count for more square roots or other Frobenius patterns

Setup:
* `L ⊃ ℚ(√d)` is Galois with group `G` of order `n`, and `G0 = Gal(L/ℚ(√d))`. A Siegel zero puts Frobenius in the coset `σG0`.
* Use coordinates `S ⊂ G` with `id ∈ S`, the favored coordinate being `θ` itself, and `k = |S|`.
* Then `U^k = N^n`, `κ = k/n`, and the generic usable density is `|S|/n = κ` (balance again).
* All Siegel-biased primes are usable iff `S ⊇ σG0`, so the minimum is `k = n/2 + 1` and `κ = 1/2 + 1/n`.
* The same count holds for non-abelian `G`, e.g. the `S₃` closure of a cubic field with quadratic resolvent `ℚ(√d)`, where `κ = 2/3` (HEURISTIC).

| n | k | κ | margin 1−κ | ideal ceiling, cube | ideal ceiling, aniso | codim-1 choice `G∖{g*}`: κ |
|---|---|---|---|---|---|---|
| 4 | 3 | 3/4 | 1/4 | 0.50 | 1.00 | 3/4 (same) |
| 8 | 5 | 5/8 | 3/8 | 0.75 | 1.50 | 7/8 |
| 16 | 9 | 9/16 | 7/16 | 0.875 | 1.75 | 15/16 |
| → ∞ | | → 1/2 | → 1/2 | → 1 | → 2 | → 1 |

The ideal ceiling is `δ < (1−2/n)/(2c_arch)`, using all usable classes including split-completely primes (HEURISTIC). Conclusions (PROPOSED):

1. **The margin improves (1/4 → 3/8 → … → 1/2) but never reaches 1/2.** Half of `G` is the unbiased coset `G0`, and the favored coordinate must lie outside the biased coset.
2. **TeX Lemma 3 only covers `n = 4`.** Its face argument needs `dim ker A = n − k = 1`. For `S = {id} ∪ σG0` the kernel has dimension `n/2 − 1 ≥ 3` once `n ≥ 8`.
   * Within the codimension-1 family (`k = n − 1`), `κ = 1 − 1/n`, so `n = 4` is optimal.
   * Larger `n` needs a field-uniform multiplicity estimate with a higher-codimension kernel (Philippon-type). That is OPEN.
   * Quick obstruction count: the subfield sublattices `O_F` project to `1/2 + 1/f ≥ κ` dimensions per lattice dimension, so subfields give no obstruction (PROPOSED).
3. **The rigorous gain is small.** `δ_max ∝ Γ²` gains at most `(1/2)²/(1/4)² = 4×`, i.e. 0.0053 → 0.021 with the crude Lemma 2. The bottleneck is Lemma 2, not the dimension count.
4. The role of `√2` can be played by any fixed auxiliary quadratic field other than `ℚ(√d)`. That changes the excluded `d` and the constant `log 8`, nothing else.

### (c) Complex zeros and the middle strip: the exact obstruction

* **Weighting is forced.** `E_p = Σ⌊α1/p⌋ ≈ S1/p`, so the lower bound only sees the `log p/p`-weighted mass. The upper bound is `S1·(κ log U + c_arch ℓ)`. The method responds only to cumulative log-mass shifts of size `≳ ℓ` at scale `q^{O(1)}`.
* **Middle strip** (PROPOSED). A zero at `β = 1 − η` shifts `Σ_{p≤X} χ(p) log p/p` by `(1 − X^{−η})/η ≤ 1/η` in total. Its local density excess is `x^{β−1} ≤ q^{−λη}`.
  * The determinant needs at least `c_arch·ℓ ≥ ℓ/4` of extra usable mass.
  * So the mechanism could act only when `log q < 2/η` (script, §D), i.e. for finitely many `q`. Any `β ≤ 1 − η` with `η` fixed is invisible.
  * RH-type information (`β > 1/2`) is power-small against a requirement that is logarithmic.
* **Complex pair** `ρ, ρ̄ = 1 − a/ℓ ± ib/ℓ` of a real `χ` (HEURISTIC).
  * Its cumulative bias tends to `−2ℓa/(a²+b²)`, so it acts like a real zero with `δ_eff = (a²+b²)/(2a)`.
  * The detectable region is the disc `|s − (1 − δ_c/ℓ)| < δ_c/ℓ`, tangent to `Re s = 1` at `s = 1`.
  * With the rigorous `δ_c ≈ 0.003` this disc lies inside the classical zero-free region for non-real zeros (Davenport §14). Explicit classical constants such as McCurley 1984 (`≈ 1/9.65`, quoted but not re-checked) are far larger than `2δ_c`.
  * So there is nothing new for complex zeros. Even the ideal `δ_c ≤ 2` keeps everything within `O(1/log q)` of 1.
* **Non-real `χ`.** There is no two-class Frobenius dichotomy, and classically there are no exceptional zeros to detect.

### (d) Effectivity

* The proof is **effective in principle** (PROPOSED). The step "suppose false, take a sequence" (TeX 665–676) is presentational.
* Every input has an explicit constant:
  * Lemma 2: `e/4`, `e/2`, Rosser–Schoenfeld (§2.1);
  * Lemma 3: no constants;
  * Lemma 6: `c0 = 1/37636`, `C0 = 192`;
  * (5.1): `log 8`;
  * Chebyshev: `θ(x) < 1.01624x`.
* The only qualitative sentence is the bounded-conductor argument at TeX 671–674 ("finitely many characters … analyticity"), and it is unnecessary. In the closed form `δ_M(ℓ) = Γ²/(4Cδ(C1 + c_arch(1+ε) + R_num/ℓ))`, the comparison closes for **every** `q ≥ 3` by taking `λ = 2a/Γ`, which is very large when `q` is small (`log U ≈ 230–270`).
* `δ_M` increases in `ℓ`, so the worst case is `q = 3`. The constant must be read from `δ_M(log 3)`, not from the large-`q` limit `δ_max`. `siegel_budget.py` Part C gives:

| H | ε | δ_M(q=3) | δ_M(q→∞) |
|---|---|---|---|
| 86 713 344 (paper/Lean) | 1/12 | 2.8·10⁻⁴ | 0.0029 |
| 10⁹ | 0.0072 | **4.4·10⁻⁴** | 0.0050 |
| 10¹² | 7·10⁻⁶ | 3.7·10⁻⁴ | 0.0053 |

* **Rough explicit constant (PROPOSED, conditional on the manuscript):** `c ≈ 3·10⁻⁴`, i.e. `(1−β) log q ≥ 3·10⁻⁴` for all `q ≥ 3`, `q ≠ 8`.
  * For `q = 8` (`χ₈`), the reverse-Lemma-2 run (§4.2) gives no real zero in `[1 − 0.231, 1)`, i.e. `δ ≥ 0.48` (EMPIRICAL, floating point).
  * The logarithms are evaluated in floating point, and the transcendental constants are rounded in the conservative direction.
  * The 97² in Lemma 6 and the crude `Σ_{p|q} ≤ ℓ` dominate the loss. Sharper tracking could plausibly give `c ≈ 10⁻²` (HEURISTIC).
* **To make it fully explicit, track:** `C1` and `Cδ` (Lemma 2), `c0` and `C0` (Lemma 6), `R_num` (Mertens and Chebyshev constants, `log H`, `log 8`), and the exceptional `d = 2`.
* The Lean theorem is purely existential (`∃ c`). It supplies no value.

## 4. Light numerics (EMPIRICAL; finite; `scripts/siegel_numerics.py`)

### 4.1 Lemma 2 constant

`consts`: `max c(s) = −0.984 < 0` over `s ∈ (1,2]` and both parities, on a 200-point grid at 30 digits. This supports §2.1.

### 4.2 Prime bias in small-`L(1,χ)` and long-inert-run fields

`bias` uses primes up to `2·10⁶`, the longest inert runs over `|D| ≤ 10⁶`, and float arithmetic. In the table:
* `φ₋` is the inert share of `Σ log p/p`;
* `M₊/ℓ` is the split mass;
* `δ_req` is the smallest `δ` Lemma 2 permits given `M₊`;
* `slack` is `((3/4) log X + ℓ/2 + log 8 − usable)/ℓ`, where usable means `Frob ∈ {id,σ,στ}`;
* the last column is the reverse-Lemma-2 zero-free interval.

| D | h, `L(1,χ)·log q` | least split p | `φ₋` at `λ = 0.5 / 1 / 2` | slack/ℓ (all λ) | no real zero in |
|---|---|---|---|---|---|
| −163 | 1, 1.25 | 41 | 1.000 / 0.817 / 0.642 | +0.96…+0.99 | `[1−0.040, 1)`, δ ≥ 0.20 |
| −67 | 1, 1.61 | 17 | 1.000 / 0.709 / 0.566 | +1.06…+1.20 | `[1−0.093, 1)` |
| −427 | 2, 1.84 | 17 | 0.783 / 0.678 / 0.578 | +0.93…+0.97 | `[1−0.037, 1)` |
| −424708 | 64, 4.00 | 73 | 0.731 / 0.605 / – | +0.70 | `[1−0.0027, 1)` |
| 997757 | –, – | 61 | 0.768 / 0.618 / – | +0.67…+0.68 | `[1−0.0020, 1)` |
| 8 (the excluded `d = 2`) | – | 7 | – | – | `[1−0.231, 1)`, δ ≥ 0.48 |

Readings:
* The bias that small `L(1,χ)` makes visible lives at `λ ≲ 0.75`, where `φ₋ > 3/4`. It has decayed to about 0.6 by `λ = 1–2`. The comparison needs `φ_adm > 13/16 + O(1/λ)` at `λ* ≈ 24`. These fields therefore cannot stress the method, as any correct theorem requires.
* `δ_req = 0` for `λ ≤ 1.5`: there, Lemma 2's `(e/4)ℓ` term absorbs everything, and Lemma 2 cannot distinguish these fields from Siegel-zero fields.
* Slack is positive and stable, which is consistent with §2.4.
* The reverse-Lemma-2 intervals are rigorous only up to floating point and series truncation (truncation only weakens them).

### 4.3 Exact determinants (Lemma 3 / 6 / 7 at tiny N)

`det N d H`:
* The determinant `Δ`, its norm `NΔ` and the valuations `v_p(NΔ)` are exact over `ℤ[√d,√2]` (fraction-free Bareiss).
* The greedy selection was computed modulo three random 61-bit primes and accepted because all three agree. This step is PROBABILISTIC.

| N, d, H | S2/S1 | `¼log\|NΔ\|` vs Hadamard (5.1) | p: class, 4E_p → v_p(NΔ) |
|---|---|---|---|
| 3, −1, 2 | 0.767 | 395.8 ≤ 1703.2 | 3: στ, 204→320; **5: τ, (80)→20**; 7: σ, 32→**32** |
| 3, −1, 3 | 0.374 | 467.8 ≤ 2012.9 | 7: σ, 88→92; 11: στ, 24→28; **5: τ, (168)→32; 13: τ, (12)→0** |
| 3, −3, 2 | 0.723 | 510.1 ≤ 1661.5 | 5: στ, 84→88; 7: **id (split)**, 32→40 |
| 3, −3, 3 | 0.421 | 581.6 ≤ 1877.7 | 5: στ, 148→156; 7: id, 76→120; 11: στ, 16→24; 13: τ, (8)→4 |
| 3, 5 / −7 / −163, 2 | 0.723 | ≤ Hadamard | every admissible p satisfies `v_p ≥ 4E_p`; p = 7 (σ) attains equality, 32 = 32 |
| 2, 5 / −1 / −7, 2 | 0.636 | ≤ Hadamard | every admissible p satisfies `v_p ≥ 4E_p`; d = −1: 5 (τ) gives (4)→0 |

Readings:
* Lemma 7 held at every admissible prime tested and is sometimes sharp (`v₇ = 4E₇`).
* The split-completely extension of §2.4 held.
* At the unusable class `τ`, the valuation is far below `4E_p`, so the Frobenius class is load-bearing.
* Raising `H` from 2 to 3 lowers `S2/S1` from 0.72 to 0.37–0.42, as Lemma 6 predicts.
* An `N = 4` (`M = 256`) run exceeded its 15-minute cap and was not completed.

`rect N d` tests the dimension count of Lemma 3. Spanning was checked by rank modulo a prime: success is exact, failure is probabilistic.
* `N = 2`: the smallest spanning cube is `t = 2`; Lemma 3 guarantees `t = 11`.
* `N = 3`: the smallest spanning cube is `t = 4`; Lemma 3 guarantees `t = 24`.
* Anisotropic boxes `t2 = t3 ∈ {0,…,4}` span with at most `1.25·M` monomials. `t2 = t3 = 0` needs `t1 = M − 1`, the Vandermonde case.
* So the count is essentially optimal at tiny `N`. Lemma 3's constant `32³` is generous, and no projection obstruction was seen.

## 5. Relevance

* **Sep 30 / Oct 5 (Q(√−3) families).**
  * Logically, if the 7/8 (or 11/12) half-plane holds for all Dirichlet `L`, then every real zero has `β ≤ 7/8`. Hence `(1−β) log q ≥ (log 3)/8 ≈ 0.137` for `q ≥ 3`, with `(log 3)/12` from 11/12. That is already far above our `3·10⁻⁴`, so **the Oct 1 theorem is a weak corollary of either QRH claim** (PROPOSED, trivial).
  * Its value is independence: it shares no lemma with theta reflection, moments or the Hecke family. It is short and finite-dimensional, so it is a much cheaper object to referee.
  * Conversely, it cannot touch the families' non-real zeros or the `7/8` boundary (§3(c)).
  * Quadratic rows:
    * A base-change quadratic Hecke character `ν = χ∘N_{K/ℚ}` has `L(s,ν) = L(s,χ)L(s,χχ₋₃)`, so Theorem 1 applies to both factors, with conductors `q` and `≤ 3q`.
    * For a non-base-change quadratic `ν`, an analog needs Lemma 2 over `K` (routine) and a determinant over a degree-8 field. That is codimension 1 with `κ = 7/8` (margin 1/8), or the open higher-codimension lemma. OPEN.
    * Cubic and sextic rows have no exceptional zeros classically, and the method has no purchase on them.
* **Repository programmes** (PROGRAMMES.md; RESULTS_INDEX has no Siegel/class-number entry).
  * For `ζ`, every prime splits in `ℚ`. There is no Frobenius dichotomy to bias, and off-line zeros give only power-small biases (§3(c)). So the mechanism says nothing about RH, Robin or the signed Möbius routes.
  * It is a clean instance of the repository's distinction "fixed-P61 is not growing-prime control". The determinant consumes the `log p/p` mass of all primes up to `q^λ`, and a fixed finite prime set contributes `O(1)` against a required `ℓ/4`.
  * The generic-balance identity (usable Frobenius density = dimension ratio) is a possible template for "detector" arguments in the families programme (#736). That is HEURISTIC; no bridge is constructed here.
* **Effective class numbers.**
  * Theorem 1 says `L(σ,χ) ≠ 0` on `[1 − c/ℓ, 1]`. The standard Siegel–Goldfeld positivity argument then gives `L(1,χ) ≥ (c e^{−Ac}/ℓ)(1 − o(1))`. That argument uses `ζ(s)L(s,χ) = Σ r(n)n^{−s}` with `r ≥ 0`, smoothing `e^{−n/x}` at `x = q^A`, and `ζ(σ)L(σ,χ) < 0` on that interval (Davenport ch. 21 uses the same device). All its constants are effective.
  * The class number formula then gives `h(D) ≫ c√|D|/log|D|` for `D < −4`, and `h(D) log ε_D ≫ c√D/log D` for `D > 0`.
  * **What the stated theorem implies:** these bounds with an **unspecified** constant, since Theorem 1 and its Lean form are existential.
  * **What it does not give as stated:** an explicit class-number bound. That needs (i) the manuscript to be correct, (ii) an explicit `c`, e.g. the rough `3·10⁻⁴` of §3(d), and (iii) explicit constants in the `L(1,χ)` step.
  * Nothing here checks (i). This file does not claim any class-number result.

## 6. Misreadings to avoid

* The theorem does not exclude real zeros in `(0,1)`. It is vacuous for `β ≤ 1 − c/log q`.
* It is not a zero-free region for complex zeros beyond the classical one. It is not GRH, not RH and not a fixed strip.
* "Effective in principle" (§3(d)) is a PROPOSED reading of the proof. The published statement and the Lean statement are existential.
* "No defect found" (PR 908 and here) is not a review. The Lean was not compiled, and Lean and TeX prove the spanning input differently.
* The ideal-bias ceilings (0.153, 0.5, 1, 2) are HEURISTIC upper limits of the mechanism, not theorems.

## 7. Reproduction

```sh
cd research/exploratory/qrh-2026-10/scripts
python3 -I siegel_budget.py                     # < 1 s, 17/17 checks
python3 -I siegel_numerics.py consts            # ~ 5 s (mpmath)
python3 -I siegel_numerics.py bias              # ~ 5 s (numpy)
python3 -I siegel_numerics.py det 3 -1 2        # ~ 3 s; also det 3 -3 3, det 3 -163 2, det 2 5 2, ...
python3 -I siegel_numerics.py rect 3 -1         # ~ 10 s
```
