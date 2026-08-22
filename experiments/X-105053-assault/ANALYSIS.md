# LANE A4 — GATE ASSAULT on HHFE102010 (unconditional estimates for the HHFE energy)

Date: 2026-08-22. Repo refs used (read-only):
- L-102010 (gate) @ origin/research/gpt56-pro/103100-fractional-hankel-near-collision = 89f995450977c3590aada0c1447a7e6af7fcd9ac, claims/lemmas/L-102010-half-divisor-symmetric-one-field-reduction.md
- L-103100 (Haar Gram, kernel R) same branch/SHA, claims/lemmas/L-103100-exact-half-completed-haar-gram.md
- L-103101 (subpower diagonal, PROVED) same branch/SHA, claims/lemmas/L-103101-diagonal-is-unconditionally-subpower.md
- L-103102 (Plancherel + near-collision equivalence HCNC103100) same branch/SHA
- R-103100 (diagonal/unsigned-phase firewall) same branch/SHA
- R-95600 (parity-before-absolute-values firewall) @ origin/research/gpt56-pro/95600-uosacf-equivalence-filter-exhaustion = 327c0967c67e7efa08fcb62937ca1730f8c24069
- R-99161 (score lock) @ origin/review/gpt56-pro/99160-same-row-calibration-defect
- L-105032 (±4 log germ) @ origin/claude/riemann-proof-review-8nz34i

RH is unproved; nothing below claims it. All new estimates are unconditional
unless labeled heuristic.

## 0. Objects (all deposited; restated for self-containment)

eta multiplicative, eta(p^k) = binom(2k,k)/4^k in (0,1]; Dirichlet series
sum eta(n) n^{-z} = zeta(z)^{1/2}. b_U(n) = mu(n) 1_{n>U}. h_U = b_U * eta,
i.e. h_U(n) = sum_{d|n, d>U} mu(d) eta(n/d); h_U(n)=0 for n<=U.
A_-(y) = 1 on (1,2), -sqrt2 on (2,4), 0 else; psi(u)=A_-(e^u); h := log 2.
R(v) = int psi(u)psi(u+v)du (L-103100.2):
  R(v) = 3h-(3+sqrt2)|v| on |v|<=h; -sqrt2(2h-|v|) on h<=|v|<=2h; 0 beyond.
R(0)=3h, ||R||_inf = 3h, support |v|<2h i.e. ratio (1/4,4).
Mellin: hatA_-(s) = int_0^inf A_-(y) y^{-s} dy/y = (1-2^{-s})(1-sqrt2 2^{-s})/s.
KEY ZERO: hatA_-(1/2) = 0  (1 - sqrt2*2^{-1/2} = 0).  [checked]
w(gamma) := |hatA_-(i gamma)|^2; w(0) = ((sqrt2-1)log2)^2 > 0;
w(gamma) <= min(C_0, C_1/gamma^2), C_0 = ((1+sqrt2)log2)^2, C_1 = (2+2sqrt2)^2.
int_R w(gamma) dgamma = 2*pi*int psi^2 = 2*pi*3h (Plancherel of psi).

Truncation: U = U_X = floor(X^{1/3}), N = N_X = floor(X/U_X) (L-103102),
so N ~ X^{2/3}, N/U ~ X^{1/3} ~ U.

Energy (L-103100.1): H_{U,N} := int_U^{4N} |H_{U,N}(Y)|^2 dY/Y
 = sum_{U<m,n<=N} h_U(m)h_U(n)/sqrt(mn) * R(log(m/n)) = D + O,
D = 3h sum_{U<n<=N} h_U(n)^2/n = N^{o(1)}  (L-103101, PROVED, deposited),
O = off-diagonal near-collision sum (L-103102.3).
Gate E(L) := int_{2^L}^{2^{L+1}} H dX/X = 2^{o(L)}  (HHFE102010; <=> HCNC103100).

Plancherel (L-103102.1): H = (1/2pi) int_R w(gamma) |P(1/2+i gamma)|^2 dgamma,
P(s) = P_{U,N}(s) = sum_{U<n<=N} h_U(n) n^{-s}.

