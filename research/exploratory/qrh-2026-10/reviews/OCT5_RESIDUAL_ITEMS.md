# Oct 5 (11/12) manuscript: the residual items left by R1–R3

```text
Status: REVIEW (bounded; external, unreviewed manuscript). It closes the three residual items in
  OCT5_REVIEW_SUMMARY.md. It is not an integration verdict.
Scope: (1) lem:quadratic (paper2.tex 1886-1913) against Goldmakher-Louvel (GL), and its one use
  (2097-2187, including the lem:smooth separation at 2112-2141); (2) the contour shifts in
  app:fixed-ray, 3395-3418, with the parts of 3296-3394 and 3426-3478 that they rely on;
  (3) R1's minor points N1 (line 752) and N2 (lines 1193-1203).
Exact sources or dependencies:
  manuscript: pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6, path
    standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
    The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex,
    SHA-256 d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d (re-hashed here).
  GL: L. Goldmakher, B. Louvel, "A quadratic large sieve inequality over number fields",
    Math. Proc. Cambridge Philos. Soc. 154 (2013), no. 2, 193-212, doi:10.1017/S0305004112000370
    (metadata read from the DOI landing page); arXiv:1112.1642v2 (31 May 2012), fetched from
    arxiv.org into a new scratch directory: PDF SHA-256 5cc5f033...dd304 (identical to the
    pre-existing local copy), TeX e-print SHA-256 12183c3c...f4947 (identical to the hash recorded by
    R3). Read in full from the TeX: Def. 1, Thm 1.1, Cor. 1.2, Sections 2-7. The journal PDF was not
    read, so the journal numbering was not compared; the arXiv v2 numbering matches the manuscript's
    citations.
  Prior reviews: OCT5_R1_REDUCTION_POISSON.md, OCT5_R3_THETA_REFLECTION.md, OCT5_REVIEW_SUMMARY.md.
What was actually run:
  a line-by-line reading of the scoped lines and of GL; the analytic argument in Section 2 written
  out in full; and reviews/oct5_residual_checks.py (SHA-256
  d175c9736a75c581b0ee314ce013d932ed7c85e9723302b16959cff5acbec9b5), run twice as
  `python3 -I oct5_residual_checks.py --out <scratch>/runN.json` (about 105 s each; Python 3.13.16,
  numpy 2.5.3, scipy 1.18.1). Both runs print ALL CHECKS PASSED and write identical JSON
  (SHA-256 e2892bb2...6adba, kept outside the repo). Labels: EXACT = integer arithmetic in Z[omega];
  FLOAT = ordinary double precision (not directed, not certified). These are finite checks. They
  replay no analytic estimate.
Smallest remaining gap: none found in the three items. What remains imported is GL Theorem 1.1
  itself, a refereed published theorem whose estimates were not re-derived here; its hypotheses
  and the way its proof uses them were checked. The failure that would invalidate item 1 is a
  failure of GL Thm 1.1 for the family psi_k below. Unchanged from R3: there is no end-to-end
  numerical test of eq:reflection.
```

RH remains unsolved. This note concerns a zero-free half-plane `Re s > 11/12` claimed in an
external, unreviewed manuscript. Even if that claim is right, it says nothing about the critical
line. Closing these three items does not make the manuscript reviewed in the repository's sense.
That requires an exact-SHA independent review and a human integrator; see
[OCT5_REVIEW_SUMMARY.md](OCT5_REVIEW_SUMMARY.md) §4.

## 0. Verdicts

