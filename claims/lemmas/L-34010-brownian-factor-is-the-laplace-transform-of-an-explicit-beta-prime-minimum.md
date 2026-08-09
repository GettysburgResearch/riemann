# L-34010 — The finite Brownian factor is the Laplace transform of an explicit beta-prime minimum

Claim ID: `L-34010`

Status: **PROPOSED COMPLETE EXACT PROBABILITY / MELLIN THEOREM — INDEPENDENT REVIEW REQUESTED**

Created: 2026-08-09

Dependencies: `L-34001`, `L-34007`

Scope: exact order-statistic representation of the finite raw Brownian factor in its genuine moment strip; no zero-free theorem and no RH claim

## 1. Rational sine-tail profile

Put

\[
\Phi_N(t)
=\prod_{k=1}^N\left(1+\frac{t^2}{k^2}\right)^{-2},
\qquad t>0.
\tag{L-34010.1}
\]

By the serial-exponential representation `L-34008`, this is exactly the Laplace transform of

\[
S_N=\sum_{j=1}^N\Gamma_{2,j}/j^2:
\]

\[
\boxed{
\Phi_N(t)=\mathbb E[e^{-t^2S_N}].
}
\tag{L-34010.2}
\]

Introduce logarithmic scale

\[
t=e^u
\]

and the decreasing profile

\[
\boxed{
R_N(u)=\Phi_N(e^u)
=\prod_{k=1}^N
\left(1+\frac{e^{2u}}{k^2}\right)^{-2}.
}
\tag{L-34010.3}
\]

It decreases strictly from one to zero.

## 2. R_N is the survival function of an explicit minimum

Let `Y_1,...,Y_N` be independent random variables with beta-prime `(1,2)` law

\[
\boxed{
\mathbb P(Y_k>y)=(1+y)^{-2},
\qquad
f_Y(y)=\frac{2}{(1+y)^3},
\quad y>0.
}
\tag{L-34010.4}
\]

Define

\[
\boxed{
U_k=\log k+\frac12\log Y_k
}
\tag{L-34010.5}
\]

and

\[
\boxed{
M_N=\min_{1\le k\le N}U_k.
}
\tag{L-34010.6}
\]

Then

\[
\begin{aligned}
\mathbb P(U_k>u)
&=\mathbb P(Y_k>e^{2u}/k^2)\\
&=\left(1+\frac{e^{2u}}{k^2}\right)^{-2}.
\end{aligned}
\]

Independence therefore gives exactly

\[
\boxed{
\mathbb P(M_N>u)=R_N(u).
}
\tag{L-34010.7}
\]

Thus

