# C1-detection-horizons: independent skeptic review

```text
Status: SKEPTIC REVIEW (exploratory archive). No RH claim. Model-world statements stay model-world.
Scope: the 21 structured claims C1-0 ... C1-IV of REPORT.md (materialized investigator return) and the code
       under experiments/code/C1-detection-horizons/.
Exact sources read for this review (full text unless marked): Platt-Trudgian arXiv:2004.09765; Mossinghoff-Trudgian
       arXiv:1410.3926 (abstract); Mossinghoff-Trudgian-Yang arXiv:2212.06867 (abstract); Voros math/0506326,
       1602.03292, 1703.02844, 2204.01036; Lagarias math/0404394; GORTTW 1910.01227; O'Sullivan 2007.13582;
       Farmer 2008.07206; Buthe 1410.7015; Johnston 2109.02249; Morrill-Platt 1809.10813; zbMATH review of
       Brown 2005 (Zbl id 2208782, L0+).
What was actually run: 7 independent scripts (below); about 15 min CPU in total, at most 2 cores.
Smallest remaining gap: the Jensen-heat bridge (C1-J2) and every single-defect horizon remain heuristic.
       The only complete proofs (C1-L2, C1-N1) check out, but the statement of C1-L2 is Oesterle's (2000).
```

## 0. Summary of verdicts

| Claim | Verdict | One-line reason |
|---|---|---|
| C1-0 | upheld_with_corrections | T0 = 3 000 175 332 800 confirmed (PT21 Thm 1). The constant 5.558691 is Mossinghoff-Trudgian-Yang 2022, not Mossinghoff-Trudgian 2015 (that one is 5.573412). |
| C1-L1 | upheld | Identity re-derived. mpmath check on 200 random zeros, error < 1.1e-35. |
| C1-L2 | prior_art_found | Proof re-checked and correct. The statement "RH(T) implies lambda_n >= 0 for n <= T^2" is Oesterle 2000 (Prop. 2), stated explicitly by Voros 2016/2017/2022. |
| C1-L3 | upheld_with_corrections | All 8 tested n* reproduced exactly by direct sums, including 5 cases that the investigator ran only through the trend surrogate. Leading-order scale n >~ T^2/delta is Voros's. At T0 the leading formula is ~11-12% low, not 19-43%. |
| C1-L4 | upheld | Worst-case stress model (all zeros above T at beta = 1-1e-12) first fails at n = 5.2 T^2 log T (T=100) and 4.7 T^2 log T (T=150). This agrees with a T^2 log T barrier and stays positive far beyond T^2. |
| C1-J1 | upheld | GORTTW Thm 1.2 and Cor 1.3 verbatim. O'Sullivan line 118 gives d <= 9e24. |
| C1-J2 | upheld_with_corrections | ODE derivation re-derived. Stated agreement "<0.3% in 24 cases" is really <=1.03% in 20 comparable cases (4 rows are NaN). "Chasse follows from Lambda <= 1/2" is heuristic only. |
| C1-J3 | upheld | Thresholds 120 / 750 / 478 independently Arb-certified with unrounded ball coefficients and a different coefficient algorithm. Predictions 119.63 / 769.40 / 480.72 / 1891.89 reproduced to 6 digits by an independent z-variable ODE. |
| C1-J4 | upheld | Independent witness for both the j=20 configuration mismatch and the j=10 off-by-one. Keep it in unresolved_findings until the author's convention is checked. |
| C1-E1 | upheld_with_corrections | T0 collapse times reproduced (0.10130 at delta_max). ODE spot checks reproduced exactly; a far-zero background changes them by <= 0.27%. A model-free reason was missing: Lambda <= 0.2 is itself derived from RH up to 2.51e12. |
| C1-N1 | upheld | Proof re-derived line by line (Mellin split, Gram matrix, minimisation over C). F reproduced. The error term is actually O(1/T^2). |
| C1-N2 | upheld_with_corrections | Numbers reproduced. Internal inconsistency: log N* = 2.1e23 (two-zero floor) versus "needs log N >~ 4e23" (single-zero corollary). |
| C1-D1 | upheld_with_corrections | Buthe evaluation reproduced (2.169e25; 1.430e25). Missed prior art: Johnston (2109.02249, Ramanujan J.) uses RH(3e12) to obtain Schoenfeld's pi bound for x <= 1.101e26. |
| C1-D2 | upheld | Explicit formula G = 2 + sum x^(rho-1/2)/(rho(1-rho)) re-derived. T0 values reproduced. |
| C1-D3 | upheld | Sketch reproduced (4.36e23 with the +1 in the tail sum, versus 4.43e23). Correctly labelled as a sketch. |
| C1-D4 | upheld_with_corrections | "|M(x)| <= m sqrt x is not a consequence of RH" is overstated. It is not known to follow and is false under RH+LI (Ingham). The detection threshold 0.5 is arbitrary. |
| C1-D5 | upheld | Residue and Gamma-damping asymptotics re-derived; numbers reproduced (9.54e12; T <~ 21.5). |
| C1-T0 | upheld_with_corrections | Numbers reproduced. Two errors: (a) de Bruijn-Newman *does* have a finite implication horizon (RH(H >= 2.51e12) gives Lambda <= 0.2, PT21 Cor. 2); (b) the pi/psi horizon should be about 1e26 (Johnston), not 2.17e25. The Li implication row is Oesterle's. |
| C1-IV | upheld_with_corrections | Same corrections as C1-T0. The Li conclusion "n >~ 10^25 needed" was already published by Voros, contrary to the report's "(n >~ 1e16-1e18, earlier heights)". |

