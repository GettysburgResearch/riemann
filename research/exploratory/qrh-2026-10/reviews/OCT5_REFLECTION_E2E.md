# End-to-end numerical test of eq:reflection (OpenAI Oct 5 manuscript, Prop. lem:reflection)

```text
Status: EXPLORATORY numerics (finite, FLOAT); external, unreviewed manuscript. No proof is claimed.
Scope: paper2.tex Prop. lem:reflection, eq:reflection (lines ~1790-1810) with the constant C, psi,
  kappa_0, sigma_p, epsilon_p, omega_{p,j}, B_{p,j} of App. app:fixed-ray (lines 2874-3433).
  Tested on 13 parameter families (28 (family, X) pairs, 56 runs with the two test functions):
  S = {(2),(lambda)}, Psi_0 in {1, (lambda/.)_3^2}, P = {} or one or two primes of norm 7 or 13,
  j_p in {0,...,5}, X from 30 to 20000. Weights: two Schwartz-class log-Gaussian test functions,
  not compactly supported (see Section 5).
Exact sources or dependencies:
  pr908:standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
    The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex,
    sha256 d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d (re-hashed this session).
  Reused, not modified: reviews/oct5_r3_theta_checks.py (sha256 504d84f3...b16e: tau, tau_1, tau_2,
    Euclid/CRT, cub_el), a2/eis.py (sha256 87ca11d9...8e65: residue symbols, gamma_j, e).
  New: reviews/oct5_reflection_e2e_gauss.c (sha256 b5c3cbe2...76b1),
       reviews/oct5_reflection_e2e_tables.py (sha256 6e18cd9d...79c3),
       reviews/oct5_reflection_e2e.py (sha256 54bf63ee...0ad0).
What was actually run (nice -n 10; at most 2 processes; Python 3.13, numpy 2.5.3, scipy 1.18.1,
  mpmath 1.3.0; gcc 13.3 -O2):
  gcc -O2 -o gauss oct5_reflection_e2e_gauss.c -lm
  python3 -I oct5_reflection_e2e_tables.py 1000000 tables_1e6.npz ./gauss     (248 s)
  python3 -I oct5_reflection_e2e.py tables_1e6.npz e2e_1e6.json               (230 s)
  Outputs are in the session scratchpad and are not committed (e2e_1e6.json sha256
  60e1ebcd7db7bbdfaf1b1e58c9d34efe4518e1a9f593b7e7cb3152ec675b7bb9). Rerun to reproduce.
  Labels: FLOAT = ordinary double precision, not directed and not certified. Residue symbols,
  matrices, CRT and fraction reduction are EXACT (Python integers).
Smallest remaining gap: compactly supported W, the hypothesis of Prop. prop:R, was not run. With
  a C_c^infty weight the Fourier bandwidth makes the dual range about 10^8 or more (R3's estimate),
  which is out of budget here. The identity was tested only for Schwartz-class log-Gaussian V_*.
  The proof uses only Mellin inversion and contour shifts, which are valid for these weights, but
  the compact-support case itself was not tested numerically. Also untested: inert primes in P,
  three or more primes in P, and non-cubic ray-class Psi_0. No higher-precision replay was run.
```

RH remains unsolved. This note checks one identity, eq:reflection, numerically. It does not test the large-sieve step,
Prop. prop:R, or anything downstream. Finite floating-point agreement is evidence, not a proof.

## 0. Verdict

**eq:reflection is numerically confirmed.** On every tested case both sides agree to a relative
error of 7e-15 to 3.6e-10. The error is explained by the measured truncation of the two sums: the
LHS cut at N(n)N(b)^3 <= 10^6 and the dual cut at N(lambda^4 l) <= 10^6. The agreement holds:

* for both the per-translate form (RHS1, derived independently here) and the paper's grouped form
  with its constant C (RHS2);
* for all three cusps sigma in {0,+,-};
* for every local case j = 0..5 (j = 0 both active and inactive);
* for two conjugate primes of norm 7, a prime of norm 13, and the pair {norm 7, norm 13};
* for two test functions and X from 30 to 20000.

Every failing control that changes anything breaks the agreement by a relative amount of 0.16 to
13.8. That is at least 4·10^8 times the largest achieved error.

No discrepancy and no convention problem was found.

## 1. The identity as tested

