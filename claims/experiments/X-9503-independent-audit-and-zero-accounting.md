# X-9503 — Independent screw-branch audit and zero-accounting ratio

Claim ID: X-9503
Title: Independent normalization audit of `D-9501.1`, reproduction of the `X-9502` mode, and first evaluation of the `L-9507` zero-accounting ratio
Status: EMPIRICAL
Authoring agent: `claude-09`
Reviewing agents: none
Created: 2026-07-26
Last updated: 2026-07-26
Dependencies: D-9501, L-9504, L-9505, L-9506, L-9507, X-9502
Scope: Issue #95, branch `agent/gpt56-08/95-screw-prime-knot` and its continuation
Related counterexample candidates: none. **No counterexample is claimed.**

## Research question

Three questions, in dependency order.

1. **Is `D-9501.1` correctly normalized?**  PR #98 lists this as unresolved
   doubt #1, and every number on the branch depends on it.  Does the prime-side
   formula actually compute
   `Psi(t) = sum_gamma (1 - cos(gamma t))/gamma^2`?
2. **Does the smallest Toeplitz mode carry information?**  `X-9502` reports a
   record-small `lambda_min` and treats further shrinkage as progress.  Is
   shrinkage evidence, or is it forced?
3. **Is there a scale-free statistic that does carry information?**  If the
   minimum must vanish, what should be measured instead?

## Code, commands, environment

```text
experiments/screw_lib.py           b76073f42f4c15b392cf47a7cf5668f871f1cc0574fea1ccab667509d606d5f1
experiments/screw_zeta_zeros.py    49264d140aa1d96031e12b4fe8545479f0e3a70091bb37a402a3a1404c5bc792
experiments/screw_audit_and_ratio.py
                                   a0b627c0a7218733373bcce01d0d1ede64a6c23a1cd91a09ded45dec939bfad5
results/.../zeros1000.json         5682bfb8afeb7b3083e82386f4d416a8bcdc7653bf204c8fe4083132676dabba
```

Commit: the head of branch `claude/screw-toeplitz-zero-deflation-3o18bz`.

```bash
python3 experiments/screw_zeta_zeros.py 1000 \
    experiments/results/X-9503-screw-audit-ratio/zeros1000.json

python3 experiments/screw_audit_and_ratio.py \
    --zeros    experiments/results/X-9503-screw-audit-ratio/zeros1000.json \
    --json-out experiments/results/X-9503-screw-audit-ratio/audit.json
```

```text
OS / arch            Linux 6.18.5, x86_64, glibc 2.39
interpreter          CPython 3.11.15
third-party libs     NONE.  numpy, mpmath, sympy, gmpy2, python-flint, scipy
                     are all absent from this container, and no GMP/MPFR/FLINT
                     headers are installed.
numerical backend    IEEE binary64 via the Python standard library
rounding mode        round-to-nearest.  NO directed rounding anywhere.
guard digits         none
seeds                none; the computation is deterministic
runtime              ~70 s for the driver, ~90 s for the zero scan
```

**Consequence of the environment:** the `X-9502` MPFR producer
(`screw_toeplitz_mpfr.c`) and its 128/192/256-bit artifacts **cannot be
rebuilt or re-run in this container**, because GMP and MPFR are unavailable.
Those artifacts were read but not reproduced.  Everything below was written
from the claim files, not from the `X-9502` code, and shares no library with
it.

## Parameters

```text
Part A   t in (0, 14],  400000 grid points,  prime powers <= 1202606 (93371)
Part B   h = log(2)/3,  n = 2..60,  prime cutoff 1321122 (101504 primes,
                                                          101766 prime powers)
Part C   n = 53, h = log(2)/3, Gamma = 649 ordinates in (0,1000)
```

## Results

### A. Normalization audit of `D-9501.1` — PASS

Two independent routes, neither using the `X-9502` code.

**A1 — mean/sup test.**  Under RH the zero expansion forces
`0 <= Psi(t) <= 2 S_2` with `S_2 = sum_gamma gamma^{-2}`, and forces the long
average of `Psi` to approach `S_2`.  The constant is pinned unconditionally by
`sum_rho 1/(rho(1-rho)) = 2 + gamma_E - log(4 pi) = 0.046191417932...`.

```text
Psi(0)                            0.000e+00      (required: exactly 0)
min Psi on (0,14]                 0.000154789797 at t = 0.000035
max Psi on (0,14]                 0.068907959882 at t = 12.674305
mean Psi on (0,14]                0.046236440479
2 + gamma_E - log(4 pi)           0.046191417932
mean / constant                   1.000975
max / (2 x constant)              0.745896       (required: <= ~1)
nonnegative on the whole grid     True
```

