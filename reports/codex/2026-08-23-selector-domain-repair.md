# Selector-domain repair for quotient-edge equalities

Date: 2026-08-23

Checkpoint base: 51c67046a726be188bf724f7b4652e299bd31ccb

## Outcome

The selector-domain hypothesis is now explicit.  An L-105107 extremal has
constant modulus \(\tau\) on the boundary of the exact domain
\(\Omega\) used in its construction.  Therefore the T-105109 quotient
equalities hold on compact rectifiable arcs of that same boundary.

For an arbitrary compact edge, one must use

\[
\|Wh\|_E\le\|W\|_E\|h\|_E.
\]

When \(E\subset\overline\Omega\), maximum modulus yields
\(\|W_*\|_E\le\tau\), which gives a valid upper envelope but generally
not equality.

## Exact firewall

For \(\Omega=\mathbb D\), \(F=e^{z^4/4}\), the first quotient has the
single order-three target at zero and exact optimum \(W_*=z^2\),
\(\tau=1\).  On the radius-\(1/2\) upper semicircle,

\[
m_1=1/8,\qquad \|W_*\|_E=1/4,\qquad
\|W_*F/F'\|_E=2,
\]

whereas the unqualified \(\tau/m_1\) expression is eight.  On the unit
upper semicircle, which lies on the selector-domain boundary, equality is
restored with value one.

## Erratum scope

The literal L/T/M/metadata/report/PR-body wording of packet 105109 is marked
overbroad or ambiguous without the same-domain qualifier.  Frozen artifacts
and historic digests remain unchanged.  This report neither reruns nor
retrospectively verifies X/T-105109.  The actual 105109 unit-circle
obstruction already satisfies the repaired hypothesis and survives.

## Exact authentication

    PASS_T105112_SELECTOR_DOMAIN_REPAIR
    15 focused tests in normal and optimized Python
    3748777ede886502e57c6ad77777807b11b98104a8ecba04b60f162b10e2b19c

No numerical or heavy computation is used.

## Remaining gate

Xi collar and denominator margins, selector/margin absorption,
phase-sensitive cancellation, strict coherence, RCMV104530, and RH remain
open.
