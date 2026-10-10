# R1 review: the reduction to a mean square and the first Poisson summation (Oct 5 quasi-RH manuscript)

```text
Status: REVIEW (bounded; external manuscript)
Scope: paper2.tex lines 206-658 (Section 2, outline; Steps 4-5 checked for internal arithmetic only),
  660-771 (Section 3, sec:reduction: Prop thm:ms -> Theorem thm:main, lines 73-75),
  773-1252 (Section 4, sec:initialization: lem:arithmetic, lem:poisson, eq:energy,
  lem:remove-exclusions, prop:poisson-reduction), 2689-2872 (App. app:gauss-identities, proof of
  lem:arithmetic), 3481-3615 (App. app:weights, lem:smooth and lem:smooth-mean-square, as invoked),
  and the interface 1261-1278 / 1611-1630 (prop:canonical -> eq:auxiliary-target), parameters only.
Exact sources or dependencies: manuscript at local ref pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6,
  path standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
  The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex (upstream openai/math@adc7f124),
  3988 lines, SHA-256 d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d.
  Prior work read: origin/claude/openai-math-riemann-analysis-w5copg = bd670c92d15f835021c6579ed273b213d71caff7
  (standalone/2026-10-07-openai-quasi-rh/README.md sections 2, 3, 8; numerics/RESULTS.md);
  pr910 = 670a76c1a3a8f325c43c1755b1cfc24d313a3e3c (UPSTREAM_HEIGHT_AND_MOMENTS.md, sections 2, 3, 7).
  Exact-symbol code: a2/eis.py, SHA-256 87ca11d98bf3ee130a6dab613b5f7efe444058320b7c22b005327686f2798e65.
What was actually run: a line-by-line reading of the scoped lines, with every displayed identity in
  Section 4 re-derived by hand. reviews/oct5_r1_checks.py (SHA-256
  4fc6c5d72aa5533a88c205b7ba8b39783212fed14e83a51e3c1b3c34afc9cd54) was written for this review and run
  in full (`python3 -I oct5_r1_checks.py --out <scratch>.json`, 114 s; it prints ALL CHECKS PASSED). It ran
  six check groups, C1-C6, and all pass. The JSON record (SHA-256 59160e44...f44d, kept outside the repo)
  was identical in two runs. The strongest check is C6.
  It is a full numerical replay of the exact identity M_D = Z + sum_xi c_xi S_xi in its final form
  eq:initial-column-output. It covers all rows u in O at tiny D, with D in {30,45,60} and H in {4,6,9,40}.
  It uses nu trivial and nu of order 3, and agrees to <= 2e-14. These are finite numerical checks. They
  replay no analytic estimate.
Smallest remaining gap: none found inside R1. Every load-bearing step in the scoped lines was verified,
  or traced to a standard imported theorem (Landau's prime ideal theorem, Hecke continuation, lattice
  Poisson summation, Hecke's quadratic Gauss-sum reciprocity). The first unverified step that R1's
  conclusion rests on lies outside R1. It is hypothesis eq:auxiliary-target (lines 1008-1013), which
  sec:completion (lines 1620-1627) supplies from Prop prop:canonical (lines 1261-1278). That proposition
  is proved from Prop prop:R (line 1317), Lemma lem:cube-reduction (line 1341) and Prop prop:transfer
  (line 1487). These are R2/R3 scope and are not reviewed here.
```

RH remains unsolved. This review covers neither RH nor the full quasi-RH claim. It checks one bounded part of an external, unreviewed manuscript: the implication

> eq:auxiliary-target (dual mean square, all scales) ⇒ Prop thm:ms (original mean square) ⇒ Theorem thm:main (no zeros of finite-order Hecke L-functions over Q(√−3), and hence of Dirichlet L-functions, in Re s > 11/12).

**Verdict for R1.** Both implications are correct as written, apart from three non-load-bearing expository points listed in Section 6. The Poisson comparison treats diagonal terms, zero frequencies, rows sharing factors with the columns, and the sixth-power rows exactly. No term is dropped, and no inequality is used before positivity is available. Everything that makes the theorem hard is concentrated in eq:auxiliary-target, which lies outside this review.

## 1. Verdict table

