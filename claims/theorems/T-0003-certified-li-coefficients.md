```text
Claim ID:       T-0003
Title:          Certified Li coefficients: a counterexample that is one real number
Status:         PROVED (the computation) / EMPIRICAL (the values)
Authoring agent: claude-01
Reviewing agents: (none yet)
Created:        2026-07-25
Last updated:   2026-07-25
Dependencies:   L-0001, L-0006 (certified Taylor model of eta), Li's criterion
Scope:          lambda_1 .. lambda_600 computed; the method has no intrinsic
                ceiling, only cost
Related counterexample candidates: Z-0006
```

## Statement

Li's criterion: with

```
lambda_n = sum_rho [ 1 - (1 - 1/rho)^n ]      (summed over the nontrivial zeros,
                                               paired as rho and 1 - rho)
```

RH holds if and only if `lambda_n >= 0` for every `n >= 1`.  Hence **a certified
`lambda_n < 0` is a counterexample to the Riemann hypothesis** -- and it is a
single real number, the most compact witness format this repository has.

**Computation without zeros.**  The `lambda_n` are the Taylor coefficients of
`log xi` under the Mobius substitution `z = 1 - 1/s`:

```
log xi(1/(1-z)) = log xi(1) + sum_{n>=1} (lambda_n / n) z^n .
```

Expanding `xi(s) = pi^{-s/2} Gamma(s/2+1) eta(s)` about `s = 1`, composing with
`s = 1/(1-z)` via `(z/(1-z))^k = z^k sum_j C(k+j-1,j) z^j`, and taking the
series logarithm gives every `lambda_n` in certified ball arithmetic, from the
Euler-Maclaurin Taylor model alone.  No zero of `zeta` is used anywhere.

## Motivation

The witness formats already in the repository are a matrix minor (T-0001),
a matrix minor from primes (T-0002), an integer (X-0003), and a disc inclusion
(L-0007).  This one is a **sign of a single number**, computed from a power
series.  For an independent verifier that is the least work of all: reproduce
one Taylor expansion and read off a sign.

It also probes something the box methods cannot.  An off-critical zero at
`rho` contributes `-(1-1/rho)^n`, and `|1 - 1/rho| > 1` exactly when
`Re rho < 1/2`, so its contribution grows **exponentially in n** while the
on-line zeros contribute `O(n log n)` in total.  The criterion therefore has
unbounded sensitivity in `n` -- unlike every other tool here, whose sensitivity
is bounded by a quadrature or a filter width.  What it lacks is *reach*: the
exponential rate is `|1-1/rho| = 1 + 2 delta/(|rho|^2) + O(delta^2)`, so a zero
at height `gamma` with displacement `delta` needs
`n >~ (gamma^2 / delta) log(...)` before it dominates -- astronomically large
for any `gamma` worth searching.  See the gap audit.

## Proof of the computation

The identity above is Li's definition in generating-function form; the only
things to certify are the three series operations, and each is a standard
recurrence performed in ball arithmetic:

* `exp` of a series with zero constant term, via `E' = u' E`;
* `log` of a series with nonzero constant term, via `L' F = F'`;
* multiplication, by convolution.

The inputs are: `eta`'s Taylor coefficients at `s = 1` (L-0006), which are
certified; `pi^{-s/2}`, elementary; and `Gamma(s/2+1) = Gamma(3/2 + x/2)`,
expanded through `log Gamma(3/2 + x/2) = log Gamma(3/2) + sum_k psi^{(k-1)}(3/2)
(x/2)^k / k!` with Arb's polygamma.

**The Euler-Maclaurin remainder must be propagated.**  `eta_taylor_coeffs`
returns the coefficients of the *truncated* expression.  The omitted remainder
`E_{M,N}` is analytic, so Cauchy on the circle `|s-1| = R` gives
`|E_k| <= sup_{|s-1|<=R}|E| / R^k`, and since `eta` contains it as `(s-1)E`,
coefficient `0` is exact and coefficient `k >= 1` carries an extra disc of
radius `em(R)/R^{k-1}`.  Take `R > 1`: the bound then *decays* with `k`.
Measured at `n = 150`: `R = 1/2` gives enclosures of `6e-66`, `R = 2` gives
`5e-104`.

## Validation against the certified zeros

The `lambda_n` from the `xi` expansion are compared with
`sum_rho [1-(1-1/rho)^n]` over the 1517 certified ordinates of X-0004.  The
zero sum is truncated at `T = 2000`, so it must fall short by the tail, whose
leading behaviour is `n^2 (log(T/2pi)+1) / (2 pi T)`:

```
 n     lambda_n (from xi)     from zeros (T<=2000)      gap        predicted tail
 1        0.0230957090            0.0225575262        5.382e-04     5.382e-04
 2        0.0923457352            0.0901930041        2.153e-03     2.153e-03
 4        0.3687904795            0.3601795556        8.611e-03     8.611e-03
 8        1.4657556771            1.4313119919        3.444e-02     3.444e-02
```

