# L-105502 — Second-chaos Wick reserve pays a ninety-percent target

Claim ID: `L-105502`  
Status: **PROVED FOR THE FROZEN STATIONARY MODEL**  
Created: 2026-08-24  
Depends on: `L-105501`; Montgomery--Vaughan mean value; `L-105500`

Let

\[
f_{2,L}(t)=1+2\operatorname{Re}
\sum_{n\le e^L}\frac{a_{2,L}(n)}{n^{it}}
\tag{L-105502.1}
\]

be the Hermitian frozen symbol.  On a long interval `I=[T,2T]`, with
`e^L=T^theta` and fixed `theta<1`, Montgomery--Vaughan mean value and
`L-105501` give

\[
\frac1T\int_I f_{2,L}(t)\,dt=1+o(1)
\tag{L-105502.2}
\]

and

\[
\frac1T\int_I|f_{2,L}(t)|^2dt
=
1+2\mathcal D_{W,2}+o(1)
<\frac{501}{500}+o(1).
\tag{L-105502.3}
\]

For any `J`-dimensional source-fixed subspace with constant reproducing
diagonal, let

\[
K_{2,L,J}=P_JM_{f_{2,L}}P_J.
\]

Compression and Parseval yield

\[
\boxed{
\liminf
\frac{(\operatorname{tr}K_{2,L,J})_+^2}
{J\|K_{2,L,J}\|_{\rm HS}^2}
\ge\frac{500}{501}.
}
\tag{L-105502.4}
\]

Suppose an arithmetic Xi compression `H_T` of the same asymptotic dimension
satisfies the explicit one-percent comparison

\[
\operatorname{tr}H_T\ge\frac{99}{100}
\operatorname{tr}K_{2,L,J},
\qquad
\|H_T\|_{\rm HS}\le\frac{101}{100}
\|K_{2,L,J}\|_{\rm HS}.
\tag{L-105502.5}
\]

Then

\[
\boxed{
\eta_T
\ge
\frac{500}{501}\left(\frac{99}{101}\right)^2
=
\frac{1633500}{1703567}
=0.958870\ldots .
}
\tag{L-105502.6}
\]

Using the full-signature descent of `L-105500`, rather than the nuisance
ledger of `L-105311`, gives

\[
\boxed{
\liminf\frac{N_0(T,2T)}{N(T,2T)}
\ge
2\frac{1633500}{1703567}-1
=
\frac{1563433}{1703567}
=0.917740834\ldots .
}
\tag{L-105502.7}
\]

The exact margin above ninety percent is

\[
\frac{1563433}{1703567}-\frac9{10}
=
\frac{302227}{17035670}>0.
\tag{L-105502.8}
\]

This is a conditional Xi conclusion.  Equations (L-105502.4) and the rational
calculation are unconditional at the frozen-model scope; (L-105502.5) is not
proved here.
