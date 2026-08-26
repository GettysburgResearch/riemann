# Review specification — T-102830

Frozen parent branch:

```text
PR #719
research/gpt56-pro/102700-half-divisor-defect-factorization
```

Mandatory checks:

1. Reconstruct the equal-pair coefficient `1/binom(k,2)` from `L-102746`.
2. Verify that moving the complete occurrence to its largest two labels leaves
   physical realization unchanged.
3. Verify the exact labelled-energy transfer factor `binom(k,2)`.
4. Check that every cofactor prime lies below `4 sqrt(Y)` on the horizon.
5. Prove injectivity of `(p,q,a)->p q a^2` from squarefree kernels.
6. Reconstruct the same-pair harmonic overlap bound.
7. Verify the quadratic Walsh character identity and Haar orthogonality.
8. Reproduce the identity-point countermodel in `R-102830`.
9. Verify the largest-discrepancy-prime parity statement with the duplicate
   `67` labels retained.
10. Confirm `L2SC102833`, `LDPC102834` and RH are not marked proved.

Immediate falsifiers:

```text
collapsing the two 67 labels before squareclass assignment;
using the Walsh average as a bound for epsilon=1;
taking an absolute value before prime-carrier recombination;
counting the largest-two and equal-pair gauges as different sources;
claiming squareclass injectivity without squaring the complete cofactor;
claiming RH from the retained replay.
```