# Independent exact-commit review: completed ternary-cube resolution

Reviewed source: `COMPLETED_TERNARY_CUBE_RESOLUTION.md`, commit
`47890a7a07a525494dedac37ab6e197c2169f902`, exact Git blob
`7301d9cbc50bde470fb3551a6262cf62378b523c`.

I read the entire candidate and then the complete file from that exact
commit. Read-only Git inspection confirmed the blob identity and an empty
working-file diff against the frozen proof. This report adds no source
mutation, computational rerun, or acceptance claim for an older contract.
I did not author this synthesis or the single-witness acquisition.

## Conclusion

No mathematical or scope blocker found. The synthesis correctly joins
the accepted marked maps to the separately established complete Tor
support. It does not use a matching Hilbert numerator as a substitute for
exactness or claim that the abandoned larger kernel computations ran.

## Source normalization and free modules

I reopened the frozen source-convention text and the full Tor-character
table. The ten Chow variables span \(\operatorname{Sym}^3V\) inside
\(V^{\otimes3}\). Literal orbit sums are the divided-power coordinate
normalization of the characteristic-zero symmetric inclusion; their
rational rescaling does not change the equivariant subspace. The module
base is the ten-variable \(\operatorname{Sym}(\operatorname{Sym}^3V)\),
not the twenty-seven-variable ambient tensor polynomial algebra.

All ten displayed \(\mathrm{GL}_3\times S_3\) Tor summands, their internal
degrees, dimensions, and the four free-module degree lists agree with
the independently frozen character table. The factor-permutation action
commutes with diagonal \(\mathrm{GL}_3\); it is not being relabeled as
arithmetic monodromy. The note correctly separates abstract equivariant
free modules from the concrete marked lifts and does not assert that
the printed matrices provide a preferred equivariant splitting.

## Global exactness

The argument has the required order:

1. The earlier exact first presentation and accepted degree-four/five
   kernels give a globally exact minimal \(D_2\).
2. The accepted eleven degree-five and seventeen degree-six lower
   \(D_3\) generators identify the complete old degree-seven subspace.
3. Independent Tor support leaves one top class, of weight \((7,7,7)\).
   The accepted exact kernel vector vanishes on a coordinate minor
   on which the complete forty-nine-element central old list is
   injective, and hence lies outside that old space.
4. Graded Nakayama first gives surjectivity of \(D_3\) onto
   \(\ker D_2\). Only then do dimension shifting, the vanishing of
   \(\operatorname{Tor}_4\), and Nakayama give injectivity of \(D_3\).

This matches the promotion proof independently reviewed in
`REVIEW_ed8c7251.md`. The global degree-seven dimensions \(775\) and
\(776\) are correctly labeled deductions after exactness, not a newly
measured full kernel or full old-space elimination. The new accepted
witness artifact is cited by its exact commit, blob, and proof digest.
Its recorded matrix counts and residual checks remain inputs from its
separate acquisition/acceptance review, `REVIEW_4019ecd9.md`; I did not
recompute them while reviewing this synthesis.

## Trace and Euler bridge

For the declared diagonal action, the graded source trace is exactly
\(\sum_d h_d(g)^3T^d\). Multiplying by
\(\det(1-T\operatorname{Sym}^3g)\) produces the alternating Tor character.
The ten-dimensional Chow-base denominator, signs, and grading agree.

At the identity the alternating numerator is
\[
 1+17T-9T^2-65T^3+65T^4+9T^5-17T^6-T^7
 =(1-T)^3(1+20T+48T^2+20T^3+T^4).
\]
The degree-two coefficient is correctly \(11-20\), and the resulting
seven-dimensional Hilbert denominator is consistent with the source.
No finite superdeterminant, pure resolution, arithmetic purity theorem,
retained-gamma identification, or RH conclusion is inferred.

## Validation provenance

The synthesis attributes successful write/check/optimized-check and
twenty-six ordinary plus twenty-six optimized tests to the coordinator's
single-witness execution. It also preserves the first failed
reconstruction attempt and distinguishes the later exact accepted lift.
Those are coordinator-reported executions, not jobs performed by this
reviewer. This review used proof/source reads and exact Git identities
only; no Python, tests, elimination, source acquisition, or Git mutation
was run.

