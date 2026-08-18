# L-98010 — The unsieved `5:3` scalar-to-target ratio is strictly ordered

Claim ID: `L-98010`  
Status: **PROVED UNCONDITIONAL ANALYTIC THEOREM**  
Created: 2026-08-18  
Depends on: the canonical `5:3` dictionary of `L-97600`; the target coordinate used by the completed-parity Lorenz ledger  
RH status: **not assumed**

Put

\[
q_*(1)=0,\qquad q_*(2)=15,\qquad q_*(3)=6,
\qquad q_*(4)=3,\qquad q_*(n)=6\quad(n\ge5),
\]

\[
Q_*(Y)=\sum_{n\ge1}{q_*(n)\over\sqrt n}\log(Y/n)_+,
\qquad
T(Y)=(4\sqrt Y-3)\mathbf 1_{Y\ge1}.
\]

For `Y>=1` define

\[
\vartheta(Y)={Q_*(Y)\over T(Y)}.
\]

Then

\[
\boxed{
\vartheta(Y)=0\quad(1\le Y\le2),
\qquad
\vartheta\text{ is strictly increasing on }(2,\infty),
\qquad
\lim_{Y\to\infty}\vartheta(Y)=6.
}
\tag{L-98010.1}
\]

In particular

\[
0<\vartheta(Y)<6\qquad(Y>2).
\tag{L-98010.2}
\]

## 1. Cell derivative

Fix an integer `N>=2` and `N<Y<N+1`. Write

\[
A_N=\sum_{2\le n\le N}{q_*(n)\over\sqrt n},
\qquad
B_N=\sum_{2\le n\le N}{q_*(n)\log n\over\sqrt n}.
\]

Then

\[
Q_*(Y)=A_N\log Y-B_N.
\]

A direct differentiation shows that the sign of `vartheta'(Y)` is the sign of

\[
{B_N\over A_N}-c(Y),
\qquad
c(Y)=\log Y-2+{3\over2\sqrt Y}.
\tag{L-98010.3}
\]

The function `c` is strictly increasing for `Y>=1`. Hence it is enough on the
whole cell to prove

\[
B_N-c(N+1)A_N>0.
\tag{L-98010.4}
\]

## 2. A Riemann-sum inequality with the exact endpoint correction

Put `y=N+1`, `s=sqrt(y)`, `c=c(y)`, and

\[
g_y(x)=x^{-1/2}(\log x-c).
\]

For `1<=x<=y`,

\[
g_y'(x)=x^{-3/2}\left(1-{\log x-c\over2}\right).
\]

Because

\[
\log x-c\le\log y-c=2-{3\over2s}<2,
\]

`g_y` is strictly increasing on `[1,y]`. The right-endpoint Riemann sum therefore gives

\[
\sum_{n=1}^{N}g_y(n)
=\sum_{n=2}^{N+1}g_y(n)+g_y(1)-g_y(y)
\ge\int_1^y g_y(x)\,dx+g_y(1)-g_y(y).
\]

All terms are elementary. One obtains exactly

\[
\int_1^y g_y(x)\,dx=2\log y-3+{3\over s},
\]

and consequently

\[
\boxed{
\sum_{n=1}^{N}g_y(n)
\ge
h(y):=\log y-1-{1\over2\sqrt y}+{3\over2y}.
}
\tag{L-98010.5}
\]

Now `h(3)>0`, and

\[
h'(y)={1\over y}+{1\over4y^{3/2}}-{3\over2y^2}>0
\qquad(y\ge3).
\]

Thus the unit-weight sum in (L-98010.5) is strictly positive for every `N>=2`.

## 3. The exceptional dictionary entries improve the inequality

For `N>=4`, compare `q_*` with the constant dictionary `6`. The correction is

\[
-6g_y(1)+9g_y(2)-3g_y(4)
=
\left({15\over2}-{9\over\sqrt2}\right)c(y)
+\left({9\over\sqrt2}-3\right)\log2.
\tag{L-98010.6}
\]

Both coefficients are positive, and `c(y)>0` for `y>=5`. Therefore

\[
\sum_{n\le N}q_*(n)g_y(n)>0
\qquad(N\ge4).
\]

For `N=2`, `B_N/A_N=log 2>c(3)`. For `N=3`, the weighted average `B_N/A_N` is larger than `log 2>c(4)`. This proves (L-98010.4) for every cell, hence strict increase on `(2,infinity)`.

At every integer knot the newly entering logarithmic hinge has value zero, so `Q_*`, `T`, and `vartheta` are continuous. The cell theorem therefore gives global strict order.

Finally, elementary integral comparison gives

\[
Q_*(Y)=24\sqrt Y+O(\log Y),
\qquad
T(Y)=4\sqrt Y-3,
\]

so `vartheta(Y)->6`. This completes the proof.

## Consequence for source ordering

For any fixed real endpoint `X`, an atom indexed by `k` has ratio

\[
{r_X(k)\over t_X(k)}
={Q_*(X/k)\over T(X/k)}
=\vartheta(X/k).
\]

Hence the Lorenz ratios are ordered exactly in the opposite direction to the source index: smaller `k` has larger ratio. Every Lorenz threshold is therefore one arithmetic cutoff, not an arbitrary subset of atoms.
