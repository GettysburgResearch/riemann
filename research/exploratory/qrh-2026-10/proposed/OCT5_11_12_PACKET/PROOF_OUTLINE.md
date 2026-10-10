# Proof outline: no zeros in Re s > 11/12 (condensation of the Oct 5 manuscript)

```text
Status: PROPOSED proof outline (an editorial condensation of an IMPORTED external proof). It adds no
  mathematics and strengthens nothing. Each step cites paper2.tex lines and the bounded agent
  review that covered it. Simplifications are marked [S1]-[S8] and listed at the end.
Scope: the deduction of thm:main (paper2.tex 73-75) from its own lemmas, lines 660-3650
Exact sources or dependencies: paper2.tex at pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6,
  SHA-256 d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d; reviews R1, R2, R3 and the
  residual note at c2050a5dd8c251f25e5fc285c0845b9f4a42487b (see README.md §1, §6)
What was actually run: nothing beyond README.md and CHECKS.md. This file is a reading aid.
Smallest remaining gap: Prop. prop:R (README.md §8)
```

RH remains unsolved. This outline is a reading aid for an independent reviewer. It is not a
substitute for the manuscript, and it is not itself reviewed. When this outline and `paper2.tex`
differ, the manuscript governs. Review labels: **R1**, **R2** and **R3** are the three bounded
reviews in `../../reviews/`, and **Res** is `OCT5_RESIDUAL_ITEMS.md`.

## 0. Notation (lines 184-205, 239-276, 795-821, 934-960)

* **Field and units.** `K = Q(ω)`, `O = Z[ω]`, `λ = 1 + 2ω`, and `N = N_{K/Q}`. An element is
  **primary** if it is `≡ 1 (mod 3)`. Each ideal prime to `3` has a unique primary generator.
* **Residue symbols.** `χ_n(u) = (u/n)_6` is the sextic residue symbol, extended by zero. On
  `(n, 6) = 1`, `χ_n³` and `χ_n²` are the quadratic and cubic symbols.
* **Gauss sums.** Put `e(z) = exp(4πi·Im z/√3)`, `α(n) = n/|n|` and
  `γ_j(n) = N(n)^{−1/2} Σ_{x mod n} χ_n(x)^j e(x/n)`.
* **Gauss-sum coefficients.** For squarefree `n` and a character `ξ` of a fixed ray class group
  (modulus supported on `S`), `a_ξ(n) = ᾱ(n) γ₂(n) ξ(n)`.
* **Soft inequality.** `A ≼ B` means `A ≪_ε D^ε B` for every `ε > 0`.
* **Two different `H`s.** `H = D^{1+ϑ}` is the original row range, and `𝓗` is a dual row range.
  [S1] This outline writes `𝓗` throughout for dual ranges, as the manuscript does.

## Step 1. From a mean square to the zero-free half-plane (lines 660-771; R1 §3)

**Input.** Prop. thm:ms (679-689): `Σ_{0<N(u)≤D^{1+ϑ}} |A_u(D)|² ≪ ‖W‖²_{C^k} D^{2+ϑ+ε}`, for
`A_u(D) = Σ_{(n,S)=1} μ(n)ν(n)χ_n(u)W(N(n)/D)`. The quantifiers are in README §2.2.

**1a. Sixth-power extraction (694-725).**

* Take primary primes `p ∉ S` with `Y/2 < N(p) ≤ Y`, where `Y = H^{1/6}`.
* Since `n` is squarefree and prime to `S`, `χ_n(p⁶) = 1_{p∤n}`. Hence
  `|A_1(D) − A_{p⁶}(D)| ≪_W D/Y`.
* By Landau's prime ideal theorem (I5) there are `J ≍ Y/log Y` such primes. Their sixth powers are
  distinct rows of norm `≤ H`. All other rows are dropped by positivity.
