# Review addendum — L/T/R/M-105112 selector-domain repair

Checkpoint base:
51c67046a726be188bf724f7b4652e299bd31ccb.

## What changed

The scalar selector norm \(\tau\) now enters an exact weighted-sup equality
only when the edge lies on the boundary of the exact selector domain.  On an
arbitrary edge the valid statement uses the actual norm \(\|W\|_E\); on a
compact subset of the domain closure, \(\tau/m\) remains an upper envelope.

This forward erratum marks the frozen L/T/M/metadata/report/PR-body wording
of packet 105109 as overbroad or ambiguous under a literal domain-free
reading.  It does not alter those files or retrospectively verify X/T-105109.

## Hostile checks

- Trace the exact selector domain through each equality.
- Require \(E\subset\partial\Omega\) for pointwise modulus \(\tau\).
- Use only an inequality on an arbitrary edge.
- Verify the unit-disk manifest and optimal selector \(z^2\).
- Verify \(F''=z^2(z^4+3)F\) is nonzero on both fixture arcs.
- Verify the radius-\(1/2\) values \(1/8,1/4,2,8\).
- Verify equality is recovered on the unit semicircle.
- Confirm all frozen 105109 and 105111 files remain untouched.
- Confirm no retrospective 105109, Xi, RCMV104530, or RH claim.

Exact replay:

    python -B experiments/X-105112-selector-domain-repair/tests/test_verify.py
    python -B -O experiments/X-105112-selector-domain-repair/tests/test_verify.py

Expected:

    PASS_T105112_SELECTOR_DOMAIN_REPAIR
    15 / 15
    3748777ede886502e57c6ad77777807b11b98104a8ecba04b60f162b10e2b19c

Xi collar/margin inputs, cofinal absorption, cancellation, strict
coherence, RCMV104530, and RH remain open.
