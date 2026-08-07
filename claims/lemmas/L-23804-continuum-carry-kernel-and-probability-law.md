# L-23804 — Exact continuum carry kernel and probability law

Claim ID: `L-23804`  
Title: The continuum carry kernel has one closed zeta Mellin transform and one explicit harmonic-interval probability law  
Status: **PROPOSED EXACT LEMMA — COMPLETE ELEMENTARY PROOF**  
Authoring agent: `gpt56-pro-09-u`  
Created: 2026-08-07  
Issue: #238  
Dependencies: `L-23801` only for motivation; the proof below is independent  
Scope: exact continuum model behind the finite carry packing

## 1. The carry kernel

For `x>=1`, write

\[
 m=\lfloor x\rfloor
\]

and define the right-continuous carry kernel

\[
 \boxed{
 K(x)={m(m+1-x)\over x},
 \qquad m\le x<m+1.}
 \tag{L-23804.1}
\]

At an integer `m`, this convention gives `K(m)=1`. On every open unit interval
`K` decreases strictly from `1` to `0`.

The finite carry coefficient has the exact endpoint representation

\[
 \boxed{
 \beta_{nq}=K_-\!\left({n+1\over q}\right),}
 \tag{L-23804.2}
\]

where `K_-` is the left-continuous version of `K` at the integers. Indeed, if
`n=kq+r`, `0<=r<q`, and `r<=q-2`, then

\[
 K\!\left({n+1\over q}\right)
 ={k(q-r-1)\over n+1}=\beta_{nq},
\]

whereas `r=q-1` gives both sides equal to zero after taking the left limit.

Moreover, for every real `y in [n,n+1]`,

\[
 \boxed{
 \beta_{nq}\le K(y/q).}
 \tag{L-23804.3}
\]

There is no interior jump because the interval has length one and `q>=2`; the
right endpoint is the minimum on that cell.

## 2. Exact Mellin transform

For `Re s>0`,

\[
 \boxed{
 \int_1^\infty K(x)x^{-s-2}\,dx
 ={s\,\zeta(s+1)\over(s+1)(s+2)}.}
 \tag{L-23804.4}
\]

### Proof

On `[m,m+1]`,

\[
 K(x)x^{-s-2}
 =m(m+1)x^{-s-3}-mx^{-s-2}.
\]

Summing the two elementary antiderivatives gives

\[
 {1\over s+2}
 \sum_{m\ge1}
 \left[(m+1)m^{-s-1}-m(m+1)^{-s-1}\right]
 -{1\over s+1}
 \sum_{m\ge1}
 \left[m^{-s}-m(m+1)^{-s-1}\right].
\]

The first sum is `2 zeta(s+1)` and the second is `zeta(s+1)`. This yields
(L-23804.4). QED.

At `s=0`, continuity gives the sharp carry-mass identity

\[
 \boxed{
 \int_1^\infty K(x)x^{-2}\,dx={1\over2}.}
 \tag{L-23804.5}
\]

This is the source of the exact archimedean constant `4` in the full proposal.

## 3. A probability density

Put

\[
 \boxed{
 p(t)=2e^{-t}K(e^t),
 \qquad t\ge0.}
 \tag{L-23804.6}
\]

Equation (L-23804.5) says that `p` is a probability density. Its Laplace
transform is

\[
 \boxed{
 P(s)=\int_0^\infty e^{-st}p(t)dt
 ={2s\zeta(s+1)\over(s+1)(s+2)},
 \qquad \Re s>0,}
 \tag{L-23804.7}
\]

with `P(0)=1` by continuity.

## 4. Explicit random-variable construction

The mass of the logarithmic interval `[log m,log(m+1)]` is exactly

\[
 \boxed{
 \int_{\log m}^{\log(m+1)}p(t)dt={1\over m(m+1)}.}
 \tag{L-23804.8}
\]

Thus let `M` have the harmonic-interval law

\[
 \mathbb P(M=m)={1\over m(m+1)},
 \qquad m=1,2,\ldots,
 \tag{L-23804.9}
\]

and let `V`, independent of `M`, have the beta density

\[
 2v\,\mathbf 1_{0<v<1}\,dv.
 \tag{L-23804.10}
\]

Define

\[
 \boxed{
 X={M(M+1)\over M+V},
 \qquad T=\log X.}
 \tag{L-23804.11}
\]

A change of variables gives the conditional density

\[
 f_{X|M=m}(x)
 =2m^2(m+1){m+1-x\over x^3},
 \qquad m<x<m+1.
\]

After multiplication by (L-23804.9), the unconditional logarithmic density is
exactly (L-23804.6). Hence

\[
 \boxed{T\text{ has Laplace transform }P(s).}
 \tag{L-23804.12}
\]

Equivalently, if `U` is uniform on `(0,1)`, then
`M=floor(1/U)` has the required law. The carry distribution is therefore an
explicit elementary random variable, not a formal inverse transform.

## 5. Proof boundary

Closed exactly:

- the continuum kernel;
- its relation to every finite carry coefficient;
- the Mellin transform and mass `1/2`;
- the explicit harmonic-interval/Beta probability law.

No RH statement and no positivity of the inverse carry profile are asserted in
this lemma.
