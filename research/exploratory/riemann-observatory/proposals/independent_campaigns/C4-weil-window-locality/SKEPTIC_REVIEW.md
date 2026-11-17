# C4-weil-window-locality: skeptic review

Status: independent skeptic review of the investigator report `REPORT.md` in this directory. It makes no claim about RH.
Scope: every structured claim from C4-0 to C4-REL. For each one I tried to refute it by re-deriving it, re-implementing it independently, searching for prior art, or looking for counterexamples.
Reviewer code: `experiments/code/C4-weil-window-locality/skeptic/`. None of it imports investigator code, except `sk_crosscheck_matrix.py`, which compares my matrix with theirs.
Reviewer outputs: `experiments/results/C4-weil-window-locality/skeptic/`.
Versions: python 3.13, numpy 2.5.3, scipy 1.18.1, mpmath 1.3.0, python-flint 0.9.0. Every computation here is non-rigorous: mpmath high precision or float64.

## Verdict summary

| claim | verdict | one-line reason |
|---|---|---|
| C4-0 | upheld_with_corrections | (a)-(c) match the sources. The coincidence window is L = 0.405379, not 0.405408. The "no kink" profile is reproduced. |
| C4-1 | upheld_with_corrections | The citations check out. It misses Zhu's Table 1 (Legendre sector floors) and the contemporaneous Danesh arXiv:2611.10726. Zhu's lambda* is restricted to even real f. |
| C4-P | upheld_with_corrections | Reproduced exactly in the same Galerkin spaces, and the normalisation was validated on the zeros side. But the values are not converged already at L >= 0.5: the true infimum is 0.3% (L=0.5), 0.7% (0.6) and >= 2.8% (0.8) lower. |
| C4-C | upheld | Re-derived line by line. Standard Schur/Sylvester argument. Only cosmetic remarks. |
| C4-LAT | upheld_with_corrections | Algebra re-derived. The aside on the mirror pair ("take a higher sinc power") is wrong as stated, but it is easily repaired and is outside the theorem. |
| C4-B | upheld_with_corrections | Every bound re-derived. The P-bound was tested against 100000 true zeros (36 cases, always satisfied). The asymptotic display has a factor-2 slip: it should read 0.704 L, not 1.407 L. |
| C4-B2 | upheld_with_corrections | Table and crossovers recomputed independently, identical. The phrase "delta >~ 0.22" should be delta >= 0.235 at T = 3e12. |
| C4-R | upheld_with_corrections | The refutation of the brief's heuristic stands. The "corrected statement" (Nyquist locality for kappa < kappa_c) is not established and is contradicted in the collision model. |
| C4-BL | upheld_with_corrections | Correct, but close to tautological: hypothesis R is equivalent to the needed matrix inequality. Hypothesis (S) must also be listed. |
| C4-D1 | upheld | 7 thresholds re-computed by a different route (zeros side, not arithmetic side). All agree within 0.002 in L. |
| C4-D2 | upheld | The N x3 threshold was reproduced. At N = 192 (my run) the threshold is 1.5543, an offset of 0.170 that is still decreasing, as stated. |
| C4-D3 | upheld_with_corrections | L_sinh at 1e12-1e50 reproduced within 0.0007, and every L* <= my L_sinh. "sinh nearly optimal (gap 0.001-0.06)" holds only for delta >= 0.3 at T >= 1e12. At delta = 0.2, T = 1e6-1e10 the gap is 0.11-0.42. |
| C4-D4 | upheld | Collision thresholds at T0 ~ 1e4 reproduced: 3.2645 and 2.8363. Their implications are under-weighted elsewhere in the report (see C4-R, C4-H, C4-REL). |
| C4-H | downgraded | "Supported by C4-D4" is false. The normalised conjecture is trivially implied by C4-B. The c >= 0 part cannot be supported by Rayleigh-Ritz numerics. |
| C4-REL | downgraded | Point (2) rests on an unproven blindness statement that the collision data contradict. |

## What was actually run (reviewer)

