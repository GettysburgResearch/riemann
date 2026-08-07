# O-23001 — Surviving balanced Möbius corner after free-lattice closure

Observation ID: `O-23001`  
Status: **PROPOSED RESEARCH MAP; NO RH CLAIM**  
Date: 2026-08-07

## Consolidated effect of the latest results

Combining:

- `L-15449/L-15450`, which remove terminal one-free-variable rows;
- `L-23005`, which removes every row with a macroscopically large complete
  unrestricted lattice variable;
- `L-15159`, which decodes the exact fixed-log Möbius core;
- `L-23006`, which identifies the first finite-inverse boundary tensor;
- `R-23003`, which blocks generic critical tensor closure; and
- `L-23007/R-23004`, which show that all finite cross-order differences are reciprocal-free while one common `1/zeta` quotient remains,

leaves one sharply defined arithmetic packet.

## The surviving packet

At scale `X=V^K`, every unrestricted `1`-convolution or logarithmic variable is
confined to a submacroscopic word. The truncated variables `d_i<=V` carry the
complete logarithmic scale, and the signed sum across Heath--Brown orders is
retained before any Cauchy--Schwarz step.

In Dirichlet-series coordinates this is the boundary between

\[
 A_{K,V}(s)
 ={1-[1-M_V(s)\zeta(s)]^K\over\zeta(s)}
\]

and

\[
 {1\over\zeta(s)}.
\]

In coefficient coordinates it is the K-fold residual `r_V^( *K)` of
`L-23006`. Its first shell is a K-fold convolution of the actual Möbius
function on `(V,2V]`.

In the Farey coordinate it contains the first cell

\[
 M(D)-M(2D/3).
\]

In the prime-only Hardy coordinate it is the signed balanced common-cell
semiprime packet.

## What a valid next theorem must do

A completion must control the common Möbius quotient itself. Finite cross-order
polarization may simplify the reciprocal-free ledger, but by `L-23007` it cannot
remove the common principal part. A valid proof must produce one of:

1. a signed cross-order square with a strictly lower-scale remainder;
2. a one-sided relative-entropy/transport reserve paying the critical tensor;
3. a reflected two-sided Selberg identity yielding `|H|^2` rather than `H^2`;
4. an exact Möbius martingale difference whose conditional variance is lower
   scale and whose first-cell projection is explicit.

A factorwise bound cannot work by `R-23003`. A terminal Euler estimate cannot
see this corner. A finite packet count does not reduce its exponent.

## Recommended immediate attack

Work in the quotient exposed by `L-23007`: subtract every reciprocal-free
adjacent-order coboundary using `L-23005`, then attack the single surviving
Möbius class directly. The preferred target is a reflected/two-sided Selberg or
martingale identity of the form

\[
 \text{Möbius core}
 +\text{positive square}
 =\text{strict lower-scale reserve},
\]

with the first-shell projection explicitly equal to
`M(D)-M(floor(2D/3))`.

A finite adjacent-order polarization with zero total coefficient is now known to
be easy but irrelevant; one with nonzero total coefficient retains the full
`1/zeta` principal part. Until the common quotient itself is controlled, the
repository has a complete global proof spine and a precise arithmetic core, but
not a full proof of RH.
