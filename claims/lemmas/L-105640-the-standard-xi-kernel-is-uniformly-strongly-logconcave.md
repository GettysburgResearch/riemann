# L-105640 — The standard Xi kernel is uniformly strongly log-concave

Claim ID: `L-105640`  
Status: **PROVED UNCONDITIONALLY BY AN EXPLICIT THETA-MIXTURE BOUND; INDEPENDENT REVIEW REQUESTED**  
Created: 2026-08-25  
Depends on: `L-105626`  
RH status: **not assumed**

## 1. Statement

Let `Phi` be the standard positive even Fourier kernel of the Riemann Xi
function. Then

\[
\boxed{
-(\log\Phi)''(u)
>{20476\over2345}>8
\qquad(u\in\mathbb R).
}
\tag{L-105640.1}
\]

Thus the source theorem of `L-105626` is not merely strict log-concavity: the
standard Xi kernel has a uniform strong-log-concavity constant exceeding
`8`.

This is a theorem about the Fourier source. It is not a total-positivity or
Laguerre--Pólya theorem and does not imply RH by itself.

## 2. Theta summands and their scores

For `u>=0`, use the standard positive theta expansion

\[
\Phi(u)=4\sum_{n\ge1}\phi_n(u),
\]

\[
\phi_n(u)
=\pi e^{5u/2}n^2(2xn^2-3)e^{-xn^2},
\qquad
x=\pi e^{2u}\ge\pi>3.
\tag{L-105640.2}
\]

Put

\[
a_n=(\log\phi_n)',
\qquad
b_n=(\log\phi_n)''.
\]

The exact formulas retained from `L-105626` are

\[
a_n={9\over2}-2xn^2+{6\over2xn^2-3},
\tag{L-105640.3}
\]

\[
b_n=-4xn^2-{24xn^2\over(2xn^2-3)^2}<0.
\tag{L-105640.4}
\]

In particular,

\[
\boxed{-b_1>4x.}
\tag{L-105640.5}
\]

Let

\[
p_n={\phi_n\over\sum_m\phi_m}.
\]

The positive-mixture identity is

\[
\boxed{
(\log\Phi)''
=\sum_np_nb_n+\operatorname{Var}_p(a_n).
}
\tag{L-105640.6}
\]

## 3. The first theta orbit has mass greater than `200/201`

`L-105626` proves

\[
{\phi_n\over\phi_1}
\le2n^4e^{-x(n^2-1)}.
\tag{L-105640.7}
\]

For `n=2`, using `x>=pi>3` and the elementary Taylor inequality `e^3>20`,

\[
2\cdot2^4e^{-3x}
<32e^{-9}
<{1\over250}.
\tag{L-105640.8}
\]

For `n>=3`, replace `x` by `3`. The first term satisfies

\[
2\cdot3^4e^{-24}
<{1\over10^6},
\]

and the ratio of consecutive terms is at most

\[
\left({4\over3}\right)^4e^{-21}
< {4\over20^7}<10^{-8}.
\]

Therefore

\[
2\sum_{n\ge3}n^4e^{-x(n^2-1)}
<{1\over1000}.
\tag{L-105640.9}
\]

Combining (L-105640.8)--(L-105640.9),

\[
\sum_{n\ge2}{\phi_n\over\phi_1}
<{1\over200},
\]

and hence

\[
\boxed{p_1>{200\over201}.}
\tag{L-105640.10}
\]

## 4. A quantitative curvature surplus

Variance is minimized at its mean, so it is bounded by the squared distance
to the first score:

\[
\operatorname{Var}_p(a_n)
\le
\sum_{n\ge2}p_n(a_n-a_1)^2
=p_1\sum_{n\ge2}{\phi_n\over\phi_1}(a_n-a_1)^2.
\tag{L-105640.11}
\]

The explicit tail ledger in `L-105626` gives the sharper retained numerical
form

\[
\boxed{
\sum_{n\ge2}{\phi_n\over\phi_1}(a_n-a_1)^2
<4x\,{1881\over7000}.
}
\tag{L-105640.12}
\]

All `-b_n` are positive, so (L-105640.5)--(L-105640.12) yield

\[
\begin{aligned}
-(\log\Phi)''
&=-\sum_np_nb_n-\operatorname{Var}_p(a_n)\\
&>p_1\,4x\left(1-{1881\over7000}\right).
\end{aligned}
\tag{L-105640.13}
\]

Now

\[
1-{1881\over7000}={5119\over7000},
\qquad
p_1>{200\over201},
\qquad
x>3.
\]

Consequently

\[
-(\log\Phi)''
>
{200\over201}\,12\,{5119\over7000}
={20476\over2345}
=8+{1716\over2345}>8.
\tag{L-105640.14}
\]

This proves (L-105640.1) on `[0,infinity)`. Evenness and smoothness of the
standard kernel give the same inequality on the negative half-line and at the
origin.

## 5. Consequences available without RH

The probability density proportional to `Phi` is uniformly strongly
log-concave. Standard one-dimensional consequences such as a Poincare bound,
subgaussian concentration after normalization, and stability of positive
tilts may therefore be invoked with an explicit source constant, provided the
normalization and hypotheses of the chosen theorem are stated.

The project-specific immediate use is more modest: the monotone
current--Turan profile of `L-105624` now has an explicit, uniformly curved
producer rather than a merely qualitative log-concavity input.

## 6. Scope and falsifiers

The proof is falsified by an error in any of:

```text
the score/curvature formulas (L-105640.3)--(L-105640.4);
the first-orbit mass bound (L-105640.10);
the retained score-variance ledger (L-105640.12);
the exact rational calculation 20476/2345>8.
```

Ordinary or strong log-concavity is only a second-order source property. No
claim is made that it implies `TP_infinity`, that every Fourier transform of a
strongly log-concave function is real-rooted, or that RH follows.