\[
\boxed{
g_N(u):=-R_N'(u)}
\tag{L-34010.8}
\]

is the probability density of `M_N`.

## 3. Explicit hazard

Logarithmic differentiation of (L-34010.3) gives

\[
\boxed{
 h_N(u)
 :=\frac{g_N(u)}{R_N(u)}
 =4\sum_{k=1}^N
 \frac{e^{2u}}{k^2+e^{2u}}.
}
\tag{L-34010.9}
\]

Moreover

\[
\boxed{
 h_N'(u)
 =8\sum_{k=1}^N
 \frac{k^2e^{2u}}{(k^2+e^{2u})^2}>0.
}
\tag{L-34010.10}
\]

Hence `M_N` has a strictly increasing hazard rate.  This property is exact and uniform in `N`.

The tails are also explicit:

```text
u -> -infinity:  g_N(u)=Theta(e^(2u));

u -> +infinity:  g_N(u)=Theta(e^(-4Nu)).
```

Therefore its bilateral Laplace transform exists throughout

\[
\boxed{-2N<\Re z<1}
\tag{L-34010.11}
\]

for the parameterization used below.

## 4. Mellin transform of the survival profile

For `-2N<Re z<0`, ordinary Mellin/Laplace exchange gives

\[
\begin{aligned}
J_N(z)
&:=\int_0^\infty
 t^{-1-2z}\Phi_N(t)\,dt\\
&=\int_{-\infty}^{\infty}
 e^{-2zu}R_N(u)\,du\\
&=\frac12\Gamma(-z)\mathbb E[S_N^z].
\end{aligned}
\tag{L-34010.12}
\]

Integrating by parts in `u` and using the endpoint decay gives

\[
\begin{aligned}
\mathbb E[e^{-2zM_N}]
&=\int_{-\infty}^{\infty}e^{-2zu}g_N(u)\,du\\
&=-2zJ_N(z)\\
&=\Gamma(1-z)\mathbb E[S_N^z].
\end{aligned}
\tag{L-34010.13}
\]

Both sides are analytic on the common genuine moment strip, so the identity extends to

\[
\boxed{-2N<\Re z<1.}
\tag{L-34010.14}
\]

No analytic continuation beyond an expectation is required there.

## 5. Exact Brownian factorization

By `L-34001`,

\[
D_N(2z)
=\frac{\mathbb E[S_N^z]}{\Gamma(1+z)}.
\tag{L-34010.15}
\]

Euler reflection gives

\[
\Gamma(1-z)\Gamma(1+z)
=\frac{\pi z}{\sin\pi z}.
\tag{L-34010.16}
\]

Combining (L-34010.13)--(L-34010.16),

\[
\boxed{
D_N(2z)
=\frac{\sin\pi z}{\pi z}
\mathbb E[e^{-2zM_N}]
}
\tag{L-34010.17}
\]

throughout the strip (L-34010.14), with removable interpretation at `z=0` and at the integer cancellation points.

## 6. The RH-facing strip is now an honest probability problem

The nontrivial zeta-zero region consumed by `L-34001` is

\[
\frac14<\Re z<\frac12.
\]

This lies strictly inside the genuine moment strip (L-34010.14), and the elementary factor

\[
\frac{\sin\pi z}{\pi z}
\]

has no zero there.  Therefore

\[
\boxed{
D_N(2z)\ne0
\iff
\mathbb E[e^{-2zM_N}]\ne0
\qquad
\left(\frac14<\Re z<\frac12\right).
}
\tag{L-34010.18}
\]

Thus finite Brownian RH stability is exactly a bilateral-Laplace minimum-phase problem for the explicit order statistic `M_N`.

No B-spline, divided-difference, gamma-prefactor, or meromorphic continuation remains in this formulation.

## 7. Critical tilt

Put

\[
z=\frac14+w.
\]

Define the critical Esscher tilt

\[
\boxed{
 d\nu_N(u)
 =\frac{e^{-u/2}g_N(u)\,du}
 {\mathbb E[e^{-M_N/2}]}.
}
\tag{L-34010.19}
\]

Then

\[
\boxed{
\frac{D_N(1/2+2w)}{D_N(1/2)}
=\frac{\sin\pi(1/4+w)}{\sin(\pi/4)}
 \frac{1/4}{1/4+w}
 \mathbb E_{\nu_N}[e^{-2wM_N}]
}
\tag{L-34010.20}
\]

where the elementary prefactor is zero-free for

\[
0<\Re w<1/4.
\]

Consequently the exact finite target may be stated as:

> prove that the critically tilted minimum `nu_N` has a zero-free bilateral Laplace transform in `0<Re w<1/4`, cofinally in `N`.

This form makes the special role of the quarter shift intrinsic.

## 8. Proof boundary

Closed exactly:

1. rational sine-tail profile;
2. representation as the survival function of a minimum of independent shifted beta-prime variables;
3. explicit strictly increasing hazard;
4. complete genuine moment strip;
5. exact Laplace/Mellin identity;
6. exact factorization of `D_N` by the minimum transform;
7. critical Esscher-tilt formulation.

Open:

1. minimum-phase theorem for the critically tilted order statistic;
2. cofinal Brownian stability;
3. RH.
