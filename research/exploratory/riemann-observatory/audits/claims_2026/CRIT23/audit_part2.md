# CRIT23 Level-2 audit, part 2 of 2: steps S6–S10, cross-checked against the independent proofs

```text
Status: EXPLORATORY AUDIT (Level 2, part 2 of 2). No new mathematical claim. Nothing here says RH is proved,
        or closer to proved. The audited theorems are asymptotic lim inf lower bounds for proportions of zeros.
        No finite-height statement follows from them, and none is made here.
Scope: steps S6-S10 of ARCHITECTURE.md Section 5:
          S6   the unconditional prime-side second moment: AF Section 5; LZ Lemma 3.1 = BGSTB24 Lemma 5
          S7   LZ's removal of the weight w(rho - rho') (Lemma 3.2)
          S8   the window constants
          S9   the counting bookkeeping: AF Section 6 including the dyadic summation, LZ Thm 1.1, KN Cor 1.2
          S10  Knausgard's certificate layer: Lemmas 2.1-2.5, Thm 2.6, Prop 3.1, Thms 3.2/5.1/6.2, Prop 5.2,
               and the Appendix A data
        S1-S5 are audited in audit_part1.md. Each step is cross-checked against the independent proof.
Exact sources or dependencies (version read; PDF SHA-256; e-print tarball SHA-256 of the copy downloaded for part 2):
        AF  = Alpoge-Furman arXiv:2608.13637v2   PDF 6de3b156...c4ef444  tarball d6a2e5ca0b1d2cec...  (paper-v5-draft18.tex)
        LZ  = Lamzouri arXiv:2609.02882v2        PDF 305df7fc...621046b  tarball 70370356f7010c42...  (ZetaZerosV2.tex)
        KN  = Knausgard arXiv:2610.08965v1       PDF aedf2891...aaf8a08200f tarball 60fb628fb12bdc1c... (knausgard839*.tex)
        BGSTB24 = Baluyot-Goldston-Suriajaya-Turnage-Butterbaugh arXiv:2306.04799v1 = Acta Arith. 214 (2024)
                                                 PDF 133071c4...ee9      tarball 6ed758704d6f1735...  (UnconditionalPC_230606.tex)
        Zero ordinates: experiments/results/zeros/zeta_zeros_1_100000_arb.tsv.gz (sha256 4d364a6b...715603).
        Full hashes: Section 5.
What was actually run: line-by-line reading of AF Sections 5-6 and Remark 6.1, LZ Section 3 and the Thm 1.1
        proof, BGSTB24 Sections 2-3 (Thm 1, Lemmas 1-5), and KN Sections 2, 3, 5, 6 and Appendix A (LaTeX and
        PDF). Every S6-S10 statement was re-derived by hand, except the error terms of BGSTB24 Thm 1, which rest on
        [GM87] and were read but not re-derived. Six independent Python scripts in
        experiments/code/claims_2026/crit23_part2/, with outputs beside them: sympy exact identities; mpmath/numpy
        quadrature; Lipschitz-grid bounds in double precision (not directed rounding); randomised and optimised
        stress tests; and a normalisation check against the first 10^5 zeta zeros. No author code, ancillary
        program, Lean development or repository content was run. KN's tables were read as data.
Smallest remaining gap: no step in S6-S10 fails. Three presentation-level slips in AF Section 5 (P2-F1 to F3)
        have no effect on any theorem. Not replayed: KN's three branch-and-bound proofs (Props 3.3, 5.3, 6.3)
        and every Lean build. BGSTB24's endpoint refinement (alpha up to 1, via [GM87] with a "slight correction")
        was not re-derived. On our reading it is not needed for LZ/KN (P2-N1).
```

## 1. Answers to the task questions, from the S6–S10 side

### 1.1 What takes the proportion from 5/12 to 2/3

This is a change of method, not an incremental gain:

* The previous record for zeros on the critical line came from the Levinson–Conrey mollifier. PRZZ20 give κ > 0.417293 on the line and κ* ≥ 0.407511 for simple zeros on the line.
* The new bound is **Montgomery's 1973 pair-correlation second-moment argument with the Montgomery–Taylor window**, made unconditional.
* It uses no mollifier, no zero-density estimate, no derivatives of ζ, and no pair-correlation information beyond Fourier support [−1, 1].

The argument rests on three facts about one operator A (LZ: on L²(−½, ½); AF: its d × d compression G̃):

1. **(exact)** tr A = N.
2. **(S6)** tr A² = Σ_{z,s} K(z − s)² = (C(f) + o(1)) N, summed over **all** zeros, on or off the line, with f = η² and K = f̂. This is Montgomery's second moment. Its prime side was already known to be unconditional (Aryan 2022; BGSTB24 Lemma 5, which carries the weight w).
3. **(S3)** The inertia structure: on-line zeros give PSD rank-one pieces, and each off-line pair gives a block of signature (1, 1) with trace 2m.

The new step is S4 (part 1). Montgomery's termwise reading m² ≥ 2m − 1 needs RH, because the summands K(γ − γ′)² must be real and nonnegative. S4 replaces that reading by a spectral inequality on the whole form. S6–S9 then turn the second-moment constant C(f) into the counts 2 − C(f) and (3 − C(f))/2.

* The flat window gives C = 4/3, hence 2/3 and 5/6. These are exactly the RH-conditional numbers of Montgomery (2/3) and Conrey–Ghosh–Gonek (5/6, via m² ≥ 3m − 2).
* The Montgomery–Taylor (MT) window minimises C(f) over admissible windows ([CCLM17, Cor. 14]) and gives C_MT = 1.32749…, hence 0.67250… and 0.83625….

In the terms of the question, then, the method is "a pair-correlation / Montgomery–Taylor-window argument", combined with a linear-algebra replacement for positivity and with nothing else. KN's refinement keeps the same second moment and adds local, computer-assisted information about how close points interact (S10).

### 1.2 Which inputs are unconditional (S6–S10)

| Step | AF | LZ | KN |
|---|---|---|---|
| S6 | Weil explicit formula for F ∈ C²_c with supp F ⊂ [−log X, log X], X = T/2π (AF (2.2)); Stirling for μ; Chebyshev–Mertens sums (AF Lemma 5.1); Montgomery–Vaughan weighted Hilbert inequality [MV74, Thm 2] (AF Lemma 2.2). No information about zeros, and no zero-free region. | BGSTB24 Lemma 5. Its proof uses Thm 1, which rests on: Landau's explicit formula (Lemma 1); Riemann–von Mangoldt (Lemma 2); the positivity identity (Lemma 3); the truncation of Lemma 4, whose error O(x^{1−2η}log³T); the mean value R(x,T) of [GM87], "corrected slightly" (BGSTB24 remark after Thm 1); and the Korobov–Vinogradov (KV) zero-free region, used only for √T ≤ x ≤ T. By P2-N1, KV and the endpoint refinement are not load-bearing for LZ. | as LZ (KN Prop 3.1 imports BGSTB24 Lemma 5 and LZ's weight device) |
| S7 | not needed (the Weil form has no weight) | the Fourier identity (Q″)^ = (2πiz)²Q̂, pure algebra | same device |
| S8 | calculus (AF Lemma 5.6) | calculus plus L¹/L² continuity of C(·) | closed form (eq:C) |
| S9 | algebra; N(t, t + 1) ≪ log t for the dyadic summation | algebra; N(T) ~ (T/2π) log T | algebra |
| S10 | — | — | algebra (convexity, Jensen, Plancherel/Fourier support), plus three finite inequalities proved by computer (branch-and-bound; `native_decide` in Lean) |

