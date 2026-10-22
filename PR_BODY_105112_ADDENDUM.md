## Checkpoint 13 — selector-domain equality repair

Exact checkpoint base:
51c67046a726be188bf724f7b4652e299bd31ccb.

The literal L/T/M/metadata/report/PR-body wording of packet 105109 is now
marked overbroad or ambiguous unless its boundary arc is understood to lie
on the boundary of the exact selector domain.  This is a separately
identified forward repair: no frozen 105109 or 105111 artifact is changed,
and no retrospective 105109 verification is claimed.

For \(E\subset\partial\Omega\), constant boundary modulus gives the exact
first and second quotient equalities.  For arbitrary \(E\), only the product
inequality using \(\|W\|_E\) is automatic; if
\(E\subset\overline\Omega\), maximum modulus gives a \(\tau/m\) upper
envelope.

The exact unit-disk fixture \(F=e^{z^4/4}\), \(W_*=z^2\) has
\(\tau=1\).  On the radius-\(1/2\) upper semicircle the domain-free formula
predicts eight, while the exact weighted norm is two.  On the unit upper
semicircle the repaired equality is exact with value one.

Exact replay:

    PASS_T105112_SELECTOR_DOMAIN_REPAIR
    15 focused tests in normal and optimized Python
    digest 3748777ede886502e57c6ad77777807b11b98104a8ecba04b60f162b10e2b19c

The same-unit-disk T-105109 obstruction survives.  No Xi margin, cofinal
passage, RCMV104530, or RH conclusion is claimed.
