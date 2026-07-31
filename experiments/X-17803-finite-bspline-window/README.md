# X-17803 — Finite B-spline pole-free window

The standard-library checker evaluates the generalized Irwin--Hall spline with
exact `Fraction` arithmetic, verifies normalization and symmetry, and proves the
crude closed `J=12` high-zero moat below `1e-20`.

It is a finite algebra regression, not a Riemann prime-window certificate.
