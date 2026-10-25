# Independent internal review of the continuation audit

Reviewer: `/root/middle_joint`, independently of the author `/root`.
Reviewed file: `ATTEMPT_AUDIT.md`, SHA256
`5209ac000a0646d07fc923f3a9c943236489c2645763c14f713d6993830a08ea`.

**Disposition: accepted within its stated imported analytic scope.** The
simultaneous witness localization is valid. The withdrawn raw-backtrack
normalization is correctly identified as invalid. Neither statement
supplies the missing residual estimate or a new zero-free region.

This is an internal review. It is not external peer review or a formal
verification of the external cap, moment and buffered-bin framework. The
reviewer authored the companion `MIDDLE_JOINT.md`; that dependency overlap
is disclosed. The present review concerns the additional continuum-scale
argument and its exact coefficient return.

## 1. Original kernel normalization

I checked the definition immediately before the first operator in the
supplied HLC paper, page 18, against its extracted text. Its prefactor is
`d_0/D` multiplied by `eta(a/Y) eta(b/Y) psi_1(t/Y)` and the stated
centered bracket and damping. The denominator Y in the cutoff arguments
is not another scalar factor `1/Y`.

Consequently the proposed original-entry estimate `O(1/Y)` does not
follow from that formula. Copying the normalization of a separately
converted clean operator would require its entire changed measure and
coordinate system. The audit correctly withdraws that argument. It also
correctly distinguishes a bound on the diagonal of `T T*` from a norm
bound for the complete operator or a signed trace. The separate integer
memory-return theorem remains a dependency of the HLC note; no false
raw-operator contraction is used in this audit's scale argument.

## 2. Uniformity of the two pointwise terms

The range `0<kappa<4/25` and `r>=29/25` ensures that
`[U,D/U^kappa]` is a nonempty interval of bounded-power scales. On it,
`T/D<=U^(-kappa)`. The complete ratio-head estimate therefore gives
`(2T/D)^(1/8)<=2^(1/8)U^(-kappa/8)`; the fixed factor two is harmless.
The far-truncated coefficient proof gives the same gain for the lower
overlap because its two scales have ratio exactly `U^(-kappa)`.

Both estimates use the same actual buffered delta, original primitive
character, natural zeros and common profile. The real Mellin cutoffs
vary only inside prescribed bounded-power ranges. The logarithmic
derivative bounds of the common cutoffs are uniform, and the scalar
contour losses can be allocated uniformly over T. The family frequency
arguments continue to share a single buffer. No extra copy of the
buffer, arbitrary row-dependent coefficient vector, or different
character presentation is introduced by allowing T to vary.

## 3. The continuum supremum is justified

Differentiating `G_T(R)=1-chi(R/T)` in log T gives exactly
`(R/T) chi'(R/T)`. Its support is the transition `T<R<2T`, and it
has uniformly bounded logarithmic derivatives of every fixed required
order. Since T>=U, both this derivative and the original far weight
retain the long actual inverse length interval
`[1-alpha,r-alpha]+O(1/log U)` with alpha=2/125. The original far
proof therefore applies with its unchanged 1/750 saving and fixed
profile orders. It does not require positivity of either cutoff.

The interval in log T has length O(log U). For sufficiently large U
one can cover it by O(log U) intervals of fixed unit length contained
in the allowed interval, shifting the final interval inward when
needed. The remaining bounded initial range is absorbed in the
constants, which may depend on the prescribed fixed kappa. This avoids
a degenerating Sobolev constant from an arbitrarily short final piece.

On each such interval the standard one-dimensional H^1 inequality
bounds the supremum squared by the integral of the square of the
function and its first derivative. The row sum is nonnegative, so it
can be taken before the integral. Summing these bounds pays only the
logarithmic number of intervals. This proves the asserted mean of the
continuum supremum. It is stronger than a union bound over a sampled
grid and requires no independence among scales.

The allowed finite-dimensional detector-profile parameters can be
included in the same Sobolev calculation. Their derivative and height
orders must be fixed first and their small polynomial-height exponent
chosen afterward, exactly as stated. The proof does not provide a
supremum over arbitrary test vectors on different rows.

## 4. The exceptional count and simultaneous lower bound

Within a fixed buffered class, compare the supremum mean with the
square of one quarter of the specified witness threshold. Chebyshev
then gives exactly the exponent
`e_0(r)-delta*r-1/750+epsilon+omega`. The count requires weight one
on that class, or a weight bounded below there; the note explicitly
states this condition.

Outside this one exceptional set, the far expression is below that
quarter threshold at every T in the continuum. The two pointwise
terms are each below one eighth of the witness threshold when
`epsilon+omega/2<kappa/8`. Applying the triangle inequality to the
exact four-term identity leaves at least one half for the corner at
**every** allowed T. The signs in the identity do not affect this
lower bound. There is no separate exceptional set secretly assigned
to each scale.

## 5. The returned coefficients repeat, so orthogonality is not available

I re-derived the exact coefficient identity from the finite divisor
return:

`D_C(T)(m) = D_(H_T,1)(m) - D_(K_T,G_T)(m) - A(m) chi(Nm/T)`.

The full support through 8D and the natural `(kd,P)=1` condition stay
present before grouping the divisors. The scalar coefficient bounds
and harmonic k summation give the two errors
`(2T/D)^theta` and `U^(-kappa*theta)` uniformly over the stated
scale interval. For every natural-unit m with Nm<=U, the low cutoff
is identically one at all those T. Hence all returned corners have
the same leading coefficient `-A(m)`, as claimed.

This is a coefficient identity, not a lower bound for the signed row
means. It prevents a purported argument based on disjoint primal
supports or independent copies of the old critical coefficient. The
finite number of disjoint exponent shells, and the logarithmic number
of ordinary dyadic scales, do not themselves yield a fixed-power
saving. An orthogonality or correlation estimate would be an additional
mathematical input, not a consequence of the simultaneous statement.

I found no missing step in the continuum localization or its stated
limitations after these checks. The remaining arithmetic estimate is
still open.
