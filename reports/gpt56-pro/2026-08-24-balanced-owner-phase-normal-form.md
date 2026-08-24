# Balanced owner-phase normal form for the four-owner restriction

## Starting point

The prior PR #719 head reduced the completion-defect programme to a coherent
two-nonzero-phase sum over four-distinct-owner semiprime squareclasses.
Fixed-squareclass core energy was known, but the phase-cardinality losses were
attached to whichever owners happened to be globally largest.

## New normalization

The phase moduli are now selected across the two physical products.

For

\[
N=pq\,a^2,
\qquad
M=rs\,b^2,
\]

owner/core overlaps are first extracted as common shifts. Each extraction
contributes `1/ell` and produces a decreasing distinct-prime renewal of
polylogarithmic total mass.

In the clean sector, a phase modulo an owner on one side is placed on the
opposite physical field. With one selected owner from each side, the two phase
cardinalities cancel the two corresponding owner weights exactly. With all
four owner phases, every explicit owner weight cancels:

\[
|\mathcal C_{P,Q}|
\ll
\left(1+{rs\over A}\right)^{1/2}
\left(1+{pq\over B}\right)^{1/2}.
\]

Thus the doubly long fixed-quadruple packet is `O(1)`, uniformly in all four
owner primes.

## Adaptive selector

No fixed number of phases is best in every dyadic regime. For phase products

\[
L_N\mid rs,
\qquad
L_M\mid pq,
\qquad
L_NL_M>1,
\]

the exact local bound is

\[
|\mathcal C_{P,Q}|
\ll
\left[
{L_NL_M\over pqrs}
\left(1+{L_N\over A}\right)
\left(1+{L_M\over B}\right)
\right]^{1/2}.
\]

There are only fifteen admissible choices. Long cores use more phase
coordinates; short cores retain more owner weight.

## Exact remaining theorem

```text
BQSP102870:
  after carrier/source/gauge/shared-owner/owner-core renewal, the coherent
  optimally normalized balanced-phase sum over clean four-owner semiprime
  squareclasses has subpower logarithmic negative mass.
```

The remaining obstruction is no longer:

```text
zero-frequency removal;
modulus cardinality;
fixed-squareclass core energy;
owner/core overlap;
shared-owner renewal;
fixed-pair long/short normalization.
```

It is exclusively coherent arithmetic summation across different clean
semiprime squareclasses. A source-blind collection of individually bounded
packets can add coherently, so the last step must use literal owner signs,
large-sieve orthogonality, or a source-faithful discrepancy transport.

```text
BQSP102870   OPEN / RH-BEARING
RH            UNPROVED
```
