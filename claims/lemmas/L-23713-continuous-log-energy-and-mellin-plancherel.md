# L-23713 — Continuous logarithmic energy and Mellin–Plancherel adapter

Claim ID: `L-23713`  
Title: The discrete fifth-shell boundary energy is dominated by one continuous logarithmic Sobolev energy with an exact inverse-zeta Hardy representation  
Status: **PROPOSED EXACT ANALYTIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Dependencies: `L-23709`, `L-23711`; elementary Laplace Plancherel  
Scope: exact energy adapter; no energy upper bound is asserted

## 1. Logarithmic state

Let

\[
C(y)=\mathfrak S_5(y),
\qquad
Q(t)=C(e^t),
\qquad t\ge0.
\tag{L-23713.1}
\]

Since `C(1)=0`, one has `Q(0)=0`. Define

\[
\boxed{
D(t)=Q'(t)+\frac12Q(t)
}
\tag{L-23713.2}
\]

in the piecewise-smooth/distributional sense. The shell kernel vanishes at every entering integer atom, so `Q` is continuous and `D` has no unlisted point-mass term.

## 2. Exact continuous interpolation of the discrete boundary vector

Fix `y=e^T>=2` and define, for real `1<=x<=y`,

\[
\mathcal Y_y(x)=x^{-1/2}C(y/x).
\tag{L-23713.3}
\]

Then

\[
\boxed{
\mathcal Y_y'(x)
=-x^{-3/2}D(T-\log x).
}
\tag{L-23713.4}
\]

Indeed `T-log x=log(y/x)`, so differentiation gives exactly the two terms in `D`.

At integer `m`,

\[
\mathcal Y_y(m)=Y_m(y)
=m^{-1/2}C(y/m)
\]

from `L-23711`.

## 3. Discrete energy is bounded by continuous energy

On every interval `[m,m+1]`, Cauchy--Schwarz gives

\[
\begin{aligned}
|Y_m-Y_{m+1}|^2
&=\left|
\int_m^{m+1}x^{-3/2}D(T-\log x)\,dx
\right|^2\\
&\le
\left(\int_m^{m+1}x^{-2}dx\right)
\left(\int_m^{m+1}x^{-1}|D(T-\log x)|^2dx\right).
\end{aligned}
\]

Since

\[
m^2\int_m^{m+1}x^{-2}dx=rac m{m+1}<1,
\]

summing over `2<=m<floor(y)` yields

\[
\boxed{
\mathcal E_5(y)
\le
\int_0^{\log(y/2)}|D(t)|^2dt.
}
\tag{L-23713.5}
\]

Thus the continuous sufficient theorem

\[
\boxed{
\int_0^T|D(t)|^2dt=o(T^2)
}
\tag{L-23713.6}
\]

implies discrete `CRE(5)`.

## 4. Exact Laplace transform

Put

\[
s=z+\frac12,
\qquad
B_5(s)=\frac{1-5^{-s}}{\zeta(s)}.
\]

From `L-23709`,

\[
\widehat Q(z)
=\frac{s\,B_5(s)}{(s-1/2)^2(s-1)}.
\tag{L-23713.7}
\]

Because `Q(0)=0`, Laplace differentiation gives

\[
\boxed{
\widehat D(z)
=(z+1/2)\widehat Q(z)
=rac{s^2}{(s-1/2)^2(s-1)}B_5(s).
}
\tag{L-23713.8}
\]

Every nontrivial zeta zero with real part greater than one half remains an uncancelled pole.

## 5. Mellin–Plancherel identity

For every `sigma>0` for which the weighted energy is finite, Laplace Plancherel gives

\[
\boxed{
\begin{aligned}
\int_0^\infty e^{-2\sigma t}|D(t)|^2dt
={1\over2\pi}\int_{-\infty}^{\infty}
\left|
\frac{s^2(1-5^{-s})}
 {(s-1/2)^2(s-1)\zeta(s)}
\right|^2d\tau,
\end{aligned}}
\tag{L-23713.9}
\]

where

\[
s=\frac12+\sigma+i\tau.
\]

This is an all-line Hardy energy. It does **not** identify one global vertical integral with one physical unit block; the scope correction of PR #241 is respected.

## 6. Exact Abel–Cesàro equivalence

Let

\[
H(T)=\int_0^T|D(t)|^2dt.
\]

For every nonnegative locally integrable energy density,

\[
\boxed{
H(T)=o(T^2)
\quad\Longleftrightarrow\quad
\sigma^2
\int_0^\infty e^{-2\sigma t}|D(t)|^2dt
\longrightarrow0
\quad(\sigma\downarrow0).
}
\tag{L-23713.10}
\]

### Proof

Integration by parts gives

\[
\int_0^\infty e^{-2\sigma t}|D(t)|^2dt
=2\sigma\int_0^\infty e^{-2\sigma t}H(t)dt.
\]

If `H(t)=o(t^2)`, rescaling `u=sigma t` and dominated convergence give the right side of (L-23713.10). Conversely,

\[
\int_0^\infty e^{-2\sigma t}|D(t)|^2dt
\ge e^{-2}H(1/\sigma),
\]

so the Abel limit implies `H(T)/T^2->0` with `T=1/sigma`.

Combining (L-23713.9)--(L-23713.10), the continuous closing theorem is exactly

\[
\boxed{
\sigma^2
\int_{-\infty}^{\infty}
\left|
\frac{s^2(1-5^{-s})}
 {(s-1/2)^2(s-1)\zeta(s)}
\right|^2d\tau
\longrightarrow0,
\qquad s=\frac12+\sigma+i\tau.
}
\tag{L-23713.11}
\]

The harmless factor `1/(2pi)` is omitted in this limit statement.

## 7. Review meaning

Equation (L-23713.11) is the precise Hardy-space statement that a reflected Selberg argument must establish. It is stronger than the discrete `CRE(5)` theorem but has three advantages:

1. its physical energy dominates the exact discrete first-crossing energy;
2. its transform is explicit and source-bound;
3. its all-line scope matches the part of the reflected Selberg programme that has actually survived review.

It remains RH-bearing. This lemma supplies an adapter, not an estimate.

## 8. Proof boundary

Closed exactly:

- the continuous interpolation and derivative identity;
- domination of discrete energy by continuous energy;
- the inverse-zeta Hardy multiplier;
- Laplace Plancherel;
- the Abel–Cesàro equivalence.

Open:

- the Hardy limit (L-23713.11);
- continuous or discrete `CRE(5)`;
- Greedy Slack/DCRS;
- RH.
