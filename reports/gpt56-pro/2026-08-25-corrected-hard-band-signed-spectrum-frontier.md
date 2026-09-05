# Corrected hard-band signed-spectrum frontier

## Binding audit

The signed source/complement index split on PR #731 is exact.  Its claimed
visible cost `<1/600`, however, was inherited from finite source-density
inequalities.  Those inequalities do not estimate the compressed Hankel
operator of the meromorphic all-pass quotient.

The exact counterfamily is

```text
N=1, D=z^m, U=N/D=z^(-m).
```

Here `N-D` is analytic and has zero Hankel operator, while

```text
||H_U P_d||_HS^2=min(d,m).
```

Thus the former numerical promotion is not available.

## Exact replacement

For a hard positive-frequency source band `[0,H]`, the literal visible charge
is

\[
V_H^-(U)=\int_0^\infty
 \min(H,\xi)|\widehat U(-\xi)|^2d\xi.
\]

The exact signed complement is

\[
\Delta_H(U)=\int_H^\infty(\xi-H)
 \bigl(|\widehat U(-\xi)|^2-|\widehat U(\xi)|^2\bigr)d\xi.
\]

Hence

\[
R_0\ge R_2-V_H^-(U)-(\Delta_H(U))_+-o(N).
\]

For simple upper companion poles `b_j=a_j+iy_j`, the visible term is the
explicit positive Gram

\[
\sum_{j,k}c_j\overline{c_k}
{1-e^{-H\alpha_{jk}}\over\alpha_{jk}^2},
\qquad
\alpha_{jk}=y_j+y_k-i(a_j-a_k),
\]

and the unobserved term has `e^(-H alpha_(jk))` in the numerator.  Repeated
poles are exact derivatives of these kernels.

## Correct ninety-percent target

The unconditional fixed-order input leaves the exact allowance

\[
{599\over625}-{9\over10}={73\over1250}=0.0584.
\]

Therefore the honest conclusion-bearing statement is

```text
HARDSIGNED106440:

limsup [V_T+(Delta_T)_+]/N < 73/1250.
```

A separately proved actual-quotient visible bound `<1/600` would restore the
signed-tail allowance `851/15000`, but the source-density contraction by itself
does not prove that row.

## Research direction

The corrected normal form suggests two non-equivalent attacks:

1. estimate the shallow endpoint-companion residue Grams directly, retaining
   pole/zero cancellation in the signed complement;
2. combine the current--Turan hierarchy on PR #729 with its exact physical
   phase-collision commutator, proving a source-to-quotient transfer whose
   conclusion is the visible Gram above.

The second route is structurally preferable: the positive higher-chaos reserve
can absorb the commutator without paying all-pass oscillations that commute
with the source.

## Status

```text
signed index split                               PROVED EXACT
visible source-density constant <1/600           PROVED AT SOURCE SCOPE
source-density -> visible quotient Hankel cost   REFUTED
hard-band visible/signed-tail formulas           PROVED EXACT
residue/exponential Gram                         PROVED EXACT
HARDSIGNED106440                                 OPEN / RECORD-BEARING
ninety percent / density one / RH                UNPROVED
```
