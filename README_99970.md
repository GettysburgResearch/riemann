# T99970 — UPBF firewall, balanced surface, and atom-free critical descent

This branch is a binding successor to PR #669.

The positive upward priority flux `U_X` cannot satisfy the advertised subpower
surface estimate.  An order-independent shell of prime pairs forces

```text
U_X >> 1/(log X)^3,
```

and its conclusion-facing integral is at least
`sqrt(Y)/(log Y)^3`.

The exact repair restores the discarded even surface and survival term:

```text
native scalar = survival + even surface - odd surface.
```

The corresponding signed coarea is exactly the native reciprocal Euler prefix;
no priority ordering removes that cancellation.

The branch also proves global positivity of every shifted quadratic SHARP
carrier `-1<=c<=3`.  The `c=-1` member vanishes at activation and gives a
quadratic-to-linear descent with no signed activation atoms.  Its remaining
critically weighted downward variation is equivalent to RH.

```text
UPBF67 positive-flux estimate             REFUTED
balanced priority surface                 PROVED EXACT
shifted quadratic family                  PROVED ALL-SCALE
activation-atom ledger                    REMOVED FOR c=-1
atom-free critical negative mass          RH-EQUIVALENT / OPEN
Riemann Hypothesis                        UNPROVEN
```

Replay:

```bash
python3 experiments/X-99970-balanced-surface/verify.py \
  --output /tmp/x99970.json
cmp /tmp/x99970.json \
  experiments/X-99970-balanced-surface/results/verification.json
```

Expected:

```text
PASS_T99970_UPBF_FIREWALL_AND_BALANCED_SURFACE
46a77ea83a85b007bd964d0f2912ddf094506854034e55ca0fbaf374e1420408
```