| # | Claim | Lines | Checked how | Result |
|---|---|---|---|---|
| 1 | Outline Step 1-2: the A_u family, the identity χ_n(p⁶) = 1_{p∤n}, and A_{p⁶} = A_1 + O(D/Y) | 212-299 | By hand. Numerics in w5copg RESULTS.md match the direct formula to 2.9e-12. | OK |
| 2 | Outline exponents in eq:intro-extraction: D^{1+ε}H^{5/6} + D²H^{−1/3} gives 11/12 + 5θ/12 | 290-298 | Exact rationals (C1) | OK |
| 3 | Outline Steps 3-5: the Gauss/Möbius identity, eq:intro-poisson-comparison, the cube-completion algebra, H_c, the transfer scale algebra ℋ' = ℋL_b/X, and the contraction ℋ' < ℋ(ℋ/X)² | 301-658 | Internal arithmetic re-derived by hand. Labelled schematic by the authors; the precise forms are in Sections 5-7. | Consistent (schematic only) |
| 4 | Prop thm:ms statement: quantifiers, and the W-dependence through C^k norms | 679-689 | Read; checked against its use in lines 694-771 and its proof in lines 1611-1630 | OK |
| 5 | Prime extraction eq:prime-extract: \|A_1\|² ≤ (2/J)Σ_p\|A_{p⁶}\|² + O(D²/Y²), J ≍ Y/log Y, with distinct rows of norm ≤ H | 696-725 | By hand. Exponents checked in exact rationals (C1). | OK |
| 6 | Mellin step: M_W holomorphic on Re s > 11/12; M_W = Ŵ/L_K^S for Re s > 1; contradiction at ϱ | 727-759 | By hand: Fubini for Re s > 1, Ŵ(ϱ) = ∫φ dy/y > 0, and the removed Euler factors are nonzero | OK (see N1) |
| 7 | Transfer to Dirichlet L-functions via L_K(s,χ∘N) = L(s,χ)L(s,χχ_{−3}) × (finitely many Euler factors) | 760-770 | Euler factors at split and inert primes checked by hand. The cases s = 1, χ principal, χ = χ_{−3} and imprimitive χ are all covered. | OK |
| 8 | All heights, all ν, uniformity of constants | 694-771 | Quantifier audit (Section 3.4) | OK. The theorem is qualitative, so no uniformity in ν or in the height is needed. |
| 9 | lem:arithmetic, prime case: J(χ²,χ²) = −p, γ₂(p)³ = −α(p), γ₁γ₂ = μαG | 2691-2772 | By hand, line by line. Prior numerics: all n with N(n) ≤ 50000. | OK |
| 10 | eq:convert2 for composite n | 850 / 2770-2772, 2864-2871 | Algebraic proof by twisted multiplicativity (Section 4.1). Direct summation over 337 composite n with N ≤ 2500, max error 6.6e-15 (C2). | OK |
| 11 | eq:recip, eq:quotient, and G as a class function mod 4 (ray class group mod 12) | 834-856, 2775-2862 | By hand: the quotient identity follows from R(a,a) = χ_a(−1). C2 checks G = class function for composite n. Prior numerics checked the 144 class pairs. | OK |
| 12 | eq:initial-paired-gauss: μμ conj ν(z₁)ν(z₂) γ(conj χ_{z₁}χ_{z₂}) = Σ_ξ c_ξ a_ξ(z₁) conj a_ξ(z₂) | 1063-1070 | By hand (Section 4.2). Direct Gauss sums mod z₁z₂ for 1242 ordered coprime pairs, 414 of them with a composite member, ν trivial and of order 3, max error 6.9e-15 (C3). | OK |
| 13 | lem:poisson: Poisson summation with excluded primes, its normalisation, and zero frequency | 875-932 | By hand (self-dual measure, O self-dual under e). Gaussian Φ with eight non-vacuous (χ, 𝔯) cases, including composite moduli and exclusions sharing a prime with 𝔪; errors ≤ 3e-14 (C4). | OK |
| 14 | lem:remove-exclusions | 962-992 | By hand: inclusion-exclusion, eq:crt-a, injectivity of f ↦ df, and XF preserved | OK |
| 15 | prop:poisson-reduction: expansion, extraction of g, Poisson, zero frequency Z | 1028-1060 | By hand. C6 replays steps A-D numerically. | OK |
| 16 | The same proof: Möbius conversion, insertion of v, the bijection (g,e,v,h) ↔ (b,f,k), eq:initial-column-output | 1061-1167 | By hand. Z-model of the bijection (C5). End-to-end C6 replay, max error 1.8e-14. | OK |
| 17 | The same proof: supports, dyadic scales, kernel, separation, final bound H D^{ε/2}‖W‖² | 1168-1251 | By hand (Section 4.5) | OK (see N2) |
| 18 | App. lem:smooth and lem:smooth-mean-square, as invoked at lines 1225-1234 | 3491-3615 | By hand: Mellin separation, Cauchy-Schwarz in r, convergence at q = 2m+4 | OK |
| 19 | Interface prop:canonical → eq:auxiliary-target (κ = θ/2, C₀ = 2, cases X < 1 and ℋ < 1) | 1261-1278, 1611-1630 | Parameter matching only | OK (parameters). Its proof is out of scope. |
| 20 | Referee checklist item 4: diagonal and zero-frequency terms; rows u sharing factors with n; sixth-power rows | 339-345, 1028-1060 | Section 5 | OK. All are treated exactly. |

