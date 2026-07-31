# Positive route continuation — eta window and reflection linearization

Date: 2026-07-31  
Agent: `gpt56-05-l`  
Issue: #180  
Branch: `agent/gpt56-05-l/154-nonlocal-barta-floor`

## Objective

Continue the positive route toward

```text
sup |Q(x)| < infinity
```

or bounded Cesaro mean square, while preserving the order-`X^2` cancellation
identified in `L-15411`.

## Result 1 — ratio 8 instead of ratio 64

The triangular construction is not tied to `h=log 4`. For every fixed `h>0`,
use contrast coefficient `c=exp(h/2)`. The transform is

```text
((1-exp(-hz))/(hz))^2 (1-exp(-h(z-1/2))).
```

It cancels the zeta pole and has no zero in the open counterexample strip. The
active annulus ratio is `exp(3h)`.

At `h=log 2`, the contrast is `sqrt(2)`, the annulus ratio is exactly `8`, and
the pole factor is the Dirichlet-eta factor `1-2^(1-s)`. The statistic has three
exact producer forms: direct ratio-8 window, four hinges in `Q(sqrt(2))`, and a
triangular smoothing of

```text
Lambda(N)-2 Lambda(N/2).
```

The corresponding real-half-plane zeta distribution has the exact covariance

```text
Cov((-1)^(N-1), log N) = -(log 2) 2^(1-s).
```

This is a useful parity/Markov normalization, but it does not continue as a
probabilistic contraction to the critical boundary.

## Result 2 — exact reflection linearization

Let

```text
F=-zeta'/zeta,
X=chi'/chi.
```

The functional equation gives

```text
F(1-s)=-F(s)-X(s)
```

and therefore

```text
F(s)F(1-s)
 =-F'(s)-zeta''(s)/zeta(s)-X(s)F(s).
```

The coefficient stream of `zeta''/zeta` is

```text
Lambda(n) log n + (Lambda*Lambda)(n) >= 0.
```

After vertical integration by parts, the reflected quadratic energy is a
linear combination of one von Mangoldt stream, one positive Selberg stream, and
one archimedean convolution. This replaces the explicit double prime-pair sum.

The remaining RH-strength object is the contour/Hardy defect between this
reflected bilinear form and the positive Abel--Hardy norm. It must retain every
zero residue crossed between the initial and critical lines.

## Exact artifact

`X-15407` checks:

- the eta hinge polynomial in `Q(sqrt(2))`;
- constant, linear, and pole-mode annihilation;
- the exact energy `h||G||^2=2-sqrt(2)/3`;
- the reflection identity on rational synthetic data;
- nonnegative synthetic Selberg coefficients.

The connector environment had no checkout or `gh`, so the committed unittest
module was not invoked directly. An independent in-session exact
`Fraction`/quadratic-field reconstruction replayed the retained certificate and
all rejecting mutations.

## Strongest new proof target

The positive programme can now be organized as

```text
ratio-8 direct prime window
  -> exact reflected Selberg replay
  -> complete contour residue ledger
  -> Pick/de Branges or matrix-carry defect bound
  -> uniform Abel--Hardy estimate
  -> RH.
```

This is materially cleaner than estimating the order-`X^2` prime-pair sum
termwise. No final defect inequality is currently proved.

## Status

- `L-15414`: `PROPOSED`.
- `L-15415`: `PROPOSED`.
- `M-15405`: `PROPOSED`.
- `X-15407`: exact finite algebra with independent in-session reconstruction.
- Bounded pointwise or mean-square prime window: not proved.
- RH: not proved.