## 1. Independent computations (code, outputs, hashes)

All code is in `experiments/code/C1-detection-horizons/skeptic/` and all outputs in `experiments/results/C1-detection-horizons/skeptic/`. Environment: Python 3.13.18, numpy 2.5.3, scipy 1.18.1, mpmath 1.3.0, python-flint 0.9.0. Before the review, the investigator's output hashes were re-verified with `sha256sum`; all 9 match REPORT.md.

| Script | What it checks | Runtime | Output sha256 |
|---|---|---|---|
| `sk_li_theorem.py` | C1-L1 identity; Lemma A/B grids; Rosser tail bounds by Stieltjes integration; worst-case stress model | 594 s | `1e4597f80d14f2ef0185081050c1b60d7cb1075d0a78186add06525003aa6720` |
| `sk_lemmaA_mp.py` | Lemma A in 60-digit mpmath (fixes a float64 artifact in part (B) above) | <10 s | `c7c4882088d38fd51f0568095e3c388f38b1a1aee2137e45f022fa2666084359` |
| `sk_li_defect.py` | C1-L3 n* by **direct** zero sums (complex recurrence) in a window around the crossing, with no trend surrogate | 28 s | `2d5bd4812142f2e2b400b96a0148391ee5c2652e405e577d2cb65f9face411b3` |
| `sk_T0_numbers.py` | Every T0-table number, re-derived with different solvers (gap-lattice t_c by ODE on an explicit lattice sum, not the closed-form integral) | 37 s | `8dd88a1247318565be481fe83f67baeb2cfe5af32680f14218bd9c9998d06cc7` |
| `sk_jensen_exact.py` | C1-J3/J4 thresholds: Arb power-series division (not tail sums), ball coefficients kept unrounded, `acb_poly.roots` plus certified sign counting | 131 s | `39ce98c2103f9d7383497b8b0f2bea5180dd875add64f4a6b4c3634afa0a3c0c` |
| `sk_jensen_bridge_ode.py` | C1-J2/J3 predictions, z-variable ODE dz/dtau = 2 z^2 sum 1/(z-z_l) with static outer zeros and analytic tail | 17 s | `0c6a182643bb99b81c253ab1c2776ee87aecb05e65fb5750dcc26986ea087d7c` |
| `sk_dbn_ode.py` | C1-E1 ODE spot checks, with and without the far/mirror zeros as a static background | 51 s | `2d31608bb2d7182e8fd654d9a903e2d78166219f93207be2368923f7e7635221` |

## 2. Claim-by-claim

