# Level-2 audit of Section 3: from Proposition 3.1 to Theorem 1.1

```text
Status: Level-2 audit of one section, done independently. It is not a review of the whole paper and does not certify the paper.
Scope: paper2.tex l.660-772 (Section 3). Also read: Theorem 1.1 (l.71-74), outline Steps 1-2 (l.212-303),
       the interface with Prop. 4.5 (l.1000-1034) and with the completion of Prop. 3.1 (l.1611-1629).
Exact sources: github.com/openai/math @ 4eaee87548250b2682affda7d05d947c05554bae,
       preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf
       (sha256 f919b57829b178c8e60e7c17b018cf773e7907cf642ef5a3347d8a826e8dbf18, re-hashed here);
       LaTeX source tex1112/paper2.tex (3988 lines) is authoritative for formulas. The PDF text of Section 3
       (sec_s3_deduction.txt) was compared with the tex and matches.
What was actually run: our own script
       research/exploratory/riemann-observatory/experiments/code/quasi_rh/s3_deduction_checks.py
       (sha256 27ac6112...e7f), run with python3 -I. Its output is in s3_deduction_checks.out in the same folder.
       No code from the OpenAI repository was run. The Lean formalization of the 7/8 companion was NOT replayed.
Smallest remaining gap: none inside Section 3. Section 3 is a complete conditional deduction:
       Proposition 3.1 => Theorem 1.1. All mathematical risk sits in Proposition 3.1 (Sections 4-7, Apps. A-B),
       which this audit does not address.
```

## 0. Verdict

Section 3 is **correct as a conditional deduction**. Every step checks once the following are granted:

1. Proposition 3.1 (l.679-689), with its stated quantifiers;
2. three standard imported facts:
   - Landau's prime ideal theorem for the fixed field K;
   - Hecke's meromorphic continuation for ray class L-functions of K;
   - L(1, χ₋₃) > 0.

The final quadratic base-change step is a standard Euler-factor identity. It is uncited in the paper. We checked it coefficient by coefficient.

- We found no verified error, no suspected gap and no missing hypothesis.
- Three presentation points are recorded (F1-F3), all harmless.
- The pole at s=1 and every character type are handled correctly.
- No uniformity in the conductor is needed. Over the imaginary quadratic field K, finite order forces a trivial infinity type.

## 1. Claim-by-claim verification

Notation: N = N_{K/Q}, and O = Z[ω]. "Rows" u are **elements** of O, not ideals. This is confirmed by the outline (l.268, "parametrized by u ∈ O_K") and by the proof of Prop. 4.5 (l.1032, Σ_{u∈O}). It must be so, because χ_n(u) = (u/n)_6 depends on the unit class of u.

### S3.0 Setup (l.665-677)
- **Restated:**
  - ν is a finite-order Hecke character of K.
  - S is a finite set of primes. It contains the primes above 2 and 3 (that is, (2) and (λ), λ = 1+2ω) and every prime dividing cond(ν).
  - A_u(D) = Σ_{(n,S)=1} μ(n)ν(n)χ_n(u)W(Nn/D), with W ∈ C_c^∞((0,∞);**C**). Here n runs over ideals prime to S, represented by their primary generators.
- **Checked:**
  - The sextic symbol (u/n)_6 is defined for every primary n prime to 6. For a prime p ∤ 6, 6 | Np−1: split q ≡ 1 (mod 6); inert q ≡ 2 (mod 3) with q odd, so 24 | q²−1.
  - Complex W is allowed. This matters: the zero detector W(y)=y^{-ρ}φ(y) in l.730 is complex, and the proof of Prop. 3.1 conjugates W (l.1072, W₀(x)=x^{-1/2} conj(W(x))).
- **Verdict:** no issue.

### S3.1 Proposition 3.1 (l.679-689): the quantifiers used downstream
- **Restated:** fix 0<ϑ≤1/10 and ε>0. Then there is k(ϑ,ε) such that, for every compact I ⊂ (0,∞), every smooth W supported in I, and every real D ≥ 2:

  Σ_{0<N(u)≤D^{1+ϑ}} |A_u(D)|² ≪_{ν,S,I,ϑ,ε} (max_{j≤k} ‖W^{(j)}‖_∞)² D^{2+ϑ+ε}.

