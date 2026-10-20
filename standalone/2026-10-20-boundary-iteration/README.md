# Boundary iteration: angular cancellation and spherical residues

20 October 2026. **Proposed source-dependent research; not integrated.**
This continues the research head
`7f6ff9dae8d3473a5835a5cbe7308148b8b3c1a0` (PR #1009).
The upstream analytic results remain dependencies, not theorems certified by
the finite checks in this packet. RH remains unproved.

The principal new cancellation claim is the angular completed cubic mean

\[
\sum_{Nr\le R}^{*}|Q_r(\sigma+it)|^2
\ll R^{1+\epsilon}(1+|t|)^C,\qquad 1/2<\sigma<3/4,
\]

for every fixed nonzero angular degree and its four realized ramified
profiles. It implies a balanced cubic bilinear estimate
\(X^{3/4+\epsilon}\), improving the earlier \(X^{5/6+\epsilon}\)
estimate for that form. The proof resums the complete dual and uses an
explicit invertible minor of the actual cusp table. It does not cover the
moving quadratic conductor in the binding sextic detector.

The second direction supplies the previously missing spherical residues,
their selected-prime action, and a compatible finite-place modification
of the physical direct probe. It gives a proposed extension of the same
boundary to **every unitary Hecke character over every number field**,
including the resonant angular types omitted by the preceding packet.
The complete statement and dependencies are in
[ALL_UNITARY_REFINED_BOUNDARY.md](global/ALL_UNITARY_REFINED_BOUNDARY.md).
These are extensions of the covered family. **No smaller numerical value
than \(B_\flat=0.874886647039964\ldots\) is proved here.**

## Main arguments

| Object | New statement or role | Scope |
|---|---|---|
| [Angular second moment](average/ANGULAR_SELF_ABSORPTION.md) | Row-scale mean and balanced \(X^{3/4+\epsilon}\) bilinear estimate | Fixed nonzero angular degree over the Eisenstein field; source-dependent analytic proof |
| [Hybrid angular mean](type_i/HYBRID_ANGULAR_MEAN.md) | Retains all three conductor/angular terms; balanced smooth-sector width \(X^{-d_*+\eta}\), where \(d_*=(\sqrt{73}-1)/48\approx0.1571667\), improving the earlier \(1/8\) | Uniform free-column cubic form; exact zero-angular term retained; no prime-sector assertion |
| [Finite profile closure](type_i/FINITE_PROFILE_CLOSURE.md) | Actual 27 cusp Mellins close on four scalar channels; exact three-by-three extraction | Finite local algebra and source-table audit |
| [Complete dual resummation](type_i/DUAL_RESUMMATION.md) | Restores the deleted cube factors with their signs | Exact local algebra; load-bearing for absorption |
| [Quadratic pair](mixed/QUADRATIC_PAIR_ABSORPTION.md) | Completed mean for a fixed moving quadratic conductor, with its explicit conductor cost | Stronger Type I estimate; insufficient in the binding mixed range |
| [Opposite cubic conductors](mixed/OPPOSITE_CUBIC_JOINT_MEAN.md) | Joint natural-count mean on Re s=2/3 for all conductor ratios, and a balanced free-column X^(8/9+epsilon) consumer | Two cubic orientations; explicit polynomial angular cost |
| [Spherical residue](global/ALL_FIELD_SPHERICAL_RESIDUE.md) | Digit support, moving-row decay, actual finite class transport, and selected multiplier \(1/Np\) | Initially fields containing the twelfth roots of unity; field descent stated separately |
| [Guarded physical probe](global/ALL_FIELD_AUXILIARY_GUARD.md) | Removes both spherical constants while preserving the original reciprocal and its principal frequency | Exact fixed-place construction; independently reviewed |
| [Full unitary boundary](global/ALL_UNITARY_REFINED_BOUNDARY.md) | Extends the inherited \(B_\flat\) to all unitary Hecke characters over all number fields | Proposed source-dependent assembly, with open half-plane and poles stated explicitly |
| [Uniform reciprocal](uniform/UNIFORM_INVERSE_AND_STRIPPING.md) | Conductor-uniform reciprocal/Mobius estimates and signed principal-factor stripping | Conditional on a common boundary for the actual unitary family |
| [Numerator barriers](type_i/NUMERATOR_MOMENT_BARRIERS.md) | Second/higher-moment and local-buffer hybrids do not improve the supplied endpoint system | Exact restricted-system obstructions, not a general impossibility theorem |
| [Mixed terminal interface](mixed/TERMINAL_INTERFACE.md) | Identifies the row-dependent coefficients and the missing conductor average | Open analytic interface |
| [Tangent certificate](scalar/TANGENT_CERTIFICATE.md) | Independently reconstructs the critical algebra, exact continuous parameter cover, and endpoint root for the closing scalar step | Exact rational replay; does not certify its analytic inputs |

The [guarded spherical mean](global/GUARDED_SPHERICAL_MEAN.md) extends
the quadratic-pair estimate to angular degree zero when a nontrivial
quadratic conductor removes the residue. Fixed conductor again gives
the balanced \(X^{3/4+\epsilon}\) bound. The
[uniform consequences](uniform/FULL_FAMILY_CONSEQUENCES.md) explain
conductor-uniform Mobius estimates and Eisenstein prime sectors under
the proposed full-family boundary.

The one-pass [averaged Type I argument](type_i/AVERAGED_TYPE_I.md) and its
[quadratic extension](type_i/QUADRATIC_TWIST_EXTENSION.md) remain useful
independent estimates. They do not require the complete finite closure
used by the stronger absorption theorem.

## Corrections and limits

An exploratory cusp minor using rows 20, 22, 26 was transcribed incorrectly
and withdrawn during this session. The final extraction uses the actual
rows **22, 26, 27**. Its matrix satisfies \(MM^*=3I\); the independent
[cusp audit](mixed/AUDIT_CUSP_REFLECTION.md) also checks the full reflection,
and its negative controls reject the withdrawn minor. There is no claim
that literal coefficient shifts preserve the cusp table: closure is at
the Mellin-series level.

An apparent improvement from the additive Gauss Gram estimate was also
rejected: Liu's current equation (13.7) already includes that estimate.
[The comparison](mixed/ADDITIVE_GRAM_COMPARISON.md) identifies the exact
overlap. Subtracting the same saving twice would produce a false boundary.

The canonical marked mean improves some length ranges, but at the binding
edge its exponent returns to the inherited value. A natural joint mean
without a quadratic-conductor loss would itself still need a separate
argument to improve the final detector. The complete length polygon and
the row-dependent coefficient restrictions must be respected.

The latest [structured-prime comparison](mixed/XU_SANG_V2_CONSUMER_AUDIT.md)
and [unequal-length deduction](type_i/UNEQUAL_STRUCTURED_PRIME_MOMENTS.md)
also fail to supply a new saving in that binding range. The
[conditional sensitivity](mixed/CONDITIONAL_BOUNDARY_SENSITIVITY.md) and
[weaker centered target](mixed/WEAKER_CENTERED_TARGET.md) quantify what
a genuine signed inverse improvement would buy; their missing analytic
premises are not claimed as results.

## Review boundary

The component reviews bind file hashes and state their scope. Finite
checkers authenticate the displayed algebra and stated finite coverage;
they do not prove contour shifts, theta continuation, the upstream
canonical recursion, or a zero-free theorem. The repository's integrated
scientific status is unchanged by this standalone packet.

Use [CLAIMS.md](CLAIMS.md) for the exact claim map,
[VALIDATION.md](VALIDATION.md) for replay and its limits, and
[NEXT_STEPS.md](NEXT_STEPS.md) for the remaining numerical-boundary
targets. The scoped [assembly review](GLOBAL_ASSEMBLY_REVIEW.md)
distinguishes independent checks from coauthor checks.
The [final exact-head audit](FINAL_HYBRID_HEAD_REVIEW.md) binds the
complete mathematical head, including the later hybrid estimates.

The [later results and comparisons](LATER_RESULTS.md) add a signed
long-divisor estimate, an exact Mobius-complement Euler product, and
stronger unconditional and conditional smooth angular estimates. They also
record a rejected novelty claim: the joint quadratic/sextic exponent
28/11 already follows from a stronger supplied estimate. Its new proof
uses fewer analytic inputs, but does not improve the best bound
recoverable from that source. The [pure cubic source comparison](type_i/PURE_CUBIC_SOURCE_COMPARISON.md)
explains why that overlap does not remove the main cubic improvement.
