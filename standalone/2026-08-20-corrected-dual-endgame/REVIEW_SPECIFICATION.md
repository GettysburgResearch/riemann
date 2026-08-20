# Hostile review specification — T-100400

Frozen base:

```text
PR #685
4f69b7656f42dcb5ff250d13adc9f88e8d18f315
```

Mandatory checks:

1. Verify `R-100400` by differentiating both proposed primitives.
2. Reconstruct the activation-zero all-integer kernel.
3. Reconstruct the Mellin transform and every positive-real cancellation.
4. Derive the atom-free future identity.
5. Recompute cell coefficients and `C1` activation matching.
6. Check the five regimes for the two-label derivative cone.
7. Verify the three- and four-label induction.
8. Reproduce the five-copy label-2 negative mutation.
9. Derive the phase-Hasse divergence identity.
10. Derive the area formula.
11. Recompute the Cauchy phase bound.
12. Reject any step replacing `PHPC100410` by the free labelled estimate.

Immediate falsifiers:

```text
using the normalized deficit in the Landau consumer;
claiming complete monotonicity from four-label positivity;
merging the two 67 labels before phase transport;
using a random-phase or source-blind collapse estimate;
claiming RH from the retained replay.
```
