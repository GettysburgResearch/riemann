# Review specification — T-107010

Frozen parent:

```text
PR #759
ebaf1dbcccecd7ed18812e786da40f1d610e497d
```

Mandatory reconstruction:

1. Verify convergence of every Bertrand width row.
2. Verify the total support budget after interleaving all rows.
3. Check local-uniform convergence and right-half-plane zero-freeness.
4. Rebuild the active-factor count for each fixed depth.
5. Verify slow variation in the exterior threshold.
6. Rebuild exact Fourier-series Parseval with the new detector.
7. Check the diagonal depth schedule uses one fixed detector.
8. Reconstruct the compact-support exponential-tail no-go.
9. Check the Cartwright logarithmic-integral boundary.
10. Confirm that `NBV107000` and RH are not marked proved.

Immediate falsifiers:

```text
an X-dependent detector;
a source-dependent choice of depth;
using low rank as arithmetic cancellation;
dropping compact causality in the lower bound;
claiming the diagonal schedule has exactly quadratic rank;
promoting the replay into a proof of RH.
```
