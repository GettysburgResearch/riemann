# Executed validation and the limits of the evidence

The new mathematical conclusion is a proposed proof requiring independent
review. Computer execution does not independently accept the BGST theorem,
the Hilbert-space source identity, or the new all-matrix spectral lemma.

## Complete inherited pressure replay

The two files under pressure/ exactly match the Git blobs at frozen main:

- dyadic_interval.py: 0b7bbbb7b3011d22399be8430710996cbdbf4258
- seven_independent_cached.py: a659bf129a09d6f3c339c673677f63a523e937f2

Their SHA256 and byte counts are in SOURCES.json. The local files were
extracted from the user-supplied Reviewer A archive, and their Git identities
were compared with the current repository listing. Their entire source was
read, not only their old result file.

Both complete searches were freshly run during this pass:

    python -B seven_independent_cached.py seven_result.fresh.json
    python -O -B seven_independent_cached.py seven_result.optimized.json

Both returned exit code zero. Elapsed times were about 248.48 and 249.08
seconds on this machine. All mathematical fields and all three table/traversal
hashes agree. The elapsed-time field appropriately differs. The two complete
output files are retained as pressure/verification.json and
pressure/verification.optimized.json. There were 713315 visited nodes and
no unresolved final cell; these are parts of ONE continuum proof, not 713315
independent mathematical theorems.

This is a replay of the earlier independent implementation, not another fresh
backend or non-author review. The pressure search uses directed 128-bit
dyadic transcendental primitives together with outward binary64 range-minimum
and accumulation bounds. Correct rounding and nextafter are explicit parts of
its arithmetic contract. No original Arb transcript or full past mutation
campaign was rerun. The labels containing “independent” in the unchanged code
refer to its earlier independence from ainta's original implementation.

## New exact constants and finite coverage controls

The new check_constants.py runs successfully with normal and optimized
isolated Python. It regenerates constants.json byte for byte in both modes.
Its only numerical arithmetic is integers and fractions. Cosine and sinc at
u^2=1/2 use alternating rational series; radicals use integer-square-root
brackets with exact squared-endpoint checks. No zeta value, supplied zero,
ordinary floating constant or quadrature is used.

The program also checks the block-offset and gap-incidence formulas for a
bounded set of sizes, independently of the paper's arbitrary-size proof.
The displayed block 322 is fixed in the accepting program. Exploratory mpmath
calculations selected it; no optimality assertion or exploratory number enters
acceptance.

For each mode, a pristine full constants receipt is accepted and FOUR actual
changed JSON files are rejected through the real command-line checker: a false
RH status, a Boolean replacing the block integer, an altered bound, and a
duplicate-key record. These are constants-receipt tests, not fresh perturbed
pressure searches or proofs of analytic soundness. Exact subprocess outcomes
are retained in EXECUTION.json. No assert controls accepting arithmetic.

## Package and publication

A SHA256 manifest authenticates every regular payload file other than itself.
An addition-only patch and fresh ZIP extraction are checked for byte identity.
The normal and optimized constants program is replayed after extraction. The
entire pressure calculation is not run a third time after packaging: the two
unmodified code files and complete outputs are authenticated by the manifest.
A small Git fixture is used only to validate the patch's additions; it is not a
full checkout of riemann and is not reported as repository-wide validation.

GitHub reads verified main and the prior research head. This session exposed no
repository publishing action; direct Git transport failed DNS resolution. Thus
this delivery is LOCAL. An uploader must create a separately recorded commit
and PR, and may not claim that the author session already pushed the packet.
No remote CI, full repository validator, native Windows execution, proof
assistant, independent referee acceptance or record claim is made.