| # | Item | Verdict | Evidence |
|---|---|---|---|
| 1 | lem:quadratic vs GL quadratic large sieve | **Matches GL Thm 1.1 exactly.** The family, moduli, primitivity, unit triviality, squarefree support, sharp cutoffs, ranges, the bound `(M+N)(MN)^ε` and the constant dependence all agree. The orientation is transposed; the manuscript's "finitely many ray classes" handles this, or GL Lemma 4.5 does. The use at 2129–2141 is admissible: its coefficients do not depend on the row. | GL TeX read in full (§1.2–1.5); checks G1–G5 EXACT (§1.6) |
| 2 | Contour shift, 3395–3418 | **Correct and complete.** The integrand is entire; `J` is bounded in vertical strips, so `𝒯` has order 1; there are polynomial bounds on both boundary lines, then Phragmén–Lindelöf, then rapid decay of `V̂_*`. No poles: the `∂_z̄` kills every constant mode, `1/Γ` is entire, and the kernel's first pole is at `t = −5/6`. The dual series converges absolutely exactly on `Re t > 1/2`. | full argument (§2); C1, C2 FLOAT, with a discriminating residue control |
| 3a | N1: identity theorem at `s = 1` (line 752) | **Harmless omission.** The zero `ϱ` is never `1`. | §3 |
| 3b | N2: smoothness of `Φ̂` at 0 (1193–1203) | **Harmless omission.** Only `(t∂_t)^j Φ̂` bounded near 0 is needed, and it holds. | §3 |

## 1. The quadratic large sieve (item 1)

### 1.1 What GL prove

**Definition 1** (GL arXiv v2). Take a number field `k ⊇ μ_n` and an integral ideal `𝔠`. An
*n-th order Hecke family* is a collection `{χ_𝔞 : 𝔞 ∈ I(𝔠), 𝔞 squarefree}` of **primitive Hecke
characters of trivial infinite type** with three properties:
1. the order of each `χ_𝔞` divides `n`;
2. `χ_𝔞(𝔟) = χ_𝔟(𝔞) C([𝔞],[𝔟])` for coprime `𝔞, 𝔟 ∈ I(𝔠)`, where `[·] : I(𝔠) → G` is a
   homomorphism to a finite group;
3. `χ_𝔞 χ̄_𝔟` is primitive modulo `𝔞𝔟` whenever `𝔞, 𝔟` are coprime and `[𝔞] = [𝔟]`.

**Theorem 1.1.** Let `{χ_𝔞}` be a quadratic Hecke family with respect to `𝔠`. Then for all
`ε > 0`, all `M, N ≥ 1` and all complex `(λ_𝔟)`,
`Σ*_{N𝔞≤M} |Σ*_{N𝔟≤N} λ_𝔟 χ_𝔟(𝔞)|² ≪_{k,𝔠,ε} (MN)^ε (M+N) Σ*_{N𝔟≤N} |λ_𝔟|²`.
Here `Σ*` runs over **squarefree ideals of `I(𝔠)`** in both variables, and the cutoffs are sharp.
The family index `𝔟` is the *inner* variable.

**Corollary 1.2** is the same bound for `χ_𝔟^{n/2}`, when `{χ_𝔞}` is an n-th order family with
`n ≥ 3` even. The manuscript cites it in the outline (line 412) but does not use it; see §1.5.

### 1.2 What the manuscript states and uses

eq:Q (1886–1899) states
`Σ*_{k≡1(3),(k,S)=1,N(k)≤ℋ} |Σ_{n≡1(3) squarefree, N(n)≍U} β(n) χ_k(n)³|² ≪_{S,ε} (ℋU)^ε(ℋ+U) Σ|β(n)|²`.
Here `χ_k(n)³ = (n/k)_2`, the quadratic residue symbol with `k` in the denominator. `S` contains
the primes above 2 and 3 and the conductor of `ν` (lines 665–667). The row `k` is the family
index, so it is the *outer* variable. The column `n` may meet `S`.

The proof (1900–1913) uses the family `ψ_k(x) = (x/k)_2 κ_λ(x)^{e_k}`, where `λ = 1+2ω`,
`κ_λ` is the nontrivial character mod `λ`, and `e_k = 0` or `1` according as `N(k) ≡ 1` or
`3 (mod 4)`.

