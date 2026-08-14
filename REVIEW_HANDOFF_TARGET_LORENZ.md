# Review handoff — Target-Lorenz vector primal/dual continuation

## Intended placement

```text
repository:    gfreund123/riemann
existing PR:   #468
branch:        research/gpt56-pro/91381-euler-shell-recovery
parent head:   a41f81466f85d52597c97b41505756a8860698d0
stacked base:  d5e03a3a63bd05b43abf4b5e37905f86e9ec59d6
```

Apply the accompanying mail patch on the existing PR branch. Recheck the live
head and claim IDs before application; later corrections control.

## Commit plan

```text
1. prove exact common-source Target-Lorenz vector primal/dual;
2. fence the false one-scalar cutoff reduction and record correct cells;
3. compose the explicit AVLT/ANRL native-root proposal;
4. add exact replay, discovery-only reconnaissance, report, audit and lock.
```

## Replay

```bash
cd experiments/X-91685-target-lorenz-vector-primal-dual
python3 verify.py
python3 recon.py
sha256sum -c SHA256SUMS
python3 -m py_compile verify.py recon.py
```

Expected:

```text
PASS_TARGET_LORENZ_VECTOR_PRIMAL_DUAL
PASS_TARGET_LORENZ_STRUCTURED_RECONNAISSANCE
```

The first verdict is an exact finite-algebra replay. The second is explicitly
nonrigorous reconnaissance for the infinite arithmetic sign family.

## Scientific boundary

```text
common-source vector optimization and separation    PROVED EXACT
target cutoff one-scalar collapse                    REFUTED EXACT
correct activation-cell parameterization             PROVED EXACT
AVLT arithmetic margin theorem                       OPEN
ANRL live atomwise root allocation                   OPEN
full implication after AVLT + ANRL                   CONDITIONAL
Riemann Hypothesis                                   UNPROVEN
```
