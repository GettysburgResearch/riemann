# Hostile review specification — T-102910

Review the live PR #719 head containing this packet.

Mandatory checks:

1. Reconstruct the geometric completion local factor
   `(1-x)(1+x)^t` and the exact factorization
   `zeta(z)^(t-1) zeta(2z)^(-t)`.
2. Keep the second labelled copy of `67`.
3. Recompute the square-source exponent `2t-2`.
4. Check the Gamma-function sign on `(-2,-1)` and `(-1,0)`.
5. Verify that `t=1/2` gives exactly `eta*eta=beta*beta_square`.
6. Reconstruct the uniform Hankel expansion and the
   Vinogradov--Korobov remainder in `L-102896`.
7. Check the derivative lower and upper bounds on the transition layer.
8. Verify uniqueness of `vartheta(X)` only in the declared thin layer.
9. Reconstruct the mean-value translation in `L-102897`.
10. Do not infer the midpoint sign from fixed strict-temperature signs.
11. Confirm `CTZD102897`, `GMBC102893`, and RH remain unproved.

Immediate falsifiers:

```text
using the affine partial completion instead of the geometric family;
dropping the duplicate-67 factor;
claiming uniform eventual sign at t=1/2;
using a zero-dependent detector;
claiming the transition root lies on a fixed side;
promoting a numerical root scan to proof;
claiming RH from the replay.
```
