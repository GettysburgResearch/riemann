# Level-2 audit of Appendix A: arithmetic identities and the cubic theta transformation

```text
Status:      Level-2 audit of one appendix, done independently. It is not a review of the whole paper,
             does not certify the paper, and is not a review approval. RH remains unsolved. Nothing
             here is evidence for or against the paper's global claim beyond the inspected appendix.
Scope:       paper2.tex l.2687-3480 (App. A):
               A.1 l.2689-2872, which proves Lemma 4.1 (statement l.823-856);
               A.2 l.2874-3479, which proves Prop. 6.2, Lemma 6.3 and Lemma 6.4 (statements l.1805-1880).
             Interfaces read: definitions l.242-262 and l.306-366; (eq:T) l.1283-1316;
             Section 6 setup l.1632-1804 (theta, Theta_k, B_{p,j}, V^sharp, cusp representatives).
Exact sources: github.com/openai/math @ 4eaee87548250b2682affda7d05d947c05554bae,
             preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf
             (sha256 f919b57829b178c8e60e7c17b018cf773e7907cf642ef5a3347d8a826e8dbf18).
             LaTeX tex1112/paper2.tex (sha256 d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d,
             re-hashed here) is authoritative for formulas.
             DR = Dunn-Radziwill, arXiv:2109.07463 (cached PDF). We RENDERED pp. 17, 18 and 77-78 as
             images and read (5.4)-(5.8), (5.13)-(5.15) and the App. A table there, because pdftotext
             drops overlines. We read (1.4)-(1.5), (1.7)-(1.8) and (2.1)-(2.3) as text.
             Patterson [Pat77], Kubota [Kub69] and IK04 were NOT consulted directly.
What was run: our own code only, run with python3 -I (Python 3.13.18, sympy 1.14.0, numpy 2.5.3,
             scipy 1.18.1, mpmath 1.3.0). Nothing from the OpenAI repository was run or imported.
             The code is in experiments/code/quasi_rh/appA_*.py; outputs are in *.out (hashes in Sec. 8).
             Total: 515,936 checked cases, 0 failures.
             The code was written independently of the sibling S6 audit (s6_*.py) and of the
             architecture checks. Their results are compared only in Sec. 7.
             The Lean formalization of the companion 7/8 theorem was NOT replayed.
Smallest remaining gap: none inside App. A. The appendix is complete given the imported facts listed
             in Sec. 4: the theta coefficients, the cusp table, the automorphy of theta on Gamma_2 with
             multiplier (c/a)_3 (all as transcribed in DR, Sec. 5.1 and App. A), the Gauss-Jacobi
             identity, cubic reciprocity with its supplements, and standard analysis (DLMF 10.43.19,
             Stirling, Phragmen-Lindelof). Our numerics corroborate every one of these at the tested
             sizes. None of it was re-proved.
```

## 0. Verdict

* **verified_error:** none.
* **suspected_gap:** none.
* **unresolved_ambiguity:** none remains. The items U1 (multiplier cases) and U2 (cusp phases) of ARCHITECTURE.md
  are closed independently here: §3.5 and §3.4.
* **missing_hypothesis:** none.
* **typo_or_presentation:** seven harmless items, APPA-P1 to APPA-P7 (§6).

The main conclusions are these.

1. **Every finite arithmetic identity in A.1 holds numerically, on wide ranges, with 0 failures.** We also re-derived
   each step by hand. The identities checked are:
   * Gauss-Jacobi for all pairs of sextic characters;
   * J(χ²,χ²) = −p as an exact element of Z[ω];
   * γ₂³ = μα;
   * the proofs of (gj), (g), (convert1), (convert2) and (crt-a);
   * the quadratic Gauss sum formula, its closed form, the square-class table and the bicharacter R;
   * sextic and cubic reciprocity, and the supplements of DR (1.5);
   * χ_c(4) = (−2/c)₃ = (c/−2)₃;
   * G as a class function, G(ab) = G(a)G(b)R(a,b), R(c,c) = χ_c(−1), and (quotient).

   Inert primes (−5, −11, −17) and non-squarefree arguments are included.
2. **The arithmetic core of A.2 was checked end to end with exact integer arithmetic.** It holds in all three cusp
   cases and with the paper's own normalisation: representatives h_p ≡ 0 (mod M²), M = λ¹²L⁴. The steps checked are:
   * the reduced denominators;
   * the construction of g, H and g₁;
   * the claim g₁ ≡ I (mod 3);
   * the multiplier formula (eq:ray-multiplier) against an independent evaluation of (c₁/a₁)₃;
   * the additive CRT (eq:ray-additive-crt);
   * the local transform (eq:ray-local-transform) with the constants ω_{p,j};
   * the **summed** identity, in which the true multiplier κ(g₁) of every tuple (h_p) is summed against
     ∏C_{p,j}(h_p) and ĕ(−δ′ℓ/c). It returns exactly conj(κ₀)·ψ·∏χ_p(σ_p)⁻²ω_{p,j}B_{p,j}.

   The uniformity claimed in Lemma 6.3 also holds. κ₀, the cusp case, u₀, c₀, δ′₀ mod D₀ and r⁻¹ mod D₀ do not change
   when k₀ is replaced by primes k₀′ ≡ k₀ (mod M²) of norm up to 6·10³⁹. We repeated the whole A.2 check with an extra
   split prime in S.
3. **The sign question D1 is settled independently.** We built our own evaluator for Kubota's theta function from
   DR (5.6)-(5.8) as rendered, and found:
   * θ(γw) = (c/a)₃θ(w) on Γ₁(3), with maximal deviation 5.5·10⁻¹⁰;
   * the conjugate multiplier (c/d)₃ misses by |1−ω| = 1.732 in all 30 cases where the symbol is nontrivial;
   * the coefficient of θ̄ at λ⁻³nb³ is 3^{5/2}|b|·conj(χ_n(λ)²)γ₂(n), including when b shares primes with n.

   Combined with the exact multiplier computation, the factor at p | k₀ is
   χ_p(h)⁻¹·χ_p(a)⁻² = χ_p(σ_p)⁻²χ_p(h)⁻³, so **B_{p,1} = χ_p³ is quadratic**. This holds for every tested
   configuration.
