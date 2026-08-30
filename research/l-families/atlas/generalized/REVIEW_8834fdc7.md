# Independent review of multiplicative recurrence and mixed-rank parents

Reviewed core commit: `8834fdc7a0dfe15f6bb95eefe0729cb77c93c807`.

Scope of this review: `MULTIPLICATIVE_RECURRENCE_AND_MIXED_PARENTS.md`, its
producer, source manifest, finite fixture, tests, and the associated
generalized README entry. The proof checkpoint was `4f4950e476`, followed by
the full replay and deformation checkpoint `0f7be357b856`; the reviewed core
includes the subsequent Sturm endpoint repair. This is not a review of every
inherited theorem or every file in the branch.

Verdict: no remaining mathematical or implementation blocker found for the
stated local, continuous-multiplicative and universal-representation claims.
This is an independent proof/source review, not a scientific integration
verdict, a machine proof of universal quantifiers, or an external novelty
certificate.

## Evidence and execution distinction

I independently read the proofs and the complete producer and test source,
checked the final endpoint-repair diff, reconstructed the key arguments,
and inspected the exact source-authentication and payload-acceptance paths.
I did not run a producer, test suite, linter, build, or numerical search in
this review. Computation was serialized by the implementation agent because
another Codex process is active on the same limited-RAM host.

The implementation agent reports Ruff, normal and optimized producer
`--check`, and all 27 tests in both normal and optimized Python passing for
the corrected core, with its fixture regenerated. These are reported
execution results, not independent executions by this reviewer.

The graph comparator has a separate review bound to
`26314df4e5ed9a5c16b7da61e155a48d325789cc`. Its later README real-part repair
and Windows checkout metadata repairs do not form part of the core theorem
review here. The implementation agent identifies the integrated branch
checkpoint as `b800f754d3c53d61746dfb3a068e250c53b62771`.

## Mathematical audit

1. The classification of normalized continuous multiplicative maps is
   correct: away from zero, a map is `r^a exp(ik theta)` with integral k;
   continuity at zero gives either the constant-one map or `Re(a)>0` and
   value zero. The compact-circle and real-logarithm arguments justify the
   character coordinates rather than assuming a branch of a complex power.
2. An eventual recurrence along one irrational orbit makes a finite
   translation combination vanish on a dense tail. Continuity extends that
   identity to the whole circle. Its Fourier coefficients have support only
   at the finitely many roots of one nonzero polynomial. Fourier uniqueness
   then supplies a Laurent polynomial. No Diophantine hypothesis or
   natural-boundary theorem is needed for this step.
3. For c>1 the two singularities at -c and -1/c are distinct. Equality of
   logarithmic derivatives on the annulus is an equality of rational
   functions; its residues force both exponents to be nonnegative integers.
   The positivity of all Laurent coefficients gives exactly m+n+1 distinct
   sampled roots and the claimed minimal order. Closure of exponential
   polynomials under products and conjugation establishes preservation of
   all recurrent sequences, including finite-prefix changes.
4. The centered-circle, origin-touching-circle, rational-rotation, and
   nonmultiplicative controls identify genuinely different hypothesis
   failures. In particular the map z^2/conjugate(z), extended by zero, passes
   the origin-touching circle and is a valid counterfeit outside c>1.
5. The multicoefficient result follows by splitting a coordinatewise
   multiplicative map into its coordinate restrictions. It explicitly
   requires the separate coordinate probes. The unitary twist weight m-n
   and dilation degree m+n are distinct and are correctly retained.
6. The discrete-deformation theorem is valid without a uniform order bound.
   Evaluation at 2 first makes total degree locally constant; on that
   neighborhood only finitely many weights remain. Evaluation at one
   irrational unit phase then isolates the weight. The bounded moduli and
   fixed-weight counts are the corresponding elementary lattice counts.
7. The generic bidegree spectrum is correct after exact collisions are
   grouped and zero combined coefficients removed. The stated noncollision
   hypothesis is necessary; real and torsion examples do not have the
   generic complex order. The Binet realization is confined to distinct
   roots and its output vectors can depend on the matrix.
