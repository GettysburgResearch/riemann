## Purpose

Continue PR #590 at exact head `223f11259b3e7134f78d6492795e6e94caca8be3`,
incorporate the live Lorenz-Bellman comparison in PR #591, and sharpen the
post-LAPBR frontier without claiming RH.

## New results

1. General subcritical-depth no-go: every even natural rough current with
   `L log(2L)=o(sum 1/p)` is eventually negative.  This rules out an entire
   class of shallow count-depth repairs, not only PR #578's chosen depth.
2. Exact root-only Bellman target: PR #590's scalar identity makes
   `RBLPTE67` equivalent to eventual root scalar positivity.
3. Exact zero-hinge map: the root scalar is `D^+(0)` in the completed Lorenz
   dual.  Thus `CPSL67` implies the scalar theorem, but is strictly stronger in
   general.

## Replay

```bash
python3 experiments/X-97810-subcritical-depth/verify.py
```

Expected:

```text
PASS_T97810_SUBCRITICAL_DEPTH_AND_ZERO_HINGE
```

## Boundary

```text
RBLPTE67                 OPEN / RH-BEARING
Riemann Hypothesis       UNPROVEN
```
