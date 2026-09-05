# Research report — primary-cardinal selector conditioning

Date: 2026-08-23

Branch: `codex/105100-residue-second-moment`

Claims: L/T/R/M-105106

## Outcome

The fixed-window selector existence result L-105105 can be sharpened much
more than a generic Hermite interpolation bound.  Its prescribed datum is
always the top local primary jet.  Therefore the unique reduced selector is
the elementary primary-cardinal sum

\[
W=\sum_c\gamma_c(z-c)^{d_c-1}M_c/M_c(c).
\]

No confluent inverse is needed.  The exact condition numbers are

\[
\kappa_c=|M_c(c)|^{-1}
=\prod_{a\ne c}|c-a|^{-d_a}.
\]

They give a computable finite-window coefficient and boundary envelope.  The
quotient also collapses:

\[
W/M=\sum_c\gamma_c/[M_c(c)(z-c)].
\]

Thus each weighted edge is bounded by a first-power target-to-edge distance,
the cardinal conditioning products, and one pole-cancelled holomorphic
factor.

## Sharp obstruction

Real/even symmetry does not cure conditioning.  A target at zero and
clustered symmetric nontargets give

\[
W=(1+z^2/\varepsilon^2)^m,
\]

with degree \(D-1\) and norm of order
\((B/\varepsilon)^{D-1}\).  Finite Blaschke factorization proves the same
scale for every holomorphic exact selector, so increasing the degree cannot
repair it.

The quartic

\[
F_\varepsilon=1+\varepsilon^2z^2/2+z^4/4
\]

simultaneously realizes the first and second L-105105 obstruction.  At
\(\varepsilon=1/5\), the exact unit-circle selector norms are \(26\) and
\(1976\), within factors \(26/25\) and \(1976/1875\) of the Blaschke lower
bounds \(25\) and \(1875\).

## Prior-art audit

L-105101 and L-105102 supply exact edge/parity identities, and L-105103
supplies the actual post-cancellation pole orders.  Draft PR #720 L-104519 is
an unweighted, fixed-ladder far-edge statement; it does not survive a
growing polynomial weight formally.

The integrated registry marks the moving-order Vandermonde claim L-92302
`GAP_BLOCKED` / `QUARANTINE`.  It is not used.  Historical finite cardinal
and Hermite identities were treated as reconnaissance only; the checkpoint
rederives its elementary formula and obstruction locally.

## Authentication

    PASS_T105106_PRIMARY_CARDINAL_CONDITIONING
    15/15 normal
    15/15 optimized
    7dc8a3075e983d48032d74e14af2d3fed5611adb9735623e32a9dfa8623ace33

No heavy computation was run.

## Remaining frontier

The exact finite reduction does not estimate Xi cardinal products,
target-to-boundary distance, or the pole-cancelled factors \(M_1F/F'\) and
\(M_2F^2/(F'F'')\).  The complete Xi manifest, weighted edge asymptotics,
cofinal passage, multiplicity defect, strict coherence, RCMV104530, and RH
remain open.