| script (skeptic/) | what it does | output (results/.../skeptic/) |
|---|---|---|
| `sk_profile.py` | Even-sector Galerkin profile, written from scratch in mpmath. Each A(y) uses an exact Gauss rule; the outer integral over [0,2L] uses one high-order Gauss rule; C0 comes from `mp.quad`, so no closed forms are used. | `sk_profile_conv.jsonl` |
| `sk_validate.py` | Explicit-formula normalisation versus the zeros side: 100000 Arb zeros plus a smooth tail, test functions g = phi_0, phi_2, phi_4 at L = 0.3, 0.6, 1.0. | `sk_validate.json` |
| `sk_thmB.py` | (1) Re-implements the C4-B margin, L_B and the crossovers from the REPORT text. (2) Checks the bound ingredients numerically. (3) Compares P(g0) with the C4-B bound using the true zeros. | `sk_thmB.json` |
| `sk_detect.py` | Detection thresholds on the zeros side, for the additive and collision models. The real part comes from 100000 zeros plus a tail. Complex evaluations use quadrature and mpmath Bessel functions. | `sk_detect_*.json` |
| `sk_crosscheck_matrix.py` | Entrywise comparison of my zeros-side matrix with the investigator's arithmetic-side matrix. | `sk_crosscheck_matrix.json` |
| `sk_sinh_highT.py` | Single Theorem-B test function on the arithmetic side, using a closed-form autocorrelation and prime phases at 90 digits. Validated against the zeros side, then used for L_sinh at 1e6 to 1e50. | `sk_sinh_highT.json` |
| `sk_flat.py` | Flat-model criterion (Galerkin and closed form) and kappa_c. | `sk_flat.json` |
| `sk_smooth.py` | Profile near the coincidence window, for C4-0(d). | `sk_smooth.json` |

Literature checked at L1 (full text read for the cited passages): Zhu arXiv:2608.24827v2 (abstract, Sec. 1.1-1.4, Prop. 2.3, Table 1, Table 3); Andrews-Connes-La Gatta arXiv:2611.13129 (abstract, Sec. 8.7); Connes-Consani arXiv:2006.13771 (introduction, Thm 1, Cor. 2); Bombieri 2000 BDIM PDF (abstract, Sec. 1, Thm 8, footnote 11, Sec. 12, Thm 12); Suzuki arXiv:2610.32704 (Thm 1.1); Danesh arXiv:2611.10726 (whole paper, which is short).
Checked at L0+ (index content only): Trudgian 2014 via the zbMATH review 1284.11119 (a = 0.112, b = 0.278, c = 2.510, T0 = e).
Searches: arXiv API queries for "Weil positivity", "Weil quadratic form", "Weil's criterion" AND support, "explicit formula" AND "off-line", "Weil functional", Burnol AND Sonine, Paley-Wiener AND zeta AND sampling, and Weil AND positivity AND support AND zeros. zbMATH queries are listed in the per-claim sections.

## Per-claim review

### C4-0: positivity windows and the coincidence. Verdict: upheld_with_corrections

- (a) Verified in CC 2006.13771, introduction. The quadratic form Q_W(g) = W_inf(g*g^*) is "defined on ... smooth functions with support in the interval [2^{-1/2}, 2^{1/2}] and whose Fourier transform vanishes at i/2". Its autocorrelation f is supported in (1/2, 2), which is (3) and the paragraph before it. Thm 1 adds the vanishing at 0. So the support refers to g, and in the log variable L = (1/2) log 2 for g. Bombieri (BDIM text, Sec. 1) states that Yoshida "verifies this positivity for t = (log 2)/2". Zhu's abstract says the same.
- (b) Matches Bombieri, Thm 12 (Sec. 12) up to PDF-extraction garbling of the log log term. Note that Bombieri reproves positivity only for "t sufficiently small" (abstract). Thm 12 has an unspecified O(1), so it does not by itself certify the whole log 2 window.
- (c) Matches Zhu, abstract and Sec. 1.4: certified 8.9e-18 <= lambda*(0.8) <= 2.27e-17. The extension to complex f is the Sec. 6 parity argument. The paper is unrefereed.
- (d) Correction: the coincidence window is L = (1/2) log(gamma_1/2pi) = 0.4053787, not 0.405408. At L = 0.405408, 2pi e^{2L} = 14.1356. The profile point labelled "0.405408" (computed at 0.40541) is therefore offset by 3e-5. This is immaterial.
- The "no feature" claim was re-checked independently: with n_even = 16 (N = 32) my code reproduces their L = 0.4 value (1.8172702e-4) and gives lambda(0.4053787) = 1.44230e-4. -ln lambda on the grid L = 0.37..0.44 (step 0.01) has first differences 0.376, 0.394, 0.413, 0.435, 0.457, 0.482, 0.507 and second differences 0.0176, 0.0192, 0.0216, 0.0221, 0.0249, 0.0252, which are smooth with no jump across 0.4054 (`sk_smooth.json`). This is at fixed N; per C4-P the profile is ~1% non-converged, but a kink would be a gross feature.
- ACL Sec. 8.7 does record the coincidence, in the words "For lambda^2 < 14.13/2pi ~ 2.25 ... no undersampling occurs: this is the regime of [5]". So the investigator's point that it is "already recorded" is correct.

