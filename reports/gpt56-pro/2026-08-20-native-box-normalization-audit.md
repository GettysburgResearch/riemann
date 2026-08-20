# Native-box normalization audit

The attempted proof of `GPMOC99800` exposed a prior statement-to-use mismatch
before the final off-diagonal estimate.

PR #658 fixes the exact normalized box pairing with vertex measure `g(n)/n`.
Consequently the Euler coefficient attached to a newly adjoined prime is
`p^-1`. PR #664's `L-99819` instead applies the `p^-1/2` operator to the
normalized potential. That operator is appropriate before the root
`sqrt(X)` normalization, but not afterward.

The correction changes the claimed plain Mertens window into the half-order
three-band window in `L-99900`. This is scientifically material: the new window
is the existing squarefree-core/GPMOC correlation, not a simpler unweighted
object.

A second exact advance rewrites the Poisson phase square as a Hardy tail square.
This removes phase-integration ambiguity but leaves the RH-bearing cumulative
Möbius cancellation intact.

RH remains unproved.
