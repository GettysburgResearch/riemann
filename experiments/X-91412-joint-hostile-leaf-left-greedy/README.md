# X-91412 — Joint hostile-leaf left-greedy replay

Status: **DIRECTED FINITE CERTIFICATE; UNIVERSAL PRODUCER SEPARATE**

This replay addresses the exact stopped leaf used by PR #456 to refute the survival-only Hall theorem:

```text
p=67, y=13, x=871.
```

It coalesces the complete even/odd causal score measures first, constructs the deterministic left-greedy displacement-eight flow, then replays every exhaustion decision in `mpmath.iv` interval arithmetic. It verifies strict target gain and strict gain in every component row `j=2,...,66`.

Run:

```bash
python3 verify.py
```

Expected verdict:

```text
PASS_JOINT_HOSTILE_LEAF_LEFT_GREEDY
```

Retained bounds:

```text
flow pieces:              151
largest upward edge:        4
target gain:              > 1.9395281350378766
minimum row:               66
minimum row gain:         > 0.008381548275463338
```

This proves that joint survival-hazard coalescence repairs the hostile leaf. It is not an all-parameter certificate and does not prove RH.

SHA-256 of the locally replayed source before GitHub serialization:

```text
c7b4641c3fb35affbf89c340578c4a292b6d9c7676b17ce6e573662edb366703  verify.py
9d7f3ce98792c6015c86f58efe28c2cbb49d5f75d8407296720451767b26db70  results/verification.txt
```