The lemma is used once, at line 2129. The coefficients there are
`β(n) = A_m(n,b)(N(n)/U)^{is} N(n)^{−1/2}` on squarefree primary `n` with `N(n)/U ∈ supp V`. The
rows are `k_0` with `N(k_0) ≤ ℋ_0`, squarefree and primary, with `(k_0, gS) = 1` and in one fixed
ray class.

### 1.3 Point-by-point match

| Aspect | GL Thm 1.1 | Manuscript | Match |
|---|---|---|---|
| Field, order | `k ⊇ μ_2`, quadratic family | `K = Q(ω)`, `ψ_k` of order 2 | yes |
| Family members | primitive Hecke characters of trivial infinite type, on ideals | `ψ_k` is trivial on the units `−1, ω` (G1). It is therefore a character of `(O/kλ^{e_k})^×` that factors through ideals; its conductor is exactly `kλ^{e_k}` (G2). It has finite order on an imaginary quadratic field, so its infinite type is trivial. | yes |
| Moduli | conductor `𝔠_𝔞·𝔞` with `𝔠_𝔞 \| 𝔠`; this is also the shape of the Fisher–Friedberg family in GL §2 | `kλ^{e_k}`, with `λ \| 𝔠 := ∏_{𝔭∈S} 𝔭` | yes |
| Property (2) | class function `C` on a finite `G` | `(α/β)_2 (β/α)_2` depends only on `(α mod 4, β mod 4)`: G3, 17 741 coprime pairs, exact. It is the Hilbert symbol at 2; the λ-symbol is trivial on λ-units. So `G = (O/24)^×` via primary generators works, as does `G = (O/4)^×`. | yes |
| Property (3) | `χ_𝔞χ̄_𝔟` primitive mod `𝔞𝔟` when `[𝔞] = [𝔟]` | Same class mod 4 gives `e_α = e_β` (G4). The `κ_λ` factors cancel, leaving `(·/αβ)_2`, which is primitive mod `αβ`. | yes |
| Support | squarefree ideals of `I(𝔠)` in **both** variables | Rows `k` are squarefree with `(k,S) = 1`. Columns `n` are squarefree but may meet `S`; write `n = s_0 n'` with `s_0 \| ∏_{𝔭∈S, 𝔭≠λ} 𝔭` (at most `2^{\|S\|}` choices). Then `(n/k)_2 = (s_0/k)_2 (n'/k)_2` and `\|(s_0/k)_2\| ≤ 1`. The manuscript instead fixes ray classes; G5 confirms that `(−2/k)_2` is a class function mod 8. | yes |
| Orientation | family index inner | family index outer | yes. Since `n' ≡ 1 (3)`, `(n'/k)_2 = ψ_k(n') = ψ_{n'}(k) C([k],[n'])`. Fix `[k]` and `[n']` and apply Thm 1.1 with `𝔞 = k`, `𝔟 = n'`. This costs a factor `≤ \|G\|²`; equivalently, use GL Lemma 4.5, `B_1(M,N) ≤ \|G\| B_1(N,M)`. |
| Units | not present (ideals) | rows and columns are primary generators, in bijection with ideals prime to 3; on primary arguments `κ_λ = 1` | yes |
| Smoothing | none (sharp cutoffs) | none in eq:Q. In the use, the `k_0`-dependent weight `V_*^♯(…/N(k_0)²)` is removed first by lem:smooth: see the next row and §1.4. | yes |
| Ranges | any `M, N ≥ 1` | `ℋ_0 ≥ 1` (line 1946); dyadic `U ≥ 1`, unbounded; `N(n) ≍ U` gives `N = CU` with a fixed `C` | yes |
| Bound | `(MN)^ε(M+N)` | `(ℋU)^ε(ℋ+U)`; not the BGL shape `M+N+(MN)^{2/3}` | yes |
| Uniformity | constant depends on `k, 𝔠, ε` (and on `\|G\|`, which is fixed once `𝔠` is) | `≪_{S,ε}`. In the use, the coefficients vary with `b, s, m, ι, t, g`; GL is uniform over all coefficient sequences. The row restrictions `(k_0,g) = 1` and the fixed ray class (modulo a fixed ideal supported on `S`, by lem:reflection-uniformity) only shrink a sum of nonnegative terms. | yes |

