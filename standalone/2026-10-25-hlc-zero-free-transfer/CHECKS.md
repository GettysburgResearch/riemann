# Verification and its limits

All commands below were run from this packet's directory on 25 October 2026.
All completed with exit code zero. Run the scripts without Python's
optimization flag: some independent control scripts use assertions.
The exact checker uses explicit failures even when assertions are disabled.

## Reproduce

    python -I check_exact_identities.py
    python -I verify_shift_bridge.py
    python -I review_affine_checks.py
    python -I paper_audit_checks.py

The first and fourth scripts require only the Python standard library.
The two middle controls also require NumPy. No remote service, private
data, credentials, or GitHub Actions runner is used.

## Exact finite identity checks

Arithmetic class: EXACT_RATIONAL, with exact pairs for complex rationals
and formal commuting variables for prime logarithms.

The exact checker recomputes:

- The CRT expectation and variance by enumerating every reduced residue,
  then compares with an independently evaluated probability generating
  polynomial. The moduli are 105, 1,155 and 15,015, with respectively
  48, 480 and 5,760 reduced residues. Both multi-prime bands and multiple
  groups are included.
- Both the coprime-prime and unrestricted prime-power logarithmic
  Möbius identities through integer 2,000, coefficient by coefficient
  in the prime logarithms.
- The false prime-only identity without the coprimality restriction:
  the \(p^2\) negative control is required to fail.
- The zero-shift \(\Lambda\mu\) identity in 303 formal prime-logarithm
  coefficients.
- Full and projected moment identities at three finite column lengths,
  with nonreal character values, natural zero masks, nonconstant row
  weights, and an exact noncoordinate complex projection. The moment
  expansion and affine \((a,p,h)\) enumeration are independent.
- The exact conditional recurrence
  \(7/8\to79/100\to31/50\to1/2\).

The character/projection cases are synthetic rational-field controls.
They validate the algebra; they are not finite computations of the
native Eisenstein family or evidence for a mean bound.

## Double-Stieltjes control on actual arithmetic

Arithmetic class: FLOATING_RECONNAISSANCE.

The script uses actual Möbius and von Mangoldt values, a polynomial
compact cutoff, and a normalized polynomial shift kernel. It computes
the original finite sum and separately integrates the exact double
Stieltjes remainder on every polynomial piece. The quadrature degree
is sufficient for those pieces; floating-point roundoff remains.

| \(X,H\) | Absolute difference |
|---|---:|
| 40, 5 | \(7.41\cdot10^{-13}\) |
| 80, 10 | \(2.01\cdot10^{-12}\) |
| 120, 12 | \(3.72\cdot10^{-12}\) |

This checks the sign, the main term, both factors of \(H\), and support
boundaries. It does not check the proposed all-scale correlation bound.

## Independent Eisenstein orientation control

Arithmetic class: MIXED. Ring factorization, divisibility, and residue
identification use exact integers. Complex embedding, angular and height
phases, profiles and projection use ordinary floating point.

The control enumerates 44 primary ideals in its finite norm range,
then uses seven rows and 18 columns with actual sextic power-residue
symbols. Both full and projected affine identities contain 374
summands. Errors were below \(3\cdot10^{-16}\).

A deliberately reversed kernel orientation changes the projected norm
by about 0.00548. Requiring that difference makes this an adversarial
test of conjugation conventions. The complex frame is a finite control,
not a replay of the complete growing PR1019 Gauss frame.

## Selected source-algebra checks

The source-audit script checks 762 parity-conjugacy cases, projective
line counts for four primes, the elementary fourth-moment count for
moduli 2 through 40, and all 216 specified three-vertex damping cases
over the projective line at 5. It also checks the zero-shift identity
through integer 100,000. The algebraic counts are exact; the last
comparison uses floating logarithms.

These do not certify the high-moment prime-memory construction,
global distinctness argument, or an asymptotic Type II estimate.

## Review scope

The analytic notes received separate agent review, including checking
the main term, Mellin noncancellation, bootstrap quantifiers, finite
CRT normalizations, Eisenstein primary convention, projection
orientation and invertible-Gram scope. File hashes bind the reviewed
versions in the review reports.

The reviewers worked within the same assistant team. One reviewer
contributed suggestions to the mark-variance derivation; that review
is not fully independent authorship. Another reviewer independently
reconstructed the shift bridge. Neither report is external peer review,
formal verification, or evidence that the open correlation estimate
has been proved.
