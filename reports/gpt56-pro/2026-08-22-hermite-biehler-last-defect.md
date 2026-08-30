# Research report — Hermite–Biehler last-defect continuation

## Motivation

PR #716 converted Levinson's intuition into exact real and complex counting,
but its final `RPCH104501` statement was the off-real zero count in expanded
notation. This continuation replaces that tautological middle gate.

## New coordinates

The companion

\[
E_{k,\lambda}=\Xi^{(k)}-i\lambda\Xi^{(k+1)}
\]

has three decisive properties:

```text
E_(k,lambda)' = E_(k+1,lambda);
its lower-half-plane index equals the nonreal-pair count of the parent;
its real-axis phase velocity is the normalized Laguerre defect.
```

The exact antiderivative interval makes reverse Rolle constructive: once the
derivative is real-rooted, one scalar interval decides whether its parent is.

## High derivative

The tilted Xi Fourier measure gives a companion asymptotic to `exp(i w_n z)`.
On boxes with `T_n sqrt(log n/n)->0`, the companion is zero-free in the lower
half-plane. This provides a direct Hermite–Biehler entry, rather than only a
real-zero count.

## Last event

If Xi has an off-line zero in a fixed rectangle, descend from the high
companion to the largest derivative index still carrying a lower zero. The
index can disappear only through:

```text
one positive real residue of Xi^(k)/Xi^(k+1);
or one vertical boundary flux.
```

This is the new frontier. It does not sum power-sized or cancellation-prone
charges across all derivatives.

## Current status

The branch proves no RH theorem. Its contribution is an exact global index, a
sharp converse-Rolle interval, the strip theorem, and a last-event
localization. The two last-event exclusions remain open.
