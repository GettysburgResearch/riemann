# L-98000 — The unsieved `5:3` scalar-to-target ratio is globally ordered

Claim ID: `L-98000`  
Status: **PROVED UNCONDITIONAL ANALYTIC THEOREM**  
Created: 2026-08-18  
Frozen base: PR #596 at `40bfd7e70521f4205e95d3960812a6cef6073c05`  
RH status: **not assumed**

Put

\[
T(Y)=(4\sqrt Y-3)\mathbf 1_{Y\ge1}
\]

and let the positive unsieved scalar be

\[
Q_*(Y)=\sum_{m\ge1}{q_*(m)\over\sqrt m}\log(Y/m)_+,
\]

where

\[
q_*(1)=0,\quad q_*(2)=15,\quad q_*(3)=6,\quad
q_*(4)=3,\quad q_*(m)=6\ (m\ge5).
\]

Define

\[
\rho_*(Y)={Q_*(Y)\over T(Y)}\qquad(Y\ge1).
\]

Then

\[
\boxed{
\rho_*(Y)=0\quad(1\le Y\le2),
\qquad
\rho_*\text{ is strictly increasing on }(2,\infty),
\qquad
\lim_{Y\to\infty}\rho_*(Y)=6.
}
\tag{L-98000.1}
\]

In particular,

\[
\boxed{0\le Q_*(Y)<6T(Y)\qquad(Y\ge1).}
\tag{L-98000.2}
\]

## 1. Cell derivative

On an activation cell `N<Y<N+1`, write

\[
A_N=\sum_{m\le N}{q_*(m)\over\sqrt m},
\qquad
B_N=\sum_{m\le N}{q_*(m)\log m\over\sqrt m}.
\]

Then

\[
Q_*(Y)=A_N\log Y-B_N.
\]

Differentiating with respect to `log Y` gives

\[
T(Y)^2{d\over d\log Y}{Q_*(Y)\over T(Y)}
=A_NT(Y)-2\sqrt Y\,Q_*(Y)=:G_N(Y).
\tag{L-98000.3}
\]

If `s=sqrt(Y)`, then

\[
G_N(s)=A_N(4s-3)-2s(2A_N\log s-B_N),
\]

and

\[
{d^2\over ds^2}G_N(s)=-{4A_N\over s}<0.
\tag{L-98000.4}
\]

Thus `G_N` is concave on every cell and its minimum is attained at an endpoint.
At an activation knot,

\[
G_N(N)=G_{N-1}(N)+{q_*(N)\over\sqrt N}T(N),
\tag{L-98000.5}
\]

so the right derivative jumps upward. It is therefore enough on a finite range
to certify the right cell endpoints `G_N(N+1)`.

## 2. Analytic tail

For `N>=4`, the exceptional coefficients give

\[
A_N=6\sum_{m\le N}m^{-1/2}-{15\over2}+{9\over\sqrt2}.
\tag{L-98000.6}
\]

The elementary decreasing-sum bounds

\[
2(\sqrt{N+1}-1)
\le\sum_{m\le N}m^{-1/2}
\le2\sqrt N-1
\]

imply, with

\[
c={27\over2}-{9\over\sqrt2},
\qquad
d={39\over2}-{9\over\sqrt2},
\]

that for `N<=Y<N+1`,

\[
12\sqrt Y-d<A_N\le12\sqrt Y-c.
\tag{L-98000.7}
\]

For `Y>=4`, integration of the upper bound gives

\[
Q_*(Y)
\le24\sqrt Y-c\log Y+C,
\tag{L-98000.8}
\]

where

\[
C=Q_*(4)-48+c\log4,
\]

\[
Q_*(4)={15\over\sqrt2}\log2
       +{6\over\sqrt3}\log{4\over3}.
\]

Substitution in (L-98000.3) yields

\[
G_N(Y)
\ge
\sqrt Y\,[2c\log Y-K]+3d,
\tag{L-98000.9}
\]

with

\[
K=36+4d+2C.
\]

The retained directed constant certificate proves

\[
2c\log8-K
>0.6515026909363199.
\tag{L-98000.10}
\]

Hence `G_N(Y)>0` for every `Y>=8`.

For the six remaining right endpoints `N=2,...,7`, the same directed replay
proves respectively

```text
G_2(3) > 26.76
G_3(4) > 36.95
G_4(5) > 39.68
G_5(6) > 49.86
G_6(7) > 59.93
G_7(8) > 69.86.
```

Concavity and the upward knot jumps now prove strict monotonicity on `(2,infinity)`.

## 3. Limit

Integrating both sides of (L-98000.7) gives

\[
Q_*(Y)=24\sqrt Y+O(\log Y).
\]

Since `T(Y)=4sqrt(Y)+O(1)`, the ratio tends to six. Strict monotonicity then
forces the strict upper bound in (L-98000.2).

## Consequence for hinges

For every `0<lambda<6` there is a unique `Y_lambda>2` such that

\[
Q_*(Y)-\lambda T(Y)
\begin{cases}
<0,&1\le Y<Y_\lambda,\\
=0,&Y=Y_\lambda,\\
>0,&Y>Y_\lambda.
\end{cases}
\tag{L-98000.11}
\]

For `lambda>=6` the positive part vanishes identically. Thus every scalar Lorenz
hinge is a one-switch arithmetic threshold rather than an arbitrary atom order.