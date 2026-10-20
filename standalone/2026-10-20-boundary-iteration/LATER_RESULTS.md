# Later results, source comparisons, and remaining gaps

20 October 2026. These additions follow the initial frozen research
commit `9bf9e21f95669abdcaa74e3b2ba54fb93e779503`. All analytic assertions
remain proposed and source-dependent. None lowers the numerical
zero-free boundary or proves RH.

## A further cubic family

The [opposite-cubic joint mean](mixed/OPPOSITE_CUBIC_JOINT_MEAN.md)
uses the actual two-conductor character `chi_c(S r^2)` in de Faveri's
Proposition 8.1. The positive cubic conductor is a fixed point of the
theta reflection, while the negative cubic conductor produces the
already audited signed divisor sum. This gives a closed joint mean
with explicit polynomial angular cost. For two conductor lengths both
N, it is

\[
                 N^{2+\epsilon}+N^{5/2-3\delta+\epsilon}
\]

on `Re s=1/2+delta`, for `0<delta<2/9`, with the stated height factor.
At `delta=1/6` the mean has natural-count size for every ratio of the
two conductor lengths: `F_(1/6)(R,H)` is bounded by a constant times
`RH`. For `R<=H` its three terms are `RH,RH,R^(1/2)H`; for `R>=H`
they are `RH,R^(2/3)H^(4/3),R^(5/6)H^(2/3)`, each at most `RH`.
Thus the general free-column bound on this line is `A^(2/3)RH`, with
the stated subpowers and angular factor. The corresponding free
inner column of length N gives a trilinear bound `N^(8/3+epsilon)`, or
`X^(8/9+epsilon)` when `X=N^3`. The inner variable is not prime-restricted.
The direct source comparisons checked do not reproduce this improvement;
no exhaustive literature-priority claim is made. Independent reviews
are [here](global/REVIEW_OPPOSITE_CUBIC_MEAN.md) and
[here](type_i/REVIEW_OPPOSITE_CUBIC.md).

## Two signed partial estimates

The [long-common-divisor estimate](global/SIGNED_MOBIUS_GCD_TAIL.md)
keeps the exact Mobius sign before the source's positive enlargement.
For original inverse lengths H,D, overlap length C, and common-divisor
length S, its complete unselected block is bounded by

\[
                 (DHq_j)^\epsilon D^2 C^{-2}S^{\beta-2},
\]

with fixed smooth-seminorm factors. It needs a common zero-free
half-plane only for the actual finite-order cubic/ray family and norm
translates; the inherited finite-order boundary suffices, subject to
its source dependencies. It gives a nontrivial long-divisor range.
The short-divisor sector remains. Its [independent review](mixed/REVIEW_SIGNED_MOBIUS_GCD_TAIL.md)
checks the character, full kernel and frequency count.

The [signed complement identity](type_i/SIGNED_MOBIUS_COMPLEMENT.md)
comes from the exact coherent cubic reflection with outer Mobius
coefficients. Its local factor `1+x-y` has an exact factorization into
three Hecke L-functions and an absolutely convergent Euler product.
Under the common zero-free premise for those actual angular and finite
characters, the smooth complementary sum has exponent

\[
 \tau_\beta(\delta)=\max\{\beta/2-1/2+2\delta,
                         \beta-1/2-\delta,\delta/2\}.
\]

For `beta>=2/3`, its optimal isolated exponent is `5 beta/6-1/2`,
at `delta=beta/6`. Combined with the pure cubic mean this saves a power
on the exact reflected tail with long complementary variable. The
full-divisor term, where that variable is one, remains unsaved.
An [independent review](global/REVIEW_SIGNED_COMPLEMENT.md) checks the
Euler product, deleted factors, contours and tail consumer.

These two results concern different signed expressions. Neither
completes the centered inverse estimate. The
[reciprocal kernel identity](global/RECIPROCAL_PROJECTOR_KERNEL.md)
and its [review](mixed/REVIEW_RECIPROCAL_PROJECTOR.md) identify a
remaining dependence jointly on both residual columns; replacing it
by arbitrary bounded coefficients loses the relevant cancellation.

## Smooth angular localization

The [conditional sector consumer](type_i/CONDITIONAL_ANGULAR_SECTORS.md)
uses the reflected cubic mean and uniform inverse cube factor. With
`A=X^a`, `B=X^(1-a)`, its smooth discrepancy from the exact zero-angular
mode saves a power at widths at least `X^(-xi_beta(a)+eta)`, where

\[
 \xi_\beta(a)=\frac{(7-4\beta)a-2(1-\beta)}{4(4-\beta)}.
\]

This improves the unconditional exponent `a/4` exactly for `a>2/3`.
For `a=1` and the proposed common boundary, the exponent is about
0.2600 instead of 0.25. The balanced width remains `X^(-1/8+eta)`.
The [independent consumer review](type_i/REVIEW_CONDITIONAL_ANGULAR_SECTORS.md)
keeps the zero mode and all positive contour buffers. This is not a
prime-counting assertion.

## A comparison that withdrew a claimed improvement

The [unequal-cutoff quadratic/sextic proof](mixed/JOINT_PAIR_UNEQUAL_CUTOFFS.md)
gives a balanced exponent 28/11 near the half-line, better than summing
our earlier fixed-conductor estimate. However, the same exponent is
already recoverable from rStation paper 5 equation (11.4) and the sextic
operator sieve. It is retained as a direct proof from a smaller set of
inputs, with an [explicit angular extension](type_i/JOINT_ANGULAR_UNIFORMITY.md),
and is not advertised as a new best conductor bound. The
[source audit](global/REVIEW_JOINT_PAIR.md) and
[final proof review](type_i/REVIEW_JOINT_PAIR.md) record that correction.
The analogous [one-conductor derivation](type_i/ASYMMETRIC_CONDUCTOR_PAIR.md)
also records its comparison and its actual quadratic character family.

By contrast, the [pure cubic comparison](type_i/PURE_CUBIC_SOURCE_COMPARISON.md)
finds only `R+R^(6/5-8 delta/5)` from that supplied completed-label
estimate and the generic cubic sieve. It therefore does not remove the
proposed `R^(1+epsilon)` improvement near the half-line.

## Authorship and review limits

The root agent and component authors jointly developed several of these
ideas; root assembly checks are not called independent reviews of those
proofs. The linked independent reviews were performed by agents who did
not author the reviewed argument. The initial exact-head reviews bind
the initial commit, not these later additions. All current source bytes
are listed in the refreshed manifest; finite algebra replay cannot
certify the analytic inputs or an infinite proof.
