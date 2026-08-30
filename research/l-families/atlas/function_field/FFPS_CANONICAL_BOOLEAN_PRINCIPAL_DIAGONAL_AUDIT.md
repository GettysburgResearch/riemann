# Independent audit: canonical Boolean principal diagonal

Status: PASS WITH EXPLICIT NATIVE-IDENTIFICATION BOUNDARY.
Review date: 2026-08-31.
Programme: #763, including the earlier signed-source work.

## Frozen identity

The reviewed scientific state is 7ccd5a044e91b32a0aa66bcf30dcf39d99f96217.
It consists of the original packet at dd241e579656f6716633ec58fe506425fa8083a2
and a separate whitespace/hash repair. The repair removes an extra final
blank line in the source manifest and updates its dependent fixture hashes;
it does not amend the original commit or change the mathematics.

The original and repair were imported as
ec2a8ee53bc5015cfae0008202e44caf827d85e3 and
6dfd2bad665665af8567a244c26c255a9d0f07b4, respectively.
Acceptance is of the complete repaired state, not of the unrepaired fixture.

| Artifact | Git blob in reviewed state |
|---|---|
| FFPS_CANONICAL_BOOLEAN_PRINCIPAL_DIAGONAL.md | 47014e5aeadccd6f9e64eae061b2ef5f0e86bfdb |
| ffps_canonical_boolean_principal_diagonal.py | 1597122e787747ca8f4b9926f55dff24b706bb0b |
| ffps_canonical_boolean_principal_diagonal.json | 0de548e376d02cebac39bde18790a6e165fb6487 |
| ffps_canonical_boolean_principal_diagonal.sources.json | 50513bf33f0e381a6f23e7a01c2806df9196ae18 |
| tests/test_ffps_canonical_boolean_principal_diagonal.py | 0c6c1d412fad238138426bab4cb50e2a0dce6738 |

The first four paths are in research/l-families/atlas/function_field/.
The fixture LF-normalized SHA-256 is
8416b5c7c1461b530801eb49532b62b2139e68cae2b6a76f11ee2a1513eb2875.

The manifest binds twelve primitive files: eleven scientific inputs at
86cac1d64364015ec2cc0f8fbb6fc75dc041c12b and
ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc, plus a signed-history context
at 08187bdfae119f66c8c82baca2d1c1068e48ff40. All twelve raw Git blob identities
and LF hashes, and four current-artifact hashes, were independently checked.
The contextual file is not substituted for a missing native theorem.

## Mathematical review

The accepted result is exactly the chart-scoped diagonal estimate (CBPD8)
in the [proof](FFPS_CANONICAL_BOOLEAN_PRINCIPAL_DIAGONAL.md).
The following load-bearing points were checked.

1. Disjoint-support convolution gives
   b_U = mu_sf - 2 mu_U + mu_U star mu_U star 1_sf.
   The canonical equal-pair share is b_U(a)/binom(omega(a)+2,2).
   The unit coefficient is zero, not one. The Beta integral supplies the
   share and the elementary signed-allocation bound supplies
   abs(B_U(a)) <= 3^omega(a), uniformly in U >= 1.
2. The amplitude is the conjugate-left, un-conjugated-right product in
   (CBPD6). Its common g-phase cancels. The original principal squared
   weight is g^2 ell rho c_ell c_rho and the measure is
   abs(kappa_hat(t))^2 dt/(2 pi). The rescaled amplitude has weight
   c_ell c_rho/(ell rho), not a complete additive conductor weight.
3. The two least primes are distinct, so c_ell c_rho <= c_2 c_3 = 6.
   Squaring the two Boolean coefficient majorants gives
   81^omega(g) 9^omega(c) 9^omega(d).
4. The literal piecewise K has exact squared logarithmic norm
   C_kappa = 128(3+sqrt(2)) log(2)-288.
   Direct integration of its three pieces gives constant coefficient -288
   and logarithmic coefficient 384+128 sqrt(2). Positivity follows from a
   nonzero square; no numerical integration or rounding is used.
5. Dropping incidence restrictions in a nonnegative majorant costs
   zeta(2)^81 for the common square-core, H_floor(16Y)^9 twice for the
   two free cores, and H_floor(16Y)^2 twice for the owner products.
   Thus D_B <= 6 C_kappa zeta(2)^81 H_floor(16Y)^22 = Y^o(1).
   The infinite product and subpower limit are justified analytically,
   not by the finite divisor panels.

The exact scope is essential: the chart is 67-free; it has one atom per
exact tuple (P,Q,g,c,d); the masks have modulus at most one; and arbitrary
duplicate carrier, shell, endpoint, amplitude or history labels cannot
be appended to the sum. Including the ordinary prime 2 is harmless for
this scalar estimate and is not a characteristic-2 Kummer assertion.

## Independent replay

The root read all five packet files, reviewed the proof and normalization,
and ran all 30 tests normally and under Python -O: both passed.
Both complete producer modes, Ruff lint/format, and the full
08187bdfae119f66c8c82baca2d1c1068e48ff40-to-reviewed-state whitespace
check passed. The repaired author worktree was clean.

A separate reviewer read all twelve bound source files, independently
replayed both test/producer modes and source identities, and reported no
material gap within the stated scope. Its additional checks covered
177 extra Boolean controls, 16 atom/mask controls, 160 ordered-divisor
controls, five harmonic panels, 276 distinct-prime weight checks and
56 extra fail-closed cases in both Python modes. It separately integrated
the literal kernel, including its zero logarithmic moment.

The root independently reconstructed all 102 published Boolean rows by
bit-subset convolution, plus 45 held-out support/cutoff rows, and compared
160 ordered-divisor values for orders 1, 2, 9 and 81 through n=40.
A second symbolic calculation reconstructed the kernel norm without
calling the producer's integration routine.

The implementation rejects Boolean integers, floats, composite or repeated
prime labels, prime 67, duplicate exact tuples, oversized support/windows,
and masks of norm above one. Source roles, complete artifact hashes,
duplicate/nonfinite JSON and typed complete-report equality are enforced.
The public numeric/work caps bound this replay, not the analytic theorem.
Result-bearing checks remain active under Python -O.

Reproduce the resident controls from the repository root:

~~~text
python -B tests/test_ffps_canonical_boolean_principal_diagonal.py
python -B -O tests/test_ffps_canonical_boolean_principal_diagonal.py
python -B research/l-families/atlas/function_field/ffps_canonical_boolean_principal_diagonal.py --check
python -B -O research/l-families/atlas/function_field/ffps_canonical_boolean_principal_diagonal.py --check
~~~

## What this acceptance does not pay

The centered difference remains exactly

    P_nat^circ - P_B^circ = (P_nat-P_B) + (D_B-D_lit).

The accepted literal-diagonal estimate and this candidate-diagonal estimate
bound only the second difference by their sum. The first is unpaid.
In particular, the masked bilateral identity (CBPD13) has not been proved.
An equality of unobserved product sources is not an equality after
pair-dependent selectors, nor is it a license to forget surviving labels.

This audit accepts no native coefficient freedom, sign/lift theorem,
full principal-moment replacement, Wick conjunction, critical-line
percentage, RH or GRH consequence. The proof and its old sources remain
immutable. Any strengthened native-map theorem needs a new packet and
a new independent source-bound review.
