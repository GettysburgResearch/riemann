# L-105431 — Real Xi critical zeros give cofinal subexponential good sides

Claim ID: `L-105431`  
Status: **PROVED CONDITIONAL GROWTH THEOREM — ASSUMES THE COMPLETE CRITICAL-POINT REALITY AT ONE RUNG; INDEPENDENT REVIEW REQUESTED**  
Created: 2026-08-24  
Depends on: `L-105430`; the standard fixed-strip growth of completed zeta  
RH status: **not assumed**

## 1. Statement

Fix `r>=0` and put

\[
F=\Xi^{(r)},
\qquad
G=F'=\Xi^{(r+1)},
\qquad
m={F\over G}.
\]

Assume that every zero of `G` is real. Fix any `H>=H_r`, where `H_r` is the
safe height from `L-105430`.

Then there is a cofinal sequence `X_n->infinity`, avoiding the zeros of `G`,
such that

\[
\boxed{
\sup_{0\le y\le H}
\left(
|m(X_n+iy)|+|m(-X_n+iy)|
\right)
\le
\exp\!\left(C_{r,H}\log X_n\log\log(3+X_n)\right).
}
\tag{L-105431.1}
\]

In particular,

\[
\boxed{
\log^+
\sup_{0\le y\le H}|m(\pm X_n+iy)|
=o(X_n).
}
\tag{L-105431.2}
\]

This is the exact growth scale needed by the finite-strip Lindelof argument in
`L-105432`.

## 2. Fixed-strip upper and safe-line lower bounds

For every fixed derivative order and fixed vertical strip, the functional
equation, the polynomial vertical-strip bound for zeta and its fixed
derivatives, and Stirling give

\[
\boxed{
|F(x+iy)|
\le
C_{r,H}
 e^{-\pi|x|/4}(2+|x|)^{A_{r,H}}
\qquad(0\le y\le H).
}
\tag{L-105431.3}
\]

At the safe line `y=H`, the Bell-polynomial estimate of `L-105430` also gives
a matching lower bound

\[
\boxed{
|G(x+iH)|
\ge
c_{r,H}
 e^{-\pi|x|/4}(2+|x|)^{-B_{r,H}}
}
\tag{L-105431.4}
\]

for all sufficiently large `|x|`. The displayed powers are deliberately
lossy; only their polynomial nature matters.

A direct derivation of (L-105431.4) is obtained in the coordinate
`s=1/2+H-ix`: the Euler product bounds `|zeta(s)|` above and away from zero,
Stirling gives the gamma factor, and

\[
\xi^{(r+1)}(s)=\xi(s)L(s)^{r+1}(1+o(1)).
\]

## 3. Local zero count

For fixed `r`, there is a constant `C_r` such that

\[
\boxed{
\#\{\gamma:G(\gamma)=0,\ |\gamma-X|\le1\}
\le C_r\log(3+X).
}
\tag{L-105431.5}
\]

One self-contained proof uses Jensen's formula in a fixed-radius disk centered
at a safe point `X-iA_r`. The disk contains the unit neighbourhood of `X` on
the real axis. Its maximum is bounded by the fixed-strip version of
(L-105431.3), while its center value has the safe-line lower bound
(L-105431.4). The common factor `exp(-pi X/4)` cancels, leaving `O_r(log X)`.

The same argument in translated fixed-radius disks gives, for every integer
`j>=0`,

\[
\#\{\gamma:j\le|X-\gamma|<j+1\}
\ll_r \log(3+X+j).
\tag{L-105431.6}
\]

## 4. Cofinal sides separated from every nearby zero

Apply (L-105431.5) to `[N-1,N+2]`. Removing intervals of radius

\[
{c_r\over\log(3+N)}
\]

around all zeros in this three-unit interval still leaves a point in
`[N,N+1]` when `c_r` is sufficiently small. Choose such a point `X_N`. Then

\[
\boxed{
\operatorname{dist}(X_N,Z(G))
\ge {c_r\over\log(3+X_N)}.
}
\tag{L-105431.7}

Parity gives the same separation at `-X_N`.

## 5. Product comparison down the vertical side

Because `G` has order one, definite parity and only real zeros, its paired
Hadamard product has no nonconstant exponential factor:

\[
\boxed{
G(z)=Cz^\varepsilon
\prod_{\gamma>0}
\left(1-{z^2\over\gamma^2}\right),
}
\tag{L-105431.8}
\]

with local uniform convergence and multiplicities retained. The possible
linear exponential is excluded by parity, and a quadratic exponential is
excluded by order one.

Equivalently, summing over all nonzero real zeros, for `0<=y<=H`,

\[
\begin{aligned}
\log { |G(X+iy)|\over|G(X+iH)| }
={}&{\varepsilon\over2}
\log {X^2+y^2\over X^2+H^2}\\
&+{1\over2}
\sum_{G(\gamma)=0}
\log { (X-\gamma)^2+y^2
       \over
       (X-\gamma)^2+H^2 }.
\end{aligned}
\tag{L-105431.9}
\]

The right side is smallest at `y=0`. Therefore

\[
\log { |G(X+iy)|\over|G(X+iH)| }
\ge
-C_H
-{1\over2}
\sum_{G(\gamma)=0}
\log\left(1+{H^2\over(X-\gamma)^2}\right).
\tag{L-105431.10}
\]

For `X=X_N`, the zeros with `|X-gamma|<1` contribute

\[
O_{r,H}(\log X\log\log X)
\]

by (L-105431.5) and (L-105431.7). On the shell
`j<=|X-gamma|<j+1`, `j>=1`, use

\[
\log(1+H^2/j^2)\ll_H j^{-2}
\]

and (L-105431.6). Summation gives only `O_(r,H)(log X)` from all remaining
zeros. Hence

\[
\boxed{
|G(X_N+iy)|
\ge
|G(X_N+iH)|
\exp\!\left[-C_{r,H}\log X_N\log\log(3+X_N)\right]
}
\tag{L-105431.11}
\]

uniformly for `0<=y<=H`.

Combining (L-105431.3), (L-105431.4) and (L-105431.11) proves
(L-105431.1). The negative side follows by parity and conjugation.

## 6. Scope

The theorem does not assume the residue signs and does not prove that the
critical zeros are real. It says that, once critical-point reality is supplied,
the quotient cannot carry an exponentially large side boundary through a
fixed physical strip.

The use of a cofinal good-side sequence is load bearing. No uniform bound on
every vertical line is claimed or required.
