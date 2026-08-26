# Hostile review specification — T-102920

Review the exact PR #719 head recorded in the source lock.

Mandatory checks:

1. Reconstruct the local identity
   `(1-x)(1+x)^t (1-x)(1+x)^(1-t)=(1-x)^2(1+x)`.
2. Differentiate it and verify the flat tangent current.
3. Keep the two labelled copies of 67 distinct.
4. Reconstruct the common-mother polarized integral and its Wronskian.
5. Verify the local source-energy expansion and the exponents
   `(1-t)^2`, `t^2`.
6. Verify that `t=1/2` uniquely minimizes the combined exponent.
7. Verify first-chaos sum `-1` and imbalance `2t-1`.
8. Reconstruct the positive-inverse generator identity
   `omega*dot(Gamma)=2 beta*Lambda`.
9. Separate the first-prime term from prime powers `k>=2`.
10. Do not promote the polylog operator norm of the latter to a one-sided
    estimate for the native field.
11. Reconstruct the source-level secant formula at the transition zero.
12. Retain `R-102872`: factor positivity is not product positivity.
13. Confirm CTZD, SGIC and RH remain unproved.

Immediate falsifiers:

```text
replacing arithmetic convolution by pointwise multiplication;
using a temperature depending on a hypothetical zero;
assigning one source region to two temperatures;
dropping the antisymmetric Wronskian without exact convolution;
calling the higher-prime-power gauge an absolute sign theorem;
claiming RH from the finite replay.
```