Notation follows paper2. O = Z[omega], lambda = 1 + 2 omega, and primary means == 1 mod 3. The
characters are e(z) = exp(4 pi i Im z/sqrt3) and echeck(z) = exp(2 pi i (z + conj z)).
chi_p = (./p)_6, with chi_p^j extended by zero (chi_p^0 = 1_{p not | .}). Also alpha(x) = x/|x|.

The test uses S = {(2), (lambda)} and the fixed modulus L = 18. phi is 18-periodic, which was checked
EXACTLY on 300 random shifts. M = lambda^12 L^4, as in the paper.

**Concrete instance (row "rho2_p7a_j1").**

* Psi_0(n) = (lambda/n)_3^2, which is conj((lambda/n)_3). It is a ray-class character mod 9,
  extended by zero on S.
* P = {p}, p = 1 + 3 omega (N(p) = 7), j_p = 1. So Psi(n) = Psi_0(n) chi_p(n), the sextic twist of
  a prime row k = p.
* Then phi(n) = chi_n(lambda)^2 Psi_0(n) = 1_{n == 1 (3), 2 not| n}.
* phihat(h_0) != 0 for 36 of the 324 classes h_0 mod 18.
* A = {p} is forced, c = c_0 p with N(c_0) in {1, 4}, and N(c) in {7, 28}. All three cusps occur.

**LHS (eq:T).**

T(X;Psi) = sum_{n sqfree primary, (n,S)=1} sum_{b primary, (b,S)=1}
  conj(alpha(n)) gamma_2(n) Psi(n) conj(alpha(b))^3 Psi(b)^3 / (sqrt(N n) N b) * V_*(N(n) N(b)^3 / X),

with gamma_2(n) = N(n)^{-1/2} sum_{x mod n} chi_n(x)^2 e(x/n).

**RHS (eq:reflection with App. app:fixed-ray).**

T(X;Psi) = sum_{h_0: phihat(h_0) != 0} C(h_0) sum_{0 != l in lambda^{-4} O}
  d_sigma(l) alpha(l) N(l)^{-1/2} psi(lambda^4 l) B_{p,1}(lambda^4 l) Vsharp(N(l) X / N(c)^2),

where:

