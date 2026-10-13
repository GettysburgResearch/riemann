# O1: the cubic row family (c = 2/3) and the reflection without sextic theta coefficients

```text
Status: PROPOSED (Lemmas 1-3, Props 4-5: elementary proofs written here, not reviewed; Lemma 2 imports
  the Kubota/CG10 functional equation) + HEURISTIC (the pipeline bookkeeping of Sections 3-6, the
  "isometry" model of a reflection) + CONDITIONAL (Section 7: sigma = 5/6, 7/8, 8/9 under named
  large-sieve / summation-formula inputs) + EMPIRICAL (Section 6 and the identity checks; floating
  point, finite). Round 2 (Section 8A): (S6) is LOCALLY CONSISTENT at every unramified prime
  (PROPOSED; imports the KP/Hoffstein Hecke relations). No zero-free region is proved. RH remains unproved. Nothing below beats 11/12
  unconditionally; the Oct 5 11/12 claim itself is an external, unreviewed import.
Scope: the cubic Kummer family A_u(D) = sum_n mu(n) nu(n) chi_n(u)^2 W(N n/D) over K = Q(omega),
  rows N u <= H = D^rho (leverage c = 2/3, boundary 1/2 + rho/3); its dual after Poisson in u and
  the Moebius absorption mu gamma_2 = chi(-1) alpha G gamma_{-1} (LEVERAGE_FAMILIES S6). Whether the
  reflection + mean-square step can be done with the 6-fold Eisenstein series (Kubota), with Weyl
  group multiple Dirichlet series, or with Rankin-Selberg, without knowing sextic theta coefficients.
  Test bed: the quartic family over Q(i) (c = 3/4).
Exact sources or dependencies:
  Repository: RUNG_STRENGTH.md (ladder law, rho = 1 wall), LEVERAGE_FAMILIES.md (S1-S7, sec. 3.2,
  sec. 5), SEXTIC_THETA_S6.md (status of (S6); sextic Kubota residue measurement), A2_LITERATURE.md
  (CG10 Thm 6.1 as quoted there: Z*(s; m, Psi) = |m_i|^{1-s_i} Z*(sigma_i s; m, sigma_i Psi), "m is
  preserved"; HB00 cubic large sieve; BBCFH06 A2 data), reviews/OCT5_R3_THETA_REFLECTION.md (the
  index-type exponent B_{p,j} = chi_p^{-j-2}; Sec. 5: angular twist kills the Kubota pole),
  a2/eis.py (imported, not modified). Oct 5 manuscript (external, unreviewed):
  scratchpad paper2.tex lines 301-660 (Steps 3-5) read.
  External, abstract only: de Faveri, Dunn, Hoffstein, arXiv:2607.07911 "Non-orthogonality of the
  cubic and quartic large sieves via Rankin-Selberg" (abs page fetched 2026-10-13 from
  export.arxiv.org, sha256 b2923dd49e63efda...; the paper body and its conjecture were NOT read).
  Kubota 1969, Patterson 1977, Kazhdan-Patterson 1984 (Hecke relations tau(m p^j) =
  G_{j+1} tau(m p^{n-2-j})): known only through the repository notes above.
  Not consulted: draft PR 930 BESSEL_CHANNELS_AND_LEAKAGE.md (pointer received, no time).
What was actually run (Python 3.13 + numpy + sympy, single process, nice 5):
  python3 ledger.py                          -> results/ledger.txt (exact rationals, asserts pass)
  python3 kubota_mobius_check.py 250 OUT     -> results/kubota_mobius_check.json (about 2 min)
  python3 local_hecke_check.py OUT           -> results/local_hecke_check.json (H3, H6; under 1 min)
  python3 dual_ms.py X H1,...,Hk OUT         for X in {4000, 20000, 50000, 100000}
                                             -> results/dual_ms_X*.json/.log (1.5 s, 24 s, 86 s, 440 s)
Smallest remaining gap: (LS*_kappa) of Section 7: a cubic large sieve for the ONE coefficient
  sequence b_n = mu(n) gamma_2(n) xi(n) (= Hecke x ray x sextic Gauss sum), with excess (calH X)^kappa,
  kappa < 4/7 (beats 11/12), kappa = 8/15 (7/8), kappa = 1/2 (5/6). Equivalently, at the structural
  level, a summation formula of row-conductor N(h)^2 for n -> mu(n) gamma_2(n) xi(n) twisted by cubic
  characters of conductor h (gives 8/9 even with the BGL/Heath-Brown exponent; 5/6 if the post-twist
  is quadratic). The 6-fold Eisenstein series supplies conductor N(h)^4 only, which gives sigma = 1.
```

RH remains unproved. "Imported" means taken from an external source or from a repository note
without independent proof here.

## 0. Verdict

1. **The Eisenstein (Kubota) route does not move the exponent, and the reason is exact.** For the
   cubic family, the absorbed dual sum is *exactly* a coefficient of the 6-fold Kubota series, with
   numerator `−h⁴` (Lemma 1, checked at 519 cases, K3). The Kubota functional equation preserves the
   numerator class (Lemma 2, imported FE). So the cubic row twist survives reflection unchanged, and
   the row conductor is `N(h)⁴`, not `N(h)²`. Every Kubota + large-sieve pipeline gives
   **σ = 1** for the cubic family. This holds with the Heath-Brown/BGL exponent and also with an
   optimal sieve applied after the reflection (ledger rows 2-3).
2. **A quadratic post-twist is unreachable by Eisenstein moves.** The modulus-side moves act on
   the numerator class `j` (mod 6) as `j ↦ j` (functional equation) and `j ↦ 4 − j` (the
   `c ≡ 0 mod p` terms, Lemma 3). The cubic family sits at `j = 4`, whose orbit is `{4, 0}`. The
   quadratic class `j = 3` has the other parity. An index-type (theta) reflection maps the twist
   exponent `t ↦ −t − m_θ`, with `m_θ` the multiplier exponent in sextic units; this changes
   parity only when `m_θ` is odd. The cubic theta has `m_θ = 2` (R3), and Oct 5 starts from an odd
   twist. For the even (cubic) twist one needs a 6-fold theta with single-Gauss-sum coefficients,
   which is (S6).
