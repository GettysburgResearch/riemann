# Recovery publication — 17 October 2026

This commit restores all 25 files from the previously delivered add-only
`riemann-affine-cancellation-and-recovery.patch`, without changing their bytes.
The old NOT PUSHED labels and old execution descriptions are historical;
this separate record supersedes only their publication status.

Base: a93d382951f8fac7b0c28783061a7ddb99fcf0a4 (PR #953).
Branch: research/affine-recovery-and-growing-shifts-20261017.

Recovered complete subtrees:

- Eleven-file affine packet: 4af7d5a47b4e51a3414fd8aa06f8e5f2221c837e.
- Thirteen-file mesoscopic packet: 13d3f1121d05f547e2067fe25103d4051e4b20cf.
- Original one-file recovery notice is also retained unchanged.

Both tree identities match the mounted originals. Both original manifests
passed. On this publication pass, BOTH complete exact checkers were freshly
run under ordinary Python and python -O; all four outputs match the respective
archived JSON byte-for-byte. The old mutation and numerical-quadrature records
are preserved; those processes were not freshly rerun. No independent review,
Lean build, complete repository CI or analytic certification is claimed.

This is a recovery checkpoint, not a mathematical strengthening. Outside
results will be imported at their precise hypotheses in a separately labeled
continuation. The original fixed-shift scope and the distinction between
positive selected covariance and total signed energy remain unchanged.
Main and integrated scientific status are untouched. Publication is through
connected GitHub actions, not a claim of a clean cloned worktree.
