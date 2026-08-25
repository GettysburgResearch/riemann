# Hostile review specification — T-102940 / T-102950

Review the live PR #719 head frozen by the accompanying source lock.

## Mandatory reconstruction

1. Expand `F_t` and `G_t` to first order and verify the antisymmetric coefficient exactly.
2. Check that `x tensor 1 - 1 tensor x` lies in the arithmetic-convolution kernel.
3. Verify `pi(V_t)=EC-M^2=-x^2(1-x)^2/4`.
4. Reconstruct the orthogonal energy identity
   `|t-1|^2+|t|^2=1/2+2|t-1/2|^2`.
5. Tensor the local decomposition and verify that every term containing one flat coordinate is globally convolution-null.
6. Verify that every surviving nonharmonic local transfer begins at degree two.
7. Reconstruct the critical residue functional and check its value `-1` on every complementary factorization.
8. Expand the logarithmic generator and verify coefficient positivity.
9. Reconstruct the positive inverse coefficient formula
   `w_j=[12j+20+(3j+7)(-1/2)^j]/27`.
10. Verify the global factorization `V(z)=zeta(z)G_V(z)` and the logarithmic inverse mass.
11. Derive the exact renewal equation from arithmetic convolution Fubini.
12. Confirm that the renewal mass is not a contraction at the critical boundary.
13. Confirm that `HMO102940`, `CHR102950`, `PCOI102930`, and RH remain unproved.

## Immediate falsifiers

```text
claiming that a flat-null tensor changes the convolved source;
claiming that an x^2 transfer removes the first-chaos residue;
using endpoint-color variance to replace the harmonic mean;
treating positive inverse coefficients as positivity of the source;
normalizing the renewal at a point where its zeta pole diverges;
claiming RH from the retained finite replay.
```
