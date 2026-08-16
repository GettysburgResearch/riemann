# T-96300 publication handoff

Apply the add-only packet to exact PR #534 head
`ef18bdda5a65334695008e4c1f5986833160d84f`.

Suggested branch:

```text
research/gpt56-pro/96300-projective-full-row-landau
```

Required pre-publication checks:

```bash
cd experiments/X-96300-projective-full-row
./build_and_replay.sh
cd ../..
sha256sum -c T96300_CONTENT_SHA256SUMS
```

The full 51,118,080-event campaign is already retained in eight disjoint chunks.
It may be rebuilt from `src/directed_tail_mpfr_arith.cpp`; publication does not
require rerunning it when the retained chunk and aggregate hashes pass.