4. **The archimedean part is correct.** We checked:
   * the Bessel-Mellin formula;
   * the derivative identities;
   * the cusp coordinates and their ∂/∂z̄ derivatives;
   * the substitution v ↦ 1/(N(c)v);
   * the full constant chain C = −(i/81)·conj(α(c))²·…, with kernel argument (2π)⁴N(ℓ)X/(27N(c)²) and gamma quotient
     Γ(7/6+t)Γ(5/6+t)/(Γ(7/6−t)Γ(5/6−t));
   * the pole structure of V^♯ and its stated decay bounds.

   The constant chain agrees to relative accuracy 6·10⁻¹⁷.

## 1. Conventions fixed before checking

* ω = e^{2πi/3}; λ = 1+2ω = √−3, so λ² = −3. An element is primary if it is ≡ 1 (mod 3). This includes the inert
  primes −q with q ≡ 2 (mod 3).
* χ_n(u) = (u/n)₆ (l.250-262). For a prime p ∤ 6, (u/p)₆ ≡ u^{(Np−1)/6} (mod p). The symbol is zero-extended and
  multiplicative in n. The cubic symbol is χ_n² and the quadratic symbol is χ_n³.
  * Our code stores values as exponents of ζ₆ = e^{iπ/3} = 1+ω.
  * Discrete logarithms were cross-checked against the defining power congruence for all residues of all primes with
    N ≤ 200.
* The paper's additive character is e(z) = exp(4πi Im z/√3) = exp(2πi Tr(z/λ)). For z = u+vω with u, v rational
  this equals exp(2πiv). O is self-dual for it.
* DR's character is ĕ(z) = exp(2πi(z+z̄)) = exp(2πi(2u−v)). We checked e(z) = ĕ(z/λ) (l.2902-2903) on 500 random
  rationals.
* DR (5.1) gives the action γw = (aw+b)(cw+d)⁻¹ on H³. DR (5.4) gives the Kubota character χ(γ) = (c/a)₃ on Γ₁(3),
  extended to Γ₂ = ⟨SL₂(Z), Γ₁(3)⟩ trivially on SL₂(Z). We confirmed this on the rendered p.17. Remark 5.1 there reads
  (c/a)₃ = conj((c/d)₃) = (b/d)₃.
* DR's Gauss sum is g(r,c) = Σ_{x mod c} (x/c)₃ ĕ(rx/c), unnormalised, by (2.1) and (5.7). Hence
  γ₂(n) = (λ/n)₃·g(1,n)/|n|. The reason is that e(x/n) = ĕ(rx/n) with r ≡ λ⁻¹ (mod n), and
  g(r,c) = conj((r/c)₃)g(1,c).

## 2. Appendix A.1 (l.2689-2872): Lemma 4.1

Lemma 4.1 (l.823-856) gives G and a symmetric ±1 bicharacter R on a fixed ray class group with (recip), (gj), (g),
(convert1), (convert2), (crt-a) and (quotient). The hypotheses are: a, b, n primary and prime to S; (a,b) = 1;
n squarefree; and a, b squarefree in (crt-a) (l.854).

