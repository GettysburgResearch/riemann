# Formalization Reviewer A cross-review of Reviewer B

## Frozen object

PR #733 was re-read at the beginning. Its head had moved from the supplied `6e6fb8b120069eaed2cc7f7cf966bb082c54eb4d` to `770c61e9d0ace520be2333f348d0bf239e0120ad`. The later head adds the missing registry and blueprint publications, so this review targets the newer exact head and tree `9d86d86981af2d16bd26c56dcb5b31f04182a505`.

RH remains unproved.

## Overall assessment

Reviewer B produced a valuable finite arithmetic layer. The row-two/row-three algebra and fixed 5:3 numerator are exact. The half-divisor coefficient construction reaches a genuine arithmetic-function Dirichlet-convolution theorem, not merely a formal-series identity. Several generic wavelet and summation-by-parts lemmas are useful reusable helpers. The branch also keeps the unfinished wavelet and half-divisor canonical claims blocked rather than falsely marking those full packets proved.

The branch is nevertheless **NOT_INTEGRATION_READY**. Independent compilation and axiom execution could not be established, and several declaration names, registry statuses, and blueprint nodes identify generic or toy lemmas with substantially stronger canonical statements.

## Accepted mathematical statements

Subject to an independent Lean build, the following source texts are accepted at their literal local scope:

- row-two and scaled row-three numerator definitions and exact common-zero elimination;
- fixed `5:3` factorization and unit-disc noncancellation;
- local `r` versus `2r^2` rational separation;
- the generic RN ratio cocycle;
- half-divisor recurrence, central-binomial/generalized-binomial identification, prime-power formula, and `eta * eta = ArithmeticFunction.zeta`;
- the generic convolution identity `(b*eta)*(b*eta)*mu = b*b`;
- generic four-tap factorization, affine/geometric annihilation, three-tap determinant minimality, finite shifts, and finite summation by parts;
- K0/K1 constructor inequality;
- both comparator statements and solution texts, pending compilation.

The light exact replay passes 51 coefficient convolutions, 500 Dirichlet-convolution evaluations, 120 one-field identities, 41 Abel identities, and the symbolic row/wavelet algebra.

## Material statement mismatches

### Sequential first owner

`firstOwner_eq_nativeEuler` proves a generic recursion on `List (R × R)`. The canonical source L-99601 is a labelled, parity-channel, future-completed shift-algebra identity with exact first-owner weights and disjoint source ownership. The current theorem is a useful algebraic shadow but not that claim. Its name and `PROVED` registry status overstate it.

### Source typing

Role indices are an improvement over a runtime `SourceRole` field and prevent direct type substitution. They do not prevent extracting an `ArithmeticFunction` and rebuilding it under a different public role constructor. Fixed and moving detector structures similarly do not encode the quantifier order that makes a detector independent of a hypothetical zero. The exact RN and `p^-1` normalization fixtures are not formalized; the current theorems are toy numeral identities.

### Wavelet

The generic four-tap polynomial is useful, but no theorem fixes `alpha=sqrt(2)`, states the exact canonical coefficients, proves the piecewise ratio-eight kernel, or establishes the actual factor-67 copy. `ratioEight_support` is only `2^3=8`; `factor67_antisymmetry` contains no 67. The finite Abel theorem is generic summation by parts, not the exact compact Abel-Mertens frame. B's blocked registry statuses are honest, but the original deliverable is incomplete.

### Conditional consumer

`fixed_native_subpower_negative_mass_implies_RH` is formally conditional, but its proof merely invokes `analytic.consumes`, a field that already states the desired implication. `data.sourceIdentity` is unused, as are the fixed-row and 5:3 theorems. It does not formalize the exact negative-mass/Landau consumer API and should not be registered as that canonical theorem.

## Build and trust result

The local environment had no Lean or Lake installation and could not resolve GitHub for checkout. A separate exact-tree CI probe PR generated open, ready, push, and synchronize triggers without touching PR #733, but GitHub exposed no workflow run or status. Thus the requested builds and scripts were not independently executed.

Static inspection found no trusted `sorry`, `admit`, custom axiom, opaque constant, unsafe declaration, challenge-side sorry import, or post-#707 dependency. The two challenge files contain the deliberate statement-only `sorry` permitted by bootstrap policy. The B-owned axiom-print files are not directly invoked by the authoritative bootstrap audit, so compiled axiom coverage remains incomplete.

## Completion answers

**Did Reviewer B complete every assigned deliverable?** NO. The exact first-owner/source firewalls, canonical wavelet/Abel layer, source locks, formal-status report, direct axiom coverage, and independent build evidence are incomplete.

**Which Lean theorems are accepted?** The literal finite algebra listed above, especially rows 2/3, fixed 5:3, half-divisor coefficients and convolution, generic wavelet algebra, and generic Abel summation, subject to compilation.

**Which are only conditional?** `fixed_native_subpower_negative_mass_implies_RH`, and it is also a statement mismatch because its consumer assumption already contains the conclusion-producing implication.

**Which names overstate their statements?** At minimum `firstOwner_eq_nativeEuler`, `rn_raw_cutoff_witness`, `normalized_p_inv_ne_p_inv_sqrt_witness`, `ratioEight_support`, `factor67_antisymmetry`, `sameK1Translation_coefficient`, and `fixed_native_subpower_negative_mass_implies_RH` when mapped to the canonical claims.

**Are B.tsv and content-B.tex resident?** YES, at the frozen final head `770c61e9d0ace520be2333f348d0bf239e0120ad`.

**Is PR #733 ready for formal reconciliation?** NO. It is useful evidence, but `NOT_INTEGRATION_READY` until the blocking fixes and exact-head build are supplied.

**Does any theorem prove RH?** NO.
