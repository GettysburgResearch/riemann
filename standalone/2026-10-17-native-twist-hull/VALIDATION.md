# Validation and scope

## Execution actually performed

- `python verify.py` and `python -O verify.py` reproduce CHECKS.json byte for byte.
- The checker has 4,162 explicit finite predicates, including setup and repeated
  guards. This number is not a count of independent analytic examples.
- Four separately executed corrupted optimized processes fail as recorded in
  MUTATIONS.json: wrong inert-prime target phase, erased split conjugate,
  erased nonunit mask, and a false native peak at t=0.
- The earlier #955 standard checker was replayed and matches its archived output.
- The previous local norm-fiber checker was replayed in both modes and matches
  its preserved output. Its mutation-generation script was not newly run.

## Exact finite arithmetic coverage

The complete good squarefree Eisenstein ideal census through norm 512 contains
147 ideals, including the unit. One construction multiplies distinct prime
ideals; another enumerates all lattice ideals and factors their generators.
They agree exactly. Distinct conjugate ideals are not collapsed by rational norm.
Both constructions share the elementary Eisenstein multiplication formula, so
this is not a claim of independent primitive arithmetic backends.

All 20 ideals of norm at most 32 give distinct literal sixth-power rows. Their
field norms and unit independence are checked. At every good prime ideal of norm
at most 128, direct finite-field exponentiation of the sextic character agrees
with the divisibility mask, both for split primes and inert quadratic fields.
All squarefree columns through norm 128 are tested on those rows. These rows
are a complete declared subset, NOT all elements of norm up to 32^6.

There are 20 complete coprime rectangle counts (five column caps, four generator
caps), each checked at moment orders 2,4,6 by an exact Jensen inequality. Residue
degree compatibility is checked for 258 lists, including the incompatible
non-Galois local pattern (1,2). Finite Fourier mass and integer log-frequency
noncollision checks support the approximation proof, not an infinite orbit test.

## A directed rational, rather than floating-point, native peak certificate

A deterministic NumPy exploratory search sampled 1,200,000 integer centers with
seed 955 and selected t=842800609. That search is NOT the certificate and is
not needed for replay. The integer is verified anew using only Fraction:

1. log(n) is enclosed by a positive atanh series after scaling n by a power of 2;
   the omitted tail is bounded by a geometric series. Endpoints are rounded
   OUTWARD to rational multiples of 10^-50.
2. pi is enclosed by Machin's identity with alternating arctangent remainders.
3. A floating-point calculation chooses an integer multiple of 2pi only. Exact
   interval subtraction then verifies that the reduced angle lies inside [-4,4].
   A wrong selector cannot silently make the certificate pass.
4. A degree-64 cosine Taylor polynomial uses the explicit Lagrange remainder,
   with an additional interval-radius error from the bound |cos'|<=1. The
   final printed interval is rounded outward.

The result proves (19) for the COMPLETE stated seven-ideal native window. It is
not a root enclosure, a theta-transform calculation, a finite-height RH check,
an asymptotic certificate, or a certificate for the large prime box in Theorem 2.

## Mathematical and publication boundaries

Proof and checker have the same author; no independent human/agent referee,
proof-assistant build, upstream theta/Lean replay, remote CI or full-repository
validator is claimed. The analytic theorems stand on their written arguments,
not on predicate counts or hashes. Their status remains PROPOSED after upload.

All new files are in one new standalone directory. No old proof or manifest is
modified. The branch update is intended for the existing #955 branch with a
lease against its inspected head; publication receipts must identify the actual
returned new commit rather than treating this intention as a successful push.
