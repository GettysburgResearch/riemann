# PR #484 exact-root composition recovery

## Purpose

Recover the unpublished `91840` packet, stack it on the newest compatible
one-shot hardening PR #487, and make every composition interface explicit.

The packet adds five exact composition lemmas and one candidate-complete theorem:

```text
L-91840  restriction before quadrature for partial-cell ownership;
L-91841  first-owner-restricted child operators;
L-91842  complete six-class common-port ledger;
L-91843  fourteen-stage source telescoping and native root identity;
L-91844  direct Y4 accounting with no benchmark bridge;
T-91840  composition with the frozen endpoint consumer.
```

## Relation to PR #487

PR #487 is the controlling implementation. It integrates Hall exactly, uses
whole endpoint cells, keeps every child as an internal colour and invokes no
auxiliary port. The recovered packet proves that these simplifications are
compatible with the more general partial-cell, exported-child and portful
interfaces and records the operation-order firewalls which PR #484 requested.

## Exact root identity

The sequential ledger gives, before any recursive row is inserted,

\[
\Omega_X=\Xi(d_X^{\rm cur})+r_X+
\sum_b\beta_bU_b^{(1)}\Omega(P_b),\qquad r_X\ge0.
\]

In the one-shot specialization the child sum is empty. The complete root cost
is the explicit sum `12012+4+48972+1=60989<61000`.

## Boundary

This is a complete proof proposal on frozen inputs and a durable recovery of the
previously missing work. It is not an accepted proof of RH. Independent review
must reconstruct the analytic Hall map, all-column capacity estimates,
prime-square moat and Mellin--Landau consumer.