* With `|x|² ≤ 2|x−y|² + 2|y|²` this gives

      |A_1(D)|² ≤ (2/J) Σ_p |A_{p⁶}(D)|² + O(D²/Y²) ≪ D^{11/6 + 5ϑ/6 + ε} + D^{5/3 − ϑ/3}.

* So `A_1(D) ≪ D^{11/12 + 5ϑ/12 + ε}`. Fix the target loss, choose `ϑ` small, and rename `ε`. This
  gives eq:mobius-saving: `A_1(D) ≪_{ν,S,W,ε} D^{11/12+ε}` (723).

The exponents were checked in exact rationals (R1 C1; R2 A). There is no Hölder step: this is the
`k = 1` case of the extraction in PR 910 (R1 §3.1).

**1b. Mellin contradiction (727-759).**

* Suppose `L_K(ϱ, ν) = 0` with `Re ϱ > 11/12`. Take `W(y) = y^{−ϱ}φ(y)` with
  `0 ≠ φ ∈ C_c^∞((1,2))` and `φ ≥ 0`. Then `Ŵ(ϱ) = ∫φ(y) dy/y > 0`.
* `𝓜_W(s) = ∫_0^∞ A_1(D) D^{−s} dD/D` is holomorphic on `Re s > 11/12`, by 1a.
* For `Re s > 1`, Fubini gives `𝓜_W = Ŵ / L_K^S(s, ν)`.
* Hecke's continuation (I6) and the identity theorem give `L_K^S·𝓜_W = Ŵ` on `Re s > 11/12`, with
  `s = 1` excluded for principal `ν` (repair N1; Res §3).
* The removed Euler factors are nonzero, so evaluation at `ϱ` gives `0 = Ŵ(ϱ) > 0`, a contradiction.
* `W` and hence all constants depend on `ϱ`, but no uniformity in `ϱ` is needed (R1 §3.4).

**1c. Dirichlet transfer (760-770).**

* `L_K(s, χ∘N) = L(s,χ) L(s,χχ_{−3})` up to Euler factors that are nonzero for `Re s > 0` (I12).
* Away from `s = 1`, a zero of `L(s,χ)` is therefore a zero of `L_K(s, χ∘N)`.
* At `s = 1`, the only possible pole–zero cancellation is excluded by `L(1,χ_{−3}) > 0` (I11).
* The Euler factors and all the `s = 1` cases were checked by hand (R1 §3.3).

## Step 2. Poisson summation in the row and the dual mean square (lines 773-1252; R1 §4)

**2a. Möbius absorption (lem:arithmetic, statement 823-857, proof 2691-2872).** There is a
unimodular function `G` and a symmetric `±1` bicharacter `𝓡` on a fixed ray class group such that,
for squarefree primary `n` prime to `S`,

    μ(n) γ_{−1}(n) = χ_n(−1) G(n)^{−1} ᾱ(n) γ₂(n)        (eq:convert2),
    ᾱ(n) γ₂(n) γ₁(n) = μ(n) G(n)                           (eq:convert1).

The proof has three parts.

* *Prime case.* The key facts are `J(χ², χ²) = −p` and `γ₂(p)³ = −α(p)`. They follow from the
  Gauss–Jacobi identity (I10) and a congruence mod 3 (R1 §4.1).
* *Composite case.* Twisted multiplicativity `γ_j(ab) = (χ_a(b)χ_b(a))^j γ_j(a)γ_j(b)`. The
  reviewer's own check is that the two sides then acquire matching factors, because `𝓡² = 1`
  (R1 §4.1).
* *Class-function facts.* `G` and `𝓡` are functions of classes mod 4. This uses Hecke's
  quadratic Gauss-sum reciprocity (I8) and cubic reciprocity (I9).

Checks: C2 checks 337 composites to `6.6e-15`; R2 E checks the paired forms; the earlier numerics
cover all `N(n) ≤ 50000`.

