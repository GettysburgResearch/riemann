# L-18513 — A positive source-canonical block transfers to every profile-soft Schur split

Claim ID: `L-18513`  
Title: One source-canonical direct certificate makes every exact profile-soft Schur block positive  
Status: `PROVED FINITE BLOCK ALGEBRA; COFINAL SOURCE-CANONICAL LOWER LAW OPEN`  
Authoring agent: `gpt56-08`  
Created: 2026-08-01  
Dependencies: `L-18512`; finite-dimensional Schur-complement algebra  
Scope: level-wise generalization of X-18508 across the X-18506 schedule

## Statement

Let `G>0` and let a self-adjoint finite Weil matrix `A` be decomposed in the
source-canonical split

\[
 U=W\oplus_G E,
 \qquad
 A=\begin{pmatrix}B&Z^*\\ Z&C\end{pmatrix}.
\]

If

\[
 C\succ0,
 \qquad
 B-Z^*C^{-1}Z\succ0,
\]

then `A` is positive definite. Consequently, for **every** other exact
`G`-orthogonal split

\[
 U=S\oplus_G H,
\]

the profile-soft harmonic Schur complement satisfies

\[
 A_{SS}-A_{SH}A_{HH}^{-1}A_{HS}\succ0.
\]

More quantitatively, if

\[
 A\succeq\delta G,
 \qquad \delta>0,
\]

then

\[
 \boxed{
 A_{SS}-A_{SH}A_{HH}^{-1}A_{HS}
 \succeq \delta G_S.
 }
\]

The subspace `S` may be the exact spectral profile-soft range, an interval
Riesz projector, or any other exact finite packet. No angle between the
source-canonical and profile-soft splits is required for the sign transfer.

## Proof

The first assertion is the standard Schur factorization

\[
 A=
 \begin{pmatrix}I&Z^*C^{-1}\\0&I\end{pmatrix}
 \begin{pmatrix}B-Z^*C^{-1}Z&0\\0&C\end{pmatrix}
 \begin{pmatrix}I&0\\C^{-1}Z&I\end{pmatrix}.
\]

Hence `A` is positive definite. Compressing a positive definite matrix to `H`
gives `A_HH>0`; applying the same factorization in the `S/H` split proves the
second Schur complement positive.

For the quantitative assertion, apply the preceding argument to

\[
 A-\delta G\succeq0.
\]

Since the split is `G`-orthogonal, the metric is block diagonal. The Schur
complement of `A-delta G` is nonnegative:

\[
 A_{SS}-\delta G_S
 -A_{SH}(A_{HH}-\delta G_H)^{-1}A_{HS}\succeq0.
\]

Moreover

\[
 A_{HH}-\delta G_H\preceq A_{HH}
 \quad\Longrightarrow\quad
 (A_{HH}-\delta G_H)^{-1}\succeq A_{HH}^{-1}.
\]

Replacing the larger inverse by the smaller one gives

\[
 A_{SS}-A_{SH}A_{HH}^{-1}A_{HS}\succeq\delta G_S.
\]

## Production consequence

At every X-18506 level it is enough to certify the source-canonical ambient
coercivity and direct Schur pivot. Once that certificate passes, every exact
buffered profile-soft projector at the same level has zero negative part.
The profile producer is then responsible only for:

1. the exact source/profile identity;
2. the graph LMI and support-derivative ledger;
3. the buffered generalized spectral export;
4. binding all objects to the same arithmetic matrix.

X-18508 additionally replays the PR #191 short in the profile basis, but this is
an independent consistency check rather than a logical necessity.

## Cofinal reduction

For an unbounded X-18506 schedule, the common profile-soft ledgers pass whenever
both of the following are emitted at every retained level:

\[
 C_j\succ0,
 \qquad
 B_j-Z_j^*C_j^{-1}Z_j\succ0,
\]

and the profile producer exports a buffered exact soft range. The remaining
cofinal arithmetic theorem is therefore the source-canonical lower law

\[
 \inf_j \lambda_{\min}(A_j,G_j)>0
\]

or any explicit positive/vanishing schedule sufficient for the repository's
cofinal lower-envelope theorem. A finite ladder cannot establish this
asymptotic statement.
