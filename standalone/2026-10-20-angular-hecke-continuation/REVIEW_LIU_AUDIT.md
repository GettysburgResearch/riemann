# Independent review of the product, bootstrap, and balanced-unitary interfaces

Reviewer: `/root/liu_paper_audit`. Date: 20 October 2026.

**Conclusion:** No blocking mathematical gap was found in the new
product-moment, bootstrap, and descent arguments at the exact versions
listed below. This is a scoped analytical review of the changes and their
interfaces to the identified source estimates. It is not an independent
certification of the complete upstream preprint, its exceptional
representation construction, or all of its scalar certificates.

## Exact reviewed versions

| File | SHA-256 |
|---|---|
| ANGULAR_PRODUCT_MOMENT.md | `f03592bb707f7341ddabe77c4911ec7abbfcfc37292447f6d7fc6f4d235aaef6` |
| ANGULAR_BOOTSTRAP.md | `0315711623796e7f4d17c3c45a921318ab0f580a1314b46b4b423e99ec924b4c` |
| FAMILY_DESCENT.md | `737cb82d8ddb4dab21909d0093c81919edd5e6c5384cec9ab72d49191e0aa0be` |
| BALANCED_UNITARY_MOMENT_ADDENDUM.md | `35448a3f2db447b3d493f39558b414594266ae2eb2bc2359d01193baaacf5636` |

