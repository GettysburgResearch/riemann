# L-15449 — Terminal lattice rows are exponentially small after exact half-pole moment cancellation

Claim ID: `L-15449`  
Title: A single unrestricted large variable in a compact high-order safe window is controlled by the first Euler remainder, uniformly in the small multiplicative packet  
Status: **PROPOSED — COMPLETE ANALYTIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-07  
Dependencies: `L-15155` for the safe-window moments; elementary Euler summation for compact bounded-variation functions  
Scope: direct closure of terminal Type-I rows; no Type-II estimate

## 1. Window and moment hypotheses

Let `W` be real or complex valued, compactly supported in

\[
[u_-,u_+],
\]

continuous, piecewise `C^1`, zero at the two support endpoints, and with

\[
W'\in L^1.
\]

Fix an integer `R>=0` and assume the half-pole moments vanish:

\[
\boxed{
\int_{\mathbb R}u^r e^{-u/2}W(u)\,du=0,
\qquad0\le r\le R.}
\tag{L-15449.1}
\]

Every high-order safe window `H^[m]` from `L-15155` satisfies (L-15449.1) for
`R=m-1`.

Let `P` be a polynomial of degree at most `R`.

## 2. One terminal lattice row

For `A>=1` and real `x`, define

\[
\boxed{
\mathcal T_{A,P,W}(x)
=
\sum_{n\ge1}
\frac{P(\log n)}{\sqrt{An}}
W\!\left(x-\log(An)\right).}
\tag{L-15449.2}
\]

The sum is finite because `W` is compactly supported. Its active lattice lies
in

\[
\frac{e^{x-u_+}}A
\le n\le
\frac{e^{x-u_-}}A.
\tag{L-15449.3}
\]

Assume

\[
\frac{e^{x-u_+}}A>1,
\tag{L-15449.4}
\]

so the active interval is separated from the initial endpoint. The finitely
many rows before this condition holds can be retained separately.

## 3. The continuous main term vanishes exactly

Put

\[
F_{A,x}(t)
=
\frac{P(\log t)}{\sqrt{At}}
W\!\left(x-\log(At)\right).
\tag{L-15449.5}
\]

Its continuous integral is

\[
I_{A,P,W}(x)=\int_0^\infty F_{A,x}(t)\,dt.
\]

With

\[
u=x-\log(At),
\qquad
t=\frac{e^{x-u}}A,
\]

one obtains

\[
\boxed{
I_{A,P,W}(x)
=
\frac{e^{x/2}}A
\int_{\mathbb R}
 e^{-u/2}
 P(x-\log A-u)W(u)\,du.}
\tag{L-15449.6}
\]

The function `u -> P(x-log A-u)` is a polynomial of degree at most `R`.
Equation (L-15449.1) therefore gives

\[
\boxed{I_{A,P,W}(x)=0.}
\tag{L-15449.7}
\]

This is the exact pole-model cancellation. It occurs before any estimate and is
uniform in `A`.

## 4. First Euler remainder

For a compact continuous piecewise-`C^1` function vanishing at its support
endpoints, the periodic first Bernoulli formula gives

\[
\sum_{n\in\mathbb Z}F(n)-\int_{\mathbb R}F(t)dt
=
\int_{\mathbb R}\widetilde B_1(t)F'(t)dt,
\qquad
|\widetilde B_1|\le\frac12.
\tag{L-15449.8}
\]

Under (L-15449.4), applying this to `F_(A,x)` gives

\[
\left|\mathcal T_{A,P,W}(x)-I_{A,P,W}(x)\right|
\le\frac12\int_0^\infty|F_{A,x}'(t)|dt.
\tag{L-15449.9}
\]

Write `y=log t` and `u=x-log A-y`. Direct differentiation gives

