# L-102953 — Squarefree Type-I is an l1 shift-transfer of the parent zero-moment lattice

Claim ID: `L-102953`  
Status: **PROVED EXACT OPERATOR TRANSFER AND POWER-SAVING BOUND**  
Created: 2026-08-25  
Depends on: `L-102880`; PR #751 `L-106080`; owner-excluded Type-I ledger  
RH status: **not assumed**

For a finite owner/exclusion set `R`, define

\[
\mathscr L_K^{(R)}(Z)
=
\sum_{(m,R)=1}\frac1m K_L(Z/m^2),
\]

and its squarefree restriction

\[
\mathscr L_{K,\rm sf}^{(R)}(Z)
=
\sum_{\substack{\mu^2(m)=1\\(m,R)=1}}
\frac1m K_L(Z/m^2).
\]

The squarefree-divisor identity gives the exact operator formula

\[
\boxed{
\mathscr L_{K,\rm sf}^{(R)}
=
\sum_{\substack{k\ge1\\(k,R)=1}}
\frac{\mu(k)}{k^2}
S_{k^4}\mathscr L_K^{(R)},
}
\tag{L-102953.1}
\]

where

\[
(S_qf)(Z)=f(Z/q).
\]

## 1. The transfer is bounded before pointwise estimation

On logarithmic `L2`, every dilation `S_(k^4)` is an isometry. On a finite
horizon it is a contraction after restriction. Moreover

\[
\sum_{k\ge1}\frac{|\mu(k)|}{k^2}\le\zeta(2).
\]

Therefore the squarefree lattice operator is an `l1` combination of the
already-closed parent lattice operators:

\[
\boxed{
\|\mathscr L_{K,\rm sf}^{(R)}\|_{\rm op}
\le
\zeta(2)\sup_W\|\mathscr L_K^{(R)}(W)\|_{\rm op}.
}
\tag{L-102953.2}
\]

All owner, marked-`67`, gauge and regional projections commute with the
square shifts. Thus the parent Type-I source/Hilbert ledger transports without
introducing a new physical-collapse interface.

## 2. Pointwise gain

Using the parent zero-moment estimate

\[
\mathscr L_K^{(R)}(W)\ll X^{o(1)}W^{-1/2}
\]

and noting that only `k<=Z^(1/4)` can meet the compact kernel support gives

\[
\boxed{
\mathscr L_{K,\rm sf}^{(R)}(Z)
\ll X^{o(1)}Z^{-1/4}.
}
\tag{L-102953.3}

For the Boolean Type-I row with `U=Y^(1/6)`, the exact weights give

\[
\begin{aligned}
|\mathcal T_{U,\rm sf}^{K,(P)}(Y)|
&\ll
X^{o(1)}Y^{-1/4}
\left(\sum_{d\le U}d^{-1/2}\right)^2\\
&\ll
\boxed{X^{o(1)}Y^{-1/12}}.
\end{aligned}
\tag{L-102953.4}

Finite owner and Boolean-factorization multiplicities are absorbed in the
existing `X^(o(1))` ledger.

## Consequence

The first review target of `M-106080` is closed:

```text
Boolean squarefree Type-I
  -> parent owner/gauge Hilbert Type-I row
```

is an exact bounded shift transfer, not merely a pointwise analogy.

The balanced owner-indexed phase/collapse transport is different and is not
proved by this lemma.
