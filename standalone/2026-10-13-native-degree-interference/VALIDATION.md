# Validation, analytic boundaries and remaining estimate

## Mathematical status

All new analytic results are proposed written proofs requiring independent
review. The author wrote the proofs and the checkers. No independent agent or
human review, proof-assistant build, whole-repository validator, upstream
external-theorem reconstruction, or remote CI run was performed.

MICROSCOPIC_PHASE.md relies on the named classical fixed-field analytic facts.
Its contour expansion is explicitly uniform in a complex disk; Cauchy's bound
on the holomorphic remainder is what gives an error proportional to theta.
A mere bound for a nonanalytic big-O expression would be insufficient. The
lower theorem uses the principal fixed twist and a nonnegative smooth test;
the stability theorem has broader coefficient and row-measure scope. Neither
one gives the desired native upper bound. The fourth-order D^(1/8) is a lower
EXCESS for changed coefficients, not a native saving or a zeta boundary.

## Freshly executed checks

1. The entire nine-case degree census was run in normal and optimized Python.
   Both complete outputs match results.json byte for byte. The largest case
   D=8192,H=12855 was also recomputed separately in optimized mode and every
   field matched its recorded case.
2. `verify.py` passed in both modes with byte-identical verification.json:
   51,174 predicates including setup. These include 3,026 complete ordered
   quartets, 2,328 literal unit-action tests, and the exact alternative-phase
   calculation. The large predicate count includes 45,732 degree-cap guards;
   it is not a count of independent asymptotic statements.
3. `verify_phase.py` passed under isolated, standard-library-only ordinary
   and optimized Python with byte-identical phase_verification.json:
   6,829 predicates including setup. It checks reciprocal-Gamma NUMERATOR
   recurrences, rational unit phases, complete small hard-window columns,
   actual sixth-power nonunit masks, and rational exponent identities. It
   does not numerically certify Gamma asymptotics, a Schwartz integral,
   the prime ideal theorem, or the infinite microscopic-phase estimate.
4. Both recovered matching-geometry programs were freshly replayed in both
   modes. They reproduce the archived results and calibration exactly.
   All archived manifest bindings were checked without modifying the files.

## Census coverage and arithmetic

All good squarefree ideal columns in D/2<Nn<=D, and all nonzero element rows
in Nu<=H, are included at each stated case. Good means outside the primes over
2 and 3. Conjugate split primes remain distinct; inert primes and literal
nonunit zeros remain. Full fourth-moment degree/unit Grams extend through
D=8192,H=12855. The complete singleton/no-singleton split is computed only
through D=1024, plus the D=H=512 pilot. No claim extends that more expensive
split to the largest case.

The parent primitive arithmetic helper is shared and hash-authenticated.
The verification's ordered-tuple method differs from the producer's product
and grade grouping, but it is not a separately implemented number-field
backend. Bounds protect every fixed-width integer array from overflow on the
accepted resource domain; no floating point enters the accepted values.
The alternative phase z=(-2+i sqrt(5))/3 is evaluated by exact polynomial
algebra in a degree-four field. Resource/type guards are exercised.

Finite hard-window diagnostics are distinct from the compact smooth test in
the analytic theorem. The census's 93.0463% cancellation is a finite ratio,
not evidence of a proved limiting rate. Both positive and negative singleton
cases are retained. No favorable case replaces the complete reported suite.

## Source-specific remaining estimate

The missing estimate is the native signed large-singleton covariance at
near-linear physical height, with its fixed-twist/test/shortened-scale
quantifiers. Its degree Gram is small only on the alternating vector if the
required arithmetic cancellation holds. Positivity of that Gram or counting
its diagonal does not prove the statement; the singleton difference matrix
is actually indefinite on an enumerated native case.

All file hashes bind exact payload bytes, not theorem truth. Publication
uses the connected GitHub actions and explicit blob/tree read-back. No local
clone or clean full-repository working-tree claim is made.
