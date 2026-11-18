# C2-countermodel-zoo: FINAL (adjudicated)

This is the adjudicator's report. `REPORT.md` (investigator) and `SKEPTIC_REVIEW.md` (skeptic) are kept unchanged as the record. Where this file disagrees with either of them, this file gives the final status and the reason.

RH is open. Nothing here proves or disproves RH, GRH, or any RH analogue for a member of the Selberg class. A countermodel only shows that some set of hypotheses does not imply "all nontrivial zeros on the symmetry line". It says nothing about whether zeta satisfies that conclusion.

```text
Status:
  ADJUDICATED EXPLORATORY DOSSIER (Riemann Observatory, independent campaign C2). No claim about RH.
  - THEOREM, with a complete proof given or completed here:
      C2-01 (Krawczyk test); C2-15 (synthetic xi~); the C2-16 identity; C2-21 (continuous Beurling toy);
      C2-24 (meta-lemma);
      C2-05 and C2-11 (right edges; computer-assisted with Arb partial sums plus explicit tail bounds);
      C2-14 (Turan inequalities for every H_t, t real), UPGRADED from CONDITIONAL. It depends on one IMPORTED
        input read only at L0+: log Phi(sqrt v) is concave (Csordas-Varga 1988). The moment lemma is proved here;
    adjudicator additions:
      C2-ADJ-1: the RH-false Euler-product family M10;
      C2-ADJ-2: the exact s=1/2 threshold for rectangular Epstein functions. It shows that
        Betermin-Samaj-Travenec Conjecture 1.1 is FALSE;
      C2-ADJ-3: the moment lemma;
      C2-ADJ-6: unconditional uniform large-shift Jensen hyperbolicity for an off-line-perturbed H_{0.2}.
  - NUMERICAL-RIGOROUS (Arb): every certified off-line zero.
      DH: 5 zeros. Epstein x^2+5y^2: 35 zeros in the strip and 9 with sigma>1 (two of them certified here a second
      time, by an independent method). Epstein x^2+57y^2: a real zero. H_t: 2 zeros. zeta_19: 1 zero.
      Completeness, UPGRADED: the off-line zeros of DH with |t|<=300 and of Epstein with |t|<=200 are exactly the
      certified ones.
  - CONDITIONAL: the "uniform in d" Jensen statement for xi~ = xi*P_Q (C2-17a, C2-28a). It needs zeta to have only
    finitely many off-line zeros, because Craven-Csordas-Smith needs finitely many non-real zeros.
  - NUMERICAL-NONRIGOROUS: the Li thresholds (CORRECTED: 20855, 7477, 112538, 40908), the hyperbolicity of rounded
    Jensen polynomials, the screens, and the mpmath replays.
  - HEURISTIC: detection scales, the "must use the Euler product" reading of the hitting set (C2-25 tail, C2-31),
    and C2-26's "must use FE or integrality".
  - REFUTED: (a) Liu-Wu (arXiv:2503.24275), "non-trivial zeros of the DH function can only lie on the critical
    line" (C2-07). (b) C2-00(i)/C2-31, "no RH-false function with an ordinary Dirichlet series, an Euler product
    over the rational primes and a self-dual FE is known; one would contradict GRH for the Selberg class". M10 is a
    witness. (c) BST Conjecture 1.1 (side finding, C2-ADJ-2).
  - WITHDRAWN: the investigator's Li table entries (20857, 7395, 112929, 41098); "Epstein zeros with sigma>1 first
    found near 3.6e6"; the matrix label "NN/CONJ" for real Epstein zeros with k > 4 pi e^{-gamma}.
  Evidence level of this adjudication:
    L2 for C2-14, C2-16, C2-21, C2-ADJ-1..3, C2-ADJ-6 (re-derived);
    L1 for these primary texts: Betermin-Samaj-Travenec arXiv:2110.09368v2 (pdf sha256 12898818...),
      Perelli arXiv:1605.02354v1 (1e09b1fa...), Johansson arXiv:1309.2877 (ac0bee43...);
      arXiv abstracts of Liu-Wu 2503.24275 and 2010.03521;
    L0+ (zbMATH review only) for Csordas-Varga 1988 (Zbl 0696.30007) and Craven-Csordas-Smith 1987 (Zbl 0625.30036);
    L0 for Bateman-Grosswald 1964 (Zbl 0128.27004: no review text, not accessed).

Scope:
  The whole zoo (M0-M9 of property_matrix.csv, plus the new M10). The 33 investigator claims C2-00..C2-32, the 7
  skeptic findings F1-F7, and 8 adjudicator items C2-ADJ-1..8. The stress-test protocol is restated as precise
  implications over the predicates P1-P11 (section 4).

Exact sources or dependencies:
  Investigator code: experiments/code/C2-countermodel-zoo/*.py. Skeptic: .../skeptic/*.py.
  Adjudicator: .../adjudicator/*.py.
  Outputs: experiments/results/C2-countermodel-zoo/{., skeptic/, adjudicator/}, each with its own SHA256SUMS.
  Zeros: the 100000 Arb-certified zeta ordinates in the session scratchpad (zeros_1_50000.tsv,
    zeros_50001_100000.tsv; 100000 lines checked). They are used only for the Li coefficients.
  Software: Python 3.13.18, python-flint 0.9.0 (Arb), mpmath 1.3.0, numpy 2.5.3, scipy 1.18.1, sympy 1.14.0.

What was actually run (adjudicator; at most 2 cores; each run took 51 s or less):
  - Hash re-verification: investigator SHA256SUMS (12/12 OK) and skeptic SHA256SUMS (all OK).
  - adj_li.py (31 s, NN): lambda_n(xi) exactly for every n <= 115000, with the S(T*) boundary term that both
    earlier codes omitted; first negative n for the 4 quadruples, scanned from n = 1.
  - adj_epstein_rouche.py (2.6 s, Arb): a second, independent Rouche-Cauchy certificate for the Epstein zeros with Re s > 1 at
    t ~ 1193.95 and t ~ 4108.11. Evaluation is by the Hurwitz-zeta form of the genus decomposition.
  - adj_side_checks.py (3.4 s, NN): F1 (functional equation, predicted zeros, log-coefficients) and F7 (theta
    integral versus Chowla-Selberg at s = 1/2; the threshold k* and Delta*).
  - adj_dh_count.py (51 s, Arb): rigorous DH zero count on [-0.6,1.6] x [1,300] and [-0.6,1.6] x [-1,1]. It uses a
    new argument-principle routine whose boundary closes exactly, plus certified sign changes on the line.
  - adj_property_matrix.py (<1 s): property_matrix_adjudicated.csv.

Smallest remaining gap:
  (1) The protocol has a structural blind spot: any step that uses all of the Selberg-class axioms, i.e. Dirichlet
      series over N + FE + Ramanujan + Euler product with theta < 1/2. Exhibiting an RH-false member there would
      refute Selberg's GRH conjecture for S. So no zoo member can test such a step.
  (2) The following are not rigorous: J^{d,0} hyperbolicity for d up to 240; that t ~ 1193.95 is the LOWEST Epstein
      zero with sigma > 1 (screen for t <= 4200 only); the Li thresholds (float64 with a stated error budget).
  (3) The single statement whose failure would invalidate the main new theorem C2-ADJ-2 is the exact
      Chowla-Selberg value Z_k(1/2) = 2 gamma + 2 log(k/(4 pi)) + 8 sum_N d(N) K_0(2 pi N k). It is derived in
      section 3.2 and confirmed by an independent theta-integral evaluation: 30 digits at k = 3, and 12 digits on
      the value 8.39e-20 at k = 4 pi e^{-gamma}.
  (4) Prior art not accessed: Bateman-Grosswald 1964 may already contain the exact threshold equation;
      Balanzario-Sanchez-Ortiz 2007 may already list DH zero #5.
```

