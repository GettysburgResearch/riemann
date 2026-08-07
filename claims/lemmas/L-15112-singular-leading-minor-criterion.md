# L-15112 — The correct leading-principal-minor criterion at corank one

Claim ID: `L-15112`  
Status: **PROVED ELEMENTARY MATRIX LEMMA**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Dependencies: Sylvester's criterion and the Schur complement  
Scope: correction of the semidefinite-certificate warning in PR #173  
Related counterexample candidates: none

## Statement

Let `A=A^T` be an `n by n` real symmetric matrix and let

\[
 \Delta_k=\det A[1{:}k,1{:}k]
\]

be its leading principal minors in one fixed ordering.

### A. Valid corank-one certificate

If

\[
 \boxed{
 \Delta_k>0\quad(1\le k<n),
 \qquad
 \Delta_n=0,}
 \tag{L-15112.1}
\]

then

\[
 \boxed{A\succeq0,\qquad \operatorname{rank}A=n-1.}
 \tag{L-15112.2}
\]

Thus it is too broad to say that a singular positive-semidefinite matrix always requires all principal minors. Strict positivity of every proper leading principal minor, together with exact zero determinant, is already sufficient at corank one.

### B. Invalid nonnegative-leading-minor test

The weaker condition

\[
 \Delta_k\ge0\quad(1\le k\le n)
\]

is not sufficient. For example,

\[
 A=\operatorname{diag}(1,0,-1)
\]

has leading minors

\[
 1,0,0
\]

but inertia `(1,1,1)`.

Therefore a checker that merely rejects negative leading minors can accept an indefinite singular matrix.

## Proof of Part A

Write

\[
 A=\begin{pmatrix}B&b\\b^{\mathsf T}&d\end{pmatrix},
\]

where `B` is the leading `(n-1) by (n-1)` block. The inequalities

\[
 \Delta_1,\ldots,\Delta_{n-1}>0
\]

make `B` positive definite by Sylvester's criterion.

The determinant factorization is

\[
 \det A=\det B\,(d-b^{\mathsf T}B^{-1}b).
\]

Since `det B>0` and `det A=0`, the Schur complement vanishes:

\[
 d=b^{\mathsf T}B^{-1}b.
\]

Hence

\[
 A=
 \begin{pmatrix}I&0\\b^{\mathsf T}B^{-1}&1\end{pmatrix}
 \begin{pmatrix}B&0\\0&0\end{pmatrix}
 \begin{pmatrix}I&B^{-1}b\\0&1\end{pmatrix},
\]

which is positive semidefinite and has rank `n-1`. QED.

## Audit consequence

The PR #173 warning should identify the exact predicate used by the failed certificate:

- if it checked only nonnegativity of leading minors, the diagnosis is correct;
- if it truly checked every proper leading minor strictly positive and the determinant exactly zero, then its reported indefinite inertia is incompatible with those premises and one of the computations or descriptions is wrong.

For production, pivoted exact `LDL^T`, exact symmetric congruence, or all-principal-minor checking remain the safest general interfaces, especially when the kernel dimension may exceed one.