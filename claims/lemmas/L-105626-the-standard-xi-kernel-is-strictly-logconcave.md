# L-105626 — The standard Xi Fourier kernel is strictly log-concave

Claim ID: `L-105626`  
Status: **PROVED UNCONDITIONALLY BY AN EXPLICIT MIXTURE-VARIANCE BOUND; INDEPENDENT REVIEW REQUESTED**  
Created: 2026-08-25  
Depends on: the classical theta-series formula for the standard Xi kernel  
RH status: **not assumed**

## 1. Standard positive summands

For `u>=0`, use

\[
\Phi(u)=4\sum_{n\ge1}\phi_n(u),
\]

\[
\phi_n(u)
=
\left(
2\pi^2n^4e^{9u/2}
-3\pi n^2e^{5u/2}
\right)e^{-\pi n^2e^{2u}}.
\tag{L-105626.1}
\]

Put

\[
x=\pi e^{2u}\ge\pi,
\qquad y_n=xn^2.
\]

Then

\[
\boxed{
\phi_n(u)
=\pi e^{5u/2}
 n^2(2xn^2-3)e^{-xn^2}>0.
}
\tag{L-105626.2}
\]

All series below converge absolutely and locally uniformly with their first two
derivatives.

Define the logarithmic score and curvature

\[
a_n=(\log\phi_n)',
\qquad b_n=(\log\phi_n)''.
\]

Direct differentiation gives

\[
\boxed{
a_n
={9\over2}-2y_n+{6\over2y_n-3},}
\tag{L-105626.3}
\]

\[
\boxed{
b_n
=-4y_n-{24y_n\over(2y_n-3)^2}<0.}
\tag{L-105626.4}
\]

In particular

\[
-b_1\ge4x.
\tag{L-105626.5}
\]

## 2. Exact mixture identity

Let

\[
p_n={\phi_n\over\sum_m\phi_m}.
\]

For every positive mixture,

\[
\boxed{
(\log\Phi)''
=\sum_np_nb_n
+\operatorname{Var}_p(a_n).
}
\tag{L-105626.6}
\]

Variance is minimized at the mean, hence

\[
\operatorname{Var}_p(a_n)
\le
\sum_{n\ge2}p_n(a_n-a_1)^2.
\tag{L-105626.7}
\]

Also

\[
-\sum_np_nb_n\ge p_1(-b_1).
\]

Consequently strict log-concavity follows from the single unnormalized bound

\[
\boxed{
\sum_{n\ge2}
{\phi_n\over\phi_1}
(a_n-a_1)^2
<-b_1.
}
\tag{L-105626.8}
\]

## 3. Uniform elementary majorant

Put `q_n=n^2-1`. From (L-105626.2),

\[
{\phi_n\over\phi_1}
=
{n^2(2xn^2-3)\over2x-3}
e^{-xq_n}
\le2n^4e^{-xq_n},
\tag{L-105626.9}
\]

because `x>=pi>3`.

From (L-105626.3),

\[
|a_n-a_1|
\le
2xq_n+{6\over2x-3}
\le3xq_n.
\tag{L-105626.10}
\]

The last inequality uses

\[
6\le xq_n(2x-3),
\]

which already holds at the minimum `x>3`, `q_n>=3`.

Therefore

\[
\boxed{
\sum_{n\ge2}
{\phi_n\over\phi_1}(a_n-a_1)^2
\le
18x^2
\sum_{n\ge2}
n^4q_n^2e^{-xq_n}.
}
\tag{L-105626.11}
\]

For every `q_n>=3`, the function `x exp(-x q_n)` is decreasing on
`[pi,infinity)`. Thus it suffices to bound

\[
S=\sum_{n\ge2}n^4q_n^2e^{-\pi q_n}.
\]

Using `pi>3` and the elementary Taylor bound `e^3>20`,

\[
144e^{-3\pi}<144e^{-9}<{18\over1000}.
\tag{L-105626.12}
\]

For `n>=3`, put

\[
c_n=n^4(n^2-1)^2e^{-3(n^2-1)}.
\]

The first term satisfies

\[
c_3=5184e^{-24}<{1\over10^6},
\]

because `e^24=(e^3)^8>20^8`. Moreover

\[
{c_{n+1}\over c_n}<10^{-8}
\qquad(n\ge3),
\]

by the explicit ratio and `e^21>(e^3)^7>20^7`. Hence

\[
\sum_{n\ge3}c_n<{1\over10^6}(1-10^{-8})^{-1}
<{1\over1000}.
\]

A deliberately looser rational summary is therefore

\[
\boxed{S<{19\over1000}.}
\tag{L-105626.13}
\]

Using `pi<22/7`,

\[
{9\over2}x
\sum_{n\ge2}n^4q_n^2e^{-xq_n}
\le
{9\over2}\pi S
<
{9\over2}{22\over7}{19\over1000}
={1881\over7000}<1.
\tag{L-105626.14}
\]

Multiplying by `4x` gives

\[
18x^2
\sum_{n\ge2}n^4q_n^2e^{-xq_n}
<4x
\le-b_1.
\tag{L-105626.15}
\]

Equations (L-105626.11) and (L-105626.15) prove (L-105626.8).

## 4. Conclusion

Substitution in the exact mixture identity yields

\[
\boxed{
(\log\Phi)''(u)<0
\qquad(u\ge0).
}
\tag{L-105626.16}
\]

The even extension is therefore strictly log-concave on each open half-line,
with the expected symmetric derivative at the origin.

This proof uses neither interval arithmetic nor the recent external preprints
claiming the same source property. It uses only the standard theta formula,
positivity of its summands, elementary calculus, `3<pi<22/7`, and a Taylor
lower bound for `e^3`.

## 5. Consequence for the current–Turán profile

Combining with `L-105624` gives unconditionally for the standard Xi source

\[
\boxed{
\xi\longmapsto
{h e^{-h\xi}\Lambda_2(\xi)\over j_h(\xi)}
\text{ is nonincreasing on }[0,\infty)
\qquad(h>0).
}
\tag{L-105626.17}
\]

Thus the `LC` source hypothesis in `L-105625` is paid for Xi. The remaining
interface is the exact inner/causal realization of the physical derivative
all-pass and its finite-window seams.

## 6. Scope

Strict log-concavity is a second-order source theorem and does not imply that
the Fourier transform has only real zeros. It does not prove the
Laguerre--Polya `TP_infinity` property or RH. The final sentence of Section 5
uses only the new monotone-profile theorem, not any external assertion that
log-concavity itself closes RH.
