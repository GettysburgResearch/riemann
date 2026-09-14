## T-106660 — optimized cross-trace and rational resolvent gates

A hostile readback found one stale promotion in `L-106611`: the denominator
phase mean is a majorant of the canonical all-pass charge, not an equality.
The file is corrected in place.

Two exact scalar continuations are now proved.

```text
canonical shallow charge
  <= m_- - |Delta|
   = min_theta (1/4pi) int beta_-' |1-e^(i theta)U|^2

canonical shallow charge
  <= (1+tau) tr[D* G D (G+tau D* G D)^(-1)].
```

The first optimizes the harmless constant all-pass phase and is exact for one
principal channel. The second is a square-root-free rational certificate with
the exact positive gap

```text
tau tr[K(I-K)(I+tau K)^(-1)].
```

For the carrier-free mesoscopic Riemann--Siegel packets, either scalar total
below `11/500 N`, plus the already-paid regularization ledger, implies more
than 90% after the `3/40 N` deep charge.

Replay:

```text
PASS_T106660_PHASE_OPTIMIZED_RESOLVENT_GATE
exact checks: 70
```

The required Xi scalar estimate remains open. Ninety percent, density one, and
RH remain unproved.
