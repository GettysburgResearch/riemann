# T-93851 proposed heat-resolvent handoff

```text
base PR:       #498
base head:     6cc0da2fa5711017e260ebdcea4ba8c22e453288
status:        PROPOSED
RH:            UNPROVEN
```

## Exact new bridge

\[
\mathcal A_\circ(N)=-2\int_0^\infty\sum_ph_{p,N}(t)dt,
\]

\[
|\mathcal A_\circ(N)|^2
\le4\int_0^\infty e^t|\sum_ph_{p,N}(t)|^2dt,
\]

and the same-prime heat diagonal is at most

\[
8960N\log(2N).
\]

## Open producer

Prove

\[
\left|\sum_{p<r}\int_0^\infty e^th_{p,N}(t)h_{r,N}(t)dt\right|
\ll N\log^B N.
\]

This implies CPBD and hence RH through the reviewed cubic Mellin criterion. No
such estimate is claimed in this packet.
