# L-91030 — A unit-atom barrier closes the arithmetic Green removal for every scale `a>=1/3`

Claim ID: `L-91030`  
Status: **PROPOSED COMPLETE UNCONDITIONAL LARGE-SCALE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-12  
Corrected: 2026-08-12 — replaced a double-counted integral estimate by a monotonicity proof and exact finite lower certificate  
Depends on: `L-91026`; exact certificate in `X-91023`  
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

## 3. Monotonicity of `s zeta(1+s)`

Put

\[
 G(s)=s\zeta(1+s).
\]

Then

\[
 G'(s)
 =1+\sum_{n\ge2}n^{-1-s}(1-s\log n).
 \tag{L-91030.6}
\]

Discarding the nonnegative terms gives

\[
 G'(s)
 \ge1-\sum_{n\ge2}
 n^{-1-s}(s\log n-1)_+.
 \tag{L-91030.7}
\]

The continuous function

\[
 h_s(x)=x^{-1-s}(s\log x-1)_+
\]

is nonnegative and unimodal. For any nonnegative unimodal function on the half-line,

\[
 \sum_{n\ge2}h_s(n)
 \le\int_1^\infty h_s(x)\,dx+\max_{x\ge1}h_s(x).
\]

Here

\[
 \int_1^\infty h_s(x)\,dx=\frac{e^{-1}}s,
\]

and

\[
 \max h_s
 =\frac{s}{1+s}e^{-2-1/s}
 <e^{-2}.
\]

Thus, for `s>=2/3`,

\[
 \sum_{n\ge2}h_s(n)
 <\frac{3}{2e}+e^{-2}<1.
\]

The last inequality follows, for example, from `e>8/3`. Therefore

\[
 \boxed{G'(s)>0\qquad(s\ge2/3).}
 \tag{L-91030.8}
\]

## 4. Exact lower certificate at `s=2/3`

Since `x^(-5/3)` is decreasing,

\[
 \zeta(5/3)
 \ge
 \sum_{n=1}^{30}n^{-5/3}
 +\int_{31}^{\infty}x^{-5/3}\,dx.
\]

Consequently

\[
 \boxed{
 G(2/3)
 \ge
 L_{30}:=
 \frac23\sum_{n=1}^{30}n^{-5/3}
 +31^{-2/3}.
 }
 \tag{L-91030.9}
\]

The exact integer/rational certificate in `X-91023` proves

\[
 \boxed{
 L_{30}>\frac{1414214}{10^6}>\sqrt2.
 }
 \tag{L-91030.10}
\]

For completeness, the replay chooses, for every `1<=n<=31`, the least integer `U_n` satisfying

\[
 U_n^3\ge n\,10^{18}.
\]

Then

\[
 n^{-5/3}\ge\frac{10^{12}}{nU_n^2},
 \qquad
 31^{-2/3}\ge\frac{10^{12}}{U_{31}^2},
\]

so the complete lower bound is a `Fraction` computation. The rational upper bound for `sqrt(2)` is certified by

\[
 (1414214/10^6)^2>2.
\]

Combining (L-91030.8) and (L-91030.10),

\[
 \boxed{
 s\ge\frac23
 \quad\Longrightarrow\quad
 s\zeta(1+s)>\sqrt2
 \quad\Longrightarrow\quad
 r_s<\frac1{\sqrt2}.
 }
 \tag{L-91030.11}
\]

Equations (L-91030.5) and (L-91030.11) yield

\[
 \boxed{
 \mathcal B_{2a,a}(t)>0
 \qquad
 (a\ge1/3,\ t\ge0).
 }
 \tag{L-91030.12}

## 5. Consequence

This strengthens `L-91027` from `a>=1/2` to `a>=1/3` using the unit atom, monotonicity of `s zeta(1+s)`, and one finite exact lower certificate.

Together with `L-91028`, the unresolved arithmetic scale interval is

\[
 \boxed{
 a_0\le a<\frac13
 }
\]

for some non-effective `a_0>0`.

The completed critical-boundary source-to-Hardy intertwiner remains a separate RH-bearing obligation.