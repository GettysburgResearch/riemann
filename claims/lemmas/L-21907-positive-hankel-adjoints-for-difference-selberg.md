# L-21907 — Explicit positive-Hankel adjoints for the difference-squared Selberg equation

Claim ID: `L-21907`  
Title: Every real exponential has a closed completely monotone adjoint for the square-preserving first-difference Selberg operator  
Status: **PROPOSED — COMPLETE ELEMENTARY ADJOINT AND ENERGY IDENTITY; COMPLEX/TYPE-II ESTIMATE OPEN**  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Dependencies: `L-21906`; elementary Laplace-density calculus  
Scope: positive dual cone for the differenced centered-prime measure

## 1. Operator

Retain

\[
 \mathscr L_h
 =\mathscr L\Delta_h+2h\tau_h
 \tag{L-21907.1}
\]

and

\[
 \mathscr L_h^*
 =(I-\tau_h^*)\mathscr L^*+2h\tau_h^*.
 \tag{L-21907.2}
\]

The differenced centered measure

\[
 \mu_h=\Delta_h\nu
\]

satisfies

\[
 \mathscr L_h\mu_h+\mu_h*\mu_h=\Delta_h^2R.
 \tag{L-21907.3}
\]

## 2. Positive spectral density

Fix

\[
 h>0,
 \qquad
 s>{1\over2}.
\]

For `u>=s`, define

\[
 \boxed{
 m_{h,s}(u)
 =
 { (1-e^{-hs})(s-1/2)^2
  \over
   (1-e^{-hu})^2(u-1/2)^2}.
 }
 \tag{L-21907.4}
\]

This density is positive and integrable.  Its boundary value is

\[
 m_{h,s}(s)={1\over1-e^{-hs}}.
 \tag{L-21907.5}
\]

Moreover

\[
 \boxed{
 {m_{h,s}'(u)\over m_{h,s}(u)}
 =-{2\over u-1/2}
  -{2h\over e^{hu}-1}.
 }
 \tag{L-21907.6}
\]

Put

\[
 \boxed{
 f_{h,s}(y)
 =\int_s^\infty m_{h,s}(u)e^{-uy}du.
 }
 \tag{L-21907.7}
\]

Then `f_(h,s)` is completely monotone, and

\[
 f_{h,s}(x+y)
 =\int_s^\infty
  [m_{h,s}(u)^{1/2}e^{-ux}]
  [m_{h,s}(u)^{1/2}e^{-uy}]du
 \tag{L-21907.8}
\]

is a positive Hankel kernel.

## 3. Exact adjoint identity

For a general positive density `m` supported on `[s,infinity)`, integration by
parts shows that the Laplace density of `mathscr L_h^*f` is

\[
 \begin{aligned}
 &(1-e^{-hu})m'(u)\\
 &\quad+
 \left[
  {2(1-e^{-hu})\over u-1/2}
  +2he^{-hu}
 \right]m(u),
 \end{aligned}
 \tag{L-21907.9}
\]

plus the boundary atom

\[
 (1-e^{-hs})m(s)\,\delta_s.
 \tag{L-21907.10}
\]

Equations (L-21907.5)--(L-21907.6) make the continuous density vanish
identically and normalize the boundary atom to one.  Therefore

\[
 \boxed{
 \mathscr L_h^*f_{h,s}=e^{-s\,\cdot}.
 }
 \tag{L-21907.11}
\]

This is the exact differenced analogue of `L-21905`.

As `h` tends to infinity, the factor `(1-e^{-hu})` tends to one and
(L-21907.4) reduces to the undifferenced density of `L-21905`.

## 4. Exact positive energy identity

Let

\[
 M_h(s)=\langle\mu_h,e^{-s\,\cdot}\rangle
 =(1-e^{-hs})H(s),
 \tag{L-21907.12}
\]

and

\[
 \mathcal R_h(s)
 =\langle\Delta_h^2R,e^{-s\,\cdot}\rangle
 =(1-e^{-hs})^2\mathcal R(s).
 \tag{L-21907.13}
\]

Pair (L-21907.3) with `f_(h,s)`.  Fubini and the positive representation
(L-21907.8) give

\[
 \boxed{
 M_h(s)
 +\int_s^\infty m_{h,s}(u)M_h(u)^2du
 =\int_s^\infty m_{h,s}(u)\mathcal R_h(u)du.
 }
 \tag{L-21907.14}
\]

The quadratic prime channel is a literal nonnegative square.  In particular,

\[
 \boxed{
 M_h(s)
 \le
 \int_s^\infty m_{h,s}(u)\mathcal R_h(u)du.
 }
 \tag{L-21907.15}
\]

## 5. Positive mixtures

For any finite positive matrix measure `Lambda` on `(1/2,infinity)`, define

\[
 F_{h,\Lambda}(y)
 =\int f_{h,s}(y)d\Lambda(s).
 \tag{L-21907.16}
\]

Its matrix Hankel kernel is positive and

\[
 \boxed{
 \mathscr L_h^*F_{h,\Lambda}
 =\int e^{-sy}d\Lambda(s).
 }
 \tag{L-21907.17}
\]

Thus the square-preserving differenced equation has the same complete positive
real-exponential test cone as the original equation, but without the
undifferenced ramp in its nonlinear variable.

## 6. Exact remaining limitation

The identity controls the real Laplace transform `M_h(s)`.  It does not by
itself control

\[
 M_h(\sigma+it)
\]

uniformly on vertical lines, nor does it represent an arbitrary compact signed
prime window by a positive exponential mixture.  The latter obstruction is
visible in `R-21903`: positive Hankel adjoints retain a real-exponential shape
constraint.

A full RH proof from (L-21907.14) still needs one of:

1. a conditionally positive adjoint for the actual finite-difference spline,
   with every annihilated moment verified;
2. a signed Type-II factorization converting the remaining ratio channel into
   a nonnegative square;
3. a theorem promoting the real family (L-21907.14) to the required vertical
   Hardy or all-order Stieltjes positivity.

These are the exact remaining arithmetic/analytic gates.  They are not supplied
by the positive exponential cone alone.

## 7. Proof boundary

- The density, adjoint identity, positive kernel, and energy equation are exact.
- No RH assumption is used.
- The result strengthens the available Selberg algebra but does not prove the
  prime-only energy estimate or RH.