3. **WMDS (mechanism b): no finite Weyl group.** For the (row, column) double series of the dual,
   the Cartan product is `a·b ≥ 4` for every free unimodular Gauss-sum weight in the row
   (Prop. 4). The group is affine `Ã₁` or worse. The A2 / B2 / G2 cases need `a·b ≤ 3`. The
   mean-square series in three variables has `det = 4a(2 − a)`. It is finite only when the column
   conductor exponent is `a = 1`; here `a = 4`, so it is indefinite.
4. **Rankin–Selberg over the Fourier index (mechanism c, and coordinator Q3) loses `𝓗³`.** It
   gives σ = 13/12. Rankin–Selberg is useful only on the dual side of an index-type reflection, and
   that reflection needs (S6).
5. **The only known obstruction to an optimal sieve is harmless here (Prop. 5).** That obstruction
   is the Gauss-sum (Kubota-pole) bias of dFDH/DR. Even if a 6-fold pole were present in the dual
   rows, it would contribute `≪ X^{1/6}𝓗^{1/3} ≤ X` to the dual mean square.
   **EMPIRICAL:** the absorbed coefficients `μγ₂` show no `(HX)^{2/3}` excess on a grid with
   `X ≤ 10⁵` columns-norm and `H ≤ 2X`. Their mean square sits at the diagonal, `0.85–0.97 ×
   rows·‖b‖²`, like random phases. The control `γ₂` (no μ) shows the predicted excess
   `≈ 0.06 (X²/H)^{1/3}`, with constant 0.056–0.065 stable over `X = 4·10³ … 10⁵`.
6. **Exponent ledger (exact; `ledger.py`).** σ(κ) = (9κ − 2)/(6κ) for the direct pipeline with
   large-sieve excess `(𝓗X)^κ`. That gives 5/6 at κ = 1/2, 7/8 at κ = 8/15, 11/12 at κ = 4/7, and
   1 at κ = 2/3. **Coordinator benchmark corrected:** a conductor-`N(h)²` reflection that keeps a
   cubic twist, followed by BGL, needs `𝓗 ≤ X^{5/6}` (not `X^{2/3}`). That is ρ ≥ 7/6 and
   **σ = 8/9 < 11/12**. It is hypothetical: no such reflection is known, and Kubota gives
   conductor `N(h)⁴`, hence σ = 1.
7. **Quartic test bed:** the mechanism does **not** reproduce 7/8. The 4-fold Kubota numerator is
   `h³` (conductor `N(h)³`, Lemma 1 general form), which gives σ = 65/64 with BGL. 7/8 needs a GL(2)
   quartic theta with single-Gauss-sum coefficients, which the Eckhardt–Patterson shape contradicts.

8. **Round 2 (§8A): (S6) is LOCALLY CONSISTENT (PROPOSED).**
   * The Kazhdan–Patterson/Hoffstein relations reproduce the known cases: n = 3 determined
     (Patterson) and n = 4 free with a quadratic support condition (Suzuki).
   * For n = 6 they leave `τ(p)` free at each `p`.
   * (S6) is equivalent to `τ(mp³)/τ(m) = μ(p)·c(η/α)(p)χ_p(16)G(p)·ε`. What remains is global:
     (S6-glob), contradicted by [BH]'s numerics for one theta and open for the rest.

Best result: no unconditional improvement. The sharpest new statements are the exact obstruction
(conductor exponent 4, parity of the numerator class) and the reduction of 5/6 / 7/8 / 8/9 to the
named inputs of §7, together with finite evidence that LS*₁/₂ is true for these coefficients.

## 1. The absorbed dual is a 6-fold Kubota coefficient

Notation: `χ_n = (·/n)₆`; `γ_j(r, n) = N(n)^{−1/2} Σ_{x mod n} χ_n(x)^j e(rx/n)`; `γ_j(n) = γ_j(1, n)`;
`α(n) = n/|n|`; `G(n) = conj χ_n(4) γ₃(n)`; all `n` squarefree primary, prime to 6.

**Poisson.** For `A_u = Σ μ(n)ν(n)χ_n(u)² W`, Poisson in `u` gives the Gauss sum of
`χ_{n₁}²·conj χ_{n₂}²` at frequency `h`. By CRT it equals
`χ_{n₁}(n₂)² conj χ_{n₂}(n₁)² · g₂(n₁) g₋₂(n₂) · conj χ_{n₁}(h)² χ_{n₂}(h)²`. The cross factor is `1`
by cubic reciprocity (`χ²` is the cubic symbol and `n₁, n₂` are primary). So, up to the separation of
the weights (as in Oct 5 Lemma lem:poisson), the dual is
`Σ_{N h ≤ 𝓗} |B_h|²` with `𝓗 = D²/H` and

    B_h(X) = Σ_n μ(n) ν(n) γ₂(n) conj χ_n(h)² U(N n/X).

**Lemma 1 (numerator class; PROPOSED, proof here).** For `(n, h) = 1`,

    μ(n) γ₂(n) conj χ_n(h)² = α(n) G(n) · γ₋₁(−h⁴, n).

*Proof.* S6 of LEVERAGE_FAMILIES gives `μγ₂ = χ(−1)αGγ₋₁`. Substituting `x ↦ x·y⁻¹` gives
`γ₋₁(y, n) = χ_n(y)γ₋₁(n)`, and `χ_n(−h⁴) = χ_n(−1)χ_n(h)⁴ = χ_n(−1) conj χ_n(h)²`. ∎

