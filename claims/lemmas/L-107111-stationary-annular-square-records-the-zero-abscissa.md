# L-107111 — The stationary annular square records the exact zero abscissa

**Claim ID:** `L-107111`  
**Status:** unconditional quantitative detector theorem  
**Date:** 2026-08-31  
**Depends on:** `L-107110`, `L-106800`, `L-107100`  
**RH:** unproved

Fix `q=67` and write

\[
\mu_q(n)=\mu(n)\mathbf1_{q\nmid n},
\qquad
A_q(Y)=\sum_{n\le Y}{\mu_q(n)\over\sqrt n},
\]

\[
\mathfrak M_q(X)=\max_{Y\le X}|A_q(Y)|.
\]

For each `Y`, apply `L-107110` to

\[
a_n={\mu_q(n)\over\sqrt n}\mathbf1_{n\le Y}
\]

and put

\[
\mathfrak Q_q(X)=\max_{Y\le X}\mathcal Q_q(a).
\]

If

\[
N_q(X)=2+\lceil\log_qX\rceil,
\]

then

\[
\boxed{
{\mathfrak M_q(X)^2\over N_q(X)}
\le \mathfrak Q_q(X)
\le4N_q(X)\mathfrak M_q(X)^2.
}
\tag{L-107111.1}
\]

The proof is purely deterministic: the upper bound uses that every band sum
is a difference of two prefixes; the lower bound chooses a maximizing prefix
and applies Cauchy to its partition into shifted bands.

Let

\[
\Theta=\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}.
\]

The half-weight and finite-Euler transport in `L-106800` gives

\[
\operatorname{pexp}\mathfrak M_q=\Theta-{1\over2}.
\]

Since `N_q(X)=X^{o(1)}`, (L-107111.1) proves

\[
\boxed{
\limsup_{X\to\infty}
{\log(1+\mathfrak Q_q(X))\over\log X}
=2\Theta-1.
}
\tag{L-107111.2}
\]

Equivalently, for every `1/2<=sigma<=1`,

\[
\boxed{
\zeta(s)\ne0\quad(\Re s>\sigma)
\Longleftrightarrow
\mathfrak Q_q(X)\ll_\varepsilon X^{2\sigma-1+\varepsilon}.
}
\tag{L-107111.3}
\]

In particular,

\[
\boxed{
\mathrm{RH}
\Longleftrightarrow
\mathfrak Q_q(X)=X^{o(1)}.
}
\tag{L-107111.4}
\]

## Literal beta source

Let

\[
\beta=(\delta_1-\delta_q)^{*2}*\mu_q,
\qquad
B(Y)=\sum_{n\le Y}{\beta(n)\over\sqrt n}.
\]

With `a=q^{-1/2}`, the exact sharp-prefix identities are

\[
B(Y)=A_q(Y)-2aA_q(Y/q)+a^2A_q(Y/q^2),
\]

\[
A_q(Y)=\sum_{j\le\log_qY}(j+1)a^jB(Y/q^j).
\]

Hence

\[
(1-a)^2\max_{Y\le X}|A_q(Y)|
\le \max_{Y\le X}|B(Y)|
\le(1+a)^2\max_{Y\le X}|A_q(Y)|.
\]

Applying (L-107111.1) to either source shows that the stationary q-adic
square may be written with the literal beta coefficients or with the cleaner
q-free Möbius channel without changing its power exponent.

## Unconditional bound

The source-locked Vinogradov--Korobov Mertens estimate and Abel summation give,
for some `c>0`,

\[
\boxed{
\mathfrak Q_q(X)
\ll X\exp\left[-c(\log X)^{3/5}
(\log\log X)^{-1/5}\right].
}
\tag{L-107111.5}
\]

This is a genuine stretched-exponential saving for the exact detector, but it
is still `X^{1-o(1)}` and proves no fixed new zero-free half-plane.

## Scope

The theorem supplies a stationary fixed-kernel quantitative detector. It does
not estimate its RH-bearing high-primitive off-diagonal contribution.