# X-91551 — native packet-loss gluing

This exact rational replay checks the algebra of `T-91551`:

- child target weights form a subprobability vector;
- packet loss is homogeneous in the actual child packet;
- favorable negative child losses are permitted;
- a score-superordinate parent ledger and score-noncontracting lift imply
  parent native loss at most current debt plus weighted child losses.

It does not certify the arithmetic Hall producer, physical carry feasibility,
the factor-54 outer/collar machinery, or RH.

```bash
python3 verify.py
```
