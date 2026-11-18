# Level-2 audit of Section 6: proof of the completed mean-square estimate (Prop. 5.2)

```text
Status:      Level-2 audit of one section, done independently. It is not a review of the whole paper,
             does not certify the paper, and is not a review approval. RH remains unsolved; nothing here
             is evidence for or against the paper's global claim beyond the inspected section.
Scope:       paper2.tex l.1632-2216 (Section 6: Lemma 6.1, Prop. 6.2, Lemma 6.3, Lemma 6.4, Lemma 6.5,
             Lemma 6.6, proof of Prop. 5.2). Because Prop. 6.2 and Lemmas 6.3-6.4 are proved in App. A.2,
             we also audited l.2874-3479 (App. A.2) and the parts of App. B (Lemma B.1 l.3491-3555,
             Lemma B.3 l.3621-3648) that Lemma 6.6 invokes. Interfaces: (eq:T), (eq:completed-twist),
             Prop. 5.2 statement (l.1283-1332), outline Step 4 (l.356-421), Lemma 4.1 (eq:recip).
Exact sources: github.com/openai/math @ 4eaee87548250b2682affda7d05d947c05554bae,
             preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf
             (sha256 f919b57829b178c8e60e7c17b018cf773e7907cf642ef5a3347d8a826e8dbf18, re-hashed: matches).
             LaTeX tex1112/paper2.tex (sha256 d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d)
             is authoritative; the PDF text of Section 6 (sec_s6_completed.txt) agrees on every formula spot-checked.
             DR = Dunn-Radziwill, "Bias in cubic Gauss sums: Patterson's conjecture", arXiv:2109.07463
             (cached PDF); pages 16-18 and 77-78 were RENDERED and read as images (pdftotext drops overlines).
             GL = Goldmakher-Louvel, arXiv:1112.1642v2 (cached text): Def. 1, Thm 1.1, Cor. 1.2, Sec. 2, Sec. 5.
             Patterson [Pat77] and Kubota [Kub69] were NOT consulted directly; only through DR's transcription.
What was run: our own code only (python3 -I, numpy/scipy/sympy/mpmath); nothing from the OpenAI repository.
             experiments/code/quasi_rh/s6_*.py with saved outputs s6_*.out (Sec. 3 lists them with hashes).
             The Lean formalization of the companion 7/8 theorem was NOT replayed.
Smallest remaining gap: none found inside Section 6 / App. A.2. The section is complete GIVEN three imported
             inputs, which we checked only as stated and numerically, not by re-proof:
             (i) GL Theorem 1.1; (ii) Patterson's coefficient formula DR (5.7)-(5.8) and cusp formulas
             DR (5.13)-(5.14)/App. A table; (iii) automorphy of theta on Gamma_2 with DR's multiplier (5.4).
```

## 0. Verdict

* **verified_error:** none.
* **suspected_gap:** none.
* **unresolved_ambiguity:** none left inside the section. The four open items that the architecture map
  assigned to this region are now closed:
  * U1, the multiplier cases v_λ(c)=1 and (c,λ)=1: a hand proof is in §2.4, and an exact integer check covers
    all three cases (§3, C4).
  * U2, the cusp identification and phases: checked numerically to about 1e-14 (§2.3, C3).
  * U3, the GL hypotheses: checked against GL Def. 1 (§2.8, C6).
  * U4, the contour shift: §2.5.
* **typo_or_presentation:** six harmless items (P-S6-1 to P-S6-6, §4).
* **The decisive sign question (D1 in ARCHITECTURE.md) is settled numerically.** We evaluated Kubota's cubic
  theta function from the Patterson/DR coefficient formula DR (5.6)-(5.8) and tested its automorphy directly:
  * θ(γw) = (c/a)₃ θ(w) for γ = (a b; c d) ≡ I (mod 3), to about 1e-13 (truncation-limited);
  * the conjugate multiplier (c/d)₃ = conj (c/a)₃ is wrong by 1.73 = |1 − ω| whenever the symbol is nontrivial;
  * SL₂(Z)-invariance and periodicity under Z + 3O hold to about 1e-15.

  Three facts are used together: DR's coefficient formula, DR's multiplier, and the paper's use of the
  conjugate theta function (l.1661-1678, l.3149-3165). Together they give the exponent chain
  χ_p(h)^{-1}·χ_p(a)^{-2} = χ_p^{-3}, so B_{p,1} = χ_p³ is **quadratic**. The quadratic large sieve is
  therefore the correct tool.
* **The arithmetic of App. A.2 was checked end to end with exact integer arithmetic.** The steps covered are:
  * the reduced denominators;
  * the matrices g, H and g₁, and the claim g₁ ≡ I (mod 3);
  * the multiplier κ(g₁) = (c₁/a₁)₃, computed independently and compared with the paper's three-case formula;
  * the claim that κ₀, the cusp index σ, δ'₀ and r⁻¹ mod D₀ depend only on (h₀, A, r mod M²) (Lemma 6.3),
    tested by replacing r with primes r' ≡ r mod M² of norm about 10⁴⁷;
  * the additive CRT;
  * the summed local identity that produces the factors B_{p,j}.

  There were 0 failures in 80 configurations and 216 uniformity checks. The numerical agreement is at least
  1e-13.
* **The archimedean normalisation was checked.** The scalar is C = −(i/81)·conj(α(c))²·…, and the weight
  V_*^♯ has the gamma quotient Γ(7/6+t)Γ(5/6+t)/(Γ(7/6−t)Γ(5/6−t)) and scale (2π)⁴x/27. We re-derived both by
  hand and checked both numerically (mpmath, relative error 1e-12 to 1e-16).
