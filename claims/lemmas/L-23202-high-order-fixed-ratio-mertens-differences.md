# L-23202 — High-order fixed-ratio Mertens differences retain the full RH exponent

Claim ID: `L-23202`  
Title: Every finite order of the geometric `2/3` difference is RH-equivalent, and the first Farey cell is its first rung  
Status: **PROPOSED EXACT TRANSFER LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-21`  
Created: 2026-08-07  
Issue: #232  
Dependencies: `L-23003`, `T-23002`; the classical Mertens criterion  
Scope: full RH equivalence, not an estimate

## 1. Geometric differences

Extend

\[
M(x)=\sum_{n\le x}\mu(n)
\]

by `M(x)=0` for `0<=x<1`. Put

\[
c=\frac23,
\qquad
(T_cF)(x)=F(cx),
\qquad
\Delta_c=I-T_c.
\tag{L-23202.1}
\]

For every integer `m>=1`, define

\[
G_m(x)=\Delta_c^mM(x)
=
\sum_{j=0}^{m}
(-1)^j{m\choose j}M(c^jx).
\tag{L-23202.2}
\]

## 2. Exact inversion

Because `T_c^jM(x)=0` for all sufficiently large `j`, the formal binomial
series for `(I-T_c)^(-m)` terminates pointwise. Therefore

\[
\boxed{
M(x)
=
\sum_{j=0}^{\infty}
{m+j-1\choose j}
G_m(c^jx),
}
\tag{L-23202.3}
\]

where the sum is finite for every fixed `x`.

This can also be verified by applying `(I-T_c)^m` and using the generating
identity

\[
\sum_{j\ge0}{m+j-1\choose j}z^j=(1-z)^{-m}.
\]

## 3. RH equivalence

For every fixed `m>=1`, the following are equivalent:

1. RH;
2. for every `epsilon>0`,
   \[
   G_m(x)=O_{m,\epsilon}(x^{1/2+\epsilon});
   \tag{L-23202.4}
   \]
3. 
   \[
   |G_m(x)|^2/x=x^{o(1)}.
   \tag{L-23202.5}
   \]

RH implies (L-23202.4) immediately from the classical bound for `M`.

Conversely, insert (L-23202.4) into (L-23202.3):

\[
|M(x)|
\ll_{m,\epsilon}
x^{1/2+\epsilon}
\sum_{j\ge0}
{m+j-1\choose j}
c^{j(1/2+\epsilon)}.
\]

The series converges because its coefficients grow polynomially while
`c^(1/2+epsilon)<1`. Hence

\[
M(x)=O_{m,\epsilon}(x^{1/2+\epsilon}),
\]

and the Mertens criterion gives RH.

Thus increasing the difference order does not weaken the spectral target. It
provides additional exact boundary cancellations while retaining the complete
rightmost-zero exponent.

## 4. First critical Farey cell

`L-23003` proves, for integer `D`,

\[
B_{D,1}
=
\left(\frac{i}{2\pi}+\frac1{2\pi^2}\right)
\Delta_cM(D).
\tag{L-23202.6}
\]

Thus the first positive critical Farey cell is the `m=1` member of the hierarchy.
Repeatedly applying the same geometric difference gives

\[
\Delta_c^{m-1}B_{\bullet,1}(D)
=
\left(\frac{i}{2\pi}+\frac1{2\pi^2}\right)
G_m(D),
\tag{L-23202.7}
\]

when the cell coefficient is interpreted at the corresponding real cutoff
with the usual floor convention.

Consequently any high-order packet proposal must eventually prove
(L-23202.4), either explicitly in this coordinate or through an exact
cross-route transfer.

## 5. Why this is the correct audit gate

The row-growth counterexample in `R-22802` shows that arbitrary Farey vectors
cannot satisfy a subpower critical-cluster operator bound. Equations
(L-23202.6)--(L-23202.7) explain why: the coherent first row is already an
RH-equivalent Mertens increment.

Accordingly, a valid completion must retain at least one of:

- the actual Möbius signs before divisor compression;
- an exact Selberg quadratic identity that implies the same difference bound;
- a source-specific terminal packet recurrence whose output controls `G_m`;
- an independently verified RH-equivalent scalar of equal strength.

A generic large sieve, deletion of low cells, or a finite positive ladder is
not a substitute.

## 6. Proof boundary

This lemma proves the equivalence and exact inversion. It supplies no estimate
for `G_m`. The square-root bound remains the RH-bearing arithmetic theorem.
