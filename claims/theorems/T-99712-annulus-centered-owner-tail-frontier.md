# T-99712 — Annulus-centered owner-tail closure frontier

Claim ID: `T-99712`  
Status: **CONCLUSION-COMPLETE REDUCTION; ONE MULTIPLICATIVE TAIL PACKING OPEN**  
Created: 2026-08-20  
Depends on: `L-99710`--`L-99715`; PR #653 negative-mass Landau theorem  
RH status: **unproved**

The blockwise packet of `T-99711` can be sharpened once its support is centered
at the bottom of its own annulus.

For `2^L<=x<2^(L+1)`, put

\[
M=M_L,
\qquad
R_L=2^{M+3},
\qquad
N_0=x/R_L,
\]

and

\[
b_{x,L}(n)
={\beta(n)\over\sqrt n}\Phi_M(x/n).
\tag{T-99712.1}
\]

The packet is supported on `N_0<=n<=R_LN_0=x`.  Define the exact nested tail

\[
\mathcal T_{x,L}(y)
=
\sum_{n\ge yN_0}b_{x,L}(n),
\qquad1\le y\le R_L.
\tag{T-99712.2}
\]

`L-99715` with fixed Poisson width `tau=1` gives

\[
\boxed{
\mathcal P_{x,L}
=|W^{[M_L]}(x)|^2
+2\int_1^{R_L}y|\mathcal T_{x,L}(y)|^2dy.
}
\tag{T-99712.3}
\]

At the same fixed width, the logarithmic-owner square has the uniform gap

\[
\overline V_1(n)\ge|a(n)|^2.
\tag{T-99712.4}
\]

The strip and support costs are both only

\[
R_L=2^{M_L+3}=x^{o(1)}.
\tag{T-99712.5}
\]

Thus the shrinking-width loss in `T-99710/T-99711` is completely removed.

## Single remaining theorem

> **Annulus Owner-Tail Packing (`AOTP99710`).** Uniformly on dyadic blocks,
> \[
> \int_{2^L}^{2^{L+1}}
> \left(
> 2\int_1^{R_L}y|\mathcal T_{x,L}(y)|^2dy
> \right)^{1/2}{dx\over x}
> =2^{o(L)}.
> \tag{T-99712.6}
> \]

The coefficient diagonal of this tail square is already `2^(o(L))` by
`T-99711.4`.  `AOTP99710` asks only for the source-owned off-diagonal packing.

If (T-99712.6) holds, then (T-99712.3) gives subpower logarithmic negative mass
for the blockwise filtered packet.  The positive inverse of `L-99714` transfers
that estimate to the compact conclusion packet `W`.  Its zero-safe Mellin
transform from `L-99713` and the negative-part Landau theorem then imply RH.

Therefore

\[
\boxed{\mathrm{AOTP99710}\Longrightarrow\mathrm{RH}.}
\tag{T-99712.7}
\]

## Exact proof contract

The remaining tail packing is allowed to use:

```text
the unit owner spectral gap (T-99712.4);
the exact sequential first-owner Euler identity of PR #652;
the RN endpoint cocycle for nested source tents;
the M_L logarithmic moment cancellations;
the subpower annulus ratio R_L;
the exact beta/g logarithmic coefficient energy.
```

It may not use a source-blind Hardy or large-sieve inequality.  Such estimates
pay the additive spacing of integers and reintroduce a power of `x`; the owner
labels must be retained until after the tail square is packed.

## Final narrowed graph

```text
native scalar/source and analytic consumer        CLOSED
compact pole-centered packet                      PROVED
blockwise growing moment tower                     PROVED
annulus-centered fixed-width Poisson identity      PROVED
uniform owner spectral gap                         PROVED
diagonal tail energy                               SUBPOWER / PROVED
AOTP99710 off-diagonal owner-tail packing           OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVEN
```
