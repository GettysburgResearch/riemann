# L-102884 — Exact balanced-core gcd extraction and relative large-gcd gain

Claim ID: `L-102884`  
Status: **PROVED EXACT GCD/SOURCE REDUCTION; COPRIME CROSS ESTIMATE OPEN**  
Created: 2026-08-24  
Corrected: 2026-08-24  
Depends on: `L-102868`; `L-102883`  
RH status: **not assumed**

Consider two distinct physical products in stopped balanced or smooth-boundary
blocks,

\[
N=P c^2,
\qquad
M=Q d^2,
\]

where `P` and `Q` are the external semiprime owner squareclasses. Put

\[
g=(c,d),
\qquad c=gc_1,
\qquad d=gd_1,
\qquad(c_1,d_1)=1.
\]

## 1. Exact common-square extraction

For the normalized physical vector

\[
v_n(x)=n^{-1/2}\phi(x-\log n),
\]

one has

\[
v_N=g^{-1}U_{g^2}v_{Pc_1^2},
\qquad
v_M=g^{-1}U_{g^2}v_{Qd_1^2}.
\]

Translation invariance gives

\[
\boxed{
\langle v_N,v_M\rangle
={1\over g^2}
\langle v_{Pc_1^2},v_{Qd_1^2}\rangle.
}
\tag{L-102884.1}

The identity commutes with every owner phase, fixed outer observation and
Euler/half-divisor/Wick gauge.

## 2. Relative large-gcd gain

Let `C_copr(Y;P,Q)` denote any positively homogeneous, subadditive cost for the
reduced coprime cross packet.  Representation multiplicities are `Y^o(1)` by
`L-102883`.  Therefore the contribution of common cores `g>=G` satisfies

\[
\boxed{
C_{g\ge G}(Y)
\ll Y^{o(1)}
\sum_{g\ge G}{\tau(g)^{O(1)}\over g^2}
C_{\rm copr}(Y/g^2).
}
\tag{L-102884.2}

In particular, a uniform subpower estimate for the reduced coprime packet
implies a subpower estimate for every large-gcd sector, since

\[
\sum_{g\ge1}{\tau(g)^{O(1)}\over g^{2+2\varepsilon}}<\infty.
\tag{L-102884.3}

The factor `g^-2` is an exact relative gain; it is not, by itself, a proof of
the coherent physical restriction.

## 3. Core-identical residual

If `c_1=d_1=1`, then `c=d=g`.  This term has no internal core-discrepancy
phase.  It is retained as the pure-owner coprime base packet inside the final
coherent theorem.  Equation (L-102884.2) transports its estimate through every
common square core.

If `c_1d_1>1`, the reduced coprime packet has an internal discrepancy prime and
therefore acquires the additional nonzero phase of `L-102885`.

## Exact scope

After this theorem every cross term has been reduced coefficient-exactly to one
of two coprime packets:

```text
pure-owner residual:       c_1=d_1=1;
core-discrepancy residual:  (c_1,d_1)=1 and c_1d_1>1.
```

Common-core size is no longer an independent arithmetic gate.  Both coprime
base packets remain inside the coherent owner theorem `T-102890`.