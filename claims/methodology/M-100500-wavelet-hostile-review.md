# M-100500 — Hostile review protocol for the minimal-wavelet route

1. Recompute all three formulas for \(K_0\).
2. Check \(K_0(1)=K_0(8)=0\) and continuity at \(2,4\).
3. Perform Abel summation with both endpoint terms present before cancelling.
4. Verify every coefficient in \(V(y)\).
5. Rebuild the Mellin multiplier and its zero lines.
6. Keep the half-order inverse factor \(2^{j/2}\); do not replace it by a
   polynomial-cost inverse.
7. Reject any diagonal or free-labelled estimate promoted to physical
   cancellation.
8. Treat `MWOC100500` and RH as open.

Immediate falsifiers:

```text
a nonzero Abel endpoint;
a missing activation-band derivative;
a multiplier zero in the translated open strip;
a sub-square-root source-blind inverse;
MWOC or RH marked proved by the replay.
```