So `B_h` is the smoothed coefficient sum of the 6-fold Kubota series, for the cover with inverse
cocycle (Gauss sums of `conj χ`), at **numerator `−h⁴`**, twisted by `α` (an angular K-type) and the
ray class factor `Gν`. It is restricted to `(n, h) = 1`, and that restriction is automatic.
Check K3: 519 `(n, h)` cases, `N n ≤ 1500`, deviation ≤ 5.9e-15.

*General form.* Take an `m`-row family, absorbed into an `n`-fold Gauss sum `γ_{±1}` (the angle
condition `e ≡ a + n/2`, LEVERAGE §1.3). Its numerator class is `r ≡ h^{1+n/2}` mod `n`-th
powers. That is `h⁴` for `n = 6` (cubic rows) and `h³` for `n = 4` (quartic rows over `Q(i)`).

**What the 6-fold Eisenstein series controls "for free" (coordinator note (1), verified).**
* *At primes:* `γ₋₁(p) = −χ_p(16) G(p) γ₂(p)/α(p)`. This is S6 combined with
  `G² = conj χ(16) χ(−1)`. Check K1: 52 primes, deviation 1.4e-15; the sign-flipped control fails by 2.
* *At all squarefree `n`:* `γ₁(n) = μ(n) α(n) G(n) γ₄(n)`. Check K2: 52 primes and 118
  composites with 2–3 factors, deviation 5.4e-15.

Since `g₆(1, c) = 0` for non-squarefree `c`, the 6-fold Kubota series at numerator 1 is exactly

    Σ_c γ₁(c) N(c)^{−s} = Σ_c^♭ μ(c) α(c) G(c) conj γ₂(c) N(c)^{−s},

and at numerator `k` (with `(c, k) = 1`) it is the same sum twisted by `conj χ_c(k)`.

The Eisenstein series therefore gives, unconditionally, meromorphic continuation and a functional
equation for **Möbius-weighted cubic Gauss sums times the Hecke character α**. (Meromorphy and the
functional equation are imported from Kubota/Patterson.) It also gives a pole at `s = 7/12` with
residue `∝ τ₆(1)`. The residue was measured as ≈ 0.22 in SEXTIC_THETA_S6.md §5 (EMPIRICAL). Hence
`Σ_{N c ≤ X} μ(c)α(c)G(c)conj γ₂(c) ≈ C X^{7/12}` (CONDITIONAL on `τ₆(1) ≠ 0` for this representative
set; supported only by that finite measurement): a Patterson-type bias created by μ.

Without μ, the α-twisted cubic series has no pole (R3 §5). This is the precise sense in which the
6-fold cover "absorbs" μ. It does not help ζ, because the oscillating Gauss sum stays.

## 2. Mechanism (a): Kubota's Eisenstein series on the 6-fold cover

**Lemma 2 (twist preservation; IMPORTED functional equation + PROPOSED reading).**
* The `r`-th Fourier coefficient of the 6-fold Kubota Eisenstein series is the Kubota series
  `ψ(r, s) = Σ_c g̃(r, c) N(c)^{−s}`.
* The functional equation `E(w, s) ↔ E(w, 1 − s)` is an identity of automorphic forms in `w`, so
  it equates Fourier coefficients **at the same index `r`**. It gives
  `ψ(r, s) = N(r)^{1/2−s} Σ_η Φ_η(s) ψ_η(r, 1 − s)`.
  * `η` runs over finitely many S-classes.
  * This is CG10 Thm 6.1 as quoted in A2_LITERATURE §1: "m is preserved", factor `|m|^{1−s}`.
* Consequences:
  * the row twist `conj χ_c(r)` survives with the same order;
  * the row conductor is `N(r)`;
  * for the cubic family `r = −h⁴`, so the row conductor is **`N(h)⁴`** and the dual length is
    `X′ = N(h)⁴/X`.

**Isometry bookkeeping (HEURISTIC).** Write `Σ_n g̃(r, n)U(N n/X) ≈ (X/N(r)^{1/2}) Σ_{N n′ ≲ N(r)/X}
g̃_η(r, n′)Ṽ`. Then for `E := X^{−1} Σ_h |B_h|²` a row-blind sieve with excess exponent κ gives

    E ≲ 𝓗 + X′ + (𝓗X′)^κ,   X′ = 𝓗⁴/X.

Requiring `E ≲ X` forces `𝓗 ≤ X^{1/2}` for κ = 2/3, and also for κ = 1/2 when the sieve is used only
after reflection. That is ρ ≥ 3/2 and **σ = 1/2 + (2/3)(3/2)/2 = 1**. When `𝓗 > X^{1/2}`, the
reflected sum is *longer* than the original (`X′ > X`), so reflecting never helps. The BGL loss in
the ladder is therefore 1 − 5/6 = 1/6 of boundary, and Kubota recovers none of it.

The Kubota functional equation does give a pointwise bound. Smoothed, with no main term (angular
twist), shifting to `Re s = −ε` gives `|B_h| ≪ N(h)^{2+ε}` (PROPOSED, given Lemma 2 and polynomial
growth in `|t|`). That is nontrivial only for
`N h < X^{1/2}`, which is again the same range.

**Lemma 3 (local class move; PROPOSED, proof here).** Let `p ∤ m`, `0 ≤ j ≤ n − 2`, and let
`ψ^{(p)}` denote the Kubota series restricted to `p ∤ c`. Then

    ψ(m p^j, s) = ψ^{(p)}(m p^j, s) + g̃(m p^j, p^{j+1}) N(p)^{−(j+1)s} ψ^{(p),ε}(m p^{n−2−j}, s),

where `ε` is a ray-class twist.

*Proof.* For `p ∤ m` and `j < n`, `g(m p^j, p^k) ≠ 0` only for `k = 0` or `k = j + 1`. For coprime
primary moduli, `g(r, c₁c₂) = χ_{c₁}(c₂)χ_{c₂}(c₁) g(r, c₁)g(r, c₂)`; this is CRT with `x = c₂x₁ + c₁x₂`.
Reciprocity turns `χ_p(c′)^{j+1}χ_{c′}(p)^{j+1}` into `ε·χ_{c′}(p)^{2j+2}`. Then
`g(mp^j, c′) = conj χ_{c′}(p)^j g(m, c′)` leaves `conj χ_{c′}(p)^{j−2j−2}`, i.e. the class
`p^{−j−2} ≡ p^{n−2−j}`. ∎

