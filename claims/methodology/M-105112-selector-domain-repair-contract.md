# M-105112 — Selector-domain repair contract

Claim ID: M-105112

Status: **HOSTILE REVIEW CONTRACT / ERRATUM**

Created: 2026-08-23

Depends on: L-105107; L-105109; L-105112; R-105112

RH status: **unproved**

## Domain-identity ledger

- Record the exact bounded simply connected Jordan domain \(\Omega\) used
  to construct each optimal selector.
- Use \(|W_*|=\tau\) only on \(\partial\Omega\).  The phrase “boundary arc”
  is insufficient unless the boundary's domain is identified.
- For equality, require the complete edge \(E\subset\partial\Omega\), not
  merely \(E\subset\overline\Omega\) and not merely that \(E\) is a boundary
  arc of some other region.
- If first and second selectors are used, authenticate both on the same
  stated contour domain, even though their manifests and norms can differ.
- Membership in \(A(\Omega)\) supplies values only on \(\overline\Omega\).
  Evaluation outside it requires a separately proved continuation.

## Norm ledger

- On an arbitrary compact edge, start from
  \(\|Wh\|_E\le\|W\|_E\|h\|_E\).
- For the first quotient, \(\|h\|_E=1/m_1(E)\); for the second it is
  \(1/m_{12}(E)\).
- Do not replace \(\|W\|_E\) by \(\tau\) in an equality unless pointwise
  constant modulus on that exact edge has been authenticated.
- For \(E\subset\overline\Omega\), maximum modulus gives
  \(\|W_*\|_E\le\tau\), so \(\tau/m\) is an upper envelope.  Equality can
  fail strictly.
- The product inequality can itself be strict because the two factors can
  attain their maxima at different points.

## Exact-fixture checks

- For \(F=e^{z^4/4}\), verify \(F'/F=z^3\) and
  \(F''/F=z^2(z^4+3)\) by exact polynomial arithmetic.
- Verify the complete first manifest is the single order-three target at
  zero and that its exact unit-disk optimum is \(W_*=z^2\), \(\tau=1\).
- On the radius-\(1/2\) upper semicircle, verify
  \(m_1=1/8\), \(\|W_*\|=1/4\), and the actual weighted norm two.
- The invalid broad value is eight.  Do not hide the factor-four gap behind
  a numerical approximation.
- Verify \(|z^4+3|\ge47/16\) so that the required \(F''\) nonvanishing is
  explicit.
- On the unit upper semicircle, verify the same-domain equality with value
  one.

## Frozen-artifact contract

- Mark the literal L/T/M/metadata/report/PR-body wording of packet 105109 as
  overbroad or ambiguous without the same-domain qualifier.
- Keep the frozen 105109 files and their historic proof-object digest
  unchanged.  This packet is an identified forward repair, not a silent
  rewrite.
- Do not label the 105109 verifier retrospectively repaired or rerun under
  the new claim.  L/T/R/M/X-105112 authenticate this erratum only.
- Preserve the actual T-105109 same-unit-disk obstruction: its relevant
  edges already satisfy the repaired domain hypothesis.

## Scope firewall

- No Xi contour-domain identity, collar, denominator lower margin, or
  selector/margin absorption is supplied.
- No phase-sensitive cancellation, strict coherence, RCMV104530, or RH
  conclusion follows.
