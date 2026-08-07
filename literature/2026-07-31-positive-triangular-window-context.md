# Literature context for the positive triangular-window route

Date: 2026-07-31  
Agent: `gpt56-05-l`  
Claims: `L-15409`--`L-15413`, `T-15406`, `M-15404`

## Scope and priority boundary

No priority claim is made for the broad equivalences

```text
RH
<-> square-root-scale prime-number-theorem mean square
<-> critical Hilbert-space approximation
<-> positivity of a zeta screw kernel
<-> absence of interior poles of a smoothed logarithmic derivative.
```

These belong to classical work of Cramer, Weil, Nyman--Beurling, and the
explicit-formula tradition. The repository contribution is the exact synthesis
around one finite triangular prime-power window, its positive renewal primitive,
and the precise cancellation barrier.

## Mean square of the PNT error

Brent, Platt, and Trudgian, arXiv:2008.06140, emphasize that under RH

```text
integral_X^(2X) (psi(x)-x)^2 dx = O(X^2),
```

while if RH is false the normalized mean square is unbounded. Their work gives
explicit conditional constants and an unconditional positive lower bound.

`T-15406` is a compact multiplicative-window version of the same critical
phenomenon. The triangular window removes the pole and all irrelevant low-order
modes, while `L-15411` exposes the prime-side quadratic diagonal that must be
canceled.

## Screw function and infinite divisibility

Nakamura and Suzuki, arXiv:2306.08317, give an exact prime formula for the zeta
screw function `g_zeta` and prove that RH is equivalent to `exp(g_zeta)` being
the characteristic function of an infinitely divisible distribution. Under RH,
`g_zeta` has a zero-frequency representation with positive zero multiplicities.

`L-15410` applies one fixed finite-difference polynomial

```text
(1-r)^2(1-2r)
```

to that exact formula. The exponential pole, linear term, and constant term are
killed, and the remaining elementary gamma correction is exponentially small.
Thus the triangular prime window and the screw/infinite-divisibility route are
the same positive problem in two coordinates.

## Von Mangoldt chains

Alexeev, Barreto, Li, Lichtman, Price, Shah, Tang, and Tao,
arXiv:2605.00301, introduce the von Mangoldt downward transition

```text
P(n -> n/q)=Lambda(q)/log n,
```

using the exact identity

```text
sum_(q|n) Lambda(q)=log n.
```

They construct invariant and sub-invariant weights, adjoint upward chains, and
a continuous zeta process, with applications to primitive sets and divisibility
chains.

`L-15412` records the additive-log convolution form of the same identity:

```text
mu*nu=t nu,
mu=sum Lambda(q)/q delta_(log q),
nu=sum 1/n delta_(log n).
```

`L-15413` gives the resulting one-step absorption interpretation. The RH target,
however, is a critical boundary square-function estimate far sharper than the
probability-region contraction estimates used in the primitive-set work.

## Nyman--Beurling context

The renewal equation is another stable-inversion formulation of the zeta
problem. Convolution by `nu` has Laplace multiplier `zeta(1+z)`. Recovering the
prime measure requires division by this multiplier. Reaching the weighted
boundary `Re z=-1/2` while permitting boundary zeros but excluding interior zeros
is structurally analogous to Nyman--Beurling/Baez--Duarte critical approximation.

A 2026 JMAA paper by Jongho Yang studies a Friedrichs angle between
Nyman--Beurling subspaces. This reinforces that subspace geometry and critical
stable inversion remain active formulations, but it does not supply the
triangular renewal square-function bound.

## Selberg symmetry

The positive arithmetic measure

```text
t mu + mu*mu
```

has Laplace transform `zeta''/zeta(1+z)` and coefficients

```text
[Lambda(n) log n + (Lambda*Lambda)(n)]/n >= 0.
```

Classical Selberg symmetry uses this positivity to prove the PNT without
zero-free-line input. `M-15404` asks for a substantially sharper signed energy
identity retaining the quadratic cross term. Applying the classical Selberg
error term after absolute values is too weak at the `exp(-x/2)` scale.

## Current literature conclusion

The newest primary work supplies useful machinery:

- localized Weil/screw operators;
- exact finite dictionaries;
- sharp time-frequency packet estimates;
- von Mangoldt Markov chains;
- conditional and explicit PNT mean-square bounds.

None currently proves the critical triangular renewal square function
unconditionally. The remaining statement is not a routine smoothing estimate:
`L-15411` shows it requires order-`X^2` signed off-diagonal cancellation.

## Accessible primary sources

- R. P. Brent, D. J. Platt, T. S. Trudgian,
  *The mean square of the error term in the prime number theorem*,
  arXiv:2008.06140.
- T. Nakamura, M. Suzuki,
  *[zeta screw function / infinite divisibility paper]*,
  arXiv:2306.08317, current March 2026 version.
- B. Alexeev et al.,
  *Primitive sets and von Mangoldt chains: Erdos Problem #1196 and beyond*,
  arXiv:2605.00301.
- M. Suzuki,
  *Weil's quadratic form via the screw function*,
  arXiv:2606.09096.
- J. Yang,
  *A Friedrichs angle between the Nyman--Beurling spaces and the Riemann
  hypothesis*, J. Math. Anal. Appl. 560 (2026), 130494.

Every imported theorem and normalization remains subject to independent review
before a project-wide claim is accepted.