So the modulus-side moves act on the class `j` by `j ↦ j` and `j ↦ n − 2 − j`. Both preserve
`j mod 2` when `n` is even. For the cubic family, `j = 4 ↦ 0`: the `c ≡ 0 mod p` terms carry *no*
twist (Ramanujan-type), never the quadratic class `j = 3`.

**What a quadratic twist would require (answer to (a)).** The class must change parity. On the
index side, a theta reflection maps the row twist exponent `j ↦ −j − κ_mult`, where `κ_mult` is the
multiplier exponent (R3: `κ_mult = 2` for the cubic theta). For the cubic family with a 6-fold theta
of multiplier exponent −1 (LEVERAGE §3.2: the multiplier angle matches the coefficient angle), the
twist `χ^{−2}` goes to `χ³`, which is quadratic. That needs `γ₋₁(n)` to be the index-`n`
coefficient of an automorphic form, i.e. (S6), which is contradicted for the one theta computed in
SEXTIC_THETA_S6. **No Eisenstein-series identity can substitute for it**: Lemmas 2–3 are the only
moves available on the modulus side, and they preserve parity.

## 3. Mechanism (b): Weyl group multiple Dirichlet series

**Prop. 4 (PROPOSED, elementary).** Consider the double series
`Z(s, w) = Σ_{h, n} ω(h) a(n) γ₋₁(−h⁴, n) N(n)^{−s} N(h)^{−w}`, with `ω(h)` any unimodular
Gauss-sum weight `γ_j(1, h)` (free, since `|γ_j(1, h)| = 1` for squarefree `h` and
`Σ_h |B_h|² = Σ_h |ω(h)B_h|²`). Then:

* The `n`-functional equation has shift `w ↦ w + 4(s − 1/2)`, i.e. `a = 4` (Lemma 2).
* The `h`-functional equation has shift `s ↦ s + b(w − 1/2)`, where `b` is the conductor exponent
  of `h ↦ ω(h)·χ_n(h)⁴`. By sextic reciprocity `χ_n(h)⁴ = ε·χ_h(n)⁴`, with `ε` ray class. Write
  `ω(h)χ_h(n)⁴ = γ_j(r, h)` and solve for the numerator `r`:
  * `j = 0` (no Gauss sum): `L(w, χ_·(n)⁴)`, a cubic character of conductor `n`, `b = 1`;
  * `j = 2`: cubic Kubota series with numerator `r ≡ n` (mod cubes), `b = 1`;
  * `j = 4`: `r ≡ n²` (mod cubes), `b = 2`;
  * `j = 1`: `r ≡ n²`, `b = 2`;
  * `j = −1`: `r ≡ n⁴`, `b = 4`;
  * `j = 3`: impossible, since a quadratic Gauss sum cannot carry a cubic twist.
* Hence `a·b ∈ {4, 8, 16}`.

The two reflections generate a finite group only when `a·b ≤ 3` (A1×A1, A2, B2, G2), so here the
group is affine `Ã₁` or larger. No finite-type WMDS contains the dual, and the expected behaviour is a
natural boundary, as for the affine moment series. ∎

*What would be needed:* `a ≤ 3`, i.e. a numerator class of conductor ≤ `N(h)³` in the column
Kubota series. Under absorption the class is `h^{1+n/2}` (Lemma 1), so `a = 1 + n/2 ≥ 4` for every
`n ≥ 6`. The quartic case has `a = 3`, `b = 1`, i.e. Cartan product 3 (G2-type); see §5.

**The mean square is a three-variable series, and it is of finite type only for `a = 1` (PROPOSED,
elementary).** Take `Σ_h |B_h|² ↔ Σ_{n₁,n₂,h} a(n₁) conj a(n₂) γ(·, n₁) conj γ(·, n₂) N(n₁)^{−s₁}
N(n₂)^{−s₂} N(h)^{−w}`. The structure of its functional equations is as follows:
* each `n_i`-equation shifts `w` by `a(s_i − 1/2)`;
* the `h`-equation (an L-function of conductor `N(n₁n₂)`) shifts both `s_i` by `w − 1/2`;
* `n₁` and `n₂` do not interact.

The generalized Cartan matrix is `[[2,0,−a],[0,2,−a],[−1,−1,2]]`, symmetrized by `diag(1,1,a)`, with
`det = 4a(2 − a)`. It is finite (`A₃`, the DGH/BBF-type case) iff `a = 1`, affine for `a = 2`, and
indefinite for `a ≥ 3`.
* The cubic family (`a = 4`) and the quartic family (`a = 3`) are both indefinite.
* Even a finite two-variable WMDS would control only *linear* statistics `Σ_h B_h V(N h/𝓗)`, not
  `Σ_h |B_h|²`.

The index↔modulus duality of the A2 series (BBCFH06, σ₁σ₂σ₁) exchanges *Gauss-sum-weighted*
variables. Our row `h` carries no intrinsic Gauss sum, and inserting one costs `b ≥ 1` (above), so
the duality has nothing to act on.

## 4. Mechanism (c): mean-value substitutes (coordinator Q3)

* **Rankin–Selberg over the Fourier index.** By Lemma 1, `B_h` is the index-`h⁴` coefficient of an
  incomplete 6-fold Eisenstein series (angular K-type) at scale X. Rankin–Selberg controls
  `Σ_{N k ≤ K} |coef(k)|² ≪ K^{1+ε}` over **all** indices. The indices `k = h⁴` with `N h ≤ 𝓗`
  are a sparse subset of `N k ≤ 𝓗⁴`. Positivity gives `E ≲ 𝓗⁴`, so `𝓗 ≤ X^{1/4}`, ρ ≥ 7/4, and
  **σ = 13/12** (ledger). No sparse-subsequence Rankin–Selberg is known.
  * Lemma 3 shows `ψ^{(h)}(h⁴)` differs from the index-`h⁴` coefficient by a term of relative size
    `N(h)^{−1/2}` on `Re s = 1/2`. That does not change the count.