## 1. Resolution of the investigator/skeptic disagreements

The skeptic raised seven findings (F1-F7). All seven are upheld, two with qualifications. The adjudicator adds four items: A1 is a rigor defect in a skeptic tool, which was fixed and rerun; A2 explains a numerical discrepancy both parties left open; A3 is a citation correction; A4 is a proof that closes a gap both parties left open.

| finding | skeptic claim | adjudication | basis |
|---|---|---|---|
| F1 | zeta(s)(1+c2^{-s}+2*4^{-s}) is RH-false and has an ordinary Dirichlet series, multiplicative coefficients, an Euler product over the rational primes, and a self-dual degree-1 FE (conductor 4). So C2-00(i) and the blind-spot sentence are wrong. | **UPHELD → C2-ADJ-1 (THEOREM).** The proof is re-derived in sect. 3.1 and checked numerically: FE defect < 1e-50, \|F\| < 2e-50 at 12 predicted zeros. Folklore status confirmed. Perelli (arXiv:1605.02354v1, sect. 3, p. 15) writes that θ < 1/2 "rules out from S all non-trivial Dirichlet polynomials, which may violate the Riemann Hypothesis", and that "examples violating it can be produced if any of the five axioms is withdrawn". No paper giving this exact family was located. | adj_side_checks.json |
| F2 | Uniform-in-d Jensen hyperbolicity for xi~ needs CCS, i.e. finitely many non-real zeros of F~. That holds iff zeta has finitely many off-line zeros. So it is CONDITIONAL. | **UPHELD.** The CCS hypothesis is confirmed from the zbMATH review (real entire, order < 2, finitely many non-real zeros). The repair is promoted to a theorem (C2-ADJ-6). Citation correction: Λ ≤ 0.2 is Platt-Trudgian 2021, Cor. 2 (arXiv:2004.09765), not Polymath 15. Polymath 15 proved Λ ≤ 0.22. | sect. 3.4 |
| F3 | The Li table in C2-16 is wrong. Correct first-negative n: 20855, 7477, 112538, 40908. | **UPHELD**, by an independent code with a different tail treatment. Every value agrees. At the first negative n the values are -941.9, -289.6, -660.6 and -124.2. At n-1 they are +358.0, +553.0, +2958.4 and +425.0. λ_n(ξ~) > 0 for all n below the threshold, scanned from n = 1. At the investigator's n = 7395 the value is **+1.8726**, positive. | adj_li.json |
| F4 | Epstein zeros with Re s > 1 occur at t ≈ 1194, far below 3.6e6. | **UPHELD.** Second, independent certificate (Rouché-Cauchy, Hurwitz route; the skeptic used a winding number on another evaluation route). Re s = 1.011049334043550716... at t = 1193.946404528846107..., and Re s = 1.015070737693118293... at t = 4108.108282536442521.... Each zero is unique in a disc of radius 1e-12. | adj_epstein_rouche.json |
| F5 | The C2-14 premise is a theorem (Csordas-Varga 1988). | **UPHELD** at L0+: the zbMATH review of Zbl 0696.30007 says "log Φ(√t) is strictly concave on 0<t<∞". The open point about the moment lemma's range (p = -1/2) is **closed here by a proof** (C2-ADJ-3, sect. 3.3), so C2-14 is a THEOREM given that input. | sect. 3.3 |
| F6 | Completeness is rigorous: DH 214 = 204 + 2·5, Epstein 253 = 183 + 2·35. | **UPHELD, with A1.** The Epstein count stands as run. For the DH count, the adjudicator's rerun with exact boundary closure and a different evaluation route (Hurwitz form) gives winding [214 ± 3e-22], 204 certified sign changes, and a low box [0 ± 7e-24]. | adj_dh_count_T300.json |
| F7 | BST Conjecture 1.1 (Δ*_c = e^γ/(4π) exactly) is false by 4.2e-20 relative. Real off-line zeros exist for every k > 4πe^{-γ} (THEOREM). | **UPHELD and sharpened → C2-ADJ-2 (THEOREM).** Refuting the conjecture needs no numerics. At k = 4πe^{-γ} the exact value is Z_k(1/2) = 8 Σ d(N) K_0(2πNk) > 0, because every term is positive. The theta integral (independent code) reproduces 8.39166873936e-20. Δ* = 0.141733239663887191395415685..., so Δ* - e^γ/(4π) = 5.947e-21. BST's text (arXiv:2110.09368v2, p. 22) claims agreement "by at least 22 decimal digits". The true agreement is 19 decimal places; the numbers differ in the 20th. | adj_side_checks.json |
| A1 | (adjudicator) | Rigor defect in skeptic/sk_wind.py. Boundary points are generated as a+(b-a)·j/n in floating point, and on the top edge of a box with x0 = -0.6 the last point is -0.6000000000000001+iy1, not the corner. That leaves a 1.1e-16 boundary piece unenclosed, so the arg sum does not close. Visible symptom: sk_lowbox.json reports the DH winding enclosure [1.70e-17 ± 3.25e-20], which excludes the integer 0. The defect cannot change an integer count with margin 0.5, but as written the certificate is incomplete. The DH counts were rerun with exact closure (above). The Epstein boxes (x0 = -0.7) close exactly. | adj_dh_count.py |
| A2 | (adjudicator) | Both the investigator (462581.69) and the skeptic (462581.694) differ from Johansson's λ_100000 = 462580.782407 by 0.91. The skeptic estimated the tail-model error at about 0.02, which is too small at n = 1e5. The cause is the boundary term -g_n(T*)S(T*) of the smooth tail, with S(T*) = 0.5949 at T* = γ_100000⁺. With that term included, λ_100000 = 462580.782419. This agrees with Johansson to 1.2e-5 and is within the error bound 1.9e-4 (sect. 3.9). The first-negative indices do not change. | adj_li.json |
| A3 | (adjudicator) | Citation corrections. Λ ≤ 0.2 is Platt-Trudgian 2021, not Polymath 15. In the C2-16 text the detection scales were halved: the correct values of 1/rate are 1962.6, 785.2, 9002.6, 3601.2, 23806 and 100003. Two investigator matrix rows (M5c, M7) are malformed CSV: unquoted commas shift their columns. This is repaired in the adjudicated matrix. | property_matrix_adjudicated.csv |
| A4 | (adjudicator) | The moment lemma is proved here (sect. 3.3), so C2-14 no longer depends on unopened sources for the lemma (Karlin-Proschan-Barlow 1961 / Borell 1973 are now attributions only). | sect. 3.3 |

## 2. Adjudicated claims table

Status vocabulary follows methodology sect. 5-8. "→" marks a change from the investigator's label.

