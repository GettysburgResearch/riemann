# L-23714 — Centered cumulative Hardy energy

Claim ID: `L-23714`  
Title: After subtracting the explicit positive linear mode, a sublinear logarithmic derivative energy forces eventual positivity of the fifth-aligned cumulative shell  
Status: **PROPOSED EXACT CONDITIONAL LEMMA; CENTERED ENERGY ESTIMATE OPEN**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Dependencies: `L-23709`; `R-23706`  
Scope: corrected energy normalization and conditional eventual-positivity theorem

## 1. Explicit main mode

Retain

\[
Q(t)=C(e^t),
\qquad
\widehat Q(z)=\frac{h(z)}{z^2},
\]

where

\[
h(z)=
\frac{s(1-5^{-s})}{(s-1)\zeta(s)},
\qquad s=z+\frac12.
\tag{L-23714.1}
\]

Define

\[
\boxed{
a_5=h(0)
=-\frac{1-5^{-1/2}}{\zeta(1/2)}>0.
}
\tag{L-23714.2}
\]

The double pole `a_5/z^2` is the explicit positive linear mode `a_5t` in `Q(t)`.

## 2. Centered derivative

Put

\[
\boxed{
U(t)=Q'(t)-a_5.
}
\tag{L-23714.3}
\]

Since `Q(0)=0`,

\[
\boxed{
Q(T)=a_5T+\int_0^TU(t)dt.
}
\tag{L-23714.4}
\]

The Laplace transform is

\[
\begin{aligned}
\widehat U(z)
&=z\widehat Q(z)-\frac{a_5}{z}\\
&=\boxed{
\frac{h(z)-h(0)}{z}.}
\end{aligned}
\tag{L-23714.5}

The apparent singularity at `z=0` is removable. Every hypothetical off-line zeta zero remains an uncancelled pole through `h(z)`.

## 3. Centered energy criterion

Assume

\[
\boxed{
\int_0^T|U(t)|^2dt=o(T).
}
\tag{L-23714.6}

Then Cauchy--Schwarz and (L-23714.4) give

\[
\left|\int_0^TU(t)dt\right|
\le
T^{1/2}
\left(\int_0^T|U(t)|^2dt\right)^{1/2}
=o(T).
\]

Consequently

\[
\boxed{
Q(T)=a_5T+o(T),
}
\tag{L-23714.7}

and hence

\[
\boxed{
C(y)=a_5\log y+o(\log y)>0
}
\tag{L-23714.8}

for every sufficiently large `y`.

This is exactly the eventual one-sign conclusion needed by Landau. No finite positive ladder is required.

## 4. Exact Abel--Cesaro form

Let

\[
H_U(T)=\int_0^T|U(t)|^2dt.
\]

For every nonnegative locally integrable energy density,

\[
\boxed{
H_U(T)=o(T)
\quad\Longleftrightarrow\quad
\sigma
\int_0^\infty e^{-2\sigma t}|U(t)|^2dt
\longrightarrow0
\quad(\sigma\downarrow0).
}
\tag{L-23714.9}

The proof is the same elementary Abel--Cesaro comparison as in `L-23713`, with `T` in place of `T^2`.

## 5. Exact Hardy multiplier

For every `sigma>0` in the weighted convergence region, Laplace Plancherel gives

\[
\boxed{
\begin{aligned}
\int_0^\infty e^{-2\sigma t}|U(t)|^2dt
={1\over2\pi}
\int_{-\infty}^{\infty}
\left|
\frac{h(\sigma+i\tau)-h(0)}{\sigma+i\tau}
\right|^2d\tau.
\end{aligned}}
\tag{L-23714.10}

Therefore the corrected source-specific Hardy theorem is

\[
\boxed{
\sigma
\int_{-\infty}^{\infty}
\left|
\frac{h(\sigma+i\tau)-h(0)}{\sigma+i\tau}
\right|^2d\tau
\longrightarrow0.
}
\tag{L-23714.11}

Again the factor `1/(2pi)` is immaterial in the limit.

Unlike the refuted uncentered energy, the multiplier in (L-23714.11) is regular at zero. It is the anchored Hardy difference quotient of the actual Euler-aligned inverse-zeta source.

## 6. Reflected Selberg interface

Write

\[
B_5(s)=\frac{1-5^{-s}}{\zeta(s)},
\qquad
r(s)=\frac{s}{s-1},
\]

so that

\[
h(z)=r(s)B_5(s),
\qquad s=z+\frac12.
\tag{L-23714.12}
\]

The inverse series

\[
A_5(s)=B_5(s)^{-1}=\frac{\zeta(s)}{1-5^{-s}}
\]

has coefficients

\[
a_5(n)=v_5(n)+1\ge1,
\]

and generalized prime weights

\[
\Lambda_5^\#(n)
=\Lambda(n)+(\log5)\mathbf1_{n=5^k}\ge0.
\]

Thus the generalized reflected Selberg algebra applies to `B_5` exactly as in the dyadic identity on PR #234. Multiplying its Hermitian logarithmic-derivative square by `|B_5|^2` gives the positive derivative energy `|B_5'|^2`.

A complete proof must still pass from that derivative reserve to the anchored difference quotient (L-23714.11) with a strict constant and all rational-factor cross terms. This is a concrete Hardy/Poincare problem, not an automatic consequence of the reflected identity.

## 7. Conditional RH consequence

If (L-23714.6), equivalently (L-23714.11), holds, then `C` is eventually positive by (L-23714.8). Subtracting its compact initial segment changes the Mellin transform by an entire function. Landau's one-sign theorem applied to

\[
\widehat C(z)
=
\frac{(1-5^{-(z+1/2)})(z+1/2)}
 {z^2(z-1/2)\zeta(z+1/2)}
\]

then shows that the transform is holomorphic for `Re z>0`. Every zero of zeta with real part greater than one half would give an uncancelled pole there. Functional-equation symmetry yields RH.

## 8. Proof boundary

Closed exactly:

- extraction of the positive linear principal part;
- the centered derivative and its regular Hardy multiplier;
- centered energy implies eventual positivity;
- Abel--Cesaro and Plancherel forms;
- the exact positive-coefficient `p=5` Selberg interface.

Open:

- the centered Hardy estimate (L-23714.11);
- its strict reflected-Selberg/Poincare proof;
- Greedy Slack/DCRS;
- RH.