* **Rankin–Selberg on dual theta coefficients** (Kubota, Patterson, Eckhardt–Patterson, dFDH) is
  exactly what an index-type reflection needs afterwards: only `Σ |d(m)|²/N(m)` enters the final
  quadratic sieve. So *after* a reflection the individual sextic theta coefficients would not matter.
  The obstruction is the *primal* side: writing `μγ₂ξ` as theta coefficients is (S6). The unknown
  coefficients cannot be averaged away there, because `μγ₂ξ/τ₆` is not periodic.

**Prop. 5 (the Gauss-sum-bias obstruction is harmless here; PROPOSED, uses the KP Hecke relation,
imported).** Suppose the 6-fold Kubota series in the dual rows had its pole at `s = 7/12`. The angular
K-type is expected to kill it (as in R3 §5), but assume it does not. The residue at numerator `h⁴` is
`∝ τ₆(h⁴) N(h⁴)^{−1/12}`, and `|τ₆(m p⁴)| = |τ₆(m)|` by the Hecke relation with `j = 4 ↔ 0`. So the
main term of `B_h` is `≪ X^{7/12} N(h)^{−1/3}`, and its contribution to `E` is

    X^{−1} Σ_{N h ≤ 𝓗} X^{7/6} N(h)^{−2/3} ≍ X^{1/6} 𝓗^{1/3} ≤ X   (𝓗 ≤ X).

Contrast the sextic and cubic operator-norm extremizers. For cubic twists of cubic Gauss sums, the
same computation gives `X^{2/3}𝓗^{2/3}`, which is exactly the BGL term (§6, control `g2`). ∎

So the only obstruction to orthogonality identified in the literature (dFDH abstract; DR) cannot
force κ > 1/2 for the coefficients the cubic family actually produces. An operator-norm conjecture
for order-3 families says nothing about this one vector. What is needed is a *restricted* large sieve
(§7).

## 5. Test beds (d)

* **Quartic over `Q(i)` (c = 3/4).**
  * Absorption: `μγ(χ) = χ(−1)αγ(ρ) conj γ(χ)` (LEVERAGE Q3).
  * Numerator: `h³` (Lemma 1 general form), so `a = 3`.
  * 4-fold Kubota + BGL: σ = **65/64**. Kubota with an optimal sieve only after it: σ = **1**.
    Direct BGL: 17/16.
  * Only a GL(2) quartic theta with one quartic Gauss sum per prime gives **7/8**, and the
    Eckhardt–Patterson shape contradicts that. *The mechanism does not reproduce 7/8.*
  * For the quartic case the two-variable product is `a·b = 3` (`b = 1`), so a G2-type finite group
    is not excluded for the *linear* series `Σ_{h,n}`. Whether a G2 WMDS with these p-parts exists
    was not checked. It would give first moments in `h` only. The mean-square three-variable series
    is indefinite (`det = 4·3·(2 − 3) < 0`, §3), so (b) is closed for the mean square in the quartic
    case too.
* **Sextic (Oct 5, c = 5/6).** Its `B_h = Σ ᾱγ₂ξχ_n(h)` is *not* a Kubota coefficient: a sextic
  twist of a cubic Gauss sum has no numerator. So (a) does not apply, and the index-type cubic theta
  is the only route. That is the imported 11/12.
* **Degree tax re-derived.**
  * Model: reflection of row-conductor exponent `a`, then an optimal sieve available *only after*
    it. Then ρ ≥ max(1, 2 − 2/a) (ledger: `a = 2, 3, 4, 6 → 1, 4/3, 3/2, 5/3`). This reproduces
    LEVERAGE §3's `2 − 2/r` with `a = r`.
  * The tax is real inside that model. It is an artifact in that it is not a theorem: an optimal
    sieve *before* reflection removes it (σ = 5/6 directly, row 8).
  * For Eisenstein (modulus-side) reflections the relevant `a` is `1 + n/2`, not the rank 2.
* `Q(ζ₁₂)`, `Q(ζ₉)`: not done.

## 6. Numerics (EMPIRICAL, floating point, finite)

`dual_ms.py`:

    M(H, X; b) = Σ_{h primary, 0 < N h ≤ H} |Σ_{n ∈ cols(X)} b_n conj χ_n(h)²|²

* `cols(X)`: squarefree primary `n` with `X/2 < N n ≤ X`, built from **split** primes only.
* Rows: primary `h`.
* `γ₂` at primes is computed directly; at composites by twisted multiplicativity. Self-check
  against `eis.gamma`: primes 1.5e-15, composites 2.4e-15, symbol tables 0 mismatches.
* Coefficients:
  * `mu_g2` (`μγ₂`, the absorbed dual coefficient);
  * `g2` (`γ₂`, Kubota-pole control);
  * `rand` (random unimodular);
  * `mu_rnd` (μ × random sign).
* Each cell reports `M/(rows·‖b‖²)`; in parentheses `M/((rows+cols)‖b‖²)` and
  `M/((rows+cols+(rows·cols)^{2/3})‖b‖²)`.

X = 50 000 (6663 columns):

| H | rows | `μγ₂` | `γ₂` | random | `μ`·sign |
|---|---|---|---|---|---|
| 3125 | 1257 | 0.849 (0.135, 0.022) | **6.73** (1.07, 0.172) | 0.944 | 0.921 |
| 12500 | 5040 | 0.914 (0.394, 0.040) | **4.66** (2.01, 0.203) | 0.959 | 0.945 |
| 50000 | 20159 | 0.931 (0.700, 0.065) | **3.39** (2.55, 0.236) | 0.938 | 0.940 |
| 100000 | 40315 | 0.933 (0.801, 0.081) | **2.86** (2.46, 0.249) | 0.941 | 0.938 |