RH, the generalized Lindelöf hypothesis, the pair-correlation conjecture and zero-density hypotheses occur nowhere in S6–S10, nor in any imported statement.

### 1.3 Load-bearing steps audited in this part

| # | Statement (short) | Location | Status |
|---|---|---|---|
| S6a | Reduction: ‖G̃ + Ẽ‖²_HS = (a²L²)⁻¹ ∬_{I×I} Φ(τ − τ′)² ν_X(τ) ν_X(τ′) + error | AF Prop 5.2 | verified; stated error exponent too strong as written (P2-F1, harmless) |
| S6b | Main terms: M[μ,μ] and M[P_X,P_X]; assembly to R(ψ) N | AF Props 5.3, 5.4, Thm 5.7 | verified (symbolic + numeric; reproduced on actual zeros to ≤ 2·10⁻⁴) |
| S6c | Off-diagonal and cross terms are o(N) | AF Props 5.4 (O₁, O₂), 5.5 | verified; one bound justified insufficiently but harmless (P2-F2) |
| S6′ | Σ_{0<γ,γ′≤T} r̂(i(ρ − ρ′) log T/2π) w(ρ − ρ′) = (T/2π) log T (r(0) + 2∫₀¹ α r + O(1/√log T)) | LZ Lemma 3.1 = BGSTB24 Lemma 5 | statement verbatim; hypotheses checked at the point of use; proof chain read; endpoint inputs not load-bearing (P2-N1) |
| S7 | K(z)² = r̂(z) w(ρ − ρ′) at z = i(ρ − ρ′) log T/2π, with r = Q − Q″/(4 log²T) | LZ Lemma 3.2, (3.2)–(3.3); KN Prop 3.1 | verified exactly (sympy) and at complex z off the line |
| S8 | C(ψ₀) = 4/3, C(f_MT) = C_MT; C_δ → C_MT; finite-L taper cost O(1/L) | AF Lemma 5.6; LZ Lemma 3.2 | verified (sympy + 30 digits) |
| S9 | Counts from inequalities; cumulative form | AF §6, Rem 6.1; LZ Thm 1.1 proof; KN Cor 1.2 | verified (21 sympy identities; operator-level tests) |
| S10a | tr A² ≥ 2cN − (2c−1)n₁ − (4c−4)n₂ − c²(h+k) + (tr φ_c(G) − tr D²) | KN (eq:key), Lemma 2.1 | verified (hand + operator-level tests) |
| S10b | Labelled Gram bound | KN Lemmas 2.2–2.5, Thm 2.6, Prop 5.2 | verified by hand; transfer lemma stress-tested |
| S10c | Certificate principles | KN Thms 3.2, 5.1, 6.2 | verified (sympy + exact rationals) |
| S10d | Window data: C(f), β, Λ, f ≤ g, Ω, thresholds | KN §3, §5, §6, App. A | all reproduced |
| S10e | Local inequalities (7- and 8-point frames) | KN Props 3.3, 5.3, 6.3 | **not proved here.** 2·10⁶-frame sampling plus local minimisation found no violation |

Within S6–S10, the smallest statement whose failure would sink CRIT23 is **S6**: the asymptotic Σ_{z,s∈Z_T} K(z − s)² = (C(f) + o(1)) N over all zeros, for a fixed smooth even f whose f ∗ f is supported in (−1, 1). The claim fails only if S6 fails together with S4 from part 1. S6 is proved twice, independently (AF §5, and BGSTB24 Thm 1 → Lemma 5 + LZ Lemma 3.2). For KN's constants, S10e must also hold.

### 1.4 Constants recomputed in this part

| Quantity | Stated | Recomputed (script) |
|---|---|---|
| (∫ψ² + 2∫₀¹ w(ψ∗ψ))/(∫ψ)², AF Thm 5.7 assembly | R(ψ₀) = 4/3; R(ψ_MT) = C_MT | 4/3 exactly; C_MT to 2·10⁻³¹ (s6_prime) |
| (ψ_MT ∗ ψ_MT)(w), closed form derived here | — | ½(1 − w)cos(√2w) + sin(√2(1 − w))/(2√2), checked by quadrature (s6_prime) |
| C(f_MT) symbolic | C_MT = ½ + cot(1/√2)/√2 = 1.3274992963205… | sympy difference evaluates below 10⁻¹⁶⁵; stationarity G″ = 0 exact (s8) |
| 2 − C_MT, (3 − C_MT)/2, LZ C₂ | 0.67250…, 0.83625…, 0.88762… | 0.67250070367941164573, 0.83625035183970582287, 0.88762000817335 (also part 1) |
| LZ C_δ → C_MT | limit | C_δ − C_MT = 7.1·10⁻⁴ at δ = 10⁻³; (C_δ − C_MT)/δ → 0.708; always > 0 (s8) |
| AF finite-L ratio R_L = (bL³ + 2∫₀^L y g)/(a²L³) | → R(ψ) | L(R_L − R) → 0.64 (flat), 0.71 (MT) (s8) |
| LZ Q″-term coefficient | O(1) | Q″(0) + 2∫₀¹ αQ″ = Q″(0) + 2Q(0) = −40.00351 for δ = 0.1 (s7) |
| KN C(f), windows 1–3 (eq:C), symbolic | 1.3327049582…, 1.32794727…, 1.33246363… | 1.3327049582817, 1.3279472728446, 1.3324636331671; margins to the rational bounds 4.2·10⁻⁸, 1.3·10⁻⁷, 1.7·10⁻⁷ (s8) |
| KN q, 2q − 1, s₀, (1 + s₀)/2, Thm 1.4b, Thm 1.5 | 1645064/1960733, … | all six equal exactly (fractions) (s9) |
| KN μ, ν, r_h, r_k | 1.960733, 3.684917, 1.792984, 0.0688 | identical (s9) |
| KN Ω, windows 1–3 | 0.015882, 0.003882, 0.075420 | 0.015882, 0.003882, 0.075420 from the tables (s10) |
| KN trivial-frame thresholds | 0.001294 → 15.975; 0.038198 → 14.927 | 0.001294 → 15.974; 0.038198 → 14.926 (s10) |
| KN β (Lipschitz-grid lower bound) | 0.06574…, 0.05106…, 0.06680… | 0.0657961, 0.0510827, 0.0668261 ≥ β (s10) |
| KN Λ | 1.67105, 1.78942, 1.67931 | 1.671052 < 1.675 = c/2; 1.789429 < 2; 1.679310 < 2 (s10) |
| KN f ≤ g margin | ≥ 10⁻⁴ | ≥ 4.96·10⁻⁴, 5.16·10⁻², 2.03·10⁻³ (Lipschitz grid) (s10) |

### 1.5 Do the independent proofs share an unverified lemma? (S6–S10; part 1 covers S1–S5)

