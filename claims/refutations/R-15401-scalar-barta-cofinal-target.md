# R-15401 — The scalar cofinal Barta target is impossible

Claim ID: `R-15401`  
Title: Refutation of the proposed positive-scalar supersolution completion  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: `L-15403`  
Scope: the final-object claim attached to `L-15402` and the scalar Barta component of `T-15401`  
Related counterexample candidates: none

## Refuted target

The branch previously identified the following as a possible final missing
object:

\[
 \operatorname*{ess\,inf}b_{a_j,\psi_j}^{\rm odd}
 \ge-2\varepsilon_j,
 \qquad
 a_j\to\infty,
 \qquad
 \varepsilon_j\to0,
 \tag{R-15401.1}
\]

with every `psi_j` strictly positive.

`L-15403` proves instead that, for every positive scalar `psi`,

\[
 \operatorname*{ess\,inf}b_{a,\psi}^{\rm odd}
 \le -{e^a\over a}
 \tag{R-15401.2}
\]

for all sufficiently large `a`. With the prime number theorem the universal
upper obstruction is asymptotic to `-16e^a/a`.

Therefore the family in (R-15401.1) cannot exist.

## Source of the false optimism

The signed-edge identity itself is exact. The failure occurs when the complete
nonnegative signed-edge remainder is discarded to obtain a pointwise scalar
floor. The local residual is independent of every edge sign. Averaging it gives

\[
 \int {L_J\psi\over\psi}
 =-{1\over2}\iint
 {\left(\psi(x)-\psi(y)\right)^2\over\psi(x)\psi(y)}J(dx,dy)
 \le0.
\]

Thus a scalar positive supersolution sees the signed graph as an unsigned
Markov graph and cannot use the large frustration energy in the cross-origin
`+` squares. The odd polar potential alone then forces an exponentially
negative mean.

This is an architectural obstruction, not a failure of one candidate profile.
No amount of spline fitting or precision escalation can repair it.

## Valid results retained

The following remain useful and are not refuted:

1. `L-15401`'s exact jump-potential-polar decomposition;
2. `L-15402`'s exact signed-edge representation;
3. the abstract signed-edge ground-state identity;
4. the finite rational regression `X-15401`;
5. `T-14302`'s cofinal lower-envelope criterion;
6. the phase-aware block and multiband reductions in PR #152.

Only the proposed **scalar positive supersolution completion** is retired.

## Required replacement

Any successful positive proof must preserve arithmetic and cross-origin phase
coherence. Two viable classes remain:

- the generalized-prolate low-symbol packet plus exact Schur correction from
  `L-14308`--`L-14311`;
- a new matrix-valued or system supersolution theorem whose local residual
  retains signed-edge channels rather than erasing them.

A scalar Barta certificate may still be useful at fixed small support, but it
cannot provide the required cofinal RH envelope.

## Counterexample and RH status

This refutation says nothing about the truth value of RH. It prevents a false
positive proof and redirects the project to phase-aware lower-floor methods.