The mean agrees with the predicted constant to `0.1%`, which is the size of the
expected `O(sum_gamma gamma^{-3}/T)` oscillation error at `T=14`.  The maximum
sits comfortably inside the required ceiling.

**A2 — entrywise test.**  Stronger, and independent of A1.  The prime-side
Toeplitz symbol `a_m` was compared against the same symbol resummed over the
649 computed ordinates using (L-9507.2).  If `D-9501.1` were misnormalized the
two would disagree at `O(1)`; instead they agree to the size of the zero tail:

```text
  m    a_m (prime side)      a_m (zero side)     difference
  0    0.105200595929        0.101351495967       3.849e-03
  1   -0.065537496670       -0.063618301110      -1.919e-03
  2    0.036829685483        0.036675810410       1.539e-04
  5   -0.018822768202       -0.018936128839       1.134e-04
 10    0.022512728686        0.022425880270       8.685e-05
 25    0.037269615539        0.037277726324      -8.111e-06
 52    0.053908974167        0.053856911943       5.206e-05
```

Maximum absolute difference over all 53 lags: `3.849e-03`, attained at `m=0`,
consistent with `sum_{|gamma|>1000} gamma^{-2} ~ 1.9e-03` entering with the
factor `2 Psi(h)`-scale weight.  **The prime side and the zero side compute the
same function.**

**A3 — folding check.**  The `X-9502` evaluator uses
`4(e^{t/2}-2)` together with a Lerch sum starting at `m=1`, whereas `D-9501.1`
uses `4(e^{t/2}+e^{-t/2}-2)` with the sum starting at `m=0`.  These differ by
the `m=0` term `4 e^{-t/2}` on both sides.  Recomputed independently, the two
agree to `3.553e-15` over `t in {0.5,1,2,5,9,13}`: the folding is correct.

### B. The minimum is monotone and vanishing (evidence for `L-9506`)

`lambda_min(H^(n)(log(2)/3))` was verified **non-increasing for every
`n = 2..60`**, as Cauchy interlacing requires.  The exact identity
`b^T H b = 2 Psi(nh)` for the all-ones `b` reproduced with relative error
`0.0` in binary64 at every recorded `n`.

```text
   n      lambda_min     2Psi(nh)/n       n*lam     n^2*lam   id.relerr
   4    1.734031e-02   1.825346e-02   6.936e-02   2.774e-01     0.0e+00
   8    5.896532e-03   9.556839e-03   4.717e-02   3.774e-01     0.0e+00
  16    8.796752e-04   6.536212e-03   1.407e-02   2.252e-01     0.0e+00
  32    6.492293e-05   3.507976e-03   2.078e-03   6.648e-02     0.0e+00
  48    2.406416e-05   1.401867e-03   1.155e-03   5.544e-02     0.0e+00
  53    1.928554e-05   2.071504e-03   1.022e-03   5.417e-02     0.0e+00
  60    1.517630e-05   1.332374e-03   9.106e-04   5.463e-02     0.0e+00
```

The `n^2 lambda` column stabilizes near `0.054` for `n >= 36`, so empirically
`lambda_n ~ 0.054 n^{-2}`, faster than the proved `O(1/n)` ceiling.  **This
`n^{-2}` rate is an observation on `n <= 60` only and is not claimed as an
asymptotic.**

### C. Reproduction of `X-9502` and the zero-accounting ratio

**Reproduction.**  Independent implementation, no shared code:

```text
lambda_min(H^(53)(log2/3))   this work   1.9285536890e-05
                             X-9502      1.9285536220e-05
                             rel. diff   3.48e-08
```

consistent with two different binary64 eigensolvers.  The `X-9502` attribution
table also reproduces:

```text
rank  index          ordinate       pair contribution   X-9502 reported
   1    121   271.494055641648         2.960943e-06     2.9609433374e-06
   2     60   163.030709687184         2.602368e-06     2.6023676805e-06
   3    207   407.581460386896         1.379169e-06     1.3791694008e-06
   4    105   244.070898497076         8.257411e-07     8.2574108604e-07
   5    244   462.065367274881         7.813111e-07     7.8131107291e-07

top-5  cumulative   44.33%   (X-9502 reported 44.3%)
top-20 cumulative   63.93%   (X-9502 reported 63.5%)
```

The five ordinates agree with independently computed zeros to `~1e-11`, and
the 1-based indexing is confirmed.  The zero scan found 649 ordinates below
`1000` against `N(T) = theta(T)/pi + 1 = 648.6162`, i.e. `S(T) = +0.38`, so no
ordinate was missed by the scan step.

