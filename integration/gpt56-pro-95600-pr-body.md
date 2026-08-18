## Purpose

Continue PR #595 and decide whether another finite Q4 filter or moment
compression can weaken its one-sided subpower gate.

**RH remains unproved.**

## Freeze

```text
base PR:      #595
base SHA:     e66a91166b80cbf0a520e3a78ea96582d263d563
head branch:  research/gpt56-pro/95600-uosacf-equivalence-filter-exhaustion
publication:  one add-only successor commit
```

## Main results

1. `L-95600`: UOSACF is equivalent to RH, not merely sufficient.
2. `L-95601`: every subpower-invertible scale filter preserves the criterion.
3. `L-95602`: the Vinogradov–Korobov Mertens bound transfers to the exact
   ten-band packet.
4. `R-95600`: finite inner moments, diagonal data and source-blind PSD
   arguments cannot prove UOSACF.
5. `L-95603`: the finite odd-core source is stably equivalent to the compact
   Q4 current plus an explicit lower-order delayed gauge.
6. `O-95600`: floating cross-sign reconnaissance through five million
   endpoints; nonprobative.

## Replay

```bash
python3 experiments/X-95600-filter-invariance/verify.py \
  --output /tmp/x95600.json
cmp /tmp/x95600.json \
  experiments/X-95600-filter-invariance/results/verification.json
sha256sum -c T95600_CONTENT_SHA256SUMS
```

Expected:

```text
PASS_X_95600_Q4_SUBPOWER_EQUIVALENCE_AND_FILTER_EXHAUSTION
```

## Exact boundary

```text
UOSACF / annular subpower             RH-EQUIVALENT
finite-filter weakening               EXHAUSTED
classical unconditional scale         X^(1-o(1))
nonlocal compact-current estimate      OPEN / RH-EQUIVALENT
Riemann Hypothesis                     UNPROVEN
```
