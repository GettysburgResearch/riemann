# C1-detection-horizons: FINAL (adjudicated)

This is the adjudicator's report. `REPORT.md` (investigator) and `SKEPTIC_REVIEW.md` (skeptic) are kept unchanged as the record. Where this file disagrees with either of them, this file gives the final status and the reason. RH is open. Nothing here claims to prove or disprove it. A "detection horizon" is either a theorem about what a finite computation can imply, or a model statement about a hypothetical zero. Model statements stay model statements.

```text
Status:
  ADJUDICATED EXPLORATORY DOSSIER. No claim about RH or its negation.
  - THEOREM (complete proof given or completed here):
      C1-L1 (Li quadruple identity);
      C1-L2 (RH(T), T>=100  =>  lambda_n > 0 for n <= T^2). The STATEMENT is Oesterle 2000, Prop. 2
        (unpublished), reported by Voros (arXiv:1703.02844, eq. (13)). The PROOF here is complete and independent;
        the adjudicator wrote out its Rosser tail bounds;
      C1-N1 (Nyman-Beurling floor for an off-line zero pair) and Corollary N2;
      C1-ADJ-MONO (real-rootedness of Jensen polynomials is monotone in the degree; classical).
  - NUMERICAL-RIGOROUS (Arb): the exact Jensen thresholds of Farmer's model functions. The X_10 threshold
    (real-rooted for d <= 119, non-real for d >= 120) now has three independent certified implementations.
  - IMPORTED (L1 unless marked): Platt-Trudgian T0; GORTTW Thm 1.2; Buthe and Johnston psi/pi horizons;
    PT21 Cor. 2 (Lambda <= 0.2); Burnol and BDBLS liminf; Morrill-Platt Thm 13.
  - HEURISTIC / NUMERICAL-NONRIGOROUS: every single-defect detection scale, the Jensen-heat bridge, and the
    de Bruijn-Newman collapse model.
  - PROPOSITION-PROOF-SKETCH: C1-L4 (T^2 log T barrier); C1-D3 (Nicolas implication horizon).
  One sentence is REFUTED: "de Bruijn-Newman has no finite RH-implication" (in C1-T0). PT21 Cor. 2 is the
  counterexample.
  Evidence level of this adjudication:
  - L2 for C1-L2, C1-N1, C1-J3/J4 (re-derived or recomputed here);
  - L1 for the primary texts re-read here: PT21; Voros 1703.02844; Johnston 2109.02249; Farmer 2008.07206;
    GORTTW 1910.01227; Morrill-Platt 1809.10813; Burnol math/0103058;
  - L0+ (abstract only) for Mossinghoff-Trudgian-Yang 2212.06867 and Sra 2611.02944.

Scope:
  zeta only. Families:
  (a) Keiper-Li lambda_n;
  (b) Jensen polynomials (GORZ "even" J^{d,n} for Xi; Farmer's classical J^{d,0} for the toy X_j);
  (c) Nyman-Beurling / Baez-Duarte d_N;
  (d) explicit-formula families: Schoenfeld psi/theta/pi, Nicolas/Robin/Lagarias, Mertens, Riesz/Baez-Duarte c_k;
  (e) the de Bruijn-Newman constant Lambda.
  Hypothetical defect: one quadruple {rho0, conj rho0, 1-rho0, 1-conj rho0}, rho0 = 1/2+delta+iT,
  0 < delta < 1/2, all other zeros as stated per claim.

Exact sources or dependencies:
  Per claim, in Section 2. Primary texts re-read by the adjudicator (pdf sha256, first 8 hex digits):
  - Platt-Trudgian, arXiv:2004.09765 (3362f66a): Thm 1, Cor. 1, Sec. 3.2, Sec. 3.4, Cor. 2;
  - Voros, arXiv:1703.02844 (669fb5ad): eqs. (13), (17), (18);
  - Johnston, arXiv:2109.02249v2 (5bc9cafa): abstract, Thm 3.2, (3.19)-(3.20) and iteration;
  - Farmer, arXiv:2008.07206v2 (ad0d5507): (2.2), Sec. 4.2, Table 4.1;
  - GORTTW, arXiv:1910.01227 (f203487a): definition of RH_m(T), Thm 1.2, Cor. 1.3;
  - Morrill-Platt, arXiv:1809.10813v4 (2214cba1): Lemma 5, Thm 13;
  - Burnol, arXiv:math/0103058 (999f05d5): Thms 1.2, 1.3.
  Abstracts via the arXiv API, 2026-11-17: 2212.06867, 2611.02944, 2610.38870, 2105.05386, 1206.6973.
  Zeros: EXP-0001 (first 100000 ordinates, Arb), used by the investigator and the skeptic.

What was actually run:
  - Investigator: 9 scripts. Skeptic: 8 scripts (see their files).
  - All 9 investigator and 8 skeptic output hashes were re-verified by the adjudicator; all match.
  - Adjudicator: 2 new scripts in experiments/code/C1-detection-horizons/adjudicator/, 1 core:
    (i)  adj_numbers.py: mpmath, 50 digits, 0.13 s. Li index at T0; the T^2 log T barrier constant; THEOREM L1
         tail bounds and margin; N1 floor and its second-order term; Buthe and Johnston horizons at T0;
         gap-lattice t_c(T0, delta); Nyman-Beurling and Nicolas numbers at T0.
    (ii) adj_farmer_x10.py: Arb, 4000 bits, 103 s. Third independent certification of the X_10 Jensen threshold:
         partial-fraction coefficients, certified sign changes, and a complex Krawczyk test.
  - Literature re-checks: arXiv API queries for newer verification heights, Jensen/de Bruijn-Newman prior art,
    and Nicolas finite-range prior art.

Smallest remaining gap:
  (a) No error-controlled theorem links the Jensen degree to the de Bruijn-Newman time (C1-J2 is heuristic).
  (b) No explicit "RH(T) => Nicolas/Robin for x <= X(T)" theorem exists (C1-D3 is a leading-order sketch). So
      the Robin computations are uninformative beyond T0 only heuristically, not as a theorem.
  (c) Every single-defect horizon is a model statement. A configuration of several defects with adversarial
      phases could fail earlier (C1-L4).
  (d) The statement whose failure would invalidate the T0 table is Platt-Trudgian's Thm 1 (RH up to
      3 000 175 332 800). The statement whose failure would invalidate C1-L2 is Rosser's N(T) bound
      (Section 3.1). Both are IMPORTED.
```

---

## 1. How the disagreements were resolved

