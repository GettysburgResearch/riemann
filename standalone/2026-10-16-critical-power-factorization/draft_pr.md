# Proposed PR: uniform critical-power factorization and exact Gaussian recovery

Status: PROPOSED component mathematics; not independently reviewed. No full RH,
native higher-moment estimate, or new zero-free boundary. This draft has NOT
been published in the current session.

Base: #949, cdb0666fc48d5166f5edd81f394b13e2001a6b5d.
Proposed branch: research/critical-power-factorization-20261016.
Adds only standalone/2026-10-16-critical-power-factorization/.

## Changes

- Factor the 0/1/6 source from #948/#949 into an ordinary Mobius channel, a
  weighted sixth-power Mobius channel, and a correction.
- Generalize algebraically to every integer m>=2, with coefficient
  q^(m/2-1) at degree m. No automorphic realization for general m is asserted.
- Prove that correction and its inverse have uniform absolute coefficient
  mass at weight 1/2 at most exp(5[F:Q]), independent of m, after the original
  prime exclusions over 2 and 3. The inverse and shared-prime term are retained.
- Continue this correction and its inverse to Re(s)>m/(2(m+1)); at m=6 this
  is 3/7 and supplies a critical kernel tail T^(-1/14+rho). This is NOT a
  continuation or zero-free region for zeta.
- Close the noncompact Gaussian interface left separate in #948. State exact
  same-measure, same-height, shorter-scale envelope comparisons and match
  #949's normalized signed probe, including its scalar C_S.
- Record the irreducible OPEN-G2 dyadic mean-square estimate. It would imply
  the desired zero exclusion, but is not established by the factorization.

## Provenance and overlap

The first sixth-power normalization, the 0/1/6 coefficients, and critical
logarithmic native comparisons already occur in #948/#949 and are credited.
Euler algebra, convolution and Mellin inversion are classical. This proposal
adds the constant-cost two-channel correction, general m statement, priced
tail, and actual Gaussian interchanges. No global priority claim is made.

## Validation

450 exact local phase configurations; 972 exact physical convolution
identities on a declared three-prime Eisenstein semigroup and all 54 rows of
norm <=13. This is not a full native-column census. Ordinary/optimized outputs
match. Three process-level mutations are rejected. The written analytic proofs
and finite diagnostics have the same author; no independent review or Lean
build. See VALIDATION.md and REPLAY.json.

Review focus: the coefficient-norm proof, original prime exclusions, the
3/7-versus-zeta distinction, shared-prime degree seven, and infinite Gaussian
interchanges before any use of the critical bound.