* **Lemma 6.6 and the proof of Prop. 5.2 were re-derived line by line.** The bookkeeping is correct. This covers
  the decomposition s = t·k₀, the (a², Y) updates, the j_p = 4 re-indexing (also verified numerically), the
  Mellin separation, the large-sieve application, the dyadic and geometric sums, and the v-sum ζ_K(2).

Section 6 therefore proves Prop. 5.2 as stated (l.1317-1332). This holds provided GL Theorem 1.1 and the
Kubota/Patterson facts listed under "Smallest remaining gap" are correct. Those are published results, and
our numerics corroborate the second and third.

## 1. Conventions fixed before checking

* ω = e^{2πi/3}, λ = 1+2ω = i√3. An element is primary if it is ≡ 1 (mod 3).
* There are two additive characters. ĕ(z) = exp(2πi(z+z̄)) = exp(4πi Re z) is DR's character. The paper's
  character is e(z) = exp(4πi Im z/√3) = ĕ(z/λ), which is consistent with l.2902-2904. ĕ is trivial
  on λ⁻¹O, the inverse different.
* (x/π)₃ ≡ x^{(Nπ−1)/3} (mod π) and (x/π)₆ ≡ x^{(Nπ−1)/6}. These are extended multiplicatively in the
  denominator, with zero extension. We verified numerically that this is DR's convention: cubic reciprocity
  holds for 66 primary primes with norm < 200, and the supplements DR (1.5) hold, with 0 failures.
* DR (2.1): g(r,c) = Σ_{x mod c} (x/c)₃ ĕ(rx/c). Then γ₂(n) = (λ/n)₃ g(1,n)/|n|. This follows by substituting
  x = λy in γ₂(n) = N(n)^{-1/2}Σ (x/n)₃ ĕ(x/(λn)).
* DR (5.4), read on the rendered p.17: χ(γ) = (c/a)₃ for γ = (a b; c d) ∈ Γ₁(3) := {γ ≡ I mod 3} with c ≠ 0,
  extended to Γ₂ = SL₂(Z)Γ₁(3) by χ|_{SL₂(Z)} ≡ 1. Remark 5.1 of DR gives (c/a)₃ = conj (c/d)₃ = (b/d)₃.
  **The two "natural" conventions are therefore exact complex conjugates on Γ₁(3).**
* DR (5.7), rendered: τ(μ) = **conj** g(1,c) |d/c| 3^{n/2+5/2} for μ = ±λ^{3n−3}cd³ (n ≥ 0). The analogous
  conj g(ω^iλ², c) terms, with phases e^{∓2πi/9}, apply for μ = ±ω^iλ^{3n−4}cd³ (n ≥ 1). DR (5.8):
  c, d ≡ 1 (3), μ²(c) = 1, with **no coprimality of c and d**.

## 2. Claim-by-claim verification

### 2.1 Lemma 6.1 (theta realization), l.1686-1718

*Claim.* T(X;k,f) = (3^{5/2}√X)^{-1} Σ c_θ(nb³)φ_k(nb³)·conj α(nb³)·W(N(nb³)/X). Also
Θ_k = Σ_h φ̂_k(h)·conj θ(z+λ²h/q, v).

*Checks.*

1. **The coefficient of conj θ.** The coefficient of conj θ at ℓ is conj τ(−ℓ). This is because conjugation
   sends ĕ(ℓz) to ĕ(−ℓz), and τ is even (DR, below (5.8)). At ℓ = λ⁻³nb³ this coefficient equals
   3^{5/2}|b|·g(1,n)/|n|, which is 3^{5/2}|b|·conj(χ_n(λ)²)·γ₂(n). This is (eq:intro-theta-coefficients),
   l.364-366. **Numerically verified** (C5a) for 33 pairs (n,b), including (n,b) ≠ 1; the maximum error is
   3e-13.
2. **The product identity** c_θφ_k = 3^{5/2}|b|γ₂(n)Ψ_k(n)Ψ_k(b)³. It uses three facts:
   * |χ_n(λ)|² = 1;
   * χ_b(λ)⁶ = 1, valid for b coprime to λ;
   * complete multiplicativity of Ψ_k, including zero extension.

   All three hold.
3. **Substitution.** With V_*(y) = √y·W(y), substitution recovers (eq:T) exactly. We also confirmed
   conj α(nb³) = conj α(n)·conj α(b)³ and |b| = N(b)^{1/2}.
4. **Fourier inversion.** φ_k is periodic modulo some q, because (k/n)₆ is periodic in n by sextic
   reciprocity. The relation e(λ³ℓh/q) = ĕ(λ²ℓh/q) shows that the translate is by λ²h/q. Inversion uses the
   self-duality of O under e. The constant terms cancel because φ_k(0) = 0, since 0 is not ≡ 1 (mod 3).
5. **Support of the indices.** Only indices ℓ = λ⁻³m with m primary survive. Indices of the form −λ⁻³cd³,
   or with other λ-powers, are killed by φ_k, so (eq:T-theta) is exactly the conj θ-coefficient sum.

*Result:* no issue.

### 2.2 Kubota automorphy: exact law, multiplier, level (imported; used at l.3089-3101, l.3149-3165)

*What the paper uses.* The paper uses four facts:
1. θ(g₁w) = κ(g₁)θ(w) with κ(g₁) = (c₁/a₁)₃ for g₁ ≡ I (mod 3);
2. θ(γw) = θ(w) for γ ∈ SL₂(Z);
3. θ(z+t, v) = θ(z, v) for t ∈ Z + 3O;
4. the Fourier expansion (eq:cubic-theta-definition) with DR's τ.