| id | final status | adjudicated statement (corrected where needed) | basis | change |
|---|---|---|---|---|
| C2-00 | header | (i) **REFUTED** as written: M10 (C2-ADJ-1) is RH-false with an ordinary Dirichlet series, an Euler product over Q-primes and a self-dual FE, and it is not in the Selberg class (it violates θ < 1/2). (ii) SUPERSEDED: completeness is now NUMERICAL-RIGOROUS (C2-04, C2-09). (iii) SUPERSEDED: the premise is IMPORTED (Csordas-Varga). | F1, F6, F5 | corrected |
| C2-01 | THEOREM | Complex Krawczyk test (exactly one zero in D, located in K, if K ⊂ int D). | proof in zoo_common.py; re-derived by skeptic | — |
| C2-02 | IMPORTED + NUMERICAL-RIGOROUS | Definition of the DH function, κ, the L-form, and the FE (5/π)^{s/2}Γ((s+1)/2)f(s) symmetric. Identity and FE checked in Arb at sample points by two routes. | Titchmarsh §10.25 (L0) | — |
| C2-03 | NUMERICAL-RIGOROUS | Five certified off-line DH zeros (first: 0.80851718245663738555 + 85.69934848537759217193 i). Certified by Krawczyk on the Hurwitz form (investigator) and by an Arb winding number on the L-form (skeptic). | dh_zeros.json, sk_dh.json | — |
| C2-04 | **NUMERICAL-RIGOROUS** | For 1 ≤ \|t\| ≤ 300, the zeros of f off σ = 1/2 are exactly the 5 certified zeros ρ and their images ρ̄, 1-ρ, 1-ρ̄. Every other zero with \|t\| ≤ 300 is simple and lies on σ = 1/2. There are no zeros with \|t\| < 1. Proof: the box [-0.6,1.6] × [1,300] contains all zeros with 1 ≤ t ≤ 300 (C2-05 and the FE). Its winding is 214, the line has 204 certified sign changes, and 214 = N_line + 2N_right with N_line ≥ 204 and N_right ≥ 5. | sk_dh_count, adj_dh_count (A1) | ↑ from NN |
| C2-05 | THEOREM (computer-assisted) + HEURISTIC + PROPOSITION-PROOF-SKETCH | f(s) ≠ 0 for Re s ≥ 1.13514. The skeptic's recomputation with P = 1e8 even allows 1.13086. The value 1.1204 is HEURISTIC. "sup Re ρ = the root of S(σ) = π - 2 arctan κ, which lies rigorously in [1.11464, 1.13086]" is a PROPOSITION-PROOF-SKETCH (Bohr-Kronecker), presumably the Bombieri-Ghosh 2011 result (IMPORTED, L0+). | dh_right_edge.json, sk_edges.json | — |
| C2-06 | NN + HEURISTIC + IMPORTED | No DH zero with σ ≥ 1 for t ≤ 4000 on the screened lines (on σ = 1, min \|f\| = 0.1839 at t ≈ 240.40, replayed). Infinitely many zeros in σ > 1 (Davenport-Heilbronn 1936). | sk_dh_sigma1 | — |
| C2-07 | **REFUTED** (target: Liu-Wu, arXiv:2503.24275 abstract and Thm 3.1; also 2010.03521) | The claim "non-trivial zeros [of the DH function] can only lie on the critical line" is false. Witnesses: (a) certified off-line zeros, by two independent methods and evaluation routes; (b) the classical theorem that the DH function has infinitely many zeros in σ > 1 (DH 1936; Titchmarsh §10.25). Failing step: a strict ratio inequality is evaluated at a common zero of f(s) and f(1-s), which is 0/0. Methodology class: `verified_error`, with an independent witness (skeptic). | REPORT, SKEPTIC §3 | — |
| C2-08 | IMPORTED (genus theory) + numerical checks | Z_{x²+5y²} = ζL(χ_{-20}) + L(χ_{-4})L(χ_5). Λ_Q(s) = (√20/2π)^sΓ(s)Z_Q(s) is symmetric. Checked by Chowla-Selberg at complex s (skeptic) and, in the adjudicator's Hurwitz route, against the lattice sum at s = 3 (agreement 1.0e-11, which equals the truncation error). | sk_epstein_cs.json, adj_epstein_rouche.json | label clarified |
| C2-09 | NUMERICAL-RIGOROUS | 35 certified off-line zeros of Z_{x²+5y²} with 2 ≤ t ≤ 200. **Completeness for 1 ≤ \|t\| ≤ 200 is rigorous** (253 = 183 + 2·35; no zeros with \|t\| < 1). So 15.6682495... is rigorously the lowest off-line zero. | epstein_zeros.json, sk_ep_count_T200.json | completeness ↑ |
| C2-10 | NUMERICAL-RIGOROUS | Three certified zeros with Re s > 1 at t ≈ 3.59e6, 4.13e6, 5.00e6 (the first re-certified by the skeptic). **Narrative corrected:** lower zeros with Re s > 1 are certified at t = 1193.9464 (σ = 1.011049) and t = 4108.1083 (σ = 1.015071) by the skeptic and the adjudicator, and at t ≈ 148065.85, 272795.96, 506416.50 and 939506.18 by the skeptic. | F4 | narrative withdrawn |
| C2-11 | THEOREM (computer-assisted) | Z_{x²+5y²}(s) ≠ 0 for Re s ≥ 1.17816 (S_upper = 2.9079 < π with P = 1e8). | sk_edges.json | — |
| C2-12 | NUMERICAL-RIGOROUS | Real zero of Z_{x²+57y²} in [0.654651202577622799100319554093, ...488]. Its existence also follows from C2-ADJ-2, because √57 > k* = 7.0555. Prior-art note: BST Conjecture 1.1 is false (C2-ADJ-2). | epstein_zeros.json, sk_epstein_cs.json | note added |
| C2-13 | IMPORTED + NUMERICAL-RIGOROUS + NN | H_t has a non-real zero for every t < 0 (Rodgers-Tao 2020, L0+). Certified zeros at t = -20 (59.93415640055167 + 4.35624274468846 i) and t = -50 (81.39103746111884 + 13.42451530784157 i), both reproduced to 18 digits by heat-flow convolution. | dbn_Ht.json, sk_dbn.json | — |
| C2-14 | **THEOREM** (given IMPORTED Csordas-Varga 1988, L0+) | For every real t and m ≥ 1: b_m(t)² > ((2m-1)/(2m+1)) b_{m-1}(t) b_{m+1}(t), with b_m(t) = ∫_0^∞ u^{2m}e^{tu²}Φ(u)du. Equivalently γ_m² > γ_{m-1}γ_{m+1} for γ_m = m!b_m/(2m)!. So all Turán inequalities hold for every H_t, including every t < 0, where H_t has non-real zeros. Proof: sect. 3.3. | F5, C2-ADJ-3 | ↑ from CONDITIONAL |
| C2-15 | THEOREM | ξ~ = ξ·P_Q is entire of order 1, real, satisfies ξ~(1-s) = ξ~(s), and its zeros are those of ξ plus Q. ζ·P_Q is unbounded on σ = 2, so it is not an absolutely convergent Dirichlet series in σ > 1. | elementary | — |
| C2-16 | THEOREM (identity) + **NUMERICAL-NONRIGOROUS (corrected table)** | λ_n(ξ~) = λ_n(ξ) + Σ_{ρ∈Q}[1-(1-1/ρ)^n]. First n with λ_n(ξ~) < 0: **20855** for (0.6,14), **7477** for (0.75,14), **112538** for (0.6,30), **40908** for (0.75,30). Not reached by 2e5 for (0.8085,85.7) and (0.6,100). The heuristic predicts about 3.2e5 and 1.5e6. Scales 1/rate: 1962.6, 785.2, 9002.6, 3601.2, 23806 and 100003, each ≈ γ0²/δ within 0.2%. | adj_li.json, sk_li.json | table replaced |
| C2-17 | split | (a) **CONDITIONAL** on zeta having only finitely many off-line zeros: for ξ~, J^{d,n} is hyperbolic for all d once n ≥ n0. (b) Unconditional analogue: **THEOREM** C2-ADJ-6. (c) "Some RH-false function has the (non-uniform) GORZ property": THEOREM, by the skeptic's case split, given IMPORTED GORZ 2019. (d) Turán signs k ≤ 78: NUMERICAL-RIGOROUS. Hyperbolicity for d, n ≤ 40 (d+n ≤ 79): NN, replayed independently. First non-hyperbolic J^{d,0} at exactly d = 40 for (0.9,5): NN, replayed. J^{d,0} hyperbolic up to d = 240: NN, not replayed. (e) "Visibility tracks Im X0/\|X0\|": HEURISTIC. | F2 | THEOREM → CONDITIONAL (a) |
| C2-18 | NUMERICAL-RIGOROUS (Turán signs) + NN (hyperbolicity) | Turán k ≤ 78 and J^{d,n} with d, n ≤ 40 hyperbolic for ξ_f (DH) and ξ_Q (Epstein), despite off-line zeros at heights 85.7 and 15.67. The Epstein part was replayed independently from theta moments. The DH part was not replayed. | synthetic_xi.json, sk_jensen_epstein.json | — |
| C2-19 | IMPORTED (secondary sources at L1; DMV itself L0) | DMV 2006: for each θ ∈ (1/2,1) there is a discrete g-prime system with N(x) = ρx + O(x^θ), π(x) = Li(x) + Ω_±(x exp(-c√log x)), and zeros realizing the de la Vallée Poussin region. The brief's "x^{1/2}-ish" description fits Zhang 2007 and BDR 2023, not DMV. | BDV 2004.11501; Broucke 2507.13780 | — |
| C2-20 | IMPORTED | Zhang 2007 (L0+); BDR 2023 Thm 1.1 (α ∈ [0,1), β ∈ [1/2,1)) and Thm 1.3 (assuming RH: β ≥ 2α/(α+2) > 2/5 for 1/2 < α < 2/3) (L1). | — | — |
| C2-21 | THEOREM | Explicit continuous Beurling system: dΠ ≥ 0, dN ≥ 0, ζ_Π = (s/(s-1))exp(-E1((s-ρ)L) - E1((s-ρ̄)L)), zeros exactly {0, ρ, ρ̄}, the exact explicit formula, and N(x) = Ax + O(x^σ) for every σ > β. Wording: "Euler product" here means ζ = exp∫x^{-s}dΠ with a continuous prime measure, not a product over discrete primes. | proof in REPORT; re-derived by skeptic and adjudicator | wording |
| C2-22 | NUMERICAL-RIGOROUS | ζ_19 has a zero with Re ρ ∈ [1.0010955115364748, 1.0010955115364778] near t = 600884.20343. It is certified by two methods. That it is the lowest such zero for t ≤ 2e6 is NN (Newton-step screen). | partial_sums_N19.json, sk_zeta19.json | — |
| C2-23 | IMPORTED (L0/L0+) | Hurwitz, Selberg and Ihara rows, with corrections. Selberg: "RH-false" means nontrivial real zeros in (1/2,1), besides s = 1 and the topological trivial zeros. Ihara: the RH analogue concerns the poles of Z(u), u = q^{-s}, with λ = q^s + q^{1-s} (not s(1-s) = λ). It holds iff the graph is Ramanujan. | — | wording |
| C2-24 | THEOREM | Meta-lemma: if a member W satisfies predicates P_1..P_k with the normalisation stated for zeta and W is RH-false, then P_1 ∧ ... ∧ P_k ⇏ RH_W. A step whose only zeta inputs are P_1..P_k cannot decide RH. Caveat (Hamburger, as generalised by Perelli 2016 sect. 3): in S^#, degree 1 + conductor 1 ⇒ F = cζ. So the lemma bites only on steps that do not use conductor 1 together with a degree-1 FE. | elementary | — |
| C2-25 | split | "S1 ⇏ RH" (DH witness): THEOREM. Corrected Epstein clause: replacing "entire, degree 1, \|a_n\| ≤ 1, a_1 = 1" by "pole at s = 1, degree 2, 0 ≤ a_n ≪ n^ε" still does not imply RH (witness Z_{x²+5y²}/2): THEOREM. "A valid proof must use multiplicativity / the Euler product": **REFUTED as a necessity claim**, since DH also lacks positivity, the pole and conductor 1. It is not sufficient either: M10 has an Euler product. The valid form is the hitting-set statement in sect. 4. | F1 | → split |
| C2-26 | split | "S2 ⇏ RH": THEOREM (imported DMV/Zhang/BDR, plus C2-21). "Must use a FE or integrality": HEURISTIC. Boundary statement (no RH-false Beurling system with N(x) = Ax + O(x^θ), θ < 1/2, is known unconditionally; BDR reach β > 2/5 assuming RH): IMPORTED state of the literature (BDR, L1), not an exhaustive search. | — | → split |
| C2-27 | THEOREM (meta) given IMPORTED; PROPOSITION-PROOF-SKETCH (trace-formula positivity ⇔ λ_1 ≥ 1/4) | S3 (Euler product over norms > 1, FE s ↔ 1-s, nontrivial zeros ↔ spectrum) ⇏ RH. Witnesses: Selberg zeta with λ_1 < 1/4; Ihara zeta of non-Ramanujan graphs (stated for poles). | C2-23 | wording |
| C2-28 | split | Structural uniform-in-d part for ξ~: **CONDITIONAL** (as C2-17a); unconditional version C2-ADJ-6. Finite ranges: Turán k ≤ 78 (NR), J^{d,0} d ≤ 240 for (0.6,5) (NN), **λ_n > 0 for n ≤ 20854** for (0.6,14) (NN; corrected from 20856). | F2, F3 | THEOREM → split |
| C2-29 | THEOREM given IMPORTED Rodgers-Tao (L0+) | If a kernel class contains Φ and is closed under K ↦ e^{-εu²}K for some ε > 0, then "every member has a real-rooted cosine transform" is false. The Turán part (all moment Turán inequalities hold in the class {e^{tu²}Φ : t ∈ R}) is a THEOREM via C2-14. | C2-13, C2-14 | Turán part ↑ |
| C2-30 | SP-7 IMPORTED + NR; SP-8 THEOREM (logic) + NR; SP-9 IMPORTED | SP-7: Turán's route through zero-free ζ_N is closed (Montgomery 1983; Platt-Trudgian 2016; ζ_19 certified). SP-8: no finite zero census can *establish* RH. A census can refute it, so "decide" was wrong. In natural relatives, the rigorously lowest off-line zeros are at 15.67 (Epstein) and 85.70 (DH). Zeros with σ > 1 are certified at t ≈ 1193.95 (Epstein; lowest for t ≤ 4200 by screen only) and t ≈ 6.0e5 (ζ_19; lowest for t ≤ 2e6 by screen only). SP-9: positive-proportion arguments also apply to Epstein (Rezvyakova) and DH (Karatsuba). | F4, F6 | corrected |
| C2-31 | **HEURISTIC** (hitting-set reading); blind-spot sentence **REFUTED** | The theorem is: for every zoo member W, a valid RH proof must use some property in Missing(W) (sect. 4). It does **not** follow that every proof must use the Euler product, because each Missing(W) has several elements. The blind spot is the full Selberg class, not "Euler product + FE + Dirichlet series" (M10). | F1 | THEOREM → HEURISTIC |
| C2-32 | NUMERICAL-NONRIGOROUS | mpmath replay agrees with every Arb certificate (ratios ≤ 3.03e-15). | crosscheck_mpmath.json | — |
| C2-ADJ-1 | **THEOREM** | Family M10 (sect. 3.1): RH-false, with P1, P2, P3, P6, P7 (conductor 4), P9, P10 and P11. It violates only P4 (θ < 1/2, \|α_p\| ≤ 1), P5 (Λ_F ≥ 0) and P8 (conductor 1). | adj_side_checks.json | new (from F1) |
| C2-ADJ-2 | **THEOREM** (+ NN numerics, two codes) | The exact s = 1/2 threshold for Z_k = Σ'(m² + k²n²)^{-s}. BST Conjecture 1.1 is false. A real zero in (1/2,1) exists for every k > k* (sect. 3.2). | adj_side_checks.json, sk_bst_threshold.json | new (from F7) |
| C2-ADJ-3 | **THEOREM** (classical; proof written out) | Log-concavity of Γ(p+1)^{-1}∫_0^∞ v^p g(v)dv on p > -1 for log-concave g > 0 (sect. 3.3). | — | new |
| C2-ADJ-4 | NUMERICAL-NONRIGOROUS | With the boundary term -g_n(T*)S(T*), λ_100000(ξ) = 462580.78242 (Johansson: 462580.78241). Without it, 462581.69. Error budget \|E_n\| ≤ 1.9e-4 at n = 1e5. | adj_li.json | new (A2) |
| C2-ADJ-5 | NUMERICAL-RIGOROUS | Second, independent certificate of the Epstein zeros with Re s > 1 at t ≈ 1193.946 and 4108.108 (Rouché-Cauchy; Hurwitz route). | adj_epstein_rouche.json | new |
| C2-ADJ-6 | **THEOREM** given IMPORTED CCS 1987 (L0+), Platt-Trudgian 2021 Cor. 2, and Pólya-Schur/Jensen | Unconditional uniform large-shift Jensen hyperbolicity for an off-line perturbation of H_{0.2} (sect. 3.4). | — | new (repairs F2) |
| C2-ADJ-7 | methodology finding | The rigor defect in sk_wind.py (A1). It is repaired in adj_dh_count.py. | adj_dh_count_T300.json | new |
| C2-ADJ-8 | HEURISTIC | The first negative Li index of ξ~ satisfies n* ≈ rate^{-1}·log(λ_{n*}(ξ)/2), with rate = (1/2)log((β²+γ0²)/((1-β)²+γ0²)). It is within 0.03-1.1% of the four exact values (predicted 20794 / 7394 / 112357 / 40895 against 20855 / 7477 / 112538 / 40908). The residual is at most one oscillation period (about 2πγ0). | one-liner, sect. 6 | new |

