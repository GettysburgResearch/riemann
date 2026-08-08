# L-27605 — Exact annulus Mellin and dyadic factorization

Claim ID: `L-27605`  
Title: The prime-annulus window is an exact stable two-step dyadic difference of one elementary parabolic kernel  
Status: **PROPOSED COMPLETE EXACT ALGEBRA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-08`  
Created: 2026-08-08  
Dependencies: `L-27601`--`L-27604`  
Scope: exact window/filter algebra and exponent-preserving transfer; no prime-annulus energy estimate and no RH conclusion

## 1. The finite annulus window

Put

\[
W(u)=
\begin{cases}
2u-1,&1/2<u\le1,\\[1mm]
1/2-4u,&1/4<u\le1/2,\\[1mm]
0,&\text{otherwise}.
\end{cases}
\tag{L-27605.1}
\]

Then the prime-annulus statistic of `T-27601` is

\[
\mathfrak P(X)=X^{-1/2}\sum_{q\le X}\Lambda(q)W(q/X).
\tag{L-27605.2}
\]

The endpoints may be assigned by the conventions of `T-27601`; their individual weights agree with the displayed formulas and no asymptotic issue occurs.

## 2. Exact Mellin transform

For `Re s>0`, direct integration gives

\[
\begin{aligned}
A(s)
&:=\int_0^\infty W(u)u^{s-1}\,du\\
&=\int_{1/2}^{1}(2u-1)u^{s-1}\,du
 +\int_{1/4}^{1/2}(1/2-4u)u^{s-1}\,du.
\end{aligned}
\]

After collecting the four endpoints,

\[
\boxed{
A(s)=
\frac{(s-1)(1-2^{-s})(1-2^{-s-1})}{s(s+1)}.
}
\tag{L-27605.3}
\]

Thus, with

\[
E(s)=(1-2^{-s})(1-2^{-s-1}),
\qquad
R(s)=\frac{s-1}{s(s+1)},
\]

one has exactly

\[
\boxed{A(s)=E(s)R(s).}
\tag{L-27605.4}
\]

This is the multiplier already occurring in the pole-preserving commutator of `L-27602`. In particular, no extra factor `2^{-s}`, no factor `3`, and no unrecorded endpoint correction belongs in the raw annulus transform.

## 3. Exact physical dyadic factorization

Define

\[
r(u)=(2u-1)\mathbf1_{(0,1]}(u)
\tag{L-27605.5}
\]

and let

\[
(D_2f)(u)=f(2u).
\tag{L-27605.6}
\]

Then a cell-by-cell calculation gives

\[
\boxed{
W=(I-D_2)(I-\tfrac12D_2)r.
}
\tag{L-27605.7}
\]

Indeed, expansion gives

\[
W=r-\frac32D_2r+\frac12D_2^2r,
\tag{L-27605.8}
\]

which equals `2u-1` on `(1/2,1]`, equals `1/2-4u` on `(1/4,1/2]`, and vanishes below `1/4` by exact cancellation.

The Mellin transform of `r` is

\[
\int_0^1(2u-1)u^{s-1}du
=\frac{s-1}{s(s+1)},
\]

while `D_2` multiplies Mellin transforms by `2^{-s}`. This independently reproduces (L-27605.3).

## 4. Stable scalar filter

Define the unfiltered parabolic prime statistic

\[
\mathfrak Q(X)
=X^{-1/2}\sum_{q\le X}\Lambda(q)r(q/X).
\tag{L-27605.9}
\]

Scaling (L-27605.8) gives the exact finite identity

\[
\boxed{
\mathfrak P(X)
=\mathfrak Q(X)
-\frac{3}{2\sqrt2}\mathfrak Q(X/2)
+\frac14\mathfrak Q(X/4),
}
\tag{L-27605.10}
\]

with the usual floor convention at noninteger endpoints.

The shift polynomial factors as

\[
\boxed{
1-\frac{3}{2\sqrt2}z+\frac14z^2
=(1-2^{-1/2}z)(1-2^{-3/2}z).
}
\tag{L-27605.11}
\]

Both roots of the inverse recursion have modulus strictly below one. Hence the inverse filter has nonnegative absolutely summable coefficients. Consequently `mathfrak P` and `mathfrak Q` have the same polynomial growth exponent and the same subpower status.

This is a stable source transfer, not an estimate of either statistic.

## 5. Chebyshev–parabolic form

Let

\[
\psi(X)=\sum_{q\le X}\Lambda(q),
\qquad
B(X)=\sum_{q\le X}q\Lambda(q).
\]

Then

\[
\boxed{
\sqrt X\,\mathfrak Q(X)
=\frac{2B(X)}X-\psi(X).
}
\tag{L-27605.12}
\]

Stieltjes summation gives equivalently

\[
\boxed{
\frac{2B(X)}X-\psi(X)
=\psi(X)-\frac2X\int_{1^-}^{X}\psi(t)\,dt,
}
\tag{L-27605.13}
\]

with the endpoint convention encoded in the Stieltjes integral.

Combining (L-27605.10) and (L-27605.12) yields the exact dyadic parabolic representation of the prime-annulus statistic.

## 6. Proof boundary

Closed exactly:

1. the Mellin transform of the two-band annulus;
2. the physical two-step dyadic factorization;
3. the stable finite scalar filter;
4. equality of polynomial growth exponents;
5. the Chebyshev/parabolic representation.

Not closed:

1. a subpower pointwise or local-energy bound;
2. a Weil-positive upper estimate;
3. `PAE`;
4. RH.