*Exact source statements.* Facts 1, 2 and 4 are DR (5.4), the sentence following it, and (5.6)-(5.8). Fact 3
follows from 2 and the support of τ. These match the paper's transcription exactly. The level is
Γ₁(3) ⊂ Γ₂ with [Γ:Γ₂] = 27. The paper only ever applies the multiplier to g₁ ∈ Γ₁(3), and the invariances
only to SL₂(Z) and to translations. This is legitimate.

*Independent numerical test* (s6_theta_automorphy.py, s6_theta_controls.py). We built θ from DR (5.6)-(5.8)
with brute-force Gauss sums. The radius was R = 7 (1318 coefficients) or R = 9.5 (2440 coefficients).
Results:

| test | result |
|---|---|
| θ(z+1,v)=θ(z,v), θ(z+3ω,v)=θ(z,v) | rel. diff ≤ 6e-16 (and θ(z+ω) ≠ θ(z): rel. diff ≈ 1, as it must be, since T^ω ∉ Γ₂) |
| θ(Ew)=θ(w), E=(0 −1;1 0) | rel. diff ≤ 4e-15 |
| θ(γw)/θ(w) for 9 matrices γ ≡ I (mod 3), c ∈ {3, 3ω, 3+3ω, −3, 6+3ω, 3+6ω}, 2 points each | equals (c/a)₃ to ≤ 2e-13 at height 0.33 and ≤ 1.4e-8 at height 0.18 (truncation) |
| same ratio vs (c/d)₃ = conj (c/a)₃ | off by 1.73 whenever (c/a)₃ ≠ 1 |
| control A: replace conj g by g in DR (5.7) | automorphy fails at O(1) (1.9) |
| control B: drop the terms with (c,d) ≠ 1 | automorphy fails at 1.1e-2 ≫ 1e-8 |

Conclusions:
* The multiplier convention (c/a)₃ is exactly consistent with the coefficients conj g.
* The coefficient formula is correct without any (c,d)-coprimality. The cube completion (Lemma 6.1, and
  Lemma 5.3 downstream) needs exactly this (architecture item E9).
* The paper uses conj θ with multiplier conj κ (eq:theta-cusp-automorphy, l.3161-3163). This is therefore the
  correct transformation law for its coefficients γ₂(n).

*Result:* no issue. This closes the architecture's D1/E8 sign question.

### 2.3 Cusp expansions and Lemma 6.4 (support and size), l.1762-1779, l.1859-1879, l.3102-3142

*Claims.*
* The representatives are γ₀ = I, γ₊ = (1 0; ω 1) and γ₋ = (1 0; ω² 1). These are DR's γ₁, γ₁₀ and γ₁₉.
* The coefficients are t₀ = τ, t₋(ℓ) = ω²τ₁(ω²ℓ)ĕ(ℓ) and t₊(ℓ) = ωτ₂(ωℓ)ĕ(ℓ), with no constant term at
  γ_±.
* The support is ℓ = uλ^m nb³ with m ≥ −4.
* The size bound is |d(ℓ)| ≤ 27·3^{m/6}|b|.

*Source comparison.*
* DR App. A (rendered p.78) lists d₁₀(μ) = ωτ₂(ωμ)ĕ(μ) and d₁₉(μ) = ω²τ₁(ω²μ)ĕ(μ). DR (5.15) says F_j = F_j^⋆
  has no constant term for j ≥ 10. The paper's (eq:cusp-fourier-coefficients) is an exact transcription.
* In DR (5.13)-(5.14), τ₁ and τ₂ are supported only at λ-adic valuation −4, with modulus 9|d|. This gives
  |t_±| = 9|b| ≤ 27·3^{−2/3}|b|, which is about 12.98|b|.
* τ is supported on m ≡ 0 or 2 (mod 3) with m ≥ −3. We checked |τ| = 3^{k/2+2}|b| for m = 3k−4 (which is
  ≤ 27·3^{m/6}|b|), and |τ| = 3^{k/2+5/2}|b| = 27·3^{m/6}|b| for m = 3k−3, where the bound is sharp.

*Independent numerical test* (s6_theta_cusps.py). We evaluated θ(γ_±w) from the infinity expansion at the high
point γ_±w, and compared it with the series Σ t_±(ℓ)vK_{1/3}(4π|ℓ|v)ĕ(ℓz) built from DR (5.13)-(5.14). The
relative error at 3 points per cusp is ≤ 9e-15. The control (t₋ series used at γ₊) fails with relative error
1.1. All 3171 nonzero coefficients of each t_± within the radius sit at valuation −4 and have |t| = 9|b|
exactly.

*Reduction of H to γ_σ*, l.3089-3101. The cusp expansion is chosen as follows:
* H = (1 0; λ 1) gives σ = −;
* H = (1 0; −λ 1) gives σ = +;
* H = (u₀ −1; 1 0) gives σ = 0, −, + according as u₀ ≡ 0, ω, −ω modulo Z+3O.

By hand: (1 0; x 1) = E·T^{−x}·E^{−1}, and λ ≡ ω² (mod Z+3O). Also T^ωE = (−1 −1; 1 0)γ₁₉ and
T^{−ω}E = Eγ₁₀. **Numerically** (s6_theta_H_reduction.py), θ(Hw) = θ(γ_σw) to 8e-12 for 7 matrices H, and
the wrong cusp fails at relative error 0.2 to 1.3. The prose "translating by ω or −ω, then applying inversion,
gives − and +" (l.3097-3100) is consistent with this.

*Weight decay* (eq:theta-weight-decay), proved at l.3452-3472.
* The first numerator pole of the gamma quotient is at t = −5/6. Shifting to Re t = −1/4 gives x^{1/4} for
  x ≤ 1. Shifting to Re t = A gives x^{−A}.
* By Stirling, |G(t)| ≍ |Im t|^{4 Re t}. This, with the factor |t|^j from (x∂_x)^j, accounts for the
  exponent ⌈4A⌉+j+2 in (eq:ray-kernel).
