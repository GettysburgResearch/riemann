# T-105115 - Common safe-rectangle transfer frontier

Claim ID: T-105115

Status: **PROPOSED EXACT FINITE TRANSFER; XI COFINAL INPUT OPEN**

Created: 2026-08-23

Depends on: L-105115; L-105114; L-105113; L-105112

RH status: **unproved**

## Result

If \(|B_T|<\Delta_T\) and \(|B_\eta|<\Delta_\eta\), L-105115 turns a
finite family of closed positive-radius bad disks into an explicit
positive-measure Cartesian family of common safe symmetric rectangles.  In
particular, the strict radius-only gate

\[
\Delta_T>2S,\qquad\Delta_\eta>2S
\]

is worst-case sharp using only the total disk radius \(S\).  Restricting one
prescribed nonnegative \(q\in L^1(I_T\times I_\eta)\) to the safe product
selects a common rectangle with exact parameter-normalization factor

\[
\kappa=\frac{\Delta_T\Delta_\eta}
{(\Delta_T-|B_T|)(\Delta_\eta-|B_\eta|)}.
\]

On that rectangle, direct raw quotient bounds use only lower bounds for
\(F'\) and \(F''\), permit zeros of \(F\), and retain the L-105112
selector-domain distinction.  Comparison to the unrestricted shell mean
requires a globally integrable prescribed cost; raw singularities inside
bad disks do not satisfy that premise automatically.

## Programme split

    PROJECTION105115
      Exact merged coordinate bad sets and safe-product measure.
      Closed finitely by L-105115.

    RADIUS105115
      Sharp strict 2S radius-only relaxation.
      Closed finitely by L-105115 and R-105115.

    TONELLI105115
      One common safe rectangle for a prescribed aggregate cost.
      Closed for a fixed finite integrable shell by L-105115.

    RAW105115
      Direct F/F' and F^2/(F'F'') envelopes allow zeros of F.
      Closed conditionally on the stated upper/lower moduli.

    SELECTOR105115
      Inferring outer-selector equality on an intermediate boundary.
      Invalid in general by the L-105112 domain firewall.

    XISHELL105115
      Authenticate a cofinal Xi shell satisfying the strict radius gate.
      Open.

    XIABSORB105115
      Absorb reciprocal, projection, length, and actual selector costs.
      Open.

## Boundary

    finite supporting-line safe product              PROPOSED EXACT / REVIEW PENDING
    exact restricted-Tonelli normalization           PROPOSED EXACT / REVIEW PENDING
    strict 2S radius-only gate                        PROPOSED SHARP / REVIEW PENDING
    raw quotient edge envelopes                      CONDITIONAL EXACT
    all safe rectangles characterized                NOT CLAIMED
    cofinal Xi disk and growth certificate           OPEN
    complete actual Xi pole manifests                OPEN
    selector and reciprocal absorption               OPEN
    strict Xi jet coherence                          OPEN
    RCMV104530                                        OPEN
    Riemann Hypothesis                               UNPROVED

No Xi evaluation, root scan, contour quadrature, cofinal passage, or RH
conclusion is part of this finite theorem.
