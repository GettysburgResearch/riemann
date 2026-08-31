# Actual complementary-variable action on Chow Tor

Status: preregistered before the first new acquisition, 2026-08-31.
Scope: characteristic-zero source algebra, d=3 and m=2,3; internal grades at most three in this first packet. RH remains unproved.

## Source and independent information

The primitive is R_j=(Sym^j Q^3)^{tensor m}. Source monomials are ordered tuples of exponent triples. The Chow variables are the literal coefficient-one orbit sums W=Sym^m Q^3 inside R_1. Every multiplication and Koszul differential is rebuilt from those monomials. No predecessor Python module is executed.

Authenticate every frozen object before parsing any predecessor JSON:

- a895f47628b0bc7c7ee5e0392df2f79c24166f92, `../MATHEMATICS.md`, blob bbd847461b4955a93b4533fa687cdd8724e2347c;
- the same freeze, `../replay.py`, blob 795566f6ec91bf68dd7ee2f77450e73afd131032;
- the same freeze, `../verification.json`, blob 310ffc95cb6eaf19281de52dd18d2f2884bc0f49;
- 08147ccecfe684af76a8417861fcccda61abe601, `../TERNARY_CUBE_TOR_CHARACTERS.md`, blob f8edf2aac25e96434f77e1fc1681b8f22c609071;
- the same freeze, `../tor_characters.verification.json`, blob 4ea01d1d6fbb0383e31f03f060a8511dd3c7a1e4.

The proposed external proof input is PR782 head 552fe0b78fd96b02fe5836269e6795a992c935be, `standalone/2026-08-31-segre-chow-equivariant-synthesis/THEOREM_I.md`, blob 749cc53453e4842ca010c4028d2a9b35024e3208. Its exact bytes are captured as `sources/PR782_THEOREM_I.md`; no branch merge is performed. It supplies the interpretation of the new action, not its numerical answers.

## Fixed acquisition

1. For both m=2 and m=3 rebuild all Koszul complexes K(W;R) in grades 1,2,3. Match their complete differential hashes, differential ranks and homology weight dimensions with the authenticated primitive records. Check d squared equals zero directly.
2. Let Q=(1-e_sym)R_1. Within each word-content orbit use all words except the first, each minus its orbit average, as the Q basis. This defines a complement, not an arbitrary section of R_1/W. Its dimensions are 3 and 17.
3. Construct exact cycle representatives and full boundary-reduction witnesses for B_0 in grades 1,2,3 and B_1 in grades 2,3. Choices of homology basis are marked and are not claimed equivariant splittings.
4. Compute every Q multiplication on these groups. The ternary-cube focus is the complete 340-column map Q tensor B_(1,2) -> B_(1,3), including zero columns. Retain actual source cycles, action coordinates and boundary witnesses, rather than ranks alone.
5. Reconstruct the quotient multiplication from all symmetric Q-pairs; verify the Q -> B_(0,1) isomorphism, commutativity, and annihilation of B_(0,2) by Q. Check every W action on B_(1,2) against the explicit Koszul wedge homotopy.
6. Compute factor-permutation actions from the source and verify equivariance for a transposition and, for m=3, a three-cycle. Record action ranks and source-defined annihilator dimensions as discoveries, not preset predictions.

The frozen dimension comparisons are calibration inputs: for m=2, B_0 has dimensions 1,3 and B_1 has dimensions 3,1 in grades 2,3; for m=3 these are 1,17,11 and 20,65. Their agreement does not replace any new multiplication calculation.

## Arithmetic, resources and acceptance

Use integer/Fraction arithmetic only. Source grade <=3, total Koszul chain dimension <=5000, each elimination block <=512 rows and <=512 columns, stored exact numerator/denominator bit lengths <=4096, owned artifact <=16 MiB. Stream weight blocks. The first acquisition is expected below 150 MiB and one minute; a 240-second explicit time guard and one-GiB working-set guard refuse excess. No cap is increased within this contract. No computation is duplicated concurrently.

`q_action.py --write` produces `q_action.verification.json`; `--check` reconstructs it from the authenticated primitives and compares canonical JSON, including numeric types. Both modes bind this preregistration, mathematics, replay note, producer, external capture and `tests/test_equivariant_pass_q_action.py`. Reject duplicate JSON keys, floats/Booleans in exact-number positions, nonfinite values, malformed/colliding sparse indices, wrong source hashes, missing action columns, altered cycles, false boundary witnesses, and out-of-cap requests. Test ordinary and optimized Python.

## Meaning and next gate

The result is an actual finite Sym(Q)-module action on Chow Tor, not the ambient Tor table. The E2 page of change of rings requires a further Koszul-Q homology calculation; a higher differential requires still more chain data. No degeneration or nondegeneration is inferred from an Euler-character match. Degree-four/five Q-Koszul work receives a separate preregistration after this action packet is stable.
