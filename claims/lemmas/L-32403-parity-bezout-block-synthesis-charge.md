# L-32403 — Exact dyadic-block charge for the parity Bézout synthesis

Claim ID: `L-32403`  
Title: Finite parity reconstruction routes one unfiltered block through only four predecessor blocks with normalized synthesis charge below `4/15` of the analysis reserve  
Status: **PROPOSED COMPLETE FINITE-BLOCK LEMMA**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #263 `L-26206`; `L-32402`  
Scope: exact block routing of the finite source synthesis; no Selberg upper estimate is asserted

## 1. Vertical and physical normalizations

Let `L=log 2`, fix `sigma>=1/2`, and write

\[
r=2^{-\sigma}\le2^{-1/2}.
\]

Retain

\[
U(z)=\sum_{j=0}^3u_jz^j
\]

from `L-26206`, with all `u_j>0`.  If `B_+(sigma+it)` and `B_-(sigma+it)` are the two parity-filtered vertical signals, exact Bézout reconstruction is

\[
O(\sigma+it)
=U(2^{-\sigma-it})B_+(\sigma+it)
 +U(-2^{-\sigma-it})B_-(\sigma+it).
\tag{L-32403.1}
\]

Let `b_+(x),b_-(x),o(x)` be the corresponding physical logarithmic signals after removing the common exponential carrier. Multiplication by `2^{-j(\sigma+it)}` is translation by `jL` with coefficient `r^j`. Thus

\[
\boxed{
 o(x)=\sum_{j=0}^3u_jr^j
 [b_+(x-jL)+(-1)^jb_-(x-jL)].
}
\tag{L-32403.2}
\]

No approximation or frequency collapse is used.

## 2. Exact block alignment

Use the dyadic blocks

\[
I_m=[mL,(m+1)L].
\]

Define

\[
E_m=\int_{I_m}(|b_+(x)|^2+|b_-(x)|^2)dx,
\qquad
O_m=\int_{I_m}|o(x)|^2dx.
\tag{L-32403.3}
\]

Every delay `jL` maps `I_m` exactly onto `I_(m-j)`. Applying Cauchy--Schwarz to the eight terms in (L-32403.2) gives

\[
\boxed{
O_m
\le q_\sigma\sum_{j=0}^3E_{m-j},
\qquad
q_\sigma=2\sum_{j=0}^3u_j^2r^{2j}.
}
\tag{L-32403.4}
\]

There is no fractional-block collar.

## 3. Uniform rational charge

Since `r<=2^(-1/2)`,

\[
q_\sigma\le q_{1/2}
=2\left[u_0^2+\frac{u_1^2}{2}
+\frac{u_2^2}{4}+\frac{u_3^2}{8}\right].
\]

Direct simplification gives

\[
\boxed{
q_{1/2}=\frac{1761-1170\sqrt2}{36}<3.
}
\tag{L-32403.5}
\]

Indeed `sqrt(2)>551/390` because `2*390^2=304200>551^2=303601`, and this lower bound implies `1170sqrt(2)>1653`.

PR #263 proves the pointwise analysis reserve

\[
|p(z)|^2+|p(-z)|^2\ge45/4
\]

on the same critical annulus. Therefore the synthesis charge, measured against that fixed analysis reserve, satisfies the exact strict ratio

\[
\boxed{
\frac{q_\sigma}{45/4}<\frac4{15}<1.
}
\tag{L-32403.6}
\]

This comparison has no arbitrary source rescaling: the analysis polynomial and Bézout synthesis are the exact fixed pair of `L-26205/L-26206`.

## 4. What this closes

The finite reconstruction itself cannot create:

- an unbounded delay family;
- a same-block fractional collar;
- a synthesis charge equal to or larger than the available parity-frame reserve.

Any physical PEFRC failure must therefore come from the Selberg/prime forcing and its source-bound cross terms, not from the finite inverse filter or block bookkeeping.

## 5. What this does not close

Equation (L-32403.6) is **not** an upper estimate for the current filtered energy `E_m`. A full proof still has to derive, from the independent-frequency reflected Selberg identity, a source-complete inequality whose return terms are exactly the synthesized predecessor blocks controlled above.

In particular, coefficientwise positivity of the Selberg forcing may not be substituted for that missing physical inequality.

## 6. Proof boundary

Closed exactly: four-block synthesis routing and strict normalized charge `<4/15`.

Open: source-coupled reflected upper estimate, strict global recurrence, RH.