### C1-0 (IMPORTED) — upheld_with_corrections
- PT21 (arXiv:2004.09765, line 56): "The Riemann hypothesis is true up to height 3 000 175 332 800." Confirmed. PT21 Cor. 2 gives Lambda <= 0.2 provided H > 2.51e12, which is used below.
- **Correction (attribution).** PT21 itself (line 161) states that "the current best value is R = 5.573412 by Mossinghoff and Trudgian". The constant 5.558691 comes from Mossinghoff, Trudgian and Yang, arXiv:2212.06867 (2022), whose abstract also says that for 3e12 <= |t| <= exp(64.1) their intermediate bounds give an even larger zero-free region. The effect on delta_max(T0) is in the 5th digit: 0.493755 (5.573412) versus 0.493738 (5.558691). A better intermediate-range region would lower delta_max slightly, so the single-defect minima in C1-T0 are, if anything, slightly underestimated (conservative direction).
- A brief arXiv search found no newer peer-reviewed rigorous verification height.

### C1-L1 (THEOREM) — upheld
Re-derivation:
- z_rho = (rho-1)/rho, and z_{1-conj rho} = (-conj rho)/(1-conj rho) = 1/conj(z_rho).
- The quadruple then gives 4 - 2(r^n + r^-n) cos(n phi).
- r^2 = 1 - 2 delta/((1/2+delta)^2+T^2).
- On the line, phi_gamma = pi - 2 arctan(2 gamma) = 2 arctan(1/(2 gamma)).
- Absolute convergence of sum Re(1 - z^n) holds because Re(n/rho) = n beta/|rho|^2 >= 0 and the remainder is O(n^2/|rho|^2).

mpmath check (`sk_li_theorem.py` (A)) on 200 random (beta, gamma, n): maximum error 1.1e-35.

### C1-L2 (THEOREM L1) — prior_art_found (mathematically upheld)
**Proof audit.** Each step was re-derived:
- Lemma A is in fact sharper than stated: a <= delta/((1/2-delta)^2+gamma^2) <= delta/gamma^2, and phi = arctan(beta/gamma) + arctan((1-beta)/gamma) <= 1/gamma. In 60-digit mpmath the ratio a/(|beta-1/2|/(gamma^2-1)) stays <= 1 and phi*gamma <= 1, with phi above its lower bound everywhere (`sk_lemmaA_mp.json`). The float64 grid in `sk_li_theorem.json` (B) reports a ratio of 3.51; that is a cancellation artifact of log|z| at gamma ~ 1e7 and is recorded as negative knowledge.
- Lemma B grid: minimum margin 0, attained only at the origin. The constants are conservative: max (cosh x - 1)/x^2 = 0.5105 < 0.5639, and min (1 - cos y)/y^2 = 0.4516 > 0.4496.
- Regime II needs n phi <= n/gamma <= 1, which holds.
- Regime I uses x = n a <= T^2 * 0.5/(T^2 - 1) <= 0.50006. Holds.
- Rosser-based tails, re-done by Stieltjes integration with Rosser's E(t): the rigorous upper bound for sum gamma^-4 is at most 0.339 times the claimed bound, and the claimed lower bound for sum gamma^-2 is at most 0.193 times the rigorous one, for T in [100, 1e13].
- The final inequality holds with a large margin: the scaled margin is >= 1.19 at T = 100 and grows with T.
- Strict positivity follows because Regime II always contains infinitely many zeros.
- The corollaries T0^2 = 9.00105e24 and 317^2 = 100489 are correct.

**Prior art (missed).** The investigator cites Oesterle's typescript as inaccessible. But Voros states the result explicitly, attributing it to Oesterle [2000, Prop. 2]:
- arXiv:1703.02844, eq. (13): "Re rho = 1/2 for all zeros with |Im rho| <= T0 => lambda_n >= 0 for all n <= T0^2".
- arXiv:1602.03292, §1.2: "no lambda_n can go negative as long as n < T0^2 [Oesterle; Biane-Pitman-Yor 2001 §2.3]".
- arXiv:2204.01036, line 353: same statement.

The investigator's proof is an independent, explicit and verified write-up of Oesterle's statement, with strict positivity for T >= 100. It is not a new result, and the note "possibly new in this explicit form" should be dropped.

