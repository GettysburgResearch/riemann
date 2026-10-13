# V. Numerics of the 7/8 proof's arithmetic: Patterson bias, floor-row cancellation, Gram term

**Status:** EMPIRICAL (ordinary floating point, $X,U\le4\times10^5$, $Y\le2000$; no certificate).
**Scope:** three absolute-value steps of the 7/8 architecture, each replaced by the actual sum it bounds, at computable sizes: (1) the Patterson/Dunn–Radziwiłł bias of cubic and sextic Gauss sums under ray-class twists; (2) the floor-row cross-row sum $\sum_u\xi(u)D_1(u)D_2(u)$ in a Dirichlet-polynomial model (the sum that Lemma 10.4 bounds row by row, notes N/U); (3) the additive Gram term of Prop. 15.2 (note J) with its $P_a^{1/6}$ exceptional frequencies.
**Exact sources:** OpenAI 30 Sept 2026 paper (Prop. 15.2, Lemma 10.4; definition and purpose of $\xi$ in §6.1, lines 2698–2713, with the Poisson consequence in §7.1; Hasse–Davenport in Section 4); Dunn–Radziwiłł arXiv:2109.07463 (bias constant); notes J, N, U of this wave.
**What was actually run:** `../scripts/cubic/` (Eisenstein arithmetic; three experiments, raw tables in `exp*_out.md`; run from `scripts/cubic/`, the scripts insert their own directory on `sys.path`). The pre-use checks of §0 (unit modulus, multiplicativity, Hasse–Davenport, reality) were scratch checks; the Hasse–Davenport one is committed as `hd_check.py` (referee pass R2, 42 split primes $p\le199$).
**Smallest remaining gap:** the floor-row sum empirically cancels like $U^{1/2}$ (300–1000× below the trivial bound) but the proof must bound *hypothetical zero rows*, which no experiment can see; and a $U^{2/3}$ sextic-bias component is not excluded case by case at these sizes. The Gram term's $1/6$ exponent is unmeasurable below $P_a\sim10^7$.

Scripts: `../scripts/cubic/eis.py` (Eisenstein arithmetic, residue symbols, Gauss sums), `../scripts/cubic/exp1.py`, `exp2.py`/`exp2b.py`/`exp2c.py`, `exp3.py`; raw outputs `exp1_out.md`, `exp2b_out.md`, `exp3_out.md`, logs `exp2c.log`. 50-minute budget; all numbers below are from runs that completed.

## 0. Conventions and checks

O = Z[omega], omega = e^{2 pi i/3}; primary c = 1 mod 3 (x = 1, y = 0 mod 3 for c = x + y omega); each ideal coprime to 3 has exactly one primary generator. (u/pi)_6 = zeta_6^k with zeta_6 = -omega^2 = e^{i pi/3}, computed in the residue field F_p (split pi, p = 1 mod 3, omega -> r with r^2 + r + 1 = 0) or F_{p^2} = F_p[omega] (inert -p, p = 2 mod 3; the sextic symbol is undefined at 2, so sextic experiments use moduli coprime to 6). e(z) = exp(4 pi i Im z / sqrt 3), so for pi = a + b omega split, e(d/pi) = exp(-2 pi i b d/p).

Verified numerically before use:
* |gamma_j(pi)| = 1 for j = 1, 2, 3 at all primes; inert primes give gamma_j(-p) = 1 exactly (pure Gauss sums).
* Multiplicativity gamma_j(ab) = chi_a(b)^j chi_b(a)^j gamma_j(a) gamma_j(b) checked against direct summation over Z/(p_a p_b) for four prime pairs, residual 0 to machine precision (j = 1 and 2).
* Hasse-Davenport: gamma_1 gamma_2 = -alpha(pi) * conj(chi_pi(4)) * gamma_3 holds exactly in this normalization (with chi_pi(4) instead of its conjugate the residual is |1-omega| exactly at the primes where 2 is a cubic non-residue, p != x^2 + 27 y^2, and zero otherwise; referee check hd_check.py), i.e. the paper's relation up to the orientation of chi(4).
* Patterson sum over primary squarefree c is real to machine precision (gamma_2(conj c) = conj gamma_2(c)).

## 1. Experiment 1: Patterson bias and twisted sums (X = 10^5)