| # | Point | Resolution | Basis |
|---|---|---|---|
| 1 | C1-0: source of the zero-free-region constant 5.558691 | **Skeptic upheld.** 5.558691 is Mossinghoff-Trudgian-Yang 2022 (arXiv:2212.06867, abstract). PT21 Sec. 3.2 quotes 5.573412 (Mossinghoff-Trudgian 2015). delta_max(T0) = 0.4937382 (MTY) vs 0.4937548 (MT), a fifth-digit effect. | Primary texts; adj_numbers (a). |
| 2 | C1-L2: novelty of "RH(T) => lambda_n >= 0, n <= T^2" | **Skeptic upheld.** Voros 1703.02844 eq. (13) states it verbatim and attributes it to Oesterle [2000, Prop. 2], unpublished. "Possibly new in this explicit form" is withdrawn. The investigator's proof is complete. The adjudicator completed its only sketched step, the Rosser tail integrals (Sec. 3.1). Strict positivity for T >= 100 is a minor addition. | Voros text lines 181-185; adj_numbers (c). |
| 3 | C1-L3: accuracy of the leading formula (T^2/delta) log(T^2/delta) | **Both correct in their own range.** On the investigator's grid (17.6 <= T <= 7e4), n*/lead is 1.19-1.43. At T0 it is 1.110-1.118 (adjudicator: 1.1100, 1.1129, 1.1161, 1.1174, 1.1184 for delta = 0.001 ... delta_max). The claim text must give the range. The 60/63 trend-surrogate cases must be disclosed in the claim itself. The skeptic's direct sums reproduce n* exactly in 8 cases. | adj_numbers (a); sk_li_defect.json. |
| 4 | C1-L4: constants of the T^2 log T barrier | **Clarified.** For one quadruple with delta -> 1/2 just above T, the amplitude-crossing index is n = c(T) T^2 log T, with c(T) = 5.84 (T=100), 5.44 (1e3), 4.53 (T0), 4.10 (1e100), so c(T) -> 4. The skeptic's stress model (all zeros above T at beta = 1-1e-12) fails 10-18% earlier: 5.24 at T=100, 4.69 at T=150. That matches the sketch: the positive side (c < 2) is reachable only against adversarial phases. The sketch status is kept. | adj_numbers (b); sk_li_theorem.json (E). |
| 5 | C1-J2: "<0.3% agreement in 24 cases" | **Skeptic upheld.** dbn_jensen.json Part C has 20 comparable rows; the 4 rows at T = 300.74 have no partner. Maximum deviation 1.025% (T=17.58, delta=0.45), then 0.40% (T=51.37) and 0.27% (T=100.07). Below 0.3% holds only for T >= 100. Moreover, Part C compares two model calculations: it is an internal consistency check of the change of variables, not a validation against Jensen polynomials of Xi. The only external validation is on Farmer's toy functions (C1-J3), with deviations within 2.6%. "Chasse's bound follows from Lambda <= 1/2" becomes "is heuristically reproduced by". | Recomputed from dbn_jensen.json. |
| 6 | C1-J3: is "first non-real degree" certified for all d? | **Resolved by a theorem.** Real-rootedness of J^{d,0} is monotone in d (C1-ADJ-MONO, Sec. 3.3). So the certified pair (real at D, non-real at D+1) fixes the threshold for all d. The skeptic's caveat ("assumes real-rootedness at all lower d") is discharged. | Proof in Sec. 3.3. |
| 7 | C1-J4: classification of the Farmer discrepancy | **Resolved; aligned with the Observatory's separate L2 audit FND-0002 (`verified_error`, minor).** j=10: three independent Arb certifications give real-rooted at d=119 and a non-real zero at d=120 and d=121, under Farmer's own definition (2.2). The certifications are the investigator's, the skeptic's and the adjudicator's (adj_farmer_x10.json). Farmer's "only real zeros for d <= 118, and for all larger d it has non-real zeros" is false at d=119. j=20: the printed column (4 first real zeros, 749) is exact for moving 9pi/2 and 11pi/2, not the "two zeros closest to 20" of the text, whose maximum is 477. Neither slip affects Farmer's conclusion. The audit F6 confirms the printed j=40 and j=60 values exactly. | adj_farmer_x10.json; audits/L2_flag_audits/F6-farmer-table.md. |
| 8 | C1-E1 and C1-T0: does de Bruijn-Newman have a finite implication horizon? | **Skeptic upheld; one investigator sentence REFUTED.** PT21 Sec. 3.4: Polymath15 Table 1 row 2 gives Lambda <= 0.2 "provided one has shown H > 2.51e12", hence Cor. 2. A model-free consequence follows: any constraint on zeros implied by Lambda <= 0.2 is already implied by RH(2.51e12) plus the unconditional analysis behind Polymath15. So it adds nothing beyond RH(T0) plus unconditional theory. The same holds for the 2026 claim Lambda < 0.156821 (Planat-Raymond; Observatory audit F8, same RH height input). Separately, the model says that no proved or claimed bound >= 0.1013 can exclude a single quadruple above T0. | PT21 lines 199-208; audit F8. |
| 9 | C1-N1: order of the error term | **Skeptic upheld and sharpened.** F = (4 delta/T^2)(1 - c(delta)/T^2 + O(T^-4)) with c(delta) = (1/2+delta)^2 + 5 delta, identified numerically to 6+ digits at T = 1e4 (0.3101, 0.8600, 1.8125, 3.4301 for delta = 0.01, 0.1, 0.25, 0.49). The stated (1 + O(1/T)) is true but weak. | adj_numbers (d). |
| 10 | C1-N2: log N* = 2.1e23 vs "needs log N >~ 4e23" | **Skeptic upheld.** The consistent model figure uses the two-zero floor of THEOREM N1: log N* = beta/F = 2.105e23 at delta_max. The figure 4.21e23 uses the weaker one-zero Corollary N2 and is withdrawn as the headline. | adj_numbers (g). |
| 11 | C1-D1: psi/pi implication horizon at T0 | **Skeptic upheld.** Johnston (arXiv:2109.02249v2, Thm 3.2): if RH holds up to T and (9.06/log log x) sqrt(x/log x) <= T, then all four Schoenfeld bounds hold (psi, theta from x >= 59 or 599; Pi, pi from 59 or 2657). At T = 3e12 this gives x <= 1.10e26 (adjudicator: 1.1020e26; paper: 1.101e26). The Buthe value 2.169e25 is already printed in PT21 Cor. 1. | Johnston and PT21 texts; adj_numbers (e). |
| 12 | C1-D4: "\|M(x)\| <= m sqrt x is not a consequence of RH" | **Skeptic upheld.** This is an unprovable non-implication claim as stated. Replaced by: no such bound is known to follow from RH. Under the linear independence hypothesis for the ordinates (Ingham 1942), M(x)/sqrt x is unbounded, so for each m the bound fails for some x. | Logic; Ingham (recalled, L0). |
| 13 | C1-T0 and C1-IV: Li prior art "(n >~ 1e16-1e18, earlier heights)" | **Skeptic upheld.** Voros 1703.02844 eq. (18) already states n >~ 2 T0^2, "currently implying n >~ 1e25". | Voros text lines 228-232. |

