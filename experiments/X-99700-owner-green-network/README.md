# X-99700 — Owner-Green network algebra

This lightweight standard-library replay checks the finite algebra behind `T-99700`.

It verifies:

1. `beta*g=epsilon` through the frozen finite limit;
2. the logarithmic-owner probability identity as a formal prime-log vector;
3. the signed owner-martingale identity;
4. exact zero quadratic variation on every squarefree non-67 state in range;
5. detailed balance of every labelled prime-power birth/death edge;
6. edgewise positivity of `E(f,f Phi)` for all local coefficient transitions;
7. the three decorated squarefree fibres and same-vertex trace cancellation.

Run:

```bash
python3 verify.py --output results/verification.json
```

Expected verdict:

```text
PASS_T99700_OWNER_GREEN_NETWORK_ALGEBRA
```

The replay deliberately does **not** certify `PXGC99700`. It includes the squarefree zero-quadratic-variation negative control and records

```text
pxgc99700_proved = false
rh_established   = false
```

No heavy endpoint scan, Hall campaign, or formal build is run.