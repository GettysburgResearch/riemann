# L-102884 — Balanced-core gcd extraction closes the large-common-core sector

Claim ID: `L-102884`  
Status: **PROVED EXACT GCD DECOMPOSITION AND POWER-SAVING SECTOR**  
Created: 2026-08-24  
Depends on: `L-102868`; `L-102883`  
RH status: **not assumed**

Consider two distinct physical products in stopped balanced blocks,

\[
N=P c^2,
\qquad
M=Q d^2,
\]

where

\[
P=pq,
\quad Q=rs,
\quad c=uvm,
\quad d=u'v'm'.
\]

Put

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

Translation invariance therefore gives

\[
\boxed{
\langle v_N,v_M\rangle
={1\over g^2}
\langle v_{Pc_1^2},v_{Qd_1^2}\rangle.
}
\tag{L-102884.1}

The identity commutes with owner phases, the fixed outer observation and every
Euler/half-divisor/Wick gauge.

## 2. Large-gcd sector

The number of Vaughan representations of one core product is `Y^o(1)` by
`L-102883`.  Hence, for every `G>=2`, the complete free/equal-product energy of
terms with `g>=G` is bounded by

\[
\sum_{g\ge G}{\tau(g)^{O(1)}\over g^2}
\,Y^{o(1)}
\ll G^{-1+o(1)}Y^{o(1)}.
\]

Thus

\[
\boxed{
\text{the sector }g\ge Y_0^\eta
\text{ has power-saving cost for every fixed }\eta>0,
}
\tag{L-102884.2
\]

where `Y_0` is the smaller of the two local core scales.

## 3. Core-identical terms are automatically large-gcd

In a nonempty stopped balanced block,

\[
c\asymp\sqrt{Y_P},
\qquad
d\asymp\sqrt{Y_Q}.
\]

If the reduced cores satisfy `c_1=d_1=1`, then `c=d=g`.  On a fixed
ratio-eight physical shell the two local scales are comparable up to an
absolute factor. Consequently

\[
g\gg Y_0^{1/2}.
\]

Hence the core-identical sector belongs to (L-102884.2), for example with
`eta=1/4`.

## Exact scope

After removing the large-gcd sector with `G=Y_0^(1/4)`, every remaining cross
term has

```text
g<Y_0^(1/4);
(c_1,d_1)=1;
c_1 d_1>1.
```

It therefore has at least one internal core-discrepancy prime, supplying the
additional nonzero phase in `L-102885`.