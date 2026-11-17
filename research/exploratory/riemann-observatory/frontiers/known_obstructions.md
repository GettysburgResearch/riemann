# Known obstructions: an atlas

```text
Status: SYNTHESIS (exploration layer). Each entry states an obstruction exactly, with its status and source,
        and the class of arguments it rules out. Elimination statements have the form "no argument using only
        P1..Pk can prove X". They are only as strong as the witness behind them. Each says which hypotheses a
        valid proof must use; none says RH is false or hard. RH is open. Quasi-RH and the 2/3 result are
        unrefereed 2026 claims (11/12 audited by the Observatory with no error found; 7/8 not audited; Lean
        claimed, not replayed).
Scope: countermodels; generalized primes; false positivity conditions; heat flow; parity; mollifier and
        density-currency ceilings; the bandwidth-one ceiling of the 2026 critical-line method; finite
        detection horizons; Weil-window certificate costs; the quasi-RH method floor; Siegel-method limits;
        zero-density and zero-free-region barriers; correlation barriers; function-field transfer barriers;
        spectral-realization barriers; host-programme obstructions; verified obstructions from the
        discovery register.
Exact sources or dependencies: frontiers/ledger.jsonl (LED, corrected values); frontiers/research_programs.md;
        connections/connections.jsonl (CON; the corrected form is used for needs_correction items, and
        vocabulary_only items are excluded); connections/repository_bridge.jsonl (BRG);
        audits/verified_findings.md (FND); audits/quasi_rh/DOSSIER.md §2 and §4; audits/claims_2026/CRIT23 §7
        and SIEGEL §7; campaigns C1 (REPORT + SKEPTIC), C2 (REPORT + SKEPTIC), C3 FINAL, C4 (REPORT + SKEPTIC),
        C5 (REPORT + SKEPTIC); history/abandoned_approaches.md §2 and §14; corpus/bibliography.jsonl (PAPER).
What was actually run: the sources were read. One mpmath script re-evaluated these quoted constants: kappa_c,
        lambda*, C_MT, 3 - 2*sqrt2, C(Delta), beta(n,h) and B(l). All agree with their sources. No new
        computation of zeros was run.
Smallest remaining gap: several obstructions rest on unrefereed or author-stated ceilings (OB-15b, OB-17a,
        OB-18e/g) or on Observatory sketches [O] (OB-18b-d); these are flagged in place. No entry has had human
        expert review.
```

Labels follow `frontiers/missing_lemmas.md`: THEOREM (refereed or unrefereed), AI-generated unrefereed, CONDITIONAL, Observatory-proposed, [O], HEURISTIC, CONJECTURE, NUM-RIG, NUM-NONRIG.

**Meta-lemma (C2-24; THEOREM, elementary logic; skeptic upheld).** Suppose a function W satisfies predicates P1..Pk, with the same normalisation and quantifiers as stated for ζ, and has a zero off its symmetry line. Then the implication P1 ∧ … ∧ Pk ⇒ RH_W is false. So any argument whose only ζ-inputs are P1..Pk is invalid.

Caveat (Hamburger 1921): steps that use ζ's exact functional equation (Γ_R(s), conductor 1) together with the Dirichlet-series property already pin down c·ζ. The meta-lemma bites only on steps that do not use the conductor or the Γ-type. The C2 skeptic corrects the campaign's "hitting-set corollary" C2-31, which is **downgraded** to a protocol heuristic: a proof must use some property each witness lacks, not necessarily the Euler product.

---

## Part I. Countermodels

### OB-1. Davenport–Heilbronn

**Statement.**
- **Definition.** f(s) = 5^{−s}[ζ(s,1/5) + κζ(s,2/5) − κζ(s,3/5) − ζ(s,4/5)], with κ = (√(10−2√5) − 2)/(√5 − 1) = 0.2840790438…. Equivalently f = ((1 − iκ)/2)L(s,χ) + ((1 + iκ)/2)L(s,χ̄) mod 5, with χ(2) = i.
- **Functional equation.** ξ_f(s) = (5/π)^{s/2}Γ((s+1)/2)f(s) = ξ_f(1−s). IMPORTED (Titchmarsh §10.25); PAPER-0417; C2-02.
- **Certified off-line zeros.** NUM-RIG (C2-03; C3-D14; C2 skeptic re-certified by the argument principle):
  - 0.80851718245663738555… + 85.69934848537759217…i;
  - 0.6508300806… + 114.1633427…i;
  - 0.5743560504… + 166.4793059…i;
  - 0.7242576946… + 176.7024612…i;
  - 0.8695305796… + 240.4046723…i.
