# Hostile review specification — T-102930

Review PR #719 from the exact primewise-gauge source lock.

## Mandatory reconstruction

1. Verify the coordinatewise local product
   `(1-x)^2(1+x)^t(1+x)^(1-t)=(1-x)(1-x^2)`.
2. Differentiate with independent complementary variables and reconstruct the
   flatness identity.
3. Keep both labelled copies of `67` distinct.
4. Verify the local energy identity and its unique minimizer.
5. Check that endpoint temperatures give unique exponent allocations.
6. Confirm that endpoint choices are source-owned and occur before phases,
   Cauchy, physical collapse, and negative parts.
7. Reconstruct `EC=M^2-D^2` and verify that `D^2` starts at `x^2`.
8. Recompute the transfer series and verify its linear coefficient is zero.
9. Preserve `R-102872` and `R-102873`: factor positivity and gauge flatness do
   not orient the arithmetic product.
10. Confirm `PCOI102930`, `SGIC102890`, `CTZD102897`, and RH remain unproved.

## Immediate falsifiers

```text
changing the product detector with the primewise gauge;
using one physical 67 instead of two labels before collapse;
placing the same owner prime independently in two regions;
charging sparse endpoint energy more than once;
claiming endpoint-color averaging removes the midpoint mean;
turning the arithmetic convolution square into a pointwise scalar square;
claiming RH from the finite replay.
```
