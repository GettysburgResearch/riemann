# Hostile review specification — T-103020

Mandatory checks:

1. reconstruct the minimum-pair/equal-pair edge array;
2. derive the row sums and star potential of `L-102961`;
3. verify the star potential is zero-sum and nonincreasing;
4. prove the complete-graph gradient identity in `L-103005.3`;
5. verify that every nonzero gradient coefficient connects a minimum label to a later label;
6. reconstruct the radial actual-owner endpoint factorization of PR #730;
7. verify that only the squared endpoint term is discarded, and only into the frozen polylog ledger;
8. apply the Wronskian sign with the correct prime order;
9. derive all three coefficient classes in `L-103006.1`;
10. verify the positive symmetric-rectangle expansion `L-103006.3`;
11. verify each symmetric rectangle splits into two elementary Plücker bipartitions;
12. confirm `PLC103020`, `BCI102990`, and RH remain unproved.

Immediate falsifiers:

```text
using the equal-pair physical invariance to delete owner-dependent phases;
reversing the Wronskian order convention;
dropping the signed middle Euler block from a rectangle;
claiming TP2 alone or the replay orients every Pluecker rectangle;
claiming star closure proves the row-zero cycle;
claiming RH from T-103020.
```