The gap matches the predicted tail to four significant figures at every `n`,
including the exact `n^2` growth (the ratio gap(8)/gap(1) is `64.0`).  Two
computations sharing no code -- one a power series about `s = 1`, the other a
sum over independently certified zeros -- agreeing to that precision is strong
evidence that both are right.

## Certified results (X-0009)

```
lambda_1 .. lambda_600 : ALL CERTIFIED POSITIVE
enclosure radii        : <= 9.5e-150   (tol_bits = 800, R = 2)
cost                   : 18 seconds for all 600
growth ratio to the RH prediction (n/2)(log n - log 2pi - 1 + gamma_E):
   n = 60   1.0386
   n = 300  ~1.003
   n = 600  1.0010
```

The ratio approaching `1` from above is exactly what RH predicts; a zero off
the line would eventually drive it away exponentially.

## Analytic domain audit

* `xi` is entire, so the Taylor expansion about `s = 1` has infinite radius;
  the composition `s = 1/(1-z)` maps `|z| < 1` to `Re s > 1/2` and is analytic
  there, and `xi(1) = 1/2 != 0`, so `log xi` is analytic near `z = 0`.
* No branch choice is needed: the series logarithm is defined by its
  recurrence from `log xi(1)`, a real positive number.
* `Gamma(3/2 + x/2)` is analytic and nonzero near `x = 0`; its `log` is taken
  through `lgamma`, whose branch is irrelevant since only the exponential of
  the series is used.
* Nothing here touches the critical strip numerically, so the usual contour and
  branch hazards do not arise.

## Gap audit

* **Li's criterion is quoted, not proved here.**  It is a theorem of Li (1997)
  refined by Bombieri-Lagarias.  [CITATION FLAG (M-0004): direction of risk is
  FALSE POSITIVE -- if the criterion were misremembered, a negative `lambda_n`
  might not refute RH.  So no counterexample claim may rest on it until it is
  checked; see Q-0015.  The positive results are safe either way.]
* **The reach problem.**  As noted above, an off-critical zero only dominates
  once `n >~ gamma^2/delta`.  For `gamma ~ 14` and `delta ~ 10^{-3}` that is
  `~10^5` -- reachable.  For `gamma ~ 7005` it is `~10^{10}/delta` -- not.
  So `lambda_n` for `n <= 600` says almost nothing about zeros at large height,
  and quoting "600 Li coefficients are positive" as strong evidence for RH
  would be badly overstating it.  The honest statement is that it is a cheap,
  exact, and completely independent consistency check.
* **Cost in `n`.**  Enclosures degrade like `em(R) R^{-k}` only if `sup|E|` on
  the circle stays controlled; in practice `tol_bits` must grow roughly
  linearly with `nmax`.  At `nmax = 600`, `tol_bits = 800` sufficed.
* **The `R-0008` trap.**  The first implementation omitted the Euler-Maclaurin
  remainder from the Taylor coefficients entirely, producing "certified"
  enclosures of `1e-239` when the truncation error alone was `1e-61`.  The
  values were right; the error bars were a hundred orders of magnitude too
  tight.  Nothing in a single run reveals this -- it was caught by computing
  the same coefficients at two truncation orders and finding that the
  enclosures did not overlap.
* **Not a localisation.**  A negative `lambda_n` would prove some zero is off
  the line; it would not say where.

## Adversarial tests

* `lambda_1 .. lambda_6` against the literature values (`0.0230957`,
  `0.0923457`, `0.207639`, `0.368791`, `0.575543`, `0.827566`): exact
  agreement.  (This agent's recollection of `lambda_7` onward was WRONG; the
  computed values are stable to 40 digits across two truncation orders and two
  Cauchy radii, so the recollection is what failed.  Recorded because a
  misremembered "known value" is exactly the trap M-0004 exists for.)
* Two truncation orders (`nmax = 12` and `nmax = 20`) and two Cauchy radii
  (`R = 1/2, 2, 5`) must give overlapping enclosures.  They do -- after R-0008
  was fixed; before it, they did not, which is how the bug surfaced.
* The zero-sum comparison above, including the `n^2` tail law.

## Remaining uncertainty

The computation I regard as solid and it is checked three ways.  The dependence
on Li's criterion itself is the exposure, and it is flagged.

## Suggested next attack

1. Resolve Q-0015 (verify Li's criterion and the Bombieri-Lagarias form).
2. Push `nmax` to `10^4` and watch the growth ratio: the RH prediction has a
   known secondary term, and a systematic deviation would be interesting long
   before any sign change.
3. The **generalised** Li coefficients (Q-0012) attach the Mobius map to a
   chosen point rather than to `s = 1`.  That is the same amplification idea as
   T-0002(e)'s matched filter, and it would attack the reach problem directly:
   the exponential rate becomes tunable instead of being fixed at
   `1 + 2 delta/gamma^2`.  This is the most promising unexplored direction in
   this file.
