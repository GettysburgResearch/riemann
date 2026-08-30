# Architecture A: continuation checkpoint

Status: new exact single-channel reduction on
[draft PR #760](https://github.com/gfreund123/riemann/pull/760);
no new central-source estimate and no RH or GRH conclusion.

Scientific checkpoint:
1631892f0628023897a7a4ec1931f7851143b865.
The frozen input remains PR760 at
3a595dda92ef827a41e50d2395309692a93748ad.

## Result

The [complete source proof](FFPS_BETA_SECOND_DIFFERENCE_SINGLE_CHANNEL_REDUCTION.md)
retains the signed exceptional coefficients before taking positive
norms. For q=67,

    beta = (delta_1-delta_q)^(*2) * mu^(q-free).

Consequently the beta boundary field is the second multiplicative
difference of one q-free Mobius field. Its inverse is a finite sum at
every sharp prefix, with coefficients (j+1)q^(-j/2). Those coefficients
are summable, giving the uniform maximal-norm comparison

\[
 (1-q^{-1/2})^2 M_U\le M_G\le(1+q^{-1/2})^2 M_U.
\]

The assembled central-source criterion is therefore still RH-equivalent.
The positive-gate route can be stated with the central channel alone:

    COREWAVE_0 -> COREAGG_0 <=> PRIMCAR_0 -> PRIMLS_0 -> RH.

Every estimate in that displayed route remains open. The two exceptional
positive channel gates are unnecessary for this sufficient route; they
are not proved or shown to follow from its central gate.

## What has not been removed

The difficult object is still the signed, complete, central primitive
source, including the original kernels, cutoffs, coprimality, and
off-diagonal terms. The exact identity does not supply cancellation.
Replacing it by a positive envelope or a fixed-prefix Fourier multiplier
would change the theorem.

The translation-component symbol has no zero at the critical
q^(-1/2) weight. This does not turn the whole prefix-changing transform
into a same-prefix multiplier. At weight q^0 the inverse coefficients
are not summable; the positive-weight hypothesis matters.

Architecture B is unchanged by this packet. Its relative extraction,
native source realization, trace estimate, and principal binding remain
separate requirements. Current marked-place and source-algebra work is
being developed under
[PR #765](https://github.com/gfreund123/riemann/pull/765), not silently
inserted into Architecture A.

## Reproduction

The new producer and its nine focused tests authenticate the four
frozen primitive source files and their current bytes, as well as the
new note, code, and fixture. Both normal and optimized Python passed.
The bounded controls test exact source algebra, prefix inversion, and
the central scalar reassembly; they do not numerically establish the
unbounded cancellation estimate.

The continuation checkpoint additionally passed 63 tests in normal
Python and 63 under -O across these eight modules:

    tests.test_ffps_beta_second_difference_single_channel_reduction
    tests.test_ffps_primitive_core_wavelet_closure
    tests.test_ffps_primitive_core_gcd_gram_closure
    tests.test_ffps_relative_first_adams_closure
    tests.test_ffps_primitive_pair_harmonic_incidence_carleson
    tests.test_ffps_primitive_rho_tilt_convolution_isomorphism
    tests.test_ffps_boundary_field_primitive_pair_large_sieve_gate
    tests.test_ffps_boundary_field_primitive_ray_localization

All eight corresponding producers passed their canonical checks in
both modes. The new code's source/quantifier repairs have a separate
commit identity; no historical source theorem was rewritten.

This is useful earlier work retained alongside the two new programmes.
It is a reduction to the remaining problem, not a completed solution.
