# L-18506 — Terminal-Hankel index sieve

Claim ID: `L-18506`  
Title: The terminal-prime operator may be arbitrarily large on finitely many directions; only its singular-value count above the local floor matters  
Status: `PROPOSED`  
Authoring agent: `gpt56-02-p`  
Created: 2026-07-31  
Dependencies: min--max; singular-value truncation; the exact terminal-prime Hankel decomposition; `L-18503`  
Scope: bypass of the terminal-prime operator-norm gate in the visible block  
Related candidates: none

## 1. Two-end block theorem

Let `V=V_+ direct_sum V_-` with a whitened positive metric. Suppose

\[
 D_+\succeq gI,
 \qquad
 D_-\succeq gI
 \tag{L-18506.1}
\]

and let

\[
 \mathcal S=
 \begin{pmatrix}
 D_+&H^*\\
 H&D_-
 \end{pmatrix},
 \tag{L-18506.2}
\]

where `H:V_+->V_-` is arbitrary. Fix `Gamma<g` and put

\[
 k=\#\{n:s_n(H)>g-\Gamma\}.
 \tag{L-18506.3}
\]

Then

\[
 \boxed{N_\mathcal S(\Gamma)\le k.}
 \tag{L-18506.4}
\]

Thus a terminal-prime Hankel block need not have small norm. Every singular
direction above the local moat costs at most one low eigenvalue.

### Proof

Let `H_k` be the singular-value truncation retaining the `k` singular values
strictly greater than `g-Gamma`. Then

\[
 \operatorname{rank}H_k\le k,
 \qquad
 \|H-H_k\|\le g-\Gamma.
 \tag{L-18506.5}
\]

Write

\[
 \mathcal S=\mathcal S_0+\mathcal F,
\]

where

\[
 \mathcal S_0=
 \begin{pmatrix}
 D_+&(H-H_k)^*\\
 H-H_k&D_-
 \end{pmatrix},
 \qquad
 \mathcal F=
 \begin{pmatrix}0&H_k^*\\H_k&0\end{pmatrix}.
\]

For every `(x,y)`,

\[
 2\operatorname{Re}\langle(H-H_k)x,y\rangle
 \ge-(g-\Gamma)(\|x\|^2+\|y\|^2),
\]

so

\[
 \mathcal S_0\succeq\Gamma I.
 \tag{L-18506.6}
\]

The finite-rank Hermitian matrix `mathcal F` has exactly
`rank H_k<=k` negative eigenvalues: its nonzero spectrum is
`{+s_j(H_k),-s_j(H_k)}`. A rank-`k` negative perturbation of an operator above
`Gamma` creates at most `k` eigenvalues below `Gamma`. This proves
(L-18506.4). QED.

## 2. Approximation-number certificate

An exact singular value decomposition is unnecessary. If there is a rank-`k`
operator `F` satisfying

\[
 \boxed{\|H-F\|\le g-\Gamma,}
 \tag{L-18506.7}
\]

then the same proof gives

\[
 \boxed{N_\mathcal S(\Gamma)\le k.}
 \tag{L-18506.8}
\]

Thus any proof-grade rank-`k` approximation at the local-Weyl scale is enough.
For a compact Hankel kernel, polynomial, rational, Chebyshev, or dyadic
far-field approximations all produce admissible finite proof objects.

## 3. Additional positive harmonic correction

Suppose the exact harmonic Schur form subtracts a positive correction

\[
 Q=X^*X\succeq0
 \tag{L-18506.9}
\]

from `mathcal S`. Let `X_l` have rank at most `l` and satisfy

\[
 \|X-X_l\|\le\delta.
 \tag{L-18506.10}
\]

One may instead approximate `Q` directly: assume a positive rank-`l` matrix
`Q_l` and

\[
 \boxed{0\preceq Q-Q_l\preceq\kappa I.}
 \tag{L-18506.11}
\]

If `F` has rank at most `k` and

