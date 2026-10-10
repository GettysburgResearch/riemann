# LANE P4 — FALSIFICATION-FIRST NUMERICS (W-pinch mechanism stress test)
PLAN (10 lines):
1. Read T-105059 (exact W_u def, normalization), L-105058.5/.4, X-105059 NOTES.
2. Replicate W_u EXACTLY: Lambda(X)=sum_{N/2<n<=N} h_U(n) n^{-1/2} tent(n), U=floor(X^{1/3}).
3. Compute (1/log T) int_1^T u W_u^2 du/u on log grid, T up to 1e6+; watch stabilize vs decay.
4. Compare against u m(u)^2 mass (L-105058.5 proved) on same grid.
5. Spectral: transform of W-sequence at s=-1/2+h+i*gamma_1, h in {0.02,0.01,0.005,0.0025}.
6. Fit blowup exponent: log(1/h) (half-pole) vs 1/h (full pole), for unweighted vs weighted.
7. If restoration absent: test Riemann-Liouville half-derivative in log u as corrected weight.
8. Verdict early in NOTES; refine with error bars.
9. All data to JSON in lane dir.
10. Final: MECHANISM VERDICT + exponent fits.

## CONVENTIONS LOCKED (from T-105059.5/.6 + num_e4.py)
Lambda(u) = sum_{N/2<n<=N} h_U(n) n^{-1/2} ln(2n/N)/ln2, U=u, N=u^2 (X=u^3 anchor).
W_u = Lambda*sqrt(ln N)/u.  Unweighted comparator V_u = Lambda/u.
Target: limsup (1/lnT) int_1^T u W_u^2 du/u >= c0' > 0. Benchmark: u m(u)^2 mass (proved >= c0=0.0159).
KEY FINITE-DATA DISCRIMINANT (h->0 at fixed s needs u ~ e^{1/h}: h=0.005 => u~e^200 IMPOSSIBLE;
we use the exact dual): half-pole (s-rho)^{-1/2} <-> gamma_1-oscillation amplitude of
sqrt(u)V_u ~ (ln u)^{-1/2} (=> W-mass/lnT ~ const iff nothing worse);
full-pole restoration <-> amplitude of sqrt(u)W_u ~ (ln u)^0.
FAILURE MODES TO DETECT: amplitude of sqrt(u)V_u decaying like (ln u)^{-3/2}
(Selberg-Delange-type, would leave W-mass ~ 1/ln -> 0: NOT RESTORED), or faster.
Measurement: sliding log-window projection a(L)=mean_win[ A_u e^{-i gamma_1 ln u} ],
A in {sqrt(u)m, sqrt(u)V, sqrt(u)W}; fit log|a| vs log ln u -> beta. beta_W ~= 0 <=> RESTORED.
Plus mass curves M(T)=(1/lnT)int u W^2 du/u vs same for m; plus feasible-h J(h) scan.

## ===== EARLY VERDICT (2026-08-23, first full run, u in [20, 12649], N=u^2 to 1.6e8) =====
## MECHANISM VERDICT: RESTORED. The sqrt(log N) weight DOES restore the full pole.
Grid: 307 log-spaced integer u, dLn=0.02; Lambda via exact prefix-sum identity (validated vs
brute-force h_U sieve at u=50,101,200,316: agreement to 1e-14). Files: stage1_big.json, stage2_big.json.
(A) gamma_1-amplitude decay exponents, amp ~ (ln u)^{-beta}, sliding log-windows width 2.0:
    beta_V (UNWEIGHTED tent field sqrt(u)Lambda/u):  0.519 +/- 0.040  <- HALF-POLE (ln u)^{-1/2}: WALL CONFIRMED
    beta_W (sqrt(log N)-WEIGHTED):                   0.008 +/- 0.037  <- FULL POLE (const amp): RESTORED
    beta_m (control sqrt(u)m(u)):                   -0.041 +/- 0.033  <- const, control passes
    [Error-bar provenance (F9): the +/- values are ordinary least-squares standard
    errors of the fitted slope in log(amp) vs log(ln u), computed over the sliding
    log-window fit points (stage2 pipeline); they capture fit scatter only, NOT the
    systematic (ln u)^{-eps} drift caveat recorded at the end of this file. The
    tighter bars quoted in VERDICT.json (e.g. beta_W 0.008 +/- 0.028) come from the
    same estimator on the pooled full-window fit; both are statistical.]
(B) TRACKING: corr(sqrt(u)W_u, sqrt(u)m(u)) = -0.9645, regression slope = -0.2466.
    PREDICTED chain constant: 2*c_tent*sqrt2/sqrt(pi), c_tent = 1-(2/ln2)(1-1/sqrt2) = 0.15466
    => 0.2468. MEASURED |slope| 0.2466. Match to 1e-3. (Sign negative = the known unfixed
    overall sign in the convention chain, T-105059.4; irrelevant for quadratic energy.)
