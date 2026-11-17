# C5-function-field-transfer: FINAL (adjudicated)

This is the adjudicator's report. `REPORT.md` (investigator) and `SKEPTIC_REVIEW.md` (skeptic) are kept unchanged as the record. Where this file disagrees with either of them, this file gives the final status and the reason.

```text
Status:
  ADJUDICATED EXPLORATORY DOSSIER. RH is open. Nothing here proves or disproves RH, or claims to.
  It contains:
  - THEOREM, with complete proofs here or in REPORT.md (each re-derived by the skeptic and the adjudicator):
    C5-L0, C5-L1, C5-T1 (modulo IMPORTED intersection theory and Rosati positivity), C5-T2,
    C5-T3 (confluent form), C5-L2, C5-S1, C5-D1, C5-SK-ASYM;
  - adjudicator theorems, proved in Sec. 3:
    C5-ADJ-W (sharp window theorem over F_q, no RH and no squarefreeness assumed),
    C5-ADJ-LOG ("no finite window suffices over Q" is false as stated),
    C5-ADJ-MODEL (window positivity plus counting asymptotics cannot force RH);
  - computer-assisted exact results:
    C5-E1 (fake curve zeta functions exist; census corrected), C5-E2, C5-E3, C5-E4 instances,
    C5-ADJ-SHARP (the window threshold is attained in the formal class);
  - IMPORTED literature statements, with locations and evidence level;
  - HEURISTIC synthesis (ingredient table, obstruction readings, assessment);
  - open targets, labelled CONJECTURE (open target).
  REFUTED as literally stated:
  - the sentence "over Q no finite Weil window can suffice" (in C5-T3, OB2(c), ML-E1, A);
  - the decay law "lambda_min(L) ~ exp(-L e^L)" in OB9.
  Evidence level of this adjudication:
  - L2 for items re-derived here: Suzuki 2610.41115 Sec. 4; Connes-Consani 1910.14368 Conj. 4.1 and eq. (4.1);
    Pritsker 1307.5361 Sec. 1; Deligne Weil I pp. 284-286;
  - L1-partial for Bombieri, Sem. Bourbaki 430 (formulas partly lost in the Numdam OCR);
  - L0+ (abstract or review only) for Zhu 2608.24827, Andrews-Connes-La Gatta 2611.13129,
    Niedbala Giraudin 2610.00386, and Zhang 1990 (Zbl 0723.11047).

Scope:
  Function-field side: the four proofs of RH for curves over F_q.
  - Weil: C x C with Castelnuovo-Severi / Hodge index, plus the Jacobian/Rosati variant.
  - Stepanov-Bombieri.
  - Deligne, Weil I/II.
  - Weil explicit-formula positivity.
  Number-field side, mapped against these: Deninger; Connes 1999 and CCM 2009; Connes-Consani (arithmetic site,
  scaling site, Riemann-Roch for Spec Z, 2026 Jacobian); Haran; Manin; Borger; Hesselholt/TP; Scholze;
  Bombieri 2000; Suzuki 2026.
  Normalisation (used throughout):
  - Z(T) = P(T)/((1-T)(1-qT)), P(T) = prod_{i<=2g}(1 - alpha_i T) in Z[T], h = log q;
  - FE: P(T) = q^g T^{2g} P(1/(qT));
  - beta_i = alpha_i/sqrt q;  s_k = sum alpha_i^k;  t_k = q^{-k/2} s_k;  T_N = (t_{m-n})_{0<=m,n<N};
  - d = number of distinct beta_i;  m = number of distinct beta_i with |beta_i| > 1.
  "Formal class" = P in Z[T] with P(0) = 1, deg 2g, the FE, and place counts
  B_d = (1/d) sum_{e|d} mu(d/e)(q^e+1-s_e) >= 0 for all d.

Exact sources or dependencies:
  Per claim, in Sec. 2 and the ingredient table (Sec. 4).
  Primary texts opened by the adjudicator:
  - Suzuki arXiv:2610.41115v1: Sec. 1 (def. (1.4), a* = dh/2), Sec. 2.2, Sec. 4
    (fibre decomposition (4.1), Thm 4.1, Props 4.2-4.3, Cor 4.4);
  - Connes-Consani arXiv:1910.14368v1: Sec. 4, eq. (4.1) and Conjecture 4.1;
  - Pritsker arXiv:1307.5361: Sec. 1 (Gorshkov; bracket 0.4213 < t_Z < 0.4232; remark after Prop 1.3);
  - Deligne, La conjecture de Weil I, Publ. IHES 43 (Numdam PMIHES_1974__43__273_0): Cor (3.8), (3.9), both p. 286;
  - Bombieri, Counting points on curves over finite fields, Sem. Bourbaki 430 (Numdam SB_1972-1973__15__234_0):
    Sect. II Thm 1 (q = p^a, a even, q > (g+1)^4); Sect. III, which opens with the omega_1 = q, omega_2 = 1 remark.
  Abstracts and reviews (arXiv API, zbMATH API, fetched 2026-11-17):
  - Zhu 2608.24827v2; Andrews-Connes-La Gatta 2611.13129v1; Niedbala Giraudin 2610.00386v3;
  - Zbl 0723.11047 (W.-B. Zhang 1990; review by Knopfmacher).
  Prior-art searches: 6 arXiv API queries (Selberg class / function field / arithmetical semigroup /
  Euler product counterexample). None returned a function-field Selberg-class counterexample.
  Certified zeros: zeros_1_50000.tsv (sha256 6a7eb7ab...cc88) and zeros_50001_100000.tsv (494b5c10...5e5a).

What was actually run:
  Investigator (REPORT.md): 5 scripts, ff_*.py, total about 1,060 s.
  Skeptic (SKEPTIC_REVIEW.md): 4 independent re-implementations, skeptic_*.py.
  Adjudicator: all 5 + 10 recorded hashes re-verified (sha256sum -c: all OK). Then 4 new scripts under
  experiments/code/C5-function-field-transfer/adjudicator/, none importing investigator or skeptic code:
  (i)   adj_exact_checks.py, 10.9 s, exact integers / Arb balls / exact real-root counting:
        - the 41 g>=2 "undecided" census cases;
        - the g=1 boundary;
        - worked examples (a), (b), (c), including an all-d positivity certificate;
        - the confluent inertia theorem on 195 synthetic FE polynomials (101 non-squarefree, 162 RH-false);
        - the exact first indefinite Toeplitz size for all 522 fakes listed in fake_census.json;
  (ii)  adj_window_fibre.py, 46.8 s, IEEE double, NUMERICAL-NONRIGOROUS:
        - the fibre identity behind C5-ADJ-W, without RH, on 4 zeta functions (3 fakes, 1 curve);
        - the explicit negative test function for the hidden fake q=3, g=3;
  (iii) adj_ob_numbers.py, 1.5 s: OB2(a) sum over 10^5 zeros, and OB9 rate bookkeeping;
  (iv)  adj_model_window.py, 3.2 s, IEEE double: illustration of C5-ADJ-MODEL.
  Hashes: results/C5-function-field-transfer/adjudicator/SHA256SUMS.

Smallest remaining gap:
  (Conceptual; ML-W0.) No number-field object carries a pairing whose positivity has a reason independent of RH.
  The smallest precise statement that would count as progress is ML-W0(c):
    on the square of the scaling site, define Dim H^0 satisfying (a), (a') and (b) of Sec. 5, such that
      Dim H^0(D(f)) + Dim H^0(-D(f)) >= s(f,f)
    for every real f in C_c^inf([2^{-1/2}, 2^{1/2}]) with int f d*u = int f du = 0.
  This would re-derive by a Riemann-Roch mechanism a positivity already known (Yoshida; Connes-Consani 2021).
  (Window route; EFR.) C5-ADJ-MODEL shows that zero-side window positivity plus counting asymptotics cannot
  yield RH. So any effective finite reduction must use prime-side (Euler product) structure.
```

---

## 1. How the disagreements were resolved

