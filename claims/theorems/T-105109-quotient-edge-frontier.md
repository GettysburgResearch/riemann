# T-105109 — Quotient-edge frontier

Claim ID: T-105109

Status: **PROPOSED EXACT FINITE-WINDOW LEDGER; COFINAL CONTROL OPEN**

Created: 2026-08-23

Depends on: L-105106; R-105106; L-105107; L-105109; R-105109

RH status: **unproved**

## Result

The boundary side of the jet-observable bridge now has an exact denominator
ledger.  With

\[
\mathscr L=F'/F,
\qquad
\mathscr A=\mathscr L^2+\mathscr L'=F''/F,
\tag{T-105109.1}
\]

the first and second carriers are \(1/\mathscr L\) and
\(1/(\mathscr L\mathscr A)\).  If \(m_1\) and \(m_{12}\) are their
positive boundary denominator margins, the boundary-optimal selectors obey

\[
\boxed{
\|W_{1,*}F/F'\|_E=\tau_1/m_1(E),
\qquad
\|W_{2,*}F^2/(F'F'')\|_E=\tau_2/m_{12}(E).
}
\tag{T-105109.2}
\]

The equality, rather than merely an upper bound, comes from the constant
boundary modulus of the optimal selectors.

L-105109 proves two independence results.  First, zero-free exponential
gauges preserve arbitrary finite interior zero/jet data while collapsing a
chosen boundary denominator.  Second, the explicit real-even zero-free
family

\[
F_s(z)=\exp(z^2/2-z^4/(4s))
\tag{T-105109.3}
\]

has fixed target coefficients, stable interior event topology, and bounded
optimal selector norms, while both optimally weighted boundary supremum
envelopes diverge as exterior critical points approach the contour.

The full weighted contour integrals remain fixed at one.  Therefore the
result isolates an absolute-edge obstruction and leaves phase-sensitive
oriented-edge cancellation open.

## Programme split

    LOGMARGIN105109
      Exact logarithmic-derivative denominator identities and weighted
      boundary margins.  Closed finitely by L-105109.

    JETGAUGE105109
      Finite interior zeros/jets do not certify either boundary margin.
      Closed by the finite-jet exponential gauge in L-105109.

    EXTCOLLAR105109
      Stable-manifest, bounded-selector exterior-critical counterfamily.
      Closed finitely by L/R-105109.

    XICOLLAR105109
      Authenticate a cofinal Xi collar and lower bounds for both boundary
      denominators.  Open.

    XICANCEL105109
      Alternatively prove phase-sensitive oriented-edge cancellation strong
      enough to bypass the absolute envelope.  Open.

    XICOFINAL105109
      Combine quotient control with Green–Gram selector costs, correction
      terms, multiplicity defect, and strict jet coherence.  Open.

## Boundary

    logarithmic quotient-margin ledger             PROPOSED EXACT / REVIEW PENDING
    constant-modulus weighted-sup equality          PROPOSED EXACT / REVIEW PENDING
    finite jets determine boundary margins          REFUTED
    bounded selector norms control absolute edges   REFUTED
    interior manifest supplies exterior collar      REFUTED
    Xi exterior-collar/lower-margin estimate        OPEN
    Xi oriented-edge cancellation estimate         OPEN
    cofinal strict jet coherence                    OPEN
    RCMV104530                                      OPEN
    Riemann Hypothesis                              UNPROVED

No divergence of an oriented contour integral is claimed.  No RCMV104530
or RH conclusion follows.