**Ratio.**  `rho_Gamma = lambda_max(Z_Gamma, H)`, which RH forces to be `<= 1`:

```text
      T  #zeros      rho_Gamma        1-rho   frozen-vector frac   RH violated
     30       3    0.917653283    8.235e-02             0.001491         False
    100      29    0.958050343    4.195e-02             0.021992         False
    300     138    0.984294685    1.571e-02             0.430728         False
    500     269    0.988417038    1.158e-02             0.592278         False
   1000     649    0.993360504    6.639e-03             0.727487         False
```

`rho` rises monotonically with `Gamma` and stays below `1` throughout.  **No
violation was found, at any `T`.  This is consistent with RH.**

The last two columns are the finding.  The optimized `b` accounts for `99.34%`
of the finite screw form, while the frozen `lambda_min` eigenvector — the
direction `X-9502` ranks and deflates against — accounts for only `72.75%`.

### D. Feasibility of the `L-9505` two-sided box

The excess-positive failure mode of (L-9505.15) needs `4 n S_T` below the
Rayleigh scale being tested (`~1.9e-05` here).  With
`S_T ~ (log(T/2pi)+1)/(pi T)`:

```text
         T          S_T      4 n S_T   / lambda_min     zeros below T
     1e+03    1.932e-03    4.096e-01       2.12e+04         6.477e+02
     1e+04    2.665e-04    5.650e-02       2.93e+03         1.014e+04
     1e+06    4.131e-06    8.758e-04       4.54e+01         1.747e+06
     1e+08    5.597e-08    1.187e-05       6.15e-01         2.480e+08
```

The box only becomes non-vacuous near `T ~ 10^8`, requiring of order
`2.5 x 10^8` certified zero bins **and** exact completeness of coverage.  The
excess-positive route is therefore not reachable by this project at `n=53`.
`L-9507` was designed to avoid this requirement.

## Interpretation

1. `D-9501.1` is correctly normalized.  PR #98's unresolved doubt #1 is
   resolved in the affirmative by two independent routes.  The rest of the
   branch rests on a sound foundation.
2. `X-9502`'s central numbers are independently reproduced.  The frozen mode,
   the attribution table, the five influential ordinates, and the prime-power
   counts all check out.
3. The record-small minimum is **not** evidence about RH.  It is a monotone
   non-increasing sequence with a proved ceiling tending to zero (`L-9506`).
   The adaptive-deflation table in the continuation report — residual minimum
   falling from `1.40e-05` to `5.06e-06` as zero pairs are removed — is
   measuring the same forced decay and should not be read as approach to a
   violation.
4. The zero-accounting ratio (`L-9507`) is a scale-free replacement.  Its first
   evaluation gives `0.9934`, below `1`, consistent with RH.
5. Deflating against the frozen `lambda_min` eigenvector optimizes the wrong
   direction, by a wide margin (`0.7275` vs `0.9934`).

## Limitations

- **Everything here is binary64 with round-to-nearest.**  No directed rounding,
  no interval arithmetic, no certified enclosure.  Nothing in this experiment
  may be used as a certificate.
- The zero ordinates come from floating sign changes of a Hardy `Z` computed by
  Euler-Maclaurin.  They are **not** certified zero bins.  The
  Riemann-von Mangoldt count check makes it unlikely that ordinates were
  missed, but "unlikely" is not "proved".
- `rho_Gamma` is computed through a Cholesky congruence of a matrix with
  condition number `6.3e4`.  A value marginally above `1` at this conditioning
  would be a rounding artifact, not a discovery.  None was observed.
- Part A tests `t <= 14` only, because the prime cutoff is `e^t`.  A
  normalization error that switches on only at large `t` would not be caught.
- The `n^{-2}` decay in part B is observed on `n <= 60` and is not an
  asymptotic claim.
- `S_T` in part D uses the Riemann-von Mangoldt density heuristically, not a
  proved tail bound.  It is used only for an order-of-magnitude feasibility
  statement.
- The `X-9502` MPFR artifacts could not be re-run here (no GMP/MPFR). Their
  directed endpoints are **not** independently confirmed by this experiment;
  only the binary64 value they enclose is.

## Associated issues and claims

Issue #95; PR #98.  Claims: `D-9501` (audited), `L-9504` (used), `L-9505`
(feasibility of its box assessed), `L-9506` (new, evidence in part B),
`L-9507` (new, evidence in part C), `X-9502` (reproduced).

## Output digest

```text
experiments/results/X-9503-screw-audit-ratio/audit.json
experiments/results/X-9503-screw-audit-ratio/zeros1000.json
```