8. The unequal-rank Segre numerator proof correctly applies the largest
   factor first. At each later differential step the leading multiplier
   `(M-j+1)/j` is strictly positive, and signs at the previous negative
   roots, zero, and negative infinity force one additional simple negative
   root. The degree A-M and H(1) follow by induction and telescoping.
9. Evaluating a finite graded virtual representation parent at the identity
   permits zeros and poles only at roots of unity. The negative-root lemma
   therefore excludes all profiles except, after deleting rank-one factors,
   the empty list, a single rank, and the pair (2,2). The explicit rank-two
   numerator identity proves the remaining case and extends to repeated
   eigenvalues by polynomial coefficient identities.
10. The formal infinite virtual product is a recursion in the representation
    ring, not an analytic product. The second class is the negative sum of
    the even, nonempty exterior-square terms. Its negative dimension gives
    the all-effective obstruction. Repeated/conjugate input necessity still
    follows from the identity specialization, and the stated continuous
    representation category correctly permits conjugation without calling
    it holomorphic algebraic.

## Findings repaired during review

Two proof precision issues were repaired before the full replay freeze:
repeated eigenvalues can produce polynomial-in-index coefficients even for
diagonalizable matrices, and the Binet recovery vectors are not one universal
fixed matrix coefficient valid for every matrix.

One concrete adversarial code case was found after initial inspection:
`sturm_negative_simple([0, 1])` counted the endpoint zero as a negative
root. Actual Segre numerators all have constant term one, so no existing
theorem, fixture value, or claimed Segre root count was affected. Commit
`8834fdc7a0dfe15f6bb95eefe0729cb77c93c807` now explicitly refuses a zero
constant term, and its test exercises that refusal. This is the correct
bounded contract for the routine being used here.

## Adversarial replay inspection

- Laurent coefficients from the binomial formula are checked against direct
  Laurent multiplication. Periodic aliasing and the origin-touching false
  positive are separate controls.
- Gaussian-rational Binet spectra are checked against an independently
  generated local coefficient recurrence. Real and torsion inputs test
  collisions instead of merely repeating generic examples.
- The Segre differential construction is checked against finite differences;
  exact rational Sturm sequences check the finite root census. Repeated and
  positive roots are explicit controls, with the zero endpoint now refused.
- The second virtual dimension is checked against its even-subset exterior
  decomposition. Rank-two determinant identities use direct four-by-four
  permutation expansion, including nonsymmetric and repeated/Jordan cases.
- Spectrum expansion is refused before building Binet denominators when its
  combinatorial cap is exceeded. Ranks, factor counts, bidegrees, coefficient
  sizes, and replay dimensions are bounded. Exact input contracts reject
  floating-point and Boolean substitutions.
- The producer authenticates frozen commit:path objects, compiled Git blob
  identifiers, normalized content hashes, and the corresponding current
  primitive files. The fixture must equal full source recomputation; its
  self-consistent checksum alone does not suffice. Production acceptance
  uses explicit exceptions and survives optimized Python execution.

I found no further implementation defect by inspection. Finite controls do
not prove continuity, orbit density, the all-rank interlacing induction, or
universal representation identities; those burdens are discharged only by
the separate prose arguments reviewed above.

## Literature and remaining scope

I checked the cited primary pages directly. [Morales](https://arxiv.org/abs/1306.6910)
does concern Segre Hilbert numerators and Newcomb numbers;
[Ferretti and Zannier](https://arxiv.org/abs/math/0701772) concern equations
in recurrence rings over number fields. The
[Knill--Lesieutre author page](https://abel.math.harvard.edu/~knill/kam/papers/denjoy/index.html)
gives the nearby Fourier/geometric-series setting and imposes additional
regularity and Diophantine assumptions for stronger continuation statements.
The note's limited descriptions of these sources are accurate; none is a
certificate of external novelty for the present synthesis.

The repository gain is a precise distinction between scalar recurrence
preservation, matrix-coefficient recovery, and universal determinant
representation. It does not supply a compatible prime-indexed family,
canonical completion, convergence of an infinite graded product,
automorphy, motivic realization, or an RH/GRH consequence. The qualifiers
continuous, normalized, multiplicative, c>1, irrational, generic where
specified, and universal over all matrices must survive any summary.
