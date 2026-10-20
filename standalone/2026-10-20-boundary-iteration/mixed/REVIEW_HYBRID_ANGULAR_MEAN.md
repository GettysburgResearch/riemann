# Scoped review of the hybrid angular mean and sector optimization

20 October 2026. Reviewed `../type_i/HYBRID_ANGULAR_MEAN.md`, SHA256
`dcf9f71ae9d828f71741ae255be7d41323b9ea3ca7ab184b1c9fbeb31de82ae8`.

Authorship scope matters: the reviewer independently audited the initial
hybrid mean and consumers (H1)--(H13). The reviewer then proposed the
fixed-displacement optimization and the enlarged normalization used in
Section 4, so this receipt is a coauthor check of that extension, not
an independent review of its own idea. The global-route agent separately
checked the enlarged normalization and exact optimizer.

The original-side cubic sieve has exactly the three terms retained in
(H1). All its cube sums remain convergent. With `0<delta<1/6`, their
row powers exceed `2 delta`, and the finite-supremum partial summation
closes. The second term also supplies the initial height control, using
the previously audited uniform gamma quotient and Gaussian three-lines
argument. The natural cutoff `C0 R^(1/2+theta) L^2` contracts uniformly
after its small losses are chosen inside the final allowances.

The fixed-displacement Type-I bound (H7) follows with the stated row
and angular exponents. Mellin inversion uses a free inner variable and
only fixed radial seminorms. Fourier summation retains the exact zero
mode and the same outer coefficients in all angular modes. The two
simple all-ratio constraints in (H10), their crossing at `a=5/7`, and
the conditional comparison (H12)--(H13) check algebraically.

For (H17), retaining the positive exponent in `(RL)^epsilon0` is
essential. Its middle weighted Abel integral is bounded by
`R^epsilon0/epsilon0`, so its contribution is precisely the required
`R^(-2 delta)` multiple of the normalized middle monomial. That finite
constant is absorbed by `C0`; it is not a new conductor power. The
original middle row exponent is no larger than `2 delta` when
`delta>=1/6`. The other row powers remain strictly greater than
`2 delta` throughout `delta<1/4`. All finite cutoffs and the initial
height argument therefore still close.

At balance, the three errors give the exact thresholds in (H19).
The identity `d2-d1=delta(1-2delta)/(4(1-delta))` makes the middle
constraint nonbinding. The first decreases and the third increases;
their crossing solves `12 delta^2-13 delta+2=0`. Its smaller root lies
strictly between `1/6` and `1/5`, inside the proved range, and yields
`d*=(sqrt(73)-1)/48`. No limiting endpoint or numerical optimization
is used. A fixed buffer in the sector width absorbs all small losses
and gives an actual power saving relative to `X Delta`.

No gap was found in these scoped arguments. This improves smooth angular
localization for the specified free-column Gauss form. It does not
prove prime-sector asymptotics, sharp-interval estimates, cancellation
of the spherical mode, or any lower numerical zero-free boundary.