(C) MASSES (1/lnT) int u X^2 du/u: mass_W = 0.00088->0.00134 (T=100->1e4, slowly GROWING);
    mass_V ~ 0.00013 FLAT (killed by 1/ln: half-pole); mass_m 0.303->0.166 (decreasing toward
    its asymptote ~0.027). Coherence: slope^2 * c_0(gamma_1-pair share) = 0.0608*0.0159 = 9.7e-4
    ~ measured mass_W 1.3e-3. Candidate explicit constant c_0' ~ 0.06*c_0 ~ 1e-3.
(D) h-scan (feasible window h>=0.09 given lnT=9.4; h<0.005 needs u~e^200: IMPOSSIBLE, the
    ln-dual amplitude measurement above is the honest discriminant): h*J_W ~ 0.0003-0.0004
    plateau (1/h law) while J_W/ln(1/h) still rising => full pole; J_V flat*ln only.
NEXT: robustness (window widths, cmin, jackknife), within-U-cell N-sweep stability, phase lock.

## ===== FINAL VERDICT (all stages complete) =====
## MECHANISM VERDICT: **RESTORED** — the sqrt(log N) weight restores the full pole, exactly
## as T-105059.6 designed. No correction to the lemma statement is needed.
Evidence chain (files stage1_big.json, stage2_big.json, stage3.json, stage4.json, stage5.json):
1. beta-exponents (amp of gamma_1-component ~ (ln u)^{-beta}), 9 window/cutoff configs,
   jackknife errors: beta_V (unweighted) = 0.51-0.62 (half-pole wall CONFIRMED, exactly 1/2
   within the m-control systematic); beta_W = 0.006-0.117 with beta_W - beta_m(control)
   ~= 0.02-0.03 in every config (FULL POLE: constant amplitude).
2. Two-zero quantitative pinch test (frequency scan, sharp peaks ONLY at gamma_1, gamma_2):
   predicted amp = C_chain / (|rho-1| |zeta'(rho)|), C_chain = 2 c_tent sqrt2/sqrt(pi)
   = 0.247167 (c_tent = 1-(2/ln2)(1-1/sqrt2)): gamma_1: pred 0.02203 meas 0.02174 (ratio 0.987);
   gamma_2: pred 0.01034 meas 0.01058 (ratio 1.023). GAMMA-INDEPENDENT chain constant times
   the residue factor — the pinch factorization structure itself is verified, not just one number.
3. Per-window lock: aW/am = 0.2489 +/- 0.0033 across ln u in [3,9.4]; phase diff = 3.129 +/- 0.011
   (= pi: the known global sign, T-105059.4). W_u tracks -C_chain * (gamma-osc of m(u)) uniformly.
4. Masses: (1/lnT) int u W^2 du/u = 1.34e-3 at T=1e4 vs predicted gamma_1-pair share
   C_chain^2 c_0 = 9.71e-4 (the rest = gamma_2+, consistent). mass_V flat 1.3e-4 (dies as 1/ln:
   half-pole). CANDIDATE EXPLICIT CONSTANT for the lemma: c_0' = C_chain^2 c_0 ~= 9.7e-4
   (with C_chain the tent-chain constant as measured; the deposit-grade c_0' must come from the
   w1-w4 proofs, but numerics say it is ~1e-3, NOT vanishing).
5. Pinch coefficient NONVANISHING (w4 numerically settled): measured 0.2489 vs predicted 0.2472.
6. Pointwise |F(-1/2+h+i gamma_1)| h-scan: NON-DIAGNOSTIC at any reachable T (identical local
   exponents for W, V, m at h in [0.08,0.6]; h=0.005 requires u ~ e^{200}). The orchestrator's
   literal item (2) h-list is information-free at finite T; the ln-dual amplitude measurement
   (item 1 above) is the mathematically equivalent honest discriminant. Pipeline validated on
   synthetic ground truth: beta(half)=0.502, beta(full)=-0.009, beta(half*sqrt(ln N))=-0.009.
7. Within-U-cell N-sweep (u=300..2500, N in [u^2, u^2+3u]): W varies by <~15% around anchor,
   cell-mean ~ anchor; anchoring at N=u^2 is representative; no cell pathology.
8. Exactness: prefix-sum Lambda identity validated vs brute-force h_U sieve to 1e-14.
CAVEATS (honest): u-range ln u <= 9.44 (N <= 1.6e8); ln ln u leverage 1.1-2.24 only — a
conspiratorial (ln u)^{-eps} drift with tiny eps is not excluded by ANY finite computation,
but beta_V = 0.5 lands exactly on the predicted half-pole on the same data, so the method
resolves the 1/2-vs-0 distinction cleanly. RH nowhere used or claimed.