## 2. Section 2 (outline), lines 206-658

* **Step 1 (218-237).** Smoothed Möbius sums are a valid route to zero-free regions. The precise version is in Section 3; see Section 3 below.
* **Step 2 (239-299).** The definitions agree with the precise sections. "Primary" means ≡ 1 mod 3; the six units represent (O/3)^×. In eq:intro-extraction the log Y from J ≍ Y/log Y is absorbed into D^ε. The exponents check out. With H = D^{1+θ} and Y = H^{1/6}, D^{1+ε}H^{5/6} = D^{11/6+5θ/6+ε}, and D²H^{−1/3} = D^{5/3−θ/3}. The A_1 bound is therefore D^{11/12+5θ/12+ε}, and the second term, D^{5/6−θ/6}, is always smaller (C1, exact rationals for θ = 1/10, 1/20, 1/1000).
* **Step 3 (301-349).** The Hasse/Heath-Brown identity matches eq:convert2. The classical model (−1/m) = (g/√m)² is correct for odd squarefree m. eq:intro-poisson-comparison is the B = F = 1 slice of the precise bound eq:weighted. Multiplied by D, Z ≍ H becomes the DH term, and the slice (HB/D²)·B·(XF)²·E/(XF) becomes (H/D)Σ|B_h|². ℋ ≍ D²/H is correct.
* **Steps 4-5 (351-658).** I checked only the internal algebra:
  * c_θ(nb³)χ_{nb³}(λ)² = 3^{5/2}|b|γ₂(n) for (b,λ) = 1;
  * eq:intro-cube-completion follows from |b| N(b)^{−3/2} = N(b)^{−1};
  * the Möbius inversion eq:intro-cube-inversion;
  * the condition ℋ²H_c³/X ≤ X if and only if H_c ≤ (X/ℋ)^{2/3};
  * H_c ≍ D^{2θ/3} at X ≍ D, ℋ ≍ D^{1−θ};
  * the transfer bookkeeping E(ℋ,L) ≼ X + (ℋ/L²)(YL + Y·E') with Y = XL/ℋ, which gives X + (X/L)E';
  * ℋ' = ℋ/N(b)³ < ℋ³/X² when H_c³ = X²/ℋ².

  All consistent. The analytic content (theta transformation, quadratic large sieve, transfer) is not reviewed here.

## 3. Section 3 (sec:reduction), lines 660-771

### 3.1 Prime extraction (lines 694-725)

* **χ_n(p⁶) = 1_{𝔭∤n}.** n is squarefree and prime to S, and p ∉ S. For 𝔭 ∤ n, (p⁶/n)_6 = Π_{q|n}(p/q)_6⁶ = 1. For 𝔭 | n the symbol is 0 by convention. Correct.
* **|A_1 − A_{p⁶}| ≤ ‖W‖_∞·#{n : 𝔭 | n, N(n) ≍ D}.** The count is ≪ D/N(𝔭) + 1 ≪ D/Y, because D/Y = D^{(5−θ)/6} ≥ 1. Degree-2 primes, with norm q², are allowed and harmless.
* **The averaging inequality |A_1|² ≤ (2/J)Σ|A_{p⁶}|² + 2 max|A_1 − A_{p⁶}|².** This is the elementary |x+y|² ≤ 2|x|² + 2|y|², averaged over the J primes. The rows p⁶ are distinct: unique factorisation and primary generators make p ↦ p⁶ injective. They have N(p⁶) ≤ Y⁶ = H, so they appear among the rows of eq:ms. All other rows are dropped by positivity. The review request mentions a Hölder step, but this version has none: the step is the k = 1 case of PR 910's Proposition 7.2, eq. (7.7). At k = 1 the one-shot error D/Y = D^{5/6−θ/6} is harmless, as PR 910 also notes. PR 910 needs the exact Möbius recursion only for k ≥ 2.
* **eq:prime-extract.** (2/J)·D^{2+θ+ε} ≪ D^{2+θ+ε}(log Y)/Y. Here (2+θ) − (1+θ)/6 = 11/6 + 5θ/6 and 2 − (1+θ)/3 = 5/3 − θ/3 (C1). The order of limits is legitimate: fix θ, then choose the loss in thm:ms, then rename ε.

### 3.2 Mellin contradiction (lines 727-759)

* **Ŵ(ϱ).** W(y) = y^{−ϱ}φ(y) is complex-valued, smooth, and supported in (1,2) ⊂ I = [1,2]. The statement of thm:ms allows complex W (the outline uses W ∈ C_c^∞((0,∞);C)). Ŵ(ϱ) = ∫φ(y)y^{−1}dy > 0.
* **Holomorphy of M_W.** A_1(D) is continuous in D and vanishes for D < 1/2. The bound A_1 ≪ D^{11/12+ε} for every ε gives locally uniform convergence on Re s > 11/12.
* **Termwise integration.** For Re s = σ > 1, Σ_n N(n)^{−σ}∫|W(y)|y^{σ−1}dy < ∞ justifies Fubini, and gives M_W = Ŵ(s)·Π_{𝔭∉S}(1 − ν(𝔭)N𝔭^{−s}) = Ŵ(s)/L_K^S(s,ν). The definition of L_K^S multiplies L_K by the removed factors (1 − ν(𝔭)N𝔭^{−s}), which is correct, and these factors are nonzero for Re s > 0.
* **Conclusion.** By analytic continuation, L_K^S·M_W = Ŵ on Re s > 11/12 (minus s = 1 when ν is trivial; see N1). At a zero ϱ ≠ 1 this gives 0 = Ŵ(ϱ) > 0. Correct.

### 3.3 Dirichlet transfer (lines 760-770)

χ∘N_K is a character of the ray class group mod qO, hence a finite-order Hecke character.

* **Euler factors.** At p ∤ 3q split, the factor is (1 − χ(p)p^{−s})^{−2}, which equals L_p(χ)L_p(χχ_{−3}) because χ_{−3}(p) = 1. At p inert, it is (1 − χ(p)²p^{−2s})^{−1}, which equals (1 − χ(p)p^{−s})^{−1}(1 + χ(p)p^{−s})^{−1}. The finitely many remaining factors have the form (1 − a p^{−ks})^{±1} with |a| ≤ 1. They have no zeros or poles in Re s > 0. Imprimitive χ is covered the same way.
* **A zero ϱ ≠ 1 of L(s,χ).** The other factor L(s,χχ_{−3}) has its only possible pole at s = 1. So the product vanishes at ϱ, and so does L_K(ϱ, χ∘N). This contradicts the Hecke conclusion.
* **s = 1.** If χ is not principal and not χ_{−3}-induced, then χ∘N is nontrivial, and nonvanishing at s = 1 follows from the Hecke result itself. If χ is χ_{−3}-induced, Dirichlet's theorem gives L(1,χ_{−3}) > 0, as cited. If χ is principal, s = 1 is a pole and does not need treatment.

Correct.

### 3.4 Quantifiers: all heights, all ν, uniformity of constants

* **Heights.** The contradiction fixes ϱ first. W, and with it the constant in eq:mobius-saving through ‖W‖_{C^k}, depends on ϱ. Then D → ∞. No uniformity in Im ϱ is needed, because holomorphy is qualitative, so every height is covered. PR 910 §3.2 explains why a height-dependent constant cannot be turned into a height-local improvement. That point does not affect this deduction.
* **Characters ν.** Each ν is fixed with its own S, chosen to contain the primes above 2 and 3 and those dividing the conductor of ν. Constants may depend on (ν, S, I, θ, ε). The theorem needs no uniformity in ν. Corollary cor:primes-ap (lines 84-97) claims an "absolute, effective" constant. That would follow from the exact zero-free half-plane by the explicit formula, but it is outside R1 and was not checked.
* **Derivative order.** In thm:ms, k = k(θ, ε) does not depend on I. The proof gives k = 2J(θ, ε/4) + 4 (line 1232, q = 2J + 4).

## 4. Section 4 (sec:initialization), lines 773-1252

### 4.1 Arithmetic identities (lines 795-862; proofs at lines 2689-2872)

**Prime case (lines 2691-2772).** I re-derived each step.

* **Counting identity.** #{x : 4x(1−x) = y} = 1 + χ_p³(1−y). Hence χ_p(4)J(χ_p,χ_p) = J(χ_p,χ_p³).
* **Gauss-Jacobi.** Together with γ_jγ_{−j} = χ_p(−1)^j and γ₂γ₄ = 1, it gives γ₁γ₂ = conj χ_p(4)γ₃γ₂³.
* **J(χ²,χ²) ≡ 0 mod p.** The exponents (q−1)/3 + ℓ lie strictly between 0 and q−1. N(J) = q, so J is a unit times p.
* **J(χ²,χ²) mod 3.** Π_{x≠0,1}x(1−x) = 1 forces Σj_x ≡ 0 mod 3. Then (ω−1)·3m ∈ (3) gives J ≡ q − 2 ≡ −1 mod 3, which fixes J = −p.
* **Conclusion.** γ₂³ = γ₂²/γ₄ = J/√q = −α(p).

The argument covers both split primes and inert primes −ℓ, which have residue field F_{ℓ²}.

**Composite case of eq:convert2, by twisted multiplicativity.** For coprime squarefree primary a, b, write x = x₁b + x₂a. This gives

γ_j(ab) = (χ_a(b)χ_b(a))^j γ_j(a)γ_j(b) for every j ∈ Z,

with j = −1 meaning conj χ. Write ρ = χ_a(b)χ_b(a). By eq:recip, ρ = R(a,b)χ_a(b)², so ρ³ = R(a,b)³χ_a(b)⁶ = R(a,b) because R = ±1 and χ⁶ = 1.

* **LHS(n) = μ(n)γ_{−1}(n).** Then LHS(ab) = LHS(a)LHS(b)·conj(ρ).
* **RHS(n) = χ_n(−1)G(n)^{−1}conj α(n)γ₂(n).** With G(ab) = G(a)G(b)R(a,b), α(ab) = α(a)α(b) and χ_{ab}(−1) = χ_a(−1)χ_b(−1), this gives RHS(ab) = RHS(a)RHS(b)·R(a,b)ρ².
* **The two factors agree.** conj(ρ) = R(a,b)ρ² if and only if R(a,b)ρ³ = 1, if and only if R(a,b)² = 1, which holds.

So eq:convert2 for all squarefree n follows from the prime case, eq:recip, and the multiplicativity rule for G. The same bookkeeping confirms the other CRT extensions.

* **eq:gj.** Both sides of γ₁γ₂ = μαG acquire ρ³. This holds by definition of G = conj χ_n(4)γ₃, before R is identified, so the paper's order of proof (line 2770) is legitimate.
* **γ₁γ_{−1}.** The factor ρ·conj ρ = 1.
* **γ₂(ab).** Here ρ² = χ_b(a)⁴ by cubic reciprocity, which is eq:crt-a.

C2 confirms eq:convert2 by direct summation, with no CRT, for all 337 composite squarefree n with N(n) ≤ 2500 (312 with two prime factors, 25 with three). Max error: 6.6e-15. In the same run, G = conj χ_n(4)γ₃(n) agrees with the class-mod-4 closed form conj((n mod 2) ∈ {1,ω,ω²})·Γ_quad(n mod 4). The w5copg numerics had already checked all 14120 n with N ≤ 50000. C2 uses an independent code path.

**eq:quotient (lines 2853-2862).** In the class group, G(a⁻¹) = R(a,a)/G(a) follows from G(1) = 1. Then:

* R(a,a) = χ_a(−1): for primary a, (−1/a)_6 = (−1/a)_2, and the product formula gives (−1/a)_2 = (−1,a)_2 = R(a,a). This is stated at line 2851 and checked numerically in w5copg.
* Hence G(ba⁻¹) = G(b)G(a⁻¹)R(b,a⁻¹) = χ_a(−1)conj G(a)G(b)R(a,b).

Correct. The closed form of Γ_quad (eq:quadratic-gaussian, line 2789) is Hecke's quadratic Gauss-sum reciprocity. I accepted it as classical: its proof is sketched, and both the prior numerics and C2 confirm it.

### 4.2 eq:initial-paired-gauss (lines 1063-1070)

For coprime z₁, z₂, CRT gives

γ(conj χ_{z₁}χ_{z₂}) = conj χ_{z₁}(z₂)·χ_{z₂}(z₁)·γ_{−1}(z₁)γ₁(z₂).

* **First factor.** By eq:recip, conj χ_{z₁}(z₂)χ_{z₂}(z₁) = R(z₁,z₂).
* **Second factor.** By eq:convert2, μ(z₁)γ_{−1}(z₁) = χ_{z₁}(−1)conj G(z₁)·β(z₁), where β = conj(α)γ₂.
* **Third factor.** By eq:convert1 and |γ₂| = 1, μ(z₂)γ₁(z₂) = G(z₂)conj β(z₂).
* **Assembly.** By eq:quotient, μμ γ = G(z₂z₁⁻¹)β(z₁)conj β(z₂). Then conj ν(z₁)ν(z₂)G(z₂z₁⁻¹) = conj ν(t)G(t⁻¹) with t = z₁z₂⁻¹. This is exactly the expanded function Σ_ξ c_ξ ξ(t), and ξ(z₁)conj ξ(z₂) = ξ(t).

C3 sums γ(conj χ_{z₁}χ_{z₂}) directly over a residue system mod z₁z₂ (no CRT) for 1242 ordered coprime pairs with N(z₁z₂) ≤ 1500, and evaluates G as a class function mod 4. The paired identity holds to 6.9e-15 with ν trivial and with an order-3 ray class ν of conductor (2).

### 4.3 lem:poisson (lines 875-932)

* **Self-duality.** e(z) = exp(2πi Tr(z/√−3)). The pairing (z,w) ↦ e(zw) makes O self-dual, because the inverse different is (1/√−3)O. The measure (2/√3)dx dy is self-dual and gives O covolume 1.
* **Unfolding.** Unfolding mod 𝔪 at scale ℋ/N(d) gives f̂(h/m) = (ℋ/N(d))Φ̂(ℋN(h)/(N(d)N(𝔪))).
* **Gauss sum.** For primitive χ, Σ_a χ(a)e(ah/m) = conj χ(h)·√N(𝔪)·γ(χ) holds for every h, including (h,𝔪) ≠ 1 and h = 0.
* **Zero frequency.** For χ principal and 𝔪 = 1 it equals ℋΦ̂(0)Π(1 − 1/N𝔭).

All agree with eq:poisson.

C4 checks eq:poisson to ≤ 3e-14 for a Gaussian Φ, for which Φ̂(t) = (2/√3)e^{−4πt/3}. A radial Φ makes both sides vanish identically when χ is nontrivial on O^×, so the eight test cases were chosen with χ trivial on units. They include composite moduli 𝔪 (one has three prime factors in z₁z₂), principal χ with one and two excluded primes, and an exclusion 𝔯 that shares primes with 𝔪.

### 4.4 Lemma lem:remove-exclusions (lines 962-992)

Write n = dm with d | r₀. Then a_ξ(dm) = a_ξ(d)a_ξ(m)χ_m(d)⁴ and χ_{dm}(f)⁴ = χ_d(f)⁴χ_m(f)⁴, so the sum becomes C₁(X/N(d); k, df).

* The factor χ_m(d)⁴ enforces (m,d) = 1, and χ_d(f)⁴ kills the terms with (d,f) ≠ 1.
* Cauchy-Schwarz over the τ(r₀) values of d gives the factor τ(r₀).
* f ↦ df is injective into the squarefree dyadic range [FN(d), 2FN(d)), and (X/N(d))(FN(d)) = XF.

Correct.

### 4.5 Prop prop:poisson-reduction (lines 1000-1252)

Each step was re-derived:

1. **Majorant (1023-1035).** Φ ≥ 0 is radial Schwartz, Φ ≥ 1 on [0,1], and Φ̂ has compact support. Such Φ exist: take Φ(|z|²) = c|ψ̌(λz)|² with ψ radial in C_c^∞. Then Σ_{0<Nu≤H}|A_u|² ≤ D·M_D. The sum over u runs over all of O, so units, non-primary u, u = 0 and every p⁶ are included.
2. **Common factor (1036-1042).** With g = (n₁,n₂) and n_j = gz_j: squarefreeness gives (z₁,z₂) = (z₁z₂,g) = 1, and conj χ_{n₁}(u)χ_{n₂}(u) = 1_{(u,g)=1}·conj χ_{z₁}(u)χ_{z₂}(u). The character χ = conj χ_{z₁}χ_{z₂} is primitive mod z₁z₂: it is a product of order-6 characters at distinct primes, since N(𝔭) ≡ 1 mod 6 for 𝔭 ∤ 6.
3. **Zero frequency (1054-1060).** It occurs only for χ principal, that is z₁ = z₂ = 1. Then
   Z = (H/D)Φ̂(0)Σ_g|W|²Π(1 − 1/N𝔭) ≪ H‖W‖²_∞.
   The diagonal n₁ = n₂ with h ≠ 0 is kept. These terms vanish once HN(h)/N(e) > C_Φ, which holds for large D.
4. **S_ξ (1076-1100).** The factor (1/D)·H/√(Nz₁Nz₂)·conj W·W = (H N(g)/D²)·W₀·conj W₀ with W₀(x) = x^{−1/2}conj W(x). Also χ(e)conj χ(h) = χ_{z₁}(he⁵)conj χ_{z₂}(he⁵). Both correct.
5. **Inserting v (1106-1137).** 1_{(z₁,z₂)=1} = Σ_{v|(z₁,z₂)}μ(v). With z_j = vm_j, the identity a_ξ(vm) = a_ξ(v)a_ξ(m)χ_m(v)⁴ and |a_ξ(v)χ_v(he⁵)|² = 1_{(v,h)=1} (using (v,e) = 1) give the displayed sum. The Φ̂ argument becomes HN(h)/(N(e)N(v)²N(m₁)N(m₂)).
6. **Bijection (1141-1167).** The map (g,e,v,h) ↦ (b,f,k) = (g/e, ev, eh), with inverse e = (f,k), v = f/e, g = be, h = k/e, is a bijection between:
   * {g squarefree, e | g, (g,v) = 1, h ≠ 0 with (h,v) = 1}, and
   * {b, f squarefree with (b,f) = 1, k ≠ 0}.
   It satisfies he⁵v⁴ = kf⁴, μ(e)μ(v) = μ(f), N(g)/N(e) = N(b), gv = bf, and N(e)²N(v)² = N(f)². C5 checks this in a Z-model: 278,519 sources map injectively, and the inverse is legal on 15,900 targets.
7. **Supports and scales (1168-1202).** N(b)N(f) ≤ b₀D and N(k) ≤ C_Φb₀²D²/(HN(b)²) ≤ ℋ. With X = D/(BF): r ∈ [1,4), a ≤ C_Φb₀², and the kernel is supported in [a₀/4, b₀]². These satisfy eq:initial-scales with C = C_{I,Φ}.
8. **Mean-square input (1212-1224).** Σ_{f,k}|S_U(b,f,k)|² = XF·E_{(b)} ≤ XF·τ(b)Σ_{d|b}E(ℋ, X/N(d), FN(d)) ≪ D^{ε/2}(XF)²‖U‖². The shifted scales still satisfy eq:initial-scales, because B is unchanged, F' ≥ 1, and X'F' = D/B.
9. **Separation (1225-1240).** Lemma lem:smooth-mean-square is applied with rows (f,k), w_r = 1, c_r = μ(f)1_{(f,b)=1}, I = [a₀/4, b₀] ⊂ int I_* = [a₀/8, 2b₀], and q = 2J + 4. The result is |S_{ξ;B,F}| ≪ D^{ε/2}‖W‖²_{C^q}·(2HB/D²)·O(B)·(D/B)² = D^{ε/2}‖W‖²H. Summing over the O(log² D) dyadic pairs and the finitely many ξ, and adding Z, gives M_D ≪ HD^ε‖W‖².

**End-to-end replay (C6).** Both sides of the exact identity were computed numerically:

* the left side, (1/D)Σ_{u∈O}e^{−πN(u)/H}|A_u(D)|², with u running over every u of O with N(u) ≤ 16H and W a bump on (1,2);
* the right side, Z plus eq:initial-column-output, with Σ_ξ c_ξ a_ξ(m₁)conj a_ξ(m₂) evaluated as conj ν(m₁)ν(m₂)G(m₂m₁⁻¹)β(m₁)conj β(m₂) and the k-sum running over every k ≠ 0 with N(k) ≤ 9(2D)²/H.

| D | H | ν | M_D | Z | Σ_ξ c_ξ S_ξ | abs. error |
|---|---|---|---|---|---|---|
| 30 | 6 | trivial | 0.7574802363 | 0.5009765555 | 0.25650 | 5.6e-16 |
| 30 | 6 | order 3 | 0.7521794556 | 0.5009765555 | 0.25123 | 1.1e-15 |
| 30 | 40 | order 3 | 4.3228220185 | 3.3398437033 | 0.98298 | 1.8e-14 |
| 45 | 4 | trivial | 0.5956489153 | 0.4326239083 | 0.16302 | 5.6e-16 |
| 60 | 9 | order 3 | 0.8157936237 | 0.9216711908 | −0.10588 | 3.1e-15 |

These exact identities depend on no asymptotic input. A Gaussian Φ is not the paper's Φ, because its Φ̂ is not compactly supported, but the identity is exact for every Schwartz Φ. Compact support of Φ̂ is used only in step 7, which is a support bound checked by hand.

During development, one bug was found in the review's own script: a missing factor 1/3 in the Gaussian Φ̂. It was found by replaying the intermediate forms in sequence: the u-sum, the pair sum, the Poisson form, the (g,e,h,z₁,z₂) form, the post-v form, and the (b,f,k) form. Every intermediate form agreed with M_D to ~1e-15 once the bug was fixed. No discrepancy is attributable to the manuscript.

## 5. Checklist item 4: diagonal and zero-frequency terms in eq:intro-poisson-comparison

* **Zero frequency.** h = 0 contributes only when χ = conj χ_{z₁}χ_{z₂} is principal, that is n₁ = n₂. For any nonprincipal primitive χ, conj χ(0) = 0. The principal contribution is exactly Z, including the coprimality density Π(1 − 1/N𝔭) from the exclusion (u,g) = 1. Z ≍ H is the DH term in eq:intro-poisson-comparison. It is retained, not estimated away.
* **Diagonal with h ≠ 0.** These terms are kept inside S_ξ, with v = m₁ = m₂ = 1, and bounded together with everything else. For the paper's Φ̂ they vanish for large D, since HN(h)/N(e) ≥ D^θ/b₀ > C_Φ.
* **Rows u sharing factors with n.** Factors shared with g are removed exactly by 1_{(u,g)=1} and the Möbius sum over e | g in lem:poisson. Factors shared with z₁z₂ give zero automatically through the zero extension of the primitive χ. Equivalently, the Gauss-sum identity holds for every frequency h. Dual rows k sharing factors with m_j are zero by χ_{m_j}(k) = 0. Dual rows sharing factors with f are removed by χ_m(f)⁴.
* **Sixth-power rows.** The rows u = p⁶, and more generally u = unit·w⁶, are ordinary terms of the u-sum. The Poisson identity is exact over all u ∈ O (C6), and the only inequality before the dual estimate is positivity (Φ ≥ 1 on [0,1], Φ ≥ 0). No main term is lost: a large A_1, which is what the extraction uses, would have to appear on the dual side. Whether the dual estimate eq:auxiliary-target can absorb it is exactly the content of that hypothesis. A rough sanity count is consistent with the target. Suppose the dual rows with kf⁴ a sixth power (column sum Σ a_ξ(n)U) carried a Patterson-type main term X^{5/6}. Their total contribution to E would be ≪ (ℋ/F²)^{1/6}X^{2/3} ≤ D^{5/6}, below XF. This is a heuristic remark only, not a check of Sections 5-7.

## 6. Non-load-bearing findings

* **N1 (line 752-756).** For trivial ν, L_K^S has a pole at s = 1. The identity L_K^S·M_W = Ŵ then holds on {Re s > 11/12} \ {1}, and M_W(1) = 0 is forced. The text says it holds "on Re s > 11/12". This is harmless, because a zero ϱ is never 1.
* **N2 (lines 1193-1203).** The bound sup‖K_{b,f,k}‖_{C^q} ≪ ‖W‖²_{C^q} needs t ↦ Φ̂(t) smooth with bounded derivatives on [0, 16C/a₀²], including near t = 0, because a = HN(k)/(N(f)²X²) can be as small as about D^{θ−1}. This holds because a smooth radial function of w is a smooth function of |w|² (Whitney), but the paper does not state it.
* **N3 (Sec. 2, wording).** The outline calls eq:intro-poisson-comparison and Steps 4-5 "rough". The precise statements replace them, and nothing in Sections 3-4 relies on the outline.

No error was found in the scoped lines.

## 7. What this review does not cover

* It does not review the proofs of Prop prop:canonical, prop:R, lem:cube-reduction, prop:transfer, the theta transformation (App. app:fixed-ray), the quadratic large sieve input, or Corollary cor:primes-ap and the arithmetic consequences (lines 84-125).
* The numerical checks are finite and at tiny scales. They test the conventions and the exactness of the identities. They are not evidence for eq:ms, eq:auxiliary-target, or Theorem thm:main.

## 8. Reproduction

```
cd research/exploratory/qrh-2026-10/reviews
python3 -I oct5_r1_checks.py                          # about 2 min; prints ALL CHECKS PASSED
python3 -I oct5_r1_checks.py --quick                  # smaller ranges, two C6 cases
python3 -I oct5_r1_checks.py --out /path/outside/repo.json   # optional JSON record
```
