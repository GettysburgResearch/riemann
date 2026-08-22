# L-102707 — Continuous half-divisor geodesic and polarized Hankel current

Claim ID: `L-102707`  
Status: **PROVED EXACT SOURCE/KERNEL IDENTITY**  
Created: 2026-08-22  
Depends on: `L-102701`; `L-102706`  
RH status: **not assumed**

Use the local half-divisor path

\[
\ell_\tau(x)
=\tau\sqrt{1-x}+(1-\tau)\sqrt{1-x^2},
\qquad 0\le\tau\le1.
\]

For all labelled primes, including the second `67`, define the arithmetic
source

\[
\Lambda_\tau=\prod_p \ell_\tau(p^{-1/2}U_p).
\]

Then

\[
\Lambda_0=\lambda^\square,
\qquad
\Lambda_1=\lambda,
\]

and

\[
\Lambda_\tau*\Lambda_\tau
=\prod_p h_\tau(p^{-1/2}U_p).
\]

## 1. Root-free tangent

The local tangent is

\[
\dot\ell_\tau(x)
=\sqrt{1-x}-\sqrt{1-x^2}.
\]

It is independent of `tau` and satisfies

\[
\boxed{\dot\ell_\tau(0)=0.}
\tag{L-102707.1}
\]

Hence the global tangent

\[
\dot\Lambda_\tau=\frac{d}{d\tau}\Lambda_\tau
\]

has no unit/root coordinate.

Differentiating the arithmetic convolution square gives

\[
\boxed{
\frac d{d\tau}(\Lambda_\tau*\Lambda_\tau)
=2\dot\Lambda_\tau*\Lambda_\tau.
}
\tag{L-102707.2}
\]

Integrating from `0` to `1` recovers the completion defect:

\[
\boxed{
\beta-\beta^\square
=2\int_0^1\dot\Lambda_\tau*\Lambda_\tau\,d\tau.
}
\tag{L-102707.3}
\]

## 2. Positive ratio-four spline and current

Let `A` be the positive ratio-four spline of PR #696 and put

\[
B=A*_M A.
\]

PR #719 gives

\[
\boxed{\Phi_*=(2D-1)B.}
\tag{L-102707.4}
\]

Define the two fields

\[
G_\tau(Y)
=\sum_n\frac{\Lambda_\tau(n)}{\sqrt n}A(Y/n),
\]

\[
\dot G_\tau(Y)
=\sum_n\frac{\dot\Lambda_\tau(n)}{\sqrt n}A(Y/n).
\]

Finite arithmetic and Mellin Fubini yield

\[
\boxed{
H_{\rm def}(X)
=(2D-1)
\int_0^1
2\int_0^\infty
\dot G_\tau(Y)G_\tau(X/Y)\frac{dY}{Y}
\,d\tau.
}
\tag{L-102707.5}
\]

This is a continuous polarized Hankel current.  Its left field is root-free at
every `tau`; the right field carries the unique unit coordinate.

## 3. Gauge compatibility

By `L-102706`, the squared source

\[
\Lambda_\tau*\Lambda_\tau
\]

is related to the Euler completion path by a multiplier whose local expansion
starts at `p^(-1)`.  Therefore the owner/transfer cancellation of PR #718 and
the polarized half-divisor current above are the same defect in two
polylogarithmically equivalent gauges.

This closes the source-typing interface between the stress-tensor route and the
ratio-four half-divisor route.

## Boundary

Equation (L-102707.5) does not orient the signed Hankel current.  Any estimate
must keep the `tau` integral, the root-free tangent, and the companion field
attached until after carrier recombination.