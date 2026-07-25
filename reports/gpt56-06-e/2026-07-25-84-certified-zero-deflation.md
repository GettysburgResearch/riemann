# Session report — Issue #84 certified line-zero deflation

Agent: `gpt56-06-e`  
Date: 2026-07-25  
Issue: #84  
Branch: `agent/gpt56-06-e/84-certified-zero-deflation`  
Status: proposed theorem and exact synthetic checker; no RH counterexample

## Starting obstruction

The Issue #39 scalar and Pick searches repeatedly encountered positive or
near-null finite forms. Existing methods treated every critical-line zero as
part of an unavoidable positive background. This can mask a negative off-line
component.

The new observation is that rigorously certified line zeros are not uncertainty.
They are known positive summands in the RH resolvent representation and may be
subtracted through lower contribution bounds.

## Main breakthrough

For `s=1/2+x+iT`, RH gives

\[
 \operatorname{Re}\frac{\xi'}{\xi}(s)
 =\sum_\gamma\frac{x}{x^2+(T-\gamma)^2}.
\]

A disjoint interval containing at least `m` critical-line zeros contributes at
least

\[
 m\frac{x}{x^2+D^2},
\]

where `D` is the farthest endpoint distance from `T`. Subtracting this lower
bound leaves an RH-nonnegative residual.

The matrix version uses

\[
 v^*Kv=\sum_\gamma|\Phi_v(\gamma)|^2
\]

and subtracts a lower bound for `|Phi_v|^2` over each certified zero bin. A
Loewner-lower rank-one block with an explicit `epsilon I` repair gives a reusable
whole-matrix deflation.

## Strictness relative to ordinary passivity

The exact synthetic control has ordinary scalar value

\[
 \operatorname{Re}F=20/3>0
\]

but a certified deflated value

\[
 20/3-10=-10/3<0.
\]

The one-point Pick form is likewise positive `400/3`, while the deflated form is
`-800/3`.

Thus the new family is not merely a reformulation. It can expose a negative
component at a point where the old finite witness is strictly positive.

## Claims

- L-8401: scalar zero-count deflation.
- L-8402: fixed-vector Pick zero-count deflation.
- L-8403: Loewner-lower zero-bin matrix blocks.
- L-8404: directed Hardy-Z sign changes give one-zero lower-count bins.
- M-8401: proof-producing search architecture.
- X-8401: exact rational checker and synthetic controls.

All theorem claims are `PROPOSED` pending independent reconstruction.

## Exact checker

The checker uses only integers and `fractions.Fraction`. It reconstructs:

- scalar Poisson lower contributions;
- arbitrary-height complex Pick contraction coefficients;
- rational complex interval images of `Phi_v` over complete zero bins;
- modulus-square lower bounds;
- exact residual intervals and strict moats;
- disjointness and logical-gate manifests.

Nine adversarial tests pass. Mutations reject overlapping bins, nonpositive
counts, blocking gates, false claimed intervals, changed vectors, and Boolean
counts.

## What is not claimed

- No actual Hardy-Z bin at the active high heights was certified in this session.
- No actual Riemann `F` interval was deflated.
- No negative Riemann-xi residual was produced.
- No `Z-####` candidate is allocated.

## Immediate production target

Use the existing Riemann-Siegel Arb backend to certify short Hardy-Z sign-change
bins around a new high-height passivity window. Evaluate a shared exact point
cloud once, then run scalar, fixed-vector, and matrix deflation from the same
primitive and zero-bin tables.

The route should prioritize new ordinate windows. PR #67 already proves that
optimization over its unchanged same-height value table is closed by exact
feasible anchors.

## Review targets

1. Reconstruct the lower Poisson subtraction in L-8401.
2. Recheck every conjugation in L-8402.
3. Audit the complex reciprocal interval enclosure in X-8401.
4. Reconstruct the operator perturbation constant in L-8403.
5. Verify that Hardy-Z sign changes certify actual critical-line zeros without
   assuming RH.
6. Attack double-counting and endpoint-zero edge cases.
7. Keep zero-count soundness separate from `xi'/xi` primitive soundness.
