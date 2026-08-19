# Hostile review specification for T-99240

Review in this order.

1. Re-derive the coefficient dictionary `gamma_j`.
2. Verify the elementary kernel integral (L-99240.6) exactly.
3. Verify the cumulative moment identity (L-99240.9).
4. Verify the base and increment inequalities proving `kappa_j>0`.
5. Reconstruct the finite Möbius Fubini identity (L-99241.2).
6. Check that the Hall target is exactly `T=4sqrt(y)-3`, not the equality
   scalar `2sqrt(y)-1`.
7. Verify matched Hall bonuses remain current-only.
8. Verify same-index child placement is literal endpoint restriction in the
   positive kernel source.
9. Verify the random-key tree reproduces the root marginal with no duplicated
   rough factor.
10. Re-derive the fixed-row Mellin transform and large-j noncancellation.
11. Apply Landau only after nonnegativity of the exact same row is established.

Immediate falsifiers:

```text
a negative kappa_j value;
a missing activation term in the convolution;
a source coefficient applied twice;
a Hall bonus exported to a child;
a mismatch between the source-tree output and c_X(j);
a positive-real pole in the fixed-row continuation;
cancellation P_j(rho)=0 for every sufficiently large j.
```

No score or radix-four capacity claim is an antecedent.
