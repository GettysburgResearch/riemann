# O-99250 — The live graph collapses to one scalar SHARP Harnack tail

Claim ID: `O-99250`  
Status: **LIVE ROUTE SYNTHESIS AT FROZEN SHAS**  
Created: 2026-08-19  
RH status: **unproved**

## Frozen review graph

The conclusion-facing sequence was read in this order:

```text
PR #635 @ b8d4772b5cab0655b3edf68864df6d925c76b5ba
    refutes the constant-score / same-row composition;

PR #638 @ 73ee57ccc684f4062769a6d1c0456b3ef6318db2
    proves the second-order Volterra inverse has two boundary modes and knot atoms;

PR #636 @ 387f775f95d5e21e01c3fb39d91acc5b67f62b02
    isolates fixed-row positivity and a common-parent tree, conditional on a root frame;

PR #642 @ 07aa0d4838458a1b2d3af9e5bc96616baa6b4767
    replaces that root frame by an exact positive SHARP row kernel.
```

The exact kernel theorem is the decisive advance. It identifies one scalar
signed state

\[
\Psi(x)=\sum_{n\le x}\mu(n)n^{-1/2}T(x/n)
\]

as the primitive source of every fixed component row.

## Interface reconstruction

The kernel source exposes two facts that were previously separate obligations:

1. `Q_Y(j)/T(Y)` is increasing because the normalized kernel density is
   pointwise increasing in `Y`;
2. every smaller endpoint is a Radon–Nikodym thinning of the same parent
   density.

Thus compact Hall profile monotonicity, Hall bonus positivity, and one-parent
child ownership are all consequences of one formula. The exact child factor is

\[
\mathbf1_{t\le Z}\frac{T(Z/t)}{T(Y/t)}.
\]

A raw support cut is not exact and is retained as a negative control.

## Scalarization before composition

Once every row is a positive convolution of `Psi`, it is wasteful to carry a
row index, a vector measure, two Volterra anchors, and a recursive common-parent
proof into the analytic consumer. Apply the factor-67 dilation to `Psi` itself:

\[
\mathfrak H_{67}(x)=\Psi(x)-67^{-1/2}\Psi(x/67).
\]

This has four simultaneous advantages:

```text
one real scalar instead of every physical coordinate;
local coefficient (1,-2,1) at 67 instead of an implicit endpoint frame;
a direct reciprocal-zeta Mellin transform with automatic zero noncancellation;
a strict descent coefficient 67^(-1/2)<1/8.
```

The exact directed scan through `10^8` has a lower minimum above `1.2834`, far
from a rounding-level sign decision.

## Current disposition

The strongest conclusion-facing route is now

\[
\boxed{
\mathfrak H_{67}(x)\ge0\quad(x\ge100000001)
}
\]

plus an exact finite theorem below that point. This one tail implies RH directly
by Landau and also regenerates the full PR #642 component-row chain.

This is not a proof of the tail. It is a reduction with all previously named
composition interfaces either reconstructed exactly or removed from the
conclusion-facing path.