### 1.4 The use at 2097–2187, including the separation step R3 left open

R3 (gap (i)) did not read lines 2112–2141. I read them against lem:smooth (3491–3556):
* The weight `V(x)V_*^♯(Rx)` with `x = N(n)/U` and `R = 3^m U N(b)³ℋ_0²/(Y N(k_0)²)` has the
  form `K_R` (3528), with `d = 1` and `F = V_*^♯`.
* `‖V_*^♯‖_{A,q} < ∞` is exactly eq:theta-weight-decay. It bounds `(x∂_x)^j V_*^♯` by
  `min(x^{1/4}, x^{−A})`.
* So `|c_{b,k_0}(s)| ≪ (1+R)^{−A}(1+|s|)^{−2}`. Since `N(b) ≥ B` and `N(k_0) ≤ ℋ_0`, we have
  `R ≥ z_* = 3^m U B³/Y`. This gives the `k_0`-free majorant in eq:theta-separated-columns.
* `G_{b,s}(k_0)` has coefficients independent of `k_0`. Hence lem:recombine (one index) gives
  `Σ_{k_0} |F_b(k_0)|² ≤ (∫w)² sup_s Σ_{k_0} |G_{b,s}(k_0)|²`.
* The cube variable `b` stays outside the large sieve. Cauchy–Schwarz in `b` uses only
  `|χ_{k_0}(b)³| ≤ 1` and `Σ_{B≤N(b)<2B} N(b)^{−1} ≪ 1`, so the non-squarefree part of the dual
  index never enters GL.
* `Σ_{N(n)≍U} |β(n)|² ≪ a²` holds.
* `U ≤ 81 Y z_*` (because `m ≥ −4` and `B ≥ 1`), and the two dyadic sums at 2157–2161 are
  correct.

Non-squarefree rows are reduced to squarefree ones through `k = u_0 s v²` and
`T(X; u_0sv², f) = T(X; u_0s, fv²)` (2190–2196), which is correct since `8 ≡ 2 (mod 6)` (line 2192). The unit
`u_0` and the part `t` of `s` meeting `gS` go into the fixed factor `Ψ_0`. So GL is only ever
applied with squarefree rows `k_0` coprime to `S`, as it requires.

### 1.5 How GL's proof uses the hypotheses

I read GL §§3–7 to see whether the proof needs more than Definition 1:
* Rows (`𝔞`) range over `I(𝔠)` throughout (§6.1 sums over `𝔞 ∈ I(𝔰)`, `𝔰 = rad 𝔠`). Our
  `k_0` are coprime to `S`.
* Property (3) is used in §6.1, "the conductor of `χ_{𝔟_1}χ_{𝔟_2}` is precisely `𝔟_1𝔟_2`", for
  Poisson summation (Cor. 6.1). This uses the root number `ε(χ) = 1` for primitive quadratic
  Hecke characters, a classical fact that GL state. Our products `(·/αβ)_2` are such characters.
* Property (2) is used in Lemma 4.5 (duality, factor `|G|`) and in §5. We have it with a fixed
  finite `G`.
* Lemma 4.2 needs `χ_{𝔟_1}χ̄_{𝔟_2}` nonprincipal for `𝔟_1 ≠ 𝔟_2`. For `ψ`, the restriction to
  ideals prime to `𝔟_1𝔟_2λ` is `(·/𝔟_1𝔟_2𝔤^{−2})_2`, with `𝔤 = (𝔟_1, 𝔟_2)`. This is nontrivial
  unless `𝔟_1 = 𝔟_2`.
* GL's Remark 4 notes that the bound fails without the squarefree restriction. The manuscript
  respects it in both variables (§1.3, §1.4).

