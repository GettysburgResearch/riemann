## Checkpoint J — companion partial index and norm/rank firewall (T-105550)

The final `MATRIXLERC105541` field now has a topological normal form.  After
common-factor cancellation, `E_delta=F'+i delta F` has no real zero, and its
upper/lower half-plane zero counts satisfy

```text
N_plus+N_minus = distinct zero count of F;
N_plus-N_minus = distinct real zero count of F.
```

Equivalently the companion Cayley ratio has winding equal to the real-root
count.  The finite Blaschke quotient has

```text
rank H_u = N_minus,
rank H_conj(u) = N_plus,
deg u = ||H_conj(u)||_HS^2-||H_u||_HS^2.
```

A separated model-space theorem converts Hankel energy into a count only after
paying the denominator-kernel condition number and the cross-factor value
floor.  A rank-one Blaschke dipole with norm tending to zero proves that no
source-blind Schatten estimate can replace that payment.

This removes the arbitrary vertical/collar bookkeeping from the conceptual
frontier, but it does not prove the required Xi partial-index estimate.

```text
companion half-plane count                  PROVED EXACT
Cayley winding / Toeplitz index             PROVED EXACT
separated Blaschke rank-energy bridge       PROVED EXACT
norm-only companion counting                REFUTED EXACT
COMPSEP105550 / direct winding estimate     OPEN / RECORD-BEARING
90 percent / public record / RH             UNPROVED
```
