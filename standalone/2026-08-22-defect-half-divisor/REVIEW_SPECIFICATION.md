# Review specification — T-102700

Frozen base:

```text
PR #718
41a087387812e89ce800c59f43582799fee24782
```

Mandatory checks:

1. Reconstruct the arithmetic square lift coefficientwise.
2. Verify `lambda*lambda=beta` with the duplicate 67 label.
3. Verify `(lambda-lambda_square)*(lambda+lambda_square)`.
4. Recompute the ratio-four spline multiplier and
   `Phi_*=2 A_- *_M A`.
5. Verify the two-field finite Fubini identity.
6. Recompute the local square-sum Euler exponent `1/4`.
7. Verify the divisor-bound same-product estimate.
8. Derive the physical Gram and support restriction.
9. Verify that every cofactor prime is below `sqrt(X)` and that `(p,a)->p a^2`
   is injective.
10. Reconstruct the same-owner harmonic-window bound.
11. Confirm no cross-owner off-diagonal estimate is smuggled into the diagonal
   proof.
12. Confirm `HDNC102703` and RH remain unproved.