**2b. Poisson with exclusions (lem:poisson, 875-932).** For a primitive character `χ` mod `𝔪` and
an exclusion ideal `𝔯`,

    Σ_k χ(k) 1_{(k,𝔯)=1} Φ(N(k)/𝓗) = (𝓗γ(χ)/√N𝔪) Σ_{d|rad 𝔯} μ(d)χ(d)/N(d) Σ_h χ̄(h) Φ̂(𝓗N(h)/(N(d)N𝔪)).

The zero frequency survives only for `χ = 1`. The normalization was re-derived: `O` is self-dual
under `e(zw)` and has covolume 1 (R1 §4.3; C4 to `3e-14`).

**2c. Reduction to a dual problem (prop:poisson-reduction, 1000-1252).**

1. Majorize the row sum by a radial `Φ ≥ 0`, with `Φ ≥ 1` on `[0,1]` and `Φ̂` compactly supported
   (1024-1035).
2. Expand the square. Write `g = (n₁,n₂)` and `n_j = g z_j`. The row character
   `χ̄_{z₁}χ_{z₂}` is primitive mod `z₁z₂`.
3. Apply 2b in `u`. The zero frequency (`z₁ = z₂ = 1`) is `Z ≪ H‖W‖²_∞` and is kept exactly
   (1054-1060).
4. The paired Gauss-sum identity eq:initial-paired-gauss (1063-1070) turns
   `μ(z₁)μ(z₂)ν̄(z₁)ν(z₂)γ(χ̄_{z₁}χ_{z₂})` into `Σ_ξ c_ξ a_ξ(z₁) ā_ξ(z₂)`. **The Möbius coefficients
   become cubic Gauss-sum coefficients.**
5. Remove `(z₁, z₂) = 1` by Möbius inversion in `v`. Then change variables bijectively,
   `(g,e,v,h) ↦ (b,f,k) = (g/e, ev, eh)`, which gives eq:initial-column-output (1141-1167; C5).
6. Split `b` and `f` into dyadic ranges. This gives the scales (eq:initial-scales, 1001-1006)

       X = D/(BF),    0 < 𝓗 ≤ C D²/(H B²),    Σ := XF = D/B,    so 𝓗/Σ ≪ D^{−ϑ}.

7. Separate the coupled kernel with lem:smooth-mean-square (3566-3615). Remove the exclusion
   `(n,b) = 1` with lem:remove-exclusions (962-992).

**Conclusion of Step 2.** If the dual mean square

    E(𝓗,X,F;ξ,W) = (XF)^{−1} Σ*_{F≤N(f)<2F} Σ_{0<N(k)≤𝓗} |Σ*_{(n,S)=1} a_ξ(n) χ_n(k) χ_n(f)⁴ W(N(n)/X)|²

satisfies `E ≼ ‖W‖²_{C^J} · XF` in these ranges (eq:auxiliary-target, 1008-1013), then thm:ms holds.

R1's strongest check is C6: an end-to-end numerical replay of the exact identity
`M_D = Z + Σ_ξ c_ξ S_ξ` at `D ∈ {30, 45, 60}`, to `≤ 2e-14`. Diagonal terms, zero frequencies,
shared factors and the sixth-power rows are all treated exactly; positivity of `Φ` is the only
inequality used before the dual estimate (R1 §5).

## Step 3. The canonical descent (lines 1254-1629; R2 §3)

**Target (prop:canonical, 1261-1277).** Fix `κ > 0` and `C₀ ≥ 1`. If `𝓗, X, F ≥ 1`,
`Σ = XF ≤ D^{C₀}` and `𝓗 ≤ Σ D^{−κ}` (a **positive gap**), then `E(𝓗,X,F;ξ,W) ≼ ‖W‖²_{C^J} Σ`.

