# Lane 2 — Decision engine: certify M_2, M_3, M_sc > 0 on [1e6, x_sat]
# CHECKPOINT NOTES (incrementally updated)

## 0. System (frozen 61-smooth, per L-105031(f) + core.py conventions)

Lattice: squarefree divisors d | P_61 (2^18 = 262144 of them), P_61 = 117288381359406970983270 ≈ 1.1729e23.
Active at x: d <= x. Atoms T_x(d) = (4 sqrt(x/d) - 3)/sqrt(d) > 0 for d <= x.
Odds (mu = -1): demands. Evens (mu = +1): capacities. D = sum_o T(o).
Greedy prefix fill c*: evens ascending by d, theta*(e) = 1 below threshold e*,
partial theta*(e*) = (D - C_<)/T(e*) in (0,1], 0 above. Fill completes iff
TB_s(x) = sum_e T(e) - D = 4 sqrt(x) A^s_x - 3 B^s_x >= 0 — PROVED >= 1.676601
for all real x in [2, P61] (L-105031(f), lattice.py, complete 2^18 enumeration);
for x > P61: TB = 4 sqrt(x) prod(1-1/p) - 3 prod(1-1/sqrt p), prod(1-1/p) > 0.13,
so TB > 1e11. Hence e* exists and fill never exhausts capacity.

Margins (all three must be > 0):
  M_j(x)  = sum_e theta*(e) Q_{x/e}(j)/sqrt(e) - sum_o Q_{x/o}(j)/sqrt(o),  j = 2,3
  M_sc(x) = (3/4)[ sum_o 1/sqrt(o) - sum_e theta*(e)/sqrt(e) ]
          = (3/4)[ -B^s_x + sum_e (1-theta*(e))/sqrt(e) ]   (identical algebra)

Q_Y(j) = sum_{j<=m<=Y} gamma_j(m) log(Y/m)/sqrt(m), gamma_j(j) = A_j = (j+1)/(j-1),
gamma_j(j+1) = -B_j = -(j+1)(j-2)/(j(j-1)), gamma_j(m) = C_j = 2/(j(j-1)) for m >= j+2.
j=2: A=3, B=0, C=1.  j=3: A=2, B=2/3, C=1/3.  Q_Y(j) = 0 for Y < j. Q >= 0 (verified
cellwise below; consistent with L-99240 kernel positivity).

## 1. KEY IDENTITY (F-identity; exact, from demand equality)

Since sum_e theta* T(e) = D exactly:
  4 sqrt(x) [sum_e theta*/e - sum_o 1/o] = 3 [sum_e theta*/sqrt(e) - sum_o 1/sqrt(o)]
                                        = -4 M_sc(x)
  =>  F := sum_e theta*(e)/e - sum_o 1/o = -M_sc(x)/sqrt(x).           (F-identity)

Consequence 1 (conditioning): with q_j(Y) := Q_Y(j) - 4 C_j sqrt(Y) (define
q_j(Y) = -4 C_j sqrt(Y) for Y < j so Q = 4C_j sqrt(Y) + q_j identically),
  M_j(x) = -4 C_j M_sc(x) + [ sum_e theta* q_j(x/e)/sqrt(e) - sum_o q_j(x/o)/sqrt(o) ].
The sqrt(x)-scale parts cancel EXACTLY; q_j(Y) = O(log Y). This removes the
9-digit cancellation at x ~ 1e23 and is how the evaluator computes M_j.

## 2. LEMMA A (breakpoint structure; jumps are favorable)

Breakpoints in x: lattice activations x = d. Between activations, M_2, M_3, M_sc
are continuous and piecewise-C^1 (kinks only: floor knots Y = x/d crossing
integers, where Q is continuous since the entering term has log(Y/m) = 0; and
greedy threshold-index shifts, where the marginal term passes continuously
through theta = 0/1).

(A1) EVEN activation (x = e, mu(e) = +1): the new even is the largest active
divisor; since TB >= 1.676 held just below x = e using only evens < e, the fill
threshold satisfies e* < e, so theta*(e) = 0 on entry. M_j unchanged. M_sc in
the -B form: -B_x decreases by 1/sqrt(e), sum_e (1-theta*)/sqrt(e) increases by
1/sqrt(e): NET ZERO. Even activations are exactly margin-neutral.