40315 primary c with N c <= 10^5, 35287 squarefree, 9602 prime (both pi and conj pi counted; inert ones included). gamma_2 at every prime by direct summation (discrete-log tables), extended to squarefree c with the cross phases. S_chi(X) = sum_{N c <= X} gamma_2(c) chi(c). Fits: slope of log|S| vs log X on 25 log-spaced points in [2000, 10^5]; "rms" = rms of |S(x)| over x in (X/2, X] (smooths the oscillation). Naive least-squares standard errors (autocorrelated, so optimistic).

| series | twist chi | slope |S| | slope rms | |S(X)|/X^{5/6} | |S(X)|/X^{1/2} |
|---|---|---|---|---|---|
| gamma_2, squarefree | none (Patterson) | **0.835 +- 0.005** | 0.833 +- 0.003 | 0.247 | 11.5 |
| gamma_2, squarefree | xi9(1,0) | 0.21 +- 0.16 | 0.37 +- 0.05 | 0.000 | 0.007 |
| gamma_2, squarefree | xi9(0,1) | **0.832 +- 0.004** | 0.830 +- 0.002 | 0.356 | 16.5 |
| gamma_2, squarefree | xi9(1,1) | **0.832 +- 0.002** | 0.829 +- 0.002 | 0.245 | 11.4 |
| gamma_2, squarefree | xi9(1,2) | 0.53 +- 0.11 | 0.40 +- 0.02 | 0.007 | 0.31 |
| gamma_2, squarefree | (c/lam)_6, N lam = 7 | 0.35 +- 0.13 | 0.39 +- 0.02 | 0.005 | 0.22 |
| gamma_2, squarefree | (c/lam)_3 = (lam/c)_3 | 0.61 +- 0.10 | 0.49 +- 0.05 | 0.004 | 0.17 |
| gamma_2, squarefree | conj (c/lam)_3 | **0.812 +- 0.008** | 0.818 +- 0.005 | 0.160 | 7.4 |
| gamma_2, squarefree | (c/lam)_2 | 0.38 +- 0.10 | 0.37 +- 0.05 | 0.003 | 0.16 |
| gamma_2, squarefree | alpha(c)^6 (infinite order) | 0.75 +- 0.10 | 0.66 +- 0.05 | 0.004 | 0.17 |
| gamma_2, primes only | none | 0.737 +- 0.014 | 0.751 +- 0.013 | 0.071 | 3.3 |
| gamma_2, primes only | xi9(0,1) / xi9(1,1) | 0.730 / 0.691 | 0.723 / 0.686 | 0.100 / 0.065 | |
| gamma_2, primes only | xi9(1,0) / (c/lam)_6 | 0.24 / 0.22 | 0.26 / 0.26 | 0.001 / 0.002 | |
| gamma_1 (sextic), squarefree odd | none | 0.71 +- 0.06 | 0.65 +- 0.03 | 0.029 | 1.33 |
| gamma_1 (sextic), squarefree odd | xi9(1,0) / xi9(0,1) / xi9(1,1) / xi9(1,2) | 0.73 / 0.93 / 0.72 / 0.59 | 0.71 / 0.88 / 0.70 / 0.58 | 0.026 / 0.025 / 0.030 / 0.012 | 1.2 / 1.2 / 1.4 / 0.5 |

xi9(a,b)(c) = omega^{a s + b t} where (c-1)/3 = s + t omega mod 3: these are exactly the 8 nonprincipal ray class characters mod 9 (ray class group mod 9 has order 9).

Findings.
* Patterson/Dunn-Radziwill: the squarefree sum is C X^{5/6} with C = 0.247 +- 0.005 stable from X = 2000 to 10^5 (slope on [10^4, 10^5]: 0.838 +- 0.005). Primes: slope 0.74-0.75, which is 5/6 - 1/log X as expected for X^{5/6}/log X; S_p(X) log X / X^{5/6} = 0.81 at X = 10^5 (Dunn-Radziwill constant 0.503 if one counts only one of pi, conj pi; our sum counts both, so 0.81 vs 1.0 is within the 1/log X convergence).
* Generic cancellation: twists by (c/lam)_6, (c/lam)_2, xi9(1,0), xi9(1,2) give |S| ~ X^{0.2-0.5}, i.e. at or below square root (the fitted exponents < 1/2 reflect |S(X)| being O(10) absolute at X = 10^5: 0.2-0.3 X^{1/2}).
* **The cubic bias is not killed by every nonprincipal ray character mod 9.** xi9(0,1) and xi9(1,1) (and their conjugates) leave the full X^{5/6} bias, with a *larger* constant (0.356); the characters xi9(1,0), xi9(1,2) and their conjugates kill it. The cubic twist (lam/c)_3 (= Patterson series at m = lam) has an exponent 0.49-0.61 at this X, while its conjugate keeps the full bias (0.812, C = 0.16 = |tau(lam^2)|-type coefficient). So "twist by a fixed nonprincipal finite-order character" does NOT uniformly imply cancellation: the bias survives exactly the characters of the two Galois-stable order-3 subgroups <xi9(0,1)>, <xi9(1,1)> of the dual of the ray class group mod 9 (isomorphic to (Z/3)^2; conjugation acts by xi9(a,b) -> xi9(a,-a-b)) and is killed by those of <xi9(1,0)>, <xi9(1,2)>; the biased set is a union of two subgroups, not a subgroup, and the pattern is the expected cusp-dependence of the Patterson residue (the twisted series carries the constant terms at the cusps a/9), not a surprise.
* Sextic sums: the untwisted sum has exponent 0.65-0.71, consistent with the Kubota-Patterson pole at 1/2 + 1/6 = 2/3 for n = 6; **all four mod-9 twists tested keep an exponent 0.58-0.93 > 1/2**. The sextic bias is the one relevant to the floor rows (Experiment 2).