| # | Point | Resolution | Basis |
|---|---|---|---|
| 1 | C5-T3 needs P squarefree (investigator). | **Skeptic upheld.** For N >= d: inertia(T_N) = (d-m, m, N-d), with d = #distinct roots. So RH <=> T_{2g} >= 0 holds with no squarefree hypothesis. The investigator's "false without squarefreeness" applies only to the count n_0 = N-2g. | Proof re-derived (Sec. 3.2). Exact checks: skeptic 9,900 + 249 + 93; adjudicator 195 synthetic polynomials (101 non-squarefree, 15 of them RH-true), 0 failures. |
| 2 | Window corollary of C5-T3: PROPOSITION-PROOF-SKETCH (investigator) vs. proof sketch without RH (skeptic 3.2). | **Promoted to THEOREM (C5-ADJ-W) and sharpened.** Positivity on C_c^inf(-a,a) <=> T_{ceil(2a/h)} >= 0. Hence RH <=> positivity for one (every) a > (d-1)h/2, in particular a > (g-1/2) log q. The report's window [-g log q, g log q] is correct only if it bounds the support of the factor u (Suzuki's convention), not of the autocorrelation u*u~. It is not sharp. | Complete proof in Sec. 3.3. Suzuki 2610.41115 Sec. 4 read; its fibre identity is RH-free. Numerical identity check: relative error < 4e-15 on 12 tests. |
| 3 | "Over Q no finite window can suffice" (C5-T3, OB2(c), ML-E1, A). The skeptic says it is not a theorem unless RH is false. | **Skeptic upheld and sharpened: the literal sentence is false.** In classical logic there is an L0 with Pos(L) => RH for all L >= L0 (C5-ADJ-LOG). The meaningful content is (i) no explicit L0 is known, and (ii) a precise model statement, now a THEOREM (C5-ADJ-MODEL): zero-side window positivity and counting asymptotics never force RH. | Sec. 3.5. |
| 4 | E1: the 41 g>=2 "undecided" candidates (A/q > 0.9997). | **Skeptic upheld.** All 41 are non-admissible: the first negative B_d is at d = 4 (17 cases), 5 (11), 6 (7), 7 (6). The code returns `undecided_cap` before computing any B_d (`ff_common.py` lines 175-178). Their exclusion was correct, but the description in REPORT.md is wrong. | adj_exact_checks.json, part (1). |
| 5 | E1: the g=1 boundary a = +-(q+1). | **Skeptic upheld.** a = q+1 gives P = (1-T)(1-qT), Z == 1, all B_d = 0. It is admissible and RH fails. a = -(q+1) gives B_2 = -(q+1) < 0. The census JSON flagged only a = q+1; the text "a = +-(q+1)" misdescribes it. | adj_exact_checks.json, part (2): all 14 q. |
| 6 | OB9 decay law exp(-L e^L). | **Skeptic upheld: REFUTED as a decay law.** In Zhu's abstract, exp(-L e^L) is an RH-conditional *upper* bound. The data give -ln lambda_min ~ c e^{2L}: c = 11.91 at L = 2 (Zhu, 3.2e-283) and c = 12.42 at lambda^2 = 300 (ACLG, 1e-1618). The Fuchs rate is 4 pi = 12.57. Certification therefore needs about (c/ln 10) e^{2L}, i.e. about 5.2-5.5 e^{2L} digits, not L e^L. | adj_ob_numbers.json. Abstracts re-read. |
| 7 | OB6: "auxiliary integer polynomials cannot even give the PNT". | **Skeptic upheld.** Pritsker (after Prop 1.3) explicitly leaves sequences of weights w_n with B(w_n) -> 1 open. Current bracket: 0.4222286000 <= t_Z([0,1]) <= 0.4226846976 (Niedbala Giraudin 2026, abstract, unrefereed). Still > 1/e. | Pritsker text, lines 201-207; arXiv abstract. |
| 8 | ML-C1: which function lives in the window (q^{-1/2}, q^{1/2}). | **Skeptic upheld.** CC Conj. 4.1 is stated after eq. (4.1), which constrains h_1, with h = h_1 * h_2 supported in (1/q, q). Only this reading makes S = {inf} u {p < q} the set of primes that enter. For q = 3 the window is Pos((log 3)/2) = Pos(0.549). | 1910.14368 Sec. 4, read. |
| 9 | C5-A: "certification is a standard interval-arithmetic task". | **Skeptic upheld.** That describes certifying a numerical inequality on a window. ML-C1 asks the semilocal framework to *prove* it. These are different tasks. | Logic. |
| 10 | C5-I-D: page of Weil I Cor (3.8)/(3.9). | **Skeptic upheld.** Both are on p. 286. | Numdam OCR, page markers. |
| 11 | C5-I-S: Bombieri 430 not checked (skeptic). | **Partly checked by the adjudicator.** Sect. II Thm 1 hypothesis "q = p^a, a even, q > (g+1)^4" is verified. Sect. III opens with: "if omega_1 = q, omega_2 = 1 then (2) is verified, nu_r is always 0 but (3) is false". The lower-bound argument uses the Galois closure C' -> P^1. The displayed bound (2g+1) sqrt q and the key lemma are lost in the OCR; they stay as in PAPER-0131. | Numdam scan (cached text). |
| 12 | OB2(a): sum 1/\|rho\| ~ (log T)^2/(2 pi). | **Both upheld, refined.** Exactly, sum_{\|gamma\|<T} 1/\|rho\| = (1/2 pi) log^2(T/2 pi) + C + o(1). At T = 74,920.8 the sum is 13.9875, against 14.0220 for the refined term and 20.05 for (log T)^2/(2 pi). Treating this sum as "def(Delta)" is a HEURISTIC convention. | adj_ob_numbers.json; partial summation of Riemann-von Mangoldt. |
| 13 | Prior art for E1 and OB5. | **Skeptic upheld.** Additive arithmetical semigroups satisfying Axiom A# do not in general satisfy a Riemann-type hypothesis (Zhang 1990; the zbMATH review text says he "discusses the general non-validity of a Riemann-type hypothesis"). The curve-shaped census (FE, deg 2g) is the only part possibly new. Ihara zetas of non-Ramanujan graphs (Terras) stay at L0+ via the skeptic. | zbMATH API, Zbl 0723.11047. |

No investigator theorem is refuted in its mathematical content. Two interpretive sentences are REFUTED as literally stated (rows 3 and 6) and replaced by correct statements.

---

## 2. Adjudicated claims table