### C4-1: prior art. Verdict: upheld_with_corrections

Verified against the full texts:
- Zhu Prop. 2.3 (Beurling sampling plus Littlewood gaps under RH).
- Zhu Table 3 values (1.05e-6 at L=0.5, ..., 3.19e-283 at L=2.0).
- The law -ln lambda* ~ C N(T*)/ln N(T*) with C = 20.13 ~ 2pi^2, and the quoted definition of T* = 2pi e^{2L}.
- Zhu Thm 1.3 (exp(-L e^L)) and Thm 1.4 (T1 = 2pi e^{A_L}, A_L ~ 4e^L).
- ACL: lambda^2 - 1 even and lambda^2 - 2 odd minuscule eigenvalues; the 2469 zeros up to height 3000 at lambda^2 = 250.
- Bombieri Thm 8. The exact statement is "number of negative eigenvalues of H(Gamma;t) equals the number of distinct complex conjugate pairs" for finite multisets Gamma. Footnote 11 covers fake zeros with k <= 320.
- Suzuki 2610.32704, Thm 1.1.

Corrections:
1. Zhu's lambda* is an infimum over real even f (his eq. (1)). It is not "exactly as the brief", which allows all g. Zhu's Thm 6.2 shows the window ground state at L = 0.8 is even, so the comparison is legitimate there.
2. Missed overlap: Zhu Table 1 already gives converged Legendre-basis sector floors for both parities at L = 0.5..1.2: 9.34e-7, 1.61e-9, 4.18e-13, 1.65e-17, 4.14e-23, 5.88e-30, 2.04e-38, 7.94e-49, with the odd/even ratios. C4-P therefore replicates Zhu Table 1, not only Table 3, and the "different basis" remark applies only to Table 3.
3. Missed contemporaneous work: P. Danesh, arXiv:2611.10726 (7 Nov 2026), "A quantitative two-interval criterion for the Riemann hypothesis". It asks "whether the Weil form can detect a zero ... away from the critical line" using two narrow, widely separated supports. It shows that an off-line zero forces the normalised cross term to grow faster than e^{(delta - eps)·separation}. This is the same e^{delta x} mechanism as C4-B. However, Danesh states that the "first violating separation" is left undetermined, so it gives no (T, delta) window law and does not anticipate C4-B, C4-LAT or C4-R.
4. With those additions, I agree that I found no statement of which (T, delta) a window detects.

### C4-P: window profile. Verdict: upheld_with_corrections

Independent reproduction (`sk_profile.py`): my own mpmath code, using a different quadrature route and no closed forms. In the same Galerkin space it reproduces the investigator's values to all printed digits:

| L | N | investigator | skeptic |
|---|---|---|---|
| 0.3 | 24 | 0.00757304658233 | 0.00757304658233095 |
| 0.5 | 40 | 9.37661316452e-7 | 9.37661316451519e-7 |
| 0.6 | 48 | 1.62064509585e-9 | 1.62064509584518e-9 |
| 0.8 | 72 | 1.70155900214e-17 | 1.70155900214101e-17 |

The explicit-formula normalisation was validated against 100000 Arb zeros plus a smooth tail (`sk_validate.json`). The diagonal entries for phi_0, phi_2, phi_4 at L = 0.3, 0.6, 1.0 agree to |diff| <= 1e-8, which is the accuracy of the tail model.

Correction (precision overstated): the values are not converged in N for L >= 0.5, not only for L >= 0.9. Larger bases in my code give:

| L | best N | skeptic value | change vs investigator | Zhu Table 1 |
|---|---|---|---|---|
| 0.5 | 50 / 60 / 80 | 9.36027e-7 / 9.35236e-7 / 9.34583e-7 | -0.33% | 9.34e-7 |
| 0.6 | 64 / 80 | 1.61286e-9 / 1.60956e-9 | -0.68% | 1.61e-9 |
| 0.8 | 92 / 112 | 1.65615e-17 / 1.65315e-17 | -2.8% | 1.65e-17 |

The investigator's values at L = 1.0 (6.257e-30) and 1.1 (2.057e-38) are also above Zhu's Table 1 reference values (5.88e-30, 2.04e-38), by 6.4% and 0.8%. Convergence is algebraic: the ground state has endpoint structure (ACL Sec. 8.7 notes that the form domain allows jumps at the ends). The six significant digits printed in C4-P are therefore not meaningful. The values are valid only as Rayleigh-Ritz upper bounds that sit 0.3-6% above the infimum.

The other statements check out:
- "11-27% below Zhu's certified upper bound": arithmetic checked.
- "Inside the L = 0.8 enclosure": true.
- Odd/even ratios: they agree with Zhu Table 1 (e.g. 207.5 vs 208 at L = 0.5).

