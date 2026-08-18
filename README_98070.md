# T98070 deterministic recovery packet

Collision-safe regeneration of the negative-mass / Euler–Hurwitz / vanishing-hinge
work originally described under the now-colliding `98060` namespace.

## Frozen source

- repository: `gfreund123/riemann`
- source PR: `#608`
- source branch: `agent/recursive-dickman-threshold-closure`
- source head: `f362acf56bbbbd183976b6377fbe883193886e1a`
- source tree: `33387b767da8a6c69d824f5bfee33c864d9cc299`
- publication namespace: `98070`
- reserved publication branch: `agent/98070-negative-mass-euler-hurwitz`

The publication branch was created on GitHub at the frozen source head, but this ZIP
does **not** claim that a successor commit or PR has been published.

## Replay

```bash
bash experiments/X-98070-negative-mass-euler-hurwitz/replay.sh
sha256sum -c T98070_CONTENT_SHA256SUMS
```

The current p=67 scanner was freshly replayed through `10^6`, giving
`Q67=2.55967670964739158` at `Y=536`. The bundled legacy `10^8` JSON is
quarantined because it is incompatible with the current scanner already at
`Y=584`; it is retained only for provenance and supplies no evidence.

RH remains unproved.
