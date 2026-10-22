# T-105105 — CRT jet-observable frontier

Claim ID: T-105105

Status: **PROPOSED EXACT FIXED-WINDOW BRIDGE; ANALYTIC ESTIMATES OPEN**

Created: 2026-08-23

Depends on: L-105103; L-105104; L-105105

RH status: **unproved**

## Result

The local-jet/global-observable existence gap from T-105104 is closed on a
fixed regular window once its exact denominator-event manifest is supplied.
Finite confluent CRT selectors turn the leading odd-order jet coefficients
into simple residues while annihilating every nontarget actual pole:

\[
\frac1{2\pi i}\int_{\partial\Omega}W_1\frac F{F'}
=\sum_{\mathcal T}\rho_c^{\rm jet},
\qquad
\frac1{2\pi i}\int_{\partial\Omega}W_2\frac{F^2}{F'F''}
=\sum_{\mathcal T}(\rho_c^{\rm jet})^2.
\tag{T-105105.1}
\]

This removes both kinds of algebraic contamination at the identity level:
nonreal or ineligible \(F'\)-events and \(F''\)-only adjacent poles are
assigned zero congruences. Multiple target poles are converted with the
exact powers \(r-1\), \(2r-2\), and the load-bearing factor \(r\).

For polynomials, square-free multiplicity decomposition plus ordinary CRT
also constructs root-free all-odd-stratum carrier polynomials \(R,H\). That
corollary is an all-root trace encoder, not a rational projector onto an
arbitrary real interval.

## Remaining continuation gates

    XIJETMAN105105
      Produce and authenticate the complete Xi denominator-event manifest on
      cofinal regular windows.

    JETSELNORM105105
      Bound selector degree, coefficients, and boundary norm strongly enough
      for the weighted edge integrals.

    JETEDGE105105
      Estimate the four weighted edges, including endpoint and parity errors.

    MULTDEF105105
      Control the multiplicity defect retained by T-105104.

    XITRANS105105
      Combine the selector moments with the jet-coherence transfer and total
      zero-count ratios without changing support or multiplicity conventions.

## Boundary

    fixed-window selector existence               PROPOSED EXACT / REVIEW PENDING
    nontarget pole annihilation                    PROPOSED EXACT / REVIEW PENDING
    root-free polynomial all-stratum encoder       PROPOSED EXACT / REVIEW PENDING
    Xi event manifest                              OPEN
    selector norm / weighted edge estimates        OPEN
    cofinal-window passage                          OPEN
    strict Xi jet-coherence margin                  OPEN
    RCMV104530                                      OPEN
    Riemann Hypothesis                              UNPROVED
