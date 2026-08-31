# Ternary-cube actual presentation: replay contract

Scientific status: proof and producer are written; the new matrix calculations
and tests have **not yet been run**. The writer runs no computation. Root must
serialize the scout and validation under the shared RAM policy.

The first command is `python presentation_replay.py --scout`. It authenticates
the corrected first source at `a895f47628b0bc7c7ee5e0392df2f79c24166f92`, computes
the marked generators and only the degree-two source kernel, prints bounded
dimensions and exact-bit statistics, and writes no fixture. The full commands
are `--write`, `--check`, and optimized `python -O ... --check`, followed by the
ordinary and optimized suite `tests/test_segre_hadamard_presentation.py`.

The acceptance record retains all source coordinates, sparse evaluation
matrices, generator lifts, relation columns, and old-relation multiples. It
checks exact source substitution, complete weight ranks, primitive integer
normalization, and agreement with frozen Tor dimensions. It is not a fit of a
minimal polynomial, numerator, or Betti table. No predecessor is executed.

Every owned proof/contract/producer/test file is hashed after canonical LF
normalization, and the enclosing record is hashed. Candidate comparison is by
typed canonical JSON with `allow_nan=False`; Python numeric equality is not an
acceptance criterion. The first source's old `6c376a48` checker limitation was
repaired at the pinned `a895f476` freeze; no old executable bytes are imported.

All finite matrices are retained, but the full-presentation conclusion also
uses the proved Chow-module duality and the frozen actual Koszul homology, as
explained in SHP3. Independent review must distinguish proof checking, source
code reading, and parent-reported execution. Second/third differential matrices
and equivariant minimal splitting are not claimed.
