# X-96500 - parity-covariant gluing and fixed-depth no-go replay

This experiment has two proof-grade backends:

1. Python exact integer and rational interval arithmetic for the parity cocycle,
   activation identities, the 239-atom odd-history Target-Lorenz obstruction,
   the depth-two source partition, and the rows-2/3 noncancellation algebra.
2. A direct 256-bit MPFR interval program for the complete depth-two current
   block at X=200000.

Replay:

```bash
./build_and_replay.sh
```

Expected verdict:

```text
PASS_X_96500_PARITY_COVARIANT_GLUE_AUDIT
918b3ccfb7f99d764e01302ffc2f358fda0e3e2ccfc27eeb038799cf0ee05293
E_T(71,13)-O_T(71,13)>17
```

The MPFR subcertificate must report:

```text
PASS_MPFR_DIRECTED_TWO_LEVEL_STAR_NEGATIVITY
A_2(200000)<-11 and A_3(200000)<-2
```

Scope:

```text
parity-blind PR #550 gluing argument       refuted
fixed-depth local positive reset           refuted
full-row/two-row nonnegativity             not refuted
GPHT23 global producer                     open
Riemann Hypothesis                         unproved
```
