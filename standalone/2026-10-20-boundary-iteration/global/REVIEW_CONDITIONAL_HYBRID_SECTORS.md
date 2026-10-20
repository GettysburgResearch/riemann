# Independent review of the conditional hybrid sectors

20 October 2026. Reviewed `type_i/CONDITIONAL_HYBRID_SECTORS.md`,
SHA256 `dfd11daedbbd407b4a53e085cb2d38384ca44559cbf8c5abe41651ff9dca606e`.
The reviewer did not author that argument. The exact reflected cubic
family, the hybrid mean, and the stated common-family reciprocal
theorem remain its explicit analytic inputs.

No new-interface defect was found in the reviewed version.

## Reflection, reciprocal and contour

The chosen line satisfies `p>(2 beta+1)/6>=1/3`, hence
`delta=1/2-p` lies strictly between zero and `1/6`. This is inside
the original hybrid theorem H2, without the enlarged normalization.
Its three row exponents exceed `2 delta`. The reflected mean multiplies
each normalized term by `B^(2 delta)L^(8 delta)` after partial
summation. Substitution of `delta=1/2-p` gives respectively

`B^(2-2p)L^(4-8p)`,
`B^(1-p)L^(4-4p)`, and
`B^(3/2-p)L^(10/3-4p)`.

Thus CH2 keeps all three terms with their correct conductor and
angular exponents. No term is removed through a positivity argument.

The cube Hecke factor has argument `3p-1/2+3it`, with a fixed strict
gap to the common boundary. Its angular conductor has the stated
quadratic size, and its finite conductor is fixed. The reciprocal
theorem therefore costs an arbitrarily small angular subpower and
the deleted row primes cost a row subpower. The premise is explicitly
for the actual characters in these factors; it is not inferred from
a theorem about unrelated finite-order characters.

On the whole strip to the right of this line, the cube reciprocal
has no zero denominator. A possible principal pole gives a zero of
the inverse, not an extra contour pole. The nonzero angular completed
series is entire by the imported theorem. These facts justify the
Mellin shift used here. The line and its gap are fixed before length
or angular limits; no endpoint uniformity is required.

## Consumers and comparisons

Cauchy over the outer variable contributes `B^(1/2)` to each square
root of CH2, giving exactly CH3. The common bounded outer coefficient
is retained in every Fourier mode. Fixed radial Mellin decay absorbs
the polynomial height bounds without a number of derivatives growing
with the angular order. The inner variable remains unrestricted by
new arithmetic coefficients.

I independently derived all three Fourier width thresholds in CH5
from CH3. Their positive angular powers give the stated inverse-width
costs. The zero Fourier coefficient is kept exactly. Approaching the
limiting value of `p` with a fixed buffer for the requested exponent
loss proves CH6 without asserting an endpoint reciprocal estimate.

The comparisons CH7--CH10 also check. With common denominator
`2(7-4 beta)(7-2 beta)`, the difference `xi_1-xi_3` has numerator
`a(1+beta)(7-4 beta)-7(1-beta)`. For `a>=5/9` it is positive
throughout `1/2<=beta<1`; at `a=5/9,beta=1/2` it is already `2/3`.
The crossing of the remaining two lines is precisely
`a_c=(23-8 beta)/(3(11-4 beta))`, strictly between `5/9` and `5/7`.

I recomputed the differences on each of the three intervals in CH9
and CH10, including the intermediate numerator at `a=5/7`.
They prove strict improvement for every `a>5/9` and equality at
`a=5/9`. The comparison is against the best of the displayed
unconditional fixed-displacement inequalities on this range: the
third threshold cannot increase for `a>=5/9`, and for `a>=5/7`
the middle threshold cannot increase on either side of `delta=1/6`.
The new all-ratio optimization records the same fact separately.

The balanced unconditional exponent is correctly retained. At `a=1`
the minimum reproduces `(5-2 beta)/(4(4-beta))`. The note makes no
assertion of global optimality over other methods or other contours.

## Scope

This is a conditional improvement in smooth angular localization for
the stated free-column cubic Gauss form, assuming the common boundary
for its actual cube factors. It neither lowers that boundary nor
provides a prime-sector theorem. It preserves the spherical zero
mode and does not replace the moving quadratic/sextic detector by a
pure cubic estimate.
