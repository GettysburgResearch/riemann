# X-99100 — Exact score-debt supermartingale replay

Run:

```bash
python3 verify.py
```

The checker verifies:

- exact causal/hazard coefficient algebra;
- `1/sqrt(67)<1/8` by the exact square comparison `64<67`;
- a varying-depth, branching actual-mass tree;
- exact current-mass plus descendant-debt telescoping;
- rejection of the mutation that counts current/survival coefficients as
  recursive mass;
- directed rational square-root enclosures proving the fixed `P_61` terminal
  ledger is below `3600`.

The replay does not prove the compact Hall theorem, the equality endpoint
measure, the terminal unit-debt estimate, the all-column theorem, the endpoint
consumer, or RH.