| Step (line) | Restated claim | Check by hand | Numerical check |
|---|---|---|---|
| l.2695 | Fix a primary prime p ∤ 6 | "p ≡ 1 (mod 3)" means primary in O, so inert p = −q is included. The proof never uses that N(p) is prime. | All steps below were run for 74 split primes and 3 inert primes (N ≤ 400). |
| l.2700-2704 | #{x : 4x(1−x) = y} = 1 + χ_p³(1−y) | 4x(1−x) = 1−(2x−1)² and 2 is invertible mod p. | 14,309 cases (A1.count) |
| l.2705-2708 | χ_p(4)J(χ,χ) = J(χ,χ³) | Group the sum by y = 4x(1−x); Σ_y χ(y) = 0. | 77 (A1.chi4J) |
| l.2709-2715 | γ₁γ₃/γ₄ = J(χ,χ³)/√N = χ(4)γ₁²/γ₂ | Gauss-Jacobi g(A)g(B) = J(A,B)g(AB) needs AB ≠ 1; that holds here (χ⁴ and χ² are nontrivial). | Gauss-Jacobi for **all** 20 pairs (i,k) with i+k ≢ 0 (mod 6): 1,540 cases. The two instances: 77 + 77. |
| l.2716-2721 | γ_jγ_{−j} = χ_p(−1)^j for j ≢ 0 (mod 6); γ₂γ₄ = 1 | Standard; χ_p² is cubic, so χ_p²(−1) = 1. | 385 + 77; also \|γ_j\| = 1 (385) |
| l.2722-2726 | γ₁γ₂ = conj(χ_p(4))γ₃γ₂³ | From the two Gauss-Jacobi relations, using 1/γ₄ = γ₂. | 77 |
| l.2732-2746 | J(χ²,χ²) ≡ 0 (mod p) | χ²(x) ≡ x^{(q−1)/3}; Σ_{x∈F_q} x^e = 0 for 0 < e < q−1. | Vanishing power sums for every ℓ in [0,(q−1)/3] and q ≤ 200: 1,444 cases; J ≡ 0 (mod p): 77 |
| l.2747-2758 | ∏_{x≠0,1} x(1−x) = 1, Σj_x ≡ 0 (mod 3), J ≡ −1 (mod 3) | Wilson's theorem twice; ω^j ≡ 1 + j(ω−1) mod (ω−1)² = (−3ω); the term count is q−2 ≡ −1. | 77 + 77 + 77 |
| l.2759-2762 | J(χ²,χ²) = −p, exactly in Z[ω] | The norm is q and the unit is ≡ −1 (mod 3). This matches Ireland-Rosen's J(χ_π,χ_π) = π for π ≡ 2 (mod 3). | 77, exact integer pairs; also equal to the complex J (77) |
| l.2763-2769 | γ₂³ = γ₂²/γ₄ = −α(p) | — | 77 |
| l.2770-2772 | CRT extension to squarefree n: γ₂³ = μα and (gj) | Twisted multiplicativity γ_j(ab) = γ_j(a)γ_j(b)(χ_a(b)χ_b(a))^j. For j=3 this gives G(ab) = G(a)G(b)(a/b)₂(b/a)₂ consistently; for j = 2 the factor is a sixth power, hence 1. | 237 composite n (2-3 primes, N ≤ 2000): twisted multiplicativity for j = 1, 2, 3 (711); γ₂³ = μα (237); (gj) (237); (g) (237) |
| l.2773-2783 | (crt-a): a_ξ(ab) = a_ξ(a)a_ξ(b)χ_b(a)⁴ | χ_a(b)² = (b/a)₃ = (a/b)₃ = χ_b(a)² by cubic reciprocity. | 474 (with ξ ≡ 1 and ξ = conj χ_·(4)) |
| l.2786-2813 | Γ_quad(c) := \|c\|⁻¹Σ_{x mod c} e(x²/c) = ½Σ_{y mod 2} e(−cy²/4) for 2 ∤ c | Poisson summation with a Gaussian. The Fourier-transform constant \|c\|/(2√r_η), with r_η = 1 + 3N(c)η²/16, is correct for the Haar measure giving O covolume 1 (APPA-P1). The error bound O_c(η²Σ\|y\|²e^{−Cη\|y\|²}) = O_c(1), normalised to O(η), is right. | 1,618 moduli c, N(c) ≤ 700 (non-primary and λ \| c included); the stated Gaussian transform at 140 (c,η,y) points by exact complex-Gaussian algebra, plus 1 brute-force 2-D quadrature (agreement 1e-14) |
| l.2814-2827 | Closed form (1 + i^{−b} + i^a + i^{b−a})/2; depends only on c mod 4; invariant under squares; table 1, 1, i, −i at 1, −1, λ, −λ | (O/4)^× ≅ F₄^× × (1+2O)/(1+4O); the squares are F₄^×. | 1,618 + 12 + 144 + 4 |
| l.2828-2837 | R((−1)^eλ^f, (−1)^gλ^h) = (−1)^{eh+fg+fh}; symmetric bicharacter | — | 144 pairs, symmetry 144, bilinearity 1,728 triples |
| l.2838-2846 | Γ_quad(p) = γ₃(p); extends to squarefree n | Each y has 1+χ_p³(y) square roots, and Σ_y e(y/p) = 0. | 77 primes + 237 composites |
| l.2846-2848 | R(a,b) = χ_b(a)/χ_a(b) for coprime primary a, b | Γ_quad(ab) = (a/b)₂(b/a)₂Γ_quad(a)Γ_quad(b) holds for all coprime odd moduli, by CRT; the cubic part cancels by reciprocity. See APPA-P3 for non-squarefree a, b. | **29,870** ordered coprime pairs among 179 primary elements prime to 6 (N ≤ 600, non-squarefree and inert included): sextic reciprocity, cubic reciprocity, R = (a/b)₂(b/a)₂, twisted Γ_quad |
| l.2849-2852 | χ_c(4) = (−2/c)₃ = (c/−2)₃ is a character mod 2; G is a class function, G(ab) = G(a)G(b)R(a,b), R(c,c) = χ_c(−1) | (4/c)₆ = (2/c)₃ and (−1/c)₃ = 1; −2 is a primary prime; reciprocity applies. | 179 + 179 elements; G a class function mod 12 (150 composites + 77 primes); G(ab) on all 144 class pairs; R(c,c) = χ_c(−1) for 179 elements |
| l.2853-2862 | G(a⁻¹) = χ_a(−1)conj(G(a)); (quotient) | G(1) = 1 and R(a,a⁻¹) = R(a,a) = χ_a(−1). | 12 + 144 |
| l.2864-2872 | (convert1), (convert2) | They follow from (gj), from γ₁γ₋₁ = χ_n(−1), and from μ² = 1. | 237 + 237 |
| DR (1.5), used at l.2931 | (ω/d)₃ = ω^{α₂}, (λ/d)₃ = ω^{−α₃} for d ≡ 1+α₂λ²+α₃λ³ (mod 9); (λ/n)₃ periodic mod 9 | — | 179 + 179 + 179 |

**Ray class group.** G and R depend on c only through c mod 4 (Γ_quad) and c mod 2 (χ_c(4)). For primary c they
therefore factor through the ray class group mod 12. Its modulus is supported on S, as Lemma 4.1 asserts. The
relation G(n) = conj(χ_n(4))γ₃(n) for squarefree n (eq:g) is the content checked by A1.G_is_class_fn.

**Verdict on A.1:** complete and correct. Only APPA-P1 to APPA-P3 (presentation) apply.

## 3. Appendix A.2 (l.2874-3479): Prop. 6.2, Lemma 6.3 and Lemma 6.4

### 3.1 Finite Fourier expansion (l.2906-3025)

* **φ and its periodicity (l.2906-2938).** φ(n) = χ_n(λ)²Ψ₀(n)·1[n ≡ 1 (3), (n,S) = 1] is periodic mod L. This
  holds once L contains λ⁴ = 9, 2 and the conductor of Ψ₀.
  * Checked: 800 cases, for Ψ₀ trivial and for Ψ₀ = (·/−2)₃.
  * Checked: |φ̂| ≤ 1, Σφ̂ = φ(0) = 0, and Fourier inversion (120 cases).
* **(eq:ray-fourier) (l.2992-3001)** was verified against the definition of C_{p,j}(h). This covers all 44 primes
  with N ≤ 200 (split and inert), j = 0,…,5 and every h mod p: 25,464 cases.
  * Local Fourier inversion: 6,168 cases.
  * The e(−y/p) Gauss sum identity (l.2981-2986): 385 cases.
* **Nondegeneracy of (x,h) ↦ e(xh/q)** on O/q, which Fourier inversion needs: checked for six moduli q, including
  q = 18 and q = 18π₇ (375 cases).
* **The claim Θ_Ψ = Σ_h c_F(h)·θ̄(z+z_h, v) (l.2963-2980)** was verified **end to end**.
  * We evaluated both sides numerically: the left side from its defining Fourier series, the right side from
    216-252 translates of our θ evaluator.
  * Setting: Ψ = χ_p^j with N(p) = 7, j ∈ {1, 0, 4}, L = 18, at 9 points (z, v); agreement better than 1e-8.
  * The constant terms cancel because Σc_F = φ(0)∏χ_p^{j_p}(0) = 0.