### C1-L3 (HEURISTIC + NUMERICAL) — upheld_with_corrections
- **Not independent as run.** In 60 of 63 grid cases the investigator's "collision model on 100000 zeros" replaces lambda^RH_n by the trend plus a fitted offset of 1.767. The "mpmath re-check" uses the same surrogate, so the reported n*/n_amp in [1.0000, 1.0085] there is close to an identity check.
- **Independent check** (`sk_li_defect.py`): lambda_n is computed by direct sum over all 100000 zeros (minus the two collided) plus a smooth tail, exactly on a window around the crossing. The first negative n is **identical** to the investigator's n* in all 8 cases:
  - (17.58; 0.45 / 0.2 / 0.1): 6406 / 16016 / 34578
  - (51.37; 0.45 / 0.1): 70361 / 363780
  - (100.07; 0.45 / 0.2): 302437 / 728131
  - (300.74; 0.45): 3246393

  Five of these cases were run by the investigator only with the surrogate. In every case n* - n_amp is smaller than one phase period 2 pi T. The direct lambda^RH minus trend stays within +-134 in every window. lambda_100000 (model) = 462580.016, reproducing the report.
- T0 values reproduced: 1.1859e27 (delta_max), 2.367e27, 6.004e27, 6.217e28, 6.431e29.
- **Correction.** At T0 the ratio n*/[(T^2/delta) log(T^2/delta)] is 1.110-1.118, not 1.19-1.43. The 19-43% range holds only on the tested grid T <= 7e4.
- **Prior art.** Voros (1703.02844, eqs. (17)-(18); 1602.03292, eq. (14)) already gives n >~ T^2/|t| as a necessary detection scale and n >~ 2 T0^2, about 10^25. Only the log refinement X(log X + 2 log log X - log 4) goes beyond Voros, and it is heuristic.

### C1-L4 (PROPOSITION-PROOF-SKETCH) — upheld
Worst-case stress model (`sk_li_theorem.py` (E)): actual ordinates, every zero above T moved to beta = 1 - 1e-12, and the zeros above gamma_100000 dropped (they only add positive Regime-II terms).

| T | lambda_n positive for all n < | = (T^2 log T) times | lambda at T^2 | lambda at T^2 log T | lambda at 2 T^2 log T |
|---|---|---|---|---|---|
| 100 | 241171 | 5.24 | 32531 | 148880 | 242080 |
| 150 | 528862 | 4.69 | 76179 | 263669 | 234855 |

Interpretation:
- Failure occurs at the T^2 log T scale and only 8-16% earlier than the single quadruple at T (n_2 = 2.62e5 and 6.33e5).
- This supports "exponent 2 is optimal for arguments using only RH(T) + zero counting" and is consistent with c < 2.
- Not a proof: the stress model fixes the actual phases; adversarial phases could fail earlier, but still at scale T^2 log T.

