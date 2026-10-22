# Review addendum — L/T/R/M-105110 oriented-edge cancellation

Checkpoint base:
`99a5eef2160e85609da590cb76b632511b33f112`.

## What changed

Exterior simple-event principal parts now have an exact straight-edge
cancellation ledger.  Their absolute norms may diverge while their oriented
integrals stay bounded, provided their projections remain away from corners
and their weighted residues are summable.

The pole-subtracted remainder is separately load bearing.  A fixed-manifest
real-even family with no exterior critical points has an exponentially large
individual edge even though its full normalized contour charge remains one.

## Hostile checks

- Verify the Cauchy-kernel orientation and logarithm/arctangent signs.
- Verify the absolute kernel is the sum of two `arsinh` terms.
- Verify endpoint projection causes logarithmic divergence.
- Verify the weighted first/second exterior residue coefficients.
- Verify both exact \(F_\delta\) quotient identities and edge integrals.
- Keep \(a\) fixed in the absolute-integral divergence statement.
- Verify \(F_N'/F_N=ze^{-Nz^2}\) and the global one-event manifest.
- Verify the rational lower chain giving \(e^N/(5N)>N^2/30\).
- Verify the full contour remains one and no individual-edge conclusion is
  inferred from it.
- Verify the first-only, moving-family, infinite-order, shrinking-window
  scope.

Exact replay:

    python -B experiments/X-105110-principal-part-edge-cancellation/tests/test_verify.py
    python -B -O experiments/X-105110-principal-part-edge-cancellation/tests/test_verify.py

Expected:

    PASS_T105110_PRINCIPAL_PART_EDGE_CANCELLATION
    18/18 normal / 18/18 optimized
    3f0286c2d574e8252fe9903f4f62d86e510275bdf4a1a085e3f232873aec9532

Xi continuation, exterior-event authentication, residue sums, corner
control, remainder estimates, cofinal strict coherence, RCMV104530, and RH
remain open.