- **Checked against its use:**
  - Section 3 needs only one fixed W at a time: the extraction W, and then one W per hypothetical zero ρ. So all W-dependence may sit in the implied constant.
  - D is real, which the Mellin integral requires. The proof covers all D ≥ 2: l.1621-1628 treats "large D" by Prop. 5.1 and "bounded D … by counting".
  - Normalization: D^{2+ϑ} = D·H with H = D^{1+ϑ}, consistent with the outline (eq:intro-ms), l.286-289.
- **Not checked:** the proof of Prop. 3.1 itself (Sections 4-7). This is out of scope.
- **Verdict:** the interface is consistent.

### S3.2 Rows u = p^6 and the identity χ_n(p^6) = 1_{𝔭∤n} (l.695-699)
- **Restated:** H = D^{1+ϑ}, Y = H^{1/6}. For each prime 𝔭 ∉ S with Y/2 < N𝔭 ≤ Y, take the primary generator p.
- **Checked:**
  - Take squarefree n prime to 6: (p^6/n)_6 = Π_{q|n} (p/q)_6^6. This is 1 unless q = 𝔭, and 0 if 𝔭 | n. For non-squarefree n the same holds factor by factor, and μ(n)=0 there anyway.
  - Numerically verified (C1): 24 076 pairs (p, n), with 52 primes of norm ≤ 250 and 463 columns including non-squarefree ones. 0 failures.
  - Remark: since every unit ε satisfies ε^6 = 1, p^6 depends only on the ideal 𝔭. The choice "p ≡ 1 (mod 3)" in l.698 is therefore harmless but unnecessary.
- **Verdict:** correct.

### S3.3 The difference bound |A_1 − A_{p^6}| ≪_W D/Y (l.700-705)
- **Checked:**
  - A_1 − A_{p^6} = Σ_{(n,S)=1, 𝔭|n} μ(n)ν(n)W(Nn/D) exactly. This was verified numerically (C2, 33 pairs (D, p), 0 failures).
  - Write n = 𝔭m. The count is at most #{m : Nm ≤ b₀D/N𝔭}, where supp W ⊂ [a₀, b₀]. Since #{𝔞 : N𝔞 ≤ x} ≤ x for all x > 0 (numerically, sup ratio = 1.000, attained at x=1; asymptotically π/(3√3)·x), the count is ≤ 2b₀D/Y.
  - The bound is uniform in 𝔭.
- **Verdict:** correct. The implied constant depends on supp W and ‖W‖_∞.

### S3.4 The number of rows J (l.706-709)
- **Restated:** "J ≍ Y/log Y such primes; their sixth powers are distinct rows of norm at most H."
- **Checked:**
  - Only the lower bound J ≫ Y/log Y is used. It holds for Y ≥ Y₀(S), by the prime ideal theorem minus at most |S| exceptions.
  - The rows are distinct: p^6 = p'^6 forces (p)^6 = (p')^6, hence 𝔭 = 𝔭'.
  - Norm: N(p^6) = N𝔭^6 ≤ Y^6 = H.
  - Inert primes (N𝔭 = ℓ²) are included harmlessly.
  - Numerically (C3), with S = {(2),(λ)}: J(Y) ≥ 1 exactly for Y ≥ 7. The ratio J/(Y/(2 log Y)) is 0.995, 1.041, 1.028, 1.023, 1.021 at Y = 10³, 10⁴, 10⁵, 10⁶, 2·10⁶.
- **Presentation point (F1):** for D < D₀(S, ϑ), J may be 0 and dividing by J is meaningless. With S = {(2),(λ)}, D₀ = 7^{6/(1+ϑ)} ≈ 4.07·10⁴ at ϑ = 1/10 and 7^6 = 117 649 as ϑ → 0. It is larger when cond(ν) adds small primes to S. The claimed bound for D ≤ D₀ follows trivially from |A_1(D)| ≪_W D ≪ D₀. The paper is silent about this. It is harmless because the constants may depend on ν, S, W, ϑ.

### S3.5 The averaging inequality and the exponents (l.711-717)
- **Restated:**

  |A_1|² ≤ (2/J) Σ_p |A_{p^6}|² + O_W(D²/Y²) ≪ D^{2+ϑ+ε}/Y + D²/Y² = D^{11/6+5ϑ/6+ε} + D^{5/3−ϑ/3}.

