# L-105312 — A Cauchy-power jet model has enough effective-rank reserve

Claim ID: `L-105312`  
Status: **PROVED ABSTRACT TOEPLITZ THEOREM + ELEMENTARY MODEL LIMIT**  
Created: 2026-08-23  
RH status: **not assumed**

## 1. Abstract Toeplitz reserve

Let `G_J` be a positive semidefinite Hermitian Toeplitz matrix with diagonal
one. Suppose its normalized correlations satisfy

\[
|r_k|^2\le q^{k^2}
\qquad(k\ge1),
\qquad 0<q\le\frac1{50}.
\tag{L-105312.1}
\]

Then

\[
\frac{\|G_J\|_{\rm HS}^2}{J}
\le 1+2\sum_{k\ge1}q^{k^2}
\le1+\frac{2q}{1-q}
\le\frac{51}{49}.
\]

Since `tr G_J=J`, its normalized effective rank satisfies

\[
\boxed{
\frac{(\operatorname{tr}G_J)^2}
{J\|G_J\|_{\rm HS}^2}
\ge\frac{49}{51}.
}
\tag{L-105312.2}

## 2. An exact positive Cauchy-power model

Fix `eta>0`, put

\[
h_L=\frac{2\pi}{L},
\qquad
Q_L=2\left\lceil\frac15\eta^2L^2\right\rceil-1,
\]

and take a polynomially growing number `J_L` of grid points `x_j=jh_L`.
Define

\[
\boxed{
(G_L)_{jk}
=
\left(
\frac{2i\eta}{x_j-x_k+2i\eta}
\right)^{Q_L}.
}
\tag{L-105312.3}

This is positive semidefinite. Indeed, up to a positive normalization,

\[
(2\eta-i(x_j-x_k))^{-Q_L}
=
\frac1{\Gamma(Q_L)}
\int_0^\infty
u^{Q_L-1}e^{-2\eta u}e^{iu(x_j-x_k)}\,du,
\]

so `G_L` is a Gram matrix of exponential vectors against a positive gamma
measure.

Its squared normalized correlation at displacement `k` is exactly

\[
|r_{k,L}|^2
=
\left(
1+\frac{h_L^2k^2}{4\eta^2}
\right)^{-Q_L}.
\tag{L-105312.4}

For every fixed `k`,

\[
|r_{k,L}|^2
\longrightarrow
\exp\!\left(-\frac{2\pi^2}{5}k^2\right).
\tag{L-105312.5}

A standard two-range estimate makes the convergence summable: for
`k<=delta L`, use the uniform Taylor lower bound for `log(1+x)`; for
`k>delta L`, (L-105312.4) is exponentially small in `L^2`, while `J_L` grows
only polynomially. Therefore

\[
\frac{\|G_L\|_{\rm HS}^2}{J_L}
\longrightarrow
\Theta
:=
\sum_{k\in\mathbb Z}
\exp\!\left(-\frac{2\pi^2}{5}k^2\right).
\tag{L-105312.6}

Since `exp(-2 pi^2/5)<1/50`,

\[
\Theta
<1+2\sum_{k\ge1}50^{-k}
=\frac{51}{49}.
\]

Consequently

\[
\boxed{
\liminf_{L\to\infty}
\frac{(\operatorname{tr}G_L)^2}
{J_L\|G_L\|_{\rm HS}^2}
\ge\frac{49}{51}.
}
\tag{L-105312.7}

The model is purely archimedean. It proves that localization geometry itself
has ample reserve; it is not asserted to equal the arithmetic Xi matrix.

## 3. One-percent perturbation still exceeds the record target

Let `K_J` be Hermitian and suppose, relative to a model satisfying
(L-105312.2),

\[
\operatorname{tr}K_J\ge\frac{99}{100}\operatorname{tr}G_J,
\qquad
\|K_J\|_{\rm HS}\le\frac{101}{100}\|G_J\|_{\rm HS}.
\tag{L-105312.8}

Then

\[
\boxed{
\frac{(\operatorname{tr}K_J)_+^2}
{J\|K_J\|_{\rm HS}^2}
\ge
\frac{49}{51}\left(\frac{99}{101}\right)^2
=
\frac{160083}{173417}
>\frac{919}{1000}.
}
\tag{L-105312.9}

Thus a source-faithful evaluation of a growing Xi Pick compression within one
percent of the Cauchy-power gamma carrier would clear the robust threshold of
`T-105310`.

## 4. Scope

The theorem does not prove the one-percent comparison for the arithmetic Xi
kernel. It turns that comparison into a concrete trace and Hilbert--Schmidt
prime-side target with substantial numerical reserve.