X = 100 000 (13 320 columns; 440 s):

| H | rows | `μγ₂` | `γ₂` | random | `μ`·sign |
|---|---|---|---|---|---|
| 6250 | 2521 | 0.932 (0.148, 0.020) | **8.31** (1.32, 0.175) | 0.952 | 0.919 |
| 25000 | 10080 | 0.948 (0.408, 0.033) | **5.70** (2.45, 0.201) | 0.940 | 0.935 |
| 100000 | 40315 | 0.940 (0.707, 0.053) | **4.02** (3.02, 0.227) | 0.943 | 0.943 |
| 200000 | 80622 | 0.937 (0.804, 0.066) | **3.38** (2.90, 0.238) | 0.943 | 0.943 |

Readings.
* **`μγ₂` has no excess.** At every cell, `M ≤ 0.97 rows·‖b‖²`, within ~5 % of random phases. In
  particular, with fewer rows than columns, `M` is *below* the `(rows+cols)` sieve and far below BGL
  (ratio ≤ 0.08 at X = 5·10⁴).
* **`γ₂` shows the Gauss-sum excess with the predicted law.** At `H = X`, `(ratio − 1)/X^{1/3}` is
  0.065, 0.063, 0.065, 0.065 for X = 4·10³, 2·10⁴, 5·10⁴, 10⁵. At `H = X/16`,
  `(ratio − 1)/(X²/H)^{1/3}` is 0.056, 0.058, 0.062, 0.062. The excess over BGL's own scale stays
  at a fixed fraction (BGL-normalized ratio 0.16–0.24): the `(HX)^{2/3}` term is attained. This is the `X^{5/3}H^{2/3}` Kubota-pole term of the cubic numerator-`h`
  series, i.e. the BGL/HB extremizer mechanism of DR/dFDH, seen at finite size.
* Fitting `c′(X²/H)^{1/3}` to the `μγ₂` excess gives `c′ ≤ 0`. At `X = 10⁵`, `H = 6250`, the
  `μγ₂` ratio is 0.932 against 0.952 for random phases, with `(X²/H)^{1/3} = 117`. Any BGL-type
  component is below about 1 % of the `γ₂` control's constant 0.062. The BGL-normalized ratio of
  `μγ₂` *falls* with X, from 0.043 to 0.022 to 0.020 at `H = X/16`. For `γ₂` it stays flat at
  0.16–0.18.
* Caveats:
  * split primes only;
  * primary rows only;
  * sharp column cutoff;
  * one seed for the random controls.

  This is a finite trend, not evidence of an asymptotic. It is consistent with Prop. 5 and with
  RUNG_STRENGTH §5: diagonal-sized behaviour, no structure to exploit.

## 7. Exponent ledger and the smallest missing statements

`ledger.py` (exact rationals; all asserts pass), with `c = 2/3`, `σ = 1/2 + ρ/3`, `X = D`,
`𝓗 = D^{2−ρ}`:

| pipeline | ρ | σ | label |
|---|---|---|---|
| direct cubic sieve on the absorbed dual, κ = 2/3 (HB/BGL) | 3/2 | 1 | PROPOSED |
| 6-fold Kubota FE (conductor `N(h)⁴`) + BGL | 3/2 | 1 | PROPOSED (imports FE) |
| 6-fold Kubota FE, optimal sieve only after it | 3/2 | 1 | PROPOSED (model) |
| Rankin–Selberg over index `k = h⁴` | 7/4 | 13/12 | PROPOSED |
| primal Heath-Brown sieve on μ coefficients | 2 | 7/6 | PROPOSED |
| hypothetical conductor-`N(h)²` reflection, cubic post-twist, BGL | 7/6 | **8/9** | HEURISTIC |
| (S6) sextic theta, quadratic post-twist | 1 | **5/6** | CONDITIONAL on (S6) |
| (LS*₁/₂) for the absorbed coefficients, no reflection | 1 | **5/6** | CONDITIONAL |
| quartic: 4-fold Kubota + BGL / optimal-after / GL(2) theta | 11/8 / 4/3 / 1 | 65/64 / 1 / 7/8 | PROPOSED / PROPOSED / CONDITIONAL |
| Oct 5 sextic family (cubic theta) | 1 | 11/12 | IMPORTED |

**Statement A (LS*_κ, the smallest analytic input).** For each fixed ray-class character `ξ` and
`1 ≤ 𝓗 ≤ X`:

    Σ_{N h ≤ 𝓗} |Σ_{N n ≍ X}^♭ μ(n) γ₂(n) ξ(n) conj χ_n(h)² U(N n/X)|² ≪ (𝓗 + X + (𝓗X)^κ) X^{1+ε}.

Under the Poisson bookkeeping, this gives σ(κ) = (9κ − 2)/(6κ):
* κ = 1/2 gives 5/6;
* κ = 8/15 gives 7/8;
* κ < 4/7 beats 11/12;
* κ = 2/3 (known, HB00) gives 1.

It is a *restricted* sieve for one coefficient sequence. Its only known obstruction is harmless
(Prop. 5), and the finite data in §6 show κ = 1/2 behaviour. By Poisson in `h` it is equivalent to
the cubic family's own `Mom(1, 3 − 1/κ)`, so it must be proved with input specific to `μγ₂ξ`.

**Statement B (the smallest structural input).** A summation formula with row conductor `N(h)²`
for `n ↦ μ(n)γ₂(n)ξ(n)` twisted by cubic characters of conductor `h`, with dual coefficients
controlled in ℓ² (Rankin–Selberg suffices).
* With the known cubic sieve after it: **σ = 8/9** (beats 11/12).
* If the post-twist is quadratic: **σ = 5/6**.

The 6-fold Eisenstein series gives this with conductor `N(h)⁴` only (Lemma 2); (S6) would give
conductor `N(h)²` and a quadratic twist. Statement B sits strictly between them, since it asks for a
summation formula and no coefficient identity.

