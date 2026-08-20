# Hostile continuation after the active-pair/collar wave

The newest PR #664 appears to simplify the collar obstruction to an unweighted
ratio-67 Mertens window. That simplification does not survive the canonical
normalization.

The box scalar before normalization has coefficient `beta(n)/sqrt(n)` and
kernel `W`. After division by `sqrt(X)`, the kernel becomes `phi=W/sqrt(.)`
and the coefficient becomes `beta(n)/n`. A rough-prime step consequently
changes from `p^(-1/2)` on `W` to `p^(-1)` on `phi`.

This correction is load-bearing. With `p^(-1/2)` the deep half-order mode
cancels and the collar slope becomes an unweighted Mertens window. With the
native `p^(-1)` coefficient the half-order mode survives and the collar slope
is the half-order duplicate-67 window. Its subpower negative-mass estimate is
RH-equivalent.

The pass also opens PR #659's Poisson square. Cauchy averaging produces the
kernel `min(m,n)^(2 tau)`, whose exact Brownian/Hardy factorization is the point
value plus all nested tail squares. This identifies precisely what an owner
Carleson theorem must control and prevents local phase coercivity from being
mistaken for off-diagonal cancellation.

The result is a substantial normalization repair and a sharper frontier, not a
proof of RH.