- **Checked:**
  - First, |A_1|² ≤ 2|A_{p^6}|² + 2|A_1 − A_{p^6}|²; then average over the J primes.
  - Positivity: Σ_p |A_{p^6}|² ≤ Σ_{0<N u≤H} |A_u|².
  - Apply Prop. 3.1 with loss ε/2. Then (log Y)/Y · D^{ε/2} ≪ D^{ε}/Y.
  - Exponents, checked with sympy (C4):
    - (2+ϑ) − (1+ϑ)/6 = 11/6 + 5ϑ/6;
    - 2 − (1+ϑ)/3 = 5/3 − ϑ/3;
    - their difference is 1/6 + 7ϑ/6 > 0, so the first term dominates;
    - half of the first exponent is 11/12 + 5ϑ/12;
    - the outline's (eq:intro-extraction), D H^{5/6} + D² H^{-1/3}, gives the same exponents.
  - The first term is strictly decreasing in Y. Under the constraint Y^6 ≤ H, Y = H^{1/6} is therefore optimal.
  - The resulting exponent increases in ϑ, so ϑ → 0 is optimal. Hence 11/12 = (1 + 5/6)/2 is the limit of this extraction.
- **Verdict:** correct.

### S3.6 Passing ϑ → 0 (l.718-724)
- **Checked:** for any target loss ε, take ϑ = ε (say) and Prop.-loss ε/5. Each ϑ has its own constant. No uniformity in ϑ is needed, because only the exponent tends to 11/12. This yields (eq:mobius-saving): A_1(D) ≪_{ν,S,W,ε} D^{11/12+ε} for every ε>0 and every fixed W.
- **Verdict:** correct.

### S3.7 Zero detection by the Mellin transform (l.726-757)
- **Restated:**
  - Suppose L_K(ϱ,ν) = 0 with Re ϱ > 11/12.
  - Take φ ∈ C_c^∞((1,2)), φ ≥ 0, φ ≠ 0, and W(y) = y^{-ϱ}φ(y). Then Ŵ(ϱ) = ∫φ dy/y > 0.
  - M_W(s) = ∫_0^∞ A_1(D)D^{-s} dD/D is holomorphic on Re s > 11/12.
  - On Re s > 1, M_W = Ŵ/L_K^S. The identity extends to Re s > 11/12, and evaluating at ϱ gives a contradiction.
- **Checked:**
  - W is smooth, complex and supported in supp φ ⊂ (1,2), so Prop. 3.1 and (mobius-saving) apply to this fixed W.
  - The value Ŵ(ϱ) = ∫ y^{-ϱ}φ(y) y^{ϱ} dy/y = ∫φ dy/y > 0. Checked numerically at ϱ = 0.95 + 14.1347i (C5); the imaginary part is < 10^{-39}.
  - Convergence and holomorphy of M_W:
    - Since Nn ≥ 1 and W(Nn/D) ≠ 0 needs Nn < 2D, A_1(D) = 0 for D ≤ 1/2.
    - On [1/2, 2], A_1 is a finite sum of continuous functions of D.
    - On [2, ∞), |A_1(D)| D^{-σ-1} ≪ D^{-1-ε} once σ ≥ 11/12 + 2ε.
    - Locally uniform absolute convergence then gives holomorphy, by Morera/Fubini.
  - Termwise identity:
    - The substitution y = Nn/D gives ∫_0^∞ W(Nn/D)D^{-s} dD/D = (Nn)^{-s}Ŵ(s). The orientation and the sign of y^{s} were checked, and verified by quadrature for three (N, s) pairs with relative error < 10^{-29} (C5).
    - Tonelli applies for σ > 1, since Σ_n (Nn)^{-σ} ∫|W|y^σ dy/y < ∞.
    - Σ_{(n,S)=1} μ(n)ν(n)(Nn)^{-s} = Π_{𝔭∉S}(1−ν(𝔭)N𝔭^{-s}) = 1/L_K^S(s,ν). This uses ν(𝔭)=0 for 𝔭 | cond(ν), so the definition in l.749-750 is consistent.
  - Continuation:
    - L_K^S is meromorphic on C, with at most a simple pole at s=1 for principal ν. Ŵ is entire.
    - L_K^S·M_W − Ŵ is meromorphic on the connected domain Re s > 11/12 and vanishes on Re s > 1, so it vanishes identically.
    - At s=1 for principal ν, the singularity is removable and M_W(1)=0 (see F3).
  - Evaluation at ϱ:
    - If ν is principal, ϱ ≠ 1, because s=1 is a pole of ζ_K and not a zero.
    - L_K^S(ϱ) = L_K(ϱ)·Π_{𝔭∈S}(1−ν(𝔭)N𝔭^{-ϱ}) = 0, since the finite product is entire. This gives 0 = Ŵ(ϱ) > 0.
    - The paper's remark that the omitted factors are nonzero (l.756) is true for Re s > 0, because |ν(𝔭)N𝔭^{-s}| < 1. However, the direction used does not need it (F2).