* B_{p,1} = chi_p^{-3} = chi_p^3 (quadratic).
* psi(m) = e(-delta'_0 r^{-1} m / D_0), with D_0 = lambda^3 c_0 and r = p.
* C(h_0) = -(i/81) conj(alpha(c))^2 phihat(h_0) conj(kappa_0) chi_p(sigma_p)^{-2} omega_{p,1}.
* omega_{p,1} = chi_p(-1) gamma_1(p) gamma_3(p) chi_p(epsilon_p)^{-3}.
* sigma_p = lambda^2 c/p and epsilon_p = -((lambda^3 c/p) sigma_p)^{-1}, both mod p.
* kappa_0 = kappa(g_1) chi_p(a)^{-2}, with kappa(g_1) = (c_1/a_1)_3.
* d_sigma(l) = conj(t_sigma(-l)), where t_0 = tau, t_-(l) = omega^2 tau_1(omega^2 l) echeck(l) and
  t_+(l) = omega tau_2(omega l) echeck(l).
* The weight is Vsharp(x) = (2 pi i)^{-1} int_{(0)} Vhat_*(-t) Gamma(7/6+t)Gamma(5/6+t) /
  (Gamma(7/6-t)Gamma(5/6-t)) ((2pi)^4 x/27)^{-t} dt.

All construction data are computed exactly as App. app:fixed-ray prescribes:

* h_p == 0 mod M^2 representatives;
* z_h = a/c in lowest terms, normalized (a == 1 mod 3 if lambda | c, else c == 1 mod 3);
* delta' from the three congruences;
* H and sigma from the paper's three-case rule;
* g_1 = g H^{-1} == I mod 3.

For general P, B_{p,j} and omega_{p,j} follow eq:theta-local-factors and the omega_{p,j} display.
Inactive j = 0 primes contribute (1 - 1/N(p)).

## 2. Implementation (independent pieces)

* **LHS.** gamma_2(n) is built by twisted multiplicativity from prime cubic Gauss sums. The sums
  are computed in C over all 78,549 primary primes of norm <= 10^6.
  * Checks: C vs R3's g1_prime, 423 primes, 3.6e-15.
  * g1(conj p) = conj g1(p): 4.4e-15. This identity is used to halve the work.
  * gamma_2 vs direct eis.gamma: 109 n, 2.0e-15.
  * The sum covers 282,269 n and 31 b.
* **RHS1, per translate.** The term is
  -(i/81) c_F(h) conj(kappa(g_1)) conj(alpha(c))^2 sum_l d alpha N^{-1/2} echeck(-delta' l/c) Vsharp.
  This file derives it from eq:theta-cusp-automorphy, eq:theta-mellin-functional-equation and
  eq:dual-cusp-mellin-series. Its inputs are independent of the paper's closed forms:
  * c_F is computed by direct finite Fourier sums, not by eq:ray-fourier.
  * kappa(g_1) = (c_1/a_1)_3 comes from a big-integer cubic Jacobi-symbol algorithm (Euclid plus
    cubic reciprocity, with supplementary laws tabulated mod 9 from primes). It does not use
    eq:ray-multiplier. It has 0 mismatches against R3's factorization-based cub_el on 400 random
    pairs.
* **RHS2, grouped.** This is the paper's formula: C, psi, B_{p,j}, omega_{p,j}, sigma_p, epsilon_p.
  Within each group (h_0, A) the following were EXACTLY constant across all h_p in every case:
  the normalized c, the cusp sigma, kappa_0, and delta' mod D_0. This confirms the claims behind
  Lemma lem:reflection-uniformity for the tested families. The reduced denominator c/r agreed with
  that of lambda^2 h_0/L up to a unit in every translate (asserted).
* **Dual coefficients.** d_0, d_+ and d_- were evaluated at all 3,627,558 lattice points with
  N(lambda^4 l) <= 10^6, of which 2,499,624 are nonzero. The code re-implements R3's DR
  (5.7)/(5.13)/(5.14) transcriptions, from one factorization per point. It matches R3's functions
  to 1.6e-13 on 3,738 points. R3 had validated those functions by automorphy (checks A, B, E, F).
* **Vsharp.** Computed by the trapezoid rule on Re t = 0 with closed-form Vhat_*. A cubic spline in
  ln x (h = 5e-4) is used for evaluation. Two cross-checks:
  * against an mpmath Mellin-Barnes quad (20 digits): <= 7.4e-15 at x in {0.003, ..., 400};
  * against an independent real-space representation
    Vsharp(x) = int V_*(y) G^{2,0}_{0,4}(y (2pi)^4 x/27 | 7/6, 5/6, -1/6, 1/6) dy/y
    (mpmath meijerg): <= 4.3e-15.
* **Test functions.**
  * TF1: V_*(y) = exp(-(ln y)^2/0.5).
  * TF2: V_*(y) = ln(y/2) exp(-(ln(y/2))^2/0.405), which changes sign.

## 3. Results

Each row gives:

* the relative errors |RHS - LHS|/|LHS|;
* tail = the change in RHS1 between cutting N(lambda^4 l) at 5e5 and at 10^6, relative to |LHS|;
* Vtail = sup |Vsharp| beyond the dual cut;
* V*cut = V_*(10^6/X) at the LHS cut.

Controls are listed in the order:
(a) kappa instead of conj kappa, in RHS1;
(b) alpha(c)^2 instead of conj(alpha(c))^2;
(c) echeck(-delta' l/c) dropped;
(d) psi dropped, in RHS2;
(e) B_{p,j} built with the conjugate-convention exponent -j+2, so B_{p,1} = chi_p, sextic;
(f) conj kappa_0 replaced by kappa_0;
(g) C with +i/81 instead of -i/81.

| family | X | TF | abs LHS | RHS1 | RHS2 | tail | Vtail | V*cut | controls (a)-(g) |
|---|---|---|---|---|---|---|---|---|---|
| Psi_0=1, P={} (sigma=0 only) | 600 | 1 | 0.252 | 6.2e-14 | 6.2e-14 | 1.4e-11 | 1.4e-13 | 2e-48 | 3.42 0* 1.00 1.00 0* 3.42 2.00 |
| | 3000 | 2 | 0.0514 | 5.9e-14 | 5.8e-14 | 3e-16 | 3e-16 | 4e-28 | 0.93 0* 1.00 1.00 0* 0.93 2.00 |
| | 20000 | 2 | 0.0065 | 2.1e-10 | 2.1e-10 | 2e-15 | 3e-16 | 2.5e-11 | 13.8 0* 1.00 1.00 0* 13.8 2.00 |
| Psi_0=rho^2, P={} (all 3 cusps) | 30 | 1 | 0.258 | 4.0e-14 | 4.0e-14 | 2e-16 | 4e-16 | 6e-95 | 0.50 0* 1.42 1.42 0* 0.50 2.00 |
| | 300 | 2 | 0.0190 | 1.9e-13 | 1.9e-13 | 1e-15 | 3e-16 | 7e-59 | 6.19 0* 3.99 3.99 0* 6.19 2.00 |
| p=1+3w, j=1 | 300 | 1 | 0.311 | 1.3e-13 | 1.3e-13 | 3e-11 | 5e-13 | 7e-58 | 0.96 0.74 1.00 0.73 1.95 1.31 2.00 |
| | 3000 | 2 | 0.0377 | 6.1e-14 | 6.0e-14 | 1e-15 | 3e-16 | 4e-28 | 3.23 0.74 1.00 0.69 3.12 1.80 2.00 |
| | 20000 | 1 | 0.119 | 9.3e-14 | 9.4e-14 | 4e-16 | 4e-16 | 5e-14 | 0.39 0.74 1.00 1.02 1.95 1.46 2.00 |
| p=1+3w, j=0 (active + inactive groups) | 3000 | 1 | 0.0733 | 1.2e-14 | 1.2e-14 | 0 | 4e-16 | 5e-30 | 2.16 1.06 0.97 1.92 0.35 0.82 2.00 |
| p=1+3w, j=2 | 3000 | 2 | 0.201 | 1.6e-14 | 1.6e-14 | 2e-16 | 3e-16 | 4e-28 | 1.41 0.74 1.00 0.16 1.43 0.41 2.00 |
| p=1+3w, j=3 | 3000 | 1 | 0.205 | 1.6e-14 | 1.7e-14 | 4e-16 | 4e-16 | 5e-30 | 1.42 0.74 1.00 0.29 0.95 0.69 2.00 |
| p=1+3w, j=4 (Ramanujan factor) | 300 | 1 | 0.234 | 1.1e-13 | 1.1e-13 | 5e-12 | 5e-13 | 7e-58 | 2.16 0.74 3.93 0.76 1.12 1.65 2.00 |
| p=1+3w, j=5 | 3000 | 1 | 0.0871 | 2.4e-14 | 2.6e-14 | 9e-16 | 4e-16 | 5e-30 | 2.08 0.74 1.00 1.37 2.46 3.40 2.00 |
| p=-2-3w (conjugate), j=1 | 3000 | 2 | 0.0377 | 5.9e-14 | 5.8e-14 | 8e-16 | 3e-16 | 4e-28 | 3.23 0.74 1.00 0.69 3.12 1.80 2.00 |
| p=1-3w (N=13), j=1 | 20000 | 2 | 0.0879 | 1.1e-11 | 1.1e-11 | 4e-16 | 3e-16 | 2.5e-11 | 1.52 2.00 1.00 0.56 3.35 1.40 2.00 |
| P={1+3w, 1-3w}, j=(1,1), 2592 translates | 20000 | 1 | 0.546 | 1.6e-11 | 1.6e-11 | 3.5e-9 | 5e-10 | 5e-14 | 1.11 1.88 1.00 0.71 1.16 1.04 2.00 |
| Psi_0=1, p=1+3w, j=1 (N(c)=252) | 20000 | 1 | 0.148 | 4.1e-12 | 4.1e-12 | 3e-10 | 5e-12 | 5e-14 | 1.45 0.74 1.00 4.48 2.10 3.16 2.00 |
| Psi_0=1, p=1+3w, j=4 | 10000 | 1 | 0.103 | 3.6e-10 | 3.6e-10 | 2.5e-8 | 5e-10 | 4e-19 | 0.83 0.74 1.00 1.00 0.69 5.76 2.00 |

The table shows representative rows. Every row of the run is in e2e_1e6.json (56 rows). Over all
56 rows:

* max relerr(RHS1) = 3.6e-10 and max relerr(RHS2) = 3.6e-10; the minimum is 6.5e-15;
* 43 of 56 rows are below 2e-13;
* the larger errors occur only where a measured truncation indicator (tail, Vtail or V*cut) is
  of the same size.

0* marks a control that is the identity in that family, so it cannot discriminate:

* when P = {}, c in {1, -2} or c_0 has alpha(c_0)^2 real, so (b) is the identity;
* when P = {}, there is no B factor, so (e) is the identity.

All controls that change anything break the agreement; the smallest such effect is 0.16 (control
(d), j = 2). Before the 10^6 tables were built, a 3·10^4 table already gave 4.9e-12 to 8.6e-12 at
X = 100 for Psi_0 = rho^2, P = {}. The error at small X fell as X grew, as truncation predicts.

**What the controls show.**

* **(a), (f): the multiplier convention.** Conjugating Kubota's multiplier gives relative errors
  0.39 to 13.8. This settles the convention end to end. It agrees with R3 checks A, D and E.
* **(e): the quadratic twist.** Building B_{p,1} as chi_p (sextic, the conjugate-convention
  exponent) instead of chi_p^3 fails by 0.61 to 11.0 in the j = 1 rows. This is the
  load-bearing point for the quadratic large sieve.
* **(c), (d): the ray phase.** Dropping it fails by about 1.
* **(b), (g): scalar and argument conventions.** Both fail.

## 4. Coverage and limits

* **Local cases.** j_p = 0..5 at a prime dividing the row. j = 0 includes an inactive (h_p = 0)
  group together with active groups. Two conjugate split primes of norm 7, a split prime of norm 13,
  and one two-prime row (N(c) up to 364).
* **Cusps.** With Psi_0 = 1, every translate with phihat(h_0) != 0 has v_lambda(c) = 2, so only
  sigma = 0 occurs. The Psi_0 = (lambda/.)_3^2 families have c_0 | 2 and exercise sigma = +, -, 0,
  including the H = [[u_0,-1],[1,0]] case. The v_lambda(c) = 1 branch (H = [[1,0],[+-lambda,1]])
  never occurs with L = 18 for these phi, so that branch is not exercised here. R3 check F covers it
  locally.
* **Uniformity.** In every group the normalized c, the cusp sigma, kappa_0 and delta' mod D_0 were
  constant over the h_p, with h_p == 0 mod M^2. This is the content behind
  Lemma lem:reflection-uniformity, checked for one fixed r per family. It was not checked as k_0
  varies over a ray class.
* **Accuracy.** Ordinary double precision; not certified. The run reaches the double-precision
  floor (1e-14 to 1e-13) whenever both truncation indicators are below it.
* **Not covered.**
  * inert primes in P, and three or more primes;
  * non-cubic Psi_0 (for example characters mod 4 or with a nontrivial 2-part);
  * the v_lambda(c) = 1 branch, as noted above;
  * Prop. prop:R, the large sieve, lem:squarefree-completed and Lemma lem:smooth.

## 5. Compact support (the remaining gap)

Prop. prop:R assumes W in C_c^infty(I). The identity eq:reflection itself is derived by:

1. Mellin inversion of V_*;
2. the functional equation of the entire function T(s,Psi);
3. contour shifts, justified by rapid decay of Vhat_* on vertical lines in a strip.

The log-Gaussian Vhat_* are entire and have Gaussian decay in every vertical strip, so the same
proof applies to them verbatim. The LHS converges absolutely.

A compactly supported bump has Vhat_* decaying only like exp(-c|Im s|^{1/2}). Vsharp then becomes
small only for x beyond about 10^7 to 10^8, as R3 Section 6 noted. The dual range would exceed
10^9 lattice points. That is out of this budget. The C_c^infty case is therefore **not** run.
Only the Schwartz-class case is confirmed numerically.

## Reproduction

```
cd research/exploratory/qrh-2026-10/reviews
gcc -O2 -o /tmp/gauss oct5_reflection_e2e_gauss.c -lm
python3 -I oct5_reflection_e2e_tables.py 1000000 /tmp/tables_1e6.npz /tmp/gauss   # ~4 min, 2 threads
python3 -I oct5_reflection_e2e.py /tmp/tables_1e6.npz /tmp/e2e_1e6.json            # ~4 min
# optional: E2E_ONLY=<family,...> E2E_X=<X,...> to run a subset
```