| ID | Short statement | Investigator | Skeptic | FINAL status |
|---|---|---|---|---|
| C5-00 | Header | header | upheld w/ corrections | Superseded by this header (descriptive; census, window and OB9 corrections applied) |
| C5-L0 | P satisfies the FE <=> P(T) = T^g h(1/T+qT), h monic in Z[x]; RH <=> all x_i real, x_i^2 <= 4q | THEOREM | upheld | **THEOREM** |
| C5-L1 | B_d >= 0 for all d => max\|alpha\| <= q; census bounds | THEOREM | upheld | **THEOREM** ("positive lower density" replaced by "infinitely many d", which suffices) |
| C5-T1 | Gram identity xi_m.xi_n = -q^{min} s_{\|m-n\|}; Hodge index and Rosati give the same PSD matrix | THEOREM mod IMPORTED | upheld | **THEOREM** (modulo IMPORTED projection formula, Delta^2 = 2-2g, transversality, Rosati positivity) |
| C5-T2 | RH <=> T_N >= 0 for all N <=> \|t_k\| <= 2g for all k | THEOREM | upheld | **THEOREM** |
| C5-T3 | Inertia of T_N; RH <=> T_{2g} >= 0; window corollary; "no finite window over Q" | THEOREM + sketch | upheld w/ corrections | **THEOREM** (inertia, confluent form, Sec. 3.2). Window corollary: **THEOREM** (C5-ADJ-W). Clause "over Q no finite window can suffice": **REFUTED** as stated (C5-ADJ-LOG) |
| C5-I-W | Load-bearing ingredients W1-W6, R1 of Weil's proofs | IMPORTED | upheld | **IMPORTED** (Milne 1509.00797 Sec. 1, L1) |
| C5-I-S | Stepanov-Bombieri ingredients S1-S5 | IMPORTED | could not check | **IMPORTED** (Bombieri 430 L1-partial: Thm 1 hypotheses and Sect. III remark verified) |
| C5-I-D | Deligne ingredients D1-D5 | IMPORTED | upheld w/ page fix | **IMPORTED** (Cor 3.8 and 3.9 on p. 286) |
| C5-I-E | Explicit-formula positivity (Weil 1952; Bombieri 2000; CCM 2009) | IMPORTED | upheld | **IMPORTED** (via Observatory records L1; not primary-read here) |
| C5-TABLE | Ingredient table | IMPORTED + HEURISTIC | upheld w/ corrections | **IMPORTED + HEURISTIC**, corrected version in Sec. 4 |
| C5-E1 | Fake curve zeta functions exist; census over 24 (q,g) | THEOREM + NUM-RIG | upheld w/ corrections | **THEOREM** (existence; exact certified instances, adjudicator re-certified (a), (b), (c)) + **NUMERICAL-RIGOROUS** (counts, two implementations). Convention Z != 1 stated; corrected totals in Sec. 3.6 |
| C5-E2 | Brute-force validation on 5 curves + singular control | NUM-RIG | upheld | **NUMERICAL-RIGOROUS** |
| C5-E3 | Inertia check on 3,300 squarefree admissible P | NUM-RIG + NUM-NONRIG | upheld (exact) | **NUMERICAL-RIGOROUS** (all 3,300 x {T_{2g}, T_{2g+1}} exact via the skeptic's integer Gram method; float-only items superseded) |
| C5-L2 | Mod-2 criterion for quadratic-type Euler products over P^1 | THEOREM | upheld | **THEOREM** (the 1-unit step is proved elementarily in Sec. 3.7) |
| C5-E4 | Fake quadratic-type L-functions (\|a_v\| <= 1, conductor degree 2g+2) violating RH | THEOREM + NUM-RIG + HEURISTIC | upheld | **THEOREM** (instances) + **NUMERICAL-RIGOROUS** (counts, two algorithms) + **HEURISTIC** (Selberg-class reading) |
| C5-S1 | Over Q a one-sided bound psi(x) <= x + C x^theta implies no zeros with Re s > theta; over F_q the upper one-sided bound does not imply RH | THEOREM | upheld | **THEOREM** (classical, Landau) |
| C5-D1 | Uniform zero-free strip for k-fold zero sums <=> RH | THEOREM | upheld | **THEOREM** (trivial, set-level). The identification with zeros of Kurokawa's zeta^{(x)k} is IMPORTED (L0+), not verified |
| C5-OB1 | No Frobenius, no nontrivial self-product (Haran Rem 4.12; Borger; CC defect Id_eps) | IMPORTED | upheld | **IMPORTED** |
| C5-OB2 | Infinite genus: (a) divergence; (b) Stepanov needs q > (g+1)^4; (c) finite window; (d) CC 2026 | THEOREM + IMPORTED + HEURISTIC | upheld w/ corrections | (a) **THEOREM** (with refined asymptotic) + HEURISTIC (def(Delta) reading); (b) **HEURISTIC**; (c) **REFUTED** as stated, replaced by C5-ADJ-W / C5-ADJ-LOG / C5-ADJ-MODEL; (d) **IMPORTED** |
| C5-OB3 | Archimedean place | IMPORTED | upheld | **IMPORTED** |
| C5-OB4 | No real-coefficient Weil cohomology (Deninger 2022 Thm 2.13) | IMPORTED | upheld | **IMPORTED** (L1) |
| C5-OB5 | Formal axioms insufficient, even over F_q | THEOREM + IMPORTED + HEURISTIC | upheld w/ prior art | **THEOREM** (F_q instances) + **IMPORTED** (DH, Kaczorowski-Perelli) + **HEURISTIC** ("both directions"); prior art: arithmetical semigroups |
| C5-OB6 | Polynomial-method barrier over Z | IMPORTED | upheld w/ corrections | **IMPORTED**, corrected: "not with the one-variable method, nor with any fixed weight of type (1.12)"; bracket updated |
| C5-OB7 | No family through Spec Z; Deligne's engine gives Ramanujan | HEURISTIC + IMPORTED | upheld | **HEURISTIC + IMPORTED** |
| C5-OB8 | Sign and absorption in Connes 1999 | IMPORTED + HEURISTIC | could not check | **IMPORTED** (record-level L1-partial) + **HEURISTIC** |
| C5-OB9 | Near-radical of finite windows; decay rate | IMPORTED + HEURISTIC | upheld w/ corrections | Decay law exp(-L e^L): **REFUTED**. Corrected rate exp(-c e^{2L}), c about 12: **IMPORTED** (unrefereed numerics, abstracts) + bookkeeping in adj_ob_numbers.json. "Trace of infinite genus": **HEURISTIC** |
| C5-ML-W | Effectivity axiom on (E, xi_0, xi_1, D) <=> RH | CONJECTURE | upheld | **CONJECTURE (open target)**. The equivalence itself is a **THEOREM** (Connes' Lemma 2.1, re-derived) |
| C5-ML-W0 | Riemann-Roch on the square reproducing known small-support positivity | CONJECTURE | upheld w/ correction | **CONJECTURE (open target)**, with axiom (a') added (Sec. 5) |
| C5-ML-C1 | CC Conj. 4.1 at q = 3 | CONJECTURE | upheld w/ correction | **CONJECTURE (open target; IMPORTED statement)**, corrected reading: h_1 supported in (3^{-1/2}, 3^{1/2}) |
| C5-ML-E1 | Finite windows Pos(L) | CONJECTURE + IMPORTED | upheld w/ correction | **CONJECTURE (open target)**, reformulated as EFR (Sec. 5); "over Q no finite L suffices" is **REFUTED** as stated |
| C5-ML-Den | Deninger 2.15, quaternion field | CONJECTURE | upheld | **CONJECTURE (open target)** |
| C5-ML-TP | One cohomology with Theta realising the full Euler product | CONJECTURE | upheld | **CONJECTURE (open target)** |
| C5-ML-F1 | Intrinsic Delta.Psi(lambda) = CCM Prop 7.2 distribution | CONJECTURE | upheld | **CONJECTURE (open target)** |
| C5-ML-S | (i) psi(x) <= x + O(x^{1/2+eps}) by auxiliary objects; (ii) Pritsker's problem | CONJECTURE | upheld | **CONJECTURE (open target)**. (i) => RH is a THEOREM (C5-S1) |
| C5-A | Assessment: technical vs conceptual gaps | HEURISTIC | upheld w/ corrections | **HEURISTIC**, corrected version in Sec. 6 |
| C5-SK-INERTIA | (skeptic 3.1) confluent inertia | (new) | THEOREM | **THEOREM**, merged into C5-T3 |
| C5-SK-WINDOW | (skeptic 3.2) window corollary without RH | (new) | PROP-SKETCH | **THEOREM**, as C5-ADJ-W |
| C5-SK-ASYM | (skeptic 3.4) over F_q, the lower one-sided bound s_r <= C q^{r/2} for all r implies RH | (new) | THEOREM | **THEOREM** (re-derived; prior art not searched, likely folklore) |
| C5-ADJ-W | Sharp window theorem over F_q | (new) | (new) | **THEOREM** |
| C5-ADJ-SHARP | Threshold (g-1/2) log q attained in the formal class for 20 of the 24 tested (q,g) | (new) | (new) | **THEOREM** (computer-assisted, exact) |
| C5-ADJ-LOG | There is an L0 with Pos(L) => RH for all L >= L0 | (new) | (new) | **THEOREM** (trivial, non-constructive) |
| C5-ADJ-MODEL | Window-L zero-side positivity with zeta-like counting does not force RH | (new) | (new) | **THEOREM** (explicit, error O(T) in N(T)); refinement with error O(1): **PROPOSITION-PROOF-SKETCH** (Beurling sampling IMPORTED) |
| C5-ADJ-EFR | Effective finite reduction over Q | (new) | (new) | **CONJECTURE (open target)** |

---

## 3. The most useful precise statements

### 3.1 Normalisation

See the header. Each FE polynomial with real coefficients has its multiset {beta_i} stable under beta -> 1/beta (FE) and under beta -> conj(beta) (real coefficients). Hence t_{-n} = conj(t_n) = t_n, and T_N is real symmetric.

The zeros of Z(q^{-s}) are s = 1/2 + i gamma with e^{i gamma h} = beta_j, i.e. gamma in gamma_j + (2 pi/h) Z. Off-circle beta corresponds to non-real gamma.

### 3.2 C5-T3, confluent form (THEOREM; skeptic 3.1, re-derived)

**Statement.** Let P in R[T] with P(0) = 1 and deg P = 2g satisfy the FE. Let gamma_1, ..., gamma_d be the distinct normalised reciprocal roots, with multiplicities mu_j, and let m = #{j : |gamma_j| > 1}. Then for every N >= d,

```
inertia(T_N) = (n_+, n_-, n_0) = (d - m, m, N - d).
```

Consequences:
- RH <=> T_d >= 0 <=> T_{2g} >= 0.
- T_{2g} involves only s_1, ..., s_{2g-1}, i.e. only N_1, ..., N_{2g-1}.
- Under RH, rank T_N = d for N >= d. This is Suzuki 2610.41115, Prop 4.3, with his d.

**Proof.**
1. T_{kl} = sum_j mu_j gamma_j^k gamma_j^{-l}.
2. Let sigma be the involution gamma -> 1/conj(gamma) on the distinct roots. Then gamma_j^{-l} = conj(gamma_{sigma(j)}^l).
3. So T = V A V^*, with V = (gamma_j^k) (an N x d Vandermonde matrix with distinct nodes) and A_{j,l} = mu_j [l = sigma(j)].
4. A is Hermitian, because mu is constant on sigma-orbits.
5. A is a direct sum of blocks (mu_j) at fixed points (|gamma_j| = 1) and [[0, mu], [mu, 0]] on 2-cycles (|gamma| != 1). There are m such 2-cycles.
6. For N >= d, V has full column rank. Complete it to an invertible W = [V | V'] and apply Sylvester's law to W (A (+) 0) W^*. ∎

### 3.3 C5-ADJ-W: the sharp window theorem over F_q (THEOREM)

**Setting.** Let P be as in 3.2: real coefficients and the FE. No Euler product, no RH and no squarefreeness are assumed.

For u in L^2(R) with compact support, put û(z) = ∫ u(x) e^{izx} dx and

```
W(u) := sum_{zeros rho = 1/2 + i gamma} m_rho û(gamma) conj(û(conj gamma)).
```

This is the zero side of the explicit formula for f = u * ũ, ũ(x) = conj(u(-x)), since f̂(gamma) = û(gamma) conj(û(conj gamma)).

**Statement.** For every a > 0:

```
W(u) >= 0 for all u in C_c^inf(-a, a)   <=>   T_{ceil(2a/h)} >= 0 .
```

Consequently:
- RH(P) <=> W >= 0 on C_c^inf(-a,a) for one (equivalently every) a > (d-1)h/2.
- In particular this holds for a > (g - 1/2) log q.
- If T_{N_1} is the first indefinite T_N (N_1 <= d by 3.2), the exact detection threshold is a > (N_1 - 1)h/2.
- In terms of the autocorrelation f = u * ũ, the support half-width must exceed (N_1 - 1) log q. The prime side then involves N_r only for r <= N_1 - 1, consistent with T_{N_1} using only t_0, ..., t_{N_1 - 1}.

**Proof.**

*Step 1: fibre identity.* Fix gamma in C and let ζ = e^{i gamma h}. For t in (0, h) set

```
L_gamma u(t) = sum_k u(t+kh) e^{i gamma (t+kh)}    (a finite sum).
```

Substituting x = t + kh gives

```
û(gamma + 2 pi n/h) = ∫_0^h L_gamma u(t) e^{2 pi i n t/h} dt.
```

So (1/h) û(gamma + 2 pi n/h) are the Fourier coefficients of L_gamma u on (0, h). Polarised Parseval gives

```
sum_n û(gamma + 2 pi n/h) conj(û(conj gamma + 2 pi n/h)) = h ∫_0^h L_gamma u(t) conj(L_{conj gamma} u(t)) dt.
```

Since e^{i gamma x} conj(e^{i conj(gamma) x}) = 1 for real x, the integrand equals sum_{k,l} ζ^{k-l} u(t+kh) conj(u(t+lh)).

Summing over the zero classes with multiplicities gives

```
W(u) = h ∫_0^h <T_{r(t)} u(t), u(t)> dt.
```

Here u(t) = (u(t+kh))_{k in I(t)}, I(t) = {k : t+kh in (-a,a)} is a block of r(t) consecutive integers, and the Toeplitz entries are t_{k-l} (translation invariant). This is Suzuki's (4.1)/(4.5) with RH removed; only the periodicity of the zero set is used.

*Step 2: which matrix sizes occur.* r(t) takes only the values floor(2a/h) and ceil(2a/h) on sets of positive measure (Suzuki, proof of Prop 4.3). T_r is a principal submatrix of T_{r+1}.

*Step 3 (<=).* If T_{ceil(2a/h)} >= 0, the integrand is >= 0 almost everywhere.

*Step 4 (=>).* Let R = ceil(2a/h). Choose an open interval J in (0,h) on which r(t) = R and k_0(t) = k_0 are constant. Choose v in R^R with v^T T_R v < 0, and phi in C_c^inf(J) with phi != 0. Put

```
u(x) = sum_{l<R} v_l phi(x - (k_0+l)h).
```

Then u is in C_c^inf(-a,a), and W(u) = h (∫ phi^2) v^T T_R v < 0.

*Step 5 (consequences).* By 3.2, T_N is indefinite for N >= d iff m >= 1, and ceil(2a/h) >= d iff a > (d-1)h/2. ∎

**Checks.**
- adj_window_fibre.py compares the zero sum with the fibre integral for general non-aligned test functions. It uses 3 fakes with off-circle beta, including a complex quadruple (q=5, g=2), and one genuine curve.
- Relative difference <= 3.5e-15 in all 12 tests, with real and complex coefficients.
- For the hidden fake (q=3, g=3, h(x) = x^3 - 10x - 7), the constructed u has support [-2.7945, 2.7945], just beyond the threshold (g - 1/2) log 3 = 2.7465. It gives W(u) = -2.2110e-4, matching h (∫ phi^2) lambda_min(T_6) to 13 digits. Here lambda_min(T_5) = 0.823 > 0 and lambda_min(T_6) = -0.049.

### 3.4 C5-ADJ-SHARP: the threshold is attained in the formal class (THEOREM, computer-assisted, exact)

For each of the following (q, g) there is an admissible fake P (B_d >= 0 for all d, RH false) whose first indefinite Toeplitz size is N_1 = 2g, so that T_{2g-1} >= 0:
- g = 1: q in {5, 7, 8, 9, 11, 13, 16, 25, 27, 32, 49}. Every listed fake has N_1 = 2. With the degenerate Z == 1 this holds for every q.
- g = 2: q in {3, 4, 5, 7, 8, 9}.
- g = 3: q in {2, 3, 4}.

By C5-ADJ-W, for these P:
- Weil positivity holds on C_c^inf(-a, a) for every a <= (g - 1/2) log q;
- yet RH fails.

So over the formal class the window (g - 1/2) log q cannot be lowered.

Example: q = 3, g = 3, P = 1 - T^2 - 7T^3 - 3T^4 + 27T^6.
- B_1..B_6 = 4, 2, 1, 15, 41, 119.
- B_d >= 0 for all d is certified: exact B_d for d <= D0 = 5, plus an explicit monotone tail bound with max|alpha|/sqrt 3 <= 1.0408.
- inertia(T_5) = (5,0,0), inertia(T_6) = (5,1,0).
- The first Hasse-Weil violation is at k = 28.

Counts of listed fakes with N_1 = 2g: adj_exact_checks.json, part (5). The census JSON truncates the fake lists for 9 pairs, so these are lower bounds.

### 3.5 Finite windows over Q: what is true

Let Pos(L) mean: W(g * g~) >= 0 for all g in C_c^inf(R) with supp g in [-L, L] (log scale), for zeta.

**C5-ADJ-LOG (THEOREM; trivial, non-constructive).** There is L0 < inf such that Pos(L) => RH for every L >= L0.

*Proof.* Pos is monotone decreasing in L. By Weil's criterion, RH <=> Pos(L) for all L.
- If RH holds, every L works.
- If RH fails, some g in C_c^inf has W(g * g~) < 0. So Pos(L) fails for all L >= L0 := max|supp g|, and the implication holds vacuously. ∎

Hence the sentence "over Q no finite window can suffice" (C5-T3, OB2(c), ML-E1, C5-A) is false as stated, not merely unproved. Its defensible content is: (i) no *explicit* L0 is known, and (ii) the following model statement.

**C5-ADJ-MODEL (THEOREM, elementary).** Fix L > 0 and let R_0 be any real multiset with sum_{gamma in R_0} |û(gamma)|^2 < inf for u in C_c^inf(-L, L); for example the ordinates of any multiset with N(T) = (T/2 pi) log(T/2 pi e) + O(log T). Let

```
Z_0 = R_0 ∪ (pi/L) Z,
Z   = Z_0 ∪ {T+i delta, T-i delta, -T+i delta, -T-i delta},
```

with any T > 0 and 0 < delta <= 1/(4L). The points 1/2 + i gamma for the last four lie off the critical line, at real part 1/2 -+ delta. Then

```
W_Z(u) := sum_{gamma in Z} û(gamma) conj(û(conj gamma))  >=  0.35 L ||u||_2^2   for all u in L^2(-L, L).
```

*Proof.*
1. Fourier series on [-L, L] give sum_n |û(n pi/L)|^2 = 2L ||u||_2^2. Real points contribute |û|^2 >= 0, so W_{Z_0}(u) >= 2L ||u||^2.
2. Write A = û(T + i delta), B = û(T - i delta), U = û(T). Since |û'(z)| <= L e^{L |Im z|} ||u||_1, we get |A - U|, |B - U| <= eps := delta L e^{L delta} ||u||_1.
3. Then 2 Re(A conj B) >= 2|U|^2 - 4|U| eps - 2 eps^2 >= -4 eps^2. The same holds at -T.
4. With ||u||_1 <= sqrt(2L) ||u||_2, the quadruple contributes >= -16 delta^2 L^3 e^{2L delta} ||u||^2.
5. So W_Z(u) >= 2L (1 - 8 delta^2 L^2 e^{2L delta}) ||u||^2 >= 2L (1 - e^{1/2}/2) ||u||^2 for delta <= 1/(4L). ∎

The counting function of Z is N_{R_0}(T) + (2L/pi) T + O(1). This has zeta's leading term when R_0 is zeta-like, but an error of order T.

**Refinement (PROPOSITION-PROOF-SKETCH).** Take R_0 = ±(Gram points), so N(T) = theta(T)/pi + O(1), which matches N_zeta up to O(log T). Drop the lattice. Use instead a separated subset of R_0 of lower Beurling density (L+1)/pi > L/pi (it exists, because Gram density grows like log t/2 pi). By Beurling's sampling theorem (IMPORTED; e.g. Seip, *Interpolation and sampling in spaces of analytic functions*, 2004), W_{R_0} >= c(L) ||u||^2 on L^2(-L, L). Replacing two consecutive Gram points near a height T > 2 pi e^{2(L+1)} that are not in the subset (and their negatives) by an off-line quadruple at height T and displacement delta <= delta_0(L) keeps W >= 0, and keeps N(T) = theta(T)/pi + O(1). delta_0(L) is not explicit.

**Meaning.**
- Over F_q, C5-ADJ-W decides RH on a fixed window because the zero set has finite rank d <= 2g modulo 2 pi/h.
- Over Q, a fixed window L cannot see off-line displacements delta << 1/L (adj_model_window.py: negativity appears only for delta of order 1/L).
- So any effective finite reduction for zeta must use prime-side (Euler product) information. Zero-side positivity and density cannot supply it.
- This is the exact mathematical content of "infinite genus" for the window route. Not claimed new: an uncertainty-principle argument, cf. Bombieri 2000 Thms 10-11.

### 3.6 C5-E1 corrected census (counts NUMERICAL-RIGOROUS; existence THEOREM)

Format: admissible / RH-true / RH-false (of which: non-real x).

| g | q: counts |
|---|---|
| 1 | 2: 5/5/0; 3: 7/7/0; 4: 9/9/0; 5: 11/9/2; 7: 15/11/4; 8: 17/11/6; 9: 19/13/6; 11: 23/13/10; 13: 27/15/12; 16: 33/17/16; 25: 51/21/30; 27: 55/21/34; 32: 65/23/42; 49: 99/29/70 |
| 2 | 2: 23/23/0; 3: 74/57/17(8); 4: 172/93/79(45); 5: 326/127/199(111); 7: 880/205/675(380); 8: 1303/252/1051(596); 9: 1843/309/1534(880) |
| 3 | 2: 172/147/25(11); 3: 1759/609/1150(825); 4: 9366/1541/7825(6035) |

Convention: the degenerate Z == 1 (g=1, a = q+1, admissible and RH-false) is excluded. Including it adds 1 admissible fake to each g = 1 row.

Totals: 16,354 admissible and 12,787 fakes; with the degenerate case, 16,368 and 12,801.

The 41 g >= 2 candidates the investigator excluded as "undecided" are non-admissible: first negative B_d at d <= 7.

g = 1, P = 1 - aT + qT^2: admissible <=> -q <= a <= q+1.
- Necessity is a THEOREM: B_1 = q+1-a and B_2 = (q+a)(q+1-a)/2.
- Sufficiency is verified exactly for the 14 tested q (NUMERICAL-RIGOROUS) but not proved in general.

### 3.7 C5-L2: the 1-unit step, fully elementary

Every f in 1 + T F_2[[T]] is uniquely prod_{n>=1} (1+T^n)^{eps_n} with eps_n in {0,1}. Proof: induction on the lowest nonconstant degree, using (1+T^n)^{-1} ≡ 1 + T^n mod T^{n+1}.

Grouping n = 2^j m (m odd) and using (1+T^{2^j m}) = (1+T^m)^{2^j} in characteristic 2 gives f = prod_{m odd} (1+T^m)^{a_m}. Here a_m = sum_j eps_{2^j m} 2^j in Z_2, and the a_m are unique by uniqueness of the eps-expansion.

So prod_d (1+T^d)^{e_d} = 1 with e_d in Z iff sum_j 2^j e_{2^j m} = 0 in Z_2 for every odd m. That is the integrality condition used in C5-L2.

### 3.8 Other complete statements (proofs in REPORT.md / SKEPTIC_REVIEW.md, re-derived by the adjudicator)

- **C5-T1 (Gram identity).** On C x C put xi_n = Gamma_n - q^n h_1 - h_2. Then xi_n.h_1 = xi_n.h_2 = 0 and xi_m.xi_n = -q^{min(m,n)} s_{|m-n|}. Hodge index gives G_N = (q^{min} s_{|m-n|}) >= 0, and G_N = D T_N D with D = diag(q^{m/2}). The Rosati trace Tr(F^m (F^n)') = q^{min} s_{|m-n|} gives the same matrix.
  - The adjudicator re-checked the expansion xi_m.xi_n = Gamma_m.Gamma_n - q^m - q^n, using Gamma_n.h_1 = 1 and Gamma_n.h_2 = q^n.
  - Both of Weil's proofs feed one Gram matrix, and C5-T3/ADJ-W show that its 2g x 2g corner already decides RH.
- **C5-SK-ASYM.** For FE P with real coefficients, if s_r <= C q^{r/2} for all r (i.e. N_r >= q^r + 1 - C q^{r/2}), then RH holds.
  - Proof: the dominant-modulus sum S_r is real, with mean >= 0 and mean square >= 1, so S_r >= 1/(4M) infinitely often.
  - The opposite one-sided bound fails: example (a) has s_r > 0 for all r.
  - Over Q, Landau gives either one-sided bound on psi(x) - x (C5-S1).
- **C5-ML-W lemma (Connes 2016, Lemma 2.1).** Let E have a symmetric form and isotropic xi_0, xi_1 with <xi_0, xi_1> = 1. If every x with <x,x> > 0 has <x, xi_0 + xi_1> != 0, then <x,x> <= 2 <x,xi_0><x,xi_1>.
  - Proof: x' = x - <x,xi_1> xi_0 - <x,xi_0> xi_1 is orthogonal to xi_0 + xi_1, and <x',x'> = <x,x> - 2<x,xi_0><x,xi_1>.

---

## 4. Ingredient table (final; IMPORTED synthesis + HEURISTIC "missing"/"progress" columns)

Exists codes: T = theorem, C = conjectural, D = dictionary only, N = numerical. "Rec." = through an Observatory record, not primary-read in this campaign.

| ID | Function-field ingredient (exact statement; source) | Number-field analogue required | What exists | Missing | Smallest progress |
|---|---|---|---|---|---|
| W1 | C x C with intersection pairing: Gamma_m.Gamma_n = q^m N_{n-m} (m<n), Gamma_n^2 = q^n(2-2g) (C5-T1; Milne 1509.00797 Sec. 1, Thm 1.2 p.8, Ex. 1.7 p.10) | A "surface" Spec Z x_{F_1} Spec Z with divisors Delta, Psi(lambda), whose pairing is Weil's distribution | D: CCM 2009 Prop 7.2 (rec.). T: CC square of the arithmetic site; Psi(lambda) compose with defect Id_eps (PAPER-0086 Thm 7.7, rec.). T(def.): Borger W*(Spec Z) (0906.3146 Sec. 1.2). T: Haran Rem 4.12 (collapse under total commutativity). C: Scholze q-de Rham near Delta (1606.01796 p.3) | An intrinsic intersection number | ML-F1 |
| W2 | Hodge index: D.H = 0 => D^2 <= 0 (Castelnuovo-Severi), giving G >= 0 | Weil positivity on the "primitive part" (equivalent to RH) | T: small support only (Yoshida 1992; CC 2021, h_1 in [2^{-1/2}, 2^{1/2}], PAPER-0099). N (unrefereed, not replayed): Zhu Pos(0.8). T: arithmetic Hodge index on X -> Spec O_K (Faltings, Hriljac; L0), but that is a different surface | Positivity for all supports from a structural source | ML-C1, EFR; ML-W0 |
| W3 | Riemann-Roch on the surface: l(mD) + l(K-mD) >= m^2 D^2/2 + O(m); D^2 > 0 => +-mD effective; effective => D.H > 0 (Milne Lemma 1.1, Thm 1.2) | Dim H^0(D) + Dim H^0(-D) >= D.D/2 on the square, plus "effective => positive degree" | T: RR on the arithmetic curve (CC 2306.00456 Thm 1.1; 2205.01391 Thm 1.1). T: van der Geer-Schoof. C: RR on the square (Connes 2016; PAPER-0116: H^1 undefined) | H^0, H^1, Dim on the square | ML-W0 |
| W4 | Frobenius morphism of degree q; Fix(F^r) = C(F_{q^r}) | A flow whose periodic orbits are the primes, with lengths log p | T: scaling action on the adele class space (Connes 1999); Fr_lambda on the arithmetic site; Deninger foliated systems (1807.06400); Borger Lambda-lifts (trivial on Z); phi_p on TP one prime at a time | A Frobenius on an object that also has W1-W3 | Leafwise H^1 of a Deninger system for Spec Z |
| W5 | RR on C => rationality, FE, deg P = 2g (finite H^1) | Infinite H^1 with spectrum = zeros, duality, regularised determinants | T: spectral realisations (Connes 1999, critical zeros only; Meyer 2005, all zeros; CCM H^1). T: CC 2026 Pic(Spec Zbar) ~ Riemann sector (2602.15941 Thm 1.1). T: local factors as regularised determinants (Deninger 1992; CC 1211.4239) | One theory giving both det = xi and positivity | ML-Den, ML-TP |
| W6 | Constant-field tower r -> inf at fixed g; finite rank d <= 2g modulo 2 pi/h (C5-ADJ-W) | None | None (Q(mu_n) is geometric) | Conceptual. C5-ADJ-MODEL quantifies the consequence | - |
| R1 | Rosati: Tr(phi phi') > 0; Tr(F^m F^n') = q^{min} s_{\|m-n\|} | Positive trace on an algebra generated by a Frobenius flow | T: Connes (unitary on critical zeros only). T: Suzuki 2610.41115 Sec. 8 (F_q Weil Hilbert space via Rosati). Number-field version conditional on RH (2610.32704, abstract) | Unconditional positivity | Model case on a window with known positivity |
| S1 | RR on C | Arakelov RR | T (CC 2022/23; van der Geer-Schoof) | None | - |
| S2 | f o F = f^q; Bombieri independence lemma (Bourbaki 430 Sect. II) | "Free q-th powers" over Z | None (Frobenius lifts trivial on Z) | Everything | Conceptual |
| S3 | Auxiliary function; N_1 <= q + (2g+1) sqrt q + 1 for q = p^{2a} > (g+1)^4 (Bourbaki 430 Sect. II Thm 1) | psi(x) <= x + O(x^{1/2+eps}) via auxiliary objects, which alone implies RH (C5-S1) | T: Gelfond-Schnirelman/Nair give Chebyshev-type bounds; t_Z([0,1]) in [0.4222286, 0.4226847] > 1/e (Niedbala Giraudin 2026, abstract); fixed weights B(w) < 1 (Pritsker Prop 1.3) | Square-root saving; even the PNT | Pritsker's problem: w_n with B(w_n) -> 1 |
| S4 | Lower bound via Galois closure (Bourbaki 430 Sect. III); the upper bound alone is consistent with omega = (q, 1) | Not needed over Q (C5-S1); over F_q the lower half suffices formally (C5-SK-ASYM) | - | - | - |
| D1 | l-adic H^*_c, trace formula, rationality (Weil I Sec. 1) | Deninger's axioms 2.1-2.6 | C. T: no real-coefficient theory (Deninger 2204.02714 Thm 2.13). T: Hesselholt Thm A (F_q only) | The theory | ML-Den, ML-TP |
| D2 | Lefschetz pencils, big monodromy (Weil I Sec. 5, Thm 5.10) | A family in which zeta's zeros are Frobenius eigenvalues at a point | None | Conceptual (OB7) | - |
| D3 | Rankin-Landau positivity => purity (Weil I Thm 3.2 p.284; Cor 3.8-3.9 p.286) | The same for automorphic L | T: transfers (Langlands 1970; Newton-Thorne Sym^n, L0+), but yields Ramanujan, not RH | - | - |
| D4 | Tensor-power trick (loss 1/2 uniform in m) | k-uniform zero-free strip for zeta^{(x)k} | Equivalent to RH (C5-D1) | The geometric engine | - |
| D5 | Weights, Fourier transform (Weil II; Laumon 1987, L0) | Mixed arithmetic sheaves on Spec Zbar | Hodge weights at infinity only | Conceptual | - |
| E | Weil positivity; decided on the window a > (N_1-1) log q/2 (C5-ADJ-W) | Weil 1952 criterion | T: Bombieri 2000 Thms 2, 8, 10-12 (rec.); CCM 2009 (rec.); Yoshida; CC 2021. N: Zhu (unrefereed) | A positivity source; an effective finite reduction (zero-side data cannot supply one: C5-ADJ-MODEL) | EFR; ML-C1 |
| CT | Connes 1999 Thm 5 (char p): global trace formula <=> RH, true by Weil | (16) for Q <=> RH | T: semilocal trace formula (Thm 4); quasi-inner prod_F rho_v (PAPER-0125 Thm 4.8) | Global (16); ker u(F)_22 = semilocal Sonin space; positivity | ML-C1 |
| Den | Serre 1960 Kahler-type positivity on H^1 | Deninger 2.7: antilinear * with *^2 = -1 | C. T: a real structure is impossible (Thm 2.13) | The cohomology | ML-Den |
| TP | Hesselholt Thm A (X smooth proper over F_q) | The same for Spec Zbar | T: F_q only (Bokstedt periodicity); archimedean via cyclic homology (CC 1211.4239) | Periodicity and Theta for Z | ML-TP |
| F1 | Constant field F_q | "F_1" under Z | T: Borger (no archimedean place, 0906.3146 p.5); Haran; CC arithmetic site and (Spec Z)_{F_1} (2606.06604 Thms 1-2); Manin 1995 (L0+); Soule/Deitmar (L0) | An F_1-framework producing W1-W3 | ML-F1 |

Known obstructions recorded in this dossier:
- OB1: no Frobenius and no nontrivial self-product.
- OB2: infinite genus; made exact for the window route by C5-ADJ-W versus C5-ADJ-MODEL.
- OB3: the archimedean place.
- OB4: no real-coefficient Weil cohomology.
- OB5: formal axioms are insufficient. Over Q: Davenport-Heilbronn. Over F_q: the fakes of E1/E4 and arithmetical semigroups.
- OB6: the integer Chebyshev barrier.
- OB7: no family through Spec Z.
- OB8: the sign/absorption issue.
- OB9: the near-radical with -ln lambda_min ~ c e^{2L}.

---

## 5. Missing-lemma statements (final form)

- **ML-W (CONJECTURE, open target; equivalent to RH).**
  - Find a real vector space E with a symmetric form, isotropic xi_0, xi_1 with <xi_0, xi_1> = 1, and a linear map D: C_c^inf(R_+^*)_R -> E such that:
    - <Df, Dg> = 2 s(f,g) (Connes' normalisation, PAPER-0007);
    - <Df, xi_0> = ∫ f d*u and <Df, xi_1> = ∫ f du;
    - effectivity: <x,x> > 0 => <x, xi_0 + xi_1> != 0.
  - By the lemma in 3.8 this gives Weil's inequality, hence RH. Conversely RH gives such an E. All the content is in proving effectivity.
- **ML-W0 (CONJECTURE, open target; makes no claim about RH).** On the square of the scaling site define H^0(D) and Dim H^0(D) for D(f) = ∫ f(lambda) Psi(lambda) d*lambda, with:
  - (a) Dim H^0(D) > 0 implies D is linearly equivalent to an effective divisor;
  - (a') the degree against Psi(1) + Psi(1)^t is invariant under linear equivalence and equals ∫ f d*u + ∫ f du on D(f) (skeptic's addition);
  - (b) an effective nonzero divisor has positive degree;
  - (c) Dim H^0(D(f)) + Dim H^0(-D(f)) >= s(f,f) for real f in C_c^inf([2^{-1/2}, 2^{1/2}]) with both moments zero.
  - Then (a)-(c) re-derive s(f,f) <= 0 on that support, which is known by Yoshida and CC 2021.
- **ML-C1 (CONJECTURE, open target; CC Conj. 4.1 at q = 3).**
  - With S = {inf, 2}, the semilocal operator framework proves Weil's inequality for h = h_1 * h_2, h_2(x) = h_1(x^{-1}), with h_1 supported in (3^{-1/2}, 3^{1/2}) and ∫ h_1 x^{+-1/2} d*x = 0.
  - Required sub-step: identify ker u(F)_22 with the geometric semilocal Sonin space (PAPER-0125).
  - The numerical inequality (Pos(0.549)) is already covered by Zhu's unrefereed certified Pos(0.8). The content of ML-C1 is the mechanism.
- **EFR, replacing ML-E1 (CONJECTURE, open target).**
  - Find an explicit L0 and a proof, not assuming RH, that Pos(L0) => RH.
  - By C5-ADJ-LOG such an L0 exists, non-constructively. By C5-ADJ-MODEL the proof must use prime-side structure.
  - Over F_q the analogue holds with L0 = (g - 1/2) log q, sharp over the formal class (C5-ADJ-W, C5-ADJ-SHARP).
  - Smallest checkable components:
    - (i) an independent Arb replay of Zhu's Pos(0.8);
    - (ii) the semilocal mechanism ML-C1.
  - Ceiling: certifying Pos(L0) costs about 5.4 e^{2 L0} digits (OB9 corrected).
- **ML-Den (CONJECTURE, open target; Deninger 2204.02714 Sec. 2.15).** For one Galois quaternion field k/Q with group H_8 and symplectic pi with W(pi) = -1, construct number-theoretically:
  - a 2-dimensional V_k(pi) carrying the G-action;
  - an invariant alternating form that is a sum of local terms;
  - an antilinear * with *^2 = -1 making the induced form positive.
- **ML-TP (CONJECTURE, open target).** Construct one cohomology H^*(Spec Zbar) with a graded derivation Theta such that prod_v L_v(s)^{-1} = (ratio of det_inf(s - Theta | H^i)) for Re s > 1. It should extend Hesselholt's Thm A and the archimedean cyclic-homology description at the same time.
- **ML-F1 (CONJECTURE, open target).** In some F_1-framework, define Delta.Psi(lambda) intrinsically and prove it equals the CCM 2009 Prop 7.2 distribution.
- **ML-S (CONJECTURE, open target).**
  - (i) psi(x) <= x + O_eps(x^{1/2+eps}) by an auxiliary-object argument; this already implies RH (C5-S1).
  - (ii) Smallest step: Pritsker's problem, weights w_n of type (1.12) with B(w_n) -> 1.

---

## 6. Assessment (HEURISTIC, corrected)

**Most technical gap (well-posed, finite, auditable): semilocal and finite-window Weil positivity (ML-C1, EFR components).**
- The operators are explicit: prolate/Sonin spaces and quasi-inner local factors.
- Only finitely many places enter.
- Certifying a *numerical* window inequality is an interval-arithmetic task, with cost about 5.4 e^{2L} digits.
- *Proving* it within the semilocal framework (ML-C1) is not routine; it needs the Sonin identification.

Ceiling: by C5-ADJ-MODEL, no amount of window positivity on the zero side, plus density information, yields RH. A finite reduction needs arithmetic input. Over F_q that input is the finite rank d <= 2g, and nothing analogous is known over Q.

**Most conceptual gap: the positivity source.**
- Over F_q, positivity comes from effectivity (Riemann-Roch on C x C) or from Rosati positivity. Both act on the single Gram matrix of C5-T1.
- Over Q one needs either a surface with W1-W3 (ML-F1, ML-W0) or a cohomology with quaternionic Hodge-* positivity (ML-Den, OB4).
- ML-W0 is the model case that would re-derive a known positivity by the Riemann-Roch mechanism.

**Routes ranked by type of obstruction:**
1. Weil C x C / Rosati: conceptually blocked at W1-W3, with the clearest target.
2. Explicit formula / Connes trace formula: technically open, with real partial results. Globally RH-equivalent.
3. Deligne: conceptually blocked (OB7). D4 is equivalent to RH (C5-D1), and its positivity engine proves Ramanujan, not RH.
4. Stepanov-Bombieri: blocked quantitatively (OB6) and structurally (S2). Over Q only one one-sided bound would be needed (C5-S1).

---

## 7. Negative results and withdrawn statements

- **REFUTED as stated:** "over Q no finite window can suffice" (C5-T3, OB2(c), ML-E1, A). See C5-ADJ-LOG; the replacements are C5-ADJ-MODEL and EFR.
- **REFUTED as stated:** OB9 "lambda_min(L) decays like exp(-L e^L); certification needs about L e^L digits". At L = 2, exp(-L e^L) = 3.8e-7, against the reported bound 3.2e-283. The correct order is exp(-c e^{2L}) with c about 12.
- **Corrected description:** the 41 "undecided" census cases are non-admissible (B_d < 0 at d <= 7), not cases needing D0 > 4000. Code flaw: `positivity_all_degrees` gives up before the cheap exact B_d screen.
- **Corrected convention:** g = 1, a = q+1 (Z == 1) is admissible and RH-false. The investigator's counts hold with Z != 1 imposed.
- **Corrected reading:** the C5-T3 window [-g log q, g log q] bounds the support of u, not of u * u~. The sharp threshold is (d-1) log q/2.
- **Corrected citation:** OB6 "cannot even give the PNT" overstates Pritsker.
- **Recorded failures** (from REPORT.md and SKEPTIC_REVIEW.md, confirmed):
  - the d <= 12 admissibility screen was abandoned;
  - y^2 = x^5 + x + 1 over F_3 is singular (negative control);
  - E3 Rump enclosures were insufficient;
  - the Castelnuovo 2x2 route with smeared divisors reduces to Cauchy-Schwarz, i.e. to RH;
  - the one-sided Stepanov upper bound is insufficient over F_q;
  - skeptic bug: n_1(P^1) = q instead of q+1, fixed.
- **Adjudicator negative knowledge:**
  - A first draft of adj_exact_checks.py raised "ambiguous modulus" on every on-circle root, because Arb balls cannot decide |alpha| = sqrt q. The classification was rewritten through x = alpha + q/alpha: realness is certified, and x^2 versus 4q is decided with an exact fallback.
  - In adj_model_window.py the B-spline subspace (24 functions) cannot resolve frequencies near T = 50 at L = 2. Its minimum there is trivially 2L. The subspace minimum is only an upper bound for the true infimum, so that row illustrates nothing.

---

## 8. Reproducibility

Versions: Python 3.13.18, python-flint 0.9.0, sympy 1.14.0, numpy 2.5.3, scipy (recorded in JSON), mpmath 1.3.0. At most 2 cores were used.

Run from `research/exploratory/riemann-observatory/experiments`, with `D=<scratchpad>/data` holding the certified zero TSVs.

```bash
# verify recorded hashes
(cd results/C5-function-field-transfer && grep -v 'code/' SHA256SUMS | sha256sum -c)   # investigator: 5 outputs
grep 'code/' results/C5-function-field-transfer/SHA256SUMS | sha256sum -c               # investigator: 5 scripts
sha256sum -c results/C5-function-field-transfer/SKEPTIC_SHA256SUMS           # skeptic: 4 scripts + 6 outputs
sha256sum -c results/C5-function-field-transfer/adjudicator/SHA256SUMS       # adjudicator: 4 scripts + 4 outputs
# investigator (scripts write to fixed paths under results/C5-function-field-transfer/: run in a copy to keep the record)
python3 code/C5-function-field-transfer/ff_fake_census.py        # 731 s  -> fake_census.json
python3 code/C5-function-field-transfer/ff_curves_check.py       #        -> curves_check.json
python3 code/C5-function-field-transfer/ff_inertia_check.py      # 197 s  -> inertia_check.json
python3 code/C5-function-field-transfer/ff_fake_quadratic.py     # 134 s  -> fake_quadratic.json
# skeptic
python3 code/C5-function-field-transfer/skeptic_census_indep.py small    # ~76 s
python3 code/C5-function-field-transfer/skeptic_census_indep.py q4g3     # ~111 s
python3 code/C5-function-field-transfer/skeptic_inertia_exact.py         # minutes
python3 code/C5-function-field-transfer/skeptic_pointcount.py results/C5-function-field-transfer/skeptic_pointcount.json
python3 code/C5-function-field-transfer/skeptic_quadratic_indep.py
# adjudicator
python3 code/C5-function-field-transfer/adjudicator/adj_exact_checks.py results/C5-function-field-transfer/fake_census.json \
        results/C5-function-field-transfer/adjudicator/adj_exact_checks.json                          # 10.9 s
python3 code/C5-function-field-transfer/adjudicator/adj_window_fibre.py \
        results/C5-function-field-transfer/adjudicator/adj_window_fibre.json                          # 46.8 s
python3 code/C5-function-field-transfer/adjudicator/adj_ob_numbers.py $D/zeros_1_50000.tsv $D/zeros_50001_100000.tsv \
        results/C5-function-field-transfer/adjudicator/adj_ob_numbers.json                            # 1.5 s
python3 code/C5-function-field-transfer/adjudicator/adj_model_window.py \
        results/C5-function-field-transfer/adjudicator/adj_model_window.json                          # 3.2 s
```

Adjudicator output hashes (sha256):

| file | sha256 |
|---|---|
| `adj_exact_checks.json` | `e8f4f66e8f6015ed06417f6682ce280db7fb95c2bc9d7255702d34e5729e4ecb` |
| `adj_window_fibre.json` | `1b29734546306f56ca58fb9b14d2615c4ebd68df8a9977d01f0b08d997ad91a0` |
| `adj_ob_numbers.json` | `02f4eba3aab9fdfa21114c3a7a160eda0867248cc486ca2005c42edbf33780fb` |
| `adj_model_window.json` | `fe18a41dfeec51a392e5fe1e73445be1e49443bccef8677af3be4a0a49758d69` |

The cheapest end-to-end check of C5-ADJ-W and C5-ADJ-SHARP: for P = 1 - T^2 - 7T^3 - 3T^4 + 27T^6 (q = 3), the integer Gram matrices G_N = (3^{min(m,n)} s_{|m-n|}) have inertia (5,0,0) at N = 5 and (5,1,0) at N = 6.

The results directory stays under 1 MB (652 KB).

---

## 9. Next precise steps for a researcher

1. **ML-W0 model case.** Give any definition of H^0 and Dim on the square of the scaling site (or of the CC F_1-curve squared) satisfying (a), (a') and (b), and check (c) on [2^{-1/2}, 2^{1/2}]. Success would be the first instance of positivity on Spec Z coming from a Riemann-Roch/effectivity mechanism rather than from analysis.
2. **ML-C1 at q = 3.**
   - Carry out the identification of ker u(F)_22 with the semilocal Sonin space for F = {inf, 2}, explicitly with prolate functions.
   - Test whether it yields Pos((log 3)/2).
   - In parallel, run an independent Arb replay of Zhu's Pos(0.8), which checks the numerical target but not the mechanism.
3. **EFR, refined model question.** In the class Z_zeta of symmetric zero multisets with N(T) = theta(T)/pi + O(log T), determine the detection horizon L*(delta, T) := inf{L : every Z in Z_zeta with an off-line point at (delta, T) has W_Z indefinite on window L}.
   - C5-ADJ-MODEL (error O(T)) and its sketch refinement (error O(1)) show that no L independent of delta works.
   - Is L* = O(1/delta + log T)?
   - This connects to the C1 detection-horizon campaign. Any EFR for zeta must exploit prime-side structure absent from this class.
4. **Function-field side, quick exact projects.**
   - (i) Prove sufficiency in "g = 1: admissible <=> -q <= a <= q+1" for all q (necessity is proved in Sec. 3.6).
   - (ii) Determine, for each (q,g), the proportion of fakes with N_1 = 2g, i.e. those for which the window (g - 1/2) log q is needed.
   - (iii) Extend E4 to q even (Artin-Schreier characters) and to a_v of higher order.
   - (iv) Quantify the "hidden fake" horizon: first Hasse-Weil violation k* versus log max|beta|. Example (b) has k* = 28 with max|beta| = 1.041.
5. **Deninger.** Compute leafwise H^1 for a twisted version of a 2018-24 Deninger system with no real structure (OB4). Test whether it is computable for spec Z.
6. **Upgrade sources.**
   - Read Weil 1948a/b, Weil 1952, Weil II and Laumon 1987 at L1; they are cited here only via Milne and records.
   - Re-OCR Bombieri 430 to recover the displayed bounds of Sect. II.
   - Check Kurokawa's multiplicity conventions for C5-D1.
   - Search prior art for C5-SK-ASYM and C5-ADJ-MODEL, both expected folklore.