**Coordinator benchmark (note (2)).** With conductor `N(h)²` and BGL, `E ≲ 𝓗 + 𝓗²/X + 𝓗²X^{−2/3}`.
Then `𝓗²X^{−2/3} ≤ X ⟺ 𝓗 ≤ X^{5/6}`, giving ρ ≥ 7/6 and σ = 8/9; the stated `X^{2/3}` / 17/18 does
not follow from this formula. The cube-removal and transfer levels of Oct 5 Step 5 were not redone
here with the BGL term, and could add constraints. Within Step 5's self-similar recursion
(`𝓗′/X′ = 𝓗/X`), the condition `𝓗′ ≤ X′^{5/6}` gets easier as `X′` shrinks, so the top level should
bind (HEURISTIC). For the actual 6-fold Kubota conductor `N(h)⁴` the answer is σ = 1.

## 8. Single most promising next step

Statement B in its weakest form. Look for a GL(2)-type (conductor `N(h)²`) Voronoi formula for
`Σ_n μ(n)γ₂(n)ξ(n)ψ(n)V(N n/X)`, with `ψ` cubic of conductor `h`, by realizing the sextic Gauss
sums `γ₋₁(n)` as coefficients of a *non-residual* automorphic object on the 6-fold cover. The
candidate is the Eisenstein series at `s = 1/2 + it` restricted to a Hecke-isotypic component where
Lemma 3's `j = 1 ↔ 3` exchange is diagonalized.

The finite test is concrete. For `n = p` prime, compute the 216-vector of local Whittaker data from
the Kazhdan–Patterson scattering matrix (SEXTIC_THETA_S6 §6), and ask whether some `s` and some
vector make the index-`p` coefficient proportional to `γ₋₁(p)` with a Hecke-character constant.
* If none does, Statement B is false for Eisenstein-type objects, and the cubic family is closed on
  known automorphic inputs.
* If one does, the pipeline gives 8/9 with the known cubic sieve.

## 8A. Round 2: is (S6) locally consistent at a prime? (the local half of the §8 test)

**Verdict: LOCALLY CONSISTENT.**
* *Label:* PROPOSED. It imports the Kazhdan–Patterson periodicity and the KP/Hoffstein Hecke
  relations exactly as stated in [BH] §1 and [CFH] (2.5), via SEXTIC_THETA_S6 §1. KP84 and Hoffstein
  1993 were not re-read.
* At an unramified prime `p`, the local data leave the index-`p` coordinate of the 6-fold theta
  free. They put no constraint on its angle, its sign or its absolute value.
* **Local data therefore do not close the cubic-family 5/6 route via (S6).** It is equivalent to the
  global statement (S6-glob) below.
  * For the one representative set computed by [BH], (S6-glob) is contradicted by their numerics.
  * For the rest of the 216-dimensional theta space it is open.

**Method.** For the `n`-fold theta on GL(2), take `p ∤ mS`. The unramified local relations are:
* (P) `τ(m p^{j+n}) = N(p)^{1/2} τ(m p^j)`;
* (H) `τ(m p^j) = G_{j+1}(m,p) τ(m p^{n−2−j})` for `0 ≤ j ≤ n−2`, and `τ(m p^{n−1}) = 0`.

Here `G_k(m,p)` is the normalized Gauss sum of the `k`-th power of the `n`-th power symbol, with
numerator `m`. (H) pairs the classes `j ↔ n − 2 − j`. That gives three kinds of orbit:
* the orbit `{0, n−2}` is tied to `τ(m)` itself, so it is determined;
* each other pair `{j, n−2−j}` carries one free coordinate;
* a self-paired class `j = (n−2)/2` gives a support condition `G_{n/2}(m,p) = 1` and a free value.

This is the Whittaker-dimension count: 1 for n = 3 (unique model), 2 for n = 4, 3 for n = 6. It
matches [DDHL]'s `n/2 − 1` undetermined classes.

| n | orbits | index-`p` data from (H) | literature | reproduced? |
|---|---|---|---|---|
| 3 | `{0,1}`; `{2}` → 0 | **determined:** `τ(mp)/τ(m) = conj G₁(m,p) = χ_p(m)² conj γ₂(p)` | Patterson (unique model): `τ₃(p)/τ₃(1) = conj γ₂(p)` | **yes**, see note (a) |
| 4 | `{0,2}`; `{1}` self; `{3}` → 0 | `τ(mp²) = conj G₁(m,p) τ(m)` determined; `τ(mp)` **free**, subject to `G₂(m,p) = 1`; `τ(mp³) = 0` | Suzuki 1983 (via [DDHL]): `τ₄(a²) ∝ conj g̃₄(a)`, a quadratic support condition, `ψ(m³ν) = 0`, "nothing about ψ(π)". The Eckhardt–Patterson √Gauss shape is a global conjecture | **yes**, literature-level only; no `Z[i]` numerics |
| 6 | `{0,4}`; `{1,3}`; `{2}` self; `{5}` → 0 | `τ(mp⁴) = G₅ τ(m)` determined; `τ(mp)` **free** with `τ(mp³) = τ(mp)/G₂(m,p)`; `τ(mp²)` **free**, subject to `G₃(m,p) = 1` | [BH] §1; [DDHL]: 2 free classes per prime | 2 free coordinates per `p` |

Note (a): Patterson's composite shape `T(n) = conj γ₂(n)` obeys (H) at 108 `(m, p)` pairs, with
deviation 2.3e-15 (H3, `local_hecke_check.py`). The cubic control of SEXTIC_THETA_S6 §5 measured
the same value numerically, with no extra root of unity.

**The n = 6 index-`p` coordinate against the (S6) shape `c·η(p)γ₋₁(p)`.**
* *Angle.* (H) imposes no angle on `τ(mp)`; it only links it to `τ(mp³)`. `γ₋₁` has the sextic
  angle, and [BH]'s data show the sextic angle mod 1/2 (SEXTIC_THETA_S6 §3.3).
