# Independent review of the hybrid angular mean

20 October 2026. Reviewed `type_i/HYBRID_ANGULAR_MEAN.md` at SHA256
`dcf9f71ae9d828f71741ae255be7d41323b9ea3ca7ab184b1c9fbeb31de82ae8`.
The reviewer did not author that argument. The inherited analytic
reflection, finite-profile closure and original cubic large sieve
remain explicit inputs; this review checks the new normalization,
its analytic interface with those inputs, and the consumers.

No new-interface defect was found in the reviewed version.

## Mean and finite-cutoff closure

The three terms in H1 are exactly the three original-side terms U11
after substituting `Y=C0 R^(1/2+theta)L^2` and removing only the stated
arbitrarily small losses. No angular phase has been placed into a
row-dependent column coefficient: on the original side it is a common
unit-modulus phase and is admitted by the existing operator estimate.

For `0<delta<1/6`, every row power in H1 exceeds `2 delta`.
Abel summation in the exact reflected divisor average therefore gives
H3 term by term. A height translation changes each positive angular
power by at most a fixed polynomial in the contour height, which the
same Gaussian absorbs. The resulting H4 contraction factor is exactly
`Y^(-4 delta)R^(2 delta+eta)L^(8 delta)`.

The finite supremum is finite before absorption: the squared U9 bound
has height power `2-4 delta+4 eta`, and the middle term of the proposed
normalization has that main height power plus its positive allowance.
The finite row and angular cutoffs therefore suffice; no desired
conductor-uniform bound is assumed at this step. Reflection decreases
the row and reverses an angular sign already included in the finite
vector. Both cutoffs close.

The extension H16--H17 also checks. In its middle term the row power
before the loss is exactly `2 delta`, so discarding the positive row
normalization would be unjustified. The proof retains it: the relevant
Abel integral is `integral_1^R u^(-1+epsilon0) du`, bounded by
`R^epsilon0/epsilon0`. This is precisely the required power. The fixed
constant `1/epsilon0` can enter the later choice of `C0`. The other
row powers remain strictly greater than `2 delta`. The original
middle exponent `1/2-delta` is at most `2 delta` when `delta>=1/6`,
and the small cutoff loss fits inside the positive final allowance.
No extension beyond the imported analytic range `delta<1/4` is used.

## Type-I and sector consumers

Cauchy over the outer variable contributes `B^(1/2)` times the square
root of the appropriate mean. This gives every row and angular power
in H7 and H18. The ordinary inverse cube factor is on its absolute
convergence line `Re(3s-1/2)>1`, so this step introduces no zero-free
premise and no moving-conductor reciprocal assumption.

The outer coefficients stay identical in every Fourier mode. For a
periodized fixed smooth bump, summing the nonzero Fourier coefficients
against the positive angular powers costs the stated powers of the
width. Its zero Fourier coefficient is retained exactly. The third
term absorbs the constant-angular-power contribution in H9 because
the width is at most one.

I independently recomputed H10, the intersection at `a=5/7`, and the
conditional comparison H12--H13. That comparison is explicitly to H10,
not an assertion that the coarse conditional expression beats the
later refined balanced result.

At balance, H18 gives the three error terms

`X^(3/4+delta/2)`,
`X^(1/2+delta) Delta^(-1+2 delta)`, and
`X^(3/4+delta/4) Delta^(-2/3+2 delta)`.

Comparison to `X Delta` gives exactly H19. The middle threshold exceeds
the first by `delta(1-2 delta)/(4(1-delta))`, while the first decreases
and the third increases. Their intersection solves
`12 delta^2-13 delta+2=0`. The smaller root lies strictly between
`1/6` and `1/5`, hence inside the proved interval, and gives

`delta_*=(13-sqrt(73))/24`,
`d_*=(sqrt(73)-1)/48`.

Choosing this fixed displacement and a fixed positive width buffer
absorbs all subpowers. No uniform constant at an endpoint is needed.
The optimization claim is correctly restricted to these three
constraints, and the displayed value exceeds both `3/20` and `5/32`.

## Scope

This gives a stronger polynomial dependence on angular order and a
smaller admissible smooth angular width for the specified free-column
cubic Gauss form. It does not give a sharp-sector or prime asymptotic,
does not discard the spherical zero mode, and does not supply the
missing quadratic/sextic detector estimate. Neither a smaller numerical
zero-free boundary nor RH follows from this addition.
