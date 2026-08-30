# Independent review: S4 arithmetic source packet

Reviewed scientific commit: `d19f421b438485c953469be59c4df8f79a30d2bf`.

I independently read the proof, producer, tests and replay contract, then checked the frozen correction to the twisted multiplicity-space definition. I did not execute the producer or tests. Root reports Ruff, all 15 tests in ordinary and optimized Python, and ordinary/optimized producer checks passing after final source bindings; all 14 declared finite-field panels were counted.

## Mathematical review

The Bring-quartic hypotheses give six distinct finite transposition branches and double-transposition inertia at infinity. The connected tame cover consequently has geometric and arithmetic group S4. The genus-19 Galois closure and the sign, pair-partition, standard and sign-standard multiplicity dimensions agree with the explicit quotient curves and ramification calculation.

I checked the discriminant identities, the squarefreeness and coprimality conditions for the degree-six auxiliary polynomial, and the resulting genus-1, genus-2, genus-4 and genus-7 quotient curves. The two independent decompositions of the genus-seven curve give the claimed degree-eight twisted factor. Its integral reciprocal polynomial is supported by an actual Frobenius multiplicity space and its induced alternating pairing, rather than only by formal division of point-count polynomials.

One source-space precision was corrected before freezing: the full central-idempotent sign-standard isotypic summand has dimension 24. The eight-dimensional space is `Hom_S4(tw,H^1(Z))`, or the A3-invariant part of that isotypic summand. The frozen proof now makes this distinction explicitly.

The load-bearing ramified Frobenius distinction is correct. At a finite branch the residual quadratic splits according to the residue-field character of -2, so invariant Frobenius traces cannot be replaced by invariant dimensions. At infinity the character of -1 controls the corresponding coset. The affine resolvent point (0,0) lies above base infinity and is counted exactly once; it is not an additional projective point of the quartic model.

## Code and coverage review

The producer authenticates its pinned field dependency before import, validates the declared small-field source, counts the six displayed source curves directly, and independently checks fibre and invariant-character identities. The p=7, b=3, c=4 panel supplies the negative finite-branch control absent from the first source family. Newton reconstruction uses only the necessary first half of each reciprocal polynomial; later p=5 extension counts provide held-out degree-eight checks. The full degree-38 Galois-closure factor is assembled from the proved representation decomposition and checked against normalized regular-character counts, not represented as an independent direct enumeration of a degree-24 affine model.

The tests exercise actual S4 permutations and inertia/Frobenius projectors, source discriminants, small direct point tuples, split and nonsplit branches, parameter refusal and source authentication. The declared field cap remains 15625. I found no remaining blocking mathematical or implementation defect in the frozen seven-file packet.

## Scope

This is a concrete classical finite-field arithmetic realization with all four nontrivial S4 factors. It does not establish a new general Galois, conductor, cohomology or Riemann-hypothesis theorem, and does not transfer positivity to the native analytic programme. The subsequently drafted closed-place Euler note is outside this reviewed commit.
