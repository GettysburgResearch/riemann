# Finite validation and its limits

Status: finite replay only, not an infinite analytic certificate.

## Accepting computations

`verify.py` contains 3,370 explicit predicates. Both ordinary and optimized
Python produce the same CHECKS.json bytes; all checks use explicit failures,
not Python assertions. Counts are broken down by gate in the JSON.

The declared complete ranges include:

- Integer cycle/cyclotomic polynomials n=2..96, all coefficients, all divisors,
  primitive degrees and exact prime-power constant terms.
- 57 complete rational matrices: n=2..20 at masses 0,1/16,1, with exact
  LDL positivity and determinant comparisons, retaining complementary modes.
- All full integer products N=2..64 through prime powers, lcms and cyclotomics.
- 124 complete divisor-fiber identities, including the unit correction, and
  627 exact endpoint-aware polynomial quadratures including noninteger N/m.
- 800 whole valuation rectangles and the same 800 all-p floor budgets.
- 25 short-conductor parameter fixtures, including growing integer sizes,
  tested by integer fourth-root and rational logarithm enclosures. These are
  parameter checks, not 25 actual quadratic-field constructions.
- 108 rational conjugate-pair/disk identities, an enclosing exponential
  calculation for the rational disk constant, and the exact Mellin continuum.
  The zero coordinates are synthetic, not numerical L-function zeros.
- 30 complete regularization comparisons: N=2,3,4,5,8,12,20,32,48,64 and
  c=1/4,1/2,1. All log-determinants and the INFINITE B(c) constant are enclosed
  by rational intervals, then compared with the finer rational error budget.

The stored enclosure is

    0.002877500498 <= B(1) <= 0.002877503173.

It is an enclosure, not an exact decimal or a fitted constant. The proof
uses B(c)'s infinite definition. Matrix coordinates are grouped into predicates;
3,370 is not a count of independent analytic propositions.

## Transcendental trust boundary

Positive rational logarithms are enclosed using a power-of-two reduction and
the positive atanh series with a geometric remainder. B(c) is enclosed using
eight Bernoulli terms, rational upper/lower integral bounds for zeta(2j+1),
and the entire Bernoulli-series tail. Pi>3 and the classical Bernoulli/zeta
identity justify the deliberately generous tail constant. No binary64
comparison is used for acceptance. Decimal strings are rounded OUTWARD from
rational interval endpoints.

Python's integer/Fraction arithmetic, the mathematical remainder derivations
and this implementation remain in the trust base. This is not a proof-assistant
formalization or a separately developed transcendental backend.

## Eight executed negative controls

MUTATIONS.json records actual optimized subprocess failures at the specified
gates: erased primitive projector; doubled mass; removed higher prime powers;
unsigned Mobius; deleted unit correction; lost Gram factor two; deleted the
conjugate zero; and wrong continuum. replay.py reruns every one and rejects
unexpected failure locations as well as false acceptance.

The original #993 normal/optimized replay and its seven original corruptions
were also freshly rerun from the delivered archive. That archive was already
published; no new recovery, theorem acceptance or duplicate import is claimed.

An initial combined normal/optimized/mutation command exceeded the 20-second
container limit after both positive outputs were written. The positive outputs
were compared, and the entire mutation batch was then separately rerun to
completion. The interrupted command is not counted as a successful full replay.
The final complete replay and any fresh-extraction/patch checks are recorded
in the external delivery receipt, not inferred from a timeout.

## Not done

No independent mathematical referee, second research agent, Lean build,
upstream theorem rebuild, actual zeta-zero computation, GitHub remote CI or
whole-repository validator was run. The new critical upper-height estimate
OPEN-PH was not proved. GitHub publication did not succeed in this session.
