# Grading-genus completion: bounded replay

Status: the proof and preregistration received independent draft review before
this implementation. The new producer and tests have not been executed. Root
serializes all validation under the standing RAM policy; the author runs no job.

The producer authenticates the exact fixed-order source at `8985f69d`, its
source chain, and the full-place, constructible H2, and geometrically connected
joint-cover proofs before importing predecessor code. Actual PBW multiplicities
are compared with an independent odd-divisor formula through source grade64.
No new finite field is enumerated.

Twenty panels use e=1,2,3,4 and five explicit policies: p_n=n,2n,3n;
p_n=1+floor(log2(n)); and p_n=n for n divisible by four and n/2 otherwise.
The latter is divergent but not monotone. Canonical products of literal
two-by-two Frobenius characteristic polynomials, with exponential counterterms,
are compared with independent trace-log series. Generator grades stop at16;
all coefficient cutoffs are at most64. Norm panels additionally allow e*d≤6
and the explicitly changed slope d*kappa≤6, with d=2,3.

Six oriented policy-quotient controls retain finite counterterm coefficients.
The first normalization change is exact: coefficient16 is -49 and coefficient24
is 686/3. The full-source obstruction is the symbolic identity
`Hhat_24=H2_24-49 H2_8+686/3` for the actual integral H2; the producer does not
invent the values of H2_8 or H2_24. Source zero multiplicities and small exact
2-power/7-power noncollision controls are retained. Infinite convergence,
necessity, density, and survival of good-place zeros use the reviewed proofs,
not an extrapolation from these samples.

The fixture binds the proof, preregistration, replay contract, producer, tests,
and source objects. Canonical JSON uses `allow_nan=False` and distinguishes
Boolean, integer, and float values even if a stored digest is left unchanged.
Run `grading_genus_replay.py --write`, ordinary and optimized `--check`, and
the ordinary and optimized `tests/test_graded_completion_grading_genus.py`
under root's serialized runner. The exact-SHA independent report follows the
completed run and science freeze.
