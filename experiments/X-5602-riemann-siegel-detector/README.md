# X-5602 — Riemann–Siegel detector: the only route with unbounded sensitivity

Experiment ID: `X-5602`
Agent: `opus5-01`
Issue: #55 (spun out of the D-0801 sensitivity analysis)
Branch: `claude/riemann-counterexample-pipeline-io8s2k`
Date: 2026-07-25
Status: executed; validated against `mpmath.zetazero`

## Why this experiment exists

`T-5602` proves that the off-critical quadruple `{1/2 ± eta ± i gamma}` is
invariant under `eta -> -eta`.  Therefore **every** functional of the zero
multiset — Weil positivity, Li coefficients, `n`-level densities, `xi`-passivity
— responds evenly in `eta` and has zero first derivative at `eta = 0`.
`L-5604` measures what that costs in practice: the executed `c = 10^{11}`
D-0801 certificate can only detect a displacement `eta > 3 x 10^-2`, which the
classical zero-free region already forbids at that height.

The single hypothesis that fails for a *counting* functional is
differentiability.  A zero count is a step function of the zero positions: it
detects any `eta > 0` exactly, not as a small perturbation of a large number.
So the counting route is the only family of methods with unbounded sensitivity,
and this repository had no capability to evaluate `zeta` at all.

There is a second asymmetry, and it is large.  To *resolve* individual zeros the
prime side needs `c >= T/2pi` terms (`C-5601`), i.e. `~T` work.  Riemann–Siegel
needs `sqrt(T/2pi)` terms per evaluation — **a square root fewer**.  At
`T = 10^{11}` the D-0801 route spends `4.12 x 10^9` prime-power terms; the same
height costs `~1.3 x 10^5` terms per Riemann–Siegel evaluation.

## What it does

`rs_zeta.c` evaluates the Riemann–Siegel `Z` function

```text
Z(t) = 2 sum_{n=1}^{N} n^{-1/2} cos(theta(t) - t log n) + R(t),
N = floor(a),  a = sqrt(t/2pi),  p = a - N,
R(t) = (-1)^{N-1} a^{-1/2} [ C0(p) + O(a^{-1}) ],
C0(p) = cos(2 pi (p^2 - p - 1/16)) / cos(2 pi p).
```

`Z` is real for real `t` and its real zeros are exactly the zeros of `zeta` on
the critical line, with the same multiplicities.  The driver counts sign changes
on a grid, refines each to a zero by false position, and compares the count with
the smooth census `(theta(t2) - theta(t1))/pi`.  **A deficit that survives grid
refinement means zeros have left the critical line.**

Two implementation points:

- **Huge phases.**  At `t = 10^{13}` the phase `t log n` reaches `1.3 x 10^{14}`
  and is needed to `~10^{-10}`.  Writing `t = T0 + s` with `T0` fixed for a
  scan, the table `A[n] = (T0 log n) mod 2pi` is built once with MPFR at 256
  bits and only the small increment `s log n` is formed per evaluation.  This is
  the `L-5601` technique transplanted; without it the scan is meaningless.
- **`C0` at its removable singularities.**  `cos(2 pi p)` vanishes at
  `p = 1/4, 3/4` where the numerator does too.  The shifted forms
  `C0 = -sin(2 pi u^2 - pi u)/sin(2 pi u)` at `p = 1/4 + u` and
  `C0 = sin(2 pi v^2 + pi v)/sin(2 pi v)` at `p = 3/4 + v`, both tending to
  `1/2`, are used near those points.

## Validation

Against `mpmath.zetazero`, which shares no code with this implementation:

| height | zeros located | max `|located - true|` | mean |
|---|---|---|---|
| `t in [1000, 1060]` | 48 (indices 650–697) | `3.44e-4` | `6.29e-5` |

All 48 matched in order with no missed or spurious zeros.  Single-point checks
at known ordinates give `|Z(gamma)|` of `2.0e-3` at `gamma_1 = 14.1347`,
`3.9e-4` at `gamma = 236.52` — consistent with the `C0`-only remainder, whose
error is `O((t/2pi)^{-3/4})` and therefore falls to `~6e-10` by `t = 10^{13}`.

Grid convergence at `t = 10^{13}`, span 5:

| points per Gram interval | sign changes |
|---|---|
| 8 | 20 |
| 16 | 22 |
| 32 | 22 |
| 64 | 22 |

so 16 is the smallest safe grid at this height and 16–32 is used.

## Executed scan

```bash
./rs_zeta --t0 1e13 --span 1000 --per-gram 16 --threads 4 \
          --emit-zeros --zeros-file results/zeros-1e13.txt \
          --out results/rs-scan-1e13.json
```

`t = 10^{13}` is **above the exhaustive verification height**: Platt–Trudgian
reach `3.0000175 x 10^{12}`.  Odlyzko-type computations have sampled zeros far
higher, but not exhaustively over an interval.  Results are in
`results/rs-scan-1e13.json`; the census deficit and the smallest normalised
neighbour gap (a Lehmer-pair statistic) are the two numbers to read.

## Limitations, stated plainly

- **This is not yet a certified computation.**  The `C0`-only Riemann–Siegel
  remainder is used with the *asymptotic* error `O((t/2pi)^{-3/4})`, not with a
  proven constant; the standard bound (Gabcke) would have to be quoted and the
  binary64 summation error bounded before any sign claim.  At `t = 10^{13}` the
  observed accuracy is `~10^{-9}` against `|Z'| = O(log t)`, so the *counting*
  is robust, but "robust" is not "proved".
- The census compares against the smooth part `(theta(t2)-theta(t1))/pi` only,
  so on its own a deficit is a *flag for investigation*, not a disproof.
  Turing's method proper is now implemented in `turing.py` and `tau_localise.py`
  — but it is **conditional on an imported bound** on `\int S(t) dt`, which this
  repository does not prove.  Two are offered: a deliberately conservative
  `3 + 0.1 log t` and Trudgian's `2.067 + 0.059 log t`.
- A deficit can also come from a grid too coarse to separate a close pair.  Any
  nonzero deficit must be re-run at higher `--per-gram` before it means
  anything.  The convergence table above is the protocol.
- `N = floor(sqrt(t/2pi))` must not change across a scan; the program refuses
  spans that would change it.

## Files

```text
rs_zeta.c                        evaluator, sign-change counter, census
census.py                        empirical Turing: tracks k - theta(gamma_k)/pi
turing.py                        Turing's method proper: which N(t1) survive |D_c + M| <= B
tau_localise.py                  and WHERE inside the window an off-line zero could then sit
verify_d0801_against_zeros.py    the explicit formula's LHS, summed over located zeros
tests/test_rs.py                 validation against mpmath.zetazero and known ordinates
results/                         scans and certificates
```

The load-bearing idea in `turing.py` is that the off-line correction
`M(t) = mult * sum_j (t - tau_j)_+` has a **quantised slope** — `0`, `mult`,
`2*mult`, ... — so an integer count `N(t1)` that is off by an amount not
divisible by `mult` cannot be repaired by any off-line configuration at all.
That is what reduces the surviving alternatives to two at the PR #71 window;
`tau_localise.py` then shows neither can place a zero near the ordinate of
interest.  See `O-5604`.

## Build

```bash
gcc -O3 -march=native -mfma -std=c11 rs_zeta.c -o rs_zeta \
    -lmpfr -lgmp -lpthread -lm
```