* V̂_* decays rapidly, uniformly for η ∈ [−A, 1/4], because V_* = √y·W is supported in a fixed I ⊂ (0,∞).

*Result:* no issue. This closes U2. The bound x^{1/4} is not sharp (the true behaviour is x^{5/6}); see P-S6-5.

### 2.4 Prop. 6.2, arithmetic part (App. A.2, l.2906-3282)

1. **Finite Fourier expansion** (l.2906-2989). φ is periodic modulo L. This uses DR (1.5) for (λ/n)₃ and the
   conductor of Ψ₀ dividing L. We checked |φ̂(h₀)| ≤ 1 and the product expansion over P. The constant terms
   cancel because φ(0)·Πχ_p^{j_p}(0) = 0. The four cases of (eq:ray-fourier) were re-derived by hand. The
   prior agent verified them numerically (check_local.py), and our summed test (item 7) re-verifies them
   implicitly.
2. **Active primes and reduced denominator** (l.3003-3025). v_p(λ²h_p/p) = −1 when h_p ≠ 0, so the reduced
   denominator is c = c₀r up to a unit. In our construction, c₀ := c/r agreed with the reduced denominator of
   λ²h₀/L up to a unit in every test, including (h₀, L) ≠ 1 (C4).
3. **Representatives h_p ≡ 0 (mod M²)** (l.3039-3044). Changing a representative mod p changes z_h by an
   element of λ²O = 3O, under which θ is periodic. Correct.
4. **δ', b_g, and g ∈ SL₂(O)** (l.3053-3074). The CRT conditions are compatible. We checked
   c | aδ'−1, and b_g ≡ 0 or −c⁻¹ mod q^{v_q(M)} by exact assertion (C4). We also checked g₁ = gH⁻¹ ≡ I
   (mod 3) in all three cases, both by hand and by assertion.
