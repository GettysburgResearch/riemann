# L-98013 — The even zero-scalar band dominates the complete signed target asymptotically

Claim ID: `L-98013`  
Status: **PROVED UNCONDITIONAL ASYMPTOTIC THEOREM**  
Created: 2026-08-18  
Inputs: the prime number theorem in the equivalent form `M(x)=o(x)`; the elementary squarefree counting theorem  
RH status: **not assumed**

The completed factor-67 owner ledger indexes every squarefree integer exactly once: primes at most `61` belong to the finite colour and primes at least `67` belong to the rough history. Thus at the root we may write the target with the ordinary Möbius function.

Put

\[
t_X(k)={1\over\sqrt k}T(X/k),
\qquad
T(Y)=(4\sqrt Y-3)\mathbf 1_{Y\ge1},
\]

and define the complete signed target

\[
\mathcal T_X=\sum_{k\le X}\mu(k)t_X(k).
\tag{L-98013.1}
\]

Let the even zero-scalar band be

\[
\mathcal Z_X
=\sum_{\substack{X/2\le k\le X\\\mu(k)=+1}}t_X(k).
\tag{L-98013.2}
\]

Then

\[
\boxed{
\mathcal T_X=o(\sqrt X),
\qquad
\mathcal Z_X\gg\sqrt X,
}
\tag{L-98013.3}
\]

and therefore

\[
\boxed{
\mathcal T_X\le\mathcal Z_X
}
\tag{L-98013.4}
\]

for every sufficiently large `X`.

## 1. The signed target is sub-main-scale

Expanding `T` gives exactly

\[
\mathcal T_X
=4\sqrt X\sum_{k\le X}{\mu(k)\over k}
-3\sum_{k\le X}{\mu(k)\over\sqrt k}.
\tag{L-98013.5}
\]

The prime number theorem gives

\[
M(x)=\sum_{n\le x}\mu(n)=o(x).
\]

Partial summation then yields

\[
\sum_{k\le X}{\mu(k)\over k}=o(1),
\qquad
\sum_{k\le X}{\mu(k)\over\sqrt k}=o(\sqrt X).
\]

Substitution in (L-98013.5) proves the first assertion of (L-98013.3).

## 2. The zero-scalar even band has square-root mass

Restrict (L-98013.2) to

\[
X/2\le k\le3X/4.
\]

On this interval `1<=X/k<=2`, so `Q_*(X/k)=0`; every such atom is genuinely zero-scalar. Also

\[
T(X/k)\ge T(4/3)={8\over\sqrt3}-3=:c_0>0,
\qquad
k^{-1/2}\ge X^{-1/2}.
\]

The indicator of positive squarefree parity is

\[
\mathbf 1_{\mu(k)=+1}={\mu(k)^2+\mu(k)\over2}.
\]

Using

\[
\sum_{n\le x}\mu(n)^2={6\over\pi^2}x+O(\sqrt x)
\]

and `M(x)=o(x)`, the number of `k` in `[X/2,3X/4]` with `mu(k)=+1` is

\[
{3\over4\pi^2}X+o(X).
\]

Consequently

\[
\mathcal Z_X
\ge {c_0\over\sqrt X}
\left({3\over4\pi^2}X+o(X)\right)
\gg\sqrt X.
\]

This completes the proof.

## Consequence for `ZMTS67`

By `L-98011`, the upper half of the zero-marginal sandwich is

\[
\mathcal T_X\le\mathcal Z_X.
\]

`L-98013` proves it unconditionally for all sufficiently large endpoints. Thus asymptotically

\[
\boxed{
\mathrm{ZMTS67}
\iff
\mathcal T_X\ge0.
}
\tag{L-98013.6}
\]

The only surviving zero-marginal target obstruction is the sign of the complete signed target itself.
