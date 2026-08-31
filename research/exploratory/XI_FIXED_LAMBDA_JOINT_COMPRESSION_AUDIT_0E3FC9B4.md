# Independent audit of the fixed-lambda joint Xi compression

Status: PASS for the exact finite and conditional mathematical claims below.
Reviewed science: `0e3fc9b482f0f115a49a6209ccbfeffae640014a`.
Authoring parent: `e669d257711d8d4a6a0ab7aeb21254fd220f7dc3`.
Parent BC science: `7fbcd592042a5cc98c17d0db2fac62f8171267f2`.
Reviewer: root, not the author of the reviewed packet.
Scientific source files were not modified.

## Mathematical review

The source is the literal unrescaled Xi and ONE constant lambda64 throughout.
This is not an addition of the earlier three varying-parameter operators.
The primitive formula, reflected evaluation, chain-rule signs, fixed-parameter
differentiation, complete boundaries and local Rouche inequalities check out.
The fourteen root discs exhaust the counts 3,5,6 and every claimed
noncancellation guard is evaluated on its entire root rectangle.

The physical matrix is V G V*, for the conjugate-linear-first convention.
Finite trace is tr(G^-1 H). The raw numerator is not treated as the reduced
numerator: under the explicit component-innerness premise, the common-factor
identity gives global P_U >= P_raw. The local raw nonvanishing makes every
certified denominator zero survive any common factor, without claiming that
lambda64 avoids the global exceptional set.

The orthogonal-increment argument is valid. For nested finite kernel spaces,
D=P_after-P_before is an orthogonal projection; applying the positive operator
P_U-P_raw to D before taking its trace gives the difference of the two exact
raw traces as a lower bound. This is not subtraction of unknown reduced
lower bounds. All cross-box entries occur in the 8- and 14-node Grams.

Accepted strict bounds: joint squared Hilbert--Schmidt norm >4.298, operator
norm >0.819, and orthogonal input increment traces >1.558 and >1.641.
The raw joint trace exceeds the sum of the three raw box traces by >0.010.
The latter is a finite verified nonadditivity witness, not a general sign law.

No band projection order, native outer metric, component innerness,
high-height uniform alignment, cofinal divergence or RH conclusion follows.

## Independent source and arithmetic replay

The adjacent independent script imports NO author module. It extends the
reviewer's separately frozen BC audit method at
`3adfd9cb4013052180fb973c55deed49bad4a809`, now fixing lambda64 in all boxes
and reconstructing all five source spans and both orthogonal increments.

Two complete panels were run: 320 bits normally and 448 bits under -O.
They use reflected log-Gamma exponentiation and a unit-s Taylor variable,
then the exact i^j chain rule. Lambda is reconstructed from the derivative
of a paired log-Gamma phase, not imported from the author helper.

Each panel certifies 832 HALF-SIZED arcs per box, 2496 arcs altogether,
using 24 Taylor coefficients, the full Cauchy remainder and exact quadrant
winding rather than the author's ray-crossing count. Every refined image
hull excludes zero and overlaps its coarse source hull. Counts are again
3,5,6, with reverse-orientation controls.

The source nodes are recertified by fresh Rouche inequalities and full
noncommon guards. All point/rectangle derivatives overlap the source balls.
All five matrices (dimensions 3,5,6,8,14) are rebuilt from those fresh
rectangles and raw values. Trace is computed by LU solution of G X=H,
not by the author's inverse or Gauss--Jordan routine. The declared exact
Gaussian-integer witnesses independently prove all norm floors. Fresh
trace intervals also prove both increment floors and nonadditivity.

This is independent implementation of the source formula and finite
acceptance arithmetic, NOT an independent special-function library.
The same pinned FLINT implementation remains trusted.

The reviewed fixture LF SHA256 is
`504071292138882ad5192fc62f765edc5615c3140542c7f597651679ba682cdb`.
The two independent report payload hashes are:

- 320 bits: `ac25de013434e7e5202010a6d70160412f9a25a4380e82253bbc7d6547f59985`.
- 448 bits: `3b2123b7fd1c1349c5991a4c73531b48a5744a4a667482d8b83aa569d6d85e51`.

Large integers were transported as raw JSON text, not parsed and
re-serialized through binary64 numbers.

## Regressions and hostile controls

The 44 new, 40 BC and 36 OA tests all pass: 120 normally in 100.840 seconds,
and 120 under -O in 97.932 seconds. These authenticate all direct/transitive
sources and the frozen native runtime, and include a separately implemented
outward rational matrix route.

Both producer modes and all four fixture/manifest LF-exact emits pass.
Four additional fully resealed derived reports were rejected only after
fresh source reconstruction: changing the global parameter anchor, changing
one root's parameter anchor, overstating an increment floor, and replacing
the global metric statement with a Fourier-band Loewner claim.
Ruff and the full source-to-review whitespace checks pass.

Proof-producing arithmetic is MIXED: directed ball enclosures, exact
rational decisions and certified finite integer coverage. Radius and matrix
operations round outward; final thresholds are exact strict rationals.
The analytic Hardy interpretation remains conditional and is not
machine-formalized. The source describes these facts in prose; explicit
canonical taxonomy labels would be a useful small release metadata
successor, with its own identity and review, not a mathematical repair.

## Reproduction

Use the pinned native runtime, without editing the science:

    python -B research/exploratory/xi_fixed_lambda_joint_independent_review.py --bits 320
    python -B -O research/exploratory/xi_fixed_lambda_joint_independent_review.py --bits 448
    python -B [-O] -m unittest tests.test_xi_fixed_lambda_joint_box_compression tests.test_xi_companion_box_count_compression tests.test_xi_companion_off_axis_ball_certificates

The smallest unproved onward step remains a source-faithful cofinal
estimate. This audit certifies neither a Bessel bound for an infinite kernel
family nor divergence of any actual-Xi weighted alignment sum.
