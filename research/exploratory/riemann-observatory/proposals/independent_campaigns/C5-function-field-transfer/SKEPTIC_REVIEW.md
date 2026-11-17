# C5-function-field-transfer: independent skeptic review

Status: EXPLORATORY review (Riemann Observatory). RH is open. Nothing in the report or in this review proves or disproves it.
Scope: every structured claim C5-00 to C5-A in `REPORT.md`, plus the code under `experiments/code/C5-function-field-transfer/` and the outputs under `experiments/results/C5-function-field-transfer/`.
Reviewer: independent skeptic agent. I did not use the investigator's drivers or helper library for any count reported below. The one exception is `ff_common.h_from_P`, used once to recover h for example (c), and its output was then checked independently.
Date: 2026-11-17.

## 1. What I actually did

### 1.1 Proofs re-derived line by line

- C5-L0, L1, L2, T1, T2, T3, S1 and D1 were all re-derived.
- The mini-lemma behind ML-W (Connes' Lemma 2.1) was re-derived.
- For C5-T3 I also proved a confluent (repeated-root) version and an extension of the window corollary to the case where RH fails. Both are in Section 3.

### 1.2 Independent re-implementations

All new code is under `experiments/code/C5-function-field-transfer/`.

| script | what it checks | how it differs from the investigator's code | runtime |
|---|---|---|---|
| `skeptic_census_indep.py` | E1, all 24 (q,g) pairs | Own construction of P and own Newton/Möbius code. Tail certificate uses sum_i (\|alpha_i\|/q)^d, which is sharper than 2g r^d. Exact B_d for d<=60 is computed **before** any tail test. RH is decided by exact Sturm counts on h and on k(u)=prod(u-x_i^2). The g=1 boundary is decided exactly. | about 76 s, plus 111 s for (4,3) |
| `skeptic_inertia_exact.py` | E3 and C5-T3, plus non-squarefree cases | T_N is congruent to the **integer** matrix G_N=(q^{min(m,n)} s_{\|m-n\|}) via D=diag(q^{m/2}). Inertia is then read off exactly from Descartes' rule on the real-rooted characteristic polynomial. No floating point and no Arb. | a few minutes |
| `skeptic_pointcount.py` | E2 | Own F_{p^r} arithmetic, using an irreducible polynomial found by trial division, then brute-force point counts. | under 1 min |
| `skeptic_quadratic_indep.py` | E4 | Uses the log-derivative identity -s_n = sum_{d\|n} d(x_d+(-1)^{n/d}y_d) instead of the investigator's c_d - y_{d/2} recursion. Exact for n <= max(D1,80). | a few minutes |

Environment: Python 3.13.18, python-flint 0.9.0, sympy 1.14.0, numpy 2.5.3, at most 2 cores. Hashes are in `experiments/results/C5-function-field-transfer/SKEPTIC_SHA256SUMS`:

- `skeptic_census_small.json` 8232795e…
- `skeptic_census_q4g3.json` 9e5835f3…
- `skeptic_inertia_exact.json` ad10e05b…
- `skeptic_pointcount.json` c69efcec…
- `skeptic_quadratic_indep.json` 71b3cc9d…
- `skeptic_undecided_resolution.json`: per-case first negative B_d for the 55 investigator "undecided" cases (14 g=1 + 41 g≥2)

The investigator's SHA256SUMS were re-hashed and all five match.

### 1.3 Sources opened

Full texts:

- Milne arXiv:1509.00797, secs 1 and 5, with page headers checked.
- Suzuki arXiv:2610.41115: sec 4 including Prop 4.3 and its proof; sec 8.
- Pritsker arXiv:1307.5361: sec 1.
- Deninger arXiv:2204.02714: secs 1-2, including Thm 2.13 and 2.15.
- Borger arXiv:0906.3146: p.5.
- Haran arXiv:2209.08536: Rem 4.12.
- Connes-Consani arXiv:2602.15941 (Thm 1.1), 2306.00456 (Thm 1.1), 2606.06604 (Thms 1-2) and 1910.14368 (Conj. 4.1 and its context).
- Hesselholt arXiv:1602.01980: Thm A and the periodicity remark.
- Scholze arXiv:1606.01796: p.3.
- Deligne, Weil I: Numdam scan, page footers checked.

Abstracts only (arXiv API): Zhu 2608.24827; Andrews-Connes-La Gatta 2611.13129; Suzuki 2610.32704; Niedbala Giraudin 2610.00386; Gauthier-Tarkhanov 1008.0499.

zbMATH reviews: Zhang 1990 (Zbl 0723.11047); Cohen 1989 (Zbl 0679.10037); the Knopfmacher-Zhang monograph (Zbl 0982.11054); Terras (Zbl 1206.05003).

## 2. Verdict summary

| claim | verdict | one-line reason |
|---|---|---|
| C5-00 | upheld with corrections | Header is accurate, except for the census, window and OB-9 corrections below. |
| C5-L0 | upheld | Re-derived, including the claim that non-real x forces \|alpha\| != sqrt q. |
| C5-L1 | upheld | Re-derived. "Positive lower density" is not shown, but infinitely many d is enough. |
| C5-T1 | upheld | Projection formula, Gram identity and Rosati trace all re-derived. Classical. |
| C5-T2 | upheld | Re-derived. The 2x2 minor is exactly Milne's Cor. 1.6 for (Delta, Gamma_r). |
| C5-T3 | upheld with corrections | Inertia statement is correct. RH <=> T_{2g}>=0 does **not** need squarefreeness (confluent version proved and checked exactly). The window corollary holds without RH. "Over Q no finite window can suffice" is not a theorem. |
| C5-I-W | upheld | Milne pp.8-10 locations verified exactly. |
| C5-I-S | could not check | Bombieri's Bourbaki 430 not opened. The content matches standard accounts. |
| C5-I-D | upheld with corrections | Weil I locations verified, except that Cor (3.8) and (3.9) are both on p.286, not pp.285-286. Milne sec 5 pages verified. |
| C5-I-E | upheld | Checked against Observatory records PAPER-0090 and PAPER-0119, not primary sources. |
| C5-TABLE | upheld with corrections | Spot-checked cells are accurate. The t_Z([0,1]) bracket is outdated. Some cells inherit the OB-2c, OB-9 and ML-C1 issues. |
| C5-E1 | upheld with corrections | All g>=2 counts reproduced exactly. The 41 "undecided" cases are all non-admissible (B_d<0 at d<=7). For g=1 the boundary a=q+1 (Z=1) **is** admissible, so every q misses one degenerate fake. Conceptual prior art exists. |
| C5-E2 | upheld | Every listed N_r reproduced by independent brute force. |
| C5-E3 | upheld | Exact integer inertia check agrees on all 3,300 cases, including T_{2g+1}. This upgrades the investigator's float-only cases to exact. |
| C5-L2 | upheld | Mod-2 / big-Witt argument and tail bound G(d) re-derived. |
| C5-E4 | upheld | All counts reproduced by a different algorithm. The interpretation is heuristic. |
| C5-S1 | upheld | Landau argument re-derived. Strengthening in Section 3.4. |
| C5-D1 | upheld | Trivially correct. The Kurokawa identification was not checked. |
| C5-OB1 | upheld | Haran Rem 4.12 and Borger verified. Arithmetic-site defect matches the PAPER-0086 record. |
| C5-OB2 | upheld with corrections | (a) is correct (numerically consistent up to T=74,920). (c) "does not imply it" is not a provable statement about the single function zeta. |
| C5-OB3 | upheld | Borger quote verified on p.5. |
| C5-OB4 | upheld | Deninger Thm 2.13 and its proof verified. |
| C5-OB5 | upheld with corrections | Function-field instances verified. The phenomenon has prior art (arithmetic semigroups, Ihara zetas). "Both directions" is heuristic. |
| C5-OB6 | upheld with corrections | "Cannot even give the PNT" overstates Pritsker, who explicitly leaves weight sequences open. The bracket is outdated. |
| C5-OB7 | upheld | Heuristic. The Langlands remark is verified in Milne pp.51-52. |
| C5-OB8 | could not check | Rests on Connes 1999 and CCM through records only. |
| C5-OB9 | upheld with corrections | The decay law exp(-L e^L) is a misquote: in Zhu it is an RH-conditional **upper bound**. The actual decay is about exp(-c e^{2L}), and the precision estimate is off by hundreds of digits. |
| C5-ML-W | upheld | Lemma re-derived. It is a faithful RH-equivalent restatement of Connes 2016. |
| C5-ML-W0 | upheld with corrections | Well-posed target. Needs degree invariance under linear equivalence written into (a)-(b). |
| C5-ML-C1 | upheld with corrections | Wording of which function is supported in the window should follow CC's intended reading. Zhu's unrefereed Pos(0.8) already covers the window numerically. |
| C5-ML-E1 | upheld with corrections | "Over Q no finite L suffices" is not a theorem. |
| C5-ML-Den | upheld | Faithful to Deninger 2.15. |
| C5-ML-TP | upheld | Consistent with Hesselholt Thm A and his periodicity remark. |
| C5-ML-F1 | upheld | Open target. CCM Prop 7.2 checked at record level only. |
| C5-ML-S | upheld | Matches Pritsker's Problem 1.4. |
| C5-A | upheld with corrections | Inherits the OB-2c and OB-9 errors. It also conflates numerical certification with proving CC Conj. 4.1. |

No claim was refuted. Nothing in the report claims a proof of RH or anything stronger than it supports, apart from the "no finite window over Q" phrasing.

## 3. New mathematics produced in this review (all elementary)

### 3.1 Confluent inertia theorem (THEOREM; answers the report's first open question)

**Setting.** Let P ∈ R[T], P(0)=1, deg P=2g, satisfy P(T)=q^g T^{2g}P(1/(qT)). Let the distinct normalised reciprocal roots be γ_1,…,γ_r, with multiplicities μ_j. Let m=#{j : |γ_j|>1}.

**Statement.** For every N ≥ r, inertia(T_N) = (n_+, n_-, n_0) = (r−m, m, N−r). In particular RH ⇔ T_r ⪰ 0 ⇔ T_{2g} ⪰ 0, **with no squarefree hypothesis**. Under RH, rank T_N = r for N ≥ r, which is Suzuki Prop 4.3 with d = r.

**Proof.**
1. T_{kl} = Σ_j μ_j γ_j^{k−l}.
2. Let V=(γ_j^k), an N×r Vandermonde matrix with distinct nodes. It has full column rank for N ≥ r.
3. Let A_{jl} = μ_j·[γ_l = 1/γ̄_j]. The multiset is stable under γ ↦ 1/γ̄, because of the functional equation and real coefficients, and μ is constant on orbits. So A is Hermitian, and T = V A V*.
4. A is a direct sum of 1×1 blocks (μ_j > 0) where |γ_j| = 1, and 2×2 blocks [[0,μ],[μ,0]] (eigenvalues ±μ) on pairs with |γ| ≠ 1.
5. Extend V to an invertible W = [V | V'] and apply Sylvester's law of inertia. ∎

**Exact check.** `skeptic_inertia_exact.py` verifies the formula for N = 2g, 2g+1, 2g+3 on:
- all 3,300 squarefree admissible P (9,900 checks, 0 failures);
- all 249 non-squarefree checks from the same censuses (0 failures);
- 93 synthetic FE polynomials with repeated roots, RH true and false (0 failures; RH ⇔ T_{2g} ⪰ 0 held in all 93).

### 3.2 Window corollary without RH (PROPOSITION-PROOF-SKETCH)

**Setting.** For u ∈ C_c^∞(−a,a), let W(u) = Σ_ρ m_ρ û(γ_ρ) conj(û(γ̄_ρ)). This is the zero side of the explicit formula for u*ũ.

**Fibre decomposition.**
1. Ordinates lie in γ_j + 2πZ/h, with h = log q and ζ_j = e^{iγ_j h}. Off-circle ζ_j are allowed.
2. Polarised Parseval on each residue class gives Σ_n û(γ+2πn/h) conj(û(γ̄+2πn/h)) = h∫_0^h L_γu(t) conj(L_{γ̄}u(t)) dt.
3. The integrand equals Σ_{k,l} ζ^{k−l} u_k ū_l, since e^{iγt}·conj(e^{iγ̄t}) = 1.
4. Hence W(u) = h∫_0^h ⟨T_{r(t)}u(t), u(t)⟩ dt with Toeplitz entries Σ_j m_j ζ_j^n.

This is Suzuki's (4.1) and the proof of his Prop 4.3, verbatim, with "≥ 0" replaced by an inertia statement.

**Consequence.** Combined with 3.1:
- RH(C) ⇔ W ≥ 0 on C_c^∞(−a,a) for any one a > (g−½) log q.
- In particular, the window [−g log q, g log q] of C5-T3 works for all P satisfying the FE, not only squarefree ones.
- The skeptic census shows fakes whose first indefinite T_N has N = 2g, for example q=3, g=3, h=x³−10x−7, where T_5 ≻ 0 and T_6 is indefinite. So for the formal class, a ≤ (g−½) log q does not suffice.

### 3.3 Logical correction: "over Q no finite window suffices"

Take Pos(L) ⇒ RH for the single function ζ. If RH is true, this implication is true for every L. So "no finite window can suffice" (C5-T3, OB-2c, ML-E1, C5-A) cannot be a theorem about ζ unless RH is false.

Two coherent readings exist, and both must be labelled HEURISTIC:
- meta-mathematical: no known argument derives RH from Pos(L);
- model-theoretic: for abstract zero multisets, a small enough off-line displacement survives any fixed window. This is plausible but was not proved by the investigator.

The function-field contrast that *is* a theorem: over F_q a finite window provably decides RH, by finite rank (3.1, 3.2). No finite-rank mechanism is known over Q.

### 3.4 Asymmetry of one-sided bounds over F_q (THEOREM, elementary; complements C5-S1)

**Setting.** P satisfies the FE with real coefficients.

**Statement.** If N_r ≥ q^r + 1 − C q^{r/2} for all r, equivalently s_r ≤ C q^{r/2}, then RH holds.

**Proof.** Take A = max|α|. If A > √q, the dominant-modulus power sum S_r = Σ_{|α|=A}(α/A)^r is real, has mean ≥ 0 and mean square ≥ 1. Exactly as in C5-L1, S_r ≥ 1/(4M) for infinitely many r. Then s_r ≥ A^r/(4M) − 2gA'^r, which exceeds C q^{r/2} for such large r. ∎

**Consequences.**
- Over F_q the *lower* half of the Stepanov-Bombieri estimate already implies RH. The upper half does not: the g=1 fakes with α > √q are counterexamples, which confirms C5-S1 and Bombieri's remark.
- Over Q, Landau's argument works for **either** one-sided bound on ψ(x) − x, since ζ has no real zeros in (θ, 1). This also matters for OB-6: the Gelfond-Schnirelman method produces *lower* bounds on ψ, which would suffice just as well.
- I did not search for prior art on this statement. It is likely folklore.

## 4. Claim-by-claim notes (only where something needs saying)

**C5-E1, the census.**

The g >= 2 counts are reproduced exactly and exhaustively: 23/23/0, 74/57/17(8), 172/93/79(45), 326/127/199(111), 880/205/675(380), 1303/252/1051(596), 1843/309/1534(880); and for g=3, 172/147/25(11), 1759/609/1150(825), 9366/1541/7825(6035). The max first Hasse-Weil violation and the max first indefinite N also match (5,5,5,7,8,5; 20,28,23; N = 4 or 6).

Two corrections:

(i) **The 41 "undecided" g>=2 cases are all non-admissible.** Each has B_d < 0 at some d ≤ 7; the list is in `experiments/results/C5-function-field-transfer/skeptic_undecided_resolution.json`. `ff_common.positivity_all_degrees` returns `undecided_cap` before computing any B_d beyond the pruning prefix d ≤ g. So the report's description ("A/q > 0.9997, tail certificate would need D0 > 4000") is wrong in substance. The exclusion happened to be correct.

(ii) **The g=1 boundary is decidable, and admissible.** Only a = q+1 is undecided. The report says a = ±(q+1), but a = −(q+1) has B_2 < 0. For P = (1−T)(1−qT) we get Z ≡ 1 and all N_e = 0, hence all B_d = 0 ≥ 0. So (F1)-(F3) hold and RH fails (α = 1, q).

Corrected g=1 rows have one extra fake each. For example q=2 becomes 6/5/1, not 5/5/0, so "no g=1 fakes for q ≤ 4" holds only up to this degenerate Z = 1. Corrected totals are 16,368 admissible and 12,801 fakes, or the report's numbers if the degenerate empty zeta is excluded by definition. The report should state that convention.

Worked examples (a), (b) and (c) were reproduced: N, B, |β|, first violation k = 1, 28 and 20, and T_6 indefinite while T_5 ≻ 0.

Prior art (conceptual): any fake with B_d ≥ 0 is an *additive arithmetical semigroup* in the sense of Knopfmacher, with B_d primes of degree d. Its zeta P/((1−y)(1−qy)) satisfies Axiom A# whenever max|α| < q. In that literature it is known that Axiom A# does not force a Riemann-type hypothesis, or even the absence of an exceptional zero at y = −1/q:
- W.-B. Zhang 1990, Zbl 0723.11047 ("discusses the general non-validity of a Riemann-type hypothesis");
- Indlekofer-Manstavičius-Warlimont 1991;
- Knopfmacher-Zhang 2001, Zbl 0982.11054.

Ihara zeta functions of non-Ramanujan (q+1)-regular graphs are a second family of the same kind: rational Euler products with nonnegative integer prime-cycle counts and a functional equation, for which RH fails (Terras 2011, Zbl 1206.05003). There the "Riemann zeros" are poles, not zeros, so they are not curve-shaped.

So the claim "possibly new in this explicit certified form" is acceptable only for the curve-shaped census itself, not for the phenomenon.

**C5-E3.** My exact Descartes/integer-Gram method covers the 52 T_{2g+1} cases and the 1 T_{2g} case that the investigator certified only in floating point. All agree.

**C5-E4.** Counts reproduced exactly: g=1 64/64; g=2 8/17, 133/199(57), 482/675(225), 1122/1534(547); g=3 362/1150(212). The method is different from the investigator's. My first run gave 0 realisations because of **my own bug**: n_1(P^1) = q instead of q+1. This is recorded in the code comment as negative knowledge. After the fix, everything agrees.

**C5-L2.** The step "1+TF_2[[T]] is topologically free over Z_2 on {1+T^m : m odd}" is correct. Every element is uniquely Π_n(1+T^n)^{ε_n} with ε_n ∈ {0,1}, and grouping n = 2^j m turns this into 2-adic exponents. The bound G(d) and the monotonicity thresholds in `tail_D1` are correct.

**C5-T3 prior art.** Suzuki 2026 Prop 4.3 already contains the RH-side statement (H_r ≻ 0 for r ≤ d, rank d for r > d, with d the number of *distinct* zeros). The off-circle count is the unit-circle analogue of Hermite's power-sum/Hankel theorem (rank = number of distinct roots, signature = number of distinct real roots). "Not claimed new" is correct.

**C5-OB2(a).** Σ_{|γ|<T} 1/|ρ| at T = 74,920.83 (10^5 zeros) is 13.99. The leading term (log T)²/(2π) = 20.05, ratio 0.70 and slowly rising. The better form (log(T/2π))²/(2π) = 14.02 agrees to about 0.03. The asymptotic is correct, but convergence of the stated leading term is slow. Treating this sum as the analogue of def(Δ) is a choice of convention, and should be labelled HEURISTIC.

**C5-OB6.** Pritsker (p.4) says of fixed weights only that B(w) < 1. He then writes: "this does not preclude the possibility that such a proof can be obtained by finding a sequence of weights w_n with B(w_n) → 1." So "auxiliary integer polynomials cannot even give the PNT" should read "not with the one-variable method, nor with any fixed weight of type (1.12)". The current bracket for t_Z([0,1]) is 0.4222286 ≤ t_Z ≤ 0.4226847 (Niedbala Giraudin 2026, arXiv abstract; upper bound after Flammang 2014). It is still above 1/e, so the conclusion is unchanged.

**C5-OB9.** Zhu's abstract reads: "Under RH, λ_min(L) ≤ exp(−L e^L) for all large L". That is an *upper* bound. His empirical law is −ln λ_min ≈ 2π²N(T*)/ln N(T*) with T* = 2πe^{2L}, which is about 2π²e^{2L}. Andrews-Connes-La Gatta give ε_λ ≤ Cδ_4(λ)(log λ)³ with δ_n ~ c_nλ^{2n+1}e^{−4πλ²}, a theorem of Connes-Kastoris. That is again exp(−c e^{2L}) with L = log λ.

The report's own data points refute exp(−L e^L). At L = 2 it gives e^{−14.8} ≈ 4×10^{−7}, against the reported 3.2×10^{−283}. Correct statement: certification precision grows like e^{2L}/ln 10 digits, up to a constant, not like L e^L. "Doubly exponential" remains true.

**C5-ML-C1.** CC 1910.14368 Conj. 4.1 says "test functions with support in (q^{−1/2}, q^{1/2})" for S = {∞} ∪ {p < q}. Consistency with the q=2 case (PAPER-0099: g supported in [2^{−1/2}, 2^{1/2}]) shows that the *factor* h_1 (or g) is the function supported in the window, while the convolution lives in (1/q, q). The report's wording "h = h1*h2-type supported in …" should say "h_1 supported in (3^{−1/2}, 3^{1/2})". Under that reading the window is Pos((log 3)/2) = Pos(0.549). Zhu's unrefereed, unreplayed Pos(0.8) would already cover it numerically, so the content of ML-C1 is the *mechanism*.

**C5-ML-W and ML-W0.** Lemma check:
- set x' = x − ⟨x,ξ_1⟩ξ_0 − ⟨x,ξ_0⟩ξ_1;
- then x' ⊥ ξ_0 + ξ_1, so effectivity gives ⟨x',x'⟩ ≤ 0;
- and ⟨x',x'⟩ = ⟨x,x⟩ − 2⟨x,ξ_0⟩⟨x,ξ_1⟩.

Conversely, given RH, take E = C_c ⊕ Rξ_0 ⊕ Rξ_1 with the obvious form. Effectivity there is equivalent to s(f,f) ≤ ∫f d*u ∫f du, which is Weil's criterion including the pole term.

For ML-W0, the deduction (c) ⇒ s(f,f) ≤ 0 needs one more item written into (a)-(b): the degree against Ψ(1)+Ψ(1)^t must be invariant under linear equivalence and equal ∫f d*u + ∫f du on D(f).

**C5-A.** "Certification is a standard interval-arithmetic task" applies to the numerical inequality on a window. It does not apply to ML-C1, which asks the semilocal framework to *prove* it (identifying ker u(F)_22 with the Sonin space). Those are different kinds of task. The rest of the ranking is a reasonable judgement.

## 5. General issues

1. **Census code flaw.** The undecided branch skips the cheap exact B_d screen; it should compute B_d for small d before giving up. It did not change any g ≥ 2 count, but it misdescribed 41 cases and missed the decidable g=1 boundary.
2. **"No finite window over Q".** This is a logical error repeated in four places (T3, OB-2c, ML-E1, A); see 3.3.
3. **OB-9.** It inverts Zhu's RH-conditional upper bound into a decay law; see Section 4.
4. **Prior art for the "formal axioms do not imply RH over F_q" theme.** Arithmetical semigroups (Knopfmacher, Zhang, Indlekofer-Manstavičius-Warlimont) and Ihara zetas of non-Ramanujan graphs should be cited in E1 and OB-5.
5. **Outdated bracket.** The t_Z([0,1]) bracket (OB-6, TABLE S3) should be updated.
6. **Minor page error.** Weil I Cor (3.8) and (3.9) are both on p.286.
7. **The report's open question on a confluent C5-T3 is answered** (3.1). The open question on Suzuki's decomposition without RH is answered at proof-sketch level (3.2).
8. **What was not verified by me.**
   - Bombieri Bourbaki 430 and Stepanov.
   - Connes 1999 Thms 1, 4, 5 and CCM 2009, except through records.
   - Weil 1948, Weil 1952, Weil II, Laumon.
   - Kurokawa's multiplicity conventions.
   - Zhu's Pos(0.8): no replay.
   - Deninger 2018 leafwise cohomology.

## 6. Negative knowledge recorded

- Skeptic bug, fixed: counting degree-1 places of P^1 as q, which omits ∞, makes every fake non-realisable in E4. The investigator's `n_places_P1` is correct.
- The tail certificate based on 2g(A/q)^d is very weak when one dominant root is real and close to q. Replacing it with Σ_i(|α_i|/q)^d, and screening exact B_d first, removes every "undecided" case in the 24 tested pairs.