\[
\begin{aligned}
\int_0^\infty|F_{A,x}'(t)|dt
\le e^{-x/2}
\int_{u_-}^{u_+}e^{u/2}
\Big(&|P'(x-\log A-u)|\,|W(u)|\\
&+|P(x-\log A-u)|
 [\tfrac12|W(u)|+|W'(u)|]
\Big)du.
\end{aligned}
\tag{L-15449.10}
\]

The multiplicative parameter `A` cancels completely from the leading
exponential factor.

Define

\[
\mathcal P_{A,x}
=
\max_{u_-\le u\le u_+}
\left(
 |P(x-\log A-u)|
 +|P'(x-\log A-u)|
\right)
\tag{L-15449.11}
\]

and

\[
C_W
=
\frac12\int_{u_-}^{u_+}e^{u/2}
\left(\frac32|W(u)|+|W'(u)|\right)du.
\tag{L-15449.12}
\]

Combining (L-15449.7)--(L-15449.12) proves

\[
\boxed{
|\mathcal T_{A,P,W}(x)|
\le C_W\,\mathcal P_{A,x}\,e^{-x/2}.}
\tag{L-15449.13}
\]

No prime theorem, zero-free region, or RH hypothesis enters this estimate.

## 5. Uniform polynomial form

Suppose

\[
\log A\le\delta x+C,
\qquad0<\delta<1,
\tag{L-15449.14}
\]

and the coefficient norm of `P` is bounded by `exp(o(x))` for a fixed degree.
Then

\[
\mathcal P_{A,x}
\le e^{o(x)}(1+x)^R,
\]

and hence

\[
\boxed{
|\mathcal T_{A,P,W}(x)|
\le e^{-x/2+o(x)}.}
\tag{L-15449.15}
\]

The point is that the estimate for one large-variable lattice row is independent
of the size of its small multiplicative prefix.

## 6. A complete terminal packet

Let `J<=x<=J+1`. Consider a source-bound terminal family

\[
\mathcal T_J(x)
=
\sum_{A\in\mathcal A_J}
 c_A\mathcal T_{A,P_A,W}(x),
\tag{L-15449.16}
\]

where

\[
A\le e^{\delta J+C},
\qquad0<\delta<\frac12,
\tag{L-15449.17}
\]

and

\[
\sum_{A\in\mathcal A_J}|c_A|
\max_{J\le x\le J+1}\mathcal P_{A,x}
\le e^{(\delta+o(J))J}.
\tag{L-15449.18}
\]

Then (L-15449.13) gives the pointwise terminal bound

\[
\boxed{
\sup_{J\le x\le J+1}|\mathcal T_J(x)|
\le
\exp\left[-\left(\frac12-\delta-o(1)\right)J\right].}
\tag{L-15449.19}
\]

Consequently its unit-block energy satisfies

\[
\boxed{
\int_J^{J+1}|\mathcal T_J(x)|^2dx
\le
\exp\left[-\left(1-2\delta-o(1)\right)J\right].}
\tag{L-15449.20}
\]

Thus every terminal family of this normal form has coefficient exponent zero;
in fact it decays exponentially.

## 7. Why the exponent is sharp for the argument

One Euler remainder contributes `e^(-J/2)`. The total number and divisor weight
of small products below `e^(delta J)` contributes `e^(delta J+o(J))`.
Therefore the terminal amplitude exponent is exactly

\[
-\frac12+\delta,
\]

and the energy exponent is

\[
-1+2\delta.
\]

The fixed-reserve condition `delta<1/2` is precisely what makes the terminal
ledger contract.

## 8. Application to the high-order safe windows

For the window

\[
W=H^{[K+1]},
\]

`L-15155` supplies (L-15449.1) through degree `K`. The exact finite
Heath--Brown and Möbius-resolvent rows contain at most one logarithmic factor,
and all finite complexity substitutions produce polynomials of bounded degree
at fixed `K`.

`L-15450` proves that every terminal Type-I row reduces to (L-15449.16), with
(L-15449.18) supplied by the fixed-order divisor bound. Hence the terminal
packet family in the corrected proposal is no longer an open Selberg/Hankel
certificate.

## 9. Proof boundary

Closed here:

- exact continuous pole-model cancellation;
- the uniform first Euler remainder;
- exponential decay of every terminal normal-form family.

Not closed here:

- the structural reduction of all terminal tuples, supplied by `L-15450`;
- balanced Type-II packet estimates;
- RH.
