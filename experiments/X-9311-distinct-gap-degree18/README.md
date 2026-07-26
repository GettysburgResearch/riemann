# X-9311 — Complete degree-18 response cone at the distinct-gap center

PR #105 retained a directed twenty-node completed-ξ table through `x=1/2` at
the exact distinct-gap ordinate

```text
20225875608339631745427 / 2^32.
```

Every one of its 14,535 declared order-two cross-Loewner rows is strictly
positive.  That does **not** decide the complete scalar response cone generated
by all real polynomials of degree at most 18 that are nonnegative on
`[0,infinity)`.

X-9311 performs that missing finite decision.

## Proof-producing pipeline

1. Regenerate all twenty exact horizontal primitives
   `x=2^-20,...,2^-1` at 512 bits with the reviewed FLINT completed-ξ producer.
2. Reuse the target-rebound proof-grade 320-zero block from PR #105.
3. Select and certify the globally nearest 256 critical-line zero balls using
   the existing guarded prefix builder.
4. Form exact directed residual logarithm intervals at every node.
5. Construct the nineteen exact response moments

   ```text
   ell_k = L(y^k), 0 <= k <= 18.
   ```

6. Build the complete moment matrices

   ```text
   H0 = (ell_(i+j)),     0 <= i,j <= 9
   H1 = (ell_(i+j+1)),   0 <= i,j <= 8.
   ```

7. Decide the whole degree-18 half-line cone:
   - exact rational midpoint-minus-box-radius LDL for positive closure;
   - otherwise numerical discovery followed by dyadic rationalization and exact
     interval contraction of a square witness.

A strict negative in `H0` emits `P(y)=q(y)^2`.  A strict negative in `H1` emits
`P(y)=y q(y)^2`.

## Why this is higher value than another minor screen

By the one-dimensional half-line sum-of-squares theorem,

```text
P(y)>=0 on [0,infinity)
iff
P(y)=sum a_r(y)^2 + y sum b_s(y)^2.
```

Therefore `H0>=0` and `H1>=0` decide the **entire** infinite degree-bounded
response cone, including mixed-coefficient portfolios not visible in the
monomial-positive cone and not implied by finitely many order-two minors.

## Inputs

```text
zero block:
experiments/X-9301-zero-deflated-xi-modulus/results/
  pr71-ordinate-screen-broad/distinct-gap-jm26/zero-block-p256.json

reviewed source patcher:
experiments/X-9301-zero-deflated-xi-modulus/build_pr71_rs_source.py

nearest-zero builder:
experiments/X-9301-zero-deflated-xi-modulus/build_pr71_nearest_certificate.py
```

## Verdicts

```text
CERTIFIED_NEGATIVE_DEGREE18_SQUARE_WITNESS
CERTIFIED_NEGATIVE_DEGREE18_Y_SQUARE_WITNESS
CERTIFIED_POSITIVE_FULL_DEGREE18_HALF_LINE_CONE
UNRESOLVED_DEGREE18_HALF_LINE_CONE
```

No result is asserted until the immutable workflow artifacts are committed.
Any Riemann-ξ negative requires independent completed-ξ and zero-isolation
reproduction plus analytic review of the inherited canonical-product and
zero-deflation gates.