## 2. Experiment 2: floor-row cross-row cancellation

R(U) = sum_{u primary, 6th-power-free, N u <= U} xi(u) D1(u) D2(u), D1 = sum_{N n <= sqrt U} (u/n)_6 N(n)^{-w}, D2 = sum_{N m <= sqrt U} mu(m) eta(m) (u/m)_6 N(m)^{-x}, n, m primary and coprime to 6, w = x = 1/2 + it. T(U) = sum_u |D1 D2| (trivial bound). U <= 10^5: 40306 rows, 96 moduli; U <= 4 x 10^5: 161k rows, ~190 moduli. Fit on 97 log-spaced U in [1000, U_max]; "rms" fit uses rms of |R| over 8 consecutive log-windows.

| U_max | t | xi | eta | Mobius | slope |R| | slope rms | slope T | rms/U^{1/2} | rms/U^{2/3} | |R|/T at U_max |
|---|---|---|---|---|---|---|---|---|---|---|
| 1e5 | 0 | xi9(1,0) | 1 | mu | 0.63 +- 0.04 | 0.61 +- 0.05 | 1.037 | 0.50 | 0.077 | 0.0011 |
| 1e5 | 0 | xi9(1,0) | 1 | plain | 0.65 +- 0.05 | 0.63 +- 0.06 | 1.074 | 0.59 | 0.091 | 0.0028 |
| 1e5 | 0 | xi9(1,0) | xi9(1,0) | mu | 0.42 +- 0.05 | 0.41 +- 0.07 | 1.052 | 0.33 | 0.051 | 0.0011 |
| 1e5 | 0 | xi9(0,1) | 1 | mu | 0.40 +- 0.06 | 0.37 +- 0.11 | 1.037 | 0.42 | 0.065 | 0.0030 |
| 1e5 | 0 | xi9(1,1) | 1 | mu | 0.65 +- 0.04 | 0.62 +- 0.07 | 1.037 | 0.57 | 0.088 | 0.0035 |
| 1e5 | 0 | (u/lam)_6 | 1 | mu | 0.63 +- 0.05 | 0.63 +- 0.15 | 1.037 | 0.35 | 0.054 | 0.0019 |
| 1e5 | 0 | **none** | 1 | mu | **1.000 +- 0.000** | 0.999 | 1.037 | 112 | 17.4 | 0.715 |
| 1e5 | 2 | xi9(1,0)/xi9(0,1)/xi9(1,1)/(u/lam)_6 | 1 | mu | 0.52/0.70/0.48/0.61 (+-0.04-0.05) | 0.54/0.66/0.49/0.61 | 1.036 | 0.43/0.46/0.31/0.49 | | |
| 1e5 | 5 | xi9(1,0)/xi9(0,1)/xi9(1,1)/(u/lam)_6 | 1 | mu | 0.47/0.52/0.50/0.57 (+-0.04-0.05) | 0.51/0.49/0.50/0.56 | 1.037 | 0.46/0.50/0.35/0.41 | | |
| 4e5 | 0 | xi9(1,0) | 1 | mu | 0.54 +- 0.04 | 0.58 +- 0.04 | 1.036 | 0.53 | 0.066 | 0.0005 |
| 4e5 | 0 | xi9(1,0) | 1 | plain | 0.68 +- 0.04 | 0.64 +- 0.02 | 1.071 | 0.82 | 0.102 | 0.0008 |
| 4e5 | 0 | xi9(1,0) | xi9(1,0) | mu | 0.49 +- 0.04 | 0.49 +- 0.05 | 1.049 | 0.32 | 0.040 | 0.0002 |
| 4e5 | 0 | xi9(0,1) | 1 | mu / plain | 0.57 / 0.46 (+-0.05) | 0.53 / 0.52 | | 0.63 / 0.46 | 0.079 / 0.057 | 0.0013 / 0.0007 |
| 4e5 | 0 | xi9(1,1) | 1 | mu / plain | 0.47 / 0.56 (+-0.04) | 0.51 / 0.56 | | 0.25 / 0.45 | 0.032 / 0.056 | 0.0012 / 0.0010 |
| 4e5 | 0 | xi9(1,1) | xi9(1,0) | mu | 0.37 +- 0.03 | 0.40 +- 0.03 | 1.049 | 0.25 | 0.031 | 0.0006 |
| 4e5 | 0 | xi9(0,1) | xi9(1,0) | mu | 0.535 +- 0.035 | 0.544 | 1.049 | 0.384 | | |
| 4e5 | 0 | (u/lam)_6 | 1 | mu | 0.61 +- 0.04 | 0.60 +- 0.08 | 1.036 | 0.48 | 0.059 | 0.0003 |
| 4e5 | 0 | (u/lam)_6 | 1 | plain | 0.82 +- 0.03 | 0.82 +- 0.08 | 1.071 | 2.29 | 0.29 | 0.0038 |
| 4e5 | 0 | (u/lam)_6 | xi9(1,0) | mu | 0.51 +- 0.04 | 0.51 +- 0.04 | 1.049 | 0.31 | 0.039 | 0.0003 |
| 4e5 | 0 | **none** | 1 | mu | **1.000 +- 0.000** | 0.999 | 1.036 | 218 | 27.1 | 0.682 |