* **Reduced denominator c = c₀r up to a unit (l.3009-3018), "including when (h₀,L) ≠ 1".** Checked in 3,024
  constructions, plus 8,487 with an extra prime in S. All three valuations v_λ(c₀) ∈ {0, 1, ≥2} occur.
* **Active primes (l.3003-3008).** The implication c_F(h) ≠ 0 ⇒ {j_p ≠ 0} ⊆ A(h) is immediate from
  C_{p,j}(0) = 0 for j ≠ 0.

### 3.2 Representatives, the residue of a, and δ′ (l.3039-3071)

* **Choice of representatives.** h_p ≡ 0 (mod M²) by CRT. Changing the representative mod p moves z_h by λ²O = 3O,
  under which θ is periodic (checked: periodicity under Z+3O, and its failure under ω).
* **"These choices fix the residue of a modulo Mc₀".** Proof: a = a₀r + Σ_p λ²c₀(r/p)h_p, with h_p ≡ 0 (mod M²) and
  c₀ | L | M.
  * Checked: a mod Mc₀ is independent of the nonzero residues h_p, in all 90 + 60 configurations.
  * Checked: it is fixed by r mod M² (uniformity test, §3.6).
* **δ′ and b_g.** The CRT conditions for δ′ and both congruences for b_g = (aδ′−1)/c were checked (A2.5, 3,024 + 8,487
  cases each), together with det g = 1. The extra-S run includes a prime q | M with q ≠ λ, 2.

### 3.3 The cusp choice H and g₁ ≡ I (mod 3) (l.3076-3097)

* **Hand proof.**
  * Case 3 | c: H = I and g₁ = g. Here a ≡ 1 (normalised), δ′ ≡ a⁻¹ ≡ 1 and b_g ≡ 0 (mod λ¹²), using λ | c₀.
  * Case v_λ(c) = 1: g₁ = (a−u₀b_g, b_g; c−u₀δ′, δ′). Here c ≡ ±λ (mod 3) = u₀.
  * Case (c,λ) = 1: g₁ = (−b_g, a+u₀b_g; −δ′, c+u₀δ′). Here δ′ ≡ 0 (mod λ¹²), b_g ≡ −c⁻¹ ≡ −1, and u₀ ≡ a.

  Checked: g₁ ≡ I (mod 3) in all 11,511 constructions.
* **Reduction to γ_σ using only SL₂(Z) and translations by Z+3O (l.3089-3097).** The paper leaves the assignment
  implicit (APPA-P4). It is as follows.
  * Case v_λ(c) = 1:
    * u₀ = λ: H·γ₋⁻¹ = (1 0; 2+3ω 1);
    * u₀ = −λ: H·γ₊⁻¹ = (1 0; −1−3ω 1).

    Each is E⁻¹T_{−x}E with x ∈ Z+3O. The other pairings give x ∉ Z+3O.
  * Case (c,λ) = 1: H = T_{u₀}E. Write u₀ ≡ bω mod Z+3O.
    * b ≡ 0: γ₀.
    * b ≡ 1: T_ωE = (−1 −1; 1 0)·γ₋.
    * b ≡ 2: T_{−ω}E = E·γ₊.

    This is consistent with "translating by ω or −ω, then applying inversion, gives − and +" (l.3095-3097).

  Checked by exact matrix identities (A2.11). Independently, θ(Hw) = θ(γ_σw) holds numerically at 33 points for all
  11 matrices H, to better than 1e-8.

### 3.4 Cusp coefficients (l.3098-3143), Lemma 6.4 support and size

* **Transcription.** (eq:cusp-fourier-coefficients) gives t₊(ℓ) = ωτ₂(ωℓ)ĕ(ℓ) and t₋(ℓ) = ω²τ₁(ω²ℓ)ĕ(ℓ). These are
  exactly DR's table entries d₁₀ and d₁₉ (rendered p.78), with γ₊ = γ₁₀ = (1 0; ω 1) and γ₋ = γ₁₉ = (1 0; ω² 1)
  (rendered p.18). Only the attribution to "[Pat77, Thm 8.1 and Table III]" is imprecise (P-S6-4).
* **Numerical check.** We built τ₁ and τ₂ from DR (5.13)-(5.14) as rendered. θ(γ_±w) then equals the stated series,
  with **no constant term**, at 5+5 points; relative error < 1e-7. This closes U2 independently.
* **Conjugation.** d_σ(ℓ) = conj(t_σ(−ℓ)) (l.3117-3119) is correct. Conjugating Σt(ℓ)vKĕ(ℓz) gives
  Σconj(t(−ℓ))vKĕ(ℓz).
* **Magnitudes (l.3120-3129).**
  * |t₀| = 3^{k/2+2}|b| for m = 3k−4.
  * |t₀| = 3^{k/2+5/2}|b| for m = 3k−3.
  * The m = −4 coefficients of t_± satisfy |t_±| = 9|b|.

  Hence |d(ℓ)| ≤ 27·3^{m/6}|b|, with equality exactly when m ≡ 0 (mod 3), and 9 ≤ 27·3^{−2/3} ≈ 12.98.
  * Checked: 2,688 coefficients of d₀ (max ratio exactly 1.000000) and 3,540 of d_±.
  * Checked: support m ≥ −4, with m = −4 for d_±.

### 3.5 The multiplier (eq:ray-multiplier) (l.3149-3206). Closes U1

The automorphy law used is θ(g₁w) = κ(g₁)θ(w) with κ(g₁) = (c₁/a₁)₃ for g₁ ≡ I (mod 3). This is DR (5.4) as rendered.
Our θ evaluator confirms it: 42 matrices γ ∈ Γ₁(3) at heights 0.19-0.33, 30 of them with a nontrivial symbol,
maximal deviation 5.5·10⁻¹⁰. The conjugate (c/d)₃ is off by 1.732 in each of those 30 cases. SL₂(Z)-invariance and
periodicity under Z+3O hold to better than 1e-9.