**3a. Completed sums (1282-1309).** Put `V_*(y) = √y W(y)`. For completely multiplicative `Ψ`
vanishing on `S`, define

    T(X;Ψ) = Σ*_{(n,S)=1} Σ_{b≡1(3),(b,S)=1} ᾱ(n)γ₂(n)Ψ(n) ᾱ(b)³Ψ(b)³ / (√N(n) N(b)) · V_*(N(n)N(b)³/X),

and `T(X;k,f) = T(X;Ψ_k)`, where `Ψ_k(n) = ξ(n)χ_n(k)χ_n(f)⁴`. The `b = 1` part is the column sum
of `E`. The extra cube index `b` supplies the cubes that appear in the Fourier expansion of the
cubic theta function.

**3b. Cube reduction (lem:cube-reduction, 1341-1467).** Möbius inversion in the cube index gives
eq:cube-inverse (1361-1373): the column sum equals `Σ_h μ(h) ᾱ(h)³ Ψ_k(h)³ N(h)^{−1} T(X/N(h)³; k, f)`.
Split it at `H_c³ = min(X, X²/𝓗²)`.

* *Short part* (`N(h) ≤ H_c`). Apply prop:R. The result is `≼ 𝓗 + 𝓗²F H_c³/X ≤ 2Σ`. Here
  `𝓗 ≤ Σ` by hypothesis, and `𝓗²F H_c³/X ≤ Σ`, with equality when `H_c³ = X²/𝓗²` (R2 C).
* *Long part* (`N(h) > H_c`). Expand `T` again and put `b = hc`. Weighted Cauchy–Schwarz then gives
  `log²·sup_{N(b)>H_c, L_b>1} E(𝓗, L_b, F)`, where `L_b = X/N(b)³`.

So `E ≼ Σ‖W‖² + sup_b E(𝓗, L_b, F)`. The supremum is empty when `𝓗² ≤ X`.

