# T-105112 — Repaired quotient-edge frontier

Claim ID: T-105112

Status: **PROPOSED EXACT FORWARD REPAIR; XI CONTROL OPEN**

Created: 2026-08-23

Depends on: T-105109; T-105111; L-105112; R-105112

RH status: **unproved**

## Result

The constant-boundary-modulus quotient equalities are exact only after the
selector domain is carried into the statement.  Let \(\Omega\) be the exact
bounded simply connected Jordan domain used to construct \(W_{j,*}\), and
let \(E\subset\partial\Omega\) be a compact rectifiable arc.  If \(F\) is
holomorphic near \(E\) and \(F,F',F''\) are nonzero there, then

\[
\boxed{
\left\|W_{1,*}\frac F{F'}\right\|_E
=\frac{\tau_1}{m_1(E)},
\qquad
\left\|W_{2,*}\frac{F^2}{F'F''}\right\|_E
=\frac{\tau_2}{m_{12}(E)}.
}
\tag{T-105112.1}
\]

For an arbitrary compact edge on which the objects are defined, the valid
general statement is

\[
\left\|W_1\frac F{F'}\right\|_E
\le\frac{\|W_1\|_E}{m_1(E)},
\qquad
\left\|W_2\frac{F^2}{F'F''}\right\|_E
\le\frac{\|W_2\|_E}{m_{12}(E)}.
\tag{T-105112.2}
\]

If \(E\subset\overline\Omega\) and the weights are the optimal selectors on
\(\Omega\), maximum modulus further gives the upper envelopes
\(\tau_1/m_1\) and \(\tau_2/m_{12}\), but not equality in general.

R-105112 makes the distinction exact.  For
\(F=e^{z^4/4}\) and the unit-disk optimum \(W_*=z^2\), the radius-\(1/2\)
upper semicircle has \(m_1=1/8\).  The broad literal formula gives eight,
whereas the exact weighted norm is two.  On the unit upper semicircle, which
is part of the selector-domain boundary, equality is restored and both
sides are one.

The frozen L/T/M/metadata/report/PR-body wording of the T-105109 packet is
therefore marked overbroad or ambiguous under a literal domain-free reading.
This separately identified packet supplies the intended same-domain reading;
it does not alter frozen files, historic digests, or retrospectively verify
T-105109.

## Programme split

    SAMEDOM105112
      Exact constant-modulus equalities on the boundary of the domain used
      to construct the selector.  Closed finitely by L-105112.

    GENERALEDGE105112
      Product inequality using the actual edge norm of the weight; tau upper
      envelope on compact subsets of the selector-domain closure.  Closed.

    OFFBOUNDARY105112
      Scalar selector norm tau gives equality on every other boundary or
      interior arc.  Refuted exactly by R-105112.

    HISTORIC105112
      Rewrite or retrospectively reverify the frozen T-105109 packet.
      Deliberately not performed.

    XICOLLAR105112
      Authenticate Xi denominator margins on changing selector-domain
      boundary arcs.  Open.

    XICOFINAL105112
      Absorb selector cost, edge length, corrections, multiplicity defect,
      and strict coherence.  Open.

## Boundary

    same-domain weighted-sup equalities              PROPOSED EXACT / REVIEW PENDING
    arbitrary-edge actual-weight-norm inequality     PROPOSED EXACT / REVIEW PENDING
    tau equality on every other arc                  REFUTED
    retrospective T-105109 verification              NOT CLAIMED
    Xi boundary margin and collar                     OPEN
    cofinal selector/margin absorption                OPEN
    phase-sensitive cancellation                      OPEN
    strict Xi jet coherence                           OPEN
    RCMV104530                                        OPEN
    Riemann Hypothesis                                UNPROVED

The T-105109 same-unit-disk exterior-critical obstruction survives the
repair.  No Xi estimate, RCMV104530, or RH conclusion follows.
