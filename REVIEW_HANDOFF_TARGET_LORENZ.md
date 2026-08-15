# Review handoff — Target-Lorenz publication repair and compact AVLT

## Frozen parent

```text
repository:  gfreund123/riemann
PR:          #468
branch:      research/gpt56-pro/91381-euler-shell-recovery
parent:      8085903e190589e3117a0c7494fb1150c2222401
```

The reviewer was correct: the parent contains `L-91720--L-91722` and `T-91720`, not the previously summarized complete `L-91696/T-91697` chain. `R-91780` records the correction.

## New durable result

```text
L-91780  exact proportional determinant reduction;
L-91781  complete real compact sign for py<166000;
L-91782  exact P61 tail prefix reserve >7/4;
L-91783  common-source all-coordinate Fubini theorem;
L-91784  native Y4-slack subcritical consumer;
T-91740  corrected conditional composition.
```

## Replay

```bash
cd experiments/X-91780-target-lorenz-compact-avlt
python3 verify.py
```

Expected:

```text
PASS_TARGET_LORENZ_COMPACT_PROPORTIONAL_AVLT
RH_UNPROVEN
```

The large activation-cell census is retained in the result object. The ordinary verifier checks its dimensions, margins, primitive-error audit, the four correlated-cell repairs, and independently replays the exact tail-prefix reserve.

## Exact boundary

```text
compact AVLT py<166000                 PROVED
Tail-AVLT py>=166000                   OPEN
formal source-Fubini                   PROVED
live source/channel allocation         OPEN
native slack recurrence                PROVED CONDITIONAL
Riemann Hypothesis                     UNPROVEN
```