- **Uniformity:** none is needed. Each ϱ has its own fixed W, and the constants may depend on W. This is exactly the qualitative Littlewood principle, as the outline says (l.244-253).
- **Verdict:** correct.

### S3.8 From Hecke L-functions over K to Dirichlet L-functions and ζ (l.759-770)
- **Restated:** L_K(s, χ∘N) = L(s,χ)L(s,χχ₋₃), up to Euler factors that are nonzero for Re s > 0. Zeros of either factor away from s=1 are excluded. At s=1, L(1,χ₋₃) > 0.
- **Checked:**
  1. **χ∘N is a finite-order Hecke character of K.** It is a ray class character mod qO. If α ≡ 1 (mod qO), then ᾱ ≡ 1 as well (qO is stable under conjugation), so Nα ≡ 1 (mod q) and Nα > 0. The 7/8 companion gives the same argument (tex78/paper.tex l.6726-6727).
  2. **Euler factors.** For a split ℓ: (1−χ(ℓ)ℓ^{-s})^{-2}. For an inert ℓ: (1−χ(ℓ)²ℓ^{-2s})^{-1} = (1−χ(ℓ)ℓ^{-s})^{-1}(1+χ(ℓ)ℓ^{-s})^{-1}. For ℓ=3: (1−χ(3)3^{-s})^{-1} against χχ₋₃(3)=0. For ℓ | q: both sides are 1.
     - So, with ν(𝔞) := χ(N𝔞) and χχ₋₃ taken mod lcm(q,3), the identity is **exact** as Dirichlet series.
     - Equivalently: χ(m)·r_K(m) = Σ_{de=m} χ(d)χ(e)χ₋₃(e), with r_K(m) = Σ_{e|m} χ₋₃(e).
     - Verified numerically (C6): r_K(m) for m ≤ 3000 by counting elements of norm m divided by 6; the coefficient identity for all 41 characters of moduli 1, 3, 4, 5, 7, 8, 9, 12, 13 and m < 800. 0 failures.
     - Passing to primitive characters changes only finitely many factors (1 − a p^{-s}) with |a| ≤ 1. These have no zeros or poles in Re s > 0.
  3. **Poles and zeros.** Dirichlet L-functions are entire except for the principal-character pole at s=1. So a zero ρ ≠ 1 of either factor, with Re ρ > 11/12, would give a zero of L_K(s, χ∘N) in Re s > 11/12, which is excluded. At s = 1 there are two cases.
     - **Cancellation impossible.** If neither χ nor χχ₋₃ is induced by the principal character, both factors are entire. χ∘N is then a nontrivial ray class character, so L_K(s, χ∘N) is entire, and the Hecke conclusion excludes a zero at s=1 too.
     - **Cancellation possible.** χ is principal, or χ is induced by χ₋₃. Then χ∘N is (imprimitively) principal, and the other factor is L(s,χ₋₃) up to factors that are finite and nonzero at s=1. Here L(1,χ₋₃) = π/(3√3) = 0.6046… > 0, checked with mpmath.
     - The citation [Dav00, Ch. 4 and 6] is appropriate: Ch. 4 covers L(1,χ)≠0 and Ch. 6 the class number formula.
  4. **ζ(s)** is the case χ = trivial character mod 1: ζ_K(s) = ζ(s)L(s,χ₋₃).
- **Cross-check:** the 7/8 companion states this step as a separate proposition, "Quadratic transfer" (tex78/paper.tex l.6705-6781), with the same case analysis. It also computes L(1,χ₋₃) = π/(3√3) explicitly.
- **Verdict:** correct. The step is uncited in the 11/12 paper but standard; this audit verified it.