## 3. The most useful precise statements

### 3.1 Theorem C2-ADJ-1 (an RH-false Euler product with a self-dual functional equation)

Let c > 2√2. Write 1 + cu + 2u² = (1 + au)(1 + bu) with a > b > 0, ab = 2, a + b = c, and put

  F_c(s) = ζ(s)(1 + c·2^{-s} + 2·4^{-s}).

Then:

1. F_c(s) = Σ a_n n^{-s}, with a_n = 1 + c·[2|n] + 2·[4|n]. The coefficients are multiplicative, a_1 = 1, and 0 ≤ a_n ≤ 3 + c.
2. F_c has an Euler product over the rational primes. The factor at 2 is (1 + a2^{-s})(1 + b2^{-s})/(1 - 2^{-s}), and the factor at p odd is (1 - p^{-s})^{-1}.
3. (s - 1)F_c(s) is entire of order 1.
4. Λ_c(s) := π^{-s/2}Γ(s/2)ζ(s)(2^s + c + 2^{1-s}) satisfies Λ_c(s) = Λ_c(1-s). This is a degree-1 FE with Γ_R(s) and conductor 4.
5. F_c vanishes at every s with 2^{-s} = -1/a or 2^{-s} = -1/b. These zeros lie on the vertical lines Re s = log₂a > 1/2 and Re s = log₂b = 1 - log₂a < 1/2, at Im s = (2k+1)π/log 2, k ∈ Z.