GL's Theorem 1.1 therefore applies to the manuscript's family and coefficients. GL's estimates
themselves (Thms 4.1, 4.3, Lemmas 4.2, 4.4, 5.1, 7.1–7.3, Prop. 5.2) were read for structure only and not re-derived. This
is an imported, refereed theorem.

**Editorial points (not load-bearing).**
* The proof could cite Thm 1.1 together with GL Lemma 4.5 (or reciprocity) for the transposition.
* `|(s_0/k)_2| ≤ 1` disposes of the `S`-part of `n` without ray classes.
* "[GL, §2]" is an example of a Hecke family, not a list of hypotheses.
* Cor. 1.2 (line 412) is not needed. The sextic symbol `(·/k)_6` is not trivial on units
  (`(ω/k)_6 = ω^{(N(k)−1)/6}`), so the twisted quadratic family above, not a sextic one, is the
  right object.

### 1.6 Finite checks (oct5_residual_checks.py, part G, EXACT unless stated)

All squarefree primary `k` prime to 6 with `N(k) ≤ 2000`: 568 rows built from 302 primary
primes. The quadratic symbol is computed by Euler's criterion in `Z[ω]/(π)`.

* **G1.** `ψ_k(−1) = ψ_k(ω) = 1` for all 568 rows. Control: `(−1/k)_2 = −1` for 288 rows, so the
  `κ_λ` twist is necessary.
* **G2.** For 109 rows (`N(k) ≤ 400`), `ψ_k` is nontrivial on `{x ≡ 1 mod f/q}` for every prime
  `q | f = kλ^{e_k}`, so it is primitive with conductor `f`. Sampled periodicity mod `f`: 0
  failures.
* **G3.** `(α/β)_2(β/α)_2` takes both values ±1 over 17 741 coprime pairs with `N ≤ 700`, and is
  constant on each of the 144 observed classes mod 4. Control: it is **not** a function of the
  classes mod 2 (9 classes take both values).
* **G4.** `α ≡ β (mod 4)` implies `e_α = e_β`: 0 failures.
* **G5.** `(−2/k)_2` is constant on each of the 48 classes mod 8.
* **G6** (FLOAT, illustration only, not evidence). With `H = U ∈ {250, 500, 1000}`,
  `λ_max(AA*)/(H+U) = 0.397, 0.370, 0.390` for `A = [(n/k)_2]`.

## 2. The contour shift in app:fixed-ray (item 2)

**Claim (3395–3418, with 3424–3433).** The identity eq:theta-mellin-inversion
`T(X;Ψ) = (2πi)^{−1} ∫_{(σ_+)} V̂_*(s−½) 𝒯(s,Ψ) X^{s−½} ds`, valid for `σ_+ > 1`, may be moved to
`Re s = σ_- < 0`. There one inserts eq:theta-mellin-functional-equation and
eq:dual-cusp-mellin-series at `1−s`, interchanges sum and integral, puts `t = ½ − s`, and moves
each kernel to `Re t = 0`. The result is the exact dual sum eq:reflection with weight `V_*^♯`.
Write `G(s) = (3^{5/2}/4)(27/(2π)²)^s Γ(s+⅓)Γ(s+⅔)`, so that eq:ray-mellin reads `J = G·𝒯` for
`Re s > 1`.

**A. `J` is entire and bounded in every vertical strip.** Let `F(v) = ∂_z̄ Θ_Ψ(z,v)|_{z=0}`.
* *As v → ∞.* The Fourier series eq:general-twisted-theta-definition has frequencies
  `|ℓ| ≥ 3^{−3/2}` and polynomially bounded coefficients. The bound
  `K_{1/3}(y) ≪ y^{−1/2}e^{−y}` for `y ≥ 2` then gives `F(v) ≪ e^{−βv}` for `v ≥ 1`.
  Differentiating termwise is justified by locally uniform convergence.
