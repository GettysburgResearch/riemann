# Validation, limitations and recovery boundaries

## New finite checks actually run

Both `python verify.py` and `python -O verify.py` reproduce CHECKS.json
byte for byte. The same-author checker has 1,821 explicit finite predicates.
Its coverage includes:

- Four exact DF detector substitutions, checking all ten norm-power terms
  and their height coefficients. Both endpoints of each supremum are kept.
- Five complete strata, all their shifted vertices, both principal contours,
  small and large frequency ranges, the changed Mellin normalization and
  the strict positive M-1 and upper-frequency gaps.
- Every polynomial inequality over 0<e<=1/10000 is checked using rational
  Bernstein coefficients on [0,1/10000]. Positivity at the closed e=0
  endpoint is NOT substituted for an admissible analytic parameter. The
  last Bernstein basis term proves required strict positivity for e>0.
- 512 synthetic zero-abscissa subsets, including exact threshold equalities,
  verify disjoint exhaustive classification and lower-count/upper-contour
  logic. They do not represent 512 tested Hecke families or any actual zero
  census. Thirty-six two-prime sixth-power-free exponent patterns verify
  the distinction between exterior norm and its radical.
- The restricted-model ceiling has explicit algebraic dual identities in
  the proof. A few rational substitutions guard their implementation;
  those substitutions alone are not the all-parameter ceiling proof.

`run_mutations.py` actually launches four corrupted `python -O` processes.
Wrong stratum count, missing good class, old principal shift, and using M=1
are each rejected by the recorded ArithmeticError. These are executed
negative controls, not descriptions of hypothetical tests.

Exploratory floating-point parameter optimization helped choose a finite
candidate; NONE of its numerical optima or tolerances is a proof input.
The retained code uses Fraction arithmetic, exact polynomial identities
and all-interval positivity checks. No numerical number-field/zero
computation or interval claim for an L-value is made. A final output cleanup
removed repetitive vertex-certificate JSON while preserving all executed
predicates; both full modes and the mutations were rerun afterwards.

## What these checks cannot establish

The checker does NOT prove the imported theta bound, the zero detector,
large-sieve theorem, generator adapter, contour height estimates, Mellin
analytic continuation, or the proposed global zero-free consequence. It
checks the exact use of their declared powers/domains. Proof and code have
the same author, not independent agent/human referees.

DF's stated theorem/character construction/detector proof and BGL Section 5
were freshly inspected, with BGL PDF screenshots. The CT v2 source body was
not obtainable in this pass. Its analytic package was adopted from the
complete exact-SHA #957 adapter and cross-checked with the older #948
archive. CONTRACTS.md makes this dependency explicit. This is a proposed
composition of imported unconditional theorems, not an independently
verified unconditional theorem certified by 1,821 arithmetic predicates.

No Lean build, full upstream analytic proof reconstruction, transitive
axiom audit, independent referee, full-repository validator, or remote CI
result is claimed. Independent review must begin with the imported source
interfaces and family matching, not the final fraction 25/27.

## Already completed publication recovery

Before writing this continuation, the two outstanding user packets were
published unchanged on draft PR #958:

- c2a388fe3b6591663fadc7a561d9bb4ed03ffb47: thirteen-file native
  norm-divisibility packet plus a separate publication notice;
- cec073b584a9e305fd09f6d31361d0f3f77cadb0: fourteen-file earlier
  norm-fiber companion plus its separate publication notice.

Both original manifests passed and both ordinary/optimized original
checkers freshly reproduced their saved JSON. Their historical mutation
and numerical records were preserved, not freshly regenerated. Complete
remote tree/contents reads matched the original local blob IDs and sizes.
The ramified-dilation predecessor is already present through #954 and is
not duplicated. No unpublished work from other conversations is claimed
recovered. The previous equal-norm sign interpretation is explicitly
corrected in the separate recovery receipt, not rewritten in archived bytes.

## Publication packaging

The new manifest binds these local files, not mathematical truth. This
continuation is add-only against cec073b584a9e305fd09f6d31361d0f3f77cadb0.
No previous proof or integrated status is edited. Final commit identities,
remote blob read-back and ZIP replay are recorded in the PR/outer receipt
after publication; they are not inferred merely from creating local files.