Hand derivation of the three cases. The paper (l.3184-3196) gives only the congruences. Here c = c₀r is normalised as
in l.3047-3049, and r is primary.

* **3 | c.** κ = (c/a)₃ = (c₀/a)₃(r/a)₃ = (c₀/a)₃(a/r)₃, by reciprocity for primary a and r.
* **v_λ(c) = 1.**
  * a(c−u₀δ′) = c(a−u₀b_g) − u₀, so a·c₁ ≡ −u₀ (mod a₁) with a₁ = a−u₀b_g.
  * Hence (c₁/a₁)₃ = (−u₀/a₁)₃·conj((a/a₁)₃).
  * Reciprocity for the primary elements a and a₁ gives (a/a₁)₃ = (a₁/a)₃ = (−u₀b_g/a)₃.
  * From b_gc ≡ −1 (mod a): conj((a/a₁)₃) = ((c/u₀)/a)₃ = ((c₀/u₀)/a)₃(a/r)₃.
* **(c,λ) = 1.**
  * κ = (−δ′/−b_g)₃ = (δ′/−b_g)₃.
  * Since −b_gc = 1−aδ′ ≡ 1 (mod 9) and ≡ 1 (mod δ′), the supplements of DR (1.5) and reciprocity give
    (δ′/−b_gc)₃ = 1.
  * Hence (δ′/−b_g)₃ = conj((δ′/c)₃) = (a/c)₃, using aδ′ ≡ 1 (mod c), and (a/c)₃ = (a/c₀)₃(a/r)₃.

Exact check: κ(g₁) = (c₁/a₁)₃ was evaluated by a reciprocity-based algorithm. That algorithm was itself validated
against the defining power-residue symbol on 3,000 random cases. It agrees with the paper's three-case formula in all
3,024 + 8,487 constructions (1,008 + 2,829 per case). We also checked the auxiliary congruences:
* a(c−u₀δ′) ≡ −u₀ (mod a₁) and b_gc ≡ −1 (mod a);
* −b_gc = 1−aδ′ ≡ 1 (mod 9);
* (δ′/−b_gc)₃ = 1.

**κ₀ is fixed.** κ₀ is independent of the nonzero h_p (90 + 60 configurations). Its sign convention makes
conj(κ) ∝ ∏χ_p(a)⁻², which is the source of the quadratic factor.

### 3.6 Additive CRT, local transform, summed identity and uniformity (l.3207-3282, l.3438-3450)

* **(eq:ray-additive-crt).** We re-derived it by partial fractions of −δ′/(D₀r) with D₀ = λ³c₀, using
  δ′ ≡ (σ_ph_p)⁻¹ (mod p). This gives ε_p = −((λ³c/p)σ_p)⁻¹.
  * Checked a ≡ σ_ph_p (mod p): 5,238 + 16,020 cases.
  * Checked the CRT identity for all tuples at 40-50 frequencies x = λ⁴ℓ, including x divisible by active primes:
    42,606 + 33,264 cases.
  * δ′ mod D₀ and r⁻¹ mod D₀ are independent of the h_p.
* **(eq:ray-local-transform) with ω_{p,j}.**
  * j ∉ {0, 4}: the Gauss sum of χ^{j+2} gives ω_{p,j} = χ(−1)^jγ_jγ_{j+2}χ(ε_p)^{−j−2} and B_{p,j} = χ^{−j−2}.
    At p | x both sides vanish, because j+2 ≢ 0 (mod 6).
  * j = 4: the factor is χ(h)⁻⁶ = 1, and Σ_{y≠0} e(yx/p) = −1 + N·1[p|x], giving ω = γ₄.
  * Active j = 0: ω = −γ₂χ(ε_p)⁻² and B = N^{−1/2}χ⁻².
  * Checked with the **actual** σ_p and ε_p of each construction, for every x mod p sampled and every j ∈ {0,…,5}:
    5,481 + 3,654 cases. Also |ω_{p,j}| = 1.
  * B_{p,1} = χ_p³ is real, quadratic and zero-extended (702 + 900 cases).
* **Summed identity (the decisive end-to-end check).** For each (h₀, A) we computed

  S(x) = Σ over all tuples (h_p)_{p∈A}, h_p ≠ 0, of ∏C_{p,j_p}(h_p)·conj(κ(g₁(h)))·ĕ(−δ′_h x/(λ⁴c)),

  with every tuple's own a, δ′ and g₁. We compared it with conj(κ₀)ψ(x)∏_p χ_p(σ_p)⁻²ω_{p,j_p}B_{p,j_p}(x).
  * Result: agreement in 4,158 + 2,772 cases, to better than 1e-8.
  * Coverage: single primes with j = 0,…,5, two-prime active sets (j = (1,1), (1,4), (0,1)) and an inert prime
    (N = 25).
  * The sum includes the multiplier cases v_λ(c) = 1 and (c,λ) = 1, which the architecture map had left unverified.
* **Lemma 6.3 (l.3438-3450).** Primes dividing k₀ have j = 1, so they are active and r = k₀·∏A_fix. We then replaced
  k₀ by primes k₀′ ≡ k₀ (mod M²).
  * The k₀′ are primary primes with N(k₀′) up to 1.05·10³⁴ (L = 18) and 6.1·10³⁹ (L = 18π₇).
  * In 18 + 9 classes, the tuple (κ₀, cusp case, u₀, c₀, δ′₀ mod D₀, r⁻¹ mod D₀) is identical across each class.
  * So d = d_σ, ψ and c₀ depend on k₀ only through k₀ mod M², as claimed. The scalar C may depend on k₀; only
    |C| ≤ 1/81 is used.

### 3.7 Archimedean part (l.3284-3437) and the kernel bound (l.3452-3479)