Findings.
* With xi removed the diagonal appears exactly: R(U) = 0.404 U (= density of primary 6th-power-free u; only the n = m = 1 term survives), slope 1.000.
* With any of the three ray-class phases xi9 and Mobius, |R(U)| is 0.25-0.6 U^{1/2} out to U = 4 x 10^5 and |R|/T = 10^{-3} to 10^{-4}: the trivial bound sum_u |D1 D2| = 0.57 U overestimates the row sum by a factor ~U^{1/2}, i.e. 300-1000 at these sizes. Averaging the nine mod-9 fits at U_max = 4 x 10^5 gives exponent 0.52 +- 0.03 (Mobius cases 0.49 +- 0.03, plain 0.57 +- 0.06); the full 4e5 table is in ../scripts/cubic/exp2c_out.md. The sextic-bias alternative U^{2/3} (which Experiment 1 says survives mod-9 twists of gamma_1) is not excluded case by case (several individual fits are 0.6-0.68 +- 0.04) but is disfavoured on average; the 1e5 -> 4e5 extension moved the fits down, not up.
* xi = (u/lam)_6 with plain x plain shows the expected pseudo-diagonal (n = lam^2, m = lam^3 makes xi chi_n chi_m principal): slope 0.82, |R| = 2.3 U^{1/2}. A Kummer-symbol "ray phase" is not safe; the Mobius factor removes it (slope 0.61).
* t-dependence is mild; eta = xi9(1,0) in the denominator polynomial lowers the sum further (0.37-0.49).

## 3. Experiment 3: direct-side Gram term

A_m = Y^{-3/2} sum_{Y/2 < N s <= Y} c(s) g(s, -m), s primary, odd, squarefree (all prime-factor counts; cross phases via the verified product formula, g(s,-m) = conj chi_s(-m) g(s,1) 1_{(s,m)=1}); m over all nonzero Eisenstein integers with N m <= Q (3.63 Q of them); S(Q) = sum_m |A_m|^2; diag(Q) = Y^{-3} sum_s |c(s)|^2 N(s) #{N m <= Q, (m,s) = 1} (exact diagonal); P_a = Y^2/Q. Random-sign controls give S/diag = 1.000 +- 0.005 at all P_a (noise floor), so deviations >= 0.01 are real.

S/diag (table rows: P_a = 4, 16, 64, 256, 729, 1024, 4096):

