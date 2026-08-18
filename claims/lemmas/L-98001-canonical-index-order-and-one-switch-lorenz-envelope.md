# L-98001 — The completed scalar Lorenz optimizer is a canonical one-switch source prefix

Claim ID: `L-98001`  
Status: **PROVED EXACT FINITE-DIMENSIONAL THEOREM**  
Created: 2026-08-18  
Depends on: `L-98000`; the completed owner ledger and scalar Lorenz dual in PRs #584/#591  
RH status: **unproved**

Absorb each positive source coefficient into its target and scalar coordinates.
For a squarefree source index `k<=X`, put

\[
t_X(k)={1\over\sqrt k}T(X/k),
\qquad
r_X(k)={1\over\sqrt k}Q_*(X/k).
\tag{L-98001.1}
\]

This is equivalent to retaining the coefficient as atom capacity, because both
coordinates are scaled by the same positive number.

The atom ratio is

\[
\boxed{
{r_X(k)\over t_X(k)}=\rho_*(X/k).
}
\tag{L-98001.2}
\]

By `L-98000`, if `k_1<k_2` then

\[
{r_X(k_1)\over t_X(k_1)}
\ge
{r_X(k_2)\over t_X(k_2)},
\tag{L-98001.3}
\]

with strict inequality whenever both quotients are greater than two. Every
ratio is in `[0,6)`, and it is zero exactly when `k>=X/2` (with the activation
endpoint interpreted by continuity).

Thus the fractional-knapsack order in the completed-parity scalar Lorenz problem
is not an endpoint-dependent sort. It is the ordinary increasing order of the
source indices.

## Exact envelope

Let

\[
1\le k_1<k_2<\cdots<k_M\le X,
\qquad \mu(k_j)=+1,
\]

be the even source indices. Define the cumulative even target and scalar
prefixes

\[
A_j=\sum_{i\le j}t_X(k_i),
\qquad
B_j=\sum_{i\le j}r_X(k_i),
\qquad A_0=B_0=0.
\tag{L-98001.4}
\]

Let `T_O,R_O` be the complete odd target and scalar demands. If target capacity
holds, choose the unique `j` (up to a zero-ratio tie) satisfying

\[
A_{j-1}\le T_O\le A_j.
\tag{L-98001.5}
\]

Then the exact Lorenz envelope is

\[
\boxed{
\Phi_X(T_O)
=B_{j-1}
+{r_X(k_j)\over t_X(k_j)}
  (T_O-A_{j-1}).
}
\tag{L-98001.6}
\]

Consequently completed scalar feasibility is equivalent to

\[
T_O\le A_M
\tag{L-98001.7}
\]

and the single one-switch inequality

\[
\boxed{
R_O\le
B_{j-1}+\rho_*(X/k_j)(T_O-A_{j-1}).
}
\tag{L-98001.8}
\]

The dual minimizing parameter is `lambda=r_X(k_j)/t_X(k_j)`, except that it may
be any point of a tied zero-ratio interval. No other atom-ratio breakpoint needs
to be checked once the target crossing is known.

## One-switch dual form

For `0<lambda<6`, let `Y_lambda` be the unique threshold from `L-98000` and put

\[
K_\lambda=X/Y_\lambda.
\]

Then the forward dual slack is exactly

\[
D_X^+(\lambda)
=
\sum_{\substack{k<K_\lambda\\\mu(k)=+1}}
  [r_X(k)-\lambda t_X(k)]
+\lambda T_O-R_O.
\tag{L-98001.9}
\]

Thus the nonlinear Lorenz profile is a single source-index switch. The remaining
arithmetic is in a Möbius/parity prefix, not in an arbitrary permutation or a
high-dimensional convex program.

## Scope

This theorem does not prove the one-switch inequality. It removes the sorting
and continuous-profile ambiguity and provides an exact canonical separator:
endpoint `X`, crossing index `k_j`, and the scalar value in (L-98001.8).