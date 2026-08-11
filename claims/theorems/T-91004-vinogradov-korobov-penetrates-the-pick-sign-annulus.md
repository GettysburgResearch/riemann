# T-91004 — Vinogradov–Korobov control penetrates the Pick-sign annulus

Claim ID: `T-91004`  
Status: **PROPOSED COMPLETE UNCONDITIONAL TRANSFER THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91009`; the classical Vinogradov–Korobov logarithmic-derivative estimate for zeta  
RH status: **unproved**

## 1. Classical analytic input

Put

\[
 \eta_{\rm VK}(T)
 =\frac1{(\log T)^{2/3}(\log\log T)^{1/3}}
 \qquad(T\text{ large}).
\tag{T-91004.1}
\]

A standard logarithmic-derivative form of the Vinogradov–Korobov theorem states that there are absolute constants `c_0,C_0>0` such that

\[
 \boxed{
 \left|\frac{\zeta'}{\zeta}(\sigma+it)\right|
 \le C_0\eta_{\rm VK}(T)^{-1}
 }
\tag{T-91004.2}
\]

whenever

\[
 \bigl||t|-T\bigr|\le4,
 \qquad
 \sigma\ge1-c_0\eta_{\rm VK}(T),
\tag{T-91004.3}
\]

for all sufficiently large `T`.

This is the conventional zero-free-region/logarithmic-derivative input used in classical prime-number-theorem error terms; see, for example, the Vinogradov–Korobov chapter of Titchmarsh's zeta monograph and modern explicit zero-free-region refinements. The theorem below is a transfer of that input, not a new zero-free-region proof.

Since

\[
 \eta_{\rm VK}(T)^{-1}
 =o(\log T),
\tag{T-91004.4}
\]

`L-91009` applies.

## 2. Unconditional annular real-ray positivity

There is an absolute `c_1>0` such that, for every sufficiently large real carrier `x`,

\[
 \boxed{
 \mathcal A_x(w)>0
 }
\tag{T-91004.5}
\]

throughout

\[
 \boxed{
 0\le w\le\frac34+
 c_1\eta_{\rm VK}(|x|+3).
 }
\tag{T-91004.6}
\]

Thus the positive real ray crosses the direct absolute-Euler boundary `w=3/4` by the Vinogradov–Korobov scale.

Equivalently, with the radial variable `t=1-w`,

\[
 \boxed{
 J_x(1)+J_x'(1)(t-1)-J_x(t)>0
 }
\tag{T-91004.7}
\]

whenever

\[
 \boxed{
 t\ge\frac14-
 c_1\eta_{\rm VK}(|x|+3).
 }
\tag{T-91004.8}
\]

This is an unconditional sign statement inside a thin part of the RH-detecting radial interval `0<t<1/4`.

## 3. Expanding-disc asymptotic

The stronger complex statement is

\[
 \boxed{
 \frac{\mathcal A_x(w)}{\log(2+|x|)}
 =\frac1{2(1+\sqrt{1-w})^2}+o(1)
 }
\tag{T-91004.9}
\]

uniformly for

\[
 \boxed{
 |w|\le\frac34+c_1\eta_{\rm VK}(|x|+3).
 }
\tag{T-91004.10}
\]

The error before normalization is

\[
 O\left(
 (\log|x|)^{2/3}(\log\log|x|)^{1/3}
 \right).
\tag{T-91004.11}
\]

The limiting object is the Catalan/Beta Stieltjes function of `L-91008`; the classical zero-free machinery therefore controls not only holomorphy but the leading sign geometry.

## 4. Relation to the zero-free region

At a matching off-line zero of depth `y`, the unit-disc pole lies at

\[
 w_y=1-y^2.
\]

Positivity through (T-91004.6) excludes poles with

\[
 1-y^2
 \le\frac34+c_1\eta_{\rm VK},
\]

which is the depth scale

\[
 y\ge\frac12-O(\eta_{\rm VK}).
\]

Thus the theorem repackages the classical near-one zero-free region into a positive Pick-ray/tangent-defect statement. It does not improve the classical zero-free region numerically.

## 5. What remains

The width in (T-91004.6) tends to zero. RH requires positivity through every fixed

\[
 \frac34<w<1
\]

and cofinally to `w=1`. Equivalently, it requires radial tangent-defect positivity all the way down to `t=0`, and the stronger criterion of `T-91002` asks for pointwise radial curvature positivity.

The Vinogradov–Korobov theorem therefore crosses the first annular boundary but does not approach the full RH endpoint.

## 6. Exact boundary

```text
VK logarithmic-derivative input                     CLASSICAL EXTERNAL INPUT
expanding Catalan/Pick asymptotic past 3/4           PROPOSED COMPLETE
real-ray positivity past 3/4 at VK scale             PROPOSED COMPLETE
radial tangent-defect sign inside t<1/4              PROPOSED COMPLETE
new zero-free-region constant                         NOT CLAIMED
fixed annular radius >3/4                              OPEN / RH-BEARING
cofinal positivity to w=1                             OPEN / RH-EQUIVALENT
radial curvature positivity on 0<t<1/4                OPEN / RH-EQUIVALENT
Riemann Hypothesis                                     UNPROVED
```