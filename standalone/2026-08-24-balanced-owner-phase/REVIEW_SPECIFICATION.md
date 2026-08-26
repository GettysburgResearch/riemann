# Hostile review specification — T-102870

Review the balanced owner-phase packet at the exact PR #719 head.

Mandatory reconstruction:

1. Verify common-factor extraction in `L-102860` and the `1/d` Gram weight.
2. Check that each selected owner prime divides exactly one reduced product.
3. Reconstruct the two nonzero Ramanujan sums, one from each physical side.
4. Verify the phase-cardinality/owner-weight cancellation in `L-102861`.
5. Reconstruct the owner/core-overlap renewal and confirm that no prime incidence
   is charged twice.
6. Apply the one-modulus core-energy theorem to both sides of `L-102863`.
7. Apply the product-modulus theorem to all four owner phases in `L-102864`.
8. Verify the fifteen choices and the local minimum in `L-102865`.
9. Reproduce `R-102840`; reject any source-blind summation of fixed-pair bounds.
10. Confirm that `BQSP102870` and RH remain unproved.

Immediate falsifiers:

```text
using an owner prime which still divides both reduced products;
reintroducing a zero additive phase;
counting one phase cardinality without its literal owner weight;
applying the long-core bound in a short-core octave;
summing O(1) fixed-pair bounds without arithmetic orthogonality;
claiming the retained replay proves BQSP102870 or RH.
```