### S3.9 Theorem 1.1 statement and scope (l.71-74, l.46-48)
- **Finite order.** Over the imaginary quadratic field K, a finite-order Hecke character has a finite-order archimedean component on the connected group C^×. That component is therefore trivial, so finite-order Hecke characters are exactly the ray class characters. "Uniformity in the infinity type" is moot.
- **No conductor uniformity is needed.**
  - The exponent 11/12 comes from ϑ, ε → 0, and these choices are independent of ν.
  - The proof of Prop. 3.1 fixes κ = ϑ/2 and C₀ = 2 (l.1621-1622) and induction depth ⌈C₀/κ⌉ (l.1606), all independent of ν.
  - The constants may depend on ν, S, the fixed ray class group and W, and they never enter the exponent.
  - Hence the half-plane is uniform in conductor and height, as asserted in l.69-72.
- **Imprimitive ν** is covered: the Euler-factor differences are nonzero for Re s > 0.
- **Landau–Siegel zeros** (abstract, l.47): ruled out as an immediate corollary, since 1 − c/log q > 11/12 for q ≫ 1.
- **Verdict:** the scope of the statement matches the proof.

## 2. Imported results used in Section 3

| Import | Exact form needed | Form in paper | Status |
|---|---|---|---|
| Landau prime ideal theorem [Lan03], [IK04 Thm 5.33] | For the fixed K and finite S: #{𝔭∉S : Y/2<N𝔭≤Y} ≫ Y/log Y for Y ≥ Y₀(S) (lower bound only) | "J ≍ Y/log Y" (l.706-708) | Standard; much weaker than the cited theorem. Confirmed numerically up to Y = 2·10⁶ (C3). IK04 was not re-fetched (it is a book); only the qualitative asymptotic is used. |
| Hecke continuation [Hec20], [IK04 §5.10] | L_K(s,ν) meromorphic on C, with only a possible simple pole at s=1 for principal ν | l.752-755 | Standard (Hecke, Math. Z. 1 (1918) and 6 (1920)). |
| Dirichlet's L(1,χ)≠0 [Dav00 Ch. 4, 6] | L(1,χ₋₃) ≠ 0 | l.768-770 | Standard; value π/(3√3) checked. |
| Quadratic base change (uncited) | L_K(s,χ∘N) = L(s,χ)L(s,χχ₋₃) up to Euler factors nonvanishing in Re s>0 | l.761-766 | Verified (C6). The identity is exact with the stated conventions. |
| Littlewood [Lit12], [MM09] | Motivation only | l.248-252 | Not load-bearing. |

No result in Section 3 is imported in a form stronger than its source.

## 3. Numerical checks (our code only)

Script: `research/exploratory/riemann-observatory/experiments/code/quasi_rh/s3_deduction_checks.py`. Run it as `python3 -I s3_deduction_checks.py [C1 … C7]`. The output is in `s3_deduction_checks.out`.

The script implements Z[ω] arithmetic from scratch:
- elements (a,b) = a + bω;
- Euclidean reduction;
- primary normalization (≡ 1 mod 3);
- the sextic symbol through x^{(N𝔭−1)/6} mod 𝔭, matched to ζ₆^k with ζ₆ = 1+ω.

