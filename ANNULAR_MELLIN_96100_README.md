# ANNULAR_MELLIN_96100

## Freeze

```text
base PR #535:  988e9bfa55e7ed13c0ddbcab2f6138a83fd4f743
compared #541: e381f444191e214cc992208b16d30a8d5fd461ac
compared #542: ca5fb69c15cda29b3b589660f9be44ea2f440677
```

## Hardened result

The old annular endpoint consumer is withdrawn because the radix-four dual pairs the native target with `P_Lambda`, not `J_Lambda`. The replacement is a direct fixed-annular-row Mellin--Landau consumer.

The exact implication is

```text
TAP4: a_2(X)>=0 and a_3(X)>=0 for all X
  -> RH.
```

The two rows suffice by the exact cancellation factorization

```text
P_2(z)=P_3(z)=0 -> -3*(2^(-z)-1)*(2^(-z)-2)=0,
```

which is impossible for `Re z>0`.

## Replay

```bash
cd experiments/X-96100-two-row-annular-mellin
python3 verify.py --limit 1000000 --output results/verification.json
python3 tests/test_verify.py
gcc -O3 -std=c11 scan_extended.c -lm -o scan_extended
./scan_extended 20000000
```

Retained proof object:

```text
80035fd9bf49a953da41b94530e9a11224b8015e12db3b9e4f277860d1c67f9e
```

## Boundary

```text
normalization firewall              PROVED
annular Mellin transform             PROVED
two-row noncancellation              PROVED
TAP4 -> RH                           PROVED IMPLICATION
TAP4                                 OPEN / RH-BEARING
Riemann Hypothesis                   UNPROVEN
```
