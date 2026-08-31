# Durable weight-block acquisition for stage five

This separate fallback is declared after repeated reserve interruptions of
the one-shot stage-five acquisition, with no mathematical failure observed.
It does not edit the frozen full producer or its certified-cache verifier.
Root alone executes it under the existing worker/reserve limits.

The checker and its 13 tests are pinned at
`356160f075ee72aed21ee03a6daf30fa3222799a`. They in turn authenticate the
exact source algorithm and successful stage-five summary at `b1c48ff9`.
The fallback uses the same ordered weight blocks and the same rational
kernel function. A call is restricted to one weight block; its resulting
local domain indices are translated back to their original matrix indices.
Because the selected column order and pivot-row order are unchanged, these
are the same primitive integer kernel vectors as the one-shot calculation.
Neither a basis dimension nor a prescribed Tor character supplies a vector.

For every matrix, compute its complete ordered-basis and column digests.
Each checkpoint key additionally binds the exact source/verifier identities,
this fallback's proof/code/test bytes, the weight, original column indices,
and the literal sparse block coefficients. Only a complete block is written,
using flush, fsync and atomic replacement in the task's weight-block directory.
An interrupted temporary file is never read as a completed block. No previous
files or directories are deleted.

Before reuse, check the exact metadata/body digest and reconstruct the block
from the current authenticated maps. Verify every primitive integer kernel
vector in those columns, unique largest coordinates, homogeneous weights,
all literal metadata types and a matching fixed-prime rank lower bound.
The same checks are made before a newly computed block is saved. These prove
rational completeness independently of the retained diagnostic elimination
bit count. The only moduli are65521 and1000003 from the existing verifier.
No unregistered modulus, rank estimate or numerical kernel is used.

The completed calculation must reproduce the frozen full stage-five summary,
the degree-four map digest and the exact old/new quotient checks. It writes
the identical `resolution_stage5.pending.json` schema used by the one-shot
producer, with `certified_for_continuation=false`. It separately records the
block manifest and reused/computed counts as acquisition diagnostics. Root
must still run the unchanged `resolution_stage5_cache.py --verify-pending`
and `--check-cache`, then freeze the certified cache before continuation.

All caps remain512 supported block rows/columns,4096 exact bits,90000 target
basis entries,16000 domain entries and64MiB per artifact. The dedicated tests
cover source authentication, exact local/global index translation, numerical
label rejection, matrix/digest mismatches, incomplete kernels, checkpoint
type/scope changes and interrupted-file handling. This is an execution
resilience change, not a new mathematical source or a larger theorem.