- **Completeness for 1 ≤ t ≤ 300.** These are exactly the off-line zeros there: the box count is 214 = 204 sign changes + 2·5 (skeptic F6, NUM-RIG). The zero at 85.70 is rigorously the lowest off-line zero.
- **Right edge.** f ≠ 0 for Re s ≥ 1.13514. THEOREM, Arb-certified (C2-05).
- **Further facts.** IMPORTED: infinitely many zeros in σ > 1. The off-line count in each strip 1/2 < σ₁ < σ₂ < 1 is ≍ T, which is density zero among the ≍ T log T zeros (LED-LFUN-14 corrected; the frontier's "positive density" was wrong). A positive proportion of zeros lie on the line (Karatsuba).
- **Refuted claim.** The assertion that all DH zeros are on the line (Liu–Wu, arXiv:2503.24275) is refuted with a witness (C2-07, skeptic upheld).

**Eliminates (C2-25 SP-1, as corrected by the skeptic).** No argument using only the following can prove RH:
- an ordinary Dirichlet series with a₁ = 1, real |a_n| ≤ 1, absolutely convergent in σ > 1;
- entire continuation;
- a self-dual degree-1 Riemann-type functional equation;
- order 1 with a Hadamard product;
- ≫ T(log T)^{1/2−ε} zeros on the line;
- Bohr almost periodicity.

The same holds for arguments using only a positive proportion of zeros on the line (SP-9). Low-degree Jensen and Turán data also cannot detect off-line zeros: for ξ_f, Turán holds for k ≤ 78 and every J^{d,n} with d, n ≤ 40 is hyperbolic despite the zero at height 85.7 (C2-18; Turán signs NUM-RIG, hyperbolicity NUM-NONRIG; the skeptic did not replay the DH part).

AF state that their inputs also hold for DH (AF §1.4, author-stated, not checked), which is why the 2026 critical-line certificate cannot reach RH (OB-15).

**Does not eliminate.** Steps that use multiplicativity of the coefficients of 1/L. The quasi-RH proof uses multiplicativity at four load-bearing points (QRH dossier §2.1 [O]).

### OB-2. Epstein zeta functions

**Statement.**
- **Z for x² + 5y² (D = −20, h = 2).**
  - 35 certified off-line zeros with 2 ≤ t ≤ 200, rigorously complete: the count is 253 = 183 + 2·35 (C2-09 with skeptic F6; NUM-RIG).
  - The lowest is 0.93296969748541410476… + 15.66824953127847…i.
  - Zeros with Re s > 1 exist. The lowest certified is at t ≈ 1193.94640 with σ ≈ 1.0110493; others are near t ≈ 4108.108 (and up to 9.4·10⁵), plus 3587891.15 (C2-10; skeptic F4). The campaign's "first found near 3.6·10⁶" was misleading.
  - Zero-free for Re s ≥ 1.17816 (C2-11, THEOREM).
- **Z for x² + 57y².** A real off-line zero at 0.6546512025776227991… (C2-12, NUM-RIG).
- **Rectangular forms.** Real off-line zeros exist for every k > 4πe^{−γ}. THEOREM per C2 skeptic F7, which also finds Bétermin–Šamaj–Travěnec Conj. 1.1 false by 4.2·10⁻²⁰.
- **On the line.** A positive proportion on the line (Rezvyakova; refereed per LED-LFUN-16 corrected).

**Eliminates (C2-25, as reformulated by the skeptic).** Replace (entire, degree 1, |a_n| ≤ 1) by (simple pole at 1, degree 2, 0 ≤ a_n ≪ n^ε). Then the following do not imply RH: a Riemann-type FE, a Dirichlet series over ℕ, a positive proportion on the line. Coefficient positivity alone is not the missing hypothesis.

### OB-3. Synthetic ξ̃ with an injected quadruple

**Statement (C2-15, THEOREM).** Let ξ̃ = ξ·∏_{ρ∈Q}(1 − s/ρ) for a quadruple Q with 1/2 < Re ρ₀ < 1. Then ξ̃ is entire of order 1, real on ℝ, satisfies ξ̃(1−s) = ξ̃(s), and N(T) changes by exactly 2.
- **Li coefficients.** λ_n(ξ̃) = λ_n(ξ) + Σ_{ρ∈Q}[1 − (1 − 1/ρ)^n] (identity).
- The first negative λ_n is at n = 20855 for ρ₀ = 0.6 + 14i. For (0.75, 14), (0.6, 30) and (0.75, 30) it is 7477, 112538 and 40908. These are the skeptic's recomputed values (F3, NUM-NONRIG); the campaign's table was wrong.
- **Jensen.** The "uniform in d" Jensen statement for ξ̃ (C2-17, C2-28) is **downgraded to CONDITIONAL on RH** (skeptic F2). It can be repaired by building on H_{0.2}.

**Eliminates (C2-28 as corrected).** No argument using only the following can prove RH:
- order 1, reality, FE, Hadamard product;
- N(T) up to O(1);
- Turán for k ≤ 78;
- λ_n > 0 for n ≤ 20854.

A valid Li or Jensen proof must use positivity for **all** n (or hyperbolicity at shift 0 for **all** d), with no finite range.

### OB-4. The local-factor countermodel F_c (C2 skeptic F1)

**Statement.** F_c(s) = ζ(s)(1 + c·2^{−s} + 2·4^{−s}) = ζ(s)(1 + a·2^{−s})(1 + b·2^{−s}), with ab = 2 and a + b = c > 0. Elementary; checked numerically (functional-equation defect < 3·10⁻³⁰).
- **Properties it has.**
  - An ordinary Dirichlet series with real, nonnegative, multiplicative coefficients (a_n ≤ 6).
  - An Euler product over the rational primes.
  - A simple pole at 1, order 1.
  - A self-dual degree-1 FE with Γ_R(s) and conductor 4, because 2^s + c + 2^{1−s} is symmetric.
- **Its zeros.** Full vertical progressions on Re s = log₂ a and Re s = 1 − log₂ a. For c = 2(2^{−1/4} + 2^{−3/4}) they lie on Re s = 1/4 and 3/4, e.g. 0.25 + 4.532i.
- **Why it is not in the Selberg class.** It fails only the local axiom: |α₂| = 2^{3/4} > 1.
- **A second defect.** Λ_F(2^k) < 0 for some k; for example F₃ has Λ(4) = −4 log 2.
- **Novelty.** Folklore for the extended Selberg class (Kaczorowski–Perelli). No specific citation was located, so no novelty is claimed.

**Eliminates.** No argument using only the following can prove RH:
- an Euler product over the rational primes;
- a Dirichlet series over ℕ with nonnegative multiplicative coefficients;
- a pole at 1;
- a self-dual degree-1 functional equation with Γ_R.

A valid proof must use at least one of: the Selberg local condition (|α_p| ≤ 1, θ < 1/2), von Mangoldt positivity Λ_F ≥ 0, or conductor 1 with Hamburger rigidity. This refutes the campaign's stated blind spot (C2-00(i), C2-31). The real blind spot is the full Selberg class, not "Euler product + FE + Dirichlet series".

### OB-5. Selberg, Ihara and Hurwitz zeta functions

**Statement (IMPORTED; C2-23; C2-27 corrected; LED-LFUN-19, LED-LFUN-18).**
- **Selberg zeta of a cocompact surface.** It has an Euler product over primitive geodesics, a functional equation and order 2. Its nontrivial zeros satisfy s(1−s) = λ_j, so λ₁ < 1/4 gives real zeros in (1/2, 1), and such surfaces exist. Selberg-zeta RH ⇔ λ₁ ≥ 1/4.
  - Congruence surfaces: λ₁ ≥ 975/4096 (Kim–Sarnak).
- **Ihara zeta.** The RH analogue concerns poles, through λ = q^s + q^{1−s} (skeptic correction). It holds iff the graph is Ramanujan; about 31% of random regular graphs fail.
- **Hurwitz ζ(s, a).** For a ≠ 1/2, 1 it has infinitely many zeros in σ > 1.

**Eliminates (SP-3).** No argument using only the following can prove RH: an Euler product over "primes" of norm > 1; meromorphic continuation; an FE s ↔ 1 − s; nontrivial zeros equal to the spectrum of a self-adjoint operator via s(1−s) = λ. A Hilbert–Pólya proof must give self-adjointness in the γ-parametrisation, or λ ≥ 1/4, or use arithmetic input these lack.

### OB-6. Function-field fake zeta functions (C5)

**Statement.**
- **C5-E1.** THEOREM (existence) with an exhaustive certified census (NUM-RIG; skeptic reproduced all g ≥ 2 counts).
  - Rational functions P/((1−T)(1−qT)) can satisfy the curve FE and an Euler product with integer place counts B_d ≥ 0 for every d, and still violate RH.
  - Over 24 pairs (q, g): 16,354 admissible, 12,787 fakes. Including the degenerate Z ≡ 1 the figures are 16,368 and 12,801 (skeptic correction).
  - Example: q = 9, g = 1, P = 1 − 7T + 9T², with |α|/3 = 1.768.
- **C5-E4.** Fake quadratic-type Euler products over ℙ¹/F_q with |a_v| ≤ 1 and conductor degree 2g + 2 (THEOREM via C5-L2).
- **Prior art for the phenomenon.** Arithmetical semigroups satisfying Axiom A# need not satisfy RH (W.-B. Zhang 1990; Knopfmacher–Zhang). Ihara zetas also exhibit it (skeptic). Only the curve-shaped census is "possibly new".
- **One-sided bounds over F_q.**
  - The lower half, s_r ≤ Cq^{r/2} for all r, implies RH. THEOREM, elementary (C5 skeptic §3.4).
  - The upper half does not: the g = 1 fakes with α > √q satisfy N_r < q^r + 1 for all r (C5-S1).

**Eliminates (C5-OB5).** No proof of the function-field RH can use only the zeta axioms: rationality, FE and an Euler product with nonnegative counts. Geometry beyond them is load-bearing. A purely formal transfer between F_q and ℚ is excluded in both directions; the "both directions" synthesis is HEURISTIC.

---

## Part II. Beurling generalized primes

### OB-7. Euler product + positivity + integer regularity

**Statement.**
- **DMV 2006 (PAPER-0581), IMPORTED.** For every θ ∈ (1/2, 1) there is a discrete Beurling system with N(x) = ρx + O(x^θ) and π(x) = Li(x) + Ω±(x·exp(−c√(log x))). The de la Vallée Poussin region is realized.
- **Zhang 2007 (PAPER-0619).** A system with N(x) = kx + O(x^{1/2}exp(c(log x)^{2/3})) whose zeta has infinitely many zeros on σ = 1 − 1/log t and none to the right.
- **Broucke–Debruyne–Révész (arXiv:2309.01567, Thm 1.1).** For every α ∈ [0, 1) and β ∈ [1/2, 1) there is a system with ψ = x + O(x^{α+ε}) and N = ax + O(x^{β+ε}), both sharp.
- **Broucke Thm 1.6 (LED-ZFR-16).** Zeros on any prescribed convex contour σ = 1 − f(log|t|), with N_P(x) = Ax + O(x^{1/2+ε}).
- **Hilberdink.** max{α, β} ≥ 1/2.
- **C2-21.** Observatory THEOREM, re-derived by the skeptic. An explicit continuous (not discrete) Euler-product system with ζ_Π = (s/(s−1))·exp(−E₁((s−ρ)L) − E₁((s−ρ̄)L)), whose zeros are exactly 0, ρ, ρ̄ (1/2 < β < 1), and N(x) = Ax + O(x^σ) for every σ > β.
- **CON-0032.** tested_supported; verifier sound_and_useful. Define "RH for ζ_P" as ψ_P = x + O(x^{1/2+ε}).
  - **T1** (Observatory-proposed; non-constructive case split given BDR Thm 1.3). For every β > 2/5, the implication "N_P(x) = ax + O(x^{β+ε}) ⇒ RH for ζ_P" is false unconditionally.
  - **T2** (to verify line by line). For Θ ∈ [1/2, 2/3) and β > 2Θ/(Θ+2), "Beurling + N_P regularity β ⇒ QRH(Θ)" is false.
  - **T3** (constructive, BDR 1.1). For β ≥ 1/2 and any Θ < 1, the QRH(Θ) implication is false.
  - **T4** (frontier). For β < 1/2 and Θ ≥ 2/3, which covers the claimed 7/8 and 11/12, no countermodel is known.

**Eliminates.** No argument using only the following can prove RH (CON-0032 T1), nor any QRH(Θ) with Θ < 1 (T3), nor any zero-free region beyond the de la Vallée Poussin shape (Broucke):
- an Euler product over generalized primes;
- nonnegative prime and integer measures;
- an explicit formula;
- N(x) = Ax + O(x^θ) with θ ≥ 1/2 (for RH: θ > 2/5).

The zero-excluding step of any proof must use a functional equation, the integrality of primes and integers (N(x) = ⌊x⌋ forces ζ_P = ζ), or another input that Beurling systems lack. The C2 skeptic notes that "must use" is a protocol heuristic, not a theorem.

**Does not eliminate.** Integer regularity with β < 2/5 (for RH), or with β < 1/2 and Θ ≥ 2/3 (for QRH). Both are open.

---

## Part III. Positivity conditions that are false

### OB-8. Conrey–Li, with the FND-0013 frequency data

**Statement.**
- **Conrey–Li 2000 (PAPER-0779), THEOREM (refereed).** de Branges' conditions are false:
  - (3.1): −Re{ξ′(ρ₃₄)ξ(1+ρ₃₄)} = −5.3891005071829451814…·10⁻⁶⁹;
  - (3.3): Re{ξ(1+282i)/ξ(2+282i)} = −0.000131957293372083…;
  - (3.7) and (3.8) for χ₄: −2.3103490049934834562·10⁻⁴⁵ and −0.00042234060658023277.
  - Sarnak gave a computation-free proof for the F(W) conditions, for all Dirichlet characters.
- **FND-0013** (valid_with_stronger_consequences; NUM-RIG by three independent Arb implementations, 0 undetermined). The zero condition fails at 195 of the first 2000 zeros, 2724 of 20000 and 15567 of 100000.
- **Failures per 1000-zero block** (C3 §3.3):

  | n₀ | 1 | 10⁴ | 9.9·10⁴ | 10⁶ | 10⁷ | 10⁸ | 10⁹ | 10¹⁰ |
  |---|---|---|---|---|---|---|---|---|
  | failures per 1000 | 80 | 131 | 167 | 193 | 194 | 209 | 227 | 224 |

- **C3-ADJ-S** (THEOREM, adjudicated). Assume the zeros up to γ_n are simple, on the line and correctly indexed. Then P_n < 0 ⇔ S(γ_n) − δ(γ_n) ∈ (3/4, 7/4) mod 2, with |δ(γ_n)| < 0.319 for 10 ≤ n ≤ 10⁵. The condition is a Gram-type condition on S(t).
- **C3-ADJ-RATE** (CONJECTURE). The failure rate tends to 1/2. Heuristic extrapolation: 25% near T ≈ 10¹⁴.
- **Not proved.** Even infinitely many failures.

**Eliminates.** No argument can prove RH through de Branges' positivity Re⟨F(z), F(z+i)⟩_{H(E)} ≥ 0 for E(z) = ξ(1−iz), or through (3.3) on F(1/ξ(1−iz)). Their hypotheses are unconditionally false.

More generally, consider any sufficient condition that reduces, as here, to a sign condition on S(γ_n) at every zero. Since S(t) is unbounded (Selberg), the statement that such conditions must fail is HEURISTIC; it is proved only for this one.

**Does not eliminate.** The de Branges-space framework itself (LED-OPS-14) and canonical systems (LED-OPS-15).

### OB-9. Partial sums: Turán's hypothesis and Montgomery 1983

**Statement.**
- **Montgomery 1983 (PAPER-0660), THEOREM.** For every large N, ζ_N(s) = Σ_{n≤N} n^{−s} has zeros in σ > 1. The location constant, σ ≈ 1 + (4/π − 1 − ε)log log N/log N, is recalled, not verified (BRG-CAUSAL_EULER-O7 correction).
- **Spira 1968.** N = 19, 22–27, 29–50.
- **Platt–Trudgian 2016.** ζ_N is zero-free in σ > 1 iff N ≤ 18 or N ∈ {20, 21, 28} (C3-D5).
- **Certified witness.** ζ₁₉ has a zero with Re ∈ [1.0010955115364747871…, 1.0010955115364777936…] near Im 600884.2034277757 (C2-22, NUM-RIG). A skeptic screen to t ≤ 2·10⁶ found no other zero with Re > 1.

**Eliminates (SP-7).** No argument of the form "ζ_N is zero-free in σ > 1 for all large N, then pass to the limit" can work. No argument can transfer zero-freeness from additive Dirichlet-polynomial truncations.

Multiplicative truncations behave differently (finite Euler products are zero-free in Re s > 0). For them the obstruction is instead zero counting: no uniform approximation is possible on regions meeting the critical line (BRG-CAUSAL_EULER-O4).

### OB-10. Sign and size conjectures at the √x scale: Ingham 1942

**Statement.**
- **Ingham 1942 (PAPER-0071), THEOREM.** Any one of M(x) < Kx^{1/2}, M(x) > −Kx^{1/2}, L(x) < Kx^{1/2} or L(x) > −Kx^{1/2} for all large x implies RH, simple zeros, and infinitely many ℤ-linear relations among the ordinates. Without such relations, limsup x^{−1/2}M = +∞ and liminf = −∞.
- **Mertens is false.** Odlyzko–te Riele (PAPER-0199).
  - limsup > 1.826054 and liminf < −1.837625 (Hurst, PAPER-0585; LED-ARITH-8: nonrigorous computation).
  - The first counterexample is below exp(1.96·10¹⁹) (Kim–Nguyen, PAPER-0786; LED-ARITH-9).
- **Pólya and Turán are false.** Pólya: Haselgrove (PAPER-0489), first failure at 906150257. Turán's T(x): first failure at 72,185,376,951,205 (PAPER-0616).
- **Stieltjes' M(x) = O(√x) is OPEN** and believed false (C3-D6).

**Eliminates.**
- Sign or size conjectures at the √x scale cannot serve as routes to RH: they are stronger than RH and expected to fail.
- No argument can use finite positivity up to X as evidence for the eventual sign of a Pólya-class detector, i.e. one with a constant main term and non-absolutely-summable zero coefficients (BRG-MELLIN_WAVELET-O1, O2; BRG-SHARP_NATIVE-O1, O2).
- Precedents of finite-to-infinite failure (C3 checklist item 13):

  | Statement | True up to | Fate |
  |---|---|---|
  | Mertens | 10¹⁶ (q ≤ 0.5706 away from small x; extreme M(7766842813) = 50286, C3-ADJ-M) | limsup > 1.826 |
  | Pólya | 906150256 | false |
  | Turán's T(x) | 7.2·10¹³ | false |
  | Oliva's step (3) | all primes p ≤ 1.39·10¹⁷ | fails below e^{727.951332668}, and infinitely often (C3-ADJ-O2, THEOREM modulo IMPORTED Platt–Trudgian and Littlewood) |
  | π(x) < li(x) | 10¹⁹ (LED-ARITH-13) | x_s < exp(727.951336108) (LED-ARITH-12) |

---

## Part IV. Heat flow

### OB-11. Rodgers–Tao Λ ≥ 0 and Dobner

**Statement.**
- Λ ≥ 0. THEOREM (refereed; Rodgers–Tao, PAPER-0036; LED-DBN-6).
- Λ_F ≥ 0 for every F in the extended Selberg class S♯, and for each t < 0, ξ_t^F has infinitely many off-line zeros. THEOREM (refereed; Dobner, PAPER-0333; LED-DBN-7).
- Over function fields, an individual Λ_D can be negative or −∞ (LED-DBN-18); Newman-type statements hold only as family suprema.

**Eliminates.**
- (a) No argument can prove RH by establishing real zeros of H_t at some negative time. There is no slack.
- (b) C2-29, THEOREM given Rodgers–Tao. Take a class of kernels that contains Φ and is closed under K ↦ e^{−εu²}K for some ε > 0. The assertion that every member has a real-rooted cosine transform is false.
  - So no argument using only properties of Φ that survive multiplication by e^{−εu²} can prove RH. Such properties include positivity, evenness, super-exponential decay, and strict log-concavity of Φ(√v) (THEOREM, Csordas–Varga 1988, per C2 skeptic F5).
  - They also include the moment Turán inequalities b_m² ≥ ((2m−1)/(2m+1))b_{m−1}b_{m+1}, which hold for every H_t (C2-14; THEOREM given Csordas–Varga and the moment lemma; the range p ∈ (−1, ∞) of the moment lemma is still to be confirmed).
  - A Fourier-side proof must use a property of Φ that fails for e^{−εu²}Φ for every ε > 0, e.g. exact theta modularity.
- (c) For host heat positivity (First-Hermite): the proof must use an input that arbitrarily small backward deformation destroys, such as the exact Euler product or Λ(n). This assumes a horizontal-strip bound and subquadratic counting for H_t, t < 0, which have not been checked from a source (BRG-OPERATORS_HEAT-O4 corrected).
- (d) CONJECTURE (CON-0033 corrected; restricted to infinite log-concavity of λ_n and its truncations). If (λ_n(t)) is strictly infinitely log-concave for all t ∈ (−t₀, 0], then infinite log-concavity cannot imply RH. Turán, higher Turán and all-degree Jensen are removed from this claim; all-degree Jensen hyperbolicity is equivalent to RH.

**Does not eliminate.** Arguments using exact modularity or arithmetic of Φ, and quantitative converse statements such as the CON-0008 persistence lemma.

---

## Part V. Parity and pretentiousness

### OB-12. Selberg's parity barrier

**Statement.** Sieve axioms based on level of distribution (Type I information, axiom R) cannot determine signed Möbius or prime sums, even at level x^{1−ε}. Classical (Selberg, PAPER-0897; Friedlander–Iwaniec; Bombieri's asymptotic sieve); BRG-SHARP_NATIVE-O3 and BRG-MELLIN_WAVELET-O8. As applied to host objects the BRG items are labelled HEURISTIC.

**Eliminates.** No argument using only sieve weights, positive kernels or Type I level-of-distribution information can prove Σ_{n≤x} μ(n) = o(x), let alone M(x) ≪ x^{1/2+ε} or any QRH(θ) with θ < 1. Genuine Type II (bilinear, sign-sensitive) input is necessary. Even with it, BRG-SHARP_NATIVE-O3 corrected records only sub-power (VK-type) savings, never x^{−1/2+ε}.

**What escapes parity (for comparison).**
- Quasi-RH. The parity information enters through the algebraic identity μ = ᾱγ₂³ (up to phases) and the automorphy of Patterson's cubic theta. The only analytic inequality is the GL quadratic large sieve (QRH dossier §2.2 [O]).
- Siegel exclusion. Integrality via the polynomial method (SIEGEL §7.4).

### OB-13. The pretentious (Halász) ceiling

**Statement (THEOREM; Granville–Soundararajan, arXiv:math/0508361, Thms 1–2; BRG-SHARP_NATIVE-O5).** For multiplicative f with |f| ≤ 1, one-sided bounds on Σ f(n)/n are only of size (log log x)^{−3/5} to 1/log x, and some f attain −c/log x.

**Eliminates.** No argument using only multiplicativity, |f| ≤ 1 and prime-sum data can reach the power savings that the host H1 premise or any RH-scale estimate requires.

---

## Part VI. Mollifier ceilings and density currency

### OB-14. Mollifier ceilings

**Statement.**
- **(a) Length.** The twisted second moment is known for θ < 4/7 with Conrey-type coefficients (PAPER-0191) and θ < 17/33 for arbitrary coefficients (PAPER-0244). The general formula fails for θ > 1, and the θ = 1 conjecture for arbitrary coefficients implies Lindelöf (BCR; MOM frontier §5(1)).
- **(b) Output at θ = 1.** κ ≥ 0.6107. CONDITIONAL (Feng, PAPER-0046). This is below 2/3.
- **(c) Perfect mollification is impossible.** THEOREM (unrefereed; Radziwiłł, arXiv:1207.6583): I(M_θ) = (1/T)∫|1 − ζM_θ|² ≥ c/θ, and ≥ 1/(0.5 + θ) under RH + PCC. LED-CRIT-9 corrected: this limits Selberg-type mollification, not directly the Levinson proportion.
- **(d) Bettin–Gonek.** THEOREM (refereed; PAPER-0064): a mollified mean square ≪ T^{1+ε} for N ≤ T^θ gives ζ ≠ 0 on Re s > 1/2 + 1/(2θ). It has content only for θ > 1, and 7/8 would need θ = 4/3. CON-0031 corrected: this is a known corollary of Bettin–Gonek plus the lengths 4/7 and 17/33, and the verifier asks that its "exponent law" be called heuristic bookkeeping.
- **(e) Twisted fourth moment.** ϑ < 1/4 is optimal even assuming Selberg's eigenvalue conjecture (BBLR; MOM frontier §5(2)).

**Eliminates.**
- No argument using only proven mollified second moments (θ < 4/7 structured, < 17/33 generic), fed through Bettin–Gonek or DWZ extraction, can give any QRH(Θ) with Θ < 1.
- No Levinson–Conrey argument with θ ≤ 1 can exceed 0.6107, conditionally.
- No Selberg-type mollifier of finite length can be perfect.

### OB-15. Density currency: proportions are blind to o(T) off-line zeros

**Statement (CON-0030, corrected; a formalisation of folklore, not a new obstruction).** Let Z and Z′ be multisets symmetric under ρ ↦ 1 − ρ̄, with local counts N(t+h) − N(t) ≤ hL + C log T. Let Z′ arise from Z by moving E(T) separated zeros of height ≤ T to ordinates where the window count is O(λ + 1). Then every n-level correlation sum with a Schwartz-decaying test function changes by O(E(T)(λ + C log T)^{n−1}). Under the verifier's condition E(T) = o(T/(log T)^{n−2}), or the stated placement, this holds for any o(T).

The following never exclude an individual off-line zero (C3-D9; abandoned §14):
- the Littlewood + Jensen output inequality used by Levinson–Conrey;
- sign-change methods (Hardy–Littlewood, Selberg).

**Eliminates.** No argument whose only zero inputs are some of the following can exclude a single off-line quadruple, any set of o(T) off-line zeros, or prove RH:
- (i) Riemann–von Mangoldt with S(t) = O(log T);
- (ii) pair or n-level correlation with o(TL) error, at any support;
- (iii) moments of Δ_U S with o(T) error;
- (iv) Levinson–Conrey mean values through Littlewood's lemma;
- (v) bandwidth-limited trace moments.

The strongest possible conclusion of such an argument is "100% critical and simple". Under the pair correlation conjecture without RH this is attained (Goldston–Lee–Schettler–Suriajaya, PAPER-0537; LED-CRIT-13). Witnesses: Davenport–Heilbronn has a positive proportion of zeros on the line; Bombieri–Hejhal give 100% for linear combinations under hypotheses (BRG-FAMILIES-O2).

### OB-16. The bandwidth-one ceiling of the 2026 critical-line method (CRIT23 §7)

**Statement.**
- **(a) Sharpness for its information** (CRIT23 check (C); NUM; author-confirmed AF §7.2(a)–(b)). The three inputs are:
  - tr A = N;
  - tr A² = (C(f) + o(1))N for one window with f∗f supported in [−1, 1];
  - the inertia structure.

  They are consistent with a configuration in which one third of the zeros are off the line (blocks of six sites: four simple on-line points, one off-line pair n ± iε, one empty site), giving ΣK²/N = 1.333625 at ε = 0.01. The same configuration is excluded by the Montgomery–Taylor window, which is exactly why that window gives more than 2/3.
- **(b) Ceilings.** Author-stated, **not audited**: every bandwidth-one certificate is ≤ 0.6818287 (AF §7.2; interval enclosures EnclOK not kernel-checked; LED-CRIT-10). Knausgård: windows with V(f) ≤ 10B(f) ≤ 0.68185 (κ*) and 0.84093 (N_d); any frame 0.67383 and 0.83998; eight- and seven-point frames 0.67357 and 0.83916. The Montgomery–Taylor window is optimal among windows of the form 2 − R(ψ) (CCLM 2017, as cited by AF).
- **(c) Support barrier.** Under a hypothetical form factor min(|α|, 1) on [−Δ, Δ], the certificate is 2 − C(Δ), with C(Δ) = 1/Δ + Δ/3 for Δ ≤ 1 and 1 + 1/(3Δ²) for Δ ≥ 1. Only Δ = 1 is unconditional (BGSTB24, PAPER-0053; AF §5).
- **(d) Positivity barrier.** BGSTB24 Thm 1 gives F(α) ≥ 0 for all α, but that sign bounds ΣK² from below, which is the wrong direction for these certificates (CRIT23 §7.3, the auditor's reading).
- **(e) Higher moments.** These are unconditional only in the Rudnick–Sarnak range X^k ≤ T^{2−ε} (AF §7.2(e), informal). Under HL*(4) the Chebyshev–Markov–Stieltjes bound gives 13/18.
- **(f) GL(d).** CON-0011 and CON-0035 corrected (Observatory computation). For an individual degree-d L-function at bandwidth 1/d:
  - the window simple-on-line certificate 2 − R*_{1/d} is negative for every d ≥ 2;
  - the distinct-zero bound 1/R*_{1/d} is positive for every d (d = 2: 0.4617, conditional on the GL(2) pair-sum asymptotic; d = 3: 0.3214).
  - The simple+critical threshold is λ* = 0.5501939647, for this window class only.
- **(g) Even 100% would not be RH** (AF §7.2(f)).

**Eliminates.**
- No argument using only the first two trace moments of the compressed Weil form with Fourier support [−1, 1], plus the on-line/off-line partition, can certify liminf N0^s/N > 0.6818287. This is author-stated; the Observatory has proved only the 2/3 sharpness in (a).
- No argument in this class can exclude o(N) off-line zeros.
- No window certificate of this shape gives simple critical zeros for an individual L-function of degree ≥ 2.

---

## Part VII. Finite-detection horizons

### OB-17. Campaign C1: Theorem L1 and the T0 table

**Statement.**
- **Theorem L1.** THEOREM: Oesterlé 2000 (unpublished, via Voros), with an independent explicit proof in C1-L2 (skeptic: prior art found, mathematically upheld). If T ≥ 100 and every zero with 0 < γ ≤ T is on the line, then λ_n > 0 for all 1 ≤ n ≤ T². At T0 this covers n ≤ 9.0011·10²⁴.
- **The table at T0**, with the skeptic's corrections. δ_max(T0) = 1/2 − 1/(5.558691 log T0) = 0.49374, using the Mossinghoff–Trudgian–Yang constant (attribution corrected).

| Criterion | Implication horizon of RH(T0) | Status | Single-defect minimal index (model) | Status |
|---|---|---|---|---|
| Li λ_n | n ≤ 9.0·10²⁴ | THEOREM (Oesterlé; C1-L2) | n* ≈ 1.19·10²⁷ | HEURISTIC; the leading formula is 11–12% low at T0 |
| Jensen J^{d,n} | d ≤ 9.0·10²⁴ | THEOREM (GORTTW, PAPER-0087) | d* ≈ 4.4·10²⁵ | HEURISTIC (C1-J2 bridge) |
| ψ, θ, π (Schoenfeld) | x ≤ 1.101·10²⁶ | THEOREM (Johnston, PAPER-0917; corrected from Büthe's 2.17·10²⁵) | x* ≈ 1.7·10²⁹ | HEURISTIC |
| Nicolas / Robin | x (= log n for Robin) ≲ 4.4·10²³ | PROPOSITION-PROOF-SKETCH (C1-D3) | x* = 10^{50.5} | HEURISTIC |
| Nyman–Beurling d_N | none | — | log N* ≈ 2.1·10²³ (two-zero floor) | HEURISTIC; rests on the conjectured BDBLS asymptotic |
| Mertens | none (|M| ≤ m√x is not known to follow from RH, and is false under RH + LI) | corrected (C1-D4) | x* ≈ 10²⁰–10²⁸ depending on |ζ′(ρ₀)| | HEURISTIC; the visibility threshold is arbitrary |
| de Bruijn–Newman | RH(H ≥ 2.51·10¹²) ⇒ Λ ≤ 0.2 | THEOREM (Platt–Trudgian Cor. 2; corrected) | needs Λ-bound below 0.101 (t_c = 0.10130) | model |
| Riesz / Báez-Duarte c_k | none | — | log k* ≈ 9.5·10¹² | HEURISTIC |

- **C1-L4** (PROPOSITION-PROOF-SKETCH; skeptic stress test 4.7–5.2·T² log T). No argument using only RH(T) plus zero counting can certify λ_n ≥ 0 beyond n of order T² log T.

**Eliminates.** These computations carry no information about zeros above T0 (implication column; THEOREM except the Robin row, which is a sketch):
- λ_n for n ≤ 9·10²⁴;
- Jensen hyperbolicity for d ≤ 9·10²⁴;
- ψ/π tables or bounds for x ≤ 1.1·10²⁶;
- Robin checks for log n ≲ 4.4·10²³ (so the verified range 10^(10^13.11), log n ≈ 3·10¹³, is uninformative);
- de Bruijn–Newman bounds Λ ≤ 0.2.

The single-defect column is model-world only.

**Related locality barrier.** Johnston–Trudgian (arXiv:2511.09978): arithmetic verification up to Y yields zero information only for |γ| ≲ Y^{1/5}. The Landau–Pintz arithmetic-to-zero-free route is "doomed to fail" for ζ (BRG-MELLIN_WAVELET-O6; ARITH frontier §5(3)). So no finite negative-mass or Mertens computation, converted by a Landau–Pintz theorem, improves current zero knowledge.

### OB-18. Weil-window detection and certificate cost (C4; Zhu; Connes–Kastoris)

**Statement.**
- **(a) Pointwise-envelope barrier** (unrefereed; Zhu Thm 1.4 and Lemma 3.2; BRG-OPERATORS_HEAT-O1 corrected). Every certificate built on the pointwise prime-comb envelope needs frequency resolution T₁ = 2πe^{A_L} with A_L ~ 4e^L. The barrier is proved only for pointwise-envelope certificates; non-envelope routes such as prolate conditioning are not covered.
- **(b) Margin collapse.**
  - ε_λ ≤ Cδ₄(λ)(log λ)³ with δ₄ ~ c₄λ⁹e^{−4πλ²}, i.e. exp(−c·e^{2L}) with L = log λ (unrefereed Connes–Kastoris theorem as stated in PAPER-0544; LED-OPS-9).
  - Zhu's exp(−L e^L) is an RH-conditional *upper* bound, not a decay law (C5-OB9 corrected).
  - Certified variational upper bounds reach 3.2·10⁻²⁸³ at L = 2.
- **(c) Galerkin truncations give upper sections only.** A finite-basis positive matrix certifies nothing about the continuum (Groskin Cor. 3.3; BRG-OPERATORS_HEAT-O3). Rayleigh–Ritz can only bound detection thresholds from above, never prove non-detection (C4 skeptic, general issue 2). The C4-P profile values are 0.3–6% above the infimum (skeptic).
- **(d) Detection is not height-local for large δ.** C4-B: THEOREM conditional on H1. C4-LAT: THEOREM in the lattice model; the crossover κ_c = 2.1773190 is the root of sinh k = 2k.
  - A window L detects defects with δ log(T/2π) > κ_c up to doubly exponential heights.
  - The brief's heuristic "blind for T ≫ 2πe^{2L}" is REFUTED (C4-R; the skeptic upheld the refutation).
  - The "Nyquist locality for near-line defects" replacement is **not established**: the collision model contradicts it, with detection up to 0.85 below L_N (C4 skeptic).
  - C4-H and C4-REL are **downgraded**.

**Eliminates.**
- No pointwise-envelope certificate can cover windows L ≳ 2 at feasible cost.
- No Galerkin or Rayleigh–Ritz computation can certify Weil positivity or window blindness.
- No argument can assume that a window L sees only heights T ≲ 2πe^{2L}.

---

## Part VIII. The quasi-RH method floor

### OB-19. Limits of the 2026 large-sieve architecture (QRH dossier §4; CON-0038; CON-0009; CON-0031)

**Statement.**
- **(a) Extraction lemma** (paper2 l.694–724; [P]; algebra checked in audit_S3 C4 and in the dossier script). A full-row mean square Σ_{0<N(u)≤H} |A_u(D)|² ≪ D^{1+ε}H with H = D^h, for an order-n residue family, gives β ≤ β(n, h) = 1/2 + h(n−1)/(2n). Hence β(6,1) = 11/12, β(4,1) = 7/8, β(3,1) = 5/6, β(2,1) = 3/4.
- **(b) h ≥ 1 is forced in paper2** [O]. Every step except the GL large sieve is an identity, a positivity enlargement or Cauchy–Schwarz. For H < D the duality sends the rows to H_dual ≍ D²/H, and the dual diagonal returns Σ|A_u|² ≍ DH + D² > DH (the large-sieve barrier). So 11/12 is the floor of this architecture with sextic rows (stated in the paper; confirmed by audit_S3). The extraction is also tight on the signal side.
- **(c) Why order 6** [O]. Only for n = 6 does Gauss–Jacobi eliminate μ, leaving cubic Gauss sums, which are Patterson theta coefficients known with no coprimality condition.
  - For n = 2 the duality is self-dual.
  - For n = 3, μ survives, and Patterson-type biases (Dunn–Radziwiłł, PAPER-0960) block cancellation without the angle twist.
  - Explicit n-fold metaplectic theta coefficients are known only for n = 2, 3 (standard; not re-verified).
- **(d) The 7/8 comparison system** [O]. B(ℓ) = 11/12 − ℓ/4 with ℓ < 1 − |b| gives B > 2/3 however good the nonprincipal estimates are. 3/4 needs ℓ = 2/3, and 1/2 would need ℓ = 5/3, which is impossible.
- **(e) Liu's optimality theorems.** Unrefereed and conditional on the 7/8 inputs:
  - PAPER-0156 Thm 34.4: B_new = 0.874957019…;
  - PAPER-0157 Thm 14.13: B♭ = 0.874886647039964…, unattained.

  These are optima of fixed semi-algebraic inequality systems (Liu's own caveat). They have been bypassed several times (ZFR frontier critique: Liu B_tw = 0.8740585038; Chang–Wang 0.87446…). **Not a barrier.**
- **(f) Generic sieves cannot substitute for the special coefficients** (QRH dossier §2.3 and C4). With de Faveri's conjecturally sharp bound Θ₆(A, B) ≍ A + B + A^{5/6}B^{1/3} + A^{1/3}B^{5/6} in place of the special-coefficient bound, the paper2 extraction gives only the trivial bound. Lower bounds exist for n = 3, 4 (DR Thm 1.4 under GRH; de Faveri–Dunn–Hoffstein unconditionally). Xu's claimed sextic lower bound A^{5/6}B^{1/3} is a secondary source. Liu (PAPER-0157, Remark 10.9) gives the same diagnosis independently.
- **(g) Ji's independent route has a floor above 11/12** (CON-0038, tested_supported, sound_and_useful; within the verifier's transcription of Ji, PAPER-0155):
  - inf Θ = 0.998327 with de Faveri's exponent;
  - with Ji's contour constraint a ≥ 1/2, inf Θ ≥ 0.996732 for **every** density input, DH and GRH for the quartic family included;
  - without that constraint, ≥ 0.9898 unconditionally and ≥ 25/26 under GRH;
  - even deleting the local-factor loss leaves 23/24 > 11/12.
- **(h) Trivialising-row extractions** (CON-0009; sound_but_known; downgraded to "within uniform-trivialising-row mean-square extractions"). β(θ, ν) = 1/2 + (1+θ)(1−ν)/2, so the critical line needs ν → 1. The route-closing pointwise lemma is GRH for the family member.
- **(i) CON-0031 corrected.** The paper2 extraction, used with only trivial rows at h ≥ 1, cannot do better than 1 − 1/(2n) ≥ 3/4. This is architecture-specific. It becomes an obstruction only with a countermodel family, or a proof that the trivial-row density r ≤ 1/n is forced.
- **(j) Consistency** [O; QRH dossier §2]. No tension with Davenport–Heilbronn (multiplicativity is used at four load-bearing points), parity (OB-12), large-sieve lower bounds, Ω-results or numerics. The proof gives no explicit zero-free region beyond the half-plane and covers finite-order characters only.
- **(k) Toward 1/2.** Every input known to reach 1/2 is of GRH strength for a family (QRH dossier §4.3 (C5)).

**Eliminates.** The class of each is named; (b)–(d) rest on [O] sketches.
- No argument using only full-row Möbius mean squares over trivialising rows u = p^n at h ≥ 1, plus extraction, gives a half-plane left of Re s = 1 − 1/(2n) (≥ 3/4).
- No argument using only generic large-sieve coefficients, without the angular theta structure, yields any QRH through the paper2 extraction.
- No zero-density input fed into Ji's quartic architecture reaches 11/12.
- No 7/8-type comparison system whose direct estimate has the shape |J_η(Z)| ≪ Z^{l_x/2 + b/12 + ε} can go below 2/3.

### OB-20. Limits of the Siegel-exclusion method (SIEGEL §7)

**Statement** (auditor's computations; the sources' constants are unrefereed):
- Every proof establishes S₋(X) ≤ κ log X + e log q + O(1), where S₋ is the inert-prime mass. The prime ideal theorem forces κ ≥ 1/2. Achieved values: OAI and Banks 13/16 → 3/4; Kerr 39/40; Guo 11/20 → 1/2.
- The zero enters only through split-prime mass ≤ bδA² log q, which yields the generic ceiling δ* = (1 − κ)²/(4bK).
- Recomputed asymptotic ceilings on c: Banks' chain 3.244·10⁻³; Kimura's 1.0196·10⁻²; Guo's comparison as stated 0.06095. With ideal arithmetic and a hypothetical y → q it is 3 − 2√2 = 0.171573 < 1/5, LZZ's computed value (PAPER-0855).
- The method has no small-prime strength. It concerns only real zeros, quadratic characters and inert primes.

**Eliminates.** No argument of the inert-prime-dominance / Frobenius-conjugation type, with κ ≥ 1/2 and a δ(log X)² analytic coupling, can prove any of: a zero-free interval [1 − η, 1); Chowla positivity on (1/2, 1); (1 − β) log q → ∞; c ≥ 1/5; anything about complex zeros. These ceilings bound chains, not zeros.

---

## Part IX. Zero density, zero-free regions, correlations

### OB-21. Barriers in the large-values route to zero density (ZDE frontier §5; LED-ZDE-18 corrected)

**Statement.**
- A(1/2) = 2, so DH is the best uniform target.
- LV(σ, τ) ≥ min(2 − 2σ, τ) (TTY Lemma 29, PAPER-0466). Montgomery's large-values conjecture therefore yields DH and nothing stronger without ζ-specific input.
- Bourgain's counterexample to the ℓ²-normalised Montgomery conjecture means Guth–Maynard need ℓ^∞ coefficients.
- Montgomery's ℓ^q conjecture ⇒ Bourgain–Kakeya ⇒ Kakeya in every dimension. This is a barrier only for proving DH via the full Conj. 3.4; DH itself is not known to imply Kakeya.
- Zero density ⇒ ζ-large values (Matomäki–Teräväinen).
- Vertical arithmetic progressions of zeros are not excluded; the DH result of Maynard–Pratt (PAPER-0096) needs Hypothesis F.
- **The 7/10 pivot** (CON-0028, sound_but_known: an immediate corollary of Gafni–Tao Thm 1.1 and the Guth–Maynard extremal point). Adding N(σ, T) = 0 for σ > θ₀ with θ₀ ≥ 7/10 leaves the short-interval thresholds 17/30 (all intervals) and 2/15 (almost all) unchanged. CON-0019 finds that the 7/8 half-plane improves the Gafni–Tao exponent μ(θ) only for 0.2445 < θ < 5/12, by at most about 0.0109.

**Eliminates.**
- No argument using only mean-value and large-values estimates valid for arbitrary ℓ²-normalised coefficients can beat the current large-value bounds.
- No proof of DH can go through the full ℓ^q large-values conjecture without settling Kakeya.
- No zero-free half-plane with θ₀ ≥ 7/10, used alone, improves the short-interval PNT exponents; this covers all the claimed 2026 half-planes.

### OB-22. Barriers for classical zero-free regions (ZFR frontier §5)

**Statement.**
- **Landau's extremal constant.** 34.468305 < V < 34.4889920009 (Mossinghoff–Trudgian, PAPER-0038; Arestov–Kondrat'ev; LED-ZFR-17). It caps the Landau/Stechkin trigonometric-polynomial method at R₀ ≈ 9.5.
- **Smoothing efficiency.** BTY smoothing (PAPER-0159) reaches efficiency 1.98 against a hypothetical maximum of 2.
- **Beurling optimality** of the classical region (OB-7; LED-ZFR-16).
- **Ford's midline method** cannot improve Stechkin's region for all |t| ≥ 3 at T₀ = 5.45·10⁸.

**Eliminates.**
- No Landau/Stechkin polynomial argument gives R₀ below ≈ 9.5.
- No argument from an Euler product plus N(x) = Ax + O(x^{1/2+ε}) improves the de la Vallée Poussin shape. The Vinogradov–Korobov shape needs the additive structure of n^{it}, and any QRH proof needs more again.

### OB-23. Correlation barriers for small gaps (SPACING frontier §5)

**Statement.**
- **AH compatibility.** THEOREM (refereed; Lagarias–Rodgers, PAPER-0103; LED-SPACING-6): an explicit sequence with all gaps half-integers reproduces every averaged band-limited GUE n-level correlation (Σ|ξ_i| < 2).
- **Montgomery–Odlyzko criterion limits** (LED-SPACING-10):
  - Conrey–Ghosh–Gonek: it cannot give μ < 1/2;
  - Goldston–Trudgian–Turnage-Butterbaugh (PAPER-0330): not μ < 0.5042, and not λ ≥ 3.6747;
  - Inoue–Kobayashi–Toma: limited to μ ≥ 0.508 and λ ≤ 3.022 for L ≤ T.
- **Conrey–Iwaniec** (PAPER-0573): a Siegel zero forces few gaps < 1/2 − ε. CON-0034 (sound_but_known): if the 2026 Siegel exclusion holds, theorems on the exceptional branch become vacuous, not false.

**Eliminates.**
- No argument using only averaged band-limited n-level correlations can prove μ < 1/2. The SPACING critique notes that resonance-weighted statistics are not covered, and Bondarenko–Heap cross 1/2 under RH plus Siegel zeros.
- No Montgomery–Odlyzko argument can give μ < 0.508 with L ≤ T.

---

## Part X. Function-field transfer barriers (C5 OB1–OB9, as corrected by the skeptic)

### OB-24. Why Weil's and Deligne's proofs do not transfer

**Statement.**
- **OB1. No Frobenius and no nontrivial self-product.** Spec ℤ ×_{Spec ℤ} Spec ℤ = Spec ℤ. Under total commutativity the arithmetic surface collapses to the diagonal (Haran Rem. 4.12). The arithmetic-site correspondences compose with a defect: Ψ(λ)∘Ψ(λ′) = Id_ε∘Ψ(λλ′) (PAPER-0086 Thm 7.7). IMPORTED.
- **OB2. Infinite genus.** Weil's 2×2 inequality needs finite defect def(Δ) = 2g. Only smeared divisors D(f) have finite defect, and for them the inequality is Cauchy–Schwarz for the Weil form, which is RH itself. THEOREM (part (a)); labelling Σ 1/|ρ| as the defect analogue is HEURISTIC. Part (c), "over ℚ no finite window suffices", is **not a theorem** (skeptic §3.3).
- **OB3. The archimedean place.** Γ_R must come from geometry; archimedean-only positivity is known only for supports in (1/2, 2).
- **OB4. Deninger 2022, Thm 2.13.** No real-coefficient Weil cohomology for arithmetic curves can realize ord_{s=1/2}L(V_π, s) functorially: a symplectic π with root number −1 would appear with odd multiplicity. Positivity must therefore be quaternionic.
- **OB6. The polynomial method over ℤ.** Gorshkov's barrier; bracket 0.4222286 ≤ t_ℤ([0,1]) ≤ 0.4226847, above 1/e. Corrected: this rules out only fixed weights; sequences of weights w_n with B(w_n) → 1 remain open (Pritsker).
- **OB7. No family through Spec ℤ.** Deligne's Rankin-squaring positivity engine transfers to automorphic L-functions but yields Ramanujan (local purity), not RH (HEURISTIC; Langlands' remark verified).
- **OB9.** Finite Weil windows over ℚ have a near-radical whose margin decays like exp(−c·e^{2L}) (corrected).
- **C5-D1.** THEOREM, elementary. In number-field form the tensor-power trick is equivalent to RH: RH ⇔ there is C < ∞ with Re w ≤ k/2 + C for all w ∈ Z^{(k)} and all k.

**Eliminates.**
- No transfer of Weil's or Deligne's proof that uses only the zeta axioms (OB-6).
- No argument that applies Rankin-squaring positivity to Satake parameters yields RH rather than Ramanujan.
- No functorial H¹ with a real Hodge-* positivity can exist.
- A tensor-power argument over ℚ with loss independent of k is RH-strength.

---

## Part XI. Spectral realization without positivity

### OB-25. Realization is cheap; self-adjointness and positivity carry the content

**Statement.**
- **Unconditional realizations exist.**
  - Connes 1999 (PAPER-0026): critical zeros, on a Sobolev space, δ > 1.
  - Meyer 2005 (PAPER-0074): all zeros; it cannot be made unitary once off-line or multiple zeros exist (LED-OPS-3 corrected).
- **Bender–Brody–Müller** (PAPER-0502). The momentum operator with a Dirichlet condition has deficiency indices (1, 0), and ψ_z = −ζ(z, x+1) ∉ L² for Re z ≤ 3/2. Weights move the real-eigenvalue line (Bellissard, PAPER-0813; C3-D4).
- **Berry–Keating xp.** Purely continuous spectrum on L²(ℝ₊) (Endres–Steiner); only the smooth term N̄(E) is reproduced (LED-OPS-17).
- **Yakaboylu** (PAPER-0095). FND-0001 is a verified error: the weight defines an indefinite form (an explicit vector with ⟨U|U⟩ = −0.0231), and the boundary condition admits spurious solutions such as s = 1/2 + 3.70362i. The current version reduces to the tautology W > 0 ⇔ RH (LED-OPS-19).
- **Connes' global trace formula** ⇔ RH is proved only in positive characteristic (FND-0006).
- **Selberg zeta** (OB-5).

**Eliminates.** No argument can prove RH by exhibiting a spectral realization, formal eigen-equation or trace formula without proving self-adjointness, unitarity or positivity on a named Hilbert space that contains the eigenvectors. This is the C3 failure mode F7.

---

## Part XII. Host-programme obstructions (BRG; host OPEN_CUTS §1–§6)

These are the verified bridge obstructions. Each line gives the obstruction, its BRG verdict and what it eliminates.

| ID | Obstruction (exact) | Verdict | Eliminates |
|---|---|---|---|
| BRG-CAUSAL_EULER-O1 | For σ₀ ∈ (1/2, 1), convergence of the corrected product to a nonzero limit at one point of Re s = σ₀ ⇔ ζ ≠ 0 on Re s > σ₀ ⇔ ψ(x) = x + O(x^{σ₀}) (Akatsuka, PAPER-0227) | confirmed_with_correction (nonzero limit needed) | Any unconditional §6 contribution that does not prove a zero-free half-plane |
| BRG-CAUSAL_EULER-O2 | log G₁(s, x) = Ω±(x^{1/2−s} log log log x/log x) (Landau, Littlewood; Gorodetsky Cor. 2.10) | confirmed | Any discrepancy rate better than ≈X^{1/2−σ}, even under RH |
| BRG-CAUSAL_EULER-O4 | Finite Euler products are zero-free on Re s > 0 while D has poles at the zeros (Gonek, PAPER-0006) | confirmed | Uniform approximation on any region meeting the critical line |
| BRG-CAUSAL_EULER-O6 | Convergence on Re s = 1/2 ⇔ ψ(x) = x + o(√x log x), the deep RH (Conrad PAPER-0081; Akatsuka) | confirmed | Any line-1/2 extension below DRH strength |
| BRG-FAMILIES-O3 | Isolating the principal member by positivity costs the family size (heuristic, memory-based per correction) | confirmed_with_correction | Principal extraction from orthogonality-only family estimates |
| BRG-FAMILIES-O4 | Family nonvanishing is proved at 1/2 − ε; individualizing needs 1/2 + ε (Iwaniec–Sarnak, PAPER-0696) | confirmed | Expecting principal extraction away from the critical exponent |
| BRG-FAMILIES-O5 | 1-level density positivity needs GRH, or zeros that are real or on the line (ILS, PAPER-0019, Cor. 10.4) | confirmed | Assuming positivity of off-line contributions |
| BRG-FAMILIES-O6 | Deuring–Heilbronn propagation of a bad zero is repulsive | confirmed_with_correction | "One bad zero ⇒ family contradiction" via classical propagation |
| BRG-FAMILIES-O7 | Density theorems need essential orthogonality; families sharing ζ as a factor admit no such bound without RH-type input for ζ (Kowalski–Michel) | confirmed_with_correction | Contradicting a density theorem by propagating a ζ zero |
| BRG-FAMILIES-O8 | S₁ = {ζ, L(s+iθ, χ)}; S♯_d is empty for 0 < d < 1 and 1 < d < 2 (Kaczorowski–Perelli, PAPER-0192, PAPER-0670) | confirmed | Interpolating degree within Selberg-type axioms below 2 |
| BRG-MELLIN_WAVELET-O3 | The negative-mass premise is RH-equivalent for each checked detector; graded version ⇔ zero-free Re s > 1/2 + θ | confirmed_with_correction (only the checked detectors) | Any partial Y^θ result with θ < 1/2 weaker than QRH |
| BRG-MELLIN_WAVELET-O7 | Character- or moduli-averaged sign criteria hold unconditionally while the member is (G)RH-hard (Suzuki, PAPER-0430) | confirmed_with_correction | Supplying the fixed principal premise from family averages |
| BRG-ROBIN-O2 | Under RH the Robin margin on SA/CA numbers is ≈ (log n)^{−1/2}, oscillating through a zero sum (Ramanujan, PAPER-0079) | confirmed | Fixed-relative-margin envelopes closing the tail |
| BRG-ROBIN-O3 | Exact-prefix subtrees have unconditional margin factors < 1, non-uniform in the exponent cap A | relation_overstated; corrected statement used | Uniform-in-A tail lemmas weaker than RH |
| BRG-ROBIN-O4 | The t-free method fails at t = 21 with the Morrill–Platt inputs; Axler reached 21 only with better Mertens-product bounds | confirmed | Unbounded-exponent t-free arguments |
| BRG-SHARP_NATIVE-O4 | The smooth-number asymptotic near y = (log x)^{2+ε} is RH-equivalent (Hildebrand) | downgraded to a heuristic barrier | Bounded-envelope crossing of the (log X)² threshold, heuristically |
| BRG-SHARP_NATIVE-O6 | The subunit-mass contraction needs m > m* ≈ 1.80207; m = 1 is the divergent prime-harmonic series (analyst computation) | confirmed | Every Euler-cube or level-mass variant reaching m = 1 without cancellation input |
| BRG-SHARP_NATIVE-O7 | Unsmoothed Σ μ(n) and Σ μ(n)/n change sign infinitely often (Kaczorowski–Pintz) | confirmed | Sign targets without enough smoothing |
| BRG-XI_PICK-O1 | Matrix-monotone classes have strict gaps P_{n+1} ⊊ P_n (Hansen–Ji–Tomiyama), on intervals other than ℝ | confirmed_with_correction | Abstract order bootstrapping in the Loewner hierarchy |
| BRG-XI_PICK-O6 | Positive definite real Hankel matrices are exponentially ill-conditioned (Beckermann; Tyrtyshnikov) | confirmed | Additive perturbation with order-independent error at growing order |
| BRG-XI_PICK-O7 | PF_k plus N(Y) ≤ k + 1 implies RH through height Y (Sra Thm C.11); unconditional PF orders are capped by verified height | confirmed | Unconditional finite-order safe-axis theorems beyond verified height, if the hierarchy concentrates information |
| BRG-OPERATORS_HEAT-O9 | Continuity of the window ground-state energy is delicate; Bombieri's claim "calls for more careful analysis" (Suzuki) | confirmed | Importing continuity across window lengths without proof |

---

## Part XIII. Verified obstructions from the discovery register

| CON | Obstruction | Verdict (corrected form used) | Atlas entry |
|---|---|---|---|
| CON-0032 | The Beurling frontier for RH (β > 2/5) and QRH (β ≥ 1/2; T2 for Θ < 2/3); open region β < 1/2, Θ ≥ 2/3 | tested_supported / sound_and_useful | OB-7 |
| CON-0038 | Ji's ℚ(i) route cannot reach 11/12 from any density input | tested_supported / sound_and_useful | OB-19(g) |
| CON-0009 | Trivialising-row extractions cannot reach the line; the closing lemma is GRH for the member | sound_but_known (downgraded scope) | OB-19(h) |
| CON-0031 | Proven mollified moments give vacuous half-planes; paper2 extraction at h ≥ 1 gives no better than 3/4 | needs_correction → architecture-specific, known corollary | OB-14(d), OB-19(i) |
| CON-0030 | Density currency: blind to o(T) off-line zeros | needs_correction → formalisation of folklore | OB-15 |
| CON-0011 / CON-0035 | Window certificates give no simple critical zeros for individual degree ≥ 2 L-functions; distinct bound 1/R*_{1/d} > 0 | needs_correction (targets restated) | OB-16(f) |
| CON-0028 | No half-plane with θ₀ ≥ 7/10 improves 17/30 or 2/15 | sound_but_known | OB-21 |
| CON-0033 | Infinite log-concavity of λ_n is (conjecturally) heat-open, hence cannot imply RH | needs_correction → CONJECTURE, restricted scope | OB-11(d) |
| CON-0034 | If Siegel exclusion holds, exceptional-branch theorems are vacuous; no unconditional positive proportion of gaps below 1/2 exists | sound_but_known | OB-23 |
| CON-0004 | No argument through n/φ(n) alone beats exp((log x)^{(1+Θ)/2}) for counting non-Robin numbers | needs_correction (sketch) | ARITH context; unproved |
| CON-0022 | "Siegel excess" constraint on Siegel's R(s) | **vocabulary_only**: no constraint on R(s) follows without the open attribution lemma | Excluded; not an obstruction |

## How to use this atlas

Apply the C3 checklist (C3 FINAL §6; HEURISTIC). Each failure-mode tag F1–F15 maps to entries above:

| Tag | Meaning | Atlas entries |
|---|---|---|
| F1 | Countermodel test | OB-1 to OB-7 |
| F2 | Argument proves too much | OB-1, OB-3 |
| F3 | Circular positivity | OB-8 |
| F4 | False sufficient condition | OB-8, OB-9, OB-10 |
| F5 | Finite-to-infinite extrapolation | OB-10, OB-17 |
| F7 | Domain gap | OB-25 |
| F11 | Factorization-only | OB-3 |
| F13 | Density read as all | OB-15, OB-16 |

An argument that survives every applicable entry must name the step that uses a hypothesis all the relevant witnesses violate: the Selberg local condition, Λ_F ≥ 0, integrality, exact modularity, or the special theta coefficients.