(A2) ODD activation (x = o, mu(o) = -1): T jumps in at T_o(o) = (4-3)/sqrt(o)
= 1/sqrt(o). New odd's own Q_{x/o}(j) = Q_1(j) = 0 (1 < j): no loss-term jump.
Demand D jumps up by 1/sqrt(o); prefix fill is monotone in D, so theta* extends:
Delta M_j = sum_e Delta theta(e) Q_{x/e}(j)/sqrt(e) >= 0 (Q >= 0). JUMP UP.
For M_sc: Delta M_sc = (3/4)[ 1/sqrt(o) - sum_e Delta theta(e)/sqrt(e) ] and
sum_e Delta theta/sqrt(e) = sum_e Delta c(e)/(T(e) sqrt(e)) = sum_e Delta c(e)/
(4 sqrt(x/e)-3) <= sum_e Delta c(e) = 1/sqrt(o)  (since e <= x => 4 sqrt(x/e)-3 >= 1).
So Delta M_sc >= 0. JUMP UP (weakly).

Hence: activations only ever push all three margins (weakly) UP. A left-limit /
grid-plus-Lipschitz certificate that ignores jumps is CONSERVATIVE.

(A2') Jump budget (for upper bounds on M_sc over an interval): total upward
M_sc jump on (x1, x2] <= (3/4) sum_{odd d in (x1, x2]} 1/sqrt(d)  (computable).

## 3. LEMMA B (exact derivative identities on C^1 pieces; t = log x)

dT/dt = 2 sqrt(x)/d.  dQ_Y(j)/dt = Sg_j(Y) := sum_{m<=Y} gamma_j(m)/sqrt(m)
(continuous across knots). d theta*(e*)/dt = [D' - C_<' - theta* T'(e*)]/T(e*)
= 2 sqrt(x) [sum_o 1/o - sum_{e<e*} 1/e - theta*/e*]/T(e*) = -2 sqrt(x) F/T(e*)
= 2 M_sc / T(e*)   (by the F-identity).

(B1)  dM_sc/dt = -(3/4) d(theta*(e*))/dt / sqrt(e*) = -(3/2) M_sc / (4 sqrt(x/e*) - 3).

(B2)  dM_j/dt = 2 M_sc (rho_j(e*) - C_j) + R_j(x),
      R_j = sum_e theta* g_j(x/e)/sqrt(e) - sum_o g_j(x/o)/sqrt(o),
      g_j(Y) := Sg_j(Y) - 2 C_j sqrt(Y)  (= -2C_j sqrt(Y) for Y < j),
      rho_j(k) = Q_{x/k}(j)/(4 sqrt(x/k) - 3) in [0, rhobar_j].
   [Derivation: bulk 2C_j sqrt(x) F = -2 C_j M_sc by F-identity; threshold term
    (d theta*/dt) Q_{x/e*}/sqrt(e*) = 2 M_sc rho_j(e*).]

g_j(Y) -> c_j^inf := A_j/sqrt(j) - B_j/sqrt(j+1) + C_j (zeta(1/2) - S(j+1)),
S(n) = sum_{m<=n} 1/sqrt(m); and g_j(Y) = c_j^inf + C_j (deltaS(N) - 2(sqrt Y - sqrt N))
for Y >= j+2, |deltaS(N) - 2(sqrt Y - sqrt N)| <= 1/sqrt(N) + 0.25 N^{-3/2}  (see §5).

## 4. COROLLARY C (M_sc sign preservation => M_sc > 0 for ALL x >= x0)

By (B1), on every C^1 piece M_sc' = -c(x) M_sc with c(x) = (3/2)/(4 sqrt(x/e*)-3)
in (0, 3/2] (since e* <= x). Gronwall: sign of M_sc is preserved forward on each
piece; M_sc is continuous at kinks and at even activations, and jumps UP at odd
activations (Lemma A). Therefore:
    M_sc(x0) > 0  ==>  M_sc(x) > 0 for all x >= x0.
Certified numerically: M_sc(1e6) = 10.7... (rigorous error bars) — see results.
This closes M_sc on [1e6, infinity) with a SINGLE rigorous evaluation.

## 5. Rigorous envelopes (for H(Y), Y >= T0 = 1e6; elementary, self-contained)

S(N) = sum_{m<=N} 1/sqrt m = 2 sqrt N + zeta(1/2) + deltaS(N),
  deltaS(N) = sum_{m>N} 1/(sqrt m (sqrt m + sqrt(m-1))^2)  in  (0, 0.5 N^{-1/2} + 0.25 N^{-3/2}].
  [increments of deltaS are negative, limit 0 defines zeta(1/2); term bound
   (1/4)(m-1)^{-3/2}, integral comparison.]
SL(N) = sum_{m<=N} log m/sqrt m = 2 sqrt N log N - 4 sqrt N - zeta'(1/2) + deltaL(N),
  0 <= deltaL(N) <= log N / sqrt N   for N >= 8.
  [inc(N) = f(N) - int_{N-1}^N f, f = log t/sqrt t decreasing for t > e^2;
   0 <= -inc(N) <= f(N-1) - f(N), telescopes to f(N).]
H(Y) = S(N) log Y - SL(N), N = floor(Y):
  H(Y) = 4 sqrt Y + zeta(1/2) log Y + zeta'(1/2) + E(Y),
  E(Y) = c(Y) + deltaS(N) log Y - deltaL(N),  c(Y) = 2 sqrt N log(Y/N) - 4(sqrt Y - sqrt N),
  |c(Y)| <= (Y-1)^{-3/2}   [u = Y-N in [0,1), log/sqrt bracketing],
  E(Y) in [ -(Y-1)^{-3/2} - log(Y-1)/sqrt(Y-1),
            (Y-1)^{-3/2} + (0.5 (Y-1)^{-1/2} + 0.25 (Y-1)^{-3/2}) log Y ].
Matches Lane 1's numerically identified expansion (zeta'(1/2) = -3.92264613920915...).

For Y < T0: EXACT O(1) evaluation via prefix arrays a_j[N], b_j[N]:
  Q_Y(j) = a_j[N] log Y - b_j[N],  a_j[N] = sum_{m<=N} gamma_j(m)/sqrt m,
  b_j[N] = sum gamma_j(m) log m/sqrt m.
For Y >= T0: q_j(Y) = c_j^inf log Y + kappa_j^inf + C_j E(Y)  where
  kappa_j^inf = -A_j log j/sqrt j + B_j log(j+1)/sqrt(j+1) + C_j (zeta'(1/2) + sum_{m<=j+1} log m/sqrt m).
  (4 C_j sqrt Y cancels ANALYTICALLY — no large numbers.)

## 6. Certification scheme (grid + per-interval Lipschitz; sound by Lemmas A/B)

Grid t_0 < t_1 < ... (t = log x) from 1e6 to x_sat = 5 P61. On [x_i, x_{i+1}]:
  Msc_hi = M_sc(x_i) + eps_sc,i + JB_i  (JB_i = (3/4) sum_{odd d in (x_i,x_{i+1}]} 1/sqrt d);
  0 <= M_sc <= Msc_hi on the interval (Cor. C + (B1) shrink + (A2') jumps).
  L_j,i = 2 Msc_hi max(C_j, rhobar_j - C_j) + |c_j^inf| (4/3) Msc_hi + Ttilde_j,i,
  Ttilde_j,i = sum over d active at x_{i+1} of gammabar_j(d)/sqrt(d),
    gammabar_j(d) = C_j (1/sqrt(Ylo-1) + 0.25 (Ylo-1)^{-3/2}) for Ylo = x_i/d >= Ycut,
    else tgbar_j (global sup of |g_j - c_j^inf| on (0, Ycut+1], computed cellwise-exactly).
  CERTIFIED on the interval if  M_j(x_i) - eps_j,i - L_j,i (t_{i+1}-t_i) > 0
  (jumps only help; Lipschitz valid on each C^1 piece; chain across kinks by
  continuity and across activations by Lemma A).
rhobar_j: global sup of rho_j computed cellwise-exactly on [j, T0] plus a
monotone tail bound for Y >= T0 (c_2^inf, kappa_2^inf < 0 => rho_2 <= 4 sqrt Y/(4 sqrt Y - 3) there).
Numerical rounding: pairwise-sum budgets 64*eps*(sum |terms|) charged into eps_j,i;
demand-equality slack charged as C_j * |sum theta T - D|_bound; fill-placement
slack charged as epsD * rhobar_j.

## 7. RESULTS (all reproduced by scripts in this dir)

VALIDATION (validate.py, validate_out.json):
- Brute-force direct-Q greedy vs fast evaluator: diffs <= 3.1e-10 at
  x = 88, 1e4, 1.23e5, 1e6. At x=1e6 fast evaluator reproduces L-105031(f):
  M2 = 106.198615827, M3 = 39.393326023, M_sc = 10.744251467.
- mpmath 40-dps independent recomputation (anchor_hp.py):
  M_sc(1e6) = 10.744251467377188083 (f64 diff 8.6e-15, budget 2.0e-10);
  x=1e4 all three margins agree to 4.5e-12.
- H-envelope on [1e6,1e7]: measured max|E| = 3.07e-8 vs bound >= 5.1e-3
  (envelope conservative by ~1e5); 0 violations at 4100 test points.
- Derivative identities (B1),(B2) vs central finite differences at
  x = 3.777e6, 5.2e8, 7.77e12: (B1) agrees to 6 decimals; (B2) to ~1e-4
  (residual = g_j asymptotic truncation in the check itself, not the identity).
- Q >= 0 cellwise-exact on [j, 1e6): 0 negative cells (min = 0 attained at Y=j).
- rhobar_2 = 1.000751, rhobar_3 = 0.333584 (cellwise sup + analytic tail).
- tgbar_2 = 1.623491 (= |c_2^inf|), tgbar_3 = 0.593570 (= |c_3^inf|).
- |g_j - c_j^inf| <= C_j (1/sqrt(N) + 0.25 N^-1.5) verified cellwise on
  [100, 1e6) with max ratio 0.5000 (bound 2x conservative).
- F-identity residual F + M_sc/sqrt(x): <= 2.8e-15 at x = 1e6 ... 5e23.

SATURATION SEAM (agrees with Lane 1 saturated facts):
- For x >= P61: M_sc = 13.903914 (constant to 6 dp), e* = 1110, theta_p = 0.4199,
  sliver = 130941 top evens (130940 unfilled + 1 partial) — all match Lane 1.
- M2(5P61) = 1316.499, M3(5P61) = 482.152; slopes across [P61, 1e24]:
  dM2/dlog x = 30.1, dM3/dlog x = 11.0 — match Lane 1's saturated formula.

CERTIFICATION (certify.py, certificate.json):
- Anchor: M_sc(1e6) >= 10.744251467 - 2e-10 > 0  =>  Corollary C gives
  M_sc(x) > 0 for ALL x >= 1e6 (no grid needed; extends past x_sat).
- TB for x >= P61: 4 sqrt(x) * 0.131587 - 3 * 0.002214 >= 1.8e11 > 0
  (so Lemma A/B apply beyond P61; on [2, P61] TB >= 1.676601 is L-105031(f)).
- Adaptive grid (400 initial intervals, geomspace [1e6, 5 P61]): ALL 400
  certified on the first pass, 0 bisections, 0 failures.
  Worst certified interval floor: M_2 >= 98.5448 (interval starting 1e6),
  M_3 >= 36.6698 (same interval). Max Lipschitz bounds used: L_2 <= 74.74,
  L_3 <= 26.59 (measured |dM_j/dt| ~ 30.1 / 11.0 — bounds ~2.4x conservative).
- CERTIFIED: M_2(x) > 0, M_3(x) > 0, M_sc(x) > 0 for all real x in
  [1e6, 5*P61 = 5.864419e23], with M_sc > 0 in fact on [1e6, infinity).

## 8. DENSE SWEEP (sweep.py -> sweep_out.npz; 117,356 evaluations, 954 s)

Coverage: [1e6,1e9] 10,001 log-uniform + ALL 43k+ lattice-activation left-limits;
(1e9,1e12] 5,000 log-uniform + all ODD activation left-limits (~49k);
(1e12, 5*P61] 10,000 log-uniform. 92,355 of the points are activation
left-limits (where the theory says local minima sit, since margins jump UP at
odd activations and decrease/flat between).

GLOBAL MEASURED MINIMA on [1e6, 5*P61 = 5.864419e23]:
  min M_2  = 106.198616 (+- 1.4e-2)  at x = 1e6 (left edge of range)
  min M_3  =  39.393326 (+- 4.7e-3)  at x = 1e6 (left edge of range)
  inf M_sc =  10.744179 (+- 2.0e-10) at x -> 1000587^- (left-limit of first
              activations above 1e6; M_sc decreases on cells, jumps up at odds
              — exactly the (B1)/(A2) structure; all cell right-endpoints in
              [1e6,1e9] were evaluated, so this is the true infimum there)
  Zero points with (margin - error) <= 0. All minima at the bottom edge:
  margins grow with x throughout the range.
Per-decade minima table in analyze.py output (sweep.log / final report).
Trend fits on x > 1e12: M_2 = 30.0967 log x - 330.65 (residuals in
[-0.005, +0.027]); M_3 = 11.0038 log x - 120.07 (residuals [-0.002, +0.009]) —
slopes match Lane 1's saturated formula (30.1 / 11.0); oscillation amplitude
< 0.03 out there. M_sc stabilizes at 13.903914 (= Lane 1's 13.9039).

## 9. FINAL STATEMENT (this lane's deliverable)

CERTIFIED (scheme of §6; certificate.json; 400 intervals, 0 failures):
  For every real x in [1e6, 5*P61 = 5.864419e23]:
      M_2(x) > 0,  M_3(x) > 0,  M_sc(x) > 0
  for the frozen 61-smooth aggregate-licensed Hall system, with certified
  interval floors >= 98.5448 (M_2) and >= 36.6698 (M_3), and
      M_sc(x) > 0 for ALL x >= 1e6  (Corollary C, no upper limit).
  Together with TB_s(x) >= 1.676601 (L-105031(f), all real x in [2, P61]) and
  TB > 0 beyond, the frozen system is FEASIBLE for all real x in
  [1e6, 5*P61], closing Lane 2's segment of T-105040.

Honesty box:
  * The certificate is float64 with explicit conservatively-assembled error
    budgets (64x-eps summation charges, envelope half-widths, demand-equality
    and fill-placement slack, prefix-table charges), not an interval-arithmetic
    library run. Slack between certified floors (36.7+) and total error scale
    (< 2e-2) exceeds 1800x. Anchor cross-checked in 40-dps mpmath (8.6e-15).
  * Analytic inputs: Lemmas A, B, Corollary C, envelope bounds (§§2-5) are
    hand-derived here; (B1)/(B2) validated by finite differences at 3 scales;
    envelope validated against exact sums on [1e6, 1e7] (conservative by ~1e5).
  * External inputs: TB_s >= 1.676601 on [2, P61] (L-105031(f) 2^18 cell
    enumeration); Q >= 0 (reproved here cellwise + analytic tail, independent
    of L-99240).
  * The scheme certifies REAL x (not a grid): grid values + Lipschitz bounds
    on every C^1 piece + jump directions cover the continuum.

## STATUS LOG
- [x] constants verified (zeta(1/2), zeta'(1/2), P61, Sigma weights)
- [x] common.py evaluator + validation vs brute force + L-105031(f) values at 1e6
- [x] envelope validation on [1e6, 1e7]
- [x] derivative-identity finite-difference validation
- [x] mpmath anchor verification (anchor_hp.py)
- [x] certification run: SUCCESS, 0 failures (certificate.json)
- [x] dense sweep: 117,356 evals, all positive, minima measured (sweep_out.npz)
