# L-91009 — Sublogarithmic logarithmic-derivative control transfers to annular Pick-ray positivity

Claim ID: `L-91009`  
Status: **PROPOSED COMPLETE TRANSFER LEMMA — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91003`, `L-91008`  
RH status: **unproved**

## 1. General input

For `T>=3`, let `eta(T)>0` be nonincreasing with `eta(T)->0`, and let `B(T)>0` satisfy

\[
 B(T)=o(\log T).
\tag{L-91009.1}
\]

Assume that for some fixed `c_0>0`, uniformly for large `T`,

\[
 \boxed{
 \left|\frac{\zeta'}{\zeta}(\sigma+it)\right|
 \le B(T)
 }
\tag{L-91009.2}
\]

whenever

\[
 |t-T|\le2,
 \qquad
 \sigma\ge1-c_0\eta(T).
\tag{L-91009.3}
\]

This is a logarithmic-derivative strengthening of a zero-free region. The lemma converts it directly into a positive real-ray statement for the safe-line Pick generator.

## 2. Expanding-disc asymptotic

Fix

\[
 0<c_1<\frac{c_0}{8}
\]

and put

\[
 R_T=\frac34+c_1\eta(T).
\tag{L-91009.4}
\]

For a real carrier `x` with `T=|x|+3`, let

\[
 s_x=\frac12+ix,
 \qquad
 \ell_x=\log(2+|x|),
\]

and let `A_x` and `Phi` be as in `L-91008`.

### Theorem 2.1

Under (L-91009.2)--(L-91009.3),

\[
 \boxed{
 \max_{|w|\le R_T}
 \left|
 \mathcal A_x(w)-\ell_x\Phi(w)
 \right|
 \ll 1+B(T).
 }
\tag{L-91009.5}
\]

Consequently,

\[
 \boxed{
 \frac{\mathcal A_x(w)}{\ell_x}
 =\Phi(w)+o(1)
 }
\tag{L-91009.6}
\]

uniformly on the expanding disc `|w|<=R_T`.

### Proof

On `|w|=R_T`, with the principal branch `r_w=sqrt(1-w)`,

\[
 \Re r_w\ge\sqrt{1-R_T}.
\]

For small `eta(T)`,

\[
 \sqrt{\frac14-c_1\eta(T)}
 \ge\frac12-2c_1\eta(T),
\]

so

\[
 \Re(s_x+r_w)
 \ge1-2c_1\eta(T)
 \ge1-c_0\eta(T).
\tag{L-91009.7}
\]

Also `|Im r_w|<=1`, so the height remains within the range of (L-91009.3), after harmless adjustment of `T` by an absolute constant.

Using

\[
 \mathscr X(s)
 =-\frac{\xi'}{\xi}(s)
 =-\frac{\zeta'}{\zeta}(s)
 -\frac1s-\frac1{s-1}
 +\frac12\log\pi
 -\frac12\frac{\Gamma'}{\Gamma}(s/2),
\]

Stirling and the input give

\[
\begin{aligned}
 \mathscr X(s_x+1)&=-\frac12\ell_x+O(1),\\
 \mathscr X'(s_x+1)&=O(1),\\
 \mathscr X(s_x+r_w)&=-\frac12\ell_x+O(1+B(T))
\end{aligned}
\tag{L-91009.8}
\]

uniformly on the circle. Insert these estimates into the square-root formula

\[
 \mathcal G_s(w)
 =\frac{(2-w)\mathscr X(s+1)-w\mathscr X'(s+1)-2r_w\mathscr X(s+r_w)}{w^2},
\]

and use

\[
 \frac{2-w-2r_w}{w^2}
 =\frac1{(1+r_w)^2}.
\]

Since `R_T` stays bounded away from zero and one, the error on the circle is `O(1+B(T))`. Averaging the conjugate carriers gives (L-91009.5) on the circle. The difference is analytic in the pole-free disc guaranteed by the same logarithmic-derivative hypothesis, so the maximum principle gives the full disc. Equation (L-91009.6) follows from (L-91009.1). `square`

## 3. Real-ray sign

For real `0<=w<1`,

\[
 \Phi(w)=\frac1{2(1+\sqrt{1-w})^2}\ge\frac18.
\]

Therefore Theorem 2.1 implies

\[
 \boxed{
 \mathcal A_x(w)>0
 \quad
 \left(0\le w\le\frac34+c_1\eta(|x|+3)ight)
 }
\tag{L-91009.9}
\]

for every sufficiently large `|x|`.

Equivalently, the radial tangent defect is positive for

\[
 \boxed{
 t\ge\frac14-c_1\eta(|x|+3).
 }
\tag{L-91009.10}
\]

This penetrates the RH-detecting interval `0<t<1/4`; it is stronger than holomorphy alone but uses the stronger logarithmic-derivative input.

## 4. Coefficient corollary

Cauchy's estimate also gives

\[
 \boxed{
 |a_k(x)-\ell_xc_k|
 \ll [1+B(T)]R_T^{-k}.
 }
\tag{L-91009.11}
\]

This is useful when the input `B(T)` is substantially smaller than the phase-blind safe-disc boundary error. It does not by itself reach the full RH-detecting order.

## 5. Boundary

```text
sublog Xcal input -> expanding-disc asymptotic     PROPOSED COMPLETE
sublog Xcal input -> annular real-ray positivity   PROPOSED COMPLETE
radial tangent defect into t<1/4                   PROPOSED COMPLETE
coefficient transfer                               PROPOSED COMPLETE
source of sublog Xcal input                         EXTERNAL ANALYTIC INPUT
cofinal annular positivity to w=1                  OPEN / RH-EQUIVALENT
radial curvature positivity on 0<t<1/4             OPEN / RH-EQUIVALENT
Riemann Hypothesis                                  UNPROVED
```