The comparison source was Baiying Liu,
[arXiv:2610.26835v1](https://arxiv.org/abs/2610.26835v1), PDF SHA-256
`5d0fd10274c8444c789b0b7925a1cd3419017fe760be3219b6be51d7fbed9bd5`.
I read the relevant source character transformations, Sections 12--14,
and the stated general-field inputs in Sections 18--19. The independent
review focused on where changing infinity type or the finite character
group could invalidate a displayed estimate.

I authored the theta/inverse notes and FINITE_ORDER_USAGE_AUDIT.md.
This report does **not** label my reading of those files an independent
review. The corresponding inverse inputs are:

- ANGULAR_THETA_AND_INVERSE.md:
  `9ed89b4acf05c6fd35e7edbc0da0f0efa00a7b2b919b766846f01da0b003aa99`;
- BALANCED_UNITARY_INVERSE_ADDENDUM.md:
  `590fef51aaf46e11c702099fd145444a58737f41d79607103c61f85c828d5e7c`.

Those inputs received separate review by the other agents, recorded in
their reports. The notation-only change from the angular integer d to
the small terminal cutoff d0 in inverse Section 5.4 was made before the
hash above was frozen.

## 1. The product moment uses a finite realized orbit correctly

The enlarged coefficient/exception group is supported in a fixed S,
whereas the analytic zero-free family allows all finite-order conductors.
This distinction is necessary. The prime-sum contour would not follow
from a zero-free statement restricted to the fixed coefficient group.

The ordinary two-transform recursion passes the fixed character on a
whole column product. Multiplicativity means that two ordinary factors
with character Omega^h retain Omega^h on their product; this operation
does not double the exponent. Whole-side conjugation reverses it, and
the other corrections have finite order. A finite initial exponent
list therefore gives a finite realized list throughout the recursion.

If the infinity vector is nonzero, membership of an exceptional
inducing character in the infinite coefficient group determines its
power uniquely from that vector. Its residual finite part then belongs
to the already fixed finite group by the definition of membership.
The fixed-character maxima are consequently over a finite list. If the
infinity vector is zero, the separate finite-order case applies.

The angular/radial coefficient is unramified at every exterior prime.
It cannot cancel nontrivial exterior Kummer inertia. The same prescribed
row valuations modulo six and the same fourth-power divisibility at a
new common simple prime remain necessary for an exceptional row. The
source sparse row count is therefore an upper bound for the enlarged
exception condition as well.

## 2. Ordinary means and reflection retain their needed estimates

For a fixed pure-angular character, the Hecke function is entire except
in the principal case. Mellin inversion to a fixed positive real line
gives the stated O(Z^epsilon) fixed-character mean, retaining the full
deleted-prime product. Its bound uses only unit-modulus Euler phases.

The leading terms of the two ordinary rectangles have the same common
norm mode and the same product of scales. Their main terms cancel
exactly. This is valid when the two profiles differ: each rectangle
retains the same ordered pair of profiles. A nontrivial angular
character has zero main term separately. The error saved by the
smallest original scale is the one used in the source centering.

Ordinary reflection has the new quotient

\[
 \prod_v\frac{\Gamma(s+b_v)}{\Gamma(1-s+b_v)},
 \qquad b_v=|ha_v|/2.
\]

Its left poles have nonpositive real parts. Some zero degrees can
give the original logarithmic small-argument kernel; positive degrees
move those poles left. The fixed shifts do not change the vertical
power. The exact natural-zero Euler restoration, conductor-times-
redundant-radical bound, and common two-scale Sobolev measure remain
present, so no conductor or row supremum has been made free.

The selected prime sums use a fixed finite character basis and complete
prime annuli. Every inducing twist used in their logarithmic derivative
belongs to the global family. On rows outside the coefficient group
it is nonprincipal. The zero-free premise, convexity on bounded real
strips, Borel--Caratheodory, and three circles give the required
subpower conductor bound before the prime contour is shifted. No
arbitrary bounded prime coefficient is substituted for this step.

The source induction inequalities and its rank order are imported with
their original hypotheses. The changed kernels, exception means, and
prime bound supply the same analytic estimates in those inequalities.

## 3. The compensated comparison does not require eta to equal one

I checked the exact source local table on pp. 94--95 and its bounds on
pp. 96--97. The table explicitly retains eta to the sixth power and
does not assume that eta has order dividing six. Its principal and
good-prime estimates use only unitary target phases. The selected
principal factor tends to minus one uniformly in those phases.

The positive identity-ray normalizer contains no target character.
There is therefore no assertion that an infinite-order character is
identically one on those primes. Changing to a detector presentation
inserts the inverse fixed-character coefficient into the original
physical prime factor; that coefficient belongs to the stated M2
basis. The theta average's additive Gram coefficient remains one.

The numerator in source (13.11) is exactly L(w,chi_u). It stays finite
order when the denominator target becomes angular. The conductor
deficit, gamma factors, approximate functional equation, and amplified
numerator average in Section 14 remain the relevant source formulas.
For a nonunit sixth-power-free row, exterior ramification also keeps
this numerator presentation outside the enlarged S-supported exception
group.

The preliminary 11/12 family bound precedes every improved prime-bound
premise. The successive comparisons use the presumed global supremum
as their temporary zero-free premise and contradict it with a strictly
smaller common continuation boundary. Their numerical gap is chosen
before target-dependent profile orders and thresholds. This is enough
for the supremum argument without uniform constants in growing
angular degree or an attained rightmost zero.

## 4. The balanced radial extension has the correct signs and pole scope

The BALANCED_UNITARY_MOMENT addendum uses the same local-weight
convention as the inverse proof. If the local weight has radial
parameter rho, the completed ordinary gamma factor is
Gamma(s+b−i rho). Reflection gives

\[
 \frac{\Gamma(s+b+i\rho)}{\Gamma(1-s+b-i\rho)}.
\]

At s=sigma+iT, its gamma arguments have imaginary parts T+rho and
−T−rho. Their exponential factors cancel exactly; near a shifted
bounded frequency one uses a fixed contour bound. The pole at
s=−b−n−i rho contributes x^(b+n+i rho) times fixed logarithmic
powers. Its absolute size is no worse than the pure-angular kernel.

Removing the common norm component makes the radial parameters sum
to zero. A balanced family member that is a pure norm character must
then have norm parameter zero. Thus only the actual principal
character has a pole in the fixed-character means. This normalization
is essential to the simple principal-only add-back statement; it has
not been omitted.

The joint infinity vector determines each realized power just as the
angular vector did. The coefficient transformations, exterior inertia
count, and full-conductor analytic family therefore retain the same
scope. The new local profile and constant-term argument are a separate
inverse input, specifically the addendum identified by its hash above;
they are not assumed as an unnamed angular moment theorem.

## 5. Base change and the normalization over real places

The extension F=K(zeta12) is finite abelian. The Hecke base-change
identity is a positive product, with no negative exponents. For a
nonzero balanced infinity type, none of its factors is a pure norm
character, so none has a pole that could cancel a zero. The zero-type
case is finite order after a common norm twist and is treated
separately. Finite Euler omissions have no zero in a positive real
half-plane.

For a degree n extension to the totally complex F, a real place of K
has n/2 complex places above it, while a complex place has n. The
normalized local norm from complex to real is |z|^2, so the radial
coefficient is copied without an extra factor of two. This gives the
stated mean

\[
 \frac{\sum_{v\mid\infty}[K_v:\mathbb R]\gamma_v}{[K:\mathbb Q]},
\]

and proves that balancing commutes with this base change.

If K does not contain E=Q(sqrt(−3)), an automorphism over K conjugates
E. The pulled-back character is invariant under this automorphism,
whereas the Eisenstein angular type changes sign. Neither excluded
balanced type is possible. If K contains E, base change repeats its
complex types and preserves the stated nonresonance. A quotient with
the same balanced infinity type has trivial infinity type and hence
finite order at fixed finite conductor.

The final exclusions are consequently exactly the two resonant
Eisenstein infinity types, with finite twists and common norm twists,
over fields containing E. No limit in the radial parameter is used
to include those excluded types. The proposed result extends the
covered Hecke families; it does not lower the numerical finite-order
boundary B_flat itself.
