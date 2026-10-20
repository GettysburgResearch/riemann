# Executed validation and its limits

The new checker was run with isolated Python, with and without optimization:

    python -I -S -B verify.py
    python -I -S -B -O verify.py

Both outputs are byte-identical to REPLAY.json. All 5,848 explicitly
counted predicates pass. They include 19 polynomial identities, exact
bilinear-rectangle certificates and affine infinite-strip checks, 95
finite quadratic-dual transform identities, 95 finite Gauss-mass checks,
90 local cube/character identities, and all 1,296 four-prime valuation
patterns for the sixth-power-free row decomposition. Several predicates
check structure or bookkeeping rather than independent mathematical facts;
the headline count is not a measure of analytic confidence.

The scalar argument is a continuous-domain certificate, not a grid sample:
its differences are first checked to be bilinear in sigma and log_C(K).
Their extrema occur at rectangle vertices; the unbounded third regime
also checks the affine slope. The symbolic geometric-mean identities
hold for the free splitting parameter, not merely the chosen splits.
The all-prime and infinite-row conclusions still require the analytic
Euler-product arguments in the text.

The checker imports the predecessor's finite-field primitives ONLY after
verifying SHA-256

    a56c35b9dece264ab1471da7aa9a8c314544e08d3d96df596162482d3955879b

for that exact file. Its existing rational quartic-root isolation is
replayed and credited. The decimal fields under inherited_root_certificate
are historical #1010 numerical evaluations, not new sum estimates. The
new rational benchmark values appear separately under benchmarks.

## Deliberate-error controls, actually run

All four new mutations fail in both ordinary and optimized Python:

| Mutation | Designated rejecting predicate |
|---|---|
| wrong-dual | quadratic_dual_transform at F7, v=1 |
| wrong-split | balanced-regime-0 polynomial identity |
| omit-residue | residue_fourth_power at valuations (0,0,0,4) |
| false-consumer | attempted identification of the 11/6 marked cost with 6/5 |

These are controlled failures of named predicates, not unrelated crashes.
The commands are, for example,

    python -I -S -B -O verify.py --mutation wrong-dual

The old #1010 finite checker was also freshly rerun in both modes, with
byte-identical results: 1,983 finite transform checks for 87 characters,
198 additional unit-phase checks, and 87 Gauss-norm checks. Its three
mutations forget-cubic, cheap-quadratic and erase-zero were freshly run
in both modes and rejected at their original local-transform/conductor
predicates. Thus fourteen mutation executions were performed in total.

## Integrity and review boundaries

Python syntax, relative Markdown links, the exhaustive new packet
manifest and all Git blob identities are checked separately before
publication. No external source HTML/PDF byte hash is invented; SOURCES.json
pins versions and source locations actually read. The predecessor proof
blob was checked against the live immutable GitHub object.

This is author-side finite validation and analytic reconstruction. There
was no independent reviewing agent, human referee, second implementation
of the analytic estimates, proof assistant, remote CI run, or
repository-wide validation. No numerical simulation of growing conductor
moments is claimed. The new completed-series mean and its zero-free-input
transfer need independent mathematical review before integration.

The manifest excludes itself and records the exact bytes of every other
new file. Running verify.py with the manifest present verifies that
inventory and each SHA-256 before mathematical checks. Publication is
additive and confined to this new research packet; no main or inherited
research file is modified.
