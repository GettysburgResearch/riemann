# T104630 hostile reconstruction handoff

## Frozen imports

```text
PR #731 head:
433490c133b26bce4163f4edf7ad04aeda9d33e3

PR #729 head:
e399156475cac82199275ea1470eaa83ec6ebbc3
```

Review in this order:

1. `L-104630`: rederive the polynomial `(v-u)(v^5-u^5)` and the
   generalized-Maxwell moments.
2. Recheck the monotone-likelihood argument against the exact Xi curvature
   constant `20476/2345`.
3. `L-104631`: verify the strong Calderón identity and the one-zero beta-prime
   scale law.
4. Verify the product-model tail estimate uses a decreasing integrated tail
   multiplier and causal contraction.
5. `L-104632`: check the operator order, degree `<=2N`, and every rational
   constant.
6. Reconstruct the imported deep charge `3/40` and fifth input `997/1000`.
7. Treat `FRACTRANS104630` as open.

Immediate falsifiers:

```text
a missing factor two in the x=(v-u)/2 change;
a reference hyperbolic moment larger than M3;
failure of the product-model tail profile to be decreasing;
total shallow denominator degree exceeding 2N;
any promotion of FRACTRANS104630 to proved.
```