5. **(eq:ray-multiplier), all three cases**, l.3175-3196. This is the paper's most compressed step (U1). Hand
   proofs:
   * **Case 3 | c** (H = I, g₁ = g): κ = (c/a)₃ = (c₀/a)₃(r/a)₃ = (c₀/a)₃(a/r)₃. This uses cubic
     reciprocity, with a and r primary.
   * **Case v_λ(c) = 1** (H = (1 0; u₀ 1)): g₁ = (a−u₀b_g, b_g; c−u₀δ', δ'), so a₁ = a−u₀b_g ≡ 1 (mod 3).
     The congruence a(c−u₀δ') = c·a₁ − u₀ ≡ −u₀ (mod a₁) gives κ = (−u₀/a₁)₃·conj (a/a₁)₃. Next,
     (a/a₁)₃ = (a₁/a)₃ = (−u₀b_g/a)₃ = (u₀c⁻¹/a)₃, using b_g·c ≡ −1 (mod a). Hence
     conj (a/a₁)₃ = ((c₀/u₀)·r/a)₃ = ((c₀/u₀)/a)₃·(a/r)₃. This is the claimed formula.
   * **Case (c,λ) = 1** (H = (u₀ −1; 1 0)): g₁ = (−b_g, a+b_g·u₀; −δ', c+δ'u₀), so κ = (δ'/(−b_g))₃.
     * Here δ' ≡ 0 mod λ^{v_λ(M)}, which contains 9. Hence 1−aδ' = −b_g·c ≡ 1 (mod 9), and the supplements for
       λ and ω are trivial. Reciprocity then gives (δ'/(−b_g·c))₃ = 1, which is the paper's l.3191-3196.
     * Hence κ = conj (δ'/c)₃ = conj (a⁻¹/c)₃ = (a/c)₃ = (a/c₀)₃(a/r)₃.
     * The paper leaves implicit both the step through aδ' ≡ 1 (mod c) and the fact (−1/·)₃ = 1. We supply
       both here (P-S6-1).

   **Exact check** (C4, s6_ray_multiplier_check.py). We computed κ(g₁) = (c₁/a₁)₃ with an independent
   Euclid/reciprocity algorithm, self-tested against the factorization-based symbol with 0 mismatches in
   2674 cases. It equals the paper's formula in all 80 configurations. The configurations cover:
   * L = λ⁵·8 and M = λ¹²L⁴;
   * 8 choices of h₀, giving v_λ(c₀) = 3, 2, 1, 0 and h₀ = 0;
   * 2-adic parts of c₀ equal to 1, 4 or 8;
   * active sets of 1 or 2 primes with norms 7, 13, 19 and 25 (25 being the inert prime 5);
   * j ∈ {0,1,2,3,4,5};
   * every tuple of nonzero h_p, from 6 up to 108 translates per configuration.

   Both case-2 cusps (+ and −) and the case-3 cusps 0 and − occur in the tests.
6. **Additive CRT** (eq:ray-additive-crt), l.3219-3230. It was re-derived from partial fractions
   1/(D₀r) = A/D₀ + B/r. Here ĕ(−δ'ℓ/c) depends only on δ' mod λ³c, and ε_p = −((λ³c/p)σ_p)⁻¹. Numerically, the
   maximum error was 1.6e-13 over all configurations (C4).
7. **Summed local identity.** This combines (eq:ray-fourier), conj (eq:ray-multiplier), (eq:ray-additive-crt)
   and (eq:ray-local-transform). We checked directly that
   Σ_{h_p≠0} Π_p C_{p,j_p}(h_p)·conj κ(g₁(h))·ĕ(−δ'(h)ℓ/c) = conj κ₀·ψ(λ⁴ℓ)·Π_p χ_p(σ_p)^{−2}ω_{p,j_p}B_{p,j_p}(λ⁴ℓ)
   for 12 random ℓ ∈ λ⁻⁴O per configuration. The maximum error was 6.5e-14 over 80 configurations (C4).
   **This is the identity that turns the sextic twist χ_p at p | k₀ into the quadratic χ_p³ on the dual side.
   It is now verified end to end, with the multiplier computed independently, not assumed.**

*Result:* no issue. U1 and the D6 residue are closed.

### 2.5 Prop. 6.2, archimedean part (l.3284-3436)

All of the following were re-derived by hand:
* the Mellin inversion (eq:theta-mellin-inversion), with T(s,Ψ) a product of two absolutely convergent series
  for Re s > 1;
* the derivative ∂_{z̄}ĕ(ℓz) = 2πi·ℓ̄·ĕ(ℓz);
* the Bessel integral, from DLMF 10.43.19 with μ = 2s+1, valid for Re s > −1/3;
* i·conj α(λ⁻³) = 1, since α(λ) = i;
* (eq:ray-mellin) with the constant (3^{5/2}/4)(27/(2π)²)^s;
* the coordinates (eq:theta-cusp-coordinates), via DR (5.1) applied with g⁻¹ = (δ' −b; −c a);
* the derivative factor ∂z'/∂z̄ = −1/(c²v²) with no z̄'- or v'-terms at z = 0;
* the substitution v ↦ (N(c)v)⁻¹, which gives −conj(α(c))²·N(c)^{1−2s}·J^∨(1−s);
* (eq:dual-cusp-mellin-series);
* the final scalar −i/81 = −(i/3^{5/2})·27^{−1/2};
* the kernel variable ((2π)⁴N(ℓ)X/(27N(c)²))^{−t} with t = 1/2−s.

**Numerically checked** (C5c, mpmath, 30 digits). For a single dual mode, the s-integral on Re s = −0.6, built
literally from (eq:ray-mellin), (eq:theta-mellin-functional-equation) and (eq:dual-cusp-mellin-series), equals
(−i/81)·N(ℓ)^{−1/2}·V_*^♯(N(ℓ)X/N(c)²). The relative error was 1e-12 to 1e-16 for three (N(ℓ), N(c), X)
triples.

**Entireness and contour shift (U4).**
* ∂_{z̄} kills the constant term of every translate at every cusp. The remaining modes decay exponentially as
  v → ∞ and, through (eq:theta-cusp-automorphy), as v → 0. Hence J(s) is entire.
* J(s) is in fact **bounded** on vertical strips, because |J(s)| ≤ ∫|∂Θ|v^{2σ−1}dv.
* T(s,Ψ) = J(s)/(gamma) therefore has at most e^{π|Im s|} growth in the strip, and polynomial growth on
  Re s > 1 and on Re s < 0 (functional equation plus Stirling).
* Phragmén-Lindelöf gives polynomial growth inside the strip. With the rapid decay of V̂_*, this justifies the
  shift. The paper's sketch at l.3395-3411 is correct and standard.
* After the shift, the dual series converges absolutely at Re t > 1/2, and moving each kernel to Re t = 0
  crosses no pole, since the first pole is at t = −5/6.

*Result:* no issue. |C| ≤ 1/81 holds because |φ̂(h₀)| ≤ 1, the inactive factors are 1−N(p)⁻¹ ≤ 1, and
|χ_p(σ_p)^{−2}ω_{p,j}| = 1.

### 2.6 Lemma 6.3 (uniformity in the twist), l.1847-1855, proof l.3438-3450

*Claim.* For each fixed (h₀, A_fix), the data (d_σ, ψ, c₀) depend on k₀ only through k₀ mod M². This requires
four things to be functions of (h₀, A, r mod M²) only: κ₀ = κ(g₁)/(a/r)₃, σ, δ'₀ = δ' mod D₀, and
r⁻¹ mod D₀.

*By hand.*
* a ≡ r·a₀ (mod M²), because every h_p ≡ 0 (mod M²). Hence a mod 3, which fixes H and σ, and a mod Mc₀ are
  both fixed.
* δ'₀ is fixed because D₀ = λ³c₀ divides Mc₀. At q | c₀ we have δ' ≡ a⁻¹; at q = λ ∤ c₀ we have δ' ≡ 0.
* In case 2, (−u₀/a₁)₃ depends on a₁ mod 9, and a₁ ≡ a mod λ^{v_λ(M)+1}.

*Exact check* (C4b, s6_ray_uniformity_check.py). For 8 values of h₀ and r ∈ {p₇, p₁₃, p₇p₁₃}:
* we replaced r by 3 large primes r' ≡ r (mod M²), with N(r') ≈ 10⁴⁶ to 10⁴⁸;
* for each r' we used random h ∈ (O/r')^×;
* we recomputed everything from scratch.

All 216 recomputations reproduced the same (case, σ, κ₀, δ'₀, r⁻¹ mod D₀, c₀).

The full Lemma 6.3 also needs Ψ₀ and its conductor to be fixed by the ray class of k₀. This holds because the
only k₀-dependence of Ψ₀ is through R(n, Πp^{v_p(k)}), a bicharacter on the fixed ray class group
(l.1981-1987, Lemma 4.1).

*Result:* no issue. This closes D2.

### 2.7 Lemma 6.5 versus Goldmakher-Louvel (imported), l.1886-1913

*GL statements (arXiv:1112.1642v2, read verbatim).*
* **Def. 1.** An n-th order Hecke family with respect to an ideal c is a collection
  {χ_a : a ∈ I(c), a squarefree} of primitive Hecke characters of trivial infinite type, satisfying:
  1. the order of each χ_a divides n;
  2. reciprocity χ_a(b) = χ_b(a)·C([a],[b]), through a homomorphism [·] : I(c) → G to a finite group;
  3. χ_aχ_b is primitive modulo ab when [a] = [b] and a, b are coprime.
* **Thm 1.1.** Σ*_{Na≤M}|Σ*_{Nb≤N} λ_b·χ_b(a)|² ≪_{k,c,ε} (MN)^ε (M+N)·Σ*|λ_b|², where Σ* runs over
  squarefree ideals in I(c).

*The paper's family* is χ_k(x) = (x/k)₂·κ_λ(x)^{e_k}, indexed by squarefree primary k, which is equivalent to
being indexed by squarefree ideals coprime to 6S.
* Trivial infinite type: for an imaginary quadratic field this means trivial on units. We checked this:
  (−1/k)₂ = (−1)^{(N(k)−1)/2} is corrected by κ_λ(−1)^{e_k} = −1^{e_k}, and (ω/k)₂ = 1 = κ_λ(ω).
* Primitive with conductor kλ^{e_k}.
* Order 2.
* Reciprocity: (n/k)₂(k/n)₂ depends only on (n mod 4, k mod 4). So [·] can be taken to be the class of the
  primary generator mod 24 (or mod 4), and C is constant on class pairs.
* Primitivity of products: within a class, e_{k₁} = e_{k₂}, so χ_{k₁}χ_{k₂} = (·/k₁k₂)₂ is primitive modulo
  k₁k₂.

*Numerical check (C6).* For 32 squarefree primary k with N(k) ≤ 120:
* unit-triviality: 0 failures;
* nonprimitive local factors: 0;
* reciprocity factor depending only on classes mod 4: 956 coprime pairs, 0 violations.

*Use.* (eq:Q) has the character indexed by the **outer** variable k, while GL Thm 1.1 indexes it by the
**inner** variable. Fixing the classes of k and n (finitely many) and applying reciprocity converts one form
into the other. Alternatively, the large-sieve norm of a matrix equals that of its transpose. Columns n meeting
S are handled by fixing the S-part n_S. Then (n_S/k)₂ is constant on classes of k modulo a fixed modulus
supported on S, and the remaining n' is coprime to c. The cost is O_S(1) from Cauchy–Schwarz over finitely
many pieces. Restricting the rows to a fixed ray class, or to (k₀, g) = 1, only decreases the left side.

*Result:* no issue. This closes U3. The paper does not spell out the swap of the indexing variable; see P-S6-2.

### 2.8 Lemma 6.6 (squarefree rows), l.1923-2187

The following steps were re-derived. Each passes.

* **Decomposition** s = t·k₀, with t the primes of s dividing g or lying in S (l.1940-1947). This makes k₀
  squarefree and primary, with (k₀, gS) = 1. Also N(t) ≤ H, and H₀ = H/N(t) ≥ 1 after discarding empty ranges.
* **(eq:theta-row-twist)** (l.1973-1994). For (n, kg) = 1, χ_n(p) = R(p,n)·χ_p(n) by (eq:recip). The power
  χ_n(p)⁴ carries no sign, since R = ±1. The case (n, kg) ≠ 1 is consistent through the zero-extension
  convention χ_p⁰ = 1_{p∤n}. So j_p ≡ v_p(k) + 4v_p(g) (mod 6).
  * The S-factors depend only on exponents mod 6, and χ_n(u₀) on six units. R(n,·) depends on a ray class.
    So Ψ₀ ranges over a finite family.
  * For p | k₀, j_p = 1.
  * P = P_fix ⊔ {p | k₀}, and c = c_*·k₀.
* **(eq:residual-quadratic-factor).** −1−2 ≡ 3 (mod 6), and χ_p(b)⁹ = χ_p(b)³, including when p | b.
  Π_{p|k₀} χ_p³ = χ_{k₀}³ for squarefree primary k₀.
* **The A_{u,m} normalisation.** From N(ℓ) = 3^m·N(n)·N(b)³ and |d| ≤ 27·3^{m/6}|b|, we get
  d·α·ψ/√N(ℓ) = A_{u,m}/(3^{m/3}√N(n)·N(b)) with |A_{u,m}| ≤ 27.
* **Uniqueness of the representation** ℓ = uλ^m·nb³. m = v_λ(ℓ); n and b come from the exponents mod 3; u is
  the unit making nb³ primary.
* **The j_p = 4 re-indexing identity** (l.2035-2062). We checked by hand that each of the three substitutions
  maps the V^♯-argument correctly:
  * the first term, at scale q²Y;
  * n = pn', giving scale qY with the q^{1/2} cancelled;
  * b = pb', giving scale Y/q with a leftover q^{−1/2}.

  **Numerically verified** (C5d) on random finite data: |difference| = 2.7e-16.
* **The (a², Y) bookkeeping** (l.2064-2088). The paper's table of updates is correct. Its consequences:
  * p | t, p ∉ S: j_p is odd (j_p ≡ 1+4v_p(g)), so the cost is q².
  * p | g, p ∤ t: j_p ∈ {0,2,4}. The cost is q for j ∈ {0,4}; j_p = 0 occurs only if v_p(g) ≥ 3. The cost is
    q² for j = 2, which needs v_p(g) ≥ 2.
  * Inactive primes cost 1.

  Hence a²Y ≪ (H₀²/X)·N(t)²·N(g), the initial Y has N(c₀) bounded, and Y ≪ D^{C₁}.
* **Index set** (l.2089-2093). Its size is #h₀ × 2^{#{p ∈ P_fix : j_p = 0}} × 6 × 3^{#{j_p = 4}}. This is
  divisor-bounded in tg.
* **Mellin separation** (l.2111-2133). This is Lemma B.1 with d = 1, F = V_*^♯ and argument R·y, where
  R = 3^m·U·N(b)³·H₀²/(Y·N(k₀)²) ≥ z_*, since N(b) ≥ B and N(k₀) ≤ H₀.
  * ||F||_{A,q} ≪ ||V_*||_{C^J}, from (eq:theta-weight-decay), because min(x^{1/4}, x^{−A}) ≪ (1+x)^{−A}.
  * The majorant (1+z_*)^{−A}(1+|s|)^{−2} is uniform in b, k₀, U, B and m.
  * The coefficients β(n) = A_m(n,b)·N(n)^{−1/2}·(N(n)/U)^{is} do not depend on k₀, since every k₀-dependence
    was moved into the scalars c_{ι,m}(k₀). Also Σ_{N(n)≍U}|β|² ≪ a².
* **Lemma B.3 and the Cauchy–Schwarz in b** give (eq:prepared-mean-square).
* **Removing the (H₀U)^σ factor.** U ≤ 81·Y·z_* holds because m ≥ −4 and B ≥ 1. Then
  (H₀U)^σ ≤ D^{σ(C₀+C₁)}(1+z_*)^σ, which is absorbed by (1+z_*)^{−2A} with A = 3.
* **Dyadic sums.** Σ_{U,B}(1+UB³/Z)^{−2} ≪ log²(2+Z). Also Σ√U·(1+UB³/Z)^{−2} ≪ √Z for all Z > 0: for
  Z < 1 the sum is ≪ Z² ≤ √Z, and for Z ≥ 1 it is ≪ √Z. With Z = Y/3^m, and log(2+Y·3^{−m}) ≤ log(2+81Y),
  the m-series Σ3^{−m/3} and Σ3^{−5m/6} converge.
* **Assembly.** The scalars c_{ι,m}(k₀) are bounded, so they act as bounded multipliers in ℓ²(k₀). Then
  Cauchy–Schwarz over the divisor-bounded ι gives a_ι²(H₀+Y_ι) ≤ H₀ + a²Y ≪ H/N(t) + H²N(g)/X. The sums over
  t | rad(gΠ_S p) and over the fixed ray classes are divisor-bounded and finite respectively.

*Result:* no issue. In particular D3 (a)-(f) of the architecture map are all confirmed.

### 2.9 Proof of Prop. 5.2, l.2189-2214

* k = u₀·s·v² with s squarefree is unique given the chosen generators. Since 8 ≡ 2 (mod 6),
  χ_n(v²) = χ_n(v)⁸, including the zero extension. Hence T(X; u₀sv², f) = T(X; u₀s, fv²), where g = fv² is
  allowed to be non-squarefree in Lemma 6.6.
* The row bound is H/N(v)² ≥ 1, and N(g) = N(f)N(v)² ≤ H·N(f) ≤ D^{2C₀}.
* Each v contributes (H + H²N(f)/X)/N(v)², and Σ_v N(v)^{−2} = ζ_K(2).
* Prop. 5.2's sum is over all k with 0 < N(k) ≪ H, which need not be primary or coprime to S. This is
  consistent with Lemma 6.6 allowing s to meet S.

*Result:* no issue.

## 3. Numerical checks (our own code; python3 -I; nothing from the OpenAI repository)

Directory: research/exploratory/riemann-observatory/experiments/code/quasi_rh/. Outputs are saved as *.out next
to each script.

| id | script | what it tests | range | result |
|---|---|---|---|---|
| C0 | s6_zw.py, s6_cubic_selftest.py | Z[ω] arithmetic; cubic reciprocity and DR (1.5) supplements; Euclid/reciprocity cubic-symbol algorithm vs factorization | 66 primes N<200; 2674 random (x,y) | 0 failures |
| C1 | s6_theta_automorphy.py | θ from DR (5.6)-(5.8): periodicity, E-invariance, θ(γw) = (c/a)₃θ(w) on Γ₁(3) | R=7, 1318 coefficients, heights 0.18-1.1 | ≤ 2e-13 at height ≥ 0.32; (c/d)₃ off by 1.73 |
| C2 | s6_theta_controls.py | same at R = 9.5 (2440 coefficients) plus controls A (g instead of conj g) and B (drop (c,d) ≠ 1) | 9 matrices × 2 points | positive ≤ 1.4e-8 (height 0.18); A fails at 1.9; B fails at 1.1e-2 |
| C3 | s6_theta_cusps.py, s6_theta_H_reduction.py | t_± = DR App. A d₁₀, d₁₉ via θ(γ_±w); support and size of t_±; θ(Hw) = θ(γ_σw) for 7 matrices H | 3171 coefficients each; 6 points each | ≤ 9e-15; ≤ 8e-12; controls fail at O(1) |
| C4 | s6_ray_multiplier_check.py | (eq:ray-multiplier) three cases (exact); κ₀, σ, δ'₀ independent of h_p; additive CRT; summed local identity | 80 configurations, 6-108 translates each, 12 values ℓ each | 0 mismatches; errors ≤ 1.6e-13 |
| C4b | s6_ray_uniformity_check.py | Lemma 6.3: data depend on r only through r mod M² (large primes r' ≡ r) | 216 recomputations, N(r') ~ 1e47 | 0 mismatches |
| C5 | s6_misc_checks.py | (a) Patterson coefficient identity incl. (n,b) ≠ 1; (c) archimedean constant −i/81 and V^♯; (d) j_p = 4 re-indexing | 33 pairs; 3 triples; random data | 3e-13; 1e-12 to 1e-16; 3e-16 |
| C6 | s6_misc_checks.py (b) | GL Def. 1 for the family (x/k)₂κ_λ^{e_k}: units, primitivity, reciprocity factor a function of classes mod 4 | 32 values of k, 956 pairs | 0 failures |

Script hashes (sha256) for the runs recorded in the .out files:

```text
a9029982dfeb67a2958e2a58a4419b7a92f8841caf58fb0110c7d15747d4485c s6_zw.py
5f4a11e7a5bb0abb6431da5ab6e43da9b125601ce97af977f24db6fb0400c7cd s6_theta.py
39b131aef5e361331647e4fe7fdaeabb8e2cc30919af9ac5b7caf5f79165dbe3 s6_cubic_selftest.py
8c2b459124d5d092a5421e146241e3d6dd662f26a13dc3b3475efada3090d54a s6_theta_automorphy.py
b523f9d4f69135747bd6dbb3b166b07fe874b1061a8157f68d2a6c5cac3d3f3f s6_theta_controls.py
d06e22712acf0172389c2aee0d6d4ff6cabcae1e4ccbad986135cdfacd7dc535 s6_theta_cusps.py
30fe6fec5be4d2186399b47575d4539fd5d01870ae5c8fcce8cd9c8f3d5ba049 s6_theta_H_reduction.py
d8ae82fc48edd630d0de311b12af6f3b4495eb0b6dd99dfcc6521d51e64cf34c s6_ray_multiplier_check.py
af52adeef7b42e8a25d4f319ec0b9b435017197f5db5567ed7b2946effcd1dbe s6_ray_uniformity_check.py
8398c9ddc50c69f7dd4ca3240b5366b8ee74d02eb9bf601fe1b9087b46ecb320 s6_misc_checks.py
```

These checks authenticate the arithmetic and analytic identities on the stated ranges only. The multiplier and
uniformity checks use exact integer arithmetic. The automorphy and cusp checks are floating-point evaluations
of truncated Fourier series, with truncation error estimated from K-Bessel decay. They are strong corroboration
of DR (5.4)/(5.7)/(5.13)-(5.14) and their table as transcribed, **but not a proof** of Patterson's
Theorem 8.1. GL Theorem 1.1 was not re-proved.

## 4. Findings

* **P-S6-1** (typo_or_presentation). l.3184-3196 compress the multiplier proof.
  * Case (c,λ)=1 additionally needs (−1/x)₃ = 1 and aδ' ≡ 1 (mod c), to pass from (δ'/(−b_g))₃ to (a/c)₃.
  * Case v_λ(c)=1 needs reciprocity for the two primary elements a and a₁ = a−u₀b_g.

  All the steps are supplied in §2.4(5), and the formula was checked exactly. Harmless.
* **P-S6-2** (typo_or_presentation). In l.1900-1912, Lemma 6.5 is stated with the character indexed by the outer
  variable k, while GL Thm 1.1 indexes it by the inner variable. The conversion, by reciprocity within fixed
  classes or by duality, is implicit in "after fixing … finitely many ray classes". Harmless.
* **P-S6-3** (typo_or_presentation). c₀ is introduced at l.3008-3009 as "the reduced denominator" of λ²h₀/L, which
  is defined only up to a unit. The formulas (c₀/a)₃ and ((c₀/u₀)/a)₃ in (eq:ray-multiplier) need the
  normalisation c = c₀r exactly. Any other choice multiplies κ₀ by a fixed cube root of unity that depends only
  on residues at S. Harmless, because κ₀ is only claimed to be fixed.
* **P-S6-4** (typo_or_presentation). l.3106-3113 attribute (eq:cusp-fourier-coefficients) to
  "[Pat77, Theorem 8.1 and Table III]". The formulas as written are DR's App. A table entries d₁₉ and d₁₀, which
  complete Pat77 Table III. Citation precision only; the formulas are correct (C3).
* **P-S6-5** (typo_or_presentation). The small-x bound x^{1/4} in (eq:theta-weight-decay) is weaker than the
  true x^{5/6}, which comes from the first pole at t = −5/6. It is sufficient for the use. Harmless.
* **P-S6-6** (typo_or_presentation). The counting statement "O_{Ψ₀,S}(2^{|P|}) terms" in Prop. 6.2 is
  pessimistic. Primes with j_p ≠ 0 are always active, so in the k₀-family the count is
  O(N(L)·2^{#{p ∈ P_fix : j_p = 0}}), which is independent of k₀. This is what Lemma 6.3 and l.2089-2093
  actually use. Harmless.
* **no_issue_found_in_inspected_portion:** all of Lemma 6.1, Prop. 6.2 (arithmetic and archimedean parts),
  Lemma 6.3, Lemma 6.4, Lemma 6.5 (as an application of GL), Lemma 6.6, and the proof of Prop. 5.2.

Architecture items closed by this audit: D1 (multiplier sign), D2 (uniformity in k₀), D3 (a)-(f), D4 (GL
hypotheses), D5 (Prop. 5.2), D6 (local transform), D7 (coefficients and cube completion, with the
no-coprimality point confirmed numerically), D8 (archimedean constant), U1, U2, U3 and U4.

## 5. What would still invalidate Section 6

* **A failure of an imported theorem as stated:**
  * GL Theorem 1.1 for quadratic Hecke families over Q(ω);
  * Patterson's coefficient formula, the cusp formulas, or the automorphy of θ on Γ₂ with multiplier
    χ(γ) = (c/a)₃, all as transcribed in DR §5.1 and App. A.

  Our numerics would detect a transcription error in the second group at the tested sizes, and found none. They
  cannot rule out an error in coefficients beyond N(cd³) ≈ 2400 (infinity) or 2900 (cusps γ_±).
* **Nothing in Section 6 depends on the parameter ϑ, on D beyond D^ε losses, or on any finite computation used
  as global evidence.** Prop. 5.2 is a pure L² estimate. The section's output enters the paper only through
  Lemma 5.3 and Prop. 5.1, which audit_S5.md checks at their interface.
