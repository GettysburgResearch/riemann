## T105415 addendum — fixed-width moving-saddle endpoint

`M-105331` identified one missing load-bearing inequality: global dominance of the exact moving saddle over the rest of the translated contour.

The new proof uses the correct ray

```text
delta_(m,z)+[0,infinity),
delta_(m,z)=u_(m,z)-w_m.
```

On its large part, first-orbit dominance of the explicit Xi kernel gives

```text
Re S_m''(t+delta)
 <= -c[m/t^2+exp(2t)] < 0.
```

The exact saddle is therefore the unique global maximum of the real action on the shifted ray. The compact initial segment loses `c m log w_m`, the local complement loses a growing Gaussian amount, and the origin/infinity connectors are exponentially negligible.

This yields a proposed complete relative asymptotic in the fixed physical strip

```text
|Re z| <= c M/log M,
|Im z| <= H,
m >= M.
```

The exact reflected phase then gives a proposed complete proof that all high Xi derivatives are real-rooted and simple in the common box, with negative critical residues, once

```text
m >= K_H T log(2+T).
```

Scientific status:

```text
global shifted-ray dominance             PROPOSED COMPLETE / REVIEW REQUIRED
fixed-width relative saddle asymptotic    PROPOSED COMPLETE / REVIEW REQUIRED
O(T log T) terminal derivative            PROPOSED COMPLETE / REVIEW REQUIRED
low-order descent                         OPEN / RH-BEARING
RH                                        UNPROVEN
```

No finite computation certifies the contour theorem. `M-105415` specifies the hostile review order.