| c(s) | Y | P_a=4 | 16 | 64 | 256 | 729 | 1024 | 4096 | kappa in S/diag = alpha + kappa P_a^{1/6} |
|---|---|---|---|---|---|---|---|---|---|
| 1 (all squarefree s) | 1000 | 0.991 | 1.035 | 1.062 | 1.076 | 1.084 | 1.098 | 1.060 | 0.026 +- 0.008 |
| 1 | 2000 | - | 1.035 | 1.064 | 1.096 | 1.141 | 1.142 | 1.105 | 0.038 +- 0.010 |
| random sign | 1000 | 1.000 | 1.001 | 1.001 | 1.000 | 1.012 | 1.005 | 0.959 | -0.006 +- 0.004 |
| random sign | 2000 | - | 0.999 | 1.001 | 1.009 | 1.018 | 1.017 | 1.007 | 0.006 +- 0.002 |
| random phase | 2000 | - | 0.999 | 1.000 | 1.000 | 1.000 | 1.006 | 0.991 | -0.001 +- 0.002 |
| 1 on primes only | 1000 | 0.996 | 1.013 | 1.017 | 1.022 | 1.033 | 1.043 | 1.017 | 0.010 +- 0.004 |
| 1 on primes only | 2000 | - | 1.017 | 1.030 | 1.045 | 1.063 | 1.066 | 1.071 | 0.024 +- 0.002 |
| random sign on primes | 2000 | - | 0.999 | 0.999 | 0.997 | 0.994 | 0.987 | 0.995 | -0.003 +- 0.001 |
| 1_{s = 1 mod 9} (ray class) | 2000 | - | 1.018 | 1.048 | 1.082 | 1.124 | 1.130 | 1.083 | 0.039 +- 0.011 |
| 1_{s = 1 mod 9} x random sign | 2000 | - | 1.001 | 1.002 | 1.009 | 1.016 | 1.008 | 1.017 | 0.007 +- 0.002 |
| xi9(1,0)(s) (nonprincipal ray char) | 1000 | 1.004 | 0.992 | 1.043 | 1.067 | 1.106 | 1.110 | 1.113 | 0.049 +- 0.007 |
| xi9(1,0)(s) | 2000 | - | 0.995 | 1.059 | 1.083 | 1.119 | 1.142 | 1.171 | 0.072 +- 0.006 |
| conj g(s)/|g(s)| (Gauss phase removed) | 2000 | - | 0.999 | 0.996 | 1.003 | 1.029 | 1.022 | 1.130 | 0.045 +- 0.010 |

(Y = 500 rows in exp3_out.md agree but are noisier; at Y = 500, P_a = 4096 means Q = 61, too small.)

Shell profile (Y = 2000, c = 1): mean |A_m|^2 / diagonal weight on N m in (Q/2, Q] is 1.10-1.16 for Q <= 4000 (P_a >= 1000), 1.04-1.06 for Q = 10^4-10^5, 1.01 at Q = 2.5 x 10^5; random signs: 1.00 +- 0.02 throughout. The excess is spread over all rows of small norm, not concentrated on sixth-power rows (for c = conj g/|g| it IS concentrated: units and (1-omega)^6, visible only at Q <= 10^3).

Findings.
* The off-diagonal excess is real, positive, structured-coefficient-only (random signs/phases kill it to the 0.5% noise floor, including on the ray class), grows slowly with P_a, and is of size 5-17% of the diagonal for P_a up to 4096. Fitting the paper's shape S/diag = alpha + kappa P_a^{1/6} gives kappa = 0.03-0.07 for ray-class/indicator/constant coefficients (kappa consistent with 0 for random coefficients); kappa P_a^{1/6} would equal the diagonal only at P_a ~ 10^7-10^9. The slope of log(S/diag) vs log P_a is 0.011-0.04, far below 1/6, because the exceptional term is a small additive correction at these sizes.
* Mechanism check: with fewer than 2 sixth powers of norm <= P_a (729 = N((1-omega)^6), 4096 = N(2^6)) the predicted count K^{1/6} cannot grow; the data show the ray-class indicator (where the e-frequencies supported at 3 are coherent) and the nonprincipal ray character xi9 (coherent with chi_e for e = (1-omega)^j) producing the largest excess (up to 1.17), exactly as the "exceptional e on the fixed support" description predicts, and the prime-only support halves it rather than removing it.
* The P_a^2/Y' term is invisible (as the note predicts, inactive).

## 4. Where the absolute-value steps are lossy in practice

