# Result report — wide curvature nomination and rigorous escalation

Agent ID: `gpt56-02-f`  
Issue: #39  
Branch: `agent/gpt56-02-f/39-arb-matched-pole-scan`  
Date: 2026-07-23  
Status: complete finite discovery/escalation batch; no counterexample found

## Discovery coverage

A deterministic base-2 van-der-Corput sequence placed 96 exact decimal window
centers throughout

```text
3,000,000,000,000 < T < 5,000,000,000,001.
```

Each window used the provenance-corrected X-3901 moment-FFT curvature transform
with

```text
spacing                0.01
samples per window     65,536
Taylor order           18
```

for a total of

```text
6,291,456 no-remainder curvature samples.
```

Every sample and every window minimum was positive. This discovery layer remains
EMPIRICAL because it does not enclose the final Riemann-Siegel quotient
remainder.

## Rigorous escalation

The eight lowest positive minima were serialized as exact rational ordinates and
passed to the Python-FLINT/Arb producer.

At each nominee the scan evaluated 19 horizontal nodes, seven model positions
per adjacent gap, and exact L-3904 vectors of dimensions two through seven.

```text
primitive Arb points per precision     152
complete Pick channels per precision  6,048
```

Results:

```text
160 bits:
  CERTIFIED_NONNEGATIVE                6,048
  CERTIFIED_NEGATIVE                       0
  UNRESOLVED_ZERO_TOUCH                    0

224 bits:
  CERTIFIED_NONNEGATIVE                6,048
  CERTIFIED_NEGATIVE                       0
  UNRESOLVED_ZERO_TOUCH                    0
```

Every 224-bit interval is contained in its corresponding 160-bit interval.
The batch therefore contributes 12,096 rigorous complete-interval
classifications with no negative and no conditioning failure.

## Interpretation

The discovery screen did not nominate an empirical negative, and the strongest
positive minima did not reveal a hidden L-3904 violation after rigorous
evaluation. This closes the declared 96-window batch only. It is not a
positivity theorem for other ordinates or vector families.

The compact frozen result is

`experiments/X-3902-arb-xi-passivity/results/curvature-nominee-result.json`.

Full window, certificate, verification, and summary files are retained as
GitHub Actions artifacts.

## Candidate status

None. No `Z-####` identifier is allocated.

## Next offense

The next computation should not repeat the same curvature filter at nearby
centers. The highest-value independent route is now the carrier finalist:
recover the exact PR #44 `c=10^11`, `K=1024` vector and perform a directed
complete-prime fixed-vector accumulation against PR #51's exact nonprime
correction moat.
