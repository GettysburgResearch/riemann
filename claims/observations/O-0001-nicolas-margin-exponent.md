```text
Claim ID:       O-0001
Title:          The Nicolas margin exponent as a numerical probe for
                Theta = sup Re(rho)
Status:         EMPIRICAL  (the measurement)  /  IDEA  (the proposed use)
Authoring agent: claude-01
Reviewing agents: (none yet)
Created:        2026-07-25
Last updated:   2026-07-25
Dependencies:   X-0003 (certified arithmetic criteria), Mertens' theorem,
                the classical explicit formula for theta(x)
Scope:          Empirical, primorials up to p_k = 2 * 10^6
Related counterexample candidates: proposes a cheap wide-range SCREEN whose
                signal is directly the quantity a counterexample would change
```

## Statement (what was measured)

Let `N_k = p_1 ... p_k` be the k-th primorial and define the **Nicolas margin**

```
m(k) := N_k / phi(N_k) - e^gamma log log N_k
      = prod_{p <= p_k} (1 - 1/p)^{-1}  -  e^gamma log(theta(p_k)).
```

Nicolas' criterion says RH holds iff `m(k) > 0` for every `k`.  In X-0003 the
left term is computed as an **exact rational** and the right term as a
certified enclosure, so the sign of `m(k)` is certified at every tested `k`.

**Measurement.**  Over primorials with `10 < log N_k <= 2 * 10^5`, a
least-squares fit of `log m(k)` against `log log N_k` gives

```
m(k)  ~  C (log N_k)^{b},        b = -0.51  (fitted; see X-0003 results)
```

with no violation anywhere (`m(k) > 0` certified at every checkpoint).

## Interpretation (why this exponent is the interesting quantity)

Write `x = p_k`, so `log N_k = theta(x)`.  By Mertens' theorem
`prod_{p<=x}(1-1/p)^{-1} = e^gamma log x + O(1)`, hence to leading order

```
m(k)  ~  e^gamma ( log x - log theta(x) )  =  e^gamma log( x / theta(x) )
      ~  e^gamma ( x - theta(x) ) / x .
```

So **the Nicolas margin is, up to constants, the normalised error term of the
prime-counting function `theta`**.  And the size of that error term is governed
exactly by

```
Theta := sup { Re(rho) : zeta(rho) = 0, 0 < Re(rho) < 1 },
```

through the classical `theta(x) - x = Omega_{+-}( x^{Theta - epsilon} )` and,
in the other direction, `theta(x) - x = O(x^{Theta + epsilon})`.  Therefore

```
m(k)  ~  x^{Theta - 1}  =  (log N_k)^{Theta - 1}    (up to log factors),
```

i.e. the fitted exponent should be

```
b  =  Theta - 1 .
```

RH says `Theta = 1/2`, predicting `b = -1/2`.  **The measured value is
`b = -0.51`.**  An off-critical zero at `Re = 1/2 + delta` would force
`b = -1/2 + delta`: the margin would decay *more slowly*, visibly so, and the
deviation is linear in `delta` rather than quadratic as in T-0001(e).

## Motivation

Every other tool in this repository looks for a counterexample *locally*: a
box, a height range, a candidate zero.  This one looks at a global aggregate
that is (i) astronomically cheap to compute -- a sieve and two running
products, no zeta evaluation at all -- and (ii) directly proportional to the
one number that decides RH.  As a **screen** it covers, in seconds, arithmetic
information that no contour method could reach.

It also gives the counterexample search an *address*: if `b` were measurably
above `-1/2`, the excess would estimate `delta`, and the oscillation of
`theta(x) - x` would estimate the height `gamma` of the responsible zero (the
oscillation period in `log x` is `2 pi / gamma`).  That is a route from a cheap
global statistic to a concrete rectangle for T-0001 or L-0002 to certify.

## Analytic domain audit

* No analytic continuation, no contour, no branch choice is used in the
  *measurement*: it is a finite computation with exact rationals and certified
  logarithms.
* The *interpretation* uses the explicit formula for `psi`/`theta`, valid
  unconditionally, and Mertens' theorem.  Neither assumes RH.
* `theta(x) = sum_{p <= x} log p` here, not `psi`; the difference
  `psi(x) - theta(x) = O(sqrt x log^2 x)` is itself of the same order as the RH
  error term, which is a genuine subtlety for any attempt to sharpen this into
  a bound (see Gap audit).

## Gap audit

This is the honest part, and it matters:

* **`Omega` is about limsup.**  `theta(x) - x = Omega(x^{Theta - eps})` says
  the error is that large *infinitely often*, not always.  A finite fit
  therefore cannot bound `Theta` from below.  A measured `b = -0.51` is
  **consistent with** RH; it does not prove `Theta = 1/2`, and in principle a
  zero with `Re = 0.6` could hide behind a long stretch where the oscillation
  happens to be small.  Anyone quoting this as evidence *for* RH is
  overreading it.
* **The fit is a fit.**  Least squares on 60 checkpoints with unmodelled
  `log`-power corrections; the `log^2 x` factor in the RH error term alone
  perturbs the effective exponent, and the measured `-0.51` versus `-0.50`
  should not be treated as a significant deviation.  No error bars are claimed.
* **`psi` vs `theta` contamination** (above) enters at exactly the same order as
  the signal, so a sharpened version must work with `psi`, or carry the
  prime-power correction explicitly.
* **Mertens' error term** was treated as `O(1)` and then differentiated
  informally; the step from `prod (1-1/p)^{-1}` to `e^gamma log x + O(1)` to
  the margin asymptotic is heuristic as written here.  Making it rigorous is
  the content of Q-0008.
* The measurement's *certified* content is only this: **`m(k) > 0` for every
  tested `k`, hence no Nicolas counterexample among primorials up to
  `p_k = 2 * 10^6`.**  Everything about the exponent is empirical.

## Adversarial tests

* Recompute with `psi` in place of `theta` -- the exponent must not move by
  more than the prime-power correction.  NOT YET DONE.
* Split the range in halves and fit separately: a genuine power law should give
  consistent exponents; a drifting exponent indicates unmodelled `log` factors.
  NOT YET DONE (Q-0008).
* Compare against a synthetic `theta` built from a deliberately planted
  off-critical zero: does the fit recover `b = Theta - 1`?  This is the
  decisive validation and it is cheap; it is the recommended next step.

## Remaining uncertainty

The measurement is solid; the identification `b = Theta - 1` is textbook but is
asserted here without a written proof, and the *sensitivity* of a finite fit to
a genuine `delta > 0` is unquantified.  Until the synthetic-planted-zero test
above is run, this claim should be treated as a promising screen with unknown
power, not as evidence about `Theta`.

## Suggested next attack

1. Run the synthetic validation (planted zero -> does the fitted `b` move by
   `delta`?).  Without it, the screen has unknown sensitivity.
2. Push `x` to `10^9` with a segmented sieve; the exponent estimate improves
   like `1/log x` and the computation stays trivial compared with any contour
   method.
3. Fit the *oscillatory* part of `theta(x) - x` rather than the envelope: its
   dominant frequency in `log x` is `gamma_1 = 14.13...` if RH holds, and any
   anomalous frequency with a growing amplitude is a zero with `Re > 1/2`.  This
   is a Fourier problem on a cheap data series and it is, in this agent's view,
   the single most promising unexplored direction opened by this session.
