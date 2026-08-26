# L-102860 — Balanced cross-side phases after common-factor extraction

Claim ID: `L-102860`  
Status: **PROVED EXACT SOURCE/PHASE IDENTITY**  
Created: 2026-08-24  
Depends on: `L-102831`, `L-102838`  
RH status: **not assumed**

Work in the four-distinct-owner sector. Write

\[
N=pq\,a^2,
\qquad
M=rs\,b^2,
\]

with

\[
p>q>P^+(a),
\qquad
r>s>P^+(b),
\]

and with the four owner primes physically distinct. Choose one owner from each
side, namely `p` from `N` and `r` from `M`.

The opposite square core may contain one of these primes, but only to even
valuation. Put

\[
c_p=\min\{v_p(N),v_p(M)\},
\qquad
c_r=\min\{v_r(N),v_r(M)\},
\]

and

\[
d=p^{c_p}r^{c_r},
\qquad
\widetilde N=N/d,
\qquad
\widetilde M=M/d.
\]

Because `p` and `r` are unsquared owners on their own sides and have even
valuation on the opposite side,

\[
\boxed{
 p\mid\widetilde N\Longleftrightarrow p\nmid\widetilde M,
 \qquad
 r\mid\widetilde M\Longleftrightarrow r\nmid\widetilde N.
}
\tag{L-102860.1}
\]

The orientation may reverse when an owner occurs in the opposite square core,
but exactly one reduced product is divisible by each selected prime.

## 1. Exact common-shift extraction

For the one-product vector

\[
v_n(u)=n^{-1/2}\phi(u-\log n),
\]

one has

\[
v_N=d^{-1/2}U_dv_{\widetilde N},
\qquad
v_M=d^{-1/2}U_dv_{\widetilde M}.
\]

Translation invariance of the fixed logarithmic observation gives

\[
\boxed{
\langle v_N,v_M\rangle
=d^{-1}\langle v_{\widetilde N},v_{\widetilde M}\rangle.
}
\tag{L-102860.2}
\]

Thus extracting a common owner power is source-exact and contributes the
helpful subcritical factor `1/d`.

## 2. One nonzero phase from each physical side

For `e_ell(x)=exp(2 pi i x/ell)`, (L-102860.1) gives

\[
\sum_{h=1}^{p-1}e_p(h(\widetilde N-\widetilde M))=-1,
\]

and

\[
\sum_{k=1}^{r-1}e_r(k(\widetilde N-\widetilde M))=-1.
\]

Multiplying,

\[
\boxed{
1=
\sum_{h=1}^{p-1}\sum_{k=1}^{r-1}
 e_p(h(\widetilde N-\widetilde M))
 e_r(k(\widetilde N-\widetilde M)).
}
\tag{L-102860.3}
\]

The two moduli now come from opposite physical products. Both principal
frequencies are absent, even in the nested-owner configurations where the two
largest of all four owners lie on the same side.

## Scope

This theorem strengthens `L-102838` by balancing the two phase directions
across the two physical fields. It is an exact identity, not an estimate. The
phase-cardinality/owner-weight cancellation is proved in `L-102861`.