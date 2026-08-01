# Integration handoff — X-18509 complete finite deficit projector

At X-18507 support `(c,N)=(10,2)`, use the exact finite lower model

```text
A = gG-D,
g=1/4,
D>0,
Gamma=1/1000.
```

The old source flag is not invariant under `D` and therefore is not the
canonical high-deficit range. Replace it by

```text
P_D = 1_(249/1000,infinity)(G^-1/2 D G^-1/2).
```

The committed certificate supplies a rational center and `G`-operator radius
`1e-52`. The exact packet and complement reduce `A`, so the PR #191 direct short
has zero cross and zero residual. The canonical floor is at least
`1/200000000`; the safe complement floor is at least `17/100`.

For a future growing emitter, repeat this schema rather than assuming source
and deficit flags coincide. The production object should retain the exact
projector definition, a rational center/radius, and direct-short floors on both
spectral blocks.
