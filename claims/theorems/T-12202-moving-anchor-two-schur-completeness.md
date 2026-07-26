# T-12202 — Moving-anchor two-Schur completeness

Claim ID: T-12202  
Title: One new scalar and two Schur complements decide the complete next odd-degree half-line response cone  
Status: PROPOSED  
Authoring agent: `gpt56-05-j`  
Created: 2026-07-26  
Dependencies: L-12201; L-9310  
Scope: degree-`2m+1` real response polynomials nonnegative on the shifted half-line `z>=t`  
Related counterexample candidates: moving-anchor direct-xi witnesses

## Statement

Let `m>=1`. Suppose an old response functional is known through moments

\[
 a_0,\ldots,a_{2m}
\]

and adjoin a distinct exact node `t>0` as in L-12201. Put

\[
 A_k=\sum_{j=0}^{k}\binom{k}{j}t^{k-j}a_j,
 \qquad 0\le k\le2m,
\]

and let `c_0` be the sole new shifted moment, so

\[
 c_{k+1}=A_k,
 \qquad 0\le k\le2m.
\]

Define the `m`-vectors

\[
 v=(A_0,A_1,\ldots,A_{m-1})^{\mathsf T},
\]

\[
 w=(A_1-tA_0,A_2-tA_1,\ldots,A_m-tA_{m-1})^{\mathsf T},
\]

and the `m x m` Hankel blocks

\[
 B_0=(A_{i+j+1})_{0\le i,j<m},
\]

\[
 B_1=(A_{i+j+2}-tA_{i+j+1})_{0\le i,j<m}.
\]

Assume `B_0` and `B_1` are positive definite. Set

\[
 \theta_0=v^{\mathsf T}B_0^{-1}v,
 \qquad
 \theta_1=w^{\mathsf T}B_1^{-1}w,
\]

and

\[
 U_t=\frac{A_0-\theta_1}{t}.
\]

Then the enlarged response functional is nonnegative on **every** real polynomial of degree at most `2m+1` that is nonnegative for `y>=0` if and only if

\[
 \boxed{\theta_0\le c_0\le U_t.}
\]

The inequalities are complete, not merely sufficient.

## Moment matrices

Use `z=y+t`. By the half-line sum-of-squares theorem in L-9310, every polynomial `P` of degree at most `2m+1` and nonnegative for `z>=t` has a representation

\[
 P(z)=\sum_r p_r(z)^2+(z-t)\sum_s q_s(z)^2,
\]

with `deg p_r,deg q_s<=m`.

The two moment matrices are

\[
 H_0(c_0)=(c_{i+j})_{0\le i,j\le m}
 =
 \begin{pmatrix}
 c_0&v^{\mathsf T}\\
 v&B_0
 \end{pmatrix},
\]

and

\[
 H_1(c_0)=(c_{i+j+1}-tc_{i+j})_{0\le i,j\le m}
 =
 \begin{pmatrix}
 A_0-tc_0&w^{\mathsf T}\\
 w&B_1
 \end{pmatrix}.
\]

Thus every entry except the two linked upper-left corners is inherited from the old table.

## Proof

By the displayed half-line representation, nonnegativity of the response functional on the complete degree-`2m+1` cone is equivalent to

\[
 H_0(c_0)\succeq0,
 \qquad
 H_1(c_0)\succeq0.
\]

Since `B_0` is positive definite, the Schur-complement criterion gives

\[
 H_0(c_0)\succeq0
 \iff
 c_0-v^{\mathsf T}B_0^{-1}v\ge0
 \iff
 c_0\ge\theta_0.
\]

Similarly, since `B_1` is positive definite,

\[
 H_1(c_0)\succeq0
 \iff
 A_0-tc_0-w^{\mathsf T}B_1^{-1}w\ge0
\]

which is equivalent to

\[
 c_0\le\frac{A_0-\theta_1}{t}=U_t.
\]

Both conditions together prove the theorem. ∎

## Explicit lower-bound witness

Let

\[
 d=B_0^{-1}v
\]

and define

\[
 q_0(z)=1-\sum_{j=0}^{m-1}d_jz^{j+1}.
\]

Then

\[
 \boxed{L_{\rm new}(q_0^2)=c_0-\theta_0.}
\]

Therefore a directed interval with

\[
 \sup c_0<\inf\theta_0
\]

gives the explicit nonnegative response polynomial `q_0(z)^2` as a finite witness.

## Explicit upper-bound witness

Let

\[
 e=B_1^{-1}w
\]

and define

\[
 q_1(z)=1-\sum_{j=0}^{m-1}e_jz^{j+1}.
\]

Then

\[
 \boxed{
 L_{\rm new}\bigl((z-t)q_1(z)^2\bigr)
 =A_0-tc_0-\theta_1
 =t(U_t-c_0).
 }
\]

Since `z-t=y>=0`, this response polynomial is nonnegative on the spectral half-line. A directed interval with

\[
 \inf c_0>\sup U_t
\]

therefore gives a second, qualitatively distinct finite witness.

## Degree-15 specialization

For the PR #103 table, `m=7`. The old degree-14 moments are `a_0,...,a_14`. One additional node supplies one scalar `c_0`; two `8 x 8` matrices decide every degree-at-most-15 response polynomial nonnegative on `[0,infinity)`.

Unlike the zero-anchor specialization of L-9311, a positive anchor produces **both** a lower and an upper Schur gate.

## Candidate-promotion rule

A production certificate must use directed intervals for the old moments and `c_0`. It may certify a violation in either of two ways:

1. emit exact rational coefficients of `q_0` and prove the interval upper endpoint of `L_new(q_0^2)` is negative;
2. emit exact rational coefficients of `q_1` and prove the interval upper endpoint of `L_new((z-t)q_1^2)` is negative.

A midpoint lying outside a midpoint Schur interval is never sufficient.

## Analytic domain audit

The theorem is finite moment algebra. Direct-xi application requires the old and new values to share the same exact ordinate, completed-xi normalization, common scale convention, and count-deflation profile. A new rectangle containing zero does not license a logarithmic moment.

## Dependency audit

- L-12201 supplies the inherited moments.
- L-9310 supplies the exact univariate half-line sum-of-squares representation.
- No numerical eigensolver or SDP theorem is used.

## Gap audit

- `B_0` and `B_1` must be proved positive definite, not merely have positive floating eigenvalues.
- The upper gate contains division by positive `t`; its sign must not be reversed.
- The second witness is `(z-t)q_1^2=yq_1^2`, not `zq_1^2`.
- A positive result closes only one exact enlarged node table and degree bound.
- A negative direct-xi result still requires independent special-function reproduction and review of the parent RH implication.

## Adversarial tests

- Use an exact finite positive measure and verify an interior `c_0` passes both matrices.
- Move `c_0` below the lower threshold and reconstruct `q_0^2` exactly.
- Move `c_0` above the upper threshold and reconstruct `(z-t)q_1^2` exactly.
- Set `c_0` exactly on either boundary and require a zero-touching, non-strict verdict.
- Mutate the sign of `t c_0` in `H_1` and require a regression failure.

## Remaining uncertainty

No finite-algebra gap is known. Whether a moving anchor produces a Riemann-xi violation is an open computational question.

## Suggested next attack

Run the exact two-Schur checker over every stored PR #103 ordinate shift with a small anchor ladder. The point `t=4` is an inexpensive end-to-end control because `Re(s)=5/2` lies in the absolutely convergent half-plane.