| Item (line) | Check |
|---|---|
| (eq:theta-mellin-inversion) l.3296-3300 | Mellin inversion by hand. V_*(N(n)N(b)³/X) = (1/2πi)∫V̂_*(w)N(n)^{−w}N(b)^{−3w}X^w dw; s = w+½ gives N(n)^{−s}N(b)^{−3s+1/2}X^{s−1/2}. T(s,Ψ) converges absolutely for Re s > 1, and its b-factor for Re s > ½. |
| (eq:fourier-derivative) l.3320 | ∂_{z̄}ĕ(ℓz) = 2πiℓ̄ĕ(ℓz) and ∂_zĕ(ℓz) = 2πiℓĕ(ℓz), checked by finite differences (50+50). |
| (eq:bessel-mellin) l.3321-3323 | DLMF 10.43.19 with μ = 2s+1, checked with mpmath to 1e-15 at 8 points with Re s > 0, and to 1e-8 at s = −0.2, where quadrature accuracy is limited. It is valid for Re s > −⅓; the paper states only Re s > 0, which is enough. |
| Termwise integration, l.3326-3330 | Σ\|coef(ℓ)\|·\|ℓ\|^{−2σ} ≍ Σ_{n,b}\|b\|N(n)^{−σ}N(b)^{−3σ} < ∞ for σ > 1. |
| Phase and scale, l.3331-3337 | i·conj(α(ℓ))\|ℓ\|^{−2s} = 27^s·conj(α(n))·conj(α(b))³N(n)^{−s}N(b)^{−3s}, using α(λ⁻³) = i: 200 random cases. |
| (eq:ray-mellin) l.3339-3343 | The constant 2πi·2^{2s−1}/(4π)^{2s+1} = i/(4(2π)^{2s}) was checked. With the coefficient identity, the constant is (3^{5/2}/4)(27/(2π)²)^s. |
| Coefficient identity used here (eq:intro-theta-coefficients) | conj(τ(−λ⁻³nb³)) = 3^{5/2}\|b\|·conj(χ_n(λ)²)γ₂(n) holds in 434 cases, including b sharing primes with n. DR (5.8) imposes no coprimality between c and d. |
| Cusp coordinates (eq:theta-cusp-coordinates) l.3166-3170 and derivatives l.3347-3358 | Checked from DR (5.1) for 100 random g ∈ SL₂(O): ∂z′/∂z̄ = −1/(c²v²), ∂z̄′/∂z̄ = 0 and ∂v′/∂z̄ = 0 at z = 0, all by finite differences. Hence the derivative is −(cv)⁻²∂_{z′} and there is no height term. |
| Entireness of J(s), l.3359-3369 | ∂_{z′} removes the constant mode of every cusp expansion. At γ₀ the constant σv′^{2/3} does not depend on z′; at γ_± there is no constant term (checked, §3.4). Each translated integral converges for every s, so splitting the finite h-sum is legitimate. |
| (eq:theta-mellin-functional-equation) l.3382-3386 | ∫v^{2s−3}F(1/(N v))dv = N^{2−2s}∫u^{1−2s}F(u)du (mpmath, 4 cases), and c⁻²N(c)^{2−2s} = conj(α(c))²N(c)^{1−2s} (100 cases). |
| (eq:dual-cusp-mellin-series) l.3389-3394 | Same constant as (eq:ray-mellin), with ∂_z in place of ∂_{z̄}, which gives α(ℓ) in place of conj(α(ℓ)). |
| Contour shift, l.3395-3411 | J(s) is bounded on vertical strips, so T = J/K has finite order. T is polynomially bounded on Re s = 1+ε (absolute convergence) and on Re s = −ε (functional equation plus Stirling, since the gamma ratio is polynomial). Phragmen-Lindelof then applies. Standard and correct. |
| Scalar C and kernel, l.3413-3437 | With s = ½−t and ds = −dt (orientation preserved), the per-ℓ integrand equals (−i/81)·conj(α(c))²·Γ-quotient(t)·((2π)⁴XN(ℓ)/(27N(c)²))^{−t}N(ℓ)^{−1/2}·V̂_*(−t). Checked at 20 random (s, X, N(c), N(ℓ)); maximal relative deviation 5.6e-17. Then \|C\| ≤ 1/81 because \|φ̂\| ≤ 1, \|1−1/N\| ≤ 1 and the remaining factors have modulus 1. |
| Poles and kernel bounds (eq:ray-kernel) | The first numerator pole is at t = −5/6, and 1/Γ is entire. On Re t = η the gamma quotient grows like \|u\|^{4η} (slope checked at η = −¼, ½, 2). For an explicit test function (log-Gaussian; it is not compactly supported and serves only for the contour statements): V^♯ is the same on Re t = −¼, 0, ½, 2; V^♯(x) = Res_{t=−5/6} + O(x^{7/6}) as x → 0, so \|V^♯\| ≪ x^{5/6} ≤ x^{1/4} (APPA-P7); \|V^♯(x)\| ≤ C_A x^{−A} for A = 1, 4 with the constants C_η of (eq:ray-kernel). |

The ℓ-sum converges absolutely at Re t > ½: Σ|d(ℓ)|N(ℓ)^{−1/2−t₀} converges, because its n-part needs t₀ > ½ and
its b-part and λ-part converge. The interchange with the t-integral and the per-ℓ shift to Re t = 0 are therefore
legitimate.

**Verdict on A.2:** complete and correct as a derivation from the imported facts of Sec. 4.

## 4. Imported results, checked against their exact original statements

