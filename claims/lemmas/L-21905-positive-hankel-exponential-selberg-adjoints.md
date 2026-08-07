# L-21905 — Explicit positive-Hankel adjoints for the centered Selberg equation

Claim ID: `L-21905`  
Title: Every exponential test has a closed completely monotone Selberg adjoint and an exact positive-square energy identity  
Status: **PROPOSED — COMPLETE ELEMENTARY ADJOINT/ENERGY IDENTITY; STOP-LOSS SYNTHESIS SEPARATE**  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Dependencies: the centered Selberg Riccati identity of PR #216; `L-20213`; elementary Laplace/Hankel calculus  
Scope: positive dual cone for the prime-polygon and Haar/dilation routes

## 1. Centered Selberg equation

Use the shared additive-logarithmic normalization

\[
 dP(y)=\sum_{n\ge2}{\Lambda(n)\over\sqrt n}\,
       \delta_{\log n}(dy),
 \qquad
 dP_0(y)=e^{y/2}{\bf1}_{y\ge0}\,dy,
 \tag{L-21905.1}
\]

and put

\[
 d\nu=dP-dP_0.
 \tag{L-21905.2}
\]

Selberg's coefficient identity gives the exact distributional equation

\[
 \boxed{
 \mathscr L\nu+\nu*\nu=R,
 }
 \tag{L-21905.3}
\]

where

\[
 \mathscr L\nu=y\,d\nu+2dP_0*d\nu.
 \tag{L-21905.4}
\]

For a sufficiently decaying test `f`, the adjoint is

\[
 \boxed{
 (\mathscr L^*f)(y)
 =y f(y)+2\int_0^\infty f(x+y)e^{x/2}\,dx.
 }
 \tag{L-21905.5}
\]

Pairing (L-21905.3) with `f` gives

\[
 \langle\nu,\mathscr L^*f\rangle
 +\iint f(x+y)\,d\nu(x)d\nu(y)
 =\langle R,f\rangle.
 \tag{L-21905.6}
\]

## 2. Closed adjoint for one exponential

Fix

\[
 s>{1\over2}
 \]

and define the positive density

\[
 \boxed{
 m_s(u)=
 \left({s-1/2\over u-1/2}\right)^2
 {\bf1}_{[s,\infty)}(u).
 }
 \tag{L-21905.7}
\]

Put

\[
 \boxed{
 f_s(y)=\int_s^\infty m_s(u)e^{-uy}\,du.
 }
 \tag{L-21905.8}
\]

Then `f_s` is completely monotone and its Hankel kernel is positive
semidefinite:

\[
 \boxed{
 f_s(x+y)
 =\int_s^\infty
  [m_s(u)^{1/2}e^{-ux}]
  [m_s(u)^{1/2}e^{-uy}]\,du.
 }
 \tag{L-21905.9}
\]

The density obeys

\[
 m_s(s)=1,
 \qquad
 m_s'(u)+{2m_s(u)\over u-1/2}=0.
 \tag{L-21905.10}
\]

Using `y e^{-uy}=-partial_u e^{-uy}` and integrating by parts,

\[
\begin{aligned}
 y f_s(y)
 &=e^{-sy}
   +\int_s^\infty m_s'(u)e^{-uy}du,\\
 2\int_0^\infty f_s(x+y)e^{x/2}dx
 &=2\int_s^\infty {m_s(u)\over u-1/2}e^{-uy}du.
\end{aligned}
 \tag{L-21905.11}
\]

Equation (L-21905.10) cancels the remaining integrals and gives the exact
identity

\[
 \boxed{
 \mathscr L^*f_s=e^{-s\,\cdot}.
 }
 \tag{L-21905.12}
\]

Thus the positive-Hankel adjoint required abstractly in `L-20213` exists in
closed form for every exponential test.

## 3. Exact nonlinear energy identity

Define the real Laplace transforms

\[
 H(s)=\langle\nu,e^{-s\,\cdot}\rangle,
 \qquad
 \mathcal R(s)=\langle R,e^{-s\,\cdot}\rangle.
 \tag{L-21905.13}
\]

Substituting `f_s` into (L-21905.6), applying Fubini, and using
(L-21905.9) gives

\[
 \boxed{
 H(s)
 +\int_s^\infty m_s(u)H(u)^2du
 =\int_s^\infty m_s(u)\mathcal R(u)du.
 }
 \tag{L-21905.14}
\]

In the zeta normalization,

\[
 H(s)
 =-{\zeta'\over\zeta}\left(s+{1\over2}\right)
  -{1\over s-1/2},
 \tag{L-21905.15}
\]

and (L-21905.14) is the integrated Riccati equation with the quadratic prime
channel retained as a literal nonnegative square.

In particular,

\[
 \boxed{
 H(s)
 \le\int_s^\infty m_s(u)\mathcal R(u)du.
 }
 \tag{L-21905.16}
\]

No absolute value of the prime-pair term occurs.

## 4. Positive mixtures

Let `lambda` be any finite positive measure supported in `(1/2,infinity)` and
put

\[
 k_\lambda(y)=\int e^{-sy}\,d\lambda(s),
 \qquad
 f_\lambda(y)=\int f_s(y)\,d\lambda(s).
 \tag{L-21905.17}
\]

Then

\[
 \boxed{
 \mathscr L^*f_\lambda=k_\lambda,
 }
 \tag{L-21905.18}
\]

and `f_lambda(x+y)` is positive semidefinite.  Hence

\[
 \boxed{
 \langle\nu,k_\lambda\rangle
 \le\langle R,f_\lambda\rangle.
 }
 \tag{L-21905.19}
\]

This is a dimension-free positive dual cone.  Finite positive quadrature gives
proof-producing rational/exponential certificates after the transcendental
inputs are directed.

## 5. Relationship to the polygon and Haar routes

The polygon/Haar arithmetic rows use stop-loss functions

\[
 k_T(y)=(T-y)_+.
 \tag{L-21905.20}
\]

They are not globally completely monotone, so (L-21905.19) does not by itself
settle their sign.  The remaining constructive question is now sharply typed:
find, for every required row, a decomposition

\[
 \boxed{
 k_T=k_\lambda+\mathscr L^*g_T+e_T
 }
 \tag{L-21905.21}
\]

such that

1. `lambda>=0` and the Hankel kernel of `g_T` is positive semidefinite;
2. the exact Selberg residual pairings of `f_lambda+g_T` pay the
   archimedean/transport threshold;
3. `e_T` has a one-sided `exp(o(T))` pairing with the centered prime measure.

The curvature-corrected dyadic route of PR #218 supplies a natural square term
for `g_T`; the prime-polygon route supplies the transport reserve.  Equation
(L-21905.14) supplies the previously missing exact positive exponential
resolvent.

## 6. Proof boundary

- The formula for `f_s`, its complete monotonicity, the adjoint identity, and
  the nonlinear energy identity are elementary and exact.
- The normalization of `R` must be shared with the chosen Selberg identity
  before composition.
- A positive exponential adjoint does not automatically synthesize the compact
  stop-loss kernel.
- The decomposition (L-21905.21) and its cofinal residual bound remain the
  arithmetic review hinge.
- No RH conclusion is claimed by this lemma alone.