Proof. (1)-(3) are immediate, since the Dirichlet convolution of multiplicative functions is multiplicative. For (4), 2^s(1 + c2^{-s} + 2·4^{-s}) = 2^s + c + 2^{1-s} is invariant under s ↦ 1 - s, and π^{-s/2}Γ(s/2)ζ(s) is invariant too. For (5): F_c = ζ·D_c with D_c(s) = (1 + a2^{-s})(1 + b2^{-s}), and ζ is finite at every s ≠ 1, so F_c vanishes at every zero of D_c. Moreover, 2^{-s} = -1/a gives Re s = log₂ a, and 2^{-s} = -1/b gives Re s = log₂ b = 1 - log₂ a. Since a = (c + √(c² - 8))/2 > √2 when c > 2√2, both lines are off Re s = 1/2. For 2√2 < c ≤ 3, log₂ a ∈ (1/2, 1] (c = 3 gives a = 2). For c > 3, log₂ a > 1, so F_c even has zeros in the half-plane of absolute convergence, as DH does. ∎

Examples. For c = 3 the zeros lie on Re s ∈ {0, 1}. For c = 2^{3/4} + 2^{1/4} they lie on Re s ∈ {1/4, 3/4}, first at 0.75 + 4.5324 i. For 0 < c ≤ 2√2, the zeros of the local factor lie on Re s = 1/2 (|a| = |b| = √2), so F_c satisfies RH iff ζ does.

Why F_c is not in the Selberg class. The coefficients of log F_c = Σ b(n)n^{-s} at n = 2^k are b(2^k) = 1/k + (-1)^{k+1}(a^k + b^k)/k, and |b(2^k)| ≍ a^k/k = n^{log₂ a}/k. Since log₂ a > 1/2, this violates axiom (v) (b(n) ≪ n^θ, θ < 1/2). The local roots -a, -b violate |α_p| ≤ 1. Also Λ_F(4) = 2 log 2 · (1/2 - (a² + b²)/2) < 0, because a² + b² = c² - 4 > 4; for c = 3, Λ_F(4) = -4 log 2. F_c lies in the extended class S^# as ζ times a degree-0 element (a Dirichlet polynomial). That is consistent with Perelli's remark quoted in sect. 1.

Consequence for the protocol. The implication

  (P1 ∧ P2 ∧ P3 ∧ P6 ∧ P7[degree 1, any conductor] ∧ P9 ∧ P10 ∧ P11) ⇒ RH

is false. A valid proof must use P4, P5, P8, or another property F_c lacks. Examples of the latter: "no Dirichlet-polynomial factor" (primitivity), or "no zeros on vertical progressions".

### 3.2 Theorem C2-ADJ-2 (rectangular Epstein functions at s = 1/2; BST Conjecture 1.1 is false)

Let Z_k(s) = Σ'_{(m,n)≠(0,0)} (m² + k²n²)^{-s} with k ≥ 1. Then

  Z_k(1/2) = 2γ + 2 log(k/(4π)) + 8 Σ_{N≥1} d(N) K_0(2πNk),

where d is the divisor function and K_0 is the Macdonald function.

(a) Z_k(1/2) is strictly increasing in k ≥ 1. It is negative at k = 1 and has a unique zero k*, given by

  k* = 4π e^{-γ} exp(-4 Σ_N d(N) K_0(2πN k*)) = 7.05550795544818276247461...

(b) At k0 = 4πe^{-γ}, Z_{k0}(1/2) = 8 Σ d(N) K_0(2πNk0) > 0. So k0 is not a zero, and k* < k0.

