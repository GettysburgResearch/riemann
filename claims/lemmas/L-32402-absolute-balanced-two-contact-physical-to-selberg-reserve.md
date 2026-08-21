# L-32402 — Absolute balanced two-contact physical-to-Selberg reserve

Claim ID: `L-32402`  
Title: On every fixed balanced cone, the RH-sensitive two-contact physical carry field is dominated by the source-matched Selberg reserve with an absolute scale-independent constant  
Status: **PROPOSED COMPLETE ELEMENTARY THEOREM — INDEPENDENT REVIEW REQUIRED**  
Author: `gpt56-sol`  
Date: 2026-08-08  
Dependencies: PR #302 `L-28009/L-28012`; elementary Chebyshev central-binomial bound  
Scope: balanced interior carry positions of the exact `b_2/A_2` Dirichlet system; endpoint neighbors are handled separately by `L-28015`

## 1. Exact fields

Use the two-contact Dirichlet system

\[
A_2(s)={\zeta(s)\over1-2^{-s}},
\qquad
B_2=A_2^{-1}.
\]

Let `Lambda_2` be its nonnegative generalized von Mangoldt sequence and define

\[
P_2(n,j)=\sum_{q\le n}\Lambda_2(q)\chi_{n,q}(j),
\]

\[
S_2(n,j)=\sum_{q\le n}C_2(q)\chi_{n,q}(j),
\]

\[
R_2(n,j)=P_2(n,j)^2-S_2(n,j)\ge0.
\]

Let `q_2=B_2*Lambda_2=-B_2 log` be the RH-sensitive inverse-source current and put

\[
Q_2(n,j)=\sum_{q\le n}q_2(q)\chi_{n,q}(j).
\]

PR #302 proves the exact generalized-Chebyshev formula

\[
\boxed{
Q_2(n,j)=G_2(n)-G_2(j)-G_2(n-j),
}
\tag{L-32402.1}
\]

where

\[
G_2(x)=\Psi_2(x)-\Psi_2(x/2),
\qquad
\Psi_2(x)=\sum_{m\le x}\Lambda_2(m).
\]

It also proves, on every fixed balanced interior cone, that

\[
P_2(n,j)\ge\eta n\log2
\tag{L-32402.2}
\]

and, for all sufficiently large `n` depending only on `eta`,

\[
\boxed{
R_2(n,j)\ge{1\over2}P_2(n,j)^2.
}
\tag{L-32402.3}
\]

The previous transference theorem used the crude estimate `Psi_2(x)<<x log x`.
The new point is that `Psi_2` has an elementary linear bound.

## 2. Elementary linear Chebyshev bound

For an integer `m>=1`, every prime power in `(m,2m]` contributes to the central
binomial coefficient, and hence

\[
\psi(2m)-\psi(m)
\le\log {2m\choose m}
\le2m\log2.
\tag{L-32402.4}
\]

For any real `x>=2`, choose `K` with

\[
2^{K-1}<x\le2^K.
\]

Monotonicity and dyadic summation of (L-32402.4) give

\[
\begin{aligned}
\psi(x)
&\le\psi(2^K)\\
&\le\sum_{r=1}^{K}2^r\log2\\
&<2^{K+1}\log2\\
&\le4x\log2.
\end{aligned}
\tag{L-32402.5}

For this two-contact system,

\[
\Psi_2(x)
=\psi(x)+\lfloor\log_2x\rfloor\log2.
\]

Since `log x<=x` for `x>=1`, (L-32402.5) implies the convenient uniform bound

\[
\boxed{
0\le\Psi_2(x)\le4x
\qquad(x\ge2).
}
\tag{L-32402.6}

The constant four is deliberately loose.

Therefore

\[
0\le G_2(x)\le\Psi_2(x)\le4x,
\]

and from (L-32402.1), writing `k=n-j`,

\[
\boxed{
|Q_2(n,j)|
\le G_2(n)+G_2(j)+G_2(k)
\le8n.
}
\tag{L-32402.7}

## 3. Absolute source-bound reserve

Fix `0<eta<=1/2` and suppose

\[
\eta n\le j\le(1-\eta)n,
\qquad
2\le j\le n-2.
\]

For all `n>=N_eta`, equations (L-32402.2)--(L-32402.3) and (L-32402.7) give

\[
\begin{aligned}
|Q_2(n,j)|^2
&\le64n^2\\
&\le {64\over\eta^2\log^22}P_2(n,j)^2\\
&\le\boxed{
{128\over\eta^2\log^22}R_2(n,j)}.
\end{aligned}
\tag{L-32402.8}

For the finitely many interior rows below `N_eta`, PR #302 `L-28009` proves
`R_2(n,j)>0`.  Hence the finite maximum

\[
C_\eta^{\rm fin}
=\max_{\substack{n<N_\eta\\
\eta n\le j\le(1-\eta)n\\2\le j\le n-2}}
{|Q_2(n,j)|^2\over R_2(n,j)}
\]

exists.  Put

\[
\boxed{
C_\eta
=\max\left(C_\eta^{\rm fin},
{128\over\eta^2\log^22}\right).
}
\tag{L-32402.9
}

Then for every balanced interior row,

\[
\boxed{
|Q_2(n,j)|^2\le C_\eta R_2(n,j).
}
\tag{L-32402.10
}

The constant depends only on the fixed balance parameter, not on the parent
scale `n`.

## 4. Finite physical normal Gram consequence

Let `dnu(n,j)>=0` be any finite measure supported on the fixed balanced interior
cone.  Multiplying (L-32402.10) and summing gives

\[
\boxed{
\sum_{n,j}d\nu(n,j)|Q_2(n,j)|^2
\le C_\eta
\sum_{n,j}d\nu(n,j)R_2(n,j).
}
\tag{L-32402.11
}

Under PR #302's exact carry-position physical localization, this is an absolute
source-specific physical-to-Selberg reserve theorem.  The logarithmic loss in
`L-28012.13` is removed completely.

No PNT, zero-free region, RH assumption, or numerical asymptotic is used.

## 5. Endpoint boundary

The restriction `2<=j<=n-2` is essential.  For odd `n`, the endpoint-neighbor
rows `j=1,n-1` can have `R_2=0` while the physical current is nonzero.

They are not omitted.  PR #302 `L-28015` proves that the complete two-contact
endpoint energy from `n>=4` is absorbed quadratically by the nearest interior
Selberg reserves with an absolute factor `32`; the finite bottom rows remain an
explicit boundary ledger.

Thus the balanced interior and the endpoint energy both have scale-independent
reserve constants.  What remains is the source-coupled lower-scale recurrence,
not a growing physical/carry condition number.

## 6. Consequence for the live proof graph

This theorem upgrades the source transference status from

```text
physical interior <= polylog(parent) * Selberg reserve
```

to

```text
physical interior <= absolute constant * Selberg reserve.
```

Therefore no `log(parent)` exponent loss is forced by the physical-to-carry
map itself.  Any remaining growth must come from the explicit proper-divisor
source-change/boundary family.

## 7. Proof boundary

Closed here:

1. an elementary linear generalized-Chebyshev bound;
2. an absolute balanced physical-field bound;
3. scale-independent domination by the source-matched Selberg reserve;
4. the corresponding finite normal-Gram inequality.

Imported:

- exact source formulas and positivity of `R_2` from PR #302.

Still open:

- source-coupled Schur elimination of the proper-divisor family;
- lower-scale recurrence for the principal inverse-zeta mode;
- RH.
