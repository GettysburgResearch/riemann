# T-105106 — Weighted selector conditioning frontier

Claim ID: T-105106

Status: **PROPOSED EXACT FINITE-WINDOW BOUND; COFINAL ESTIMATES OPEN**

Created: 2026-08-23

Depends on: L-105105; L-105106; R-105106

RH status: **unproved**

## Result

The L-105105 selectors are top-primary cardinal polynomials.  For a complete
actual-pole manifest,

\[
W=\sum_{c\in\mathcal T}
\gamma_c(z-c)^{d_c-1}\frac{M_c(z)}{M_c(c)},
\qquad
\frac WM=\sum_{c\in\mathcal T}
\frac{\gamma_c}{M_c(c)(z-c)}.
\tag{T-105106.1}
\]

This closes the exact finite-window degree and conditioning reduction without
a confluent Vandermonde inverse.  The quantities that control it are exposed
explicitly:

\[
\kappa_c=\prod_{a\ne c}|c-a|^{-d_a},
\qquad
\Lambda=\sum_{c\in\mathcal T}|\gamma_c|\kappa_c.
\tag{T-105106.2}
\]

On a disk-scale \((B,R)\),

\[
\|W\|_\infty\le(B+R)^{D-1}\Lambda,
\tag{T-105106.3}
\]

and on an edge \(E\), with \(G=Mh\),

\[
\left|\frac1{2\pi i}\int_EWh\right|
\le\frac{\operatorname{len}(E)}{2\pi}\|G\|_E
\sum_{c\in\mathcal T}\frac{|\gamma_c|\kappa_c}
{\operatorname{dist}(E,c)}.
\tag{T-105106.4}
\]

The symmetric cluster family proves that the exponent and separation loss
cannot be removed by real coefficients, even parity, greater selector
degree, or another holomorphic exact selector.

## Programme split

The former `JETSELNORM105105` gate now separates into:

    FINCARD105106
      Exact reduced selector, degree, coefficient, and finite-window
      conditioning envelope.  Closed algebraically by L-105106.

    XICARD105106
      Bound D_nu(T), the exact products kappa_nu,c(T), and target-to-boundary
      distances on authenticated cofinal Xi windows.  Open.

The former `JETEDGE105105` gate now separates into:

    FINEDGE105106
      Reduce every weighted edge to the conditioning ledger times the
      pole-cancelled holomorphic factor.  Closed algebraically by L-105106.

    XIGEDGE105106
      Estimate M_1F/F' and M_2F^2/(F'F'') with the required cofinal scale,
      including cancellations and endpoints.  Open.

An approximate-selector programme with controlled leakage is a legitimate
alternative if exact Xi conditioning products are too large; no such theorem
is asserted here.

## Boundary

    top-primary cardinal formula                 PROPOSED EXACT / REVIEW PENDING
    finite degree and coefficient envelope       PROPOSED EXACT / REVIEW PENDING
    pole-cancelled edge reduction                 PROPOSED EXACT / REVIEW PENDING
    separation-free/coalescence-free bound        REFUTED
    parity removes conditioning                   REFUTED
    Xi event manifest                             OPEN
    cofinal Xi barycentric-product estimates      OPEN
    Xi pole-cancelled holomorphic-factor bounds   OPEN
    weighted Xi edge asymptotics                  OPEN
    strict Xi jet-coherence margin                OPEN
    RCMV104530                                    OPEN
    Riemann Hypothesis                            UNPROVED

The quarantined growing-order Vandermonde claim L-92302 is not a dependency.
No RCMV104530 or RH conclusion follows from the finite-window bounds.
