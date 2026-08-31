# First actual change-of-rings d2: three highest-weight blocks

Status: preregistered before shape enumeration or differential acquisition.
Date: 2026-09-01. This is a separate continuation; the first Q-action packet is not rewritten.

## Target and frozen inputs

Work with the same ternary-cube source and complementary Q of dimension17. The immediate source is the accepted first `q_action.py`/`q_action.verification.json` freeze c7ea79747208dfa6e164cb87c2e4f9ee523cbb3d. These pins were installed after the preregistered shape calculation and before any differential acquisition. Its 340 boundary witnesses are essential inputs. Also authenticate the original a895f476 primitive and the 08147cce Tor-character proof/artifact before parsing or loading helpers. Reuse the frozen Q-action arithmetic/source helper only after exact-byte authentication; do not modify its grade-three cap or any old module.

The target is

    d2: E2_(2,1),internal4 -> E2_(0,2),internal4 = B_(2,4).

The target has character [552](1+standard)+[642]sign+[543]sign, dimension65, by the previously accepted source computation and duality. Surjectivity is a preregistered target, not assumed. No ambient Tor vanishing theorem is an acceptance premise.

## Fixed coverage and experiment

Use exactly the dominant total weights (6,4,2), (5,5,2), (5,4,3). First enumerate each relevant original Koszul-W chain basis in internal degree4, and the source/target bases of

    delta: Lambda^2 Q tensor B_(1,2) -> Q tensor B_(1,3).

Output exact sizes before elimination. Each complete weight block must have <=512 rows and <=512 columns. Refuse, and retain the shape report, if this fails. No arbitrary submatrix or random vector replaces complete coverage.

For every kernel vector z of delta in each of the three blocks, use the first packet's identities q*c=sum M(q)c'+d_W eta to construct a lift eta_z of its Q differential. Compute delta_Q eta_z in the original degree4 Koszul-W chain group, verify it is a cycle, and reduce it modulo complete W boundaries. Retain z, the lift, the resulting source cycle and the exact target quotient coordinates. Record all kernel vectors, including those with zero d2 image.

Independently certify each target H2 weight space from the full local d_W maps and match its dimensions/class traces to the frozen Tor-character table. Check that the image is stable under a factor transposition and a three-cycle. Determine its exact rank; accept partial rank as a partial result, not a success verdict for surjectivity.

## The theorem gate

If the d2 image surjects onto the whole target weight space at all three weights, then it surjects onto all of B_(2,4): any nonzero semisimple GL3 quotient would contain an irreducible summand with one of those highest weights, contradicting the corresponding full-weight surjectivity. Repeated S3 multiplicities do not evade this test because the full weight space is covered. The representation type is an explicit imported input.

The map is a genuine spectral-sequence d2, not multiplication on E1: boundaries from Lambda^3 Q tensor B_(1,1) are zero since B_(1,1)=0, so the displayed delta kernel is E2_(2,1),internal4. Also Q cannot enter B_(2,4) from degree3 because B_(2,3)=0, making its E2_(0,2) target equal to B_(2,4).

## Arithmetic and replay

New producer `d2_replay.py`; new artifact `d2.verification.json`; tests `test_equivariant_pass_d2.py`. Modes `--shape`, `--write`, `--check`. Shape mode has no rank acceptance. Full acquisition requires all pins. Exact rational arithmetic, coefficient cap4096bits, block512, sparse-lift cap4096terms, artifact16MiB, working set1GiB, wall time240seconds; expected below150MiB and30seconds. The sparse-lift guard was installed in the producer before any differential acquisition. Authentication precedes any imported-code execution or artifact parsing. Typed canonical JSON, full body hashes and source/owned proof bindings are required. No stale cache or predecessor continuation is read.

Negative controls must change a Q-boundary lift, a Koszul sign, an actual source cycle, complete block coverage, a primitive/source binding, and typed numeric encodings. Both normal and optimized replay are required. No general degeneration statement, new complete resolution, arithmetic purity or RH assertion follows.
