# Absorption interface after T-105116

The review target is the conditional chain (H.1)--(H.8) in
`reports/codex/2026-08-23-critical-residue-absorption-interface.md`.

Do not accept a closure unless the review authenticates the off-center Xi
anchors, growth loads, actual-pole manifests, fixed-selector load,
full-shell integrability where used, second-moment absorption, and a
positive signed first moment.  The optimized finite Cartan allocation does
not supply any of those inputs.

For the anchor subtask, review unmerged PR #720 L-104513 and add the
origin-multiplicity (q/z) term before importing its strip-invariance proof.
Then (a=-i) is a simultaneous nonzero anchor.  Treat the L-104531
theta-kernel formula only as a source for a new growth corollary, not as an
already proved cofinal disk bound.

The exact corollary candidate is (H.9)--(H.11) in the absorption report:
an explicit gamma-function bound for every fixed Xi derivative and positive
cosh/sinh moments at (-iy).  Recheck the Fourier normalization and import
the PR #720 source blobs before marking those inputs closed.  In particular,
the standard Xi kernel is twice L-104531's (Phi), so the safe H.9 constant
is (4\pi^2m!\), not (2\pi^2m!\).
