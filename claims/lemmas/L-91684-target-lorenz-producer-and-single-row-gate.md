# L-91684 — The target-Lorenz producer is source-faithful and score-superordinate

Claim ID: `L-91684`  
Status: **PROVED REDUCTION; ONE EXPLICIT ROW FAMILY REMAINS**  
Created: 2026-08-14  
Depends on: `L-91348`, `L-91682`  
RH status: **unproved**

## 1. Construction

For a stopped leaf let `E,O` be the positive even/odd source measures and assume `E_T>O_T`.  Let `U` be the leftmost submeasure of `E`, in increasing divisor order, with

\[
T(U)=O_T.
\]

Define

\[
\boxed{\nu=E-U.}
\tag{L-91684.1}
\]

Then `nu` is a literal source submeasure, uses every source atom at most once, and

\[
\boxed{T(\nu)=E_T-O_T.}
\tag{L-91684.2}
\]

By `L-91682`, its cutoff is one of the `185` even `P_61` divisors below `2000`.

## 2. Score superordination

For one scalar causal atom, write

\[
A=\sqrt z(\sqrt p-p^{-1/2}),
\qquad
B=1-p^{-1/2}.
\]

Then

\[
\frac{K_S}{K_T}
=\frac{5A-3B}{4A-3B}.
\]

Its derivative with respect to `A` is

\[
-\frac{3B}{(4A-3B)^2}<0.
\]

Since `A` decreases as the divisor increases, `K_S/K_T` is increasing in divisor order.  Hence the leftmost target submeasure minimizes score among all even submeasures with target `O_T`.

`L-91348` supplies an even score submeasure of score `O_S` and target at least `O_T`.  Trim it to target exactly `O_T`; its score remains at most `O_S`.  By the preceding minimization,

\[
S(U)\le O_S.
\]

Therefore

\[
\boxed{
S(\nu)=E_S-S(U)\ge E_S-O_S.
}
\tag{L-91684.3}
\]

The target-Lorenz producer has no score debt.

## 3. Exact remaining row gate

By `L-91682`, for every component row `j`, the causal row-per-target profile

\[
\rho_j(d)=\frac{K_R^{(j)}(d)}{K_T(d)}
\]

is nonincreasing in divisor order.  Thus `U` maximizes row among all even target submeasures of target `O_T`.

The producer is componentwise feasible exactly when

\[
\boxed{
\mathfrak L_{j}(p,y)
:=R_j(U)-O_R^{(j)}\ge0
\qquad(2\le j\le66).
}
\tag{L-91684.4}
\]

If (L-91684.4) holds, then

\[
R_j(\nu)=E_R^{(j)}-R_j(U)
\le E_R^{(j)}-O_R^{(j)}.
\]

All ordinary and radix-four responses follow from the positive response maps applied to the row bonus.  The one-use boundary/port ledger remains the reviewed fixed correction packet rather than a new source copy.

If `c<2000` is the target cutoff, (L-91684.4) has the explicit form

\[
\begin{aligned}
\mathfrak L_j(p,y)
={}&
\sum_{\substack{e<c\\\mu(e)=1}}
K_T(e)[\rho_j(e)-\rho_j(c)]\\
&-
\sum_{\substack{o<c\\\mu(o)=-1}}
K_T(o)[\rho_j(o)-\rho_j(c)]\\
&+
\sum_{\substack{o>c\\\mu(o)=-1}}
K_T(o)[\rho_j(c)-\rho_j(o)].
\end{aligned}
\tag{L-91684.5}
\]

The last line is termwise nonnegative.  Hence the only uncrossed producer theorem is a finite-cutoff arithmetic determinant family indexed by

```text
cutoff c: 185 even P_61 divisors below 2000;
row j:    2 <= j <= 66;
child y:  1 <= y < 67;
rough p:  p >= 67, with explicit analytic dependence.
```

The first quotient cell is closed exactly.  If `py<2j`, no odd source has an active row, while the `d=1` even source has a strictly positive row.  Therefore

\[
\boxed{\mathfrak L_j(p,y)>0\qquad(py<2j).}
\tag{L-91684.6}
\]

## 4. Boundary

This theorem replaces the false stopped-leaf Hall producer by one common source submeasure with exact target and score.  It does not assert (L-91684.4) on the remaining cells.