### C4-C: exact detection criterion. Verdict: upheld

Re-derived:
- (S) makes the closable form P coercive. Each l_z(g) = <g, e_z> is L^2-bounded and hence P-bounded, so the Riesz vectors k_z exist in H_P. The functionals vanish on the P-orthocomplement, which makes the decomposition W-orthogonal.
- On span{k_z}, W = c*(G + G M G)c with G Hermitian. G is invertible because distinct e_z are linearly independent. Sylvester's law gives (i). Continuity on H_P transfers the index to C_c^inf.
- (ii) follows from Weyl, since G^{-1} > 0 and M has one negative eigenvalue per distinct conjugate pair. The bound therefore holds even without counting multiplicity.
- (iii) follows from <P^{-1}v,v> = sup_g |<v,g>|^2 / P(g).
- (iv): for real u and v, W(u,v) is real because the zero set is invariant under gamma -> -conj(gamma) (rho -> conj rho). Hence W(u+iv) = W(u) + W(v). This part does not need (S), which matters because C4-B uses it.

Remarks:
- "(S) holds under RH by Zhu Prop. 2.3" is vacuous for nonempty Q, since under RH there is no Q. In any hypothetical scenario (S) must be assumed separately. The report effectively does this.
- "Detection is monotone in L" follows trivially from nested domains.
- This is a standard completing-the-square lemma. It is the same lemma as the host repository's S_L in CURRENT_RESULTS Sec. 7, so the investigator's "not claimed new" is appropriate.

### C4-LAT: lattice/flat two-regime law. Verdict: upheld_with_corrections

Re-derived:
- Poisson: f = g*g~ is continuous, supported in [-2L, 2L] and vanishes at +-2L, so Sum |h|^2 = (2pi/s) f(0) = Psi0 ||g||^2 for L <= pi/s, including at L = pi/s.
- With P = Psi0 I: G = Psi0^{-1}[[sinh(2dL)/d, 2L],[2L, sinh(2dL)/d]] and M = [[0,1],[1,0]]. The negative eigenvalue of G^{-1} + M is Psi0/(sinh(2dL)/d - 2L) - 1.
- kappa_c = 2.1773190 (root of sinh k = 2k).
- Null function above Nyquist: sin(pi(k+1/2) +- ib) = (-1)^k cosh b, which gives -2 d^2 cosh^2(pi d/s)(sinh(eps d)/(eps d))^8.
- Independent numerical check (`sk_flat.json`): the flat-model Galerkin minimum and the closed-form eigenvalue both change sign between 0.98 and 1.02 L_flat for d = 0.1, 0.3, 0.49.

Correction: the aside "if the mirror pair at -T0 is present, take a higher sinc power" is wrong as stated. With p sinc factors, eps = (L - pi/s)/p shrinks as p grows. The mirror term behaves like T0^2 (p/((L - pi/s) T0))^{2p}, which grows with p whenever (L - pi/s) T0 < p. So it cannot be made negligible near the Nyquist edge.

Repair: multiply h by ((r+T0)^2 + d^2) so that it vanishes at -T0 +- i d, and use sinc^6 to keep h in L^2. The theorem as stated (single pair) is unaffected.

### C4-B: growth detection under H1. Verdict: upheld_with_corrections

Re-derived line by line:
1. Values at +-i delta and the quadruple term. what(-i d) = int sinh^2 = sigma^2 and what(+i d) = -sigma^2, so the term is -2m sigma^4 (checked numerically to 1e-15).
2. The -T pair is bounded by Ac^2/(2T^2). The bound |what(z)| <= Ac/|z| for |Im z| <= d follows from one integration by parts; numerically max |what||z|/Ac <= 0.53.
3. P <= int F dN. The off-line ordinates counted in N add 2m F(T) >= 0, and the multiplicity m only helps.
4. Backlund integration by parts gives F(0) + (1/pi) int F theta' - int F' S.
5. Bounds on the transform. Checked numerically, each to within a factor ~2:
   - |what(s)| <= 2A/|s| and |what'(s)| <= 2B/|s|;
   - ||what||^2 = 2pi sigma^2 and ||what'||^2 <= 2pi L^2 sigma^2.