* *As v → 0.* `Θ_Ψ` is a finite sum of translates (eq:theta-factorized-shifts). Each translate
  is rewritten by eq:theta-cusp-automorphy. By eq:theta-cusp-coordinates, at `z = 0` we have
  `∂z'/∂z̄ = −(cv)^{−2}` and `∂z̄'/∂z̄ = ∂v'/∂z̄ = 0`. (I re-derived these: `z̄'` depends on `z`
  only through `z/(c̄²(v²+|z|²))`, and `v'` only through `|z|²`.) So the operator is
  `−(cv)^{−2}∂_{z'}`, which annihilates the constant mode `(3^{5/2}/2)1_{σ=0}v'^{2/3}`. The other
  modes have `|ℓ| ≥ 1/9` and `v' = 1/(N(c)v)`, so `F(v) ≪ v^{−C}e^{−β'/v}` for `v ≤ 1`.
* *Consequence.* `J(s) = ∫_0^∞ F(v)v^{2s−1}dv` converges absolutely and locally uniformly for all
  `s`, so `J` is entire. Moreover `|J(σ+iT)| ≤ ∫|F|v^{2σ−1}dv`, which does not depend on `T`, so
  `J` is bounded on every vertical strip.

The same holds for each single translate, because `∂_z̄` also kills its constant mode at `∞`. So
eq:theta-mellin-functional-equation, obtained by substituting `v ↦ 1/(N(c)v)` in each translate,
is an identity of entire functions; I re-derived the factor
`−κ̄ ᾱ(c)² N(c)^{1−2s}` from `c^{−2}N(c)^{2−2s}`.

**B. `𝒯` is entire, of order 1.** `𝒯 = J/G`, and `1/Γ` is entire. Stirling gives
`1/|G(σ+iT)| ≍ e^{π|T|}|T|^{−2σ}` for `|T| ≥ 1` (C1), so `|𝒯| ≪ e^{π|T|}(1+|T|)^{C}` on any strip.
The manuscript's "splitting at `v = 1` gives finite order" is correct; the split is not even
needed.

**C. The boundary lines.**
* *Right* (`Re s = σ_+ > 1`). `|𝒯| = O(1)`, since `Σ_n N(n)^{−σ}` and `Σ_b N(b)^{½−3σ}`
  converge.
* *Left* (`Re s = σ_- < 0`). eq:theta-mellin-functional-equation together with
  eq:dual-cusp-mellin-series at `w = 1−s`, where `Re w > 1`, gives
  `𝒯(s) = (elementary factors)·Γ(4/3−s)Γ(5/3−s)/(Γ(1/3+s)Γ(2/3+s))·Σ_h c'_h N(c_h)^{1−2s} D_h(1−s)`.
  Here `D_h(w) = Σ_ℓ d(ℓ)α(ℓ)ĕ(…)N(ℓ)^{−w}`, and by eq:theta-coefficient-bound it is majorized
  by `27·6·Σ_{m≥−4} 3^{m/6−mσ} Σ_n N(n)^{−σ} Σ_b N(b)^{½−3σ}`. This converges exactly for
  `σ > 1`.
  * The gamma quotient is `≍ |T|^{2−4σ_-}` (C1: the ratio is 1 + O(|T|^{−1}) at `σ = −0.25` and
    `σ = −1.1`).
  * So `|𝒯(σ_-+iT)| ≪ (1+|T|)^{2−4σ_-}`. For `|T| ≤ 1`, continuity of the entire function `𝒯`
    covers any real poles of `Γ(1/3+s)Γ(2/3+s)` on the line.
  * eq:dual-cusp-mellin-series itself holds for `Re w > 1` by Tonelli: `K_{1/3} > 0`, and
    `Σ|d(ℓ)||ℓ|·|ℓ|^{−2Re w−1} < ∞`.

