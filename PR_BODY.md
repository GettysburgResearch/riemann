## Research hardening

This is the completed add-only successor to PR #542.

It accepts an exact proof-scope failure in the imported `L-94200`: the fixed-product cube at `(j,P,n)=(3,6,24)` leaves coefficient `-1` at one knot, so the old local convex-packet proof is invalid. The positivity statement is not refuted.

The replacement is the globally owned cross-product `GLOBAL-FRONTIER-SHADOW` transport:

```text
global knot measure and rough reservoir
 -> first-crossing owners
 -> edge / shoulder / complete-block / partial-block stores
 -> monotone pairs and log-barycentric butterflies
 -> initial-prime sieve positivity
 -> full Mobius row positivity
 -> direct reciprocal-zeta Mellin transform
 -> Landau
 -> RH candidate.
```

```text
base PR #542: ca5fb69c15cda29b3b589660f9be44ea2f440677
```

The direct Mellin-Landau finish is retained. No native endpoint benchmark, factor-67 route, Target-Lorenz theorem, CPBD estimate, Mertens square-root bound, or power-saving PNT error is used.

Retained diagnostic:

```text
PASS_GLOBAL_FRONTIER_SHADOW_HARDENING_DIAGNOSTICS
global_transport_proved_by_replay=false
rh_established_by_replay=false
```

Scientific status:

```text
complete unconditional proof candidate: yes, on the written global transport
accepted proof: no
Riemann Hypothesis: unproved pending hostile reconstruction
```
