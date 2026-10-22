# T-105102 — Boundary-coherence frontier

Claim ID: T-105102

Status: **PROPOSED EXACT TWO-MOMENT REDUCTION; QUANTITATIVE INPUT OPEN**

Created: 2026-08-23

Depends on: L-105101; L-105102; PR #720 only as exact-head, post-freeze
research context

RH status: **unproved**

## Result

L-105102 converts both critical-residue moments at one regular finite window
into explicit boundary charges and correction ledgers:

\[
\mathcal M_{1,F}=-\Phi_{1,F}+C_{1,F},
\qquad
\mathcal M_{2,F}=B_F-C_{2,F}-D_{2,F}.
\tag{T-105102.1}
\]

Consequently, when \(R_F\mathcal M_{2,F}>0\) and \(\delta>0\), the full
residue-coherence gate is the single exact boundary inequality

\[
\bigl(-\Phi_{1,F}+C_{1,F}\bigr)_+^2
>
\left(\frac12+\delta\right)
R_F\bigl(B_F-C_{2,F}-D_{2,F}\bigr).
\tag{T-105102.2}
\]

This identifies five analytic quantities rather than proving favorable
estimates for them. It is the transfer-safe positive-part gate. The literal
square in the draft RCMV104530 display is equivalent only after the signed
carrier is known to be positive.

## Two continuation geometries

At each fixed regular \(T\), a sufficiently thin strip eliminates both
nonreal critical-point corrections exactly:

\[
C_{1,F}=C_{2,F}=0.
\]

The coherence quotient then contains only \(\Phi_{1,F},B_F,D_{2,F}\), but
the boundary estimates must remain valid along the potentially shrinking
\(\eta(T)\). A fixed-thickness route avoids that degeneration but must instead
control \(C_{1,F}\) and \(C_{2,F}\). Neither route is completed here.

## Correct continuation gates

    XIWIN105102
      Establish or bifurcate the simple-zero and common-zero hypotheses along
      the intended cofinal Xi windows, and verify endpoint nonvanishing for
      the L-104522 transfer interval.

    F1FLUX105102
      Obtain the signed first boundary charge Phi_1,k along an admissible
      height/strip sequence.

    FCOR105102
      Control the nonreal first-residue correction C_1,k at the R_k scale.

    BFLUX105102
      Control the second boundary charge B_k at the R_k scale.

    SCOR105102
      Control the nonreal algebraic squared-residue correction C_2,k.

    DDEBT105102
      Control the adjacent-derivative debt D_2,k.

The estimates must combine with a strict margin in (T-105102.2). Separate
upper bounds with no signed carrier margin are insufficient.

## Boundary

    first finite-window residue split          PROPOSED EXACT / REVIEW PENDING
    paired coherence quotient                  PROPOSED EXACT / REVIEW PENDING
    nonreal first-correction firewall          PROPOSED EXACT / REVIEW PENDING
    XIWIN105102                                 OPEN
    F1FLUX105102                                OPEN
    FCOR105102                                 OPEN
    BFLUX105102                                 OPEN
    SCOR105102                                 OPEN
    DDEBT105102                                OPEN
    RCMV104530                                 OPEN
    Riemann Hypothesis                         UNPROVED
