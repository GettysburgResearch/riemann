# L-91001 — Reverse-Bessel closure, inverse-Gaussian Poissonization, and the exact one-quarter Euler gap

Claim ID: `L-91001`  
Status: **PROPOSED COMPLETE EXACT TRANSFORM THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-90905`, `L-90906`, `T-90903`  
RH status: **unproved**

## 1. Purpose

The single-safe-line hierarchy of `T-90903` is indexed by the polynomials

\[
Q_k(t)=2^{k+1}P_k(t),
\qquad
Q_0(t)=1+t-t^2,
\qquad
Q_{k+1}=(t+2k+3)Q_k-tQ_k'.
\]

This note closes that recurrence in three different ways:

1. `Q_k` is an elementary difference of reverse Bessel polynomials;
2. Poissonizing the order `k` gives one explicit inverse-Gaussian/Gamma kernel;
3. Borel summation of the zero kernels exposes an exact analytic-continuation gap
   `u in [3/4,1)`—the only part of the Borel interval not visible by an absolutely
   convergent Euler series.

The result does not prove the sign required for RH. It converts the remaining
problem into a much more rigid Bessel/Loewner boundary problem.

## 2. Reverse Bessel identification

Define the reverse Bessel polynomial

\[
\theta_n(t)
=\sum_{j=0}^{n}
 \frac{(2n-j)!}{j!(n-j)!2^{n-j}}t^j.
\tag{L-91001.1}
\]

Its exponential generating function is

\[
\boxed{
\Theta(z,t)
:=\sum_{n\ge0}\theta_n(t)\frac{z^n}{n!}
=(1-2z)^{-1/2}
 \exp\!\bigl(t(1-\sqrt{1-2z})\bigr).
}
\tag{L-91001.2}
\]

The safe-line polynomials are exactly

\[
\boxed{
Q_k(t)=\theta_{k+1}(t)-t^2\theta_k(t).
}
\tag{L-91001.3}
\]

### Proof

Differentiate (L-91001.2):

\[
\partial_z\Theta
=\Theta\left((1-2z)^{-1}+t(1-2z)^{-1/2}\right).
\]

Consequently the exponential generating function of the right side of
(L-91001.3) satisfies the same first-order differential recurrence in `k` as
`Q_k`, with initial value `1+t-t^2`. Equivalently one may substitute
(L-91001.1) directly into the coefficient recurrence of `L-90906`.  Either
calculation proves (L-91001.3).

## 3. Closed exponential generating function

Since `P_k=2^{-k-1}Q_k`, (L-91001.2) gives

\[
\boxed{
\begin{aligned}
\mathscr P(u,t)
&:=\sum_{k\ge0}P_k(t)\frac{u^k}{k!}\\
&=\frac12(1-u)^{-1/2}
 \exp\!\bigl(t(1-\sqrt{1-u})\bigr)\\
&\quad\times
 \left[(1-u)^{-1}
 +t(1-u)^{-1/2}-t^2\right].
\end{aligned}}
\tag{L-91001.4}
\]

Put

\[
r=\sqrt{1-u}.
\]

Then the prime weight after the fixed factor `n^{-3/2}=e^{-3t/2}` is

\[
\boxed{
 e^{-3t/2}\mathscr P(u,t)
 =\frac{e^{-(1/2+r)t}}{2r^3}
   (1+rt-r^2t^2).
}
\tag{L-91001.5}
\]

The Poissonized weight has one exact positive sign boundary:

\[
1+rt-r^2t^2=0
\quad\Longleftrightarrow\quad
rt=\varphi,
\qquad
\varphi=\frac{1+\sqrt5}{2}.
\tag{L-91001.6}
\]

Thus Poissonized order `u` selects the prime-log boundary

\[
\log n=\frac{\varphi}{\sqrt{1-u}}.
\]

This is the continuous analogue of the discrete boundary
`tau_k approximately sqrt(2k)` in `L-90906`.

## 4. Inverse-Gaussian/Gamma probabilistic representation

Equation (L-91001.2) is a moment generating function. Let `G` be Gamma with
shape `1/2` and rate `1/2`, and let `I_t` be the inverse-Gaussian subordinator
specified by

\[
\mathbb E e^{zI_t}
=\exp\!\bigl(t(1-\sqrt{1-2z})\bigr),
\qquad z<1/2,
\tag{L-91001.7}
\]

independent of `G`. Put `Y_t=G+I_t`. Then

\[
\mathbb E Y_t^n=\theta_n(t)
\tag{L-91001.8}
\]

and therefore

\[
\boxed{
P_k(t)=2^{-k-1}\,
\mathbb E\bigl[Y_t^k(Y_t-t^2)\bigr].
}
\tag{L-91001.9}
\]

This is an infinite stochastic realization, not a finite Brownian Dirichlet
approximant. It therefore does not conflict with the high-frequency Bohr
instability of PR #376. It supplies a genuine bridge between the surviving
Brownian intuition and the safe-line Euler hierarchy.

## 5. Borel sum of the zero kernel

The zero kernel of `T-90903` is

\[
\kappa_k(z)
=-2(k+2)!\frac{z^2}{(1-z^2)^{k+3}}.
\]

Its exponential generating function is elementary:

\[
\boxed{
\sum_{k\ge0}\kappa_k(z)\frac{u^k}{k!}
=-\frac{4z^2}{(1-z^2-u)^3}.
}
\tag{L-91001.10}
\]

For the scalar `mathfrak S_k(x)` of `T-90903`, define

\[
\mathfrak B_x(u)
:=\sum_{k\ge0}\mathfrak S_k(x)\frac{u^k}{k!}.
\tag{L-91001.11}
\]

On every compact set avoiding the displayed cubic poles, the zero count gives
locally uniform convergence, and

\[
\boxed{
\begin{aligned}
\mathfrak B_x(u)
={}&\sum_{\gamma\in\mathbb R}
 \frac{4m_\gamma(\gamma-x)^2}
      {(1+(\gamma-x)^2-u)^3}\\
&-8\sum_{\Re\rho>1/2}m_\rho
 \Re\frac{(\rho-s_x)^2}
 {(1-(\rho-s_x)^2-u)^3}.
\end{aligned}}
\tag{L-91001.12}
\]

Under RH every summand is nonnegative for `0<=u<1`.

If RH is false and `(t,y)` is terminal in the sense of `T-90903`, then at
`x=t` its pair contributes

\[
-\frac{8my^2}{(1-y^2-u)^3},
\tag{L-91001.13}
\]

with a negative pole at

\[
u_0=1-y^2\in(3/4,1).
\tag{L-91001.14}
\]

Terminality puts the real part of every nuisance pole strictly to the right of
`u_0`; critical-line poles lie at `u>=1`. Hence the target dominates negatively
as `u` approaches `u_0` from below.

## 6. One moving radial sample

Let

\[
\mathscr X(s)=-\xi'(s)/\xi(s),
\qquad
s_x=\frac12+ix,
\qquad
r=\sqrt{1-u}.
\]

Taylor summation of the defining derivatives in `L-90905` gives

\[
\boxed{
\sum_{k\ge0}\mathcal H_k(s_x)\frac{u^k}{k!}
=\mathcal D_{1-u}\mathscr X(s_x)
}
\tag{L-91001.15}
\]

with

\[
\boxed{
\mathcal D_{r^2}\mathscr X(s_x)
=\frac{1}{2r^3}
 \left[
  \mathscr X(s_x+r)
  -r\mathscr X'(s_x+r)
  -r^2\mathscr X''(s_x+r)
 \right].
}
\tag{L-91001.16}
\]

Therefore

\[
\boxed{
\mathfrak B_x(1-r^2)
=-\Re\mathcal D_{r^2}\mathscr X(s_x).
}
\tag{L-91001.17}
\]

Every Poissonized order is thus one radial sample of the completed logarithmic
derivative, rather than an infinite formal hierarchy.

## 7. Radial curvature form

Put

\[
L_x(r)=\log\left|\xi\!\left(\frac12+r+ix\right)\right|.
\]

Where `xi` is nonzero,

\[
\Re\mathscr X=-L_x',
\qquad
\Re\mathscr X'=-L_x'',
\qquad
\Re\mathscr X''=-L_x'''.
\]

Hence

\[
\boxed{
\mathfrak B_x(1-r^2)
=\frac{1}{2r^3}\frac{d}{dr}
 \left[r\left(L_x'(r)-rL_x''(r)\right)\right].
}
\tag{L-91001.18}
\]

For a critical-line zero at ordinate `gamma`, the corresponding local summand is

\[
\frac{4(\gamma-x)^2}{(r^2+(\gamma-x)^2)^3}\ge0.
\]

Thus the Borel hierarchy is exactly a third-order radial curvature monotonicity
of `log|xi|`.

## 8. The exact one-quarter Euler gap

The prime part of (L-91001.16) is

\[
\frac1{2r^3}
\sum_{n\ge2}
\frac{\Lambda(n)}{n^{1/2+r+ix}}
\left(1+r\log n-r^2(\log n)^2\right).
\tag{L-91001.19}
\]

It converges absolutely exactly in the safe range

\[
\frac12+r>1
\quad\Longleftrightarrow\quad
r>\frac12
\quad\Longleftrightarrow\quad u<\frac34.
\tag{L-91001.20}
\]

Every possible false-RH pole lies at `u_0=1-y^2>3/4`. Therefore the complete
Borel interval splits sharply as

```text
0 <= u < 3/4   : one absolutely convergent Euler series;
3/4 <= u < 1   : the entire RH-bearing analytic-continuation gap.
```

This is not a bandwidth-one ceiling: it is a literal one-quarter interval in the
Poissonized derivative parameter. Any closing argument must transport positivity
or a Pick/Hausdorff structure across this exact gap without taking absolute
values.

## 9. Boundary

Proposed exact, pending review:

```text
reverse-Bessel identity;
closed order-EGF;
inverse-Gaussian/Gamma moment realization;
Borel cubic kernel;
one-radial-sample formula;
radial-curvature identity;
Euler boundary u=3/4 and false-RH poles in (3/4,1).
```

Not proved:

```text
positivity throughout the one-quarter gap;
Riemann Hypothesis.
```