* *Sign and absolute value.* The coefficients of (H) are unimodular Gauss sums, so neither `|τ(mp)|`
  nor its sign is constrained locally.
* *Hecke relation.* (S6) forces the cube-index coordinate. Check H6: 108 cases, deviation 3.4e-15.

      (S6) at p  ⟺  τ(m p³)/τ(m) = μ(p) · c (η/α)(p) · χ_p(16) G(p) · ε(m, p),   ε = χ_p(m) conj χ_m(p) ∈ {±1},

  with `G(p) = conj χ_p(4) γ₃(p)` the quadratic Gauss sum. So (S6) says the following: at cube
  indices, the 6-fold theta coefficient is `μ(p)` × a Hecke character of infinity type `α^{−1}η` ×
  a quadratic Gauss sum, twisted-multiplicative with the exact reciprocity sign. No local relation
  sees the factor `μ(p) = −1`.

**The global statement that remains (S6-glob).** There exist
* a vector `v` in the finite-dimensional space of 6-fold theta functions over `Q(ω)` (the 216
  residue classes of [BH] Lemma 2.2),
* a constant `c ≠ 0`, and
* a Hecke character `η`,

such that `Σ_η v_η ρ(p, η) = c η(p) γ₋₁(p) Σ_η v_η ρ(1, η)` for every prime `p ∉ S`, and the
coefficients are twisted-multiplicative on squarefree indices. Equivalently, that theta's global
Whittaker functional is a pure tensor `⊗_p ℓ_p` on the squarefree support, with the `ℓ_p` of the
display.

* *Local consistency.* Every `ℓ_p` exists locally. With non-unique local models (Deligne, KP), no
  theorem forces or forbids factorization of the residue's functional. (S6-glob) asks infinitely
  many conditions (one per `p`) of a vector in a 216-dimensional space, so it is overdetermined and
  generically false. This is a count, not a proof.
* *Global evidence against* (imported numerics, [BH] Conj. 5.7, one `V`):
  * `|τ(π)/τ(1)|² ∈ {1, 7/3}` is not constant.
  * In cube-index language, [BH]'s shape gives `τ(π³)² ∝ conj γ₂(π)² · (cubic Gauss sum) · (small
    algebraic)`. If their cubic Gauss sum is `γ₄`, then `τ(π³)² ∝ γ₄³ = −ᾱ`, so `τ(π³)` has
    half-integral infinity type. The display above needs the integral type `α^{−1}η`. This is
    [INF]: the conventions caveat of SEXTIC_THETA_S6 §3 applies.
* *HEURISTIC (not evidence).* CFH ties the square indices of the 6-fold theta to the cubic theta
  and cubic Gauss sums. By analogy, cube indices would be tied to the double-cover theta and
  quadratic Gauss sums. Such an object supplies `G(p)` but has no source for `μ(p)·(α^{−1}η)(p)`, so
  (S6-glob) would fail, and fail exactly in the Möbius sign. No cube-index statement of CFH type was
  found in the sources read.

**The Eisenstein-at-general-s half of the §8 test (HEURISTIC).** By Lemma 3,
`ψ(mp, s) = ψ^{(p)}(mp, s) + G₂(m,p) q^{1/2−2s} ψ^{(p)}(mp³, s)`. The first term,
`Σ_{p∤c} conj χ_c(p) g̃(m,c) N(c)^{−s}`, depends on `p` through a character of conductor `p`, not
through a Gauss sum at `p`. Only at the residue does the Hecke relation make the second structure
rigid. So no non-residual Eisenstein vector is expected to have index-`p` coefficients
`∝ γ₋₁(p)`. Statement B of §7 (any conductor-`N(h)²` summation formula) asks less than
(S6-glob) and is untouched by this test.

**Bottom line for the cubic family.** The 5/6 route via (S6) is **not locally obstructed**. It is
equivalent to (S6-glob):
* contradicted for the one theta whose prime coefficients have been computed ([BH]);
* open for the other theta functions;
* the decisive test is the cluster-scale residue-vector computation (SEXTIC_THETA_S6 §6 item 1,
  [BH] Algorithm 4.1, split `π` with `Nπ ≤ 100`).

## 9. Not done

* No direct numerical test of the load-bearing imported claim (Lemma 2: row conductor `N(r)`, so
  `N(h)⁴` for the cubic family). A finite test is feasible: the transition scale of the smoothed
  `Σ_n μγ₂ conj χ_n(h)² U(N n/X)` (all moduli, inert primes included) for one small prime `h`, at
  `X ≈ N(h)⁴` versus `N(h)²`. It needs moduli up to about `30X` and was not run. The `γ₂` control of
  §6 reproduces the cubic Kubota residue bookkeeping (`X^{5/3}H^{2/3}`), which is indirect support
  only.
* G2-type WMDS for the quartic test bed (§5) was not checked.
* `Q(ζ₁₂)`, `Q(ζ₉)` were not examined.
* dFDH: abstract only; its operator-norm conjecture was not read.
* PR 930 (Bessel channels) was not read.
* Lemma 2's FE is imported (CG10 Thm 6.1 via A2_LITERATURE, Kubota/Patterson). The isometry
  bookkeeping ignores Γ-factor transition ranges and the finite S-class mixing.

## Reproduction

```
cd research/exploratory/qrh-2026-10/offense/O1_CUBIC_FAMILY_REFLECTION
python3 ledger.py                                    # exact ledger, asserts
python3 kubota_mobius_check.py 250 out.json          # K1-K3, ~2 min
python3 local_hecke_check.py out.json                # H3, H6 (round 2)
python3 dual_ms.py check                             # gamma_2 / symbol self-check
python3 dual_ms.py 50000 3125,6250,12500,25000,50000,100000 out.json   # ~90 s
python3 dual_ms.py 100000 6250,12500,25000,50000,100000,200000 out.json
```