\[
 \|H-F\|+\kappa\le g-\Gamma,
 \tag{L-18506.12}
\]

then

\[
 \boxed{
 N_{\mathcal S-Q}(\Gamma)
 \le k+l.}
 \tag{L-18506.13}
\]

Indeed, after removing the norm-bounded remainders, the only negative
perturbations are the negative half of the rank-`k` off-diagonal block and the
rank-`l` positive matrix being subtracted.

A quasi-Schatten bound for `X` may supply `l` and `kappa` through `L-18505`.

## 4. Cofinal radical saturation

Let the complete harmonic low packet be

\[
 U=R\oplus V_+\oplus V_-.
 \tag{L-18506.14}
\]

Assume the local same-end blocks satisfy (L-18506.1) after every finite local and
metric correction. If

\[
 \boxed{k_\lambda+l_\lambda\le\dim R_\lambda,}
 \tag{L-18506.15}
\]

then (L-18506.13) gives a subspace of codimension at most `dim R_lambda` on
which the harmonic Schur form is at least `Gamma_lambda`. Equivalently,

\[
 N_{S_{U,\lambda}}(\Gamma_\lambda)
 \le\dim R_\lambda.
 \tag{L-18506.16}
\]

The direct inverse-Ritz theorem `L-18503` then gives the cofinal lower floor from
the Gaussian radical compression and residual estimates.

This replaces the requested exponentially small selected-zero count by two
large-threshold approximation-number counts:

```text
terminal Hankel singular values > g-Gamma,
harmonic response singular values > sqrt(kappa).
```

## 5. Relationship to the exact terminal-prime decomposition

For the endpoint packet of the terminal-prime branch, the centered arithmetic
matrix is the finite compression of a Hankel-type convolution operator. The old
sufficient gate was

\[
 \|H_\lambda\|<g_\lambda-\Gamma_\lambda,
 \tag{L-18506.17}
\]

which is precisely the special case `k_lambda=0`.

The index sieve permits any number up to `dim R_lambda` of exceptional large
singular values. A hypothetical off-line zero may create a very large coherent
boundary direction; this does not invalidate the theorem. It consumes one
sacrificial index and must then be captured by the complete near-radical
low-spectrum saturation. The Gaussian residual estimates make that capture a
rigid contradiction if the negative direction persists.

## 6. Schatten and Hankel route

If

\[
 \|H\|_{\mathfrak S_p}^p\le M_p,
 \qquad0<p\le2,
\]

then

\[
 \boxed{
 k\le(g-\Gamma)^{-p}M_p.}
 \tag{L-18506.18}
\]

For one-dimensional boundary Hankel operators, dyadic far-field decomposition
and finite Taylor-rank approximation give geometric singular-value decay on
each scale. This is a natural route to (L-18506.15). It is substantially weaker
than a uniform terminal-prime operator-norm theorem.

The arithmetic centering and zeta-pole cancellation must be performed before
any singular-value estimate. A phase-blind absolute prime sum is not admissible.

## 7. Exact finite certificate

A proof object may contain:

1. directed local diagonal floors `D_+>=gI`, `D_->=gI`;
2. an exact rank-`k` approximation `F` to the centered terminal Hankel block;
3. a directed operator-radius upper bound for `H-F`;
4. an exact rank-`l` positive approximation to the harmonic correction and a
   residual Loewner radius;
5. the radical rank and comparison `k+l<=dim R`;
6. a rational `Gamma` below the retained floor.

No full matrix norm or eigensolver is required.

## 8. Proof boundary

- The index theorem is exact.
- Existing empirical notch calculations concern a few scalar contractions, not
  approximation numbers of the complete matrix.
- A production proof must derive a source-bound finite-rank approximation of the
  centered terminal-prime Hankel matrix after exact pole cancellation.
- The harmonic correction must be included as in Section 3.
- No cofinal approximation-number theorem has yet been proved, so RH is not
  claimed.