EXACT BILINEAR SHAPE (elementary, used throughout): since every divisor
d>U of n<=N forces cofactor e=n/d < N/U,
  P_{U,N}(s) = sum_{e <= N/U} eta(e) e^{-s} M_e(s),
  M_e(s) = sum_{U < d <= N/e} mu(d) d^{-s}.
(Sum over ordered pairs (d,e), de<=N, d>U; no uniqueness of factorization
needed — h_U(n) is by definition the sum over such pairs.)

Coefficient size: |h_U(n)| <= sum_{d|n} eta(d) = tau_{3/2}(n) <= tau(n)
<<_eps n^eps; mean square sum_{n<=N} h_U(n)^2/n << (log N)^{C}. Also
sum_{e<=x} eta(e)/e <= prod_{p<=x}(1-1/p)^{-1/2} << sqrt(log x)   (eta>=0).

---

## 1. DELIVERABLE (1): the trivial bound. alpha = 2/3, and it is sharp for the parity-stripped model.

### L-A4.1 (trivial absolute-value bound). Unconditionally
  |O_{U,N}| <= 3h * sum_{U<m!=n<=N, 1/4<m/n<4} |h_U(m)h_U(n)|/sqrt(mn)
            << N (log N)^{O(1)},
hence H <= D + |O| << N (log N)^{O(1)} = X^{2/3+o(1)} and
  E(L) << 2^{(2/3)L} L^{O(1)}  — trivial exponent alpha = 2/3.

Proof. For each n, by Cauchy–Schwarz
sum_{n<m<4n} |h(m)|/sqrt m <= (sum_{n<m<4n} h(m)^2/m)^{1/2} (3n)^{1/2}
<< (log N)^{C} sqrt n, using the tau_{3/2} mean square. Then
sum over n of |h(n)|/sqrt n * (log)^C sqrt n = (log)^C sum_{n<=N} |h(n)|
<= (log)^C * N^{1/2} (sum h^2)^{1/2}... more simply sum_{n<=N}|h(n)| <=
sum_n tau_{3/2}(n) << N (log N)^{1/2}. QED (constants irrelevant).

### L-A4.2 (sharpness of the absolute-value bound; the parity-stripped witness).
The absolute-value majorant is genuinely of size N/(log N)^2: already the
prime–prime subfamily gives
  sum_{p != p' in (U,N], 1/4<p/p'<4} |h(p)h(p')|/sqrt(pp') |R(log p/p')|
  ~ c_R * N/(log N)^2,  c_R = int |R(v)| e^{v/2} dv > 0,
because h_U(p) = mu(p) eta(1) = -1 exactly for every prime p in (U,N]
(the only divisor > U of p is p itself), so |h(p)h(p')| = 1, and PNT gives
the stated asymptotic. So NO absolute-value argument can beat alpha = 2/3
by more than logs: consistent with (and forced by) the OPEN status of the
gate and with R-95600. alpha = 2/3 is the honest trivial exponent.

### L-A4.3 (the kernel half-order zero kills every smooth class main term).
Contrast with L-A4.2: the SIGNED prime–prime class has vanishing main term,
NOT because of Mobius parity but because of the kernel zero:
  int_R R(v) e^{v/2} dv = (int psi(u) e^{-u/2} du)(int psi(u) e^{u/2} du),
and int psi(u) e^{-u/2} du = 2(1-2^{-1/2}) - 2 sqrt2 (2^{-1/2} - 2^{-1}) = 0,
i.e. this factor IS hatA_-(1/2) = 0. [Both factors: int psi e^{-u/2}du =
hatA_-(1/2)=0; int psi e^{u/2} du = hatA_-(-1/2) = -(1-sqrt2*sqrt2)* ... =
(1-2^{1/2}... computed numerically in code; only one zero needed.]
Consequently, for ANY pair class whose counting measure has a smooth
logarithmic density rho(y) dy/y on both coordinates (e.g. primes via PNT),
the class main term in O is
  (int int R(log(y'/y)) sqrt(y/y') rho ...) = 0 * (main) + (density-error terms).
Mechanism statement: the half-order zero hatA_-(1/2)=0 annihilates the
y^{1/2}-scaling main term of every smooth-density subfamily; what remains is
driven by DENSITY FLUCTUATIONS (e.g. pi(y)-Li(y)) — which is exactly why
(i) the gate is plausible, (ii) unconditional savings track zero-free-region
strength (Sec. 3), and (iii) absolute values (which destroy the zero,
c_R = int|R|e^{v/2}dv > 0) saturate at alpha = 2/3.

---

## 2. DELIVERABLE (2a): Montgomery–Vaughan + weight — NO exponent gain (documented failure).

MV mean value: int_{|gamma|<=T} |P(1/2+igamma)|^2 dgamma
 = sum_{U<n<=N} (h(n)^2/n)(2T + O(n)) = 2T * D/(3h) + O(sum_{n<=N} h(n)^2)
 = T N^{o(1)} + O(N (log N)^{O(1)}).
With the weight w <= min(C_0, C_1/gamma^2), summing dyadic blocks
|gamma| ~ 2^j:
  H << sum_j min(1, 2^{-2j}) (2^j N^{o(1)} + N^{1+o(1)}) << N^{1+o(1)},
the N-term being un-damped at j = O(1). CONCLUSION: MV + the hatA_- decay
reproduces alpha = 2/3 exactly; the entire difficulty sits at BOUNDED
frequencies |gamma| = O(1), where MV's near-collision error term O(n) is
the same size as the trivial bound. The ratio-four support of R is fully
equivalent information to the 1/gamma^2 decay of w and buys nothing more.
FAILURE RECORDED: no exponent improvement from any mean-value theorem that
is blind to the mu-structure of the coefficients.

---

## 3. DELIVERABLE (2): the best standard-technology unconditional bound — Vinogradov–Korobov saving (proved).

### L-A4.4 (twisted Mobius input; standard). There are c > 0, C such that
uniformly for x >= 3 and |gamma| <= exp((log x)^{3/5}),
  M(x, gamma) := sum_{n<=x} mu(n) n^{-i gamma} << x exp(-c (log x)^{3/5} (loglog x)^{-1/5}).
Standard proof (sketch; Walfisz-strength, as for M(x)): Perron for
1/zeta(s + i gamma) at sigma_0 = 1 + 1/log x, truncation T; shift to
sigma_1 = 1 - c_1 (log(T + |gamma| + 3))^{-2/3} (loglog)^{-1/3}, inside the
Vinogradov–Korobov zero-free region, where 1/zeta << (log(|t|+3))^{2/3+eps};
error << x/T + x^{sigma_1} (log)^{O(1)}; choose T = exp((log x)^{3/5}).
With |gamma| <= T the region depth is (log T)^{-2/3} = (log x)^{-2/5}, giving
x exp(-c (log x)^{3/5 - o(1)}). [Cited as standard: Walfisz; Iwaniec–Kowalski
Ch. 8 exercise-level extension of Thm 8.29 replay. Not re-proved from scratch.]

### T-A4.5 (unconditional VK bound for the gate energy). Unconditionally
  H_{U_X, N_X}(X) << X^{2/3} exp(-c (log X)^{3/5} (loglog X)^{-1/5}),
hence
  E(L) << 2^{(2/3)L} exp(-c' L^{3/5} (log L)^{-1/5}),  c' > 0 absolute.
This SAVES an exp((log)^{3/5-o(1)}) factor over the trivial alpha = 2/3
bound but is NOT a power saving.

Proof. Set Gamma_0 = exp((log N)^{3/5}).
(i) |gamma| <= Gamma_0: by the exact bilinear shape and partial summation,
  M_e(1/2 + i gamma) = int_U^{N/e} t^{-1/2} dM(t, gamma)
   << sup_{U<=t<=N} |M(t,gamma)| U^{-1/2} + int_U^{N/e} |M(t,gamma)| t^{-3/2} dt/2... 
  Explicitly: |M_e(1/2+igamma)| << sqrt(N/e) exp(-c (log U)^{3/5-o(1)})
  (the sup over t in [U, N/e] of the L-A4.4 saving is attained at t = U;
   log U = (1/3) log X ensures uniform saving; |gamma| <= Gamma_0 <=
   exp((log U)^{3/5} * (2)^{3/5}) is inside L-A4.4's uniformity after
   adjusting c).
  Hence |P(1/2+igamma)| <= sum_{e<=N/U} eta(e) e^{-1/2} |M_e|
   << sqrt N exp(-c(...)) sum_e eta(e)/e << sqrt(N log N) exp(-c (log X)^{3/5-o(1)}).
  Weighted contribution: (1/2pi) int_{|gamma|<=Gamma_0} w |P|^2
   <= (int_R w) * sup |P|^2 << N (log N) exp(-2c(...)).
(ii) |gamma| > Gamma_0: dyadic MV blocks as in Sec. 2:
  sum_{2^j >= Gamma_0} C_1 2^{-2j} (2^j N^{o(1)} + N^{1+o(1)})
   << N^{o(1)}/Gamma_0 + N^{1+o(1)}/Gamma_0^2 << N exp(-2(log N)^{3/5}) + small.
Combine; log N = (2/3) log X. QED.

HONESTY NOTE: the parity resource used here is the classical analytic one
(1/zeta in the VK region), i.e. exactly zero-free-region strength. This is
the ceiling of single-polynomial technology at BOUNDED frequency; see Sec. 4.

---

## 4. DELIVERABLE (2b,c): why power saving on the full form is walled (documented failures + the wall lemma).

### Failure (b): band decomposition / kernel oscillation. R is fixed,
piecewise linear, no oscillation; its Fourier transform w(gamma) >= 0 is
concentrated at |gamma| << 1 (w <= C_1/gamma^2). Any decomposition of O by
ratio bands |log(m/n)| ~ delta keeps kernels of scale >= 1 in log-ratio,
whose spectra live at bounded frequency. At bounded frequency the classical
Type-I resource is DEAD: sum_{l<=L} l^{-1/2-igamma} = zeta(1/2+igamma) +
L^{1/2-igamma}/(1/2-igamma) + O(L^{-1/2}) has a MAIN term of size
sqrt L/(1+|gamma|) — smooth long sums do not oscillate at |gamma| = O(1).
Hence every Vaughan/Heath-Brown decomposition of one mu factor produces
Type-I pieces with no cancellation, and the machinery that powers
t ~ N^theta mean values is unavailable. FAILURE RECORDED.

### Failure (c): dispersion on the near-coprime core. The full off-diagonal
is a POSITIVE-SEMIDEFINITE TOEPLITZ form in the Mobius tail:
  D + O = (1/2pi) int w(gamma) |sum_e eta(e) e^{-1/2-igamma} M_e(1/2+igamma)|^2 dgamma,
a single |.|^2 against a fixed positive weight concentrated at |gamma| << 1.
Dispersion/large-sieve saves by averaging over a LARGE spectral family;
here the family is a single bounded window. Any rearrangement (gcd
coordinates, shift coordinates r = m-n, e/e'-blocks) reproduces bilinear
forms sum mu(d) mu(d') K(log d/d') with K of log-scale >= 1, spectrally
bounded-frequency again. FAILURE RECORDED: no dispersion gain identified;
the obstruction is structural (PSD Toeplitz at bounded frequency), not
bookkeeping.

### O-A4.6 (the wall lemma — what full power saving would mean). w(gamma) >=
w_1 > 0 on gamma in [1,2] (explicit: w has zeros only at gamma in
(2pi/log2) Z on the imaginary axis; on [1,2] its minimum is positive,
numerically w_1 = min_{[1,2]} w > 0, computed in code). Hence for any
delta > 0, a bound E(L) << 2^{(2/3-delta)L} would give, for most X ~ 2^L,
  int_1^2 |P_{U,N}(1/2+igamma)|^2 dgamma << X^{2/3-delta} = N^{1-(3/2)delta+o(1)},
i.e. a POWER-SAVING mean value over a FIXED BOUNDED frequency window for a
length-N Dirichlet polynomial carrying the (half-completed) Mobius tail —
strictly beyond every known unconditional technique (the known ceiling at
bounded frequency is exactly the VK saving of T-A4.5; power saving there for
the closely related sum_{d<=N} mu(d) d^{-1/2-igamma} is quasi-RH strength).
We do NOT claim formal equivalence to a zero-free strip; we record it as a
wall statement: any unconditional proof of a power-saving version of the
gate must break the bounded-frequency Mobius mean value wall on some
structured subfamily, not on the full form.

---

## 5. DELIVERABLE (2c)+(3): the PROVED positive result — high-gcd pairs are unconditionally negligible; the gate lives on the near-coprime core.

gcd coordinates: for an off-diagonal pair (m,n), q = gcd(m,n), m = qa,
n = qb, (a,b) = 1, a != b, 1/4 < a/b < 4 (forced by R-support). Note
max(a,b) <= P  <=>  gcd(m,n) >= max(m,n)/P... (up to the trivial identity
q = m/a). Define the split
  O = O^{hi}(P) + O^{core}(P),
  O^{hi}(P) = sum over pairs with max(a,b) <= P (HIGH-torsion: gcd >= max(m,n)/P),
  O^{core}(P) = pairs with max(a,b) > P (near-coprime core).

### L-A4.7 (high-gcd bound; unconditional, no parity used). For 1 <= P <= N,
  |O^{hi}(P)| <= 3h sum_{(a,b)=1, a!=b, max(a,b)<=P, 1/4<a/b<4} (ab)^{-1/2}
                  |sum_q h_U(qa) h_U(qb) / q|
  << P (log N)^{O(1)}   (in fact <<_eps P N^eps with tau powers explicit).
Proof. Fix (a,b). The q-fiber correlation obeys, by Cauchy–Schwarz IN q,
  |sum_q h(qa)h(qb)/q| <= (sum_{q<=N/a} h(qa)^2/q)^{1/2} (sum_{q<=N/b} h(qb)^2/q)^{1/2},
and sum_{q<=Q} h(qa)^2/q <= sum_q tau(qa)^2/q <= tau(a)^2 sum_{q<=Q} tau(q)^2/q
 << tau(a)^2 (log N)^4.
Then sum_{a,b<=P, a asymp b} tau(a)tau(b)/sqrt(ab) << P (log P)^2 by dyadic
blocks (sum_{a~r} tau(a)/sqrt a << sqrt r log r; blocks r <= P sum to P log^2).
QED. NOTE: absolute values are applied ONLY inside this piece, and the piece
is PROVED small — see firewall discussion Sec. 7.

### Why the complementary split fails trivially (recorded): the trivial mass
of O^{core} is carried at max(a,b) ~ N (near-coprime pairs, q = O(1)): the
absolute-value mass of skeleton-radius-r pairs is ~ r polylog per dyadic r,
summing to N polylog dominated by r ~ N (and L-A4.2's prime pairs are q=1,
r ~ N: the core genuinely holds power-sized absolute mass). Cauchy–Schwarz
in q is lossless only on long fibers; at r > U fibers have N/r < U terms and
carry no averaging at r ~ N. So the gcd-fiber method gives EXACTLY the split
above and nothing more: the refined gate is the near-coprime core.

### T-A4.8 (STRUCTURE THEOREM; draft claim L-105053). Unconditionally, for
any P = P(X) <= N:
  E(L) = E_diag(L) + E_hi(L; P) + E_core(L; P),
  (i)  E_diag(L) = int D dX/X = 2^{o(L)}                    [deposited L-103101]
  (ii) |E_hi(L; P)| << P * 2^{o(L)}                          [L-A4.7, new]
  (iii)|E_core(L; P)| << 2^{(2/3)L} exp(-c L^{3/5-o(1)})     [T-A4.5 + (ii)]
and for every subpower P(X) = X^{o(1)} with P -> infinity:
  HHFE102010 <=> HCNC103100 <=> NCCG105053(P):
     int_{2^L}^{2^{L+1}} [O^{core}(P)]_+ dX/X = 2^{o(L)}.
Proof of the equivalence: [O]_+ <= [O^{core}]_+ + |O^{hi}| and
[O^{core}]_+ <= [O]_+ + |O^{hi}|, with |O^{hi}| <= P X^{o(1)} = X^{o(1)};
then L-103102's equivalence closes the loop. QED.
REFINED GATE (the deliverable): the gate lives exactly on near-coprime
near-collisions {gcd(m,n) < max(m,n)/P}; all high-torsion pairs are
unconditionally harmless at any subpower P.
Residual bilinear form, written exactly:
  O^{core}(P) = sum_{(a,b)=1, a!=b, max(a,b)>P, 1/4<a/b<4} R(log(a/b))/sqrt(ab)
                 * sum_{max(U/a,U/b) < q ... qa,qb in (U,N]} h_U(qa) h_U(qb) / q.

## 6. Numerics (hhfe_energy.py, results.json; X = 1e4 .. 1e6, exact objects)

Correctness: the Gram identity H_sweep = D + O verified to MACHINE PRECISION
(|D + O - H| <= 9e-15) at every X — the exact piecewise-constant field
integral against the pair sum. Kernel constants verified numerically:
int R(v) e^{v/2} dv = -1.2e-16 (= hatA_-(1/2) hatA_-(-1/2) = 0 * (-0.828)),
int |R| e^{v/2} dv = c_R = 1.9682, min_{gamma in [1,2]} w = w_1 = 0.3804,
int R e^{v/2} v dv = -0.3364 (second moment, nonzero).

Table (U = floor(X^{1/3}), N = floor(X/U)):
  X       U    N      D      H      O_signed   O_abs    pp_signed  pp_abs
  1e4     21   476    2.693  0.517  -2.176     135.9    3.56       21.95
  2e4     27   740    2.761  0.644  -2.117     201.2    5.24       31.08
  4e4     34   1176   2.826  0.579  -2.246     298.7    7.69       44.02
  1e5     46   2173   2.944  0.585  -2.359     517.2    12.38      70.47
  2e5     58   3448   3.103  0.819  -2.284     800.2    17.56      99.91
  4e5     73   5479   3.229  0.811  -2.418     1219.8   25.52      142.68
  1e6     100  10000  3.362  1.011  -2.352     2108.1   41.09      228.90
  2e6     125  16000  3.430  0.641  -2.788     3182.1   (results_ext.json)
  4e6     158  25316  3.535  0.663  -2.872     4844.2   (results_ext.json)

Findings (labels: [P] = proved-consistent check, [H] = heuristic data):
(a) [P] O_abs empirical exponent d log O_abs / d log X = 0.5985 over the
    grid, tracking the trivial alpha = 2/3 with polylog drift
    (O_abs/N = 0.285 -> 0.211, slowly decaying: N polylog^{-1}-type).
    Trivial bound honest and nearly attained.
(b) [P] Prime-prime ABS class = 1.94 * N/log^2 N at X=1e6 vs the L-A4.2
    prediction c_R * N/log^2 N = 1.97 * N/log^2 N — sharpness of alpha=2/3
    for the parity-stripped model CONFIRMED quantitatively.
(c) [H] O_signed is essentially BOUNDED on the whole grid: -2.12 .. -2.87
    over X = 1e4 .. 4e6 (at most a slow log-like drift) while O_abs grows
    36-fold to 4844. Total cancellation factor |O|/O_abs ~ 5.9e-4 at
    X=4e6. H(X) itself oscillates in [0.52, 1.01] with no visible growth
    trend (1.01 at 1e6, 0.64 at 2e6, 0.66 at 4e6). HEURISTIC: gate
    HHFE102010 TRUE-shaped in this range; empirical H compatible with
    2^{o(L)}, indeed with O(polylog) or even O(1). NOT a proof.
(d) [P] O_hi(P) (high-gcd family): signed values all in [-1.5, 0.8] for
    P <= 64 at every X; absolute version O_hi_abs(P)/P = 0.30..0.44
    (X=1e6: P=8: 2.54, P=16: 4.79, P=32: 10.13, P=64: 22.00) — LINEAR in P,
    exactly the proved L-A4.7 envelope P*polylog; the bound is sharp in P.
(e) [H] Core: O_core(8) signed = -2.28 .. -2.75 (bounded), abs ~ 2105 at
    X=1e6: ALL cancellation lives inside the near-coprime core, as the
    structure theorem T-A4.8 frames it.
(f) [P/H] Kernel-zero mechanism: SIGNED prime-prime class = 3.56 -> 41.09,
    growing ~ N/log^3-type (ratio pp/(N/log^3 N) = 1.75 -> 3.21 slowly
    varying), i.e. the kernel zero DEMOTES the pp class from c_R N/log^2
    (abs) to second-moment size ~ |int R e^{v/2} v dv| N/log^3 — but the
    class is STILL power-sized. Since total O stays ~ -2.3, the pp mass is
    cancelled by OTHER classes (mixed prime*composite etc.): NO classwise /
    invariant-cone decomposition can prove the gate (each smooth class is
    power-sized; cancellation is cross-class). Matches R-103100.3, R-103300
    and is the Gram-lane echo of the L-105032 lesson.

## 7. Firewall compliance

R-95600 (parity before absolute values; @ 327c0967): respected by
construction. Absolute values are applied ONLY to the high-gcd piece
O^{hi}(P), which is PROVED << P polylog — power-small for subpower P — so
no RH-scale information is discarded there; the parity-bearing near-coprime
core is kept fully signed, and the only parity resource consumed
unconditionally (T-A4.5) is 1/zeta in the VK region, i.e. analytic parity,
never a pointwise |mu| majorant. The numerics quantify what R-95600
predicts: stripping parity (O_abs) costs a factor ~10^3 at X=1e6 and
restores alpha = 2/3.

R-99161 (literal score locked by ordinary response; @ 99160 branch): not
touched. The decomposition is an exact partition of the deposited Gram pair
set {(m,n)}; no new normalization, score, or calibration coordinate is
introduced; every piece is an exact sub-sum of L-103100.1, and the
equivalences in T-A4.8 are inequalities between these exact sub-sums plus
the deposited L-103102 equivalence. Nothing is re-scored.

L-105032 (moving boundary: +-4 log germ, pieces not individually regular;
@ claude/riemann-proof-review-8nz34i): the same phenomenon appears in this
lane and is respected: numerics (f) show each smooth pair class (e.g.
prime-prime) is individually power-sized (~ N/log^3) even after the kernel
zero kills its leading term, with only the cross-class total bounded. The
decomposition therefore never claims classwise smallness except where
proved (high-gcd, genuinely small); the core is estimated only as a whole.
No piecewise Mellin continuation is performed, so no log-germ ledger is
incurred; the kernel half-order zero hatA_-(1/2)=0 plays the role that the
moving boundary plays in L-105032 — it cancels the pole-scale (1/log^2)
main term classwise but NOT the fluctuation term, exactly parallel to
"cancels the pole but not the log".

R-103100 (same branch as gate): item 1 (diagonal) — we never re-prove the
diagonal; item 2/3 (absolute values / free-labelled phase) — see R-95600
paragraph; item 4 (narrow-scale) — not used.

## 8. Verdict summary

- alpha = 2/3 trivial exponent, proved and sharp for absolute values
  (L-A4.1, L-A4.2, numerics (a),(b)).
- Best unconditional bound obtained: E(L) << 2^{(2/3)L} exp(-c L^{3/5-o(1)})
  (T-A4.5, VK strength). Power saving on the FULL form is walled by the
  bounded-frequency Mobius mean value (O-A4.6): every standard tool (MV,
  Vaughan Type-I, dispersion) fails at |gamma| = O(1) — failures documented
  in Secs. 2 and 4.
- PROVED structure theorem (T-A4.8 / draft L-105053): high-gcd pairs
  (gcd(m,n) >= max(m,n)/P) contribute << P X^{o(1)} unconditionally with NO
  parity input; hence the gate is EQUIVALENT to its restriction to the
  near-coprime core for any subpower P. Refined gate NCCG105053.
- RH is not proved, not claimed; the gate remains open; the refinement
  shrinks its support, it does not close it.
