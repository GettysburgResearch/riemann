# Integration handoff — Issue #215 global attack

## Add

```text
L-21501  explicit triangular safe prime window
T-21501  terminal-prime Hardy-energy exponent
L-21502  finite prime-pair Gram energy and off-diagonal exponent
L-21503  Selberg log-convolution Riccati identity
M-21501  global multiplicative-dispersion attack
X-21501  exact finite Gram regression
```

## Dependency order

```text
L-21501
-> T-21501
-> L-21502
-> M-21501

L-21503 is an independent exact arithmetic identity feeding M-21501.
```

The three-way exponent comparison in `T-21501` is conditional on independent
review of `T-19801/L-19802/L-20704`; those claims are not dependencies of the
new Hardy-energy proof itself.

## Registry and status

All theorem and lemma claims are `PROPOSED` pending review. The exact finite
checker is a synthetic algebra regression. No RH result is claimed.

## Project-direction recommendation

Treat the following as the primary global arithmetic target:

\[
 [\mathcal O_G(X)]_+=\exp(o(X)),
\]

where `O_G` is the off-diagonal part of the exact finite prime-pair Gram in
`L-21502`.

Finite direct-`xi`, Pick, prolate, zero-frame, and D-0001 computations remain
valuable for falsification, normalization checks, and discovery. They should
not displace the global coherence estimate unless they supply an actual
exhaustion theorem.

## Merge/integration concerns

1. `L-21501` deliberately uses a piecewise-linear window; do not import
   arbitrary-order tail claims from smoother windows into it.
2. `T-21501` uses the product
   `widehat G * (-zeta'/zeta)` across the removable pole. Do not bound the two
   factors separately at `z=1/2`.
3. The exact energy exponent uses cumulative `L^2`, not pointwise boundedness.
4. The prime-pair diagonal is harmless; entrywise absolute-value bounds on the
   off-diagonal destroy the only relevant cancellation.
5. A finite energy ladder is not a proof of `exp(o(X))`.

## SERIOUS RESOLUTION PATH

```text
prove a subexponential upper envelope for the complete off-diagonal
multiplicative prime-pair energy of L-21502.
```

This single theorem implies RH through `T-21501` and simultaneously closes the
rightmost-zero exponent measured by the square-screw and D-0001 constant
coordinate, subject to review of their transfer identities.
