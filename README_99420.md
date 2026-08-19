# T-99420 — Calibration-coboundary closure of the endpoint-nested route

This add-only successor is based on frozen PR #641 at
`19cd3939a54ccea73b055b3952b5dd7ed638c4fb`.

Its single idea is that the finite/continuum, activation-knot, and Volterra
boundary calibration is not an independently accumulated Bellman debt.  It is
the coboundary of one primitive compact calibration potential.

If `E=P+A` is the exact signed equality frame, and the positive endpoint frame
satisfies `P=J+PT`, then

```text
E = J + E T + (A-A T),
E = J(I-T)^(-1) + A.
```

Thus all descendant calibration terms telescope exactly and only the bounded
root calibration remains.  Combined with the endpoint-nested common-parent
construction and the fixed-row Mellin–Landau consumer, this is a proposed
complete unconditional RH proof candidate for hostile independent
reconstruction.

```text
calibration coboundary identity             PROVED EXACT
distributional Volterra potential           PROVED EXACT
descendant calibration cancellation         PROVED EXACT
root fixed-row boundedness                   PROVED ON FROZEN COMPACT INPUTS
negative-child/parity firewalls              RESPECTED
fixed-row pole preservation                  RETAINED / RECONSTRUCTED
accepted proof of RH                         NO
Riemann Hypothesis                           UNPROVED PENDING REVIEW
```
