# L-91030 — A unit-atom barrier closes the arithmetic Green removal for every scale `a>=1/3`

Claim ID: `L-91030`  
Status: **PROPOSED COMPLETE UNCONDITIONAL LARGE-SCALE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-12  
Depends on: `L-91026`  
RH status: **unproved**

## 1. Scaled variables

Put

\[
 s=2a,
 \qquad
 r_s=\frac{c_s}{s}
 =\frac1{s\zeta(1+s)},
\]

and retain

\[
 e_s(y)=E_{s,0}(y/s),
 \qquad
 I_s(y)=sE_{s,1}(y/s)=\int_0^y e_s(v)\,dv.
\]

The scaled Green-removal density is

\[
 \boxed{
 b_s(y)
 =\frac2s\mathcal B_{s,s/2}(y/s)
 =-2r_s+\kappa e_s(y)+2I_s(y),
 }
 \tag{L-91030.1}
\]

where

\[
 \kappa=\sqrt{275/14}>2.
\]

## 2. The unit-atom barrier

The arithmetic sum defining `E_(s,0)` always contains its unit atom. Hence

\[
 \boxed{
 e_s(y)\ge\max(0,1-r_sy).
 }
 \tag{L-91030.2}
\]

Consequently

\[
 I_s(y)
 \ge
 \begin{cases}
 y-r_sy^2/2,&0\le y\le1/r_s,\\
 1/(2r_s),&y\ge1/r_s.
 \end{cases}
 \tag{L-91030.3}
\]

If `0<=y<=1/r_s`, then

\[
 b_s(y)
 \ge
 \kappa+2y-r_s(2+\kappa y+y^2).
 \tag{L-91030.4}
\]

The right side is concave in `y`, so its minimum on this interval occurs at an endpoint. The endpoint values are

\[
 \kappa-2r_s>0
\]

and

\[
 \frac1{r_s}-2r_s.
\]

If `y>=1/r_s`, (L-91030.3) gives directly

\[
 b_s(y)\ge\frac1{r_s}-2r_s.
\]

Therefore

\[
 \boxed{
 r_s\le\frac1{\sqrt2}
 \quad\Longrightarrow\quad
 \mathcal B_{s,s/2}(t)\ge0
 \quad(t\ge0).
 }
 \tag{L-91030.5}
\]

The inequality is strict for the zeta source.

## 3. An elementary zeta bound

For `s>0`, monotonicity of `x^(-1-s)` gives

\[
 \zeta(1+s)
 \ge
 1+2^{-1-s}+\int_2^\infty x^{-1-s}\,dx.
\]

Thus

\[
 \boxed{
 s\zeta(1+s)
 \ge
 g(s):=s+\left(1+\frac s2\right)2^{-s}.
 }
 \tag{L-91030.6}
\]

The function `g` is increasing for `s>=2/3`. Indeed,

\[
 g'(s)
 =1+2^{-s}
 \left[\frac12-\left(1+\frac s2\right)\log2\right]>0,
\]

because the magnitude of the negative correction is maximal at `s=2/3` and is less than one.

At the left endpoint,

\[
 g(2/3)
 =\frac23+\frac43\,2^{-2/3}
 >\sqrt2.
\]

For a completely rational certification one may use

\[
 2^{1/3}<1.26,
 \qquad
 \sqrt2<1.415,
\]

which gives `g(2/3)>1.50>1.415`.

Therefore

\[
 \boxed{
 s\ge\frac23
 \quad\Longrightarrow\quad
 r_s=\frac1{s\zeta(1+s)}<\frac1{\sqrt2}.
 }
 \tag{L-91030.7}
\]

Combining (L-91030.5) and (L-91030.7),

\[
 \boxed{
 \mathcal B_{2a,a}(t)>0
 \qquad
 (a\ge1/3,\ t\ge0).
 }
 \tag{L-91030.8}

## 4. Consequence

This strengthens `L-91027` from `a>=1/2` to `a>=1/3` using only the unit atom and an elementary integral lower bound for zeta.

Together with `L-91028`, the unresolved arithmetic scale interval is

\[
 \boxed{
 a_0\le a<\frac13
 }
\]

for some non-effective `a_0>0`.

The completed critical-boundary source-to-Hardy intertwiner remains a separate RH-bearing obligation.