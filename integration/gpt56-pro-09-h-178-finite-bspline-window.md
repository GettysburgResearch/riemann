# Integration handoff — finite high-order B-spline window

Add `L-17803/O-17803/X-17803` to PR #190.

The `J=12` window replaces the infinite convolution and FFT evaluator by one
exact degree-23 rational spline while retaining `|t|^-24` decay and an explicit
high-zero moat below `1e-20` after the first 100 phases.

Compose it with `L-17802` first differences and the exact phase-band comparator
of PR #181. No RH claim.
