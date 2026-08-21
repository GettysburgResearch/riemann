# R-32201 — The positive floor-prefix excess may not be separated kernel-by-kernel

Claim ID: `R-32201`  
Status: **EXACT ROUTE-SCOPE REFUTATION**  
Created: 2026-08-09  
Dependencies: `L-32204`  
Scope: prevents an invalid continuation of the critical-hinge proof; no RH conclusion

## 1. The tempting but false continuation

`L-32204` proves that after the positive top-half solve of a convex target, the lower excess is a positive combination of kernels

\[
K_{N,q}(M)
=M-N-A_M(q)
+\frac{M(M+1)}{N(N+1)}A_N(q)\ge0.
\]

It is tempting to saturate each `K_(N,.,M)` independently by a nonnegative carry inverse and then use the positive Abel coefficients of the critical hinge.

That step is false.

## 2. Exact smallest average-row mutation

Take

\[
N=7,\qquad M=8.
\]

Let `k(q)=K_(7,q)(8)` for `2<=q<=7`, and let `c` be its unique triangular inverse in the average carry matrix:

\[
k(q)=\sum_{n=q}^{7}c(n)\beta_{nq}.
\]

Exact rational back substitution gives

\[
\boxed{c(4)=-\frac13.}
\]

Thus a coordinatewise positive floor-prefix kernel need not have a nonnegative carry inverse.

## 3. Full balanced-flow mutation

The same target fails the quarter-balanced nonnegative split-flow feasibility problem on endpoint seven.  This is a finite rational LP/Farkas statement; the retained exact certificate is emitted in `X-32203-excess-kernel`.

Hence the excess decomposition

\[
e_T(q)=\sum_M a_M K_{N,q}(M),\qquad a_M\ge0,
\]

must remain **recombined with its critical coefficients**.  Positivity of each scalar kernel is not a license to separate it before the carry/Pascal transport.

## 4. Consequence

The correct current order is

```text
critical hinge
-> exact positive top-half solve
-> recombined positive floor-prefix excess
-> source-specific recycle of the complete excess
```

and not

```text
positive floor-prefix kernels
-> independent positive carry inverses.
```

This is the same structural lesson seen elsewhere in the repository: source recombination must precede positivity.