| Import | Where used | Exact form in the source | Status |
|---|---|---|---|
| Gauss-Jacobi g(A)g(B) = J(A,B)g(AB) for AB ≠ 1 [IK04 (3.18)] | l.2709 | IK04 not consulted. | Verified numerically for all 20 character pairs at 77 primes (1,540 cases). |
| Hasse, HB00 (2); DR (2.2), (1.8): g̃(c)³ = μ(c)c/\|c\| | Consistency of γ₂³ = μα | DR (1.8) and (2.2), read as text. | Consistent: γ₂ = (λ/n)₃g̃(n). The paper re-proves the fact (l.2728-2772). |
| Cubic reciprocity DR (1.4); supplements DR (1.5) | l.2847, l.2931, l.3184-3196 | (a/b)₃ = (b/a)₃ for a, b ≡ 1 (3); for d ≡ 1+α₂λ²+α₃λ³ (mod 9): (ω/d)₃ = ω^{α₂}, (λ/d)₃ = ω^{−α₃}. | Verified: 29,870 pairs; 179 + 179 elements. |
| Kubota character DR (5.4); Patterson's extension to Γ₂, trivial on SL₂(Z) | l.3089-3092, l.3150-3156 | Rendered p.17: χ(γ) = (c/a)₃ on Γ₁(3), c ≠ 0; Remark 5.1: (c/a)₃ = conj((c/d)₃) = (b/d)₃. | Verified numerically, including rejection of the conjugate (§3.5). The citation "(5.4), (5.6)": (5.6) is σ (APPA-P5). |
| θ expansion and τ, DR (5.6)-(5.8) [Pat77 Thm 8.1] | (eq:cubic-theta-definition), (eq:intro-theta-coefficients), (eq:ray-mellin) | Rendered p.17: σ = 3^{5/2}/2; τ(±λ^{3n−3}cd³) = conj(g(1,c))·\|d/c\|·3^{n/2+5/2}; the λ^{3n−4} rows carry conj(g(·λ²,c)) with phases e^{∓2πi/9}; c, d ≡ 1 (3), μ²(c) = 1, no coprimality. | Our θ built from it is automorphic, so the transcription is consistent. The paper's coefficient identity holds (434 cases). |
| Cusp data DR (5.9)-(5.15), App. A table (d₁₀, d₁₉) | (eq:cusp-fourier-coefficients) | Rendered pp. 18, 78. | Transcribed exactly; verified numerically (§3.4). |
| DR (5.1) action on H³ | (eq:theta-cusp-coordinates) | Read as text: γw = ((az+b)conj(cz+d) + a·conj(c)v², v)/(\|cz+d\|² + \|c\|²v²). | Used and verified. |
| DLMF 10.43.19 | (eq:bessel-mellin) | ∫t^{μ−1}K_ν(t)dt = 2^{μ−2}Γ((μ−ν)/2)Γ((μ+ν)/2) for Re μ > \|Re ν\|. | Verified. |
| Stirling [IK04 §5.A.4]; Phragmen-Lindelof [IK04 Thm 5.53] | l.3395-3411, l.3458-3476 | Standard. | Hypotheses (finite order, polynomial bounds on the boundary lines) checked in §3.7. |
| DR Cor. 5.1, Props. 5.1-5.3 (template) | l.3031-3037 | The case (h₀, L) ≠ 1 and several simultaneous active primes are new work in the paper. | Audited as new work in §§3.1-3.6; no reliance on DR beyond the facts above. |

## 5. Numerical checks (all ours; 0 failures)

| Script (output) | Identities | Ranges | Cases |
|---|---|---|---|
| appA1_identities.py (.out) | Everything in §2 | Primes: N ≤ 400 (77, including inert 5, 11, 17). Composites: 237 squarefree, N ≤ 2000. Reciprocity: 179 primary elements, N ≤ 600 (29,870 pairs). Γ_quad: 1,618 moduli, N ≤ 700. All 12 classes of (O/4)^×. | 148,857 |
| appA2_arith.py (.out), L = 18, S = {λ, 2} | φ periodicity, (eq:ray-fourier), reduced denominators, g, H, g₁, (eq:ray-multiplier) in 3 cases, κ₀ independence, additive CRT, local transform, summed identity, H → γ_σ matrices, Lemma 6.3 uniformity | 90 configurations (3 valuations × 3 h₀ × 10 prime/exponent patterns, primes of norm 7, 13, 19, 25); 3,024 constructions; k₀′ up to N ≈ 1.05e34 | 135,849 |
| appA2_arith.py with APPA_EXTRA_S=1 (appA2_arith_extraS.out), L = 18π₇ | Same, with an extra prime of S in M (active primes of norm 31, 13, 19, 25) | 60 configurations; 8,487 constructions; k₀′ up to N ≈ 6.1e39 | 217,011 |
| appA2_theta.py (.out) | Own θ from DR (5.6)-(5.8): coefficient identity; automorphy (c/a)₃ against (c/d)₃; Z+3O periodicity and E-invariance; θ(Hw) = θ(γ_σw); cusp expansions at γ_±; support and coefficient bounds; end-to-end Θ_Ψ = Σc_F·θ̄(z+z_h) | 2,688 coefficients with \|μ\| ≤ 10; 5,934 cusp indices; heights ≥ 0.186 | 13,345 |
| appA2_archimedean.py (.out) | §3.7 | mpmath at 30 digits and double precision | 874 |

These checks authenticate the finite arithmetic and the stated analytic identities on the tested ranges only.
* The automorphy and cusp-expansion checks are floating-point evaluations of truncated Fourier series. They strongly
  corroborate DR's transcription of Patterson's theorem, but they are **not a proof** of it.
* The multiplier, denominator, CRT and uniformity checks use exact integer arithmetic. The phases are evaluated in
  floating point from exact rationals.

## 6. Findings

