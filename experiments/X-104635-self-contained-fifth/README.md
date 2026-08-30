# X-104635 — Self-contained fifth-input replay

Run:

```bash
python3 verify.py results/verification.json
```

The replay imports the exact rational Conrey evaluator from `X-104620`,
certifies `alpha_5>49/50` at `R=1, phi(x)=1-x`, and checks every rational
constant in the self-contained fifth-endpoint 90-percent ledger.

Expected verdict:

```text
PASS_T104635_SELF_CONTAINED_FIFTH_LEDGER
48790aed9f72534e58705e5bc57676da4bc811a75a3c11e2244cb19606e94ef4
```

It does not prove `FRACTRANS104635`, more than ninety percent, or RH.
