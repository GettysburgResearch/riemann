# Validation and limits

## Actual execution

The complete new checker passes in ordinary Python and python -O, with
byte-identical EXACT.json. Its report contains 298224 explicit predicates;
233280 of them are repeated prefix/tail guards, not independent analytic cases.
The useful finite coverage is:

- 64 complete rational-integer coefficient cases through 729, comparing a
  direct local Euler assembly with the unique powerful-component decomposition;
- 46656 coefficient equalities, retaining masks and shared prime support;
- 608 critical-Jacobian and 608 normalized-short-weight inequalities;
- 60 direct finite mixed-window Fourier expansions, 60 mixed Parseval identities,
  60 integrated Cauchy comparisons and 60 frequency-mass identities;
- 64 exact dilation identities, including noninteger window lengths and complex
  phases, with 64 microscopic-interval counting bounds;
- 227 endpoint-maximal partition checks, including an explicit opposite-heavy-
  atom example whose terminal correlation is zero but intermediate maximum is not.

All these computations use integers and fractions.Fraction (pairs for complex
values). No floating-point or interval numerical result is claimed.
The odd-m coefficient fixtures choose the allowed powerful profile
z_p=phase/sqrt(p), making the stored coefficients rational. They are not tests
of every odd-m complex profile. The odd-m analytic weights are separately
checked exactly after squaring. The theoretical proof covers arbitrary profiles.

Seven actual separate corrupted optimized-Python processes fail at the expected
predicate: erased masks, wrong powerful weight, missing geometric radical,
omitted complex conjugation, wrong triangular overlap, wrong dilation Jacobian,
and missing heavy-atom cost. MUTATIONS.json records their return codes and
intended failures. These are code fault controls, not proofs of the analytic theorem.

## What the checks do not establish

They do not prove the external MRT estimate or its pretentious-distance bound.
They do not certify any infinite little-o conclusion, exact value of an implied
constant, growing-conductor result, norm-fiber theorem, or RH. No actual L-values,
zero census, theta evaluation or conjectural rate fitting was done.

The finite Fourier implementation independently expands time windows and
coefficient correlations, but both use the same exact complex arithmetic routines.
The two source constructors share elementary integer factorization. Proof and
code have the same author. No independent mathematical referee, proof assistant,
transitive axiom audit, upstream rebuild, full-repository validator or remote
CI result is claimed.

## Review priorities

1. The precise MRT v3 input (13)--(14), and the uniform perturbation for d<=log H.
2. The actual hard endpoints and equal-length real-window split in (18)--(22).
3. The sparse t_d>sqrt(H) regime: a short-interval theorem cannot be applied
   there directly, especially with growing m.
4. The whole-line energy Jacobian in (23), versus the normalized weight in (24).
5. The mixed Fourier identity and the arbitrary L2 second sequence.
6. The square-mass partition in (34), including heavy atoms and the endpoint
   maximum. The supremum over frequencies stays outside the MRT integral.
7. The rational-integer scope and the remaining logarithmic-versus-critical
   power gap. The Gaussian corollary concerns one complete shell, not the tail
   or full total energy.

## Recovery

Both original archived full checkers were rerun in ordinary and optimized
Python, and all four reports match their archived outputs byte-for-byte.
Their original source trees were reconstructed BEFORE running the scripts,
so interpreter-generated caches are not included. The files are already on
#956; they are not copied into the new directory. See RECOVERY.md/RECOVERY.json.

The only development change after the first accepting new run compacted the
JSON report to a deterministic case-list digest and explicit parameter list;
the mathematical predicates and computations were unchanged. Both final modes
were rerun. The failed interactive launch in the recovery stage is disclosed
in RECOVERY.md and is not counted as a completed execution.
