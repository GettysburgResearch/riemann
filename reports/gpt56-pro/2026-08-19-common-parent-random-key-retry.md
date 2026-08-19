# Retry publication report: factor-67 common-parent random-key attack

## Result

The missing prior branch was reconstructed from the surviving report and republished as a reviewable add-only packet.

The central theorem is the exact identity

\[
 s_kP+\sum_j\lambda_j(P-r_jC_j)=P-\sum_j\alpha_jC_j,
\]

with

\[
 \sum_j\alpha_j<67^{-1/2}<1/8.
\]

When the children are literal submeasures in one unnormalized source coordinate, a single uniform random key gives disjoint owners for all children and the residual. This closes the abstract common-parent ownership problem and leaves more than seven eighths of the parent pointwise.

## Additional insights retained

1. **Normalize last.** Partition the raw source first. Every normalized additive datum is then a mass-weighted barycenter, so convex deficits transfer by Jensen without asserting false coordinatewise domination of independently normalized children.
2. **Quantize through an integral flow polytope.** A fractional bipartite Hall flow with integer capacities is a convex combination of integral feasible flows. Selecting a leaf by one random key gives samplewise Hall feasibility; ordinary unbiased coordinatewise rounding does not.
3. **Keep the native interface fail closed.** The abstract theorems do not prove that the conclusion-producing source, score, activation, and endpoint constraints form one integral network-flow face. That source-to-leaf identification remains load bearing.

## Exact status

```text
abstract ownership theorem                 proved
factor-67 coefficient reserve              proved
normalization transfer                     proved
network Hall integrality                   proved at stated scope
full native producer application           open
RH                                          unproved
```

The verifier and seven mutation/control tests were replayed locally before publication.