No.

* **S6.**
  * AF's second moment uses the Weil explicit formula, the Montgomery–Vaughan Hilbert inequality and Mertens. It handles a T-dependent test function with explicit uniformity.
  * LZ's is BGSTB24 Lemma 5 (Landau explicit formula, Montgomery's mean-square method, [GM87]).
  * The two derivations are independent. They share only classical, refereed facts: Riemann–von Mangoldt, Stirling, Mertens, and Montgomery–Vaughan-type mean values. ([MV74] underlies both AF's Lemma 2.2 and the Dirichlet-polynomial mean value used in [GM87].)
  * BGSTB24 predates AF and was refereed (Acta Arith. 2024).
* **S7.** LZ only; AF has no weight. KN reuses LZ's device.
* **S8.** Classical Montgomery–Taylor calculus, recomputed here.
* **S9.** Each proof has its own short bookkeeping, all re-derived.
* **S10.** KN only. It depends on LZ (operator, weight removal) and BGSTB24 (Prop 3.1), and on AF only for the splitting idea. It does not use AF §5.

The theorem at 0.6725/0.83625 therefore has two proofs with disjoint unverified content. KN's refinements depend on the LZ route plus three unreplayed computer searches.

## 2. Step-by-step audit

### 2.1 S6 in AF (Section 5): the prime-side second moment

**Statements.** Throughout, Φ = (φ²)^, g = φ² ⋆ φ², a = ‖φ‖²₂/L, b = ‖φ‖⁴₄/L, ν_X = μ + Π_X + P_X, and M[u₁, u₂] = ∬_{I×I} Φ(τ − τ′)² u₁(τ) u₂(τ′).

* **Prop 5.2.** ‖G̃ + Ẽ‖²_HS = (a²L²)⁻¹ M + O_χ(N log L/L²).
* **Prop 5.3.** M[μ,μ] = 2πbL ∫_T^{2T} μ² + O(l² log L) = (bLTℓ₁²/2π)(1 + O(l⁻²)) + O(l² log L), with ℓ₁ = l + 2 log 2 − 1.
* **Prop 5.4.** M[P_X,P_X] = (T/π) Σ_{n≤X} Λ(n)²/n · g(log n) + O_χ(L²X).
* **Prop 5.5.** M[μ,P_X], M[μ,Π_X], M[P_X,Π_X], M[Π_X,Π_X] ≪_χ L²√X.
* **Lemma 5.6.** R(ψ₀) = 4/3 and R(ψ_MT) = C_MT.
* **Thm 5.7.** ‖G̃‖²_HS = (R(ψ) + O_χ(L⁻¹)) N(T,2T).

**What was checked.**

* *The identity behind Prop 5.2.* (aL²)²‖G̃ + Ẽ‖² = ∬_{ℝ²} K(τ,τ′)² ν_X(τ) ν_X(τ′), with K(τ,τ′) = Σ_{0≤k<d} φ̂(τ − α_k) φ̂(τ′ − α_k).
  * It follows from AF (2.11) by squaring the real entries and summing a finite double sum. Fubini applies because φ̂(τ) ≪ |τ|⁻² by (2.8) and |ν_X(τ)| ≪ √X + log|τ| by (5.7).
  * K = LΦ(τ − τ′) − K_out follows from Lemma 2.1, which part 1 verified at complex arguments.
  * The E₁ bound treats k = d and k = d + 1 separately, using only ∫ϑ = 2Θ₀. It correctly does **not** assume α_d ∉ [T, 2T); compare part 1's P1-F1/F2.
  * S6 uses only α_k ∈ [T, 2T) for 0 ≤ k < d and α_{d+1} > 2T. It never uses the incorrect "d = N(T,2T) + O(L)" (P1-F2).
* *Prop 5.3.* Verified: μ(τ) − μ(τ′) ≪ |τ − τ′|/T on I, ∫Φ²|x| ≪ log L, and ∫_{|x|>T} Φ² ≤ ∫Φ²|x|/T.
  * I re-derived ∫_T^{2T} log²(τ/2π) dτ − Tℓ₁² = T(1 − 2 log²2) = O(T), which confirms the second form.
* *Prop 5.4.*
  * The expansion (5.12) is correct: P_X(τ)P_X(τ′) = (1/2π²) Re Σ a_n a_m [n^{iτ}m^{−iτ′} + n^{iτ}m^{iτ′}], with τ = τ′ + x.
  * Diagonal: D = (T/π) Σ a_n² g(log n) + O(L² log L), using ∫Φ²(x) n^{ix} dx = 2πg(log n), which is AF (5.11).
  * O₂ ≪ XL, from |∫(nm)^{iτ′}| ≤ 2/log 4 and Σ a_n ≤ 3√X.
  * O₁ ≪ L²X, from Lemma 2.2 with δ_n⁻¹ ≤ 2n, which is AF (2.12).
    * Both neighbouring gaps of a prime power satisfy log(n′/n) ≥ 1/(2n).
    * The extension of [MV74, Thm 2] from the quadratic to the bilinear form, via the Hermitian matrix ΔHΔ with H_rs = i/(λ_r − λ_s), is correct.
  * The final paragraph uses the lower bound in (5.2), which is valid only for ψ₀ (P2-F3). Thm 5.7 does not rely on it.
* *Prop 5.5.*
  * M[μ,P_X] ≪ l√X is verified: integration by parts in τ′ with ∫_I |m′| ≪ lL, and Σ a_n/log n ≪ √X/L.
  * M[μ,Π_X] and M[Π_X,Π_X] follow from the sup bounds as stated.
  * M[P_X,Π_X] does not follow from them (P2-F2). The weaker bound that does follow suffices.
* *Thm 5.7 main term.*
  * g(y) = L(ψ∗ψ)(y/L) + O_χ(1) uniformly: the two transition intervals have length 1 and 0 ≤ φ² ≤ 1.
  * Partial summation with Σ_{n≤t} Λ(n)²/n = ½ log²t + O(log t) gives L³∫₀¹ w(ψ∗ψ) + O(L²). The boundary term vanishes because (ψ∗ψ)(1) = 0, and ψ∗ψ is Lipschitz.
  * The assembly constant (∫ψ² + 2∫₀¹ w(ψ∗ψ))/(∫ψ)² = R(ψ) uses 2∫₀¹ w(ψ∗ψ) = ∬|u − v|ψψ for even ψ.
  * TL/2π and N(T,2T) differ by O(T) = O(N/L).
  * Removing Ẽ costs ≪ √N · T^{−1/2}, by Prop 4.3.
* *Uniformity and limits.* AF's φ depends on T through L, so a fixed-test-function theorem such as BGSTB24 Lemma 5 cannot be applied to it directly. AF prove S6 themselves, with every implied constant depending only on (χ, ψ). No interchange of limits occurs beyond T → ∞.

**Numerics** (s6_prime_side_af.out). Lemma 5.1 (5.5) is checked to x = 2·10⁷: Σ Λ²/n − ½log²x stays near −1.57; Σ Λ²/n (log x − log n) − log³x/6 = −0.072 log²x at x = 2·10⁷. The Thm 5.7 partial summation has (sum − L²∫₀¹ w(ψ∗ψ))/L ∈ [−0.11, −0.06] for X ∈ [10⁴, 2·10⁷] and both windows, so the O(L) error is confirmed. The assembly constant equals R(ψ) to 2·10⁻³¹.

**End-to-end check on actual zeros** (s6_zero_side_data.out, part (A)). For I = [T, 2T) with T ∈ {5·10³, 1.5·10⁴, 3·10⁴}, AF's φ with a C^∞ taper, and both windows, three quantities were compared:

* the zero side Z = Σ_{γ,γ′∈I} Φ(γ − γ′)²/(a²L²);
* the **full** prime side M/(a²L²), computed numerically from μ (digamma), Π_X and P_X, with all off-diagonal and cross terms kept;
* AF's main terms Mm = [2πbL∫_I μ² + (T/π) Σ a_n² g(log n)]/(a²L²).

| window, T | Z/N(I) | M/N(I) | Mm/N(I) | R(ψ) |
|---|---|---|---|---|
| flat, 5·10³ | 1.48014 | 1.48012 | 1.48033 | 1.33333 |
| flat, 3·10⁴ | 1.44138 | 1.44138 | 1.44133 | 1.33333 |
| MT, 5·10³ | 1.48532 | 1.48529 | 1.48551 | 1.32750 |
| MT, 3·10⁴ | 1.44409 | 1.44409 | 1.44404 | 1.32750 |

* Z = M to ≤ 3.3·10⁻⁵ relative. This is the explicit formula in AF's normalisation, up to edge effects.
* Mm = M to ≤ 2·10⁻⁴ relative. So the terms AF bound by O(N/L) (O₁, O₂ and the cross terms) are numerically about 10⁻⁴ N.
* The finite-T excess over R(ψ), about 0.11 at L = 8.47, decreases with L. It matches the taper cost R_L − R ≈ 0.7/L (Section 2.5) plus ℓ₁² vs L².

All these zeros are on the line, so this checks normalisation and bookkeeping only, not the off-line mechanism.

### 2.2 S6 in LZ (and KN): the imported BGSTB24 Lemma 5

**Statement** (LZ Lemma 3.1, verbatim from BGSTB24 Lemma 5, re-checked from both LaTeX sources). Let r ∈ L¹(ℝ) be real and even, with supp r ⊂ [−1, 1] and r Lipschitz at 0. Then Σ_{ρ,ρ′: 0<γ,γ′≤T} r̂(i(ρ − ρ′) log T/2π) w(ρ − ρ′) = (T/2π) log T (r(0) + 2∫₀¹ α r(α) dα + O_r(1/√log T)), with w(u) = 4/(4 − u²) and r̂(ξ) = ∫ r e^{−2πiξα}.

**Use and hypotheses.**

* LZ apply the lemma to Q_δ = f_δ ∗ f_δ and to Q_δ″. Both are real, even, C^∞ with support in a compact subset of (−1, 1), hence L¹ and Lipschitz at 0. KN does the same with R_ε = f_ε ∗ f_ε.
* The test functions are fixed while T → ∞, so the O_r(1/√log T) needs no uniformity. The limit δ → 0 (KN: ε → 0) is taken after the lim inf.
* The summation set 0 < γ, γ′ ≤ T is exactly LZ's multiset Z_T. It is invariant under ρ ↦ 1 − ρ̄, which preserves γ and multiplicity.
* z_ρ − z_ρ′ = i(ρ − ρ′) log T/2π, so r̂(z_ρ − z_ρ′) = K(z_ρ − z_ρ′)² when r̂ = K².

**The BGSTB24 proof chain, as read.**

* (pairsum): r̂(i(ρ − ρ′) log T/2π) = ∫ r(α) T^{α(ρ−ρ′)} dα.
* Thm 1: F(α) = T^{−2α}(log T + O(1)) + α + O(1/√log T), uniformly on 0 ≤ α ≤ 1. Its proof uses:
  * Lemma 1: Montgomery's explicit-formula lemma with δ ≠ 0, derived from Landau's formula by the σ ↔ 1 − σ subtraction. Read; correct.
  * Lemma 3: the positivity representation. The integral identity ∫ dt/((1 + t²)(1 + (t + a)²)) = 2π/(4 + a²) for |Im a| < 1 was checked at complex a to 3·10⁻³² (s7 (d)). Positivity is not needed by LZ.
  * Lemma 4: truncation, with error O(x^{1−2η(T log²T)} log³T) + O(x).
  * R(x,T) from [GM87], with BGSTB24's remark: "removed an extraneous factor of log log T … using Lemma 6 there in place of Lemma 7 … the statement there has also been corrected slightly". **[GM87] was not inspected, and this step was not re-derived.**
  * The KV region, to make the Lemma 4 error O(x) for √T ≤ x ≤ T.
* The proof of Lemma 5 from Thm 1 is short, uses the Lipschitz condition at 0, and is correct as read.

**Why KV is needed in BGSTB24 Thm 1, and why it is not load-bearing for LZ** (s7 (e); P2-N1).

* At x = T the Lemma 4 error relative to x is e^{−2η log T} log³T.
  * With η = c/log t it is ≈ e^{−2c} log³T, which is unbounded. So a classical region would not give BGSTB24's uniformity up to α = 1.
  * With KV it tends to 0 eventually, but only for astronomically large T. For c = 0.05 the exponent changes sign near log T ≈ 10¹⁰ (s7 (e)). That is irrelevant for an asymptotic theorem.
* LZ's and KN's test functions have supp Q_δ ⊂ [−1 + 2ε₀, 1 − 2ε₀] for some ε₀ > 0, because f_δ ∈ C_c^∞((−1/2, 1/2)) has compact support inside the open interval. So only F(α) with |α| ≤ 1 − 2ε₀ enters.
* There, Lemma 4's error with the trivial bound δ + δ′ ≤ 1 (β ≤ 1, from the Euler product) is O(x log³T) = O(T^{1−2ε₀} log³T) = o(T).
* Montgomery's original unconditional R(x,T) evaluation, as quoted in BGSTB24, has error O(x log x) = o(T) on that range.
* On this reading, neither the KV region nor the [GM87] endpoint correction is needed for LZ Thm 1.1 or KN. They are inherited formally by citing the full BGSTB24 statement. This was not written out line by line. It refines ARCHITECTURE.md F4 and does not affect correctness.

**Finite-T calibration** (s6_zero_side_data.out, part (B); all zeros 0 < γ ≤ T; MT window with taper δ = 0.05, C_δ = 1.365753).

| T | N(T)/((T/2π) log T) | S_w/((T/2π) log T) | S/N(T) | Fejér S_w/((T/2π) log T) |
|---|---|---|---|---|
| 10⁴ | 0.6919 | 0.78013 | 1.15182 | 0.77070 |
| 3·10⁴ | 0.7247 | 0.83241 | 1.17127 | 0.82104 |
| 74920.8 | 0.7472 | 0.86946 | 1.18515 | 0.85647 |

* All ratios increase towards the asymptotic values: C_δ, and 4/3 in the Fejér case. Convergence is slow: the O(1/log T) density factor N(T)/((T/2π) log T) is still 0.75.
* The off-diagonal sum is ≈ Σ_γ ∫ K²(u) ρ_γ (1 − sinc²(ρ_γ u)) du, with rescaled density ρ_γ = log(γ/2π)/log T < 1, so it approaches its limit ∫K²(1 − sinc²) = C − 1 from below.
* This is expected behaviour, not an issue (P2-N2). It shows that **no finite-height reading of "2/3" is available from either proof.** For example, 2 − S/N(T) ≈ 0.81 at T = 7.5·10⁴ is not a bound on anything, because the theorem's error terms are not explicit.

### 2.3 S7: LZ's exact removal of the weight

**Statement.** Q = f ∗ f and r_{δ,T} = Q_δ − Q_δ″/(4 log²T). Then r̂ = (1 + π²z²/log²T) K², and at z = i(ρ − ρ′) log T/2π one has K(z)² = r̂(z) w(ρ − ρ′), equation (3.3). Applying Lemma 3.1 to the two fixed functions Q_δ and Q_δ″ gives the unweighted sum.

**Checks.**

* *The identity.* The sympy difference is 0 for symbolic complex D = ρ − ρ′ (s7 (a)). Direct quadrature with LZ's own construction (MT profile, δ = 0.1) at six complex D, including D = 0.3 + 0.7i, −0.7 + 1.9i, 0.9 and −0.45 + 3.3i, gives relative error ≤ 1.1·10⁻¹⁰. At D = 12i the error is 1.1·10⁻⁵, but there |K|² = 6·10⁻⁷ and the error is absolute quadrature error.
* *Well-definedness.* w(ρ − ρ′) is defined: 4 − (ρ − ρ′)² = 0 would need |Re(ρ − ρ′)| = 2, but |β − β′| < 1. The identity holds for **every** pair, on or off the line.
* *The Q″ term.* Its Lemma 3.1 main coefficient is Q″(0) + 2∫₀¹ αQ″ = Q″(0) + 2Q(0), by integration by parts, since Q′(1) = 0. Numerically both sides give −40.0035099695 vs −40.0035099689 (s7 (c)). After the factor 1/(4 log²T) the term is O(T/log T) = o(N), as LZ state.
* *KN's use.* KN Prop 3.1 uses the same identity and is verified by the same computation.

**Cross-check.** AF need no weight, because the Weil form is unweighted. S7 therefore has no AF counterpart and no shared lemma.

### 2.4 S8: the window constants

* *R(ψ₀) and C(f_MT).*
  * R(ψ₀) = 1 + 1/3 = 4/3 (sympy, exact).
  * C(f_MT) = C_MT symbolically: the sympy difference evaluates below 10⁻¹⁶⁵, and the stationarity d²/dt²[f + ∫|t − x| f] = 0 is exact. This is AF Lemma 5.6 and LZ's citation of [Mon75].
* *LZ's limit C_δ → C_MT.*
  * C(·) is continuous in L¹ ∩ L² on functions supported in [−½, ½], since |s − t| ≤ 1.
  * Numerically, (C_δ − C_MT)/δ → 0.708, so the convergence is linear. C_δ > C_MT always, consistent with [CCLM17, Cor. 14].
* *AF's T-dependent analogue.* The taper of width 1 is width 1/L in scaled units.
  * The finite-L main-term ratio R_L satisfies L(R_L − R) → 0.64 (flat) and 0.71 (MT), the same constant as LZ's δ = 1/L.
  * So the asymptotic constant is R(ψ), and the finite-T penalty is O(1/L).
* *Optimality.* The MT optimality ([CCLM17]) is cited by AF and LZ but is not needed for the lower bounds.
* *KN's closed form (eq:C).* C(f) = 4/3 + ½Σa_j² + π⁻²Σ((−1)^j a_j/j² − a_j²/(4j²)) for f = 1 + Σ a_j cos(2πju).
  * It was derived symbolically with three terms, and all cross terms a_j a_k (j ≠ k) vanish.
  * It matches KN's three stated values.
  * The margins to KN's rational upper bounds C₀, C₀′, C₀″ are small but positive: 4.2·10⁻⁸, 1.3·10⁻⁷, 1.7·10⁻⁷. The double-quadrature error of the |s − t| kernel (about 2·10⁻⁷) exceeds the first margin, so the margin claims rest on the exact closed form at 30 digits, which is what KN use.

### 2.5 S9: counting bookkeeping

* **AF §6.**
  * (i): rank P₁ ≥ 2 tr P₁ + 4(tr G̃ − tr P₁) − 4(s₂ + p) − ‖G̃‖² ≥ 4 tr G̃ − 2N(I′) − ‖G̃‖², using tr P₁ + 2(s₂ + p) ≤ s₁ + 2s₂ + 2p ≤ N(I′).
  * (ii): 3s₁ + 4(s₂ + p) ≥ 4 tr G̃ − ‖G̃‖², minus s₁ + 2s₂ + 2p ≤ N(I′), gives 2(s₁ + s₂ + p) ≥ (3 − R − o(1))N. N_d ≥ s₁ + s₂ + 2p ≥ s₁ + s₂ + p.
  * Both identities are checked in sympy.
* **AF cumulative form** ("summing over dyadic windows"; Remark 6.1 rate). For fixed ε choose T_ε. Then N₀ˢ(0, T] ≥ Σ_{j: T/2^j ≥ T_ε} N₀ˢ(T/2^j, T/2^{j−1}] ≥ (2 − R − ε)(N(T) − N(T_ε)).
  * For the rate, the windows with T/2^j ≥ √T have log(T/2^j) ≥ ½ log T, so they lose ≪ (log log T/log T) N(T). The rest contribute N(√T) ≪ √T log T.
  * Boundary conventions ([T, 2T) vs (T, 2T]) cost O(log²T).
  * Verified.
* **LZ Thm 1.1.**
  * (2.4)–(2.6) applied to Z_T give N₀ˢ ≥ 2N − ΣK², N_d ≥ (3N − ΣK²)/2 and N_s + N₀ ≥ 3N − ΣK².
  * For (2.7), the hypothesis ΣK² ≤ A|Z| with 1 ≤ A < 2 is met by A_T := ΣK²/N(T). A_T ≥ 1 by (2.4), and A_T → C_δ < 2. The bound is decreasing in A, so the lim inf is (5 + 2√2 − 2C_δ)/(3 + 2√2). LZ's text compresses this, correctly.
  * The constants C₀, C₁ and C₂, and the t = 2 + √2 balancing (b₁, b₂, b₃), are verified in sympy.
* **KN Cor 1.2.** N ≥ N_s + 2(N_d − N_s) gives 2q − 1. Verified.
* **Operator-level tests** (s9 (c)). There were 5982 random conjugation-invariant configurations: on-line multiplicities 1–4, off-line pairs of multiplicity 1–2, KN window-1 and MT kernels.
  * The nonzero spectrum of A = Σ ν_z F_z⟨F_{z̄}, ·⟩ was computed as that of diag(ν)·P·Gram, with Gram_{w,u} = K(u − w̄). It is real to 3.6·10⁻¹⁵.
  * tr A² = Σ ν_z ν_w K(z − w)² holds to 7·10⁻¹⁵.
  * The minimum slack of N₀ˢ ≥ 2N − tr A², N_d ≥ (3N − tr A²)/2 and N_s + N₀ ≥ 3N − tr A² is ≥ −9·10⁻¹⁶, which is rounding at equality cases.

### 2.6 S10: Knausgård's certificate layer

**Prop 3.1 (energy).** tr A² = (C(f_ε) + o(1))N for fixed ε. This is BGSTB24 Lemma 5 plus LZ's weight device (Sections 2.2–2.3). C(f_ε) → C(f) by L¹/L² convergence. Verified.

**Lemma 2.1 (threshold).** For P ⪰ 0, Q with at most p positive eigenvalues, and A = P + Q: tr A² ≥ 2c tr A − 2c tr P + tr φ_c(P) − c²p.

* Re-derived: tr(PQ₊) ≥ 0 gives the cross term; x² ≥ 2cx − c² handles Q₊; and the X = P − cI step gives tr(X₊ − Z)² ≥ 0.
* At c = 2 it contains AF Lemma 3.2.
* ARCHITECTURE.md tested it on 2·10⁴ random matrices.
* **(eq:key)** follows by inserting tr A = N, tr P = n₁ + 2n₂ and p = h + k, and rewriting with tr D² = n₁ + 4n₂ (sympy).
* Operator-level tests of (eq:key) for c ∈ {2, 3, 3.35}, of (eq:key2), and of Lemma 6.1 (two levels, t ∈ {c, c + 0.4, 27/8}) gave minimum slack ≥ −4.6·10⁻¹⁴ (s9 (c)).

**Lemma 2.2 (pinching).** Jensen's inequality for the spectral measure at an eigenvector of each block. Correct.

**Lemma 2.3 (separated points).**

* Σ v_i v_j ŵ(y_i − y_j) = ∫ w |E|² ≤ ∫ g |E|² = Λ‖v‖², because ĝ vanishes off (−θ, θ) and is continuous with ĝ(±θ) = 0.
* I re-derived that the Fourier transform of (2/θ) cos(πξ) 1_{|ξ|≤θ/2} is sinc(θ(u − ½)) + sinc(θ(u + ½)), and that Λ = γ₀∫Ψ² = (2γ₀/θ)(1 + sinc θ).
* 4000 random and near-lattice θ-separated sets per window gave max λ_max = 1.442, 1.474 and 1.437, below Λ = 1.671, 1.789 and 1.679.
* g ≥ f is needed on I only, since f = 0 off I and g ≥ 0.

**Lemma 2.4 (close pairs).** For fixed trace, φ_c(λ₊) + φ_c(λ₋) is monotone in the eigenvalue spread, by convexity. Correct.

**Lemma 2.5 (transfer) and (eq:transfer8).** The counting was verified:

* a pair at index distance s appears at positions (i, i + s), with total weight ≤ 2dd′ by (eq:budget);
* there are ≤ 6m pairs, at ≤ 8ε each, giving 48εm (eight points: 7m pairs × 2ε gives 14εm);
* each gap lies in ≤ 6 (or 7) frames;
* exactly 6 (or 7) points are left out at each position, giving −6x₂ (or −7x);
* the corrections telescope via −B_{≤4} = B₅ (or −B_{≤5} = B₆).

End to end, 3000 random θ-separated labelled sequences with m = 7…59 gave min(lhs − rhs) = 0.50 > 0 (s10 (f)).

**Thm 2.6 and Prop 5.2 (Gram bounds).** Verified:

* the maximal close-pair matching leaves a θ-separated set S;
* the pair blocks are bounded via Lemma 2.4 with |U_ij| ≥ √β − η;
* G_SS ⪯ cI follows from U_SS ⪯ (c/2)I and D ≤ 2I;
* |U² − K²| ≤ 3η, using |K| ≤ 1.

**Thms 3.2, 5.1, 6.2 (certificate principles).**

* All identities hold in sympy: ν + μ = 2c − 1 − x₁; 2ν + μ = 4c − 4 − x₂; 3ν + μ − c² = r_h; 2ν + 2μ − c² = r_k; 2c − ν = 3 − x₁ + x₂; 3 − C − b + xs = 1 + s; 2t − t²/3 − ½(4t − t²) = t²/6; 4t − t²/2 = 2e₀.
* At t = 2 + √(2 − 2x₁), Thm 6.2(b) reduces to Chandru's closed form. At (0, 0, 0) with t = 2 + √2 it reduces to LZ's C₂.
* The spread bound spn(Y) ≤ TL/2π = N(1 + o(1)), with L = log T, is correct.
* Every numerical hypothesis was checked in exact rationals (s9 (b)): μ > 0; ν, r_h, r_k ≥ 0; 2 + 2√β < c; 2dd′β ≥ x_d + x_{d′}; β ≥ x; Λ < c/2 (1.671052 < 1.675, margin 0.004); Λ < 2; t ≥ c; 4t − t² ≥ 2 + 2x₁ (2.109375 ≥ 2.1087); 4t − t² ≥ 2 + 2x (2.109375 ≥ 2.10905); e₀ > 1 + x.

**Appendix A data** (s10 (a)–(c)), parsed directly from `knausgard839tab1/2/3.tex`. The following reproduce:

* the budgets (sums ≤ 2dd′, with slack 0–4·10⁻⁶);
* the reward sums x₁ = 0.054350, x₂ = 0.069433 and κ_{i,1} ≤ κ_{i,2};
* the three Ω values;
* the trivial-frame thresholds;
* the β lower bounds (Lipschitz grid, |dK²/dt| ≤ 2π, h = 10⁻⁶);
* the f ≤ g margins (Lipschitz grid, h = 10⁻⁶);
* the three Λ values.

All of these computations are double-precision floating point, not directed rounding.

**Props 3.3, 5.3, 6.3 (local inequalities).** These were **not proved here.** I evaluated (eq:local) with exact K at 2·10⁶ random frames for each of the 2⁷ labellings of window 1, and (eq:local8) and the window-3 inequality at 2·10⁶ frames each. Gaps were biased to θ, 1, 3/2 and 2 plus exponential tails. Nelder–Mead minimisation then started from the worst samples (s10 (e)).

| Window | Minimum slack | At |
|---|---|---|
| 1 | 9.8·10⁻⁵ | all labels 1, gaps ≈ (1.04, 1.03, 1.04, 1.04, 1.05, 1.86) |
| 2 | 1.3·10⁻⁵ | gaps ≈ (1.03, 1.04, 1.97, 1.04, 1.97, 1.04, 1.03) |
| 3 | 1.65·10⁻⁴ | — |

The near-tight minima at near-integer spacings are what an optimised certificate should look like. This is consistency evidence for the transcribed data and the stated inequalities, not a proof. The proofs of record are KN's branch-and-bound searches (6.05·10⁷, 5.35·10⁸ and 5.73·10⁸ boxes) and the Lean development with `native_decide`, neither replayed.

## 3. Findings (part 2)

| ID | Class | Location | Finding | Witness | Effect |
|---|---|---|---|---|---|
| P2-F1 | typo_or_presentation (witness) | AF Prop 5.2 (statement) and its E₂ bound; Thm 5.7 error term | The proof as written yields an error O(N log L/L), not the stated O(N log L/L²). The step \|E₂\| ≪ L³B²l log L, divided by (aL²)², is ≍ B² log L ≥ 16X log L, while N(T,2T) ≍ XL. E₁ does give N log L/L². Thm 5.7's O_χ(L⁻¹) should correspondingly read O_χ(log L/L). This is consistent with AF Remark 6.1, which attributes the rate log log T/log T to Prop 5.2. The stated bound may still be true, since the displayed bounds are crude for a C^∞ taper, but the written proof does not give it. | s6_prime (d): E₂-bound/(L⁴N) = 4.7, 2.0, 0.80 at T = 10⁴, 10¹², 10⁴⁰, tracking log L/L, not log L/L² | None: still o(N). |
| P2-F2 | typo_or_presentation (justification gap, not load-bearing) | AF Prop 5.5, term M[P_X,Π_X] | "The remaining three bounds follow by inserting these sup bounds" does not give ≪ L²√X for M[P_X,Π_X]. The sup bounds give ≤ T·(3√X/T)·(3√X/π)·2πbL = 18bLX, and LX/(L²√X) = √X/L → ∞. The weaker O(LX) suffices: after division by a²L² it is O(N/L²). The claimed bound appears true. Writing M ≈ −2Σ a_n g(log n)∫_I Π_X cos(τ log n), one has \|∫\| ≪ √X/(T(L − log n)), and the upper bound in (5.2) gives g(log n) ≤ L − log n, which suggests O(X/T). | s6_prime (e): at T = 3·10⁴, M[P_X,Π_X] ≈ 5.4·10⁻³, against L²√X ≈ 5.0·10³ and LX ≈ 4.0·10⁴ | None. |
| P2-F3 | typo_or_presentation | AF (5.2) lower bound; end of Prop 5.4 proof; (5.3) | (i) 1_{[−L/2+w, L/2−w]} ≤ φ² holds only for ψ₀; for ψ_MT, φ²(u) = cos(√2u/L) < 1 on the bulk. (ii) The last paragraph of Prop 5.4's proof concludes "the second form", which is absent from the statement (a leftover). (iii) C_χ := ‖(φ²)″‖₁ is also used to bound \|φ̂(r)\|, which needs ‖φ″‖₁. Thm 5.7 uses the general rescaling g(y) = L(ψ∗ψ)(y/L) + O(1) and the upper bound g ≤ (L − \|y\|)₊, which are valid for both windows, so nothing depends on (i)–(iii). | algebra | None. |
| P2-N1 | no_issue_found (input-set refinement) | LZ Lemma 3.1 / BGSTB24 Thm 1; KN Prop 3.1 | KV enters BGSTB24 only to make the Lemma 4 error O(x) up to x = T, i.e. α = 1; the classical region would leave ≈ e^{−2c} log³T. The [GM87] "slight correction" also concerns the range up to α = 1. LZ's and KN's test functions have f ∗ f supported in [−1 + 2ε₀, 1 − 2ε₀]. There the trivial bound gives Lemma 4 error O(T^{1−2ε₀} log³T) = o(T), so on our reading neither KV nor the endpoint correction is load-bearing for the CRIT23 constants. Not written out line by line. | s7 (e) | Strengthens ARCHITECTURE.md F4. |
| P2-N2 | no_issue_found (finite-T calibration) | AF Thm 5.7 normalisation; BGSTB24/LZ normalisation | On the first 10⁵ zeros, AF's zero side and full prime side agree to 3·10⁻⁵, and AF's main terms reproduce the full prime side to 2·10⁻⁴. LZ-normalised sums converge slowly from below (S/N = 1.185 vs C_δ = 1.366 at T = 7.5·10⁴), as the density factor log(γ/2π)/log T predicts. Neither proof gives a finite-height proportion. | s6_zero (A), (B) | None. Guards against a finite-T misreading. |
| P2-N3 | no_issue_found_in_inspected_portion (data) | KN §3, §5, §6, App. A | Every certificate datum and hypothesis was reproduced: budgets, x₁, x₂, x, Ω, thresholds, β, Λ, f ≤ g, C(f) closed forms and all six rationals. Sampling plus local minimisation of the three local inequalities found no violation; the minimum slack is 1.3·10⁻⁵ (window 2). The branch-and-bound proofs were not replayed. | s8 (d), s9 (b), s10 | — |
| P2-N4 | no_issue_found_in_inspected_portion | AF Props 5.3, 5.4 (main terms, O₁, O₂), 5.5 (other three terms), Lemma 5.6, Thm 5.7 (main term), §6 incl. dyadic summation; BGSTB24 Lemmas 1, 3, 5 (read), statement of Lemma 4 and Thm 1; LZ Lemma 3.2, Rem 3.3 (its transcription of AF Thm 5.7 is consistent, with φ̂_AF(ξ) = φ̂_LZ(ξ/2π)), Thm 1.1 proof; KN Lemmas 2.1–2.5, Thm 2.6, Prop 3.1, Thms 3.2, 5.1, 6.2, Prop 5.2 | No error found beyond the items above. | Section 2 | — |

No finding in part 2 is classified verified_error, suspected_gap or missing_hypothesis. Part 1's P1-F1 (a local proof step in AF Prop 4.2, repaired there) does not propagate into S6–S10. S6 does not use the per-zero tail bound or the value of d.

## 4. AF vs LZ vs KN, step by step (S6–S10), and the combined verdict

| Step | AF | LZ | KN | Shared unverified lemma? | Status |
|---|---|---|---|---|---|
| S6 | own proof, §5: Weil EF, MV Hilbert inequality, Mertens; T-dependent test function; uniform constants | BGSTB24 Lemma 5 (refereed): Landau EF, Montgomery's method, [GM87]; KV formally | as LZ (Prop 3.1) | No. Independent derivations; common ground is classical (Riemann–von Mangoldt, Stirling, Mertens, MV-type mean values). | verified (AF error terms read; P2-F1/F2 harmless); BGSTB24 Thm 1 error terms not re-derived |
| S7 | not needed | Lemma 3.2: r = Q − Q″/(4 log²T) | same device | — | verified exactly |
| S8 | Lemma 5.6; taper gives R_L = R + O(1/L) | C_δ → C_MT (δ → 0) | eq:C closed form; rational upper bounds | No. Classical calculus. | verified |
| S9 | §6 (i), (ii); dyadic summation | Thm 1.1 proof via (2.4)–(2.7) | Thms 3.2, 5.1, 6.2; Cor 1.2 | No. | verified |
| S10 | — | — | Lemmas 2.1–2.5, Thm 2.6; computer-assisted Props 3.3, 5.3, 6.3 | KN-only content | algebra verified; data reproduced; searches not replayed |

**Combined verdict (parts 1 and 2).**

* The headline bounds are liminf N₀ˢ/N ≥ 2/3 (flat) and ≥ 0.67250… (MT), and liminf N_d/N ≥ 5/6 and ≥ 0.83625….
* They have two proofs, AF and LZ, that share no unverified lemma. The algebraic cores were proved independently: von Neumann/inertia in AF, flag/Bessel in LZ. So were the analytic cores: AF §5, and BGSTB24 + LZ Lemma 3.2.
* Every load-bearing step S1–S9 was re-derived. Every stated constant was recomputed from its formula.
* The only items not independently verified are routine:
  * the error terms of BGSTB24 Thm 1, which rest on [GM87] and are refereed, and by P2-N1 are not needed at the endpoint;
  * the Lean builds.
* KN's improvements to 0.673538… (simple, on the line) and 0.839005… (distinct) additionally depend on three computer-assisted finite inequalities. These were not replayed. They were only probed by sampling, without violation.
* All findings in either part are presentation-level: P1-F1 is a local proof slip with a repair. None affects a stated result.

## 5. Reproduction

Scripts are in `research/exploratory/riemann-observatory/experiments/code/claims_2026/crit23_part2/`. Run each from that directory with `python3 -I <script>`; outputs are `<script>.out` beside them. Environment: Python 3.13, numpy 2.5.3, scipy 1.18.1, mpmath 1.3.0, sympy 1.14.0.

`s10_kn_local.py` takes one argument: the directory holding KN's extracted LaTeX tables, here the part-2 scratch copy `…/scratchpad/audit2026/kn_src_2610.08965v1_part2/x`. Re-extract that copy from the arXiv e-print to reproduce.

| Script | Steps / checks | Runtime (4 vCPU) |
|---|---|---|
| `s6_prime_side_af.py` | S6 (AF): Lemma 5.1 sums; Thm 5.7 partial summation and constant; Prop 5.2 exponent bookkeeping (P2-F1); Prop 5.5 M[P_X,Π_X] (P2-F2) | 2.7 min |
| `s6_zero_side_data.py` | S6: zero side vs full prime side vs main terms (AF); LZ/BGSTB24 normalisation; Fejér case | 1.6 min |
| `s7_weight_removal.py` | S7: exact identity (sympy), complex-z quadrature, Q″ term; BGSTB24 Lemma 3 integral; KV vs classical region | 3 s |
| `s8_window_constants.py` | S8: R(ψ₀), C(f_MT) symbolic; C_δ → C_MT; AF finite-L R_L; KN eq:C symbolic and margins | 6 s |
| `s9_counting.py` | S9/S10c: 21 sympy identities; KN rationals and hypotheses (exact); operator-level random tests | 5 s |
| `s10_kn_local.py <tabdir>` | S10: data parsing; Ω, thresholds; β, f ≤ g (Lipschitz grids); Lemma 2.3; local-inequality sampling and minimisation; transfer lemma | 5.3 min |

SHA-256 of the sources used by part 2 (e-print tarballs as downloaded for part 2; PDFs as in ARCHITECTURE.md):

```text
d6a2e5ca0b1d2cece6597ccdfc6cbb0f458739113f28ca4ce84ac307de6b682d  AF  2608.13637v2 e-print
70370356f7010c422c92b6e467e86e8e9fe5a40696a5990e61f05582d4b3cf59  LZ  2609.02882v2 e-print
60fb628fb12bdc1ca28d6e849ce9180e9fbcc8b482021bb62d2c92b7827ac3cb  KN  2610.08965v1 e-print
6ed758704d6f1735f31953d698b6ed8b00c4e13b1fa0b54015aa1d5ad45c49ef  BGSTB24 2306.04799v1 e-print
b6c7e1d3a44fff46c572a742b6dee919ea29e6e1123c8621da785ad57c35ebf8  knausgard839tab1.tex
fc6e1afb1ab3d2e14dec2639ad5b2e5546d2a721ec57531a7d983af69225694e  knausgard839tab2.tex
66d922ec7e05eb3828e0d12fb442fe6ea6d0bf070bc49f723fed81610d49f7ae  knausgard839tab3.tex
6de3b156342e7b4a802c34f8ef40432567e9dabe006938da04233f19fc4ef444  AF PDF
305df7fcbbf96e61ccca2cbae13dcb2b7f9251b054d02dd0c78551982621046b  LZ PDF
aedf2891fbe0e55cde9ad85d4ecd8714a75dca1a258abd290d6b4aaf8a08200f  KN PDF
133071c4d85c875fe9b1a7d4001f22d7174270ab8f1fa8e6cee6178d20276ee9  BGSTB24 PDF
4d364a6ba8043e878409fe7d2ce89d2e9c6a29ba48dc1446b54c468579715603  zeta_zeros_1_100000_arb.tsv.gz
```

SHA-256 of the part-2 scripts and outputs (final runs):

```text
b891dfdacf8b634734766b462788a9481843c996d18a1dacadb029d60d3b702c  s6_prime_side_af.py
91291b87b10a029dad3aef66c3c776d3d0a08ffdbc56d15a02983f87f5c5b62e  s6_prime_side_af.out
892fa26ea1a3c9ecc90454f11d5cfafa64cc3f1c65b986c3ee4a6af7f3d508fa  s6_zero_side_data.py
06492870b7d4f624a92cc7a1500038c96d87f376355e7f7b2fc6272187a8aca4  s6_zero_side_data.out
71018ad8ae038f58a58a84c0d13460383027d16b1a3095f1881b3d0d58d1e537  s7_weight_removal.py
b09ae9e335d5cbf1a98e6d281854c77ea6a01011ae529712276cfb0be7f1a9e1  s7_weight_removal.out
2fa8cd8f8ee44ad4de1f0c9478d88935a0186afffbe48e3867aa434ea0068388  s8_window_constants.py
16ae22c4900719700c004b2d8e17a76d642a8ee030bd4bce0a00b58965b3578a  s8_window_constants.out
42c263b46c07b56373f9226c37d7f78e6732260687491caa33f2322f50685ec4  s9_counting.py
4700511a66a388d6dc3d494aa2773b2e77a7a3e6cf3a9df29798ac4c86601ef1  s9_counting.out
S10_PY_HASH  s10_kn_local.py
S10_OUT_HASH  s10_kn_local.out
```

The scripts were corrected in three places during the audit. All three were numerical or wording artefacts in the audit's own scripts, not issues in any paper:

* The BGSTB24 Lemma 3 integral first showed a 7·10⁻² discrepancy at a = 5 + 0.99i. The cause was a pole 0.01 from the real axis. With a breakpoint at t = −Re a the difference is 3·10⁻³².
* The first KV printout stopped at log T = 1.2·10⁴, before the asymptotic regime. It now runs to log T = 10¹⁵.
* An output label in s10 was reworded so that no floating-point bound is called "certified".

## 6. Not done in part 2

* No Lean development (AF, LZ/AxiomProver, KN) was built or kernel-checked. KN's `native_decide` searches and C++/Python reference verifiers were not run. Their tables were read as data only.
* The error analysis of BGSTB24 Thm 1, Lemma 4 (Montgomery's truncation argument with the x^{δ+δ′} factor) and the [GM87] mean value were read, not re-derived. [GM87] itself was not inspected. P2-N1 explains why the endpoint part is not load-bearing for LZ/KN; that observation was not written out line by line.
* AF Theorem B (Dirichlet L), Remarks 7.1–7.2 and §7.2 (ceilings), and KN §7 (ceilings) are outside CRIT23 and were not audited.
* Nothing here concerns the zeros not covered by the certificates. The theorems are insensitive to o(N) off-line zeros (AF §1.4) and are proportions in the limit T → ∞ only.
