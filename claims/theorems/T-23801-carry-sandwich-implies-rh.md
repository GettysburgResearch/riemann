# T-23801 — A sharp nonnegative carry sandwich implies RH

Claim ID: `T-23801`  
Title: Two finite nonnegative carry certificates enclosing the prime ramp within subpolynomial error force the zero-free critical half-plane  
Status: **PROPOSED COMPLETE COMPOSITION THEOREM PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-07  
Issue: #238  
Dependencies: `L-23801`, `L-23802`; elementary Laplace continuation  
Scope: exact finite-to-global deduction; the carry sandwich itself remains proposed

## 1. Carry Sandwich theorem

For every integer `X>=2`, let `mathfrak L(X)` and `mathfrak U(X)` be the finite
packing and covering values of `L-23802`.

The load-bearing finite assertion is

\[
\boxed{
4\sqrt X-X^{o(1)}
\le\mathfrak L(X)
\le\mathfrak U(X)
\le4\sqrt X+X^{o(1)}.}
\tag{T-23801.1}
\]

Equivalently, for every `epsilon>0`, there are nonnegative finite vectors
`d_X,e_X` satisfying

\[
B_X^Td_X\le w_X\le B_X^Te_X
\tag{T-23801.2}
\]

and

\[
\sum_n d_X(n)G_n
\ge4\sqrt X-C_\epsilon X^\epsilon,
\qquad
\sum_n e_X(n)G_n
\le4\sqrt X+C_\epsilon X^\epsilon.
\tag{T-23801.3}
\]

This theorem is strictly weaker than exact Carry Saturation: the lower and upper
certificates may be different, and neither need solve the triangular equations
with equality.

## 2. Prime-ramp consequence

By `L-23801/L-23802`,

\[
\mathfrak L(X)
\le\mathcal P(X)
\le\mathfrak U(X),
\]

where

\[
\mathcal P(X)
=\sum_{q=p^a\le X}
 {\Lambda(q)\over\sqrt q}\log{X\over q}.
\]

Hence (T-23801.1) gives

\[
\boxed{
\mathcal P(X)=4\sqrt X+X^{o(1)}.}
\tag{T-23801.4}
\]

No zero ordinate, explicit formula, or prime asymptotic is used in deriving
(T-23801.4) from the finite carry certificates.

## 3. Continuous interpolation

For noninteger `X`, use the same finite sum with `q<=X`. Between consecutive
prime-power knots,

\[
\mathcal P'(X)
={1\over X}\sum_{q\le X}{\Lambda(q)\over\sqrt q}.
\tag{T-23801.5}
\]

The elementary bound `Lambda(q)<=log q` gives

\[
|\mathcal P'(X)|\ll {\log X\over\sqrt X}.
\tag{T-23801.6}
\]

Thus the integer estimate (T-23801.4) extends to every real `X>=2` with the same
subpolynomial error.

## 4. Laplace transform

Put `X=e^x` and define

\[
A(x)=\mathcal P(e^x)-4e^{x/2}.
\tag{T-23801.7}
\]

Equation (T-23801.4) says

\[
A(x)=e^{o(x)}.
\tag{T-23801.8}
\]

For `Re z>1/2`, absolute convergence and one elementary integration give

\[
\begin{aligned}
\int_0^\infty\mathcal P(e^x)e^{-zx}dx
&=\sum_{n\ge2}{\Lambda(n)\over\sqrt n}
  \int_{\log n}^{\infty}(x-\log n)e^{-zx}dx\\
&={-\zeta'/\zeta(z+1/2)\over z^2}.
\end{aligned}
\tag{T-23801.9}
\]

Also

\[
\int_0^\infty4e^{x/2}e^{-zx}dx
={4\over z-1/2}.
\tag{T-23801.10}
\]

The pole at `z=1/2` cancels exactly, because the residue of
`-zeta'/zeta(z+1/2)/z^2` there is `4`. Therefore

\[
\boxed{
\int_0^\infty A(x)e^{-zx}dx
={-\zeta'/\zeta(z+1/2)\over z^2}
 -{4\over z-1/2}.}
\tag{T-23801.11}
\]

By (T-23801.8), the left side converges absolutely and defines a holomorphic
function for every `Re z>0`.

## 5. Zero exclusion

If `rho` were a nontrivial zeta zero with `Re rho>1/2`, then the right side of
(T-23801.11) would have a nonremovable pole at

\[
z=\rho-1/2
\]

inside `Re z>0`. This contradicts the holomorphy supplied by the left side.
Thus zeta has no zero to the right of the critical line. The functional equation
reflects nontrivial zeros about `Re s=1/2`, so

\[
\boxed{\mathrm{RH}.}
\tag{T-23801.12}
\]

## 6. Weaker one-sided alternatives

A reviewer may replace the two-sided sandwich by either of the following,
provided the missing opposite side is supplied independently:

1. exact Carry Saturation plus sharp signed carry-mass bounds;
2. a subpolynomial weighted negative part of the exact inverse together with a
   matching packing certificate;
3. a direct proof of (T-23801.4).

The two-sided nonnegative sandwich is preferred because every inequality is
finite and monotone under `Lambda>=0`.

## 7. Proof boundary

The deduction

\[
\text{Carry Sandwich}\Longrightarrow\text{prime ramp}\Longrightarrow\mathrm{RH}
\]

is complete. The finite carry sandwich (T-23801.1) is not proved here.