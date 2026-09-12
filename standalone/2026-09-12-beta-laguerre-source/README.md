# Exact coordinates for the actual homotopy, and its singular endpoint

**BLS26 — proposed component mathematics; RH and the signed zero-production estimate remain unproved.**

This is an add-only research continuation of PR #876 at
`8002444ec4d4bd1c6f8fa073820bcc575cb218e1`. It does not alter the parent, main,
accepted statements, review files or workflows. Its recommended review status is
DRAFT / PROPOSED, not a completed RH proof.

Start with **PROOF.md**, then **ATTEMPT_AND_REVIEW.md** and **VALIDATION.md**.

## What the new argument establishes

The actual beta-to-Brownian fixed-point law has a uniform gamma-relative L2
bound. Its full Mellin transform consequently has an absolutely convergent
Laguerre series with exact rational-function coefficients and a complete
explicit complex tail estimate. A second nonlinear convolution recurrence
reconstructs those same coefficients directly in orthogonal coordinates,
without importing a raw numerical moment table.

The intermediate source is not entire: for every theta<1 it has poles at -10
and 11 in the indicated extended domain. Their residues vanish quadratically
at theta=1. The coefficient is exactly 1024 pi^5/11907 for the normalized
residue at -10. The proof also establishes one simple REAL zero approaching
each pole from the outside as theta tends to one. These zeros are outside the
critical strip and are not Xi zeros. The parameter threshold is unevaluated. Consequently an entire multiplier
that clears the poles cannot place this whole homotopy in a GLOBAL Lee–Yang
class: those existing outside-strip zeros survive multiplication. The weaker
critical-strip route remains open.

## What did not succeed

The intended use was to obtain the actual sign of nonreal-zero production.
Nondirected derivative truncations were unstable and supply no sign verdict.
The new rigorous function-value tail bound is deliberately conservative; no
native contour/zero/collision certificate was obtained from it. Differentiating
finite coefficients does not pay for the remaining parameter-derivative tail.
The new density and coordinate theorems do not imply zero confinement.

The exact parent source response and all existing corrections remain intact.
The work is not an independent audit of the full repository or of every parent
analytic claim. Existing fixed-point and source-order inputs are explicitly
stated and partially reconstructed in PROOF.md.

## Replay (standard library, Python 3.10+)

From this directory:

```sh
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
python -I -S -B test_check.py
python -I -S -B -O test_check.py --optimized
```

`check.py --no-auth` is explicitly a development mode, NOT an authenticated
acceptance. No floating-point value, numerical zeta/gamma routine or root list
enters the accepting checker. The checker validates bounded algebra and
constant arithmetic, not the written infinite theorems.

Optional `scout.py` requires mpmath and is NONCERTIFYING. Its unproved derivative
tail is prominently identified. It writes only to a user-supplied path outside
this authenticated packet. `scout_comparison.json` is a disclosed exploratory
record, not an input to any proof or numerical acceptance.
