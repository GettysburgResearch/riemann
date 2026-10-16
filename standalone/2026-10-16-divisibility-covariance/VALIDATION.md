# Validation and review limits

## Mathematical scope

THEOREMS.md supplies complete proofs of the uniform divisibility-sector
bound, the two-pole square-coefficient expansion, the signed all-prime-
quotient asymptotic, and the four-prime forced-positive-remainder corollary.
No critical arithmetic hypothesis is assumed. The field is specifically
Q(omega) when the signs of the secondary residues are asserted.

The estimates with a power-saving remainder fix m and S before D grows.
Only the absolute comparability bound is asserted uniform in m and arbitrary
masks. The one-prime-removed Mellin error is uniform in the one moving prime,
not in arbitrary moving fields/exclusions. The principal negative sign
requires a_p=1. Higher-channel phases are unit but otherwise arbitrary.
The distinct differences 1,m-1,m require m>=3.

## What was actually run

1. `python check.py` and `python -O check.py`, at the default cap 200,000.
   Both produce RESULTS.json byte for byte.
2. Four separately executed mutated `python -O` processes: wrong prime sign,
   deleted m-1 overlap channel, erased nonunit masks, and wrong powerful
   coefficient weight. Every process exits nonzero at a recorded check;
   MUTATIONS.json retains the actual last error line and return code.
3. Syntax compilation and the final payload hash check.

Exact coefficient-pair fixtures use a new explicit Q(omega) implementation
and literal residue fields for split norms 7,7 and inert norm 25. The unit
root is epsilon=1+omega and is tested against ring exponentiation. All 54
nonzero rows with Nu<=13 are used for m=6; eight specified rows are used for
m=4 and m=8. Each coefficient-pair fixture contains all 27 ideals with local
exponents in {0,1,m} on ONLY these three prime ideals. It is NOT all native
ideals up to a large norm cutoff. The 51,030 pair equalities compare direct
coefficients with an independently assembled forced-gcd formula. The 1,890
prime-quotient equalities and literal zero tests are separately recorded.

The separate norm census is complete, not a small semigroup. It evaluates
n^2 times sum_(NI=n)|c_m(I)|^2 for EVERY integer norm n<=200,000, at each of
m=3,4,6,8. One producer multiplies the norm Euler factors with split-prime
multiplicity. The second enumerates the complete squarefree powerful ideal
d and its coprime squarefree partner r in I=r*d^m. All 800,000 resulting
integer coefficients agree; the report gives the full-vector SHA-256 per m.
The first norm-7 sixth-power fiber at 117,649 includes both conjugate prime
ideals and is separately checked. The producers share elementary prime
splitting and Python arithmetic; they are not independent formal referees.

The rational Euler-polynomial, residue-scaling and four-prime inequalities
are also checked. Repeated setup guards in the report are not independent
analytic examples. No fitted numerical slope, random sample, large finite
case, or checker success is used as proof of an infinite asymptotic.

## Self-review and limitations

The same author checked the proof for wrong Gaussian-CDF shifts, missing
1/m residues, an omitted m-1 shared-prime channel, prime ideals of equal
norm being conflated, inadmissible moving-prime constants, and an illicit
absolute summation over two large incomparable cores. The final proof
includes the required domains and exclusions beside the relevant formulas.

An exploratory floating-point calculation of the leading/secondary constants
was performed while developing the proof. It was NOT interval-certified,
is not part of the acceptance tests, and no numerical constant from it is
used in a theorem or the exact 5% margin. The latter is a rational Taylor
bound, not an optimizer or floating inequality.

No independent agent/human mathematical review, Lean build, upstream theta
reconstruction, full-repository validator, or remote CI run was performed.
A successful content hash authenticates bytes, not mathematical truth.

Preferred adversarial review: Theorem A's quotient classification and infinite
sum; (4.2)--(4.8)'s continuation and uniform one-prime division; (5.4)--(5.5)'s
Laurent/CDF residues; the all-prime interchange in (6.5); and the exact
complement definition in (7.2). Incomparable-core cancellation is not proved.