| ID | Location | Classification | Statement |
|---|---|---|---|
| APPA-P1 | l.2793-2797 | typo_or_presentation | The Fourier transform \|c\|/(2√r_η)·exp(−πηN(c)\|y\|²/(4r_η))·e(−cy²/(4r_η)) does not name its measure. It is correct for the Haar measure giving O covolume 1, where Poisson reads Σ_O f = Σ_O f̂. With Lebesgue measure the prefactor is √3\|c\|/(4√r_η) and Poisson carries a factor 2/√3. The product is the same, and (eq:quadratic-gaussian) is verified directly. Harmless. |
| APPA-P2 | l.2695 | typo_or_presentation | "primary prime p ≡ 1 (mod 3)" could be misread as a rational prime ≡ 1 (mod 3), that is, split primes only. Lemma 4.1 is used for all primes outside S, inert ones included. The proof works verbatim for p = −q with N(p) = q², and every step was verified for q = 5, 11, 17. Harmless. |
| APPA-P3 | l.2846-2848 | typo_or_presentation | R = χ_b(a)/χ_a(b) is derived through γ₃, which is defined only for squarefree arguments. (eq:recip) allows non-squarefree coprime a, b. That case follows at once by bimultiplicativity from the prime case, or from twisted multiplicativity of Γ_quad for all coprime odd moduli. Verified on 29,870 pairs including non-squarefree ones. Harmless. |
| APPA-P4 | l.3083-3097 | typo_or_presentation | The cusp index σ selected by H is left implicit. Explicitly: u₀ = λ → γ₋ and u₀ = −λ → γ₊; in the case (c,λ) = 1, u₀ ≡ 0, ω, −ω mod Z+3O → γ₀, γ₋, γ₊ (§3.3). Verified by matrix identities and numerically. Harmless. |
| APPA-P5 | l.3156 | typo_or_presentation | The citation "[DR, (5.4), (5.6)]" for κ: (5.6) defines σ = 3^{5/2}/2. Harmless. |
| APPA-P6 | l.3184-3196 | typo_or_presentation | The multiplier proof gives only the congruences. Two steps are left to the reader: for (c,λ) = 1, the passage (δ′/−b_g)₃ → (a/c)₃ via aδ′ ≡ 1 (mod c); for v_λ(c) = 1, reciprocity for a and a₁ = a−u₀b_g. Both are supplied in §3.5 and checked exactly. This is the same observation as P-S6-1, reached independently. Harmless. |
| APPA-P7 | (eq:ray-kernel), (eq:theta-weight-decay) | typo_or_presentation | The small-x bound x^{1/4} is weaker than the truth: V^♯(x) = c·x^{5/6} + O(x^{7/6}), from the first pole at t = −5/6. It is sufficient for the use. Same as P-S6-5; confirmed numerically. Harmless. |
| — | All other steps of l.2689-3479 | no_issue_found_in_inspected_portion | See the step-by-step record in §§2-3. |

## 7. Comparison with the architecture map and the sibling S6 audit

* **Architecture items closed or confirmed by this independent audit:**
  * D1 (multiplier sign; B_{p,1} quadratic);
  * D2 (uniformity in k₀, with huge k₀′);
  * D6 (finite Fourier expansion, active primes, local transform with the actual σ_p, ε_p);
  * D7 (coefficient identity, no coprimality between n and b);
  * D8 (archimedean constants, entireness, gamma quotient);
  * U1 (multiplier cases v_λ(c) = 1 and (c,λ) = 1: hand proof plus exact check);
  * U2 (cusp phases t_±: numerical check of θ(γ_±w));
  * U4 (contour shift: hypotheses of Phragmen-Lindelof checked; V^♯ contour independence checked numerically).
* **Agreement with audit_S6.md.** That audit also covered App. A.2. On every overlapping point we reach the same
  conclusions with separately written code: the automorphy multiplier, the cusp expansions, the multiplier formula,
  uniformity and the archimedean constants. Two of our observations repeat S6's: APPA-P6 = P-S6-1 and APPA-P7 = P-S6-5.
  Beyond S6, this audit adds:
  * all of A.1 (Lemma 4.1), which S6 did not audit;
  * the summed identity computed with the true per-tuple multipliers;
  * the end-to-end identity Θ_Ψ = Σc_F·θ̄(z+z_h);
  * a run with an extra prime in S;
  * k₀′ up to N ≈ 6·10³⁹.

## 8. What would still invalidate App. A, and reproduction

**Smallest statements whose failure would invalidate App. A:**
* In the imported layer: the automorphy θ(g₁w) = (c₁/a₁)₃θ(w) on Γ₁(3), together with the coefficient formula
  DR (5.7)-(5.8) and the cusp table entries d₁₀, d₁₉ in DR's conventions. If, say, the true multiplier were
  conj((c/a)₃) for this θ, then B_{p,1} would become sextic, Lemma 6.5 would not apply, and Prop. 5.2 would lose its
  proof.
* In the paper's own layer: (eq:ray-multiplier) together with (eq:ray-local-transform). Both were verified exactly.

Our numerics corroborate the imported layer at the tested sizes:
* coefficients up to |μ| ≤ 10, i.e. N(λ³μ) ≤ 2700;
* cusp indices up to |μ| ≤ 4.5;
* 42 automorphy matrices.

They cannot exclude an error in Patterson's theorem beyond those sizes. Such an error would contradict a published
theorem that has been used in the literature since 1977.

Reproduction (python3 -I, from experiments/code/quasi_rh/):

```text
sha256
39b086c2c6b61a89a42a596b7ff15f878eed50377cb799d5f87babc834fa8f7f  appA_zw.py
b3134a57ef5a54b6ae59be3511c09f4c5d6ecab4ad713f568bfbef97b0707d94  appA1_identities.py
f949fe9b93f5996cb68e7d2a480ae0ca6f726fd2247b3e147f6f72345fece11c  appA2_arith.py
47ca18bc5260ea75eaed43dbe79959529ebcbf341e58126aa2291e02e4460ab5  appA2_theta.py
5ce397d31b36b921a9cdd1ee6535f14ecea695b19db1fe2f9356feb8edae674f  appA2_archimedean.py
6fa80b26cebc5eac97c4a0d53fbf11d3edff136393c8647ff8462d753b487769  appA1_identities.out      (148,857 cases, 0 failures, ~80 s)
c701119dd6a148b91c44a0e4f86d8fb7dfdcf644dd112f0e3721bb95e34f99ca  appA2_arith.out           (135,849 cases, 0 failures, ~40 s)
2bcb542bca7b3fb781cb1a49b31157e0ff39c566fc755897bc4750572c60a42f  appA2_arith_extraS.out    (217,011 cases, 0 failures; APPA_EXTRA_S=1)
90ceff738c065260dd3a5f90d8f3a8bf04a7687aea31b188c3c22e160057f3af  appA2_theta.out           (13,345 cases, 0 failures, ~30 s)
6059330c5934e3ab49882d2115eb8412fdf39685655e97a7708218ba4c7f3e40  appA2_archimedean.out     (874 cases, 0 failures, ~10 s)
```

Test bugs fixed during the audit (none affects the paper):
* A sextic/cubic exponent mix-up in our own χ_c(4) test.
* A double normalisation of γ_j in our own ω_{p,j}.
* A mis-specified nondegeneracy test.
* A floating-point cancellation in a V^♯ contour comparison, replaced by an error-aware comparison.
* A truncation radius for θ that was too small at height 0.19 (R = 7 → 10).

After each fix the corresponding identity held exactly as the paper states it.
