# L-99025 — Parabolic benchmark comparison and the endpoint Mellin–Landau conclusion

Claim ID: `L-99025`  
Status: **PROPOSED COMPLETE SELF-CONTAINED ENDPOINT CONSUMER**  
Created: 2026-08-18  
RH status: **conclusion of the theorem**

## 1. Elementary parabolic benchmark bound

The positive parabolic benchmark is

\[
J_\Lambda(X)=\sum_{m=2}^{\lfloor X\rfloor}
 b_X(m)\log\frac m{m-1},
\]

where

\[
b_X(t)=2\sqrt t\log\frac Xt-4\sqrt t+\frac{4t}{\sqrt X}.
\]

Put `f_X(t)=b_X(t)/t`. Direct differentiation shows that `f_X` is
nonnegative and decreasing. Therefore

\[
\sum_{m=2}^X\frac{b_X(m)}m
\le\int_1^Xf_X(t)dt
=4\sqrt X-4\log X-4X^{-1/2}.
\tag{L-99025.1}

Also

\[
\log\frac m{m-1}
\le\frac1{m-1}
=\frac1m+\frac1{m(m-1)},
\]

and `b_X(m)<=2sqrt(m)log X`. Since `m-1>=m/2` and
`sum_(m>=2)m^{-3/2}<=2`,

\[
\sum_{m=2}^X\frac{b_X(m)}{m(m-1)}\le8\log X.
\]

Combining the two bounds gives

\[
\boxed{
J_\Lambda(X)<4\sqrt X+4\log X.
}
\tag{L-99025.2}

Together with `L-99024`,

\[
\boxed{
J_\Lambda(X)-\mathcal H(d_X)
\le4\log X+C_*
=o(\log^2X).
}
\tag{L-99025.3}

## 2. Complete prime-power gap

Ordinary feasibility and `Lambda(q)>=0` imply

\[
\mathcal H(d_X)
\le
P_\Lambda(X)
=
\sum_{q\le X}\frac{\Lambda(q)}{\sqrt q}\log\frac Xq.
\]

Hence

\[
F_\Lambda(X)=J_\Lambda(X)-P_\Lambda(X)
\le J_\Lambda(X)-\mathcal H(d_X)
=o(\log^2X).
\tag{L-99025.4}

## 3. Prime-square moat

Let `A(X)` be the prime-only endpoint and let

\[
H_{\rm pp}(X)=F_\Lambda(X)-A(X)
\]

be the proper-prime-power contribution. Partial summation of the square
source, using only the classical prime number theorem, gives

\[
\boxed{
H_{\rm pp}(X)
=
\frac{-1-\zeta(1/2)}4\log^2X+o(\log^2X),
}
\tag{L-99025.5}

where `-1-zeta(1/2)>0`. Powers at least three are `o(log^2X)` by absolute
summation. Thus (L-99025.4) yields `A(X)<0` for every sufficiently large `X`.

## 4. Mellin–Landau exclusion

Finite Fubini gives the Mellin transform of `A`. Its compact numerator is
zero-free at every translated open-strip zeta zero, so a hypothetical zero
`rho` with `Re rho>1/2` produces a genuine nonreal pole on the abscissa of
convergence. Since `-A(X)` is eventually nonnegative, Landau's theorem forces
a real singularity at that abscissa. The explicit transform has no such
positive-real singularity. Hence no zero lies to the right of the critical
line; the functional equation excludes zeros to the left.

The standalone manuscript includes the finite transform calculation, the
prime-square partial summation and a proof of the Landau lemma used here. No
zero-density theorem, Mertens square-root bound, power-saving PNT error, CPBD,
or RH input is used.