No investigator theorem is refuted. The one REFUTED item is an interpretive sentence in the T0 table (row 8). Withdrawn or rescoped items are listed in Section 6.

---

## 2. Adjudicated claims table

| ID | Short statement | Investigator label | Skeptic verdict | FINAL status |
|---|---|---|---|---|
| C1-0 | RH true up to T0 = 3 000 175 332 800 (first 12 363 153 437 138 zeros); delta_max(T0) = 0.49374 | IMPORTED | upheld w/ corrections | **IMPORTED** (L1 PT21 Thm 1; constant 5.558691 = MTY 2022, L0+) |
| C1-L1 | lambda_n = sum_on-line 2(1-cos n phi_gamma) + sum_quadruples 4[1 - cosh(na) cos(n phi)] | THEOREM | upheld | **THEOREM** |
| C1-L2 | T >= 100 and RH(T) => lambda_n > 0 for 1 <= n <= T^2; RH(T0) => n <= 9.0010e24; RH(317) => n <= 100489 | THEOREM | prior art | **THEOREM** (statement IMPORTED from Oesterle 2000 via Voros 2017; complete independent proof; tails written out in Sec. 3.1) |
| C1-L3 | Single-defect Li sign index n* = X(log X + 2 log log X - log 4 + o(1)), X = 1/a ~ T^2/delta; at T0: 1.19e27 (delta_max) ... 6.43e29 (0.001) | HEURISTIC + NUM | upheld w/ corrections | **HEURISTIC + NUMERICAL-NONRIGOROUS** (leading scale T^2/delta is Voros's; ratio to the leading formula 1.19-1.43 on the grid, 1.110-1.118 at T0) |
| C1-L4 | Exponent 2 optimal for RH(T)+counting arguments; barrier at n ~ (4+o(1)) T^2 log T (single defect); positive side c < 2 | PPS | upheld | **PROPOSITION-PROOF-SKETCH** (constants clarified by adj_numbers (b)) |
| C1-J1 | RH_m(T), d <= floor(T)^2 => J^{d,n} hyperbolic for all n >= m; at T0, d <= 9.0e24 | IMPORTED | upheld | **IMPORTED** (L1 GORTTW Thm 1.2; O'Sullivan fn. 1) |
| C1-J2 | Jensen-heat bridge: d* ~ T^2/(2 t_c^dBN(T,delta)); isolated pair T^2/(4 delta^2); at T0, d* = 4.44e25 (delta_max), 2.26e28 (0.01) | HEURISTIC (possibly new) | upheld w/ corrections | **HEURISTIC** ("possibly new" only as a search-limited label; agreement statistics corrected) |
| C1-J3 | Exact thresholds for Farmer's X_j and bridge predictions within 2.6% | NUM-RIG + NUM-NONRIG | upheld | **NUMERICAL-RIGOROUS** (thresholds; exact for all d by C1-ADJ-MONO) + **NUMERICAL-NONRIGOROUS** (predictions) |
| C1-J4 | Farmer Table 4.1: j=10 off by one; j=20 column is for a different configuration | unresolved_ambiguity | upheld (keep unresolved) | **NUMERICAL-RIGOROUS**; audit classification **`verified_error` (minor, non-load-bearing)**, consistent with FND-0002 |
| C1-E1 | dBN collapse time t_c(T,delta): ~2 delta^2 (isolated), ~4 delta/log(T/2pi) (dense); at T0, max 0.1013 < 0.2 | HEURISTIC + NUM | upheld w/ corrections | **HEURISTIC + NUMERICAL-NONRIGOROUS**, plus the **IMPORTED** model-free fact (PT21 Cor. 2 is derived from RH(2.51e12)) |
| C1-N1 | Off-line pair => \|\|chi - f\|\|^2 >= F for all f in B_lambda; F = (4 delta/T^2)(1+O(1/T^2)) | THEOREM | upheld | **THEOREM** (error term sharpened; second-order coefficient NUMERICAL-NONRIGOROUS) |
| C1-N2 | NB detection scale log N* ~ beta T^2/(4 delta) = 0.011548 T^2/delta; at T0 2.1e23 ... 1.0e25 | HEURISTIC | upheld w/ corrections | **HEURISTIC** (rests on the conjectured BDBLS asymptotic; 4e23 headline withdrawn) |
| C1-D1 | RH(T0) => Schoenfeld bounds for x <= 1.10e26 (Johnston); single-defect x* = 10^29.2 ... 10^1801 | IMPORTED + HEURISTIC | upheld w/ corrections | **IMPORTED** (horizon corrected to 1.10e26) + **HEURISTIC** (defect) |
| C1-D2 | Nicolas/Robin single defect: x* ~ \|rho0(1-rho0)\|^{1/delta} ~ T^{2/delta}; at T0 10^50.5 ... 10^2495 | HEURISTIC + NUM | upheld | **HEURISTIC + NUMERICAL-NONRIGOROUS** |
| C1-D3 | RH(T) => Nicolas for x <~ ((2-beta) pi T/(log(T/2pi)+1))^2 = 4.36e23 at T0 | PPS | upheld | **PROPOSITION-PROOF-SKETCH** (leading order only; error terms missing) |
| C1-D4 | Mertens: single-defect visibility x* ~ 10^20-10^28 at T0, depending on \|zeta'(rho0)\| | HEURISTIC | upheld w/ corrections | **HEURISTIC** (non-implication sentence corrected; threshold 0.5 arbitrary) |
| C1-D5 | Riesz/Baez-Duarte c_k: log k* ~ pi(T - gamma_1)/(2 delta); at T0 9.5e12 | HEURISTIC | upheld | **HEURISTIC** |
| C1-T0 | Translation table at T0 | THEOREM/IMPORTED + HEURISTIC | upheld w/ corrections | **Mixed, as corrected in Sec. 4**; the sentence "dBN has no finite RH-implication" is **REFUTED** |
| C1-IV | Which published computations are uninformative beyond T0 | Mixed | upheld w/ corrections | **Mixed, as corrected in Sec. 5** |
| C1-ADJ-MONO | J^{d,0} real-rooted => J^{d-1,0} real-rooted (any real entire f; also even Jensen) | (new) | (new) | **THEOREM** (classical; proof in Sec. 3.3; also proved in audit F6) |
| C1-ADJ-X10 | J^{d,0}_{X_10,cl} real-rooted for d <= 119 and non-real for d >= 120 | (new) | (new) | **NUMERICAL-RIGOROUS** (third implementation) |
| C1-ADJ-DBN | No dBN bound proved or claimed through 2026-11-17 can exclude a single quadruple above T0 | (new) | (new) | **HEURISTIC** (model threshold 0.1013) + **IMPORTED** (derivation from RH(T0)-type input) |
| C1-ADJ-LOCAL | Contrast: Polya-frequency and Laguerre criteria have horizons linear in the height or zero index (Sra 2026) | (new) | (new) | **IMPORTED (L0+, unrefereed)**; pointer only |

### 2a. Notes on individual claims (only where the final wording differs from REPORT.md)

- **C1-0.** Final wording: "Every nontrivial zero with 0 < gamma <= T0 = 3 000 175 332 800 has real part 1/2 (PT21 Thm 1; the lowest 12 363 153 437 138 zeros)." delta_max(T0) := 1/2 - 1/(R log T0) caps the tables, with R = 5.558691 (MTY 2022, classical-region constant, |t| >= 2). MTY's abstract says its intermediate-range bounds give a larger zero-free region for 3e12 <= |t| <= exp(64.1). So the true cap at T0 is slightly smaller. Every single-defect minimum in Sec. 4 is then a lower bound for the true minimum (the conservative direction). An arXiv API search on 2026-11-17 found no newer published rigorous height. Sra 2611.02944 (Nov 2026) still uses "about 3·10^12".
- **C1-L2.** Statement credit: Oesterle 2000, Prop. 2 (unpublished typescript, not accessed), as stated in Voros 1703.02844 eq. (13), 1602.03292 Sec. 1.2 and 2204.01036. Corollary (ii) needs RH only up to height 317, i.e. for about 148 zeros. That is classical, and it is also certified inside the Observatory by EXP-0001 (Arb isolation plus Turing count). So Johansson's rigorous signs of lambda_1, ..., lambda_100000 carry no information beyond height 317. That is a THEOREM, not a heuristic.
- **C1-L3.** Required disclosure: in 60 of 63 grid cases lambda^RH_n was replaced by the RH trend plus a fitted offset of 1.767. In 8 cases, 5 of them surrogate-only, the skeptic's direct sums over all 100000 zeros plus a smooth tail give the identical n*. At large T the replacement is immaterial. The amplitude 4 cosh(na) grows by a relative ~2 pi T a per phase period (0.3% at T = 1000, delta = 0.45). That is several orders of magnitude above the relative size of the dropped fluctuation (below 1e-6 there; the skeptic bounds the deviation from the trend by 134 in every window).
- **C1-J2.** Normalization: GORZ/GORTTW even Jensen polynomials J^{d,0}(X), with X <-> z^2 for Xi(z). Height T is in the Xi variable (zeros of Xi at gamma). t_c is in the Polymath normalization of H_t, where a quadruple gives zeros of H_0 at 2T +- 2i delta. The bridge's ingredients (Jensen multiplier sequence ~ exp(-k^2/(2d)), Gaussian multiplier, Polya) are classical. The searches re-run here (arXiv API: "Jensen polynomials" AND "de Bruijn"; AND heat; AND Riemann) found no statement of the degree-to-dBN-time map. "Possibly new" stands only as a search-limited label. As a heuristic consistency check: with t_c <= Lambda_dB <= 1/2 (de Bruijn) the bridge gives d* >= T^2, which is exactly the Chasse/GORTTW horizon. Farmer's toy data fit the same picture: certified maxima d_max ~ 1.19 j^2 for j = 10, 20 (alt), 40, 60 (audit F6).
- **C1-J3.** Certified first non-real degrees and bridge predictions:

  | Case | Predicted | Certified first non-real d | Deviation |
  |---|---|---|---|
  | X_10 | 119.63 | 120 | -0.31% |
  | X_20 (9pi/2, 11pi/2) | 769.40 | 750 | +2.59% |
  | X_20 (11pi/2, 13pi/2) | 480.72 | 478 | +0.57% |
  | X_40 | 1891.89 | 1898 (F6) | -0.32% |
  | X_60 | 4245.1 | 4243 (F6) | +0.05% |

- **C1-E1.** The adjudicator's closed-form quadrature reproduces t_c(T0, delta) = 1.9932e-4, 0.015325, 0.051619 and 0.101298 for delta = 0.01, 0.1, 0.25 and delta_max. Three implementations now agree. Inherited caveat from audit F8: the upper anchor Lambda <= 1/5 rests on Polymath15 Table 1 row 2, whose canopy step Polymath describes as one they "expect to be able to verify". That is a documentation-level ambiguity in a refereed input.
- **C1-N2.** Under RH, BDBLS (Burnol Thm 1.2) and Burnol (Thm 1.3) give liminf_{lambda->0} D(lambda)^2 log(1/lambda) >= sum m_rho^2/|rho|^2 >= beta = 2 + gamma_E - log 4 pi = 0.0461914. Burnol notes the statement is trivial if RH fails. Hence, conditionally on RH and only for sufficiently large N (non-effective), any length-N certificate with ||chi - f||^2 < F needs log N > (beta - eps)/F. The finite-N model D^2 ~ beta/log N + F in the defect world is an assumption (no synthetic d_N was run).
- **C1-D1.** The single-defect claim "isolated pi(x) values up to ~1e29 cannot reveal a quadruple above T0" needs delta >= 0.49742 > delta_max(T0). Its status is HEURISTIC. The value pi(10^29) itself was recalled, not verified (L0).
- **C1-D2 and C1-D3.** Morrill-Platt Thm 13 (Robin for 5040 < n <= 10^(10^13.11485)) is a direct interval-arithmetic run of Briggs' algorithm. The largest prime in the last colossally abundant number is 29 996 208 012 611, so log n ~ 3.0e13. It is not derived from RH(T). No theorem currently says RH(T0) implies it. Hence "uninformative beyond T0" is HEURISTIC for Robin, by two independent heuristics: the sketch horizon 4.4e23 (C1-D3) and the defect horizon 10^50.5 (C1-D2).

### 2b. Adjudicator additions

- **C1-ADJ-MONO (THEOREM, classical).** See Sec. 3.3.
- **C1-ADJ-X10 (NUMERICAL-RIGOROUS).** Method, different from both earlier implementations:
  - Taylor coefficients of X_10(sqrt u) by exact partial fractions of P(u)/Q(u), geometric expansion, and a Cauchy product with cos(sqrt u), in Arb at 4000 bits. Check against the closed form at z = 1: 0.74284833639056918494 for both.
  - R_d(u) = sum_k d!/(d-2k)! c_k u^k, so that J^{d,0}(z) = R_d(z^2).
  - Real-rooted: deg R_d certified sign changes on [0, inf), at d = 117 (58/58), 118 (59/59) and 119 (59/59).
  - Non-real: a complex Krawczyk box of half-width ~1e-34 |Im u0|, strictly self-mapped and disjoint from the real axis. Certified at d = 120 (u0 = 0.0069814102077352036289 + 0.00011115231226355949897 i) and d = 121.
  - The d = 120 root agrees with the skeptic's certified ball to all printed digits.
- **C1-ADJ-DBN (HEURISTIC + IMPORTED).** Claimed bounds below PT21's 0.2, as classified by the Observatory's audit F8 (2026-11-17):
  - Planat-Raymond 0.156821 (unrefereed; no issue found in the inspected portion);
  - Raymond 0.149396; Gordon 0.158; Mosaic 0.1875, 0.16 and 0.1595; Kornaus 0.172422; Gomila 0.1787854; Planat 0.1732 and 0.17795 (all unrefereed);
  - conditional: 0.148612, 0.13963, 0.107965.

  Every one of these is above the model threshold max_delta t_c(T0, delta) = 0.1013. So even if all were correct, none would exclude a single quadruple above T0 in the gap-lattice model. PT21's bound and the principal 2026 claim (Planat-Raymond) take their RH input at height <= T0, so they add nothing beyond RH(T0) plus unconditional theory. The RH input of the other claims was not checked here.
- **C1-ADJ-LOCAL (IMPORTED, L0+ abstract only, unrefereed, Nov 2026).** Sra, arXiv:2611.02944. From RH up to ~3e12: the densities with Laplace transforms 1/xi(1/2+sqrt s) and 1/Xi are PF_k for k = 1 810 540 931 075. Conversely, PF_k implies that all zeros below the (k+2)-nd lie on the line. Also, RH(T) implies the generalized Laguerre inequalities L_n[Xi](x) >= 0 of every order n for |x| <= T - 1/2. These criteria are local: their horizons are linear in the height or the zero index, the opposite extreme from the T^2 dispersion of Li and Jensen. Recorded as a pointer for a future campaign, not reviewed.

---

## 3. The most useful precise statements

Notation: zeros rho = beta + i gamma counted with multiplicity. RH(T) means: every zero with 0 < gamma <= T has beta = 1/2. delta = beta - 1/2.

### 3.1 Li implication horizon (THEOREM; statement due to Oesterle 2000, Prop. 2)

**Statement.** Let lambda_n = sum_rho [1 - (1 - 1/rho)^n], summed symmetrically. If T >= 100 and RH(T) holds, then lambda_n > 0 for every integer 1 <= n <= T^2.

In particular:
- RH(T0) implies lambda_n > 0 for n <= 9.00105e24;
- RH(317) implies lambda_n > 0 for n <= 100489.

**Proof.** This is the investigator's proof, re-checked by the skeptic. The tail step is completed here.

1. *Identity (C1-L1).* With z_rho = 1 - 1/rho = r e^{i phi}, the partner zero satisfies z_{1-conj rho} = r^{-1} e^{i phi}. So the pair (rho, 1 - conj rho) contributes 2[1 - cosh(na) cos(n phi)] after adding conjugates, where a = |log r|.
2. *Lemma A* (0 < beta < 1, gamma >= 14). With u = 2 delta/(beta^2 + gamma^2): a = -(1/2) log(1 - u) <= delta/((1/2 - delta)^2 + gamma^2) <= delta/gamma^2. Also phi = arctan(beta/gamma) + arctan((1 - beta)/gamma) lies in [(1/gamma)(1 - 1/(3 gamma^2)), 1/gamma].
3. *Lemma B.* For 0 <= y <= 1.1 and 0 <= x <= 0.5001: 1 - cosh x cos y >= 0.4496 y^2 - 0.5639 x^2. This holds because (1 - cos y)/y^2 >= 0.45157 and (cosh x - 1)/x^2 <= 0.51051. For all x, y: 1 - cosh x cos y >= -(cosh x - 1).
4. *Regime II* (gamma >= max(T, n)). Here n phi <= 1 and na <= 0.5/gamma, so each zero contributes >= 0.447 n^2/gamma^2.
5. *Regime I* (T < gamma < n, possible only if n > T). Here na <= T^2 * 0.5/gamma^2 < 0.5, so each zero contributes >= -0.5639 (na)^2 >= -0.141 n^2/(gamma^2 - 1)^2.
6. *Zeros with gamma <= T* lie on the line and contribute 2(1 - cos n phi) >= 0.
7. *Assembly.* lambda_n >= 0.894 n^2 sum_{gamma >= max(T,n)} gamma^-2 - 0.282 n^2 sum_{T < gamma < n} (gamma^2 - 1)^-2.
8. *Tails* (completed here). Let R(t) = 0.137 log t + 0.443 log log t + 1.588 (Rosser 1941, valid for t >= 2) and M(t) = (t/2 pi) log(t/(2 pi e)) + 7/8. For t >= T >= 100, R(t) <= R(T) + 0.58 log(t/T). Stieltjes integration by parts gives:
   - (T1) sum_{gamma>T} gamma^-4 = int_T^inf 4t^-5 (N(t) - N(T)) dt <= (log(T/2pi) + 1/3)/(6 pi T^3) + (2R(T) + 0.145)/T^4 <= (2/(3 pi T^3))(log(T/2pi) + 1/3).
   - (T2) sum_{gamma>=n} gamma^-2 >= (log(n/2pi) + 1)/(2 pi n) - (2R(n) + 0.29)/n^2 >= log(n/2pi)/(10 pi n), for n >= 100.

   The last inequalities in (T1) and (T2) reduce to 2pi(2R(T) + 0.145) <= T(log(T/2pi) + 1/3) and to n(0.8 log(n/2pi) + 1)/(2pi) >= 2R(n) + 0.29. Both hold at 100 with ratios above 8 and stay true for larger arguments, since the right side grows like T log T and the left side like log T. Numerically, the rigorous U4 is <= 0.34 of the claimed bound and the claimed L2 is <= 0.20 of the rigorous lower bound, for T in [100, T0] (adj_numbers (c)).
9. *Conclusion.* For n <= T the negative sum is empty. For T < n <= T^2, (T2) is decreasing in n, so the claim reduces to 0.0894 T log(T/2pi) > 0.1881(log(T/2pi) + 1/3). The margin is 24.16 at T = 100 and increasing. Strictness holds because Regime II always contains infinitely many zeros. ∎

### 3.2 Nyman-Beurling floor (THEOREM N1, with Corollary N2)

**Setting.** L^2(0, inf), chi = 1_(0,1], B_lambda = span{t -> {theta/t} : lambda <= theta <= 1}. Báez-Duarte's d_N uses the subspace with theta = 1/k, k <= N.

**Statement.** If rho0 and conj rho0 are zeros with Re rho0 = 1/2 + delta > 1/2, then for every lambda in (0, 1] and every f in B_lambda,

  ||chi - f||^2 >= F := a* H^-1 a - |b* H^-1 a|^2/(1 + b* H^-1 b),

where H_jk = 1/(rho_j + conj rho_k - 1), a_j = 1/rho_j, b_j = 1/(rho_j - 1), for rho_1 = rho0, rho_2 = conj rho0.

**Proof sketch** (re-derived by the skeptic and the adjudicator).
- Split g = chi - f at t = 1. On (1, inf), g = -C/t with C = sum c_k theta_k.
- Mellin at a zero gives ghat_1(rho_j) = a_j - C b_j = <g_1, t^{conj rho_j - 1}>_{L^2(0,1)}.
- G_jk = <e_k, e_j> = H_jk, so min ||g_1||^2 = v* H^-1 v.
- Then minimize (a - Cb)* H^-1 (a - Cb) + |C|^2 over complex C.

**Size of F.** F >= 2 delta/(|rho0|^2 (1 + 2 delta/|rho0 - 1|^2)) (one-zero form). Also F = (4 delta/T^2)(1 - ((1/2 + delta)^2 + 5 delta)/T^2 + O(T^-4)). The second-order coefficient is identified numerically, not proved.

**Corollary N2.** A certified ||chi - f||^2 <= eps excludes every pair with eps < F(rho), in particular every zero with 2 beta - 1 > eps |rho|^2 (1 + (2 beta - 1)/|rho - 1|^2).

### 3.3 Jensen polynomials: the imported horizon and a monotonicity lemma

- **IMPORTED (GORTTW Thm 1.2, L1).** For m >= 0, RH_m(T) means: all zeros of xi^(m)(s) with |Im s| <= T have real part 1/2. If RH_m(T) holds and d <= floor(T)^2, then the GORZ polynomial J^{d,n}(X) is hyperbolic for all n >= m. For m = 0 this recovers Chasse 2013 Thm 1.8. With T0: d <= 9.0e24 (O'Sullivan 2007.13582, fn. 1).
- **THEOREM (C1-ADJ-MONO, classical).** Let f(z) = sum alpha(j) z^j/j! be real entire with alpha(0) != 0, and J^{d}(z) = sum_{j<=d} C(d,j) alpha(j) z^j. If J^d has only real zeros, so does J^{d-1}.

  *Proof.* Put P(z) = z^d J^d(1/z) = sum_j C(d,j) alpha(j) z^{d-j}. Then P'(z) = sum_j C(d,j)(d-j) alpha(j) z^{d-j-1} = d sum_j C(d-1,j) alpha(j) z^{d-1-j} = d z^{d-1} J^{d-1}(1/z).
  - If J^d is real-rooted, P is real-rooted: its zeros are the reciprocals of those of J^d, plus 0 when the degree drops.
  - By Rolle, P' is real-rooted.
  - The nonzero zeros of J^{d-1} are reciprocals of nonzero zeros of P', hence real. ∎

  The same argument applies verbatim to J^{d,n} (replace alpha(j) by alpha(j+n)) and to the even polynomials. Consequently, a certified pair (real-rooted at D, non-real zero at D+1) determines real-rootedness for every d.
- **HEURISTIC (C1-J2).** d*(T, delta) ~ T^2/(2 t_c(T, delta)) for the even J^{d,0} of Xi near height T. For an isolated pair this is T^2/(4 delta^2).

### 3.4 Explicit-formula families

- **IMPORTED (Johnston 2021/22, Thm 3.2, L1).** Suppose RH holds for 0 < Im rho <= T and (9.06/log log x) sqrt(x/log x) <= T. Then:
  - |psi(x) - x| < sqrt(x) log^2 x/(8 pi) for x >= 59;
  - the same bound for theta for x >= 599;
  - |Pi(x) - li(x)| < sqrt(x) log x/(8 pi) for x >= 59;
  - the same bound for pi for x >= 2657.

  At T = 3e12 this covers x <= 1.10e26. The earlier Buthe condition 4.92 sqrt(x/log x) <= T gives 2.169e25 (PT21 Cor. 1).
- **HEURISTIC (C1-D2).** Nicolas' criterion is c(x) > 0, where c(x) = log prod_{p<=x}(1 - 1/p)^-1 - gamma_E - log log theta(x). The leading explicit formula is sqrt(x) log x c(x) = 2 + sum_rho x^{rho - 1/2}/(rho(1 - rho)) + o(1). Under RH the sum lies in [-beta, beta], with beta = 2 + gamma_E - log 4 pi = 0.0461914. A single quadruple breaks the criterion at x* ~ |rho0(1 - rho0)|^{1/delta} ~ T^{2/delta}. For Robin and Lagarias, log n* ~ x*.

### 3.5 de Bruijn-Newman

- **IMPORTED (PT21 Cor. 2, from Polymath15 Table 1 row 2).** RH verified to H > 2.51e12 implies Lambda <= 0.2.
- **Consequence (logic).** Lambda <= 0.2 adds no constraint on zeros beyond RH(T0) plus unconditional theory.
- **HEURISTIC (C1-E1).** A quadruple at (T, delta) keeps H_t non-real-rooted until t_c(T, delta) = int_0^{2 delta} 2y dy/(2 + 8 y^2 S(y)), where S(y) = (pi/(2ys)) tanh(pi y/s) - 1/(y^2 + s^2/4) and s = 4 pi/log(T/2 pi).

### 3.6 Structural summary (HEURISTIC)

**Implication horizons.** Every family with a finite implication horizon has one of size about T^2, up to logarithms:
- Li: n <= T^2;
- Jensen (even): d <= T^2;
- psi/pi: x ~ T^2 (log x)(log log x)^2/82;
- Nicolas (sketch): x ~ T^2/log^2 T.

The exception is the PF/Laguerre criteria (C1-ADJ-LOCAL), which are local.

**Single-defect detection.** The gap between implication and single-defect detection has two shapes:
- *Index families.* Li is T^2/delta times a logarithm. Jensen is T^2/(2 t_c). Nyman-Beurling (in log N) is T^2/delta. So the gap is a polynomial factor in 1/delta and log T.
- *Explicit-formula families.* psi/pi and Nicolas/Robin have log x* ~ (c/delta) log T against log x ~ 2 log T. So the gap is a power 1/delta >= 2 in x.

---

## 4. Table (iii): what a finite computation must exceed to say anything new beyond T0 = 3 000 175 332 800

Single-defect columns are model statements. delta_max(T0) = 0.49374. The "minimum over delta" is attained at delta_max, where the scales are smallest.

| Family (index) | Implication horizon at T0: already a consequence of RH(T0) | Status | Single-defect first-failure scale at T0: delta_max / 0.25 / 0.1 / 0.01 | Status |
|---|---|---|---|---|
| Keiper-Li lambda_n (n) | lambda_n > 0 for all n <= T0^2 = 9.0010e24 | THEOREM (Oesterle's statement; Sec. 3.1) | 1.186e27 / 2.367e27 / 6.004e27 / 6.217e28 | HEURISTIC |
| Jensen, GORZ even J^{d,n} (d) | hyperbolic for all n >= 0 and d <= floor(T0)^2 = 9.0e24 | IMPORTED (GORTTW) | 4.44e25 / 8.72e25 / 2.94e26 / 2.26e28 | HEURISTIC (bridge) |
| Schoenfeld psi, theta, Pi, pi (x) | the four Schoenfeld bounds for x <= 1.10e26 | IMPORTED (Johnston) | 10^29.23 / 10^60.24 / 10^159.0 / 10^1801 | HEURISTIC |
| Nicolas (x) / Robin, Lagarias (log n) | no theorem; sketch x <~ 4.36e23 | PPS (C1-D3) | 10^50.54 / 10^99.82 / 10^249.5 / 10^2495 | HEURISTIC |
| Nyman-Beurling / Baez-Duarte d_N (log N) | none | — | 2.11e23 / 4.16e23 / 1.04e24 / 1.04e25 | HEURISTIC (BDBLS asymptotic assumed) |
| Mertens M(x) (x) | none known | — | 10^20-10^28 at delta_max for \|zeta'(rho0)\| = 1e-2 ... 1e2 (visibility level 0.5 arbitrary) | HEURISTIC |
| de Bruijn-Newman Lambda (proved upper bound) | Lambda <= 0.2 (from RH to 2.51e12) | IMPORTED (PT21 Cor. 2) | needs a proved bound below t_c = 0.1013 / 0.0516 / 0.0153 / 1.99e-4 | HEURISTIC |
| Riesz / Baez-Duarte c_k (log k) | none | — | 9.5e12 / about 1.9e13 / about 4.7e13 / about 4.7e14 (pi T0/(2 delta)) | HEURISTIC |

Reading guide:
- **A computation entirely inside the implication column is a logical consequence of RH(T0)** (rows 1-3 rigorously; row 7 relative to unconditional theory). It cannot carry information beyond T0.
- **A computation below the single-defect column** cannot, in the model, detect any single quadruple above T0. Multi-defect conspiracies could lower the Li column by at most a bounded factor, heuristically (C1-L4: the c(T) constant moves from about 4.5 toward 2 at T0 only against adversarial phases).

---

## 5. Item (iv): published large computations, final classification

| Computation | Final classification | Status |
|---|---|---|
| lambda_n for n <= 1e5 (Johansson 2015, rigorous; Keiper, Maslanka, Coffey for smaller n) | **Implied by RH(317)**, hence by the classical verification of the first ~148 zeros | THEOREM (C1-L2 (ii)) |
| Jensen hyperbolicity: Chasse d <= 2e17, GORTTW d <= 9.36e20, O'Sullivan d <= 9e24 | **Derived from RH(T)** by Thm 1.2; d <= 3 for all n and large-n results are unconditional | IMPORTED |
| psi, theta, pi tables and Schoenfeld-type checks for x <= 1.10e26 | **Implied by RH(T0)** (Johnston) | IMPORTED |
| Isolated pi(x) for 1.10e26 < x <~ 1e29 | Formally not implied, but cannot reveal a single quadruple above T0 (needs delta >= 0.4974 > delta_max) | HEURISTIC |
| Robin/Lagarias to 10^(10^13.11485) (Morrill-Platt), 10^(10^10) (Briggs) | **Not proved to be implied by RH(T0)**, because no explicit Nicolas/Robin implication theorem exists. Uninformative by both heuristics (log n ~ 3e13 against 4.4e23 and 10^50.5) | HEURISTIC |
| Mertens M(x) for all x <= 1e16 (Hurst); isolated larger values cited by the investigator | No implication relation exists. Uninformative unless \|zeta'(rho0)\| <~ 1e-4 (arbitrary visibility level) | HEURISTIC |
| Nyman-Beurling d_N numerics; Riesz/Baez-Duarte c_k up to k ~ 1e9-1e10 (probes T <~ 21.5) | Uninformative | HEURISTIC |
| Lambda <= 0.22 (Polymath15), Lambda <= 0.2 (PT21), 2026 claims down to 0.1568 (unconditional) or 0.108 (conditional) | **No information beyond RH(T0) plus unconditional theory** (PT21 Cor. 2 logic). All are also above the model threshold 0.1013 | IMPORTED + HEURISTIC |
| Direct zero verifications in windows above T0 (Odlyzko, Gourdon, Bober-Hiary) | Not criterion computations. They inform only the windows they cover, as far as they are rigorous (not audited here; L0 pointers) | — |

No published large criterion computation found in this campaign is informative beyond T0, except trivially in the formal sense for isolated pi(x) above 1.1e26.

---

## 6. Negative results, withdrawn and rescoped statements

**Withdrawn or refuted wording** (investigator text replaced by Sec. 2):
1. C1-L2: "possibly new in this explicit form". Withdrawn; the statement is Oesterle's.
2. C1-J2: "agrees to <0.3% (24 cases)". Withdrawn; correct figure is <= 1.03% in 20 comparable rows. "Chasse's bound follows from Lambda <= 1/2" becomes "is heuristically reproduced by".
3. C1-T0: "Nyman-Beurling, Mertens and de Bruijn-Newman have no finite RH-implication". **REFUTED for de Bruijn-Newman** (PT21 Cor. 2).
4. C1-D1 and C1-T0: psi/pi implication horizon 2.17e25. Superseded by Johnston's 1.10e26.
5. C1-D4: "|M(x)| <= m sqrt x is not a consequence of RH". Withdrawn; replaced by "not known to follow; fails for some x under LI".
6. C1-N2: "excluding anything above T0 needs log N >~ 4e23". Withdrawn as the headline; the consistent figure is 2.1e23.
7. C1-0: Mossinghoff-Trudgian 2015 as the source of 5.558691. Corrected to MTY 2022.
8. C1-IV: "Voros and Lagarias make it for Li ('n >~ 1e16-1e18 needed, with earlier heights')". Corrected: Voros already gives n >~ 1e25 at T0.

**Rescoped:**
- C1-L3 "19-43% low" holds on the grid T <= 7e4 only; it is 11-12% at T0.
- C1-N1 "(1 + O(1/T))" is sharpened to (1 + O(1/T^2)).

**Negative knowledge carried forward** (from REPORT.md and SKEPTIC_REVIEW.md, all confirmed as recorded):
- the tail-tolerance bug in jensen_exact_check.py (superseded output kept);
- the overflow of the truncated w-flow ODE;
- the apparent 36% bridge failure that was a configuration mismatch;
- the inaccuracy of the pure lattice collapse formula for T <= 7e4;
- the grid artefact moving the target T = 300 to T = 546.3;
- the float64 Lemma A artefact (ratio 3.51 at gamma ~ 1e7);
- the 15-minute timeout of the vectorised stress test;
- the memory exhaustion of the unchunked far-zero background.

**New negative knowledge (adjudicator):**
- mpmath `polyroots` at 400 digits with extraprec 4000 on the degree-59/60 X_10 polynomials did not finish in 10 minutes. At 100 digits with extraprec 300 it takes about 15 s per degree and suffices, because the certificates are carried out in Arb anyway.
- `mp.findroot(..., solver='anderson')` fails on the Li amplitude crossing at T0 (residual 1e56). Bisection on [X/2^k, 2^k X] is robust.
- At 50 digits, a = -log|1 - 1/rho0| underflows to 0 for T >= 1e100. The form a = -(1/2) log1p(-2 delta/((1/2 + delta)^2 + T^2)) is required.

**Not run by anyone** (still open):
- synthetic Nyman-Beurling d_N with injected zeros;
- exact Jensen polynomials of a Xi-model (only Farmer's X_j);
- Robin directly at colossally abundant numbers in a defect model;
- full texts of Brown 2005, Chasse 2013 and Oesterle's typescript.

---

## 7. Reproducibility

Environment: Linux x86-64, Python 3.13.18, python-flint 0.9.0 (Arb), mpmath 1.3.0, numpy 2.5.3, scipy 1.18.1. At most 2 cores.

Zero data: `experiments/results/zeros/zeta_zeros_1_100000_arb.tsv.gz` (EXP-0001). The investigator's and skeptic's scripts read the scratchpad copies `.../scratchpad/data/zeros_{1_50000,50001_100000}.tsv`, path set in `common.py`.

```bash
cd /home/user/riemann/research/exploratory/riemann-observatory/experiments/code/C1-detection-horizons
# investigator (outputs in ../../results/C1-detection-horizons/)
python3 exp_li.py              # li_detection.json        0f835aa3...d411d1   ~65 s
python3 exp_dbn_jensen.py      # dbn_jensen.json          d10fb9fc...1be78e   ~445 s
python3 exp_arith.py           # arith_nb.json            ff5f4f58...e83203
python3 exp_T0_table.py        # T0_table.json            0448168e...e9fa39
python3 jensen_exact_check.py  # jensen_farmer_check.json b7afb6e6...97df
python3 jensen_root_certify.py # jensen_root_certify.json 5a15d127...a1677b
python3 farmer_j20_alt.py      # farmer_j20_alt.json      6069733a...963b3
python3 make_tables.py         # tables_C1.md             8331bb23...47b32 (the current file; the REPORT's "pre-regeneration" note is stale)
# skeptic: scripts in skeptic/, outputs in ../../results/C1-detection-horizons/skeptic/ (hashes in SKEPTIC_REVIEW.md Sec. 1)
python3 skeptic/sk_li_defect.py; python3 skeptic/sk_jensen_exact.py; python3 skeptic/sk_T0_numbers.py   # etc.
# adjudicator
python3 adjudicator/adj_numbers.py     # adjudicator/adj_numbers.json    35acfbaf0de771b46d09e7360ad57aae968e2a8b5c3b6c01554fa9c706d78eb2  0.13 s
python3 adjudicator/adj_farmer_x10.py  # adjudicator/adj_farmer_x10.json 4e9d0a5ec0838a30e5925f9472122f80f0b9511f6201fd57e08fff6aace7bff2  103 s
# manifest: results/C1-detection-horizons/adjudicator/manifest_adjudicator.json
```

Code hashes:
- `adj_numbers.py`: 326f7475...0d24.
- `adj_farmer_x10.py`: 4d3184b5...0647.

All 9 investigator and 8 skeptic output hashes were re-verified on 2026-11-17. `sk_j10_gap.txt` (46c8ba25...a112) is not listed in the skeptic's table. Total results directory: 204 KB.

Arb certificates are conditional on the correctness of FLINT/Arb. Everything mpmath produces is non-rigorous high precision.

---

## 8. Next precise steps for a researcher

1. **Li beyond T^2.** Prove "RH(T) implies lambda_n > 0 for n <= c T^2 log T" with an explicit c > 0.
   - The heuristic ceiling for arguments using only RH(T) plus N(t) bounds is c = 2 (adversarial phases).
   - The single-defect barrier is c(T) -> 4, with c = 4.53 at T0.
   - At T0 even c = 1 would push the rigorous horizon from 9.0e24 to about 2.6e26.
2. **Jensen-heat bridge.** Prove an error-controlled comparison: J^{d,0}_ev is hyperbolic near X = T^2 iff H_t is real-rooted near 2T at t = T^2/(2d), up to O(T^3/d^2). A first test case is Farmer's X_j, where certified thresholds exist for j = 10, 20, 40, 60 and the bridge is within 2.6%.
3. **Nicolas/Robin implication theorem.** Prove a Buthe/Johnston-type explicit statement: RH(T) implies Nicolas' inequality for x <= X(T), with X(T) ~ c T^2/log^2 T. This needs the explicit truncated formula for sqrt(x) log x c(x) with all O(1/log x) terms. At T0, any X(T0) >= 3.0e13 would make Morrill-Platt Thm 13 a corollary of PT21.
4. **Nyman-Beurling in a defect world.** Compute d_N with injected zeros at small T, using Vasyunin-type closed forms for the Gram matrix, to test D^2 ~ beta/log N + F. THEOREM N1 gives the exact floor to compare against.
5. **de Bruijn-Newman lower bound from a defect.** Give a rigorous lower bound t_c(T, delta) >= f(T, delta) under explicit hypotheses on the zeros within distance O(1) of T. That would turn "a quadruple implies Lambda >= t_c" into a theorem. Hard part: control of all other zeros.
6. **Primary-source gaps.** Read Brown 2005 (Li-type zero-free regions from finitely many lambda_n), Chasse 2013 Thm 1.8 and, if obtainable, Oesterle's 2000 typescript at L1. Compare Brown's region with the single-defect scale delta >~ C T^2 log N/N.
7. **Local criteria.** Audit Sra arXiv:2611.02944 (unrefereed, Nov 2026). Its PF_k horizon k* = 1.81e12 from RH(3e12) is smaller than N(T0) = 1.24e13 zeros, and its Laguerre horizon is linear in T. Classify it in the same implication/detection framework.
8. **Farmer table.** Per FND-0002, a courtesy note to the author about the j=10 entry (119) and the j=20 configuration is the remaining step. No public wording beyond "minor numerical slips; conclusion unaffected".
