# M-96000 — Hostile reconstruction protocol for the prime-sieved row route

Review in this order.

1. Reconstruct `L-94200.1--.6` from the canonical row definition.
2. Search for a negative value of
   \[
   \sum_{d\mid P_r}\mu(d)d^{-1/2}Q_{Y/d}(j).
   \]
3. Demand an explicit enumeration of every divisor-cube frontier template.
4. Check that no positive reservoir is reused by two residual paths.
5. Verify the finite identity from the full Möbius row to the initial-prime segment in `L-94201`.
6. Recompute `L-96000.4--.8`, including the powers of `k` after the substitution `X=kY`.
7. Check cancellation at the zeta pole `z=1` and analyticity on the positive real `s`-axis.
8. Recompute the coefficient
   \[
   -z(z+1)/(1-z)
   \]
   in `L-96001`.
9. Check the hypotheses and orientation of Landau's theorem.
10. Verify that no endpoint benchmark or RH-equivalent arithmetic estimate is imported.

Immediate falsifiers:

```text
one negative finite sieve row;
one unowned or double-owned frontier reservoir;
a missing k^(-s-1/2) factor;
a zero of every P_j at one open-strip point;
a positive-real singularity of the continued transform;
a sign-changing f_j;
a hidden native benchmark assumption.
```
