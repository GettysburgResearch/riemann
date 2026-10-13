# Validation and limits

## Mathematical status

PROOF.md contains proposed complete arguments for the finite projection,
the absolute Rankin majorant, the logarithmic-conductor sectors and their
one-sided remainder identity. The supercritical sharpness construction
uses one named classical prime-distribution input. The author checked the
proof locally; **no separate agent or human independently reviewed this
pass**. No formal proof assistant or upstream theta implementation was run.

The missing arithmetic statement is PROOF.md (5.4). The finite computation
does not establish it, a full fourth moment, a generalized hierarchy or RH.

## Actual execution

The standard-library checker ran under ordinary Python and `python -O`.
Both outputs were byte-identical, and both equal results/exact.json.
All acceptance guards use explicit exceptions, not removable assertions.
There are 4937 successful explicit predicates, including four negative
controls. The detailed counts are in the report.

Coverage includes:

- multiplication and conjugation in the exact sixth-root ring;
- actual residue characters at a split pair of norm 7, a split prime of
  norm 13, and an inert prime of norm 25, including their zero fibers;
- the local Rankin polynomial at orders 3, 4, 6 and 8 and k=1,...,12;
- equality of direct finite random averaging, literal Hermitian tuple
  expansion, and rough-charge block aggregation for bounded fixtures;
- all element rows at the four declared native test heights, with both
  positive and negative rough remainders;
- rejection of discarded sixth-power aliases, redrawn nonunit zeros,
  and either false monotonic comparison between native and projected
  moments.

The finite table is an arithmetic diagnostic with a hard norm window,
not an asymptotic experiment. It retains both conjugate split ideals,
the inert square norm and each nonzero element row, rather than sampling
only squarefree or principal rows. Its maximum column norm is 128 and
maximum row norm is 64. It cannot test a D-to-infinity estimate.

## Integrity

MANIFEST.json binds the released local files by byte length, SHA-256 and
Git blob SHA-1. checks/verify_manifest.py verifies exactly that inventory.
The manifest excludes itself to avoid a self-reference and includes the
verifier. A hash authenticates file identity, not a theorem.

This working environment could not resolve github.com for a local git
clone. Repository reads and publication use the connected GitHub actions.
A full local repository checkout and worktree cleanliness are therefore
not claimed. The final PR metadata and remote file identities must be
read back before reporting publication success.