**D. Phragmén–Lindelöf.** `𝒯` is holomorphic on the closed strip `σ_- ≤ Re s ≤ σ_+`. It grows at
most like `e^{π|T|}`, far below the admissible `exp(e^{α|T|})` with `α < π/(σ_+−σ_-)`. With
polynomial bounds on both edges, PL gives `|𝒯(σ+iT)| ≪ (1+|T|)^{max(0,2−4σ_-)}`, uniformly in the
strip. I did not check the IK04 numbering (Thm 5.53, §5.A.4); the statement used is the classical
one.

**E. Horizontal segments.** `V̂_*` is entire. After `j` integrations by parts,
`|V̂_*(w)| ≪_{j,K} (1+|Im w|)^{−j}` for `Re w` in a compact set `K`. On
`[σ_-+iT, σ_++iT]` the integrand is therefore `≪ (1+|T|)^{A_0−j} X^{σ_+−½} → 0`, and Cauchy's
theorem moves the line to `σ_-`. The new integral converges absolutely.

**F. Inserting the dual series.** On `Re s = σ_-`, the sum `Σ_ℓ ∫ |…||ds|` is at most
`(Σ_ℓ|d(ℓ)|N(ℓ)^{σ_-−1})·∫(1+|T|)^{2−4σ_-}|V̂_*(σ_-−½+iT)|dT < ∞`, so sum and integral may be
interchanged (Fubini). With `t = ½−s` the line is `Re t = ½−σ_- > ½`, and the dual series is
`Σ d(ℓ)N(ℓ)^{−½−t}`. This converges absolutely exactly when `Re t > ½`, as the manuscript says
(3409–3411).

**G. The kernel shift (3426–3433, 3453–3458).** For fixed `ℓ`, the `t`-integrand is
`V̂_*(−t)·Γ(5/6+t)Γ(7/6+t)/(Γ(5/6−t)Γ(7/6−t))·Y_ℓ^{−t}`, with `Y_ℓ = (2π)^4N(ℓ)X/(27N(c)²)`.
I re-derived this composition (R3 check H also did). It is holomorphic for `Re t > −5/6`. The
gamma quotient is `≍ |Im t|^{4 Re t}` (C1), and `V̂_*` decays rapidly, so the line moves to
`Re t = 0` (giving `V_*^♯`) and to `Re t = −¼` (giving the `x^{1/4}` bound). eq:bessel-mellin
is stated for `Re s > 0`; it actually holds for `Re s > −⅓` (DLMF 10.43.19). This is
conservative and harmless.

**No poles, in summary.**
* The `s`-integrand is entire: this is A–B, and the reason is that the `∂_z̄` removes the
  Kubota–Patterson constant mode at every cusp. This confirms R3 §5.
* The `t`-integrand has its first pole at `t = −5/6`, to the left of every line used.

**Uniformity.** The shift yields an exact identity. The PL and Stirling constants depend on `Ψ`,
but they enter no estimate, so the growth of `𝒫` costs nothing at this step. The uniformity
claims are carried by eq:theta-weight-decay and lem:reflection-uniformity, which R3 checked.

**Numerical checks (FLOAT).**
* **C1.** The ratios of `|left-line quotient|/|T|^{2−4σ}`, `|kernel quotient|/|u|^{4c}` and
  `|1/G|/(e^{π|T|}|T|^{−2σ}/2π)` are all `1 + O(|T|^{−1})`; at `|T| = 10^4` they lie within
  `10^{−7}` of 1.
* **C2.** `V_*^♯(x)` was computed by quadrature on several vertical lines, at `x = 10², 10⁴, 10⁶`,
  for two weights:
  * the log-Gaussian `V_*(y) = e^{−(log y)²}`, which has a closed-form `V̂_*`, on the lines
    `Re t ∈ {0.75, 2, −0.25}`;
  * the manuscript-type compactly supported `√y W(y)`, `W = e^{−1/((y−1)(2−y))}`, on the lines
    `Re t ∈ {0.5, −0.25}`.

  On every line the value agrees with the one on `Re t = 0` to `≤ 8e−15` absolutely; the
  compact-bump values are `−4.7e−3`, `9.2e−5` and `−2.3e−6`. *Control:* on `Re t = −1` the
  difference equals the residue at `t = −5/6`, which is `V̂_*(5/6)Γ(1/3)/(Γ(2)Γ(5/3))Y^{5/6}`, to
  relative `≤ 10^{−12}`, while the uncorrected difference is of the size of that residue. So the
  test does detect a crossed pole.