| step | trivial bound used | observed | empirical gap at the sizes tested |
|---|---|---|---|
| (1) sum of gamma_2 over squarefree c (Patterson) | 0.35 X | 0.247 X^{5/6} (real, one-signed) | X^{1/6} = 6.8 at X = 10^5; no room: the bias is sharp, and it survives half of the ray-class twists and one orientation of the cubic-symbol twist (the conjugate), the other cancelling at this X |
| (1') generic twists (c/lam)_6, xi9(1,0) etc. | 0.35 X | 0.2-0.3 X^{1/2} | X^{1/2} ~ 300 |
| (2) floor-row sum sum_u xi(u) L/L (Dirichlet polynomial model) | T(U) = 0.57 U | 0.25-0.6 U^{1/2} (exponent 0.52 +- 0.03 averaged) | **U^{1/2}: 300-1000 at U = 10^5 - 4 x 10^5; the largest gap of the three** |
| (3) Gram sum sum_m |A_m|^2 vs (Q/Y)(1 + P_a^{1/6}) | (Q/Y) x (1 + P_a^{1/6}) = up to 5 x diagonal at P_a = 4096 | diagonal x (1.05-1.17) | factor 3-4 at P_a ~ 10^3; kappa = 0.03-0.07 per P_a^{1/6} unit, i.e. the P_a^{1/6} term is correct in form but carries a tiny constant |

## 5. Interpretation (<= 300 words)

The three bookkeeping steps behave very differently in the data. The Patterson bias (1) is exactly as sharp as Dunn-Radziwill say: 0.247 X^{5/6}, one-signed, constant stable over two decades, and it is not removable by a generic ray-class twist: the characters xi9(0,1), xi9(1,1) leave it intact with a larger constant, and for the sextic sums every mod-9 twist tested keeps an exponent > 1/2 (fits 0.58-0.93). Any argument that treats "xi nonprincipal" as sufficient for cancellation of a Gauss-sum sum is wrong in half the cases; the biased characters are the union of two Galois-stable order-3 subgroups of the dual ray class group mod 9, which any construction using a ray phase (notes M/N/U) must avoid explicitly. The paper's own xi is a residue character mod b* (nontrivial on units at the prime over 3), used in §6.1 to force the Poisson frequencies prime to S, not a ray-class character mod 9, so this is a warning for the notes, not a referee item against the paper.

The floor-row sum (2) is where the proof's absolute values are most lossy empirically. The toy row sum with any mod-9 phase and Mobius denominator is 0.3-0.6 U^{1/2} while the trivial bound is 0.57 U; the diagonal 0.404 U appears instantly when xi is removed, and a Kummer-symbol phase (u/lam)_6 generates a pseudo-diagonal unless the Mobius factor kills the offending (n,m). The fitted exponent, 0.52 +- 0.03 averaged over the nine mod-9 cases at U <= 4 x 10^5 (0.55 over all twelve rows of exp2c_out.md, including the (u/lam)_6 cases), is consistent with square-root cancellation; a sextic-bias component U^{2/3} is not excluded by individual fits (0.6-0.68) but is not what the averages show. If the proof could use square-root cancellation across floor rows instead of row-by-row absolute values, the empirical gain is U^{1/2} at these sizes.

The Gram term (3) is qualitatively confirmed: an off-diagonal excess that only structured coefficients (indicator, ray class, ray character) produce, killed by random signs, spread over small-norm rows, largest when the coefficient is coherent with the sextic symbols supported at the S-primes. But its size is 5-17% of the diagonal up to P_a = 4096, with kappa ~ 0.03-0.07 in (Q/Y)(1 + kappa P_a^{1/6}). The term's exponent cannot be measured here (only two sixth powers below 4096), so the data neither confirm nor refute 1/6; they do say the constant is small, so the Cauchy-Schwarz loss P_a^{1/12} is asymptotic bookkeeping with no visible counterpart at any computable size.

## 6. Limitations

X, U <= 4 x 10^5 and Y <= 2000: the sextic bias U^{2/3} and square-root U^{1/2} differ by a factor 8.6 at U = 4 x 10^5, and partial-sum fits have effective errors ~0.05-0.1 (quoted standard errors are naive). Experiment 2 uses Dirichlet polynomials of length sqrt U rather than the completed L-values, moduli coprime to 6 only, and the sixth-power-free condition excludes only 64 | u. Experiment 3 sums over a dyadic shell of s with density 0.1 Y rather than a full ray class, which sets the (small) constants; the P_a^{1/6} shape fit is a two-parameter fit over 1.5 decades. The Hasse-Davenport orientation (chi(4) vs its conjugate) is a convention difference and does not affect any sum computed here. The X = 3 x 10^5 extension of Experiment 1 did not finish within the budget.
