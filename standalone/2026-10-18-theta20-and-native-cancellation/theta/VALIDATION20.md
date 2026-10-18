# Validation scope

## Acceptance arithmetic and source

`certify20.py` uses only exact integers, Fractions, and inherited outward
intervals with denominator 2^320. It authenticates the primitive source, reads
the exact rational parameter center, checks all graph inequalities on the
specified ten-coordinate cube, reconstructs the original infinite theta
moments through 20 with 98 cells, six explicit indices and every Taylor/time/
index tail, recomputes the exact rational center Jacobian, verifies both
matrix-inverse identities, and bounds the complete box Jacobian.

The root claim requires the three strict rational predicates in PROOF20.md,
Section 3. It does not accept overlapping moment intervals as an existence
proof. `certificate20.json` is accepted only when exactly reproduced by this
full reconstruction.

## Independent finite assemblies

`check_connected.py` directly enumerates all 128 states of a seven-spin tree,
including the normalized Gibbs product, both hub signs, two unequal dimers
and repeated fair leaves. Every raw moment0through 20 agrees exactly with the
conditional recurrence. Deleting a positive internal edge changes variance.

A second finite assembly multiplies all conditional generating polynomials
for the actual305-spin rational-center model, with integer powers for every
multiplicity. All raw moments0through 20 agree exactly with the cumulant-based
implementation. This independently checks the entire finite model's assembly
at its rational center. The interval contraction supplies the actual theta
root. This assembly is not a direct 2^305-state enumeration.

## Ordinary, optimized and corrupted runs

`replay.py` authenticates the payload manifest and runs both accepting scripts
in ordinary and optimized Python. Their complete standard-output strings must
agree and their complete saved receipts must be reproduced. It then launches
four separate optimized corrupted subprocesses. The exact required failures
are:

| Corruption | Required failure |
|---|---|
| Erase hub correlations | complete seven-spin assembly mismatch |
| Reverse one inner-amplitude orientation | complete seven-spin assembly mismatch |
| Reduce the fair-leaf multiplicity | complete seven-spin assembly mismatch |
| Omit the twentieth moment | all raw moment orders 0through 20 required |

Each subprocess must return nonzero and include its specified failure message.
The separate replay receipt records those actual executions. The corruption
suite tests the finite assembly; it is not an adversarial reimplementation of
the entire transcendental primitive. The mathematical proof of the primitive
and tails remains an explicit dependency.

## What is and is not claimed

The packet contains one proposed finite computer-assisted theorem. The exact
root, its full source and all graph inequalities are verified by directed
arithmetic subject to the stated code and mathematical proofs. The interval
implementation is inherited from #988/#886, not independently written. The
main polynomial author also wrote these finite controls; independent reviewer
work must be recorded separately at exact file hashes or a frozen commit.

No formal proof-assistant verification, remote CI, repository-wide validator,
certified continuation path, zero census, global extension theorem or RH proof
is claimed by these scripts. A later review or publication receipt may document
additional verification; it does not retroactively change this scope.

## Producer and finite witness data

`produce_center.py` and `seed20.json` reproduce the terminating-rational center
using 100-digit Decimal Newton iterations with the ten fixed active indices.
The source intervals are reconstructed afresh and only their midpoints are
used by this optional nondirected producer. The full source uncertainty is
paid by the separate directed checker, which does not read the seed or execute
Newton iterations. The accepted theorem can be checked directly from its
finite rational center without trusting the historical search.