## 3. R1's minor points (item 3)

**N1 (lines 752–757). Harmless.** For `ν` trivial on the ideals prime to `S`, `L_K^S(s,ν)` has a
simple pole at `s = 1`. The identity `L_K^S·𝓜_W = Ŵ` therefore holds on the connected domain
`{Re s > 11/12} ∖ {1}`, and only as an identity of meromorphic functions at `s = 1`, where it
forces `𝓜_W(1) = 0`. A zero `ϱ` of `L_K` is not the pole, so `ϱ ≠ 1`. Evaluating at `ϱ` is
legitimate and gives `0 = Ŵ(ϱ) > 0`.

*Repair (one line):* "By Hecke's continuation and the identity theorem, `L_K^S(s,ν)𝓜_W(s) = Ŵ(s)`
on `Re s > 11/12`, `s ≠ 1`; since `ϱ` is a zero of `L_K^S`, it is not its pole at `s = 1`."

**N2 (lines 1193–1204). Harmless; less is needed than R1 said.**
* With `t = a/(x_1x_2)`, the chain rule gives `x_i∂_{x_i}[Φ̂(a/(x_1x_2))] = −(t∂_tΦ̂)(t)`. On the
  box `[a_0/4, b_0]²` every `∂_x^α` is a combination of `(x∂_x)^β`, `|β| ≤ |α|`, with bounded
  coefficients. So
  `sup_{b,f,k}‖𝒦_{b,f,k}‖_{C^q} ≪_q ‖W‖²_{C^q(I)}·max_{j≤q} sup_{0<t≤16C_{I,Φ}/a_0²} |(t∂_t)^jΦ̂(t)|`,
  uniformly in `a ∈ (0, C_{I,Φ}]`. Only `(t∂_t)`-derivatives near `0` are used, not smoothness of
  `Φ̂` at `0`. This is the same `‖F‖_{A,q}` norm as in app:weights (3535).
* Those derivatives are bounded. `z ↦ Φ(|z|²)` is a radial Schwartz function, so its Fourier
  transform `w ↦ Φ̂(|w|²)` is a radial Schwartz function. Its restriction to a ray, `r ↦ Φ̂(r²)`,
  is smooth on `[0,∞)`, and `t∂_t = ½ r∂_r`. Whitney's theorem on even functions even gives
  `Φ̂ ∈ C^∞([0,∞))`.
* For the explicit choice at line 1473 (`Φ` a rescaled square of a radial Schwartz function with
  compactly supported Fourier transform), `Φ̂` is a convolution of compactly supported smooth
  radial functions.
* The same remark covers the kernel `𝒦_h` at 2316–2323 (R2 scope).

*Repair (one line):* "Here `Φ̂ ∈ C^∞([0,∞))`, being the profile of the Fourier transform of the
radial Schwartz function `Φ(|z|²)`; in fact only the bounds on `(t∂_t)^jΦ̂` near `t = 0` are
used, since `x_i∂_{x_i}Φ̂(a/(x_1x_2)) = −(t∂_tΦ̂)(a/(x_1x_2))`."

## 4. What this does and does not establish

* With these items closed, the bounded reviews R1–R3 plus this note have now read every proof line
  of the manuscript and found no wrong step. The external theorems used are GL Thm 1.1 (hypotheses
  verified here), the Dunn–Radziwiłł cusp expansions (R3), and standard classical theorems.
* This is not an independent exact-SHA review in the sense of [AGENTS.md](../../../../AGENTS.md),
  and it is not an integration. The 11/12 statement remains an external, unreviewed claim.
* Nothing here concerns the critical line or RH.