| Id | Identity / claim | Range | Result |
|---|---|---|---|
| C1 | χ_n(p^6) = 1_{𝔭∤n} | 52 primes (N𝔭 ≤ 250) × 463 columns n (products of 1-3 primes of norm ≤ 100, including non-squarefree, Nn ≤ 6000): 24 076 cases | confirmed, 0 failures |
| C2 | A_1 − A_{p^6} = Σ_{𝔭\|n} μ(n)W(Nn/D) (ν = 1, W a bump on (1,2)); count bound #{n : 𝔭\|n, Nn∈(D,2D)} ≤ c·2D/N𝔭 | D ∈ {200, 500, 1200}, N𝔭 ≤ 40: 33 cases | confirmed. max count·N𝔭/(2D) = 0.19; sup_x #{N𝔞≤x}/x = 1 |
| C3 | J(Y) ≥ 1 threshold; J/(Y/(2 log Y)) | Y ≤ 2·10⁶, S = {(2),(λ)} | J ≥ 1 iff Y ≥ 7 (so D ≥ 7^{6/(1+ϑ)}); ratio ≈ 1.02 |
| C4 | Exponent arithmetic of (eq:prime-extract) and (eq:intro-extraction); optimality of Y = H^{1/6} | symbolic in ϑ (sympy) | confirmed |
| C5 | ∫W(N/D)D^{-s}dD/D = N^{-s}Ŵ(s); Ŵ(ϱ) = ∫φ dy/y > 0 | ϱ = 0.95+14.1347i; (N,s) ∈ {(7,2+3i), (13,1.3−5i), (49,ϱ)}; mpmath at 30 digits | confirmed, relative error < 10^{-29} |
| C6 | r_K(m) = Σ_{e\|m} χ₋₃(e); χ(m) r_K(m) = (χ ∗ χχ₋₃)(m) | m ≤ 3000; 41 characters of moduli 1, 3, 4, 5, 7, 8, 9, 12, 13, m < 800 | confirmed, 0 failures |
| C7 | Illustration only, not evidence: Σ_{0<N u≤H}\|A_u(D)\|² normalized (ν=1, ϑ=0.1) | D ∈ {300, 800, 2000, 6000, 15000}; up to 142 332 rows × 4221 columns | ratio to (#rows)·Σ\|c_n\|² is 0.91-0.95 (near-diagonal); Σ/(DH) ≈ 0.06 |

C7 is far below the scale where J ≥ 1 (D ≥ 4·10⁴), and H/D = D^{0.1} ≤ 2.6 there. It cannot test Prop. 3.1 asymptotically. It is recorded only to show that the normalization D·H is the diagonal size.

A note on our first run of C6: it reported 288 mismatches. These came from a bug in our own Dirichlet-character generator, which built non-homomorphisms when the chosen generators had relations. After we rebuilt the characters from prime-power factors and asserted complete multiplicativity, C6 passes with 0 failures. This was not a defect in the paper.

## 4. Calibration remarks (not findings)

- **Strength of Prop. 3.1.**
  - Section 3 shows that Prop. 3.1 for ν = 1 alone, for every ϑ > 0, already implies ζ_K(s) ≠ 0 for Re s > 11/12, and hence a quasi-RH for ζ. B. Liu makes the same observation independently (arXiv:2610.26835v2, Remark 10.9, pdftotext line 3338 onward). Prop. 3.1 is therefore a statement of quasi-RH strength. All of the risk lies there.
  - Liu's Theorem 10.8 (statement at pdftotext line 3273; the extraction is at lines 3302-3335) re-derives the same extraction. It uses all sixth powers a^6, not only prime ones, together with the Euler identity M_1(D) = Σ_{d|rad a} μ(d)ν(d) q_d^{-1/2} M_{a^6}(D/q_d). This gains only the factor log Y, and the exponent 11/12 is the same.
- **Consistency with GRH.**
  - For fixed u, n ↦ (u/n)_6 is the Artin symbol of the Kummer extension K(u^{1/6})/K. Note μ₆ ⊂ K.
  - So A_u(D) is a smoothed Möbius sum for a finite-order Hecke character whose conductor is ≪ N(u)·O(1).
  - Under GRH for these characters, |A_u(D)| ≪ D^{1/2+ε}N(u)^ε, which gives Σ_{N u≤H} |A_u|² ≪ D^{1+ε}H.
  - So Prop. 3.1 is a "GRH on average over the sextic family" statement. It does not contradict any known result; it is simply far beyond current unconditional knowledge.
- **Tightness of the extraction.**
  - Suppose one twisted character ν·(u₀/·)_6 had a zero at β.
  - The ≈ H^{1/6} rows u₀a^6 all carry essentially the same sum, so Prop. 3.1 forces only H^{1/6}D^{2β} ≪ D^{1+ε}H. That is β ≤ 11/12 + 5ϑ/12.
  - So Prop. 3.1 gives exactly 11/12 through these rows and nothing better. This is consistent with the paper's remark that the 7/8 paper changes the extraction.

## 5. Findings

| Id | Location | Class | Claim | Witness / reasoning | Severity |
|---|---|---|---|---|---|
| F1 | l.706-713 | typo_or_presentation | "J ≍ Y/log Y" and division by J hold only for Y ≥ Y₀(S). For smaller D, J can be 0. | C3: with S={(2),(λ)}, J(Y)=0 for Y<7, i.e. D < 7^{6/(1+ϑ)} ≈ 4.07·10⁴ at ϑ=0.1. The claimed bound for D ≤ D₀ follows trivially from \|A_1\| ≪_W D. The paper is silent. | cosmetic |
| F2 | l.756 | typo_or_presentation | "The omitted Euler factors are nonzero here" is true but not needed. | L_K(ϱ)=0 already implies L_K^S(ϱ)=0, since the finite product over S is entire. Nonvanishing matters only for the converse direction. | cosmetic |
| F3 | l.752-755 | typo_or_presentation | "The identity L_K^S M_W = Ŵ holds on Re s>11/12" must be read as an identity of meromorphic functions when ν is principal. | ζ_K^S has a pole at s=1 and M_W is holomorphic there. Hence M_W(1)=0, the product has a removable singularity, and ϱ ≠ 1 automatically. | cosmetic |
| F4 | l.679-689 | typo_or_presentation | Prop. 3.1 does not say that u ranges over elements of O (not ideals). Its label is `thm:ms` although the environment is a Proposition (P3 of the architecture map). | Context fixes the reading (l.268, l.1032). Under the ideal reading χ_n(u) would be ill-defined because of units. | cosmetic |
| F5 | l.695-724 | no_issue_found_in_inspected_portion | Extraction: χ_n(p^6) identity, the D/Y difference, row distinctness and norms, the averaging inequality, the exponents (11/6+5ϑ/6, 5/3−ϑ/3), the ϑ→0 limit, and the optimality of Y = H^{1/6}. | Hand-checked and C1, C2, C4. | — |
| F6 | l.726-757 | no_issue_found_in_inspected_portion | Mellin zero detection: choice of W, positivity of Ŵ(ϱ), holomorphy of M_W, termwise integration, Euler product over S, continuation and identity theorem, evaluation at ϱ, pole at s=1. | Hand-checked and C5. | — |
| F7 | l.759-770 | no_issue_found_in_inspected_portion | Base change to Dirichlet L-functions and ζ, including the s=1 pole–zero case through L(1,χ₋₃)=π/(3√3)>0. | Hand-checked, C6, and the matching Prop. "Quadratic transfer" in tex78 l.6705-6781. | — |
| F8 | l.71-74, l.665-667 | no_issue_found_in_inspected_portion | Uniformity in ν: none is required. Finite order implies trivial infinity type over K. The exponent is independent of ν; the constants and the threshold D₀ depend on ν and S. | Qualitative Littlewood principle; κ, C₀ and the induction depth in l.1606, l.1621-1622 are independent of ν. | — |
| F9 | l.82-95 (Cor. 1.2), l.97-125 | no_issue_found_in_inspected_portion | Corollary 1.2 and the arithmetic applications are not proved in the paper (P5 of the map) and are not load-bearing. A standard sketch is consistent with the stated bound. | The zero-free half-plane plus the functional equation give 1/12 ≤ β ≤ 11/12, hence \|ρ\| ≥ 1/12 and Σ_{\|γ\|≤T} 1/\|ρ\| ≪ log²(qT). The truncated explicit formula (Davenport Ch. 19-20) with T=x gives ψ(x,χ) ≪ x^{11/12}log²(qx). Partial summation gives π(x;q,a) − Li(x)/φ(q) ≪ x^{11/12} log x, with absolute and effective constants. Not checked line by line. | — |

There is no verified_error, suspected_gap, unresolved_ambiguity or missing_hypothesis in Section 3.

## 6. Not checked here

- Proposition 3.1 itself: Sections 4-7 and Appendices A-B. Everything in Section 3 is conditional on it.
- The consequences listed at l.97-125: Vinogradov's conjecture, Miller's test, class numbers and idoneal numbers.
- The Lean formalization of the companion 7/8 theorem (`riemannZeta_ne_zero_of_seven_eighths_lt_re`). It was not replayed.

## 7. The smallest statement whose failure would invalidate Section 3's conclusion

Inside Section 3 the only non-standard input is **Proposition 3.1 (eq:ms)**.

Logically, the deduction uses only the restriction of (eq:ms) to the ≈ Y/log Y prime sixth-power rows u = p^6, with Y = D^{(1+ϑ)/6} and ϑ arbitrarily small. However, A_{p^6} = A_1 + O(D/Y), so that restriction is essentially equivalent to (eq:mobius-saving), A_1(D) ≪ D^{11/12+ε}, itself. By the Mellin argument and Littlewood's principle, (eq:mobius-saving) is equivalent to the zero-free half-plane.

So the content of the proof is the full-family bound (eq:ms) for all rows 0 < N(u) ≤ D^{1+ϑ}. Its failure, even for a single fixed ν and W, would leave Theorem 1.1 unproved for that ν. Section 3 itself adds no further risk.