6. theta' facts (numerically):
   - max theta' on (0, 2pi] = -5.3e-4;
   - (theta'(t) - (1/2)log(t/2pi)) t^2 lies in [-0.02093, -0.02083] on [2pi, 2000], comfortably below 0.4.
7. Error terms:
   - E2 via log(1+u) <= sqrt(u), plus symmetry of |what|^2;
   - E3 via int_0^inf log((t+T)/2pi)/(t+T)^2 dt = (log(T/2pi)+1)/T;
   - E4: 10A^2/(pi T^2) + 16 pi sigma^2/T^2;
   - the S term: 4 pi L sigma^2 from 2||what|| ||what'||, plus 8AB/T, plus the tail E5 = 32AB(S*(2T) + 0.112 + 0.278/log 2T)/T.
8. Trudgian constants confirmed via zbMATH 1284.11119. The bound is unconditional for T >= e.
9. Mollification/dominated convergence and the reduction to real g via C4-C(iv) are fine.

Independent numerical test against 100000 true zeros (`sk_thmB.json`, T = 1e3, 1e4, 3e4; d = 0.1, 0.3, 0.49; L = 1..4):
- The C4-B upper bound for P(g0) holds in all 36 cases, but it is loose by a factor of 10-40.
- The main-term integral (1/pi) int F theta' is within its bound sigma^2 log(T/2pi) + E2 + E3 + E4 in all cases.
- The true P deviates from the flat value sigma^2 log(T/2pi) by up to a factor of ~2 in either direction (prime-comb/S(t) fluctuations). This is why the 4 pi L S* term cannot be dropped.

Correction: the "Asymptotics" display e^{2dL}/(4d) ~ (0.5 + 1.407 L) log T has a factor-2 slip. The correct form is (0.5 + 0.704 L) log T, i.e. (1 + 1.407 L)/2 · log T. Check: at T = 1e100, d = 0.49, L_B = 8.26 gives e^{2dL}/(4d) = 1672, against (0.5 + 0.704 L) log T = 1454 and (0.5 + 1.407 L) log T = 2791. The table, which uses the exact inequality, is unaffected.

Status: this is a correct implication under H1. It is vacuous if RH holds, and it is "possibly new" only. The e^{delta x} detection mechanism is folklore and appears in Danesh 2611.10726 and Kim et al.

### C4-B2: tables. Verdict: upheld_with_corrections

`sk_thmB.py` re-implements the inequality from the REPORT text. It reproduces every L_B value to 3+ decimals. Examples:
- T = 3e12, L_N = 13.446: L_B = 6.490 (d = 0.49), 7.937 (0.4), 10.565 (0.3), 15.819 (0.2).
- T = 1e100: L_B = 8.261, 10.102, 13.442, 20.123, 40.161, 80.238.
- T = 1e1000: L_B = 10.733 (0.49), 52.317 (0.1).
The crossovers agree to 1e-6: 6.0906, 6.5941, 7.3732, 9.7665, 14.7693, 31.0486, 67.1403 and 413.1378.

Correction: "for delta >~ 0.22 its rigorous single-defect detection window is below the Nyquist window" holds at T = 3.0001753328e12 only for delta >= 0.2354. At delta = 0.22, L_B = 14.39 > L_N = 13.45.

### C4-R: the brief's heuristic. Verdict: upheld_with_corrections

The refutation stands. Read literally, the heuristic claims blindness for T >> 2pi e^{2L}, up to O(log 1/delta). Three independent lines contradict this:
- Under H1, C4-B gives detection at L_B = (1/(2d))(log log T + log log log T + O_d(1)) = o(L_N) for every fixed d > 0. This is rigorous, conditional on H1, and I re-derived it.
- In the lattice model the law is exact (C4-LAT, re-derived).
- In the injection model the growth-regime thresholds were reproduced by me on the zeros side, and up to 1e50 with the single sinh function (C4-D3 below).
No O(log 1/delta) correction can bridge log log T versus log T. The heuristic concerns hypothetical off-line zeros, so refuting it under the hypothetical H1 is legitimate.

Correction: the "corrected statement" is not established and must be restricted. It says that Nyquist locality holds for kappa <~ kappa_c, with L* ~ L_N + a small offset + a small log(1/delta) term.
1. The blindness half (no detection below about L_N) is unproven. C4-BL is conditional on R, and Rayleigh-Ritz numerics can only produce upper bounds on L*. A finite basis can never show that a window fails to detect.
2. It is contradicted in the collision model, which keeps the zero count fixed as the argument principle requires. I reproduced these thresholds independently:
   - T0 = 9999.46 (L_N = 3.686): kappa = 0.74 gives L* = 3.264, and kappa = 1.47 gives L* = 2.836. Near-line defects are detected 0.42 and 0.85 below the Nyquist window.
   - Also T0 = 1000.6, kappa = 1.01: L* = 2.306 < L_N = 2.535.
   - Even in the additive model, T0 = 7e4 with kappa = 1.86 gives L* = 4.484 < L_N = 4.659.
3. The corrected statement should read as follows. In the additive single-defect model, the finite-basis upper bounds for L* in the regime kappa < kappa_c lie at L_N + [0.02, 0.63] for T0 <= 7e4, with one exception below L_N. The local zero configuration can move L* below L_N by O(1). No proof of non-detection exists.

### C4-BL: conditional blindness. Verdict: upheld_with_corrections

The proof is correct. G = E* P^{-1} E <= (1+eta) G_flat, inversion is operator-monotone, then apply C4-C(i). The 4x4 cross-entries are O(e^{2dL}/T).

However, R(T, L, eta) restricted to V = span{e_z} is exactly the matrix inequality G <= (1+eta) G_flat. The theorem is therefore essentially a reformulation, and all the content lies in R. The conclusion also needs (S) (the setup of C4-C), and this should be stated in the hypotheses.

The heuristic part (when R holds; eta ~ 0.1-0.7 at 1e6-1e10) was not verified. Note that worst-case prime-comb alignment can be of size ~4 sigma^2 e^L. At L ~ L_flat with d near 1/2, e^L ~ (log T)^{1/(2d)} is comparable to log T. So "eta -> 0 as log T >> L" can hold only for typical T, not uniformly in T.

### C4-D1: detection thresholds. Verdict: upheld

Independent route (`sk_detect.py`): the true-zero part comes from the zeros side (100000 Arb ordinates of both signs plus a smooth tail), instead of the investigator's arithmetic side. Complex evaluations use Gauss quadrature (+-i d) and mpmath Bessel functions (mirror pair). The detection rule (lambda_min < -1e-8) and N rule are the same.

Entrywise, my matrices agree with the investigator's arithmetic-side matrices to 6.8e-8 (T0 = 100, L = 1.5, N = 48), 2.5e-7 (T0 = 1000.6, L = 2.5, N = 64) and 1.2e-6 (T0 = 1e4, L = 3, N = 64). Thresholds, skeptic vs investigator:

| T0 | delta | skeptic | investigator |
|---|---|---|---|
| 100.07 | 0.01 | 1.7098 | 1.7106 |
| 100.07 | 0.49 | 1.5465 | 1.5450 |
| 1000.57 | 0.01 | 2.9738 | 2.9747 |
| 1000.57 | 0.45 | 2.4785 | 2.4778 |
| 1000.57 | 0.49 | 2.3137 | 2.3153 |
| 9999.46 | 0.4 | 2.8598 | 2.8586 |
| 9999.46 | 0.01 | 4.0805 | 4.0805 |

All agree within the investigator's bisection resolution (0.003).

The caveat is correctly stated in the report: each number is an upper bound for the model threshold, and float64 limits the detection floor.

### C4-D2: N-convergence. Verdict: upheld

At T0 = 100.07, d = 0.01, my thresholds are N = 48: 1.7098; N = 144: 1.5582 (investigator N x3: 1.5606); N = 192: 1.5543 (offset 0.170, still decreasing).
The monotone decrease is guaranteed for nested polynomial spaces. The investigator correctly says that the N -> inf offset is not determined.

### C4-D3: large heights. Verdict: upheld_with_corrections

Independent route (`sk_sinh_highT.py`):
- I used the single Theorem-B function g0 = e^{-iTx} sinh(dx), not a Galerkin basis. Its autocorrelation has a closed form a(y). The arithmetic side uses prime phases T log p mod 2pi at 90 digits, the archimedean term sigma^2 Phi(T), and an exact pole term for T <= 1e5.
- Validation against the zeros side (100000 zeros plus tail) at T = 1e4 and 3e4: six (delta, L) cases agree to |diff| <= 2.6e-8. My first JSON listing mislabelled three of the pairings; `validation_corrected` in `sk_sinh_highT.json` has the right ones.

Results, as L_sinh (skeptic) vs L_sinh (investigator), with the investigator's L* in brackets:

| T | delta = 0.49 | delta = 0.4 | delta = 0.3 |
|---|---|---|---|
| 1e12 | 3.5897 vs 3.5891 [3.5860] | 4.2732 vs 4.2727 [4.2633] | 5.4692 vs 5.4698 [5.4308] |
| 1e15 | 3.6781 vs 3.6782 [3.6688] | 4.1978 vs 4.1976 [4.1835] | not run |
| 1e20 | 4.0191 vs 4.0188 [3.9970] | 4.6638 vs 4.6638 [4.6372] | 5.9290 vs 5.9295 [5.8764] |
| 1e30 | 4.4134 vs 4.4140 [4.4078] | 5.1016 vs 5.1016 [5.0907] | not run |
| 1e50 | 4.8846 vs 4.8850 [4.8834] | 5.7482 vs 5.7476 [5.7460] | not run |

All values agree within the investigator's bisection resolution (0.0016). The investigator's Galerkin L* is <= my L_sinh in every case, as it must be.

At the midpoint heights the investigator gives no L_sinh, but their L* is consistent with my L_sinh:
- 1e6: 2.852 vs L* 2.839 (delta = 0.49); 4.751 vs 4.611 (delta = 0.2).
- 1e8: 3.100 vs 3.061; 5.986 vs 5.570.
- 1e10: 3.320 vs 3.302; 6.369 vs 6.259.

Correction: "the single Theorem-B test function is nearly optimal: L_sinh - L* in [0.001, 0.06]" holds only for the ultra-height cases (delta >= 0.3, T >= 1e12). At delta = 0.2, T = 1e6, 1e8 and 1e10 the gap is 0.14, 0.42 and 0.11 (kappa = 2.4-4.2, close to the crossover).

Caveats that stand as the investigator states them: the archimedean approximation is O(log T/T); the 1e6-1e10 neighbours come from non-rigorous mpmath sign changes; at 1e12-1e50 the quadruple is placed at a decimal height with unknown neighbours. The headline growth-regime statement holds in this model: L* stays within 0.3 of L_flat while L_N grows to 56.6.

### C4-D4: collision variant. Verdict: upheld

I reproduced T0 = 9999.46 with d = 0.1 (3.2645 vs 3.2649) and d = 0.2 (2.8363 vs 2.8368) on the zeros side.

Note the kappa values: d = 0.1 and 0.2 correspond to kappa = 0.74 and 1.47, both far below kappa_c. These data therefore contradict the "Nyquist locality" form of C4-R, C4-H and C4-REL by up to 0.85 in L, not just "include the local configuration". The deltas in this file are 0.01, 0.03, 0.1, 0.2, 0.3, 0.4, 0.45 and 0.49. The REPORT text "delta = 0.01..0.49" is ambiguous about this.

### C4-H: two-regime law plus conjecture. Verdict: downgraded

- "Supported by ... C4-D4" is false. In the collision model L* lies 0.42-0.85 below min{L_N, L_loc} at kappa = 0.74-1.47 (T0 = 1e4).
- The conjecture |L* - min(L_N, L_flat)|/L_N -> 0 for fixed delta is not a meaningful conjecture. Under H1 (and likewise in the additive model, since the C4-B proof only uses P <= int F dN_true), L* <= L_B = O_d(log log T) and L_flat = O_d(log log T), so both are o(L_N). The statement follows from C4-B. A non-trivial version would be L*/L_flat -> 1 or |L* - L_flat| -> 0. Even these can fail at heights where the prime comb aligns (see C4-BL).
- The bound 0 <= c(T) presupposes blindness below L_N, which no Rayleigh-Ritz computation can support, and the collision data contradict it.
- The small-delta mechanism W ~ P + 2|h(T)|^2 - 2 d^2 |h'(T)|^2 (+T pair) was re-derived and is correct to O(d^2). It remains a heuristic.

### C4-REL: relevance to the host repository. Verdict: downgraded

(1) The margin collapse is correct as a qualitative statement, with the C4-P correction: the values are upper bounds, 0.3-6% high. This agrees with Zhu and with the host's own "from above" warning.

(2) "For near-line defects only windows with L >~ L_N + O(0.2) see height T", and hence prescribed families "must reach L ~ L_N", rest on the unproven blindness half. C4-BL is conditional on R, and the numerics are upper bounds only. The collision data reproduced here show near-line defects seen at L_N - 0.85. The opposite conclusion therefore remains possible: a window may see near-line defects well below L_N when the local real-zero configuration is depleted, which is exactly what an off-line pair does to the zero count. Treat this point as a heuristic question, not as guidance.

(3) C4-C and the host's S_L are the same completing-the-square lemma on different sides of the explicit formula. That is a fair structural analogy and not a result.

## General issues

1. Precision presentation. The profile values are reported to 6 significant digits, but they are 0.3-6% above the infimum (C4-P). For a programme that hinges on resolving lambda_min this matters. Report at most 2-3 digits, as upper bounds.
2. Asymmetric evidence. Every numerical threshold is an upper bound on L* (Rayleigh-Ritz). Several summary claims nevertheless assert non-detection: "Nyquist locality", "only windows with L >~ L_N", "c >= 0". Lower bounds on L* (blindness) exist only in the lattice model (exact) and under hypothesis R (C4-BL).
3. Model dependence. The additive model, which raises the local zero count by 2, is used for all headline statements. The collision model, which keeps N(T) fixed as Backlund's formula with bounded S suggests a real off-line pair would, gives systematically lower thresholds. It contradicts the near-line locality claims.
4. Small numerical slips: the coincidence window 0.405379 (not 0.405408); the asymptotic coefficient 0.704 L (not 1.407 L); delta* = 0.235 at 3e12 (not 0.22).
5. Literature: Zhu Table 1 overlaps C4-P directly and should be cited. Danesh arXiv:2611.10726 is contemporaneous related work on Weil-form detection of off-line zeros through support geometry.
6. Process note: the report is a structured return rendered to REPORT.md by `tools/materialize_results.py`. Its claims and hashes were consistent with the files I opened. I recomputed sha256 only for the files I used, and only implicitly, by reproducing their content numerically.

## Negative records (reviewer)

- My first `sk_profile.py` run used an inner Gauss rule that was too low-order (M/2+4 nodes for degree 2·maxdeg). It gave wildly wrong negative eigenvalues (-4.1, -4.9) that depended on the outer node count. I fixed it to maxdeg+2 nodes. Inexact inner rules are an easy trap here.
- I first assumed the leading 1/T correction to the archimedean term for the single sinh function was -sinh^2(dL)/T. In fact PV int log|1-u^2|/u^2 du = 0, so the 1/T term vanishes. I corrected this before producing results. It is immaterial at T >= 1e6.
- The exact archimedean r-integral via mpmath digamma costs ~2 minutes per case, so the arithmetic-side validation of the single-function formula was limited to 3 cases.

## Reviewer output manifest (sha256)

All files are in `experiments/results/C4-weil-window-locality/skeptic/`. The total size is under 100 KB.

```
c734c77e84e4134e10ea32a8ad44ee7443878e531ea8e70875827a583a914039  sk_crosscheck_matrix.json
7529c9c04d5c6fe2e63ccef8a56c465f6267ac04755f52dd18f23081a7a3caa5  sk_detect_T1001_add_Nrule_0.01.json
232efbb5e8e9c30385586367f220e8dd3087a02e9c5943f7688f6c3dcff243e0  sk_detect_T1001_add_Nrule_0.45_0.49.json
363a4726c1ee4dde04bea666903001ac30e4b1ff59b815ec5c2cd17857e947dd  sk_detect_T100_add_N144_0.01.json
5e1c46e8c9eff0cc95795e4779bce4952bd54e34420561fe4b6929bdcb4d50ba  sk_detect_T100_add_N192_0.01.json
ba7967d5746b713eeee0281ae4b125392e6dace5df30792c8581c42221a0d6eb  sk_detect_T100_add_Nrule_0.01_0.49.json
71d16ffcc647eff3128da5b2822fa844987afe2daec33ef463bc69b91716e006  sk_detect_T9999_add_Nrule_0.01.json
6ff4225d8cbeeda6c73200f05a99c1f103d458135076e65ec6926ae1c6708002  sk_detect_T9999_add_Nrule_0.4.json
67e6cb27bb66a9ca975bc9fd6620ea9c1868134b6ea7d7d3a1bc77cbd8a68546  sk_detect_T9999_collision_Nrule_0.1.json
dda3bb975fd3a6a82f41864a5ba375147d86540d0239fd160e5f2df98ddd3317  sk_detect_T9999_collision_Nrule_0.2.json
d9c2364b2afb9400724f5e817322b22cd6b0f99c03d3da1cbf418f2f34b7b15b  sk_flat.json
5ab278bbefedce431f2acfe82be2e214283a5e7debfc8748419992cb5a1fd14c  sk_profile_conv.jsonl
f541f81699f85b3f84286dadadc6575a27169dd6e42dfc13156edf9637ff7b8c  sk_sinh_highT.json
a124ae93c7210133ca6059268be0706916aa47093b565513bf6934479a621d14  sk_sinh_highT.log
b174698974d3891e1818f65ff9b2523b3c996792155f63a5272f8ef9ea8006b8  sk_smooth.json
4637bebac3e8cbff740735fee7aa6d9ad8c08497a0b2a4b6b5b41db7eae61c2c  sk_thmB.json
6261264935017dd790a4c5fe99b22704187db45486da743aa8b521516d5634e2  sk_validate.json
```

Runtimes: the profile convergence batch took about 10 min; the zeros-side detection batches about 25 min on 2 cores; sk_thmB about 6 min; sk_sinh_highT about 12 min; sk_smooth about 1 min.
Zero data: the 100000 Arb-certified ordinates from the shared scratch data directory, all 100000 lines present.

