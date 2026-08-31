# Cyclic infinity module: exact replay and limits

Status: proof and runtime prepared; root execution and exact-SHA independent
review remain pending. The proof/preregistration were independently read
before implementation. This file does not claim that the queued tests ran.

Run `cyclic_infinity_replay.py --write`, then ordinary and optimized
`--check`, and `tests/test_extension_order_cyclic_infinity.py` in both modes.
Root owns execution under the shared memory reserve and resource limits.

The producer authenticates three frozen proof-bearing source blobs before
constructing any packet output; it imports no executable upstream code.
It independently enumerates the literal Segre and added-standard monomials,
their invariant-factor divisibility, and the actual minimal quotient of C
over the full invariant base. Source degree6 and8 generation checks are
held out from the degree2/4 minimal-generator calculation. The actual C6
projection and the untwisted C3 calibration are separately retained.

All33 actual minimal monomials, both23-dimensional old degree4 spans,
normalizer permutations and determinant polynomials are included in the
artifact. The full C dimensions through degree8 are separately compared
with the frozen rational Molien function. This comparison does not replace
the monomial quotient computation or supply all-grade generation.

The polynomial matrices are multiplied before imposing uw=v^3. A separate
substitution into k[p,q] and four weighted-degree presentation/kernel/image
checks calibrate the proved exact covariant resolution. The artifact labels
F0, F1 and F2 separately: dimensions3,3,5,5 belong to F0 in degrees8,10,14,16.
No output describes the relative A_i tensor T terms as free over B'.

Arithmetic is exact integer or Fraction. The caps are Segre/combined degree8,
weighted matrix degree16, at most16 matrix rows/columns, two MiB per source
and artifact, and no field census. Fixture acceptance recomputes the whole
payload and compares canonical JSON, preserving int/bool/float distinctions;
duplicate keys, floating numbers and nonfinite JSON are rejected on input.

The proof, not a finite sampled rank pattern, establishes the all-grade
generation theorem, maximal Cohen--Macaulay property, generic rank3,
infinite projective dimension at the graded vertex, and two-periodic
covariant exactness. The classical depth/fixed-field/Auslander--Buchsbaum
inputs are named in the proof. This is not a new general invariant-theory
theorem, an arithmetic Frobenius construction for arbitrary matrices, or
an analytic improvement deduced from trace cancellation.
