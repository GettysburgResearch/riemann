# L-102104 — The two filtered bridge kernels are differential coordinates of one positive five-box spline

Claim ID: `L-102104`  
Status: **PROVED EXACT POSITIVE-SPLINE FACTORIZATION**  
Created: 2026-08-21  
Depends on: `L-102103`; PR #697  
RH status: **not assumed**

Write `h=log 2` and use logarithmic coordinate `u=log X`. Define

\[
b_0(u)=\mathbf1_{[0,h]}(u),
\qquad
b_{1/2}(u)=e^{u/2}\mathbf1_{[0,h]}(u).
\]

Their Laplace transforms are

\[
\widehat b_0(s)={1-2^{-s}\over s},
\qquad
\widehat b_{1/2}(s)={1-\sqrt2\,2^{-s}\over s-1/2}.
\]

Put

\[
\boxed{B=b_0^{*3}*b_{1/2}^{*2}.}
\tag{L-102104.1}
\]

Then `B>=0`, `supp(B) subset [0,5 log2]`, and

\[
\widehat B(s)=\left({1-2^{-s}\over s}\right)^3\left({1-\sqrt2\,2^{-s}\over s-1/2}\right)^2.
\tag{L-102104.2}
\]

Let `D=d/du=X d/dX`. The filtered source-atom kernels are exactly

\[
\boxed{K_A^\dagger=-{1\over3}D(D-1/2)^2B,}
\tag{L-102104.3}
\]

\[
\boxed{K_Q^\dagger={1\over6}(D-1/2)(2D^2+5D+9)B.}
\tag{L-102104.4}
\]

Their sum is

\[
\boxed{K_G^\dagger={1\over4}(2D-1)(2D+3)B.}
\tag{L-102104.5}
\]

Indeed, division of the filtered activation multiplier by `Bhat` leaves `-(1/3)s(s-1/2)^2`; division of the filtered quadratic multiplier leaves `(1/6)(s-1/2)(2s^2+5s+9)`. Their sum is `(1/4)(2s-1)(2s+3)`.

Thus the two middle estimates are two fixed differential coordinates of a single positive compact carrier. The unresolved arithmetic is the signed source field feeding this spline, not a kernel or normalization mismatch.