### C1-J1 (IMPORTED) — upheld
- GORTTW (1910.01227) lines 64-70: "Theorem 1.2. If RH_m(T) is true and d <= floor(T)^2, then J^{d,n}(X) is hyperbolic for all n >= m", and Cor. 1.3 (9.36e20 from Platt's 3.06e10).
- O'Sullivan (2007.13582) line 118: "may be further extended to d <= 9e24 using [PT]".
- Farmer (2008.07206, §4.2) restates Chasse's d < T^2.
- Csordas-Norfolk-Varga and Dimitrov-Lucas (d <= 3) and the GORZ large-n results are as stated.

### C1-J2 (HEURISTIC, possibly new) — upheld_with_corrections
- Re-derived the following:
  - m_k = prod_{i<k}(1 - i/d) = exp(-k(k-1)/(2d) - O(k^3/d^2)).
  - (D^2 - D) is diagonal on x^k.
  - Zero velocity: w_k' = F_ww/F_w - 1 = 2 x_k sum 1/(x_k - x_l) = sum[coth((w_k - w_l)/2) + 1].
  - Local rescaling near height T: dw = 2 dt/T and z = 2t, which gives t_dBN = T^2 tau = T^2/(2d).
  - Isolated pair: t_c = 2 delta^2, so d* = T^2/(4 delta^2).
  - Check that (D^2 - D) cos = -z^2 cos, so the cos zeros are stationary.
- **Correction 1.** The report's "agrees to <0.3% (24 cases)" is not what `dbn_jensen.json` Part C contains. Only 20 rows are comparable: the 4 rows at T = 300.74 have no Part-A partner because of the 300 -> 546.3 grid artefact. The maximum deviation is 1.03% (T = 17.58, delta = 0.45), then 0.40% (51.37, 0.45). The <0.3% figure holds only for T >= 100.
- **Correction 2.** "Chasse's bound follows from de Bruijn's Lambda <= 1/2" should read "is heuristically reproduced by". No error-controlled comparison theorem exists. The investigator's own open question says the same.
- Prior art: a quick arXiv and web search found no statement of the degree-to-dBN-time bridge. The ingredients are classical: Jensen/Laguerre multiplier sequences, the Gaussian multiplier e^{-tau k^2}, and Polya. "Possibly new" is acceptable only as a search-limited label.
- T0 values reproduced: d* = 4.443e25 (delta_max) and 2.258e28 (delta = 0.01).

### C1-J3 — upheld
- Farmer's X_10 is defined explicitly in his §4.2 (zeros 5pi/2 and 7pi/2 moved to +-10+-i), the same configuration as the investigator's.
- Independent coefficient algorithm: Arb series division of cos(sqrt u) P(u)/Q(u) at 6000-14000 bits. Coefficient radii are below double-precision underflow. Certificates apply to the **unrounded** polynomial: `acb_poly.roots`, plus certified sign changes of R(u) on (0, inf). Results (`sk_jensen_exact.json`):
  - j=10 (5pi/2, 7pi/2): real-rooted at d = 117, 118, **119**; certified non-real at 120 and 121.
  - j=20 (9pi/2, 11pi/2): real at 747, 748, 749; non-real at 750 and 751.
  - j=20 (11pi/2, 13pi/2): real at 470, 474, 476, 477; non-real at 478 and 479.
- Only the listed degrees were certified. "First non-real" assumes real-rootedness at all lower d, which Farmer's own computation supports.
- The predictions are reproduced by a separately written z-variable ODE (`sk_jensen_bridge_ode.json`):
  - 119.6273 (investigator 119.627)
  - 769.4049 (769.405)
  - 480.7170 (480.717)
  - 1891.888 (1891.888)

  The sanity residual on the cos zeros is 7e-13. Overflow warnings appeared on rejected trial steps; the accepted solution is unaffected.
- The j=40 and j=60 comparisons are against Farmer's printed values, which were not exactly re-verified here. Given J4, those printed values may carry +-1 uncertainty.

### C1-J4 — upheld (classification: keep in unresolved_findings, now with an independent witness)
- Farmer's table (2008.07206, lines 413-420) lists "# first zeros of X_j are real: 2, 4, 12, 18".
- Moving the two zeros closest to j gives 2, **5**, 12, 18; moving 9pi/2 and 11pi/2 for j=20 gives 4.
- The investigator's reading is confirmed independently for both j=20 thresholds (749/750 versus 477/478) and for the j=10 discrepancy: real-rooted at d=119, against Farmer's "only real zeros for d <= 118, and for all larger d it has non-real zeros".
- At d=119 the colliding real pair has relative separation 1.0% in u (`sk_j10_gap.py`, output `sk_j10_gap.txt`). That is not a near-degenerate case, so ordinary precision should have resolved it.
- This is an independent computational witness in the sense of methodology §6(i). Still, Farmer's exact Mathematica convention is unknown (for example, odd-d handling), and the j=20 issue is a text/table ambiguity. Recommendation: keep both under `unresolved_ambiguity`. The j=10 item may be upgraded to a minor `verified_error` only after a third check or author contact. No public error claim.

### C1-E1 (HEURISTIC + NUMERICAL) — upheld_with_corrections
- Gap-lattice model re-derived: dy/dt = -1/y - 4y S(y), with lattice zeros at +-(k+1/2)s for k >= 1. The isolated limit is 2 delta^2, and the y >> s limit is 4 delta/log(T/2pi).
- T0 values reproduced by integrating the ODE with S as an explicit 2e5-term lattice sum: 1.993e-4, 0.015325, 0.051619, 0.101299. The maximum over delta is 0.10130.
- ODE spot checks (`sk_dbn_ode.json`) reproduce the investigator's numbers exactly: 0.40110, 0.326573, 0.223239. Adding all far zeros and the mirror zeros -2 gamma as a static background changes them to 0.40002, 0.326342, 0.222883 (<= 0.27%).
- **Missing model-free argument (correction).** "Lambda <= 0.2 cannot exclude any quadruple above T0" does not need the lattice model. PT21 (lines 203-206) obtains Lambda <= 0.2 *from* RH up to H > 2.51e12 plus unconditional analysis. The bound is therefore a logical consequence of RH(T0) and cannot carry information beyond T0. The model only shows by how much a stronger bound would be needed.
- The 2026 unrefereed claims were not checked here either.

### C1-N1 (THEOREM) — upheld
Re-derived:
- On (1, inf), {theta/t} = theta/t for theta <= 1, so g_2 = -C/t and ||g_2||^2 = |C|^2.
- The Mellin transform of {theta/t} is -theta^s zeta(s)/s on 0 < Re s < 1, and g_2-hat(s) = C/(s-1) for Re s < 1.
- e_j = t^(conj rho_j - 1) is in L^2(0,1) because Re rho_j > 1/2.
- H_lk = 1/(rho_l + conj rho_k - 1) is the Hermitian Gram matrix, so min ||g_1||^2 = v* H^-1 v.
- Minimising over complex C gives the stated F (and hence a valid bound for real C).
- The single-zero bound is the one-constraint minimum, 2 delta |a|^2/(1 + 2 delta |b|^2).

Numerical F/(4 delta/T^2) = 0.990 (T = 17.6), 0.99965 (T = 100), 0.99999914 (T = 1000). The error is O(1/T^2), which is stronger than the stated O(1/T); the stated form remains true. Novelty is correctly not claimed. Burnol 2002 and BDBLS 2000 contain the Hardy-space method.

### C1-N2 (HEURISTIC) — upheld_with_corrections
- Numbers reproduced: beta = 0.0461914; at T0, log N* = beta/F = 2.105e23; the single-zero version beta/F_1 = 4.21e23.
- **Inconsistency.** The report gives log N* = 2.1e23 but then says "excluding anything above T0 needs log N >~ 4e23". The second figure uses the weaker one-zero Corollary N2. Since zeros come in conjugate pairs, the two-zero floor is legitimate and 2.1e23 is the consistent model figure.
- The model D^2 ~ beta/log N + F rests on the conjectured BDBLS asymptotic. Burnol's bound is a liminf, not a finite-N bound. No synthetic d_N was run, by either the investigator or this review.

### C1-D1 — upheld_with_corrections
- Buthe Thm 2 (1410.7015, lines 762-778) is as quoted. 4.92 sqrt(x/log x) = T gives 2.1693e25 at T0 and 1.4305e25 at 2.445e12, matching Buthe's 1.4e25.
- **Missed prior art.** D. R. Johnston, arXiv:2109.02249 (Ramanujan J.), lines 30-48, proves Schoenfeld's pi bound for 2657 <= x <= **1.101e26** using T = 3e12, with ψ/θ variants up to 9.68e25. The best published implication horizon at T0 is therefore about 1e26, not 2.17e25.
- Single-defect values reproduced: log10 x* = 29.230, 60.240, 159.03, 1801.1. The delta needed at x = 1e29 is 0.49742.

### C1-D2 — upheld
Explicit formula re-derived from S(x) = sum Lambda(n)/(n log n) + 1/(sqrt x log x) and theta = psi - sqrt x. This gives c(x) sqrt(x) log x = 2 + sum_rho x^(rho-1/2)/(rho(1-rho)) + o(1). The factor rho(1-rho) (size T^2) is what makes x* ~ T^{2/delta}. T0 values reproduced: 50.54, 99.82, 249.5, 2495.4. The Robin translation "log n* ~ x*" is heuristic, as labelled. Morrill-Platt Thm 13 (1809.10813, line 277: n <= 10^(10^13.11485)) is confirmed. The 42-case grid was not re-run; it is essentially a formula check.

### C1-D3 (PROPOSITION-PROOF-SKETCH) — upheld
- Re-derived: with |rho(1-rho)| >= gamma^2 and |x^(rho-1/2)| <= sqrt x, the tail is at most 2 sqrt(x) sum_{gamma>T} gamma^-2.
- Using sum_{gamma>T} gamma^-2 ~ (log(T/2pi) + 1)/(2 pi T) gives 4.36e23 at T0, against the report's 4.43e23.
- Truncation and O(1/log x) terms are missing, as the report says.

### C1-D4 (HEURISTIC) — upheld_with_corrections
- **Correction.** "The finite surrogate |M(x)| <= m sqrt x is not a consequence of RH" asserts a non-implication that cannot be proved. The defensible statement: no such bound is known to follow from RH, and under RH plus linear independence of the ordinates (Ingham 1942), M(x)/sqrt x is unbounded.
- The collision-model formula zeta~'(rho0) = zeta(rho0) * 2 delta/((rho0 - rho_a)(rho0 - rho_b)) is re-derived.
- The thresholds rest on the arbitrary visibility level 0.5. The numbers (20.0 / 24.05 / 28.10, and |zeta'| ~ 1.06e-4 for x = 1e16) reproduce from that choice.

### C1-D5 (HEURISTIC) — upheld
- Re-derived: the residue at s = rho/2 - 1 gives Gamma(1 - rho/2) k^(rho/2 - 1)/(2 zeta'(rho)), with |Gamma| ~ e^{-pi T/4} and size k^(delta/2 - 3/4).
- Visibility against the first zero gives log k* ~ pi (T - gamma_1)/(2 delta).
- Reproduced: log k* = 9.545e12 at delta_max, and k = 1e10 probes T <~ 21.46.

### C1-T0 (table) — upheld_with_corrections
All numeric entries are reproduced (`sk_T0_numbers.json`). Corrections:
1. "Nyman-Beurling, Mertens and de Bruijn-Newman have no finite RH-implication" is wrong for de Bruijn-Newman. The Polymath15 / PT21 method gives RH(H) => Lambda <= t0(H); concretely, H >= 2.51e12 gives Lambda <= 0.2 (PT21 Cor. 2). The implication horizon at T0 is therefore Lambda <= 0.2.
2. The psi/pi implication horizon should be 1.1e26 (Johnston), not 2.17e25.
3. The Li row "n <= 9.0e24 (THEOREM L1)" should be attributed to Oesterle (2000), as reported by Voros.

### C1-IV — upheld_with_corrections
The list of uninformative computations stands. Corrections:
- dBN bounds are uninformative for the rigorous reason in C1-E1.
- The pi(x) window "formally not implied by RH(T0)" starts at about 1.1e26 (Johnston), not 2.17e25.
- For Li, Voros (2016-2022) already states n >~ 10^25 with T0 = 2.4e12. The report's prior-art line "(n >~ 1e16-1e18 needed, with earlier heights)" understates the existing literature.

## 3. General issues

1. **Prior-art search was too shallow for the Li family.** The three later Voros papers (1602.03292, 1703.02844, 2204.01036) contain the Li implication horizon (Oesterle), the detection scale n >~ T^2/|t|, and the T0 translation n >~ 10^25. Johnston 2109.02249 supersedes the Buthe evaluation.
2. **Surrogate disclosure.** The Li "synthetic experiment" uses the trend surrogate for 60/63 cases. The results survive the direct check here, but REPORT.md should say so in the claim text, not only in the failed-attempts list.
3. **Small statistical misstatements:** the J2 "<0.3% in 24 cases" and the at-T0 ratio range of the leading Li formula.
4. **Labels are otherwise appropriate.** No finite computation is presented as proving an infinite statement, and no RH claim is made.
5. **Farmer discrepancy (J4).** It has an independent computational witness now. Per methodology §6(iv) it stays in `audits/unresolved_findings.md` until the author's convention is checked.

## 4. Negative knowledge from this review
- The float64 Lemma A grid gives a spurious violation (ratio 3.51) for gamma >~ 1e5 because log|z| cancels catastrophically. High precision is needed.
- The first stress-test implementation (vectorised cos/cosh over the full n by zero grid) did not finish in 15 min. A complex multiplicative recurrence is about 20x faster.
- The far-zero background in `sk_dbn_ode.py` first exhausted memory (4000 x 2e5 complex matrix). It is now chunked and interpolated.

## 5. Sources consulted (web)
- Voros, Simplifications of the Keiper/Li approach: https://arxiv.org/pdf/1602.03292
- Lagarias, Li coefficients for automorphic L-functions: https://arxiv.org/abs/math/0404394
- GORTTW, Jensen polynomials for the Riemann Xi function: https://arxiv.org/abs/1910.01227
- MaRDI record Q2074814 (published GORTTW, d <= 9e24): https://portal.mardi4nfdi.de/wiki/Item:Q2074814
- Other web-search hits were not used.