(c) In BST's normalisation, ζ^{(2)}(s, Δ) = (1/2)Σ'_{(j,l)}(j² + Δ²l²)^{-s} = (1/2)Δ^{-2s}Z_{1/Δ}(s), so the unique solution of ζ^{(2)}(1/2, Δ) = 0 in (0,1) is Δ* = 1/k* = (e^γ/(4π))·exp(4 Σ d(N)K_0(2πN/Δ*)) > e^γ/(4π). Numerically, Δ* - e^γ/(4π) = 5.947e-21, a relative gap of 4.196e-20 [NN]. Conjecture 1.1 of arXiv:2110.09368v2 (p. 3) is therefore **false**. Their reported agreement "by at least 22 decimal digits" (p. 22) is inconsistent with the exact formula. The two numbers agree to 19 decimal places and differ in the 20th (the skeptic's "21st" is a miscount).

(d) For every k > k*, Z_k has a real zero in (1/2, 1), and its mirror in (0, 1/2). At k = k*, Z_k has a zero of even order at s = 1/2.

Proof. The value at 1/2 comes from the Chowla-Selberg expansion

  Z_k(s) = 2ζ(2s) + 2√π k^{1-2s} Γ(s-1/2)ζ(2s-1)/Γ(s) + (8π^s k^{1/2-s}/Γ(s)) Σ_N N^{s-1/2} σ_{1-2s}(N) K_{s-1/2}(2πNk).

This follows from Poisson summation in m for each n ≠ 0. Let s → 1/2. The first two terms are 1/ε + 2γ and -1/ε + 2log(k/(4π)) + O(ε), using Γ(ε) = 1/ε - γ, ζ(2ε) = -1/2 - ε log 2π, and 1/Γ(1/2 + ε) = π^{-1/2}(1 + ε(γ + 2 log 2)). The Bessel term at s = 1/2 is 8Σ d(N)K_0(2πNk).

For (a), differentiate: d/dk[2 log k + 8Σ d(N)K_0(2πNk)] = (1/k)[2 - 8Σ d(N)·(2πNk)K_1(2πNk)]. Since x ↦ xK_1(x) is decreasing ((xK_1)' = -xK_0 < 0), for k ≥ 1 the bracket is at least 2 - 8Σ d(N)(2πN)K_1(2πN) = 2 - 0.04987... > 0. Also Z_1(1/2) = 4ζ(1/2)β(1/2) < 0.

(b) holds because K_0 > 0.

For (d): if k > k*, then Z_k(1/2) > 0, while Z_k(s) → -∞ as s → 1⁻ (simple pole with residue π/k > 0). The intermediate value theorem then gives a zero in (1/2, 1), and the FE Λ(s) = Λ(1-s) gives its mirror. At k = k*, Λ'(1/2) = 0 by symmetry, so the zero at 1/2 has even order. ∎

Checks. In adj_side_checks.json the theta integral and Chowla-Selberg agree to 30 digits at k = 3 (-1.71039257185643644598544199029). At k0 both give 8.39166873936e-20. The skeptic's sk_bst_threshold.json agrees.

Prior art. The arXiv API (two queries), WebSearch, BST's 2023 follow-up (arXiv:2307.06002, no mention of Conjecture 1.1) and McPhedran arXiv:1601.01724 were checked, and no published refutation was found. Bateman-Grosswald 1964 (Zbl 0128.27004) was not accessible; it may already contain the exact threshold equation. So the formula is not claimed new. The refutation of the 2022 conjecture is, as far as this search goes, not in the literature. Methodology sect. 6: this has an independent witness (a complete proof). It is recorded as an Observatory finding of type `verified_error`, applied to a conjecture.

### 3.3 Theorem C2-ADJ-3 (moment lemma) and C2-14 (Turán for every H_t)

**Lemma.** Let g: (0,∞) → (0,∞) be log-concave with ∫_0^∞ v^q g(v) dv < ∞ for every q > -1, and put λ(q) = Γ(q+1)^{-1}∫_0^∞ v^q g(v) dv. Then for every p and every h > 0 with p - h > -1,

  λ(p)² ≥ λ(p-h)λ(p+h),

with equality iff g(v) = Ae^{-cv}.

Proof (the classical sign-change argument, written out here).

- Choose c > 0 and A > 0 so that e(v) = Ae^{-cv} has the same (p ± h)-moments as g. Such c exists and is unique, because M_e(p+h)/M_e(p-h) = (Γ(p+h+1)/Γ(p-h+1))c^{-2h} decreases bijectively in c. Set D = g - e.
- log g - log e is concave, so {D > 0} is an interval (v1, v2) and D ≤ 0 off it. If D ≡ 0 we are done, so assume not.
- If v1 = 0 and v2 = ∞, then D > 0 a.e., which contradicts ∫v^{p-h}D = 0. If v1 = 0 < v2 < ∞, then ∫v^{p-h}(v^{2h} - v2^{2h})D < 0, because the integrand is negative on (0, v2) and ≤ 0 beyond. But this integral equals ∫v^{p+h}D - v2^{2h}∫v^{p-h}D = 0, a contradiction. The case v2 = ∞ fails the same way, so 0 < v1 < v2 < ∞.
- With w = v^h and w_i = v_i^h, put u(v) = -v^{p-h}(w - w1)(w - w2) = -v^{p+h} + (w1 + w2)v^p - w1w2 v^{p-h}. Then uD ≥ 0, and uD > 0 on a set of positive measure. So 0 < ∫uD = (w1 + w2)∫v^p D, i.e. M_g(p) > M_e(p).
- Hence λ_g(p) > λ_e(p) = Ac^{-p-1} = (λ_e(p-h)λ_e(p+h))^{1/2} = (λ_g(p-h)λ_g(p+h))^{1/2}. ∎

The result is classical (Karlin-Proschan-Barlow 1961; Borell 1973), but those sources were not opened, so they serve only as attributions.

**C2-14.** Fix t ∈ R and put g_t(v) = e^{tv}Φ(√v). The strict concavity of log Φ(√v) on (0,∞) is Csordas-Varga 1988 (IMPORTED, L0+). Since e^{tv} adds a linear term, g_t is strictly log-concave, and the super-exponential decay of Φ makes every moment finite. b_m(t) = (1/2)∫_0^∞ v^{m-1/2}g_t(v)dv. Apply the Lemma with p = m - 1/2 and h = 1 (so p - h = m - 3/2 ≥ -1/2 > -1); the inequality is strict because g_t is not exponential. Since Γ(m+1/2)²/(Γ(m-1/2)Γ(m+3/2)) = (2m-1)/(2m+1),

  b_m(t)² > ((2m-1)/(2m+1)) b_{m-1}(t) b_{m+1}(t) for all m ≥ 1 and all t ∈ R. ∎

Consequence (SP-6): every Turán inequality holds for H_t with t < 0, yet each such H_t has non-real zeros (Rodgers-Tao). No argument built only from moment Turán inequalities, or from log-concavity of the kernel in √v, can force real zeros. Prior art: CNV 1986 proved the case t = 0. The statement for t < 0 is a two-line corollary and is probably known, but it was not located.

### 3.4 Theorem C2-ADJ-6 (unconditional uniform large-shift Jensen hyperbolicity for an RH-false-type function)

Let E(X) = Σ_m b_m(0.2) X^m/(2m)!, so that H_{0.2}(z) = E(-z²). Let X0 ∈ C \ R and Ẽ(X) = E(X)(X - X0)(X - X̄0) = Σ_k γ_k X^k/k!. Then:

- there is n0 such that for every n ≥ n0 and every d ≥ 1, the Jensen polynomial J^{d,n}(X) = Σ_{j≤d} C(d,j) γ_{n+j} X^j is hyperbolic;
- some J^{d,0} is not hyperbolic.

Proof.

- H_{0.2} has only real zeros, because Λ ≤ 0.2 (Platt-Trudgian 2021, Cor. 2) and H_t is real-rooted for t ≥ Λ. Hence E is real entire of order 1/2 with only real (negative) zeros, and Ẽ has exactly two non-real zeros.
- By Craven-Csordas-Smith 1987 (real entire, order < 2, finitely many non-real zeros), Ẽ^{(n)} has only real zeros for n ≥ n0. Being of order 1/2, Ẽ^{(n)} is then in the Laguerre-Pólya class.
- By Jensen/Pólya-Schur, every J^{d,0} of Ẽ^{(n)} is hyperbolic, and J^{d,0}(Ẽ^{(n)}) = J^{d,n}(Ẽ).
- Ẽ ∉ LP because it has non-real zeros. If every J^{d,0}(X/d) were hyperbolic, their locally uniform limit Ẽ would be in LP (Hurwitz). ∎

This repairs C2-17 and C2-28. The GORZ-type property "for each d, J^{d,n} is hyperbolic for n ≥ N(d)" holds, even uniformly in d, for a function of ξ-type with an off-line zero quadruple. As GORZ themselves note, large-shift hyperbolicity is evidence, not a proof route.

### 3.5 Corrected meta-lemma and hitting set (C2-24, C2-31)

For a member W, let Missing(W) be the set of predicates (from section 4) that zeta satisfies and W violates. If W is RH-false, then every valid argument for RH_ζ must use at least one predicate in Missing(W) in its RH-deciding step (THEOREM, elementary). So the set U of predicates a valid proof uses must meet every Missing(W).

The zoo's Missing sets are not singletons: Missing(DH) = {P2, P3, P4, P5, P6, P8, P10} and Missing(M10) = {P4, P5, P8}. So nothing forces a particular single predicate. The sharpest consequence is this: U must meet {P4, P5, P8} (from M10), and U cannot consist only of predicates that some RH-false member satisfies jointly. Steps that use P4 (the Selberg θ < 1/2 local condition), or P5 (Λ_F ≥ 0) with P1 and P7, are not excluded by any zoo member. That is the blind spot.

### 3.6 Right edges and completeness (C2-04, C2-05, C2-09, C2-11)

- DH (computer-assisted THEOREM): f(s) ≠ 0 for Re s ≥ 1.13514.
- Epstein x² + 5y² (computer-assisted THEOREM): Z_Q(s) ≠ 0 for Re s ≥ 1.17816.
- NUMERICAL-RIGOROUS: every off-line zero of f with |t| ≤ 300 is one of the 5 certified zeros or their reflections, and every off-line zero of Z_Q with |t| ≤ 200 is one of the 35 certified zeros or their reflections. All other zeros in those ranges are simple and on the critical line.

### 3.7 Detection statements (Li coefficients, ξ~)

- THEOREM (identity): λ_n(ξ~) - λ_n(ξ) = 4 - 2Re[(1-1/ρ0)^n] - 2Re[(ρ0/(ρ0-1))^n].
- The last term has modulus e^{n·rate}, rate = (1/2)log((β² + γ0²)/((1-β)² + γ0²)) ≈ δ/γ0² (δ = β - 1/2). So the injected quadruple is invisible to λ_n until n ≈ rate^{-1}log(λ_n(ξ)/2) ≈ (γ0²/δ)·log(λ_n(ξ)/2). This is HEURISTIC, and checked against the 4 exact thresholds (C2-ADJ-8).
- For an off-line zero like DH's first (β = 0.8085, γ0 = 85.7), the predicted threshold is n ≈ 3.2e5, beyond the computed range.

## 4. Adjudicated stress-test protocol

Predicates, with zeta's normalisation:

- P1: ordinary Dirichlet series Σ a_n n^{-s} over N, a_1 = 1, absolutely convergent in σ > 1.
- P2: multiplicative a_n.
- P3: Euler product over the rational primes.
- P4: Selberg local condition (log F = Σ b(n)n^{-s} with b supported on prime powers and b(n) ≪ n^θ, θ < 1/2; equivalently here |α_p| ≤ 1 for polynomial local factors).
- P5: Λ_F(n) ≥ 0.
- P6: a_n ≥ 0.
- P7: self-dual FE s ↔ 1-s with Γ_R/Γ_C factors.
- P8: degree 1 and conductor 1 (with P1 and P7 this forces cζ: Hamburger).
- P9: (s-1)F entire of order 1.
- P10: simple pole at s = 1.
- P11: Ramanujan bound a_n ≪ n^ε.

Each implication below is FALSE. The witness is named, and the status is that of the witness.

| id | implication shown false | witness (status) |
|---|---|---|
| SP-1a | P1 ∧ P7 ∧ P9 ∧ P11 ∧ (Bohr a.p.) ∧ (≫T(log T)^{1/2-ε} zeros on the line) ⇒ RH | DH (NR zeros; IMPORTED Karatsuba) |
| SP-1b | P1 ∧ P6 ∧ P7[degree 2] ∧ P9 ∧ P10 ∧ P11 ∧ (positive proportion on the line) ⇒ RH | Z_{x²+5y²}/2 (NR; IMPORTED Rezvyakova) |
| SP-1c | P1 ∧ P2 ∧ P3 ∧ P6 ∧ P7[degree 1, conductor 4] ∧ P9 ∧ P10 ∧ P11 ⇒ RH | **M10** (THEOREM, C2-ADJ-1) |
| SP-2 | P3[Beurling] ∧ P5 ∧ P6 ∧ explicit formula ∧ N(x) = Ax + O(x^θ), θ ∈ [1/2, 1) ⇒ RH | DMV, Zhang, BDR (IMPORTED); C2-21 (THEOREM; continuous) |
| SP-3 | Euler product over norms > 1 ∧ FE ∧ nontrivial zeros = spectrum (via s(1-s) or q^s + q^{1-s}) ⇒ RH | Selberg zeta with λ_1 < 1/4; Ihara zeta, non-Ramanujan (IMPORTED) |
| SP-4 | order 1 ∧ real ∧ FE ∧ Hadamard ∧ N(T) = N_ζ(T) + O(1) ∧ Turán (k ≤ 78) ∧ λ_n > 0 for n ≤ 20854 ⇒ RH | ξ~ (THEOREM structure; NR/NN ranges) |
| SP-5 | (for each d: J^{d,n} hyperbolic for n ≥ N(d), even uniformly in d) ⇒ all zeros real | H_{0.2}·(X - X0)(X - X̄0) (THEOREM C2-ADJ-6) |
| SP-6 | K > 0 even, super-exponential decay, K(√v) log-concave, all moment Turán inequalities ⇒ real-rooted cosine transform | e^{tu²}Φ, t < 0 (THEOREM: C2-14 + IMPORTED Rodgers-Tao) |
| SP-7 | "ζ_N zero-free in σ > 1 for large N" (Turán's route) | ζ_19 (NR); Montgomery 1983 (IMPORTED) |
| SP-8 | any finite zero census ⇒ RH | Epstein (first off-line zero 15.67, rigorously lowest); DH (85.70, rigorously lowest) |

Practical rule (HEURISTIC). For a proposed step, write down every property of ζ it uses as predicates. If the zoo contains a member with all of them, that step cannot be the RH-deciding step. In particular:

- "uses the Euler product" is not enough (SP-1c);
- the step must also use P4, P5 or P8, or something outside this list that M10 lacks.

## 5. Negative results and negative knowledge

- **Refuted claims.**
  - Liu-Wu's "only on the critical line" claim for the DH function (C2-07).
  - The C2-00(i)/C2-31 blind-spot sentence (M10).
  - BST Conjecture 1.1 (C2-ADJ-2).
- **Withdrawn numbers.**
  - Investigator Li thresholds 20857, 7395, 112929 and 41098. The cause was linear interpolation of λ_n(ξ) on a 60-point grid plus a stride of n//2000. At n = 7395 the interpolation error flipped the sign: the true value is +1.87, against an interpolated -2.17.
  - Scales 980/393/... (halved).
  - "Epstein σ > 1 zeros first near 3.6e6".
- **Tail-model pitfall (A2).** Starting a smooth zero-density tail at the last computed zero without the boundary term g(T*)S(T*) produces errors of order g(T*)·|S(T*)|. That is about 0.9 at n = 1e5 and T* ≈ 74921. The term is harmless for small n/T* but not near n ≈ T*. Use S(T*) = N(T*) - ϑ(T*)/π - 1 exactly.
- **Argument-principle pitfall (A1).** Generating boundary points in floating point as a + (b-a)j/n can fail to close the contour at a corner. Generate the corners exactly, and build the segment balls as exact hulls of their endpoints. A winding enclosure that excludes every integer is the warning sign.
- **Precision pitfalls (investigator, confirmed).**
  - Rounding Jensen polynomials to 60 digits fabricated non-real roots at d = 100.
  - acb_series' default length silently truncated series.
  - Importing a module reset flint.ctx.prec.
  - complex128 evaluation of ζ_19 at t ≈ 6e5 has a residual floor of about 1e-10 (skeptic).
- **Malformed CSV.** Two rows of the investigator's property_matrix.csv (M5c, M7) contain unquoted commas, which shift their columns. The original is kept unchanged. A repaired copy is property_matrix_adjudicated.csv.
- **Unreproduced items** (excluded from claims):
  - the investigator's interactive certificates of Epstein zeros with Re slightly below 1 (t ≈ 1.65e6, 2.54e6, 2.68e6), whose output was not archived;
  - the skeptic's screens sk_ep_probe/newton/screen/low and sk_dh_sigma1, which printed results only.
- **Conditional, not theorem.** Applying CCS to ξ~ silently assumes zeta has finitely many off-line zeros (F2).

## 6. Reproducibility

All commands are run from `/home/user/riemann/research/exploratory/riemann-observatory/experiments`. `ZD=/tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/data` holds the zero files; regenerate them with `experiments/code/zeros_arb.py` if that directory has been cleared.

Adjudicator (outputs in results/C2-countermodel-zoo/adjudicator/, verify with `sha256sum -c SHA256SUMS` there):

```text
python3 code/C2-countermodel-zoo/adjudicator/adj_li.py results/C2-countermodel-zoo/adjudicator $ZD/zeros_1_50000.tsv $ZD/zeros_50001_100000.tsv   # 31 s
python3 code/C2-countermodel-zoo/adjudicator/adj_epstein_rouche.py results/C2-countermodel-zoo/adjudicator     # 3 s
python3 code/C2-countermodel-zoo/adjudicator/adj_side_checks.py results/C2-countermodel-zoo/adjudicator        # 3 s
python3 code/C2-countermodel-zoo/adjudicator/adj_dh_count.py results/C2-countermodel-zoo/adjudicator 300      # 51 s
python3 code/C2-countermodel-zoo/adjudicator/adj_property_matrix.py results/C2-countermodel-zoo               # <1 s
```

sha256 of the adjudicator outputs:

| file | sha256 |
|---|---|
| adj_li.json | b3132cc5df1e38a95d223fe5564bd6a3b74a3482b755519d399baf60c5abc7fb |
| adj_epstein_rouche.json | 0f88a7d3f54b6c8eb2629bd79bdc2f98cd6c7b52f06192641df92bb3637b9fd9 |
| adj_side_checks.json | 8ced43c02f4b8cd4a7a0a79beb0721fad940095d5960740b4444b69611f1d750 |
| adj_dh_count_T300.json | 9e8efa58f1b08b9ba2c37095bb6354d46b1e20589218bcdf314d2106e6371c01 |
| property_matrix_adjudicated.csv | 56dd744b7d07395f00bd9a74bc0db9dc46966b161b352903930bbdeb3d9a943f |

Heuristic C2-ADJ-8 (one-liner):

```text
python3 -c "import math;g=0.5772156649015329
for b,T in [(0.6,14),(0.75,14),(0.6,30),(0.75,30)]:
  r=0.5*math.log((b*b+T*T)/((1-b)**2+T*T));n=10/r
  for _ in range(50): n=math.log(0.25*n*(math.log(n)-1-math.log(2*math.pi)+g))/r
  print(b,T,round(n))"
```

Investigator (main certificates; results/C2-countermodel-zoo/, `sha256sum -c SHA256SUMS`):

```text
python3 code/C2-countermodel-zoo/dh_zeros.py OUT 300 1.14          # 120 s
python3 code/C2-countermodel-zoo/dh_right_edge.py OUT 100000000     # 33 s
python3 code/C2-countermodel-zoo/epstein_zeros.py OUT 200           # 240 s
python3 code/C2-countermodel-zoo/epstein_sigma_gt1.py OUT           # ~520 s
python3 code/C2-countermodel-zoo/partial_sums.py OUT 19 2e6         # 41 s
python3 code/C2-countermodel-zoo/dbn_Ht.py OUT                      # 394 s
python3 code/C2-countermodel-zoo/synthetic_xi.py OUT $ZD/zeros_1_50000.tsv $ZD/zeros_50001_100000.tsv
python3 code/C2-countermodel-zoo/jensen_degree_scan.py OUT          # 833 s
python3 code/C2-countermodel-zoo/beurling_toy.py OUT
python3 code/C2-countermodel-zoo/crosscheck_mpmath.py results/C2-countermodel-zoo
```

Skeptic (results/C2-countermodel-zoo/skeptic/):

```text
python3 code/C2-countermodel-zoo/skeptic/sk_dh_count.py OUT 300      # 104 s (see A1)
python3 code/C2-countermodel-zoo/skeptic/sk_ep_count.py OUT 200      # 99 s
python3 code/C2-countermodel-zoo/skeptic/sk_edges.py OUT 100000000   # 13 s
python3 code/C2-countermodel-zoo/skeptic/sk_ep_cert.py OUT 1.0110493 1193.9464 ...   # 0.7-858 s per zero
python3 code/C2-countermodel-zoo/skeptic/sk_li.py OUT $ZD/zeros_1_50000.tsv $ZD/zeros_50001_100000.tsv
python3 code/C2-countermodel-zoo/skeptic/sk_bst_threshold.py OUT
```

## 7. Next precise steps

1. **Rigorous Jensen thresholds for ξ~.** Certify, with Arb root isolation on the exact ball coefficients (not rounded integers), the smallest d with J^{d,0}(ξ~) non-hyperbolic. The NN value is d = 40 for (0.9, 5). Then map d*(β, γ0) and test the conjectured dependence on Im X0/|X0|. The C1 campaign's certified Jensen pipeline (adj_farmer_x10.py) can be reused.
2. **Lowest Epstein zero with σ > 1.** Prove there is none with 1 < σ ≤ 1.17816 and 0 < t < 1193.9 by a rigorous argument-principle count on [1, 1.18] × [0, 1194] (the Taylor-form winding of sk_wind.py with exact corners). Repeat for ζ_19 on t < 6.0e5.
3. **Rigorous Li thresholds.** Turn adj_li.py into an interval computation: Arb zero ordinates (already certified), Arb tail integral, and an explicit bound on E_n via Trudgian's S_1 bound. This would make "λ_n(ξ~) > 0 for n ≤ 20854, < 0 at 20855" NUMERICAL-RIGOROUS, given RH up to height 3e12 (Platt-Trudgian).
4. **Prior-art closure for C2-ADJ-2.** Obtain Bateman-Grosswald 1964 (Acta Arith. 9, 365-373) and check whether it contains the exact equation of section 3.2 and the threshold k* ≈ 7.0555. If not, consider a short note correcting BST Conjecture 1.1, after an independent agent replays the proof and numbers (methodology sect. 6(iv)).
5. **A protocol member between M10 and the Selberg class.** Is there an RH-false F with P1, P3, P5 (Λ_F ≥ 0) and P7 that is not in S? Λ_F ≥ 0 rules out polynomial local factors with zeros of the M10 type, and placing them in the denominator creates poles instead of zeros. A precise version: classify S^#_1 elements with an Euler product and Λ_F ≥ 0 (Kaczorowski-Perelli structure theorem for S^#_1). Either an RH-false example exists or the class reduces to Dirichlet L-functions. Either answer sharpens SP-1c.
6. **Restricted Weil positivity for ξ~.** Certify, for the Yoshida/Bombieri support range, whether the Weil functional stays positive for an injected quadruple at height γ0 (open question in REPORT).
7. **DH zero with σ > 1.** Use Kronecker/LLL targeting on the phases t log p for p ≡ 2, 3 mod 5, p ≤ 157, to locate and certify a DH zero with σ > 1. Compare its height with the heuristic in C2-06.
8. **Independent replay before external citation.** Both external refutations already meet methodology sect. 6(i). C2-07 (Liu-Wu) has certificates by two agents using different methods. C2-ADJ-2 (BST) has a complete proof re-derived by the adjudicator, independently of the skeptic who raised it, plus two independent codes. Before anything is cited outside the Observatory, a further agent should still do an L2 check of the Chowla-Selberg constant term (sect. 3.2) and of the Liu-Wu failing step against the full text.