**3c. Transfer (prop:transfer, 1487-1509; proved in Step 4).** Assume `1 ≤ 𝓗, L, F, Σ ≤ D^{C₀}` and
`max(𝓗, LF) ≤ Σ`. Then the smoothed `𝓐(W) ≥ E(𝓗, L, F)` satisfies

    𝓐(W) ≼ Σ ‖W‖²_{C^{4m+12}} (1 + sup E(𝓗',X',F';ξ',U)/Σ'),
    with 𝓗' ≤ 𝓗L/(ΣF),   𝓗'/Σ' ≤ 𝓗/Σ,   Σ' ≤ L,

over test functions `U` supported in `[u/16, 4v]` with `‖U‖_{C^m} ≤ 1`.

**3d. Induction (1516-1609).** Induct on `j`, with `𝓗 ≤ D^{jκ}`.

* *Base case.* `𝓗 = 1` is trivial by counting.
* *Step.* For `N(b) > H_c` (so `N(b)³ > X²/𝓗²`), apply 3c at `L = L_b`. Then

      𝓗' ≤ 𝓗/(N(b)³F²) < 𝓗(𝓗/Σ)² ≤ D^{−2κ}𝓗,    𝓗'/Σ' ≤ 𝓗/Σ ≤ D^{−κ},    Σ' ≤ L_b ≤ Σ.

  So every child satisfies the hypotheses one level down. R2 C verifies this with an exact Farkas
  identity, `h − 2κ − h' = s₁ + s₂ + 2s₃`, in log coordinates.
* *Bookkeeping.* The `ε` losses split as `ε/3 + ε/3 + ε/3`. The derivative order grows as
  `J_{j+1} = max(4J_j + 12, J_cube)`.
* *Termination.* The recursion stops after `j = ⌈C₀/κ⌉` levels.
* *Regime `𝓗 > X`.* This is possible when `F > D^κ`. Then `H_c < 1`, `b = 1` enters the supremum,
  and the contraction comes from `F^{−2}`. The manuscript handles this but does not discuss it
  (R2 F1). [S2] The outline above folds it in.

**3e. Completion (1611-1629).** By 2c, `𝓗/Σ ≪ D^{−ϑ}`. Hence prop:canonical applies with
`κ = ϑ/2` and `C₀ = 2` once `D` is large. The cases `X < 1`, `𝓗 < 1` and bounded `D` follow by
counting. This gives eq:auxiliary-target, hence thm:ms, hence thm:main.

* There are `⌈4/ϑ⌉` levels: 40 at `ϑ = 1/10`.
* The derivative order is at least `5·4^⌈4/ϑ⌉ − 4`. This is why there is no height uniformity
  (R2 F3).

## Step 4. The transfer estimate (lines 2217-2683; R2 §4)

**4a. First Poisson summation (lem:first-transfer, 2263-2349).**

* Expand `𝓐(W)` with `n_i = C u_i`. Apply 2b in the row `k`, with exclusion `C`.
* The paired identity eq:paired-first-gauss (2288) uses eq:convert1 and eq:quotient. It turns
  `a_ξ(u₁)ā_ξ(u₂)γ(χ_{u₁}χ̄_{u₂})` back into Möbius coefficients `μ(x)ξ₁(x)` with a residue twist.
* The zero frequency is `≪ 𝓗 ≤ Σ`.
* Fold `f` into `y = hf²`.
* **Enlarge the `y`-range** to `Y_{C,d} = c_I Σ L F N(d)/(𝓗 N(C)²)`. By positivity this exceeds the
  natural range by the factor `(c_I/4C_Φv²)·Σ/(LF) ≥ 1`. This is Heath-Brown's device.
  * The enlargement costs only in the diagonal, which is now `≍ Σ`.
  * It shortens the next dual range to about `𝓗L/(ΣF)` (R2 §5.1; check B).

**4b. Second Poisson summation (lem:arithmetic-poisson, 2407-2494).** Apply Poisson in `y`,
including the gcd `g`, the exclusion `e | g` and a Möbius variable `w`. A second paired identity
(2409) returns the coefficients `a_{ξ'}`.

**4c. Regrouping and the sign sum (lem:second-transfer, 2496-2670).**

* Seven auxiliary indices regroup into a new triple:

      r = tg/e,    f' = Cew,    k' = deh.

* For fixed `(r, f', k')`, every preimage has the same kernel (2550-2558). Summing before taking
  absolute values, each prime `p | f'` contributes
  `(1 + 1_{p|k'}) − 1_{p|k'} − 1_{p∤k'} = 1_{p|k'}` (2561-2566).
  * So the total coefficient is `τ(r)·1_{f'|k'}`.
  * R2 D checks this exhaustively for up to 6 primes.
  * This forced divisibility is what makes the child family smaller.
* Blocks are dyadic, with `Σ' = L/R` and `𝓗' = 𝓗L/(ΣFR²)`.
* `lem:remove-exclusions` removes the exclusion `r`. The children have exactly the form of `E`, so
  the family is closed.
* The block total is `(ΣR/L²)·R·Σ'² = Σ`. The zero frequency is `≪ Σ log L`.
* The derivative order becomes `4m + 12` (2672-2683).

R2's verdict for Steps 3-4 is "PASS conditional on Prop prop:R, Lemma lem:arithmetic and Lemma
lem:smooth-mean-square".

## Step 5. The completed mean square, prop:R (lines 1632-2214 and 2874-3479; R3, Res)

**Statement (1317-1333).** For `1 ≤ 𝓗, X, N(f) ≤ D^{C₀}`:

    Σ_{0<N(k)≪𝓗} |T(X;k,f)|² ≼ ‖W‖²_{C^J} (𝓗 + 𝓗² N(f)/X).

This statement carries all of the automorphic content.

**5a. Theta realization (1639-1718).**

* Kubota's cubic theta function `θ` is used in Dunn–Radziwiłł's normalization (1650; I2-I4).
* Its coefficients at `nb³` are `c_θ(nb³) = 3^{5/2}|b| conj(χ_n(λ)²) γ₂(n)` (363). This holds
  including `(n, b) ≠ 1`; R3 check G covers 434 cases.
* So `T(X;k,f)` is a smoothed, twisted sum of the coefficients of `θ̄` (eq:T-theta).
* Finite Fourier inversion writes the twist as a finite sum of translates `θ̄(z + λ²h/q, v)`
  (eq:theta-twist-translates). The constant terms cancel because `φ(0) = 0`.

**5b. Transformation (lem:reflection 1805-1821; proof 2904-3479).** [S3] Stated schematically.

* *Automorphy.* Each translate is moved to one of three cusps `σ ∈ {0, +, −}` by an automorphy with
  Kubota multiplier `κ(g) = (c/a)_3`. The multiplier formula eq:ray-multiplier (3175) was read by
  hand and matches `(c₁/a₁)_3` on 700/700 test instances, EXACT (R3 check D). The translate identity eq:theta-cusp-automorphy (3161) holds on 44 cases
  (check E).
* *Local twists.* The local Fourier analysis at active primes gives the factors `B_{p,j}`
  (eq:theta-local-factors, 1735). Here `B_{p,j} = χ_p^{−j−2}` for `j ≠ 0, 4`.
  * For the active exponent `j = 1` this gives `B_{p,1} = χ_p³`, **a quadratic character** (1745).
  * The sign of the exponent comes from the multiplier convention. Under the conjugate convention,
    `j = 1` would give `χ_p`, a sextic character (R3 §3; checks A, C).
* *Archimedean part.* The angular factor `ᾱ` is produced by applying `∂_z̄` at `z = 0` (3307-3343).
  * This **annihilates the constant mode at every cusp**.
  * So the Mellin transform `𝓣(s, Ψ)` is entire, and no Kubota/Patterson residue appears
    (3355-3370, 3408; R3 §5; Res §2A-B).
* *Contour shift.* The contour is moved by Phragmén–Lindelöf (3395-3418; Res §2C-F).
* *Result.* `T(X;Ψ)` is a sum of `O(2^{|𝒫|})` terms of the form

      C Σ_{0≠ℓ∈λ^{−4}O} d(ℓ)α(ℓ)/√N(ℓ) · ψ(λ⁴ℓ) Π_{p∈𝒜} B_{p,j_p}(λ⁴ℓ) · V_*^♯(N(ℓ)X/N(c)²),

  where `c = c₀ Π_{p∈𝒜} p` and `V_*^♯` is given by the gamma quotient in eq:theta-weight (1752).

**5c. Uniformity and bounds.**

* *Uniformity (lem:reflection-uniformity, 1847-1855).* For the row family `Ψ_{k₀}`, the cusp data
  `(d, ψ, c₀)` depend on `k₀` only through its ray class modulo a fixed ideal supported on `S`.
* *Support and size (lem:theta-bounds, 1859-1877).* `d(ℓ)` is supported on `ℓ = uλ^m n b³` with
  `m ≥ −4`, and `|d(ℓ)| ≤ 27·3^{m/6}|b|`.
* *Weight decay.* `|(x∂_x)^j V_*^♯(x)| ≪ ‖V_*‖_{C^J} min(x^{1/4}, x^{−A})`. The first pole of the
  kernel is at `t = −5/6` (R3 §4; Res §2G).

**5d. Quadratic large sieve (lem:quadratic, 1886-1913; I1).**

    Σ*_{k≡1(3),(k,S)=1,N(k)≤𝓗} |Σ_{n squarefree, N(n)≍U} β(n) χ_k(n)³|² ≼ (𝓗 + U) Σ|β(n)|².

This is GL Thm 1.1, applied to the family `ψ_k(x) = (x/k)₂ κ_λ(x)^{e_k}`. That family is trivial on
units, primitive of conductor `kλ^{e_k}`, and satisfies GL's reciprocity property mod 4 (Res §1;
checks G1-G5 EXACT).

