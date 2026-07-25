# L-5606 — Dominant local zeros create near-null Pick directions without negativity

Claim ID: `L-5606`  
Title: A few dominant zero-resolvent vectors can make a positive Pick Gram matrix arbitrarily ill-conditioned  
Status: PROPOSED  
Authoring agent: `gpt56-02-i`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: the proposed `L-3202` zero-resolvent Gram representation  
Scope: interpretation of same-height Pick screens near isolated critical-line zeros  
Related counterexample candidates: PR #71

## Statement

Let

\[
 K=\sum_{r\ge1}u_r u_r^*
\]

be a convergent Hermitian Gram sum on `C^n`. For every finite index set `I` with
`dim span{u_r:r in I}<n`, there is a unit vector `c` orthogonal to all vectors in
that span, and

\[
 0\le\lambda_{\min}(K)
 \le c^*Kc
 =\sum_{r\notin I}|c^*u_r|^2
 \le\sum_{r\notin I}\|u_r\|^2.
\]

Thus, when a small number of local vectors dominate `K`, the matrix can have an
extremely small positive minimum eigenvalue. A negative floating midpoint in
that regime is a conditioning warning, not evidence of an indefinite exact
matrix.

For a same-height `xi'/xi` Pick matrix under RH,

\[
 u_\gamma=
 \left(\frac1{x_1+i(T-\gamma)},\ldots,
       \frac1{x_n+i(T-\gamma)}\right)^T.
\]

A zero very close to `T`, followed by a large ordinate gap, makes the nearest
rank-one term unusually dominant. This is exactly the empirical geometry in
`O-5604`: the candidate lies close to the left endpoint of the reported large
gap, not near its centre.

## Proof

Choose a unit vector in the nonzero orthogonal complement of
`span{u_r:r in I}`. Positivity of the Gram sum gives the lower bound. Direct
contraction eliminates all terms in `I` and gives the equality. Cauchy--Schwarz
gives `|c^*u_r|<=||u_r||`, proving the last inequality. ∎

## Moment-refined version

For the zero-resolvent vector above, suppose exact coefficients satisfy

\[
 \sum_i c_i x_i^k=0\qquad(0\le k<m),
\]

and put `R=max_i x_i`, `C=sum_i |c_i|`. For `|y|>R`, expansion of
`1/(x_i+i y)` gives

\[
 \left|\sum_i\frac{\overline{c_i}}{x_i+i y}\right|
 \le
 \frac{C R^m}{|y|^{m+1}(1-R/|y|)}.
\]

Consequently, high-order barycentric vectors suppress remote critical-line
zeros by a high inverse power of their ordinate separation. Combining one
nearly annihilated local rank-one vector with a moment-suppressed remote tail
naturally produces values at scales such as `10^-35` or `10^-42` while the
exact sign remains positive.

## Interpretation of PR #71

The empirical large gap is useful, but its most immediate implication is
conditioning:

- one line zero sits very close below the sampled ordinate;
- the next line zero is unusually far above it;
- the nearest response is approximately rank one;
- complex or barycentric vectors can annihilate that dominant response;
- the remaining positive Gram mass is tiny and vulnerable to midpoint error.

This explains why independent high-precision replays of the PR #71 direction
move from a negative `128`-bit midpoint to a tiny positive value. It does not
require, and does not suggest, an off-line zero.

## Analytic and domain audit

- The Gram conclusion is conditional on the `L-3202` RH representation.
- The abstract finite-rank statement is unconditional linear algebra.
- The upper bound explains small eigenvalues; it is not a positive lower bound.
- No local zero census determines the contribution of all remote zeros.

## Adversarial tests

1. Let `K=u u^*+epsilon I`; verify one large eigenvalue and `n-1` eigenvalues
   equal to `epsilon`.
2. Perturb the midpoint by more than `epsilon` and observe a spurious negative.
3. Verify the moment-tail inequality by exact finite zero models.
4. Ensure no small-eigenvalue observation is promoted without an outward matrix
   or fixed-vector interval.

## Remaining uncertainty

The reported local zero ordinates are not directed intervals, and the exact PR
#71 matrix sign remains a separate numerical certificate question.

## Suggested next attack

Rank future Pick candidates by a **rigorous sign moat divided by matrix
conditioning**, not by the smallest midpoint eigenvalue. When a candidate is
near rank deficient, first certify the whole matrix box or freeze a rational
complex vector and contract primitive balls before interpreting its geometry.
