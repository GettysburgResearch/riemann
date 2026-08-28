# Trans-Bertrand native beta Nyquist compression

## Executive result

PR #759 reduced the native beta RH criterion to
`O(log^2 X (loglog X)^2)` deterministic samples. The new construction
interleaves every finite Bertrand box cascade inside one fixed support budget.

The same detector simultaneously enjoys every envelope

\[
 \exp\{-c_m t/W_m(t)\}.
\]

A diagonal schedule therefore beats every fixed iterated-log rank loss while
remaining one fixed source-faithful detector.

## Why this is close to optimal

Compact causality is not free. Exponential Fourier `L2` decay would analytically
continue the kernel across its support boundary and force it to vanish.
Consequently a source-blind exterior theorem cannot work at
`T=O(log X)`, and exact quadratic Nyquist rank is unavailable by this method.

The final square in the Bertrand denominator is also the precise
Cartwright-integrability threshold.

## Remaining arithmetic problem

Nothing in the construction changes

\[
 \sum_{n\le X}\frac{\beta(n)}{\sqrt n}\mathbf v_X(n).
\]

The remaining work is genuine native Möbius cancellation. The analytic
continuum and high-frequency tail are no longer plausible sources of the main
difficulty.