* GL's bound has the shape `M + N`, not `M + N + (MN)^{2/3}`.
* That is why the quadratic conversion in 5b matters (lines 409-416).

**5e. Squarefree rows (lem:squarefree-completed, 1923-2187).** Split `s = t k₀`.

* Separate the `k₀`-dependent weight `V_*^♯(…/N(k₀)²)` using lem:smooth and lem:recombine
  (2112-2141; Res §1.4).
* Apply 5d over `k₀` with dual columns `n`. The cube variable `b` stays outside the large sieve.
* The cost table at the primes of `t` and `g` gives a total of `≪ 𝓗₀ + a²Y`, with
  `a²Y ≪ 𝓗₀² N(t)² N(g)/X`. Summing over `t` gives `≼ 𝓗 + 𝓗² N(g)/X` (R3 §7).

**5f. All rows (2189-2214).**

* Write `k = u₀ s v²`. Since `8 ≡ 2 (mod 6)`, `T(X; u₀sv², f) = T(X; u₀s, fv²)`.
* Apply 5e with row bound `𝓗/N(v)²` and `g = fv²`.
* Then sum over `v`, which gives `Σ_v N(v)^{−2} = ζ_K(2)` (R3 §7).

## Step 6. Where `11/12` comes from

[S4] The manuscript's own bookkeeping is in 1a: `D^{2+ϑ}/Y` with `Y = D^{(1+ϑ)/6}`.

