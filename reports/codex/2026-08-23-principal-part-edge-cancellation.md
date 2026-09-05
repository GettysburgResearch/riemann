# Principal-part cancellation and the independent remainder debt

Date: 2026-08-23

Checkpoint base: `99a5eef2160e85609da590cb76b632511b33f112`

## Outcome

The absolute edge obstruction of L/T-105109 does not by itself obstruct an
oriented contour route.  For a simple exterior pole approaching the interior
of a straight edge, the singular Cauchy kernel has a bounded oriented
integral but a divergent supremum and absolute integral.

A complete finite split

\[
Wh=R+\sum_j\frac{r_j}{z-p_j}
\]

therefore yields a collar-independent edge estimate from three explicit
debts: corner-projection separation, a weighted-residue \(\ell^1\) sum, and
an \(L^1\) bound for the pole-subtracted remainder.

## Simultaneous quotient fixture

For

\[
F_\delta=e^{z^2/2-\delta z},
\qquad w=z-\delta,
\]

both programme carriers are rational:

\[
F_\delta/F_\delta'=1/w,
\qquad
F_\delta^2/(F_\delta'F_\delta'')
=1/w-w/(w^2+1).
\]

On a centered vertical edge their oriented integrals converge to
\(-i\pi\), while their suprema and absolute integrals diverge.  Cutting the
edge at the event projection produces a logarithmic one-sided divergence.

## Remainder firewall

The family

\[
F_N=\exp((1-e^{-Nz^2})/(2N))
\]

is real-even and zero-free, and \(F_N'\) has only the simple zero at zero in
the entire plane.  Its first target residue and optimal selector norm are one.
Nevertheless, on a shrinking-height rectangle with fixed width, the upward
right-edge integral exceeds \(e^N/(5N)>N^2/30\).  The full normalized contour
charge remains one.

There is no exterior critical principal part to blame.  The pole-subtracted
holomorphic remainder carries the growth, proving that manifest, parity, and
selector data do not make individual-edge cancellation automatic.

## Prior-art audit

No `L/T/R/M/X-105110` collision exists across the current tree or fetched
refs.  The closest programme antecedents are draft PR #720
L-104512/L-104521/L-104523, which identify phase and contour quantities but
do not bound these weighted oriented edges; PR #720 L-104519, which controls
a different Hermite--Biehler log-derivative-difference edge under an ordered
far-right exhaustion; R-105106, which requires retaining a holomorphic
remainder; and L/T-105109, which explicitly leave the phase-cancellation
route open.

The Cauchy-kernel integration and residue theorem are classical.  Novelty is
claimed only for the exact programme-specific debt split and simultaneous
first/second quotient fixture.

## Exact authentication

    PASS_T105110_PRINCIPAL_PART_EDGE_CANCELLATION
    18/18 focused tests in normal and optimized Python
    3f0286c2d574e8252fe9903f4f62d86e510275bdf4a1a085e3f232873aec9532

No numerical quadrature or heavy computation is used.

## Remaining gate

A Xi application must continue the weighted quotients across each open edge,
authenticate all approaching exterior events, control their weighted
principal coefficients and corner positions, and estimate the pole-subtracted
remainder.  It must then combine those edges with Green–Gram selector costs,
correction terms, multiplicity defect, and strict jet coherence.  RCMV104530
and RH remain open.