* *Origin of `1/6`.* The `1/6` comes from the sixth-power rows `u = p⁶`, which are the only rows on
  which `χ_n(u)` is principal for all `n`.
* *Origin of `ϑ`.* `ϑ > 0` is needed so that the dual problem starts with a positive gap,
  `𝓗/Σ ≪ D^{−ϑ}`. Step 3 needs that gap to contract.

RUNG_STRENGTH.md rewrites this as `σ = 1/2 + 5ρ/12`, with `ρ` the row/column ratio, so that `ρ = 1`
gives `11/12`. That is an elementary reformulation made in this repository, not part of the
manuscript. Its further claim, that the pipeline cannot pass `ρ = 1`, is labelled HEURISTIC there.

## Marked simplifications

| Tag | Where | What was simplified | Effect on the statement |
|---|---|---|---|
| S1 | throughout | the fixed finite sum over ray class characters `ξ` and the coefficients `c_ξ` are often suppressed; dual ranges are written `𝓗` | none; the sum is finite and fixed |
| S2 | 3d | the regime `𝓗 > X` (R2 F1) is folded into the main case | none; R2 checked that it closes |
| S3 | 5b | the transformation is stated without the active/inactive prime sets, the triples `(d,ψ,c₀)`, the constant `C`, the additive character `ψ` and the case split on `v_λ(c)` | none; full statement at 1805-1821 |
| S4 | Step 6 | the `ρ` reformulation is the repository's, not the manuscript's | none |
| S5 | Steps 2-5 | `D^ε` losses and `C^J` norms are absorbed into `≼`; the derivative orders are given only where they matter (3d, 3e, 4c) | none; see R2 F for the orders |
| S6 | 2c, 4a-4c | exclusion ideals, the `τ(r)` factor, the Möbius variables `t`, `v`, `w` and the dyadic block bookkeeping are abbreviated | none; replayed in R1 C5-C6 and R2 B, D |
| S7 | 1a | the restriction `p ≡ 1 (mod 3)` and `p ∉ S` is written once | none |
| S8 | 5e | the cost table (2066-2091) and the dyadic sums (2157-2161) are summarised by their outcome | none; read line by line in R3 §7 |

No simplification changes a hypothesis, a quantifier or an exponent. If one appears to, the
manuscript lines cited in that step govern.
