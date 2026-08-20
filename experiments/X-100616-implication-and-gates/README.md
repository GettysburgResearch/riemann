# X-100616 — Implication-matrix AND-gate replay

Run:

```bash
python3 experiments/X-100616-implication-and-gates/verify.py
```

Expected first line:

```text
PASS_T100616_IMPLICATION_MATRIX_AND_GATES
```

The standard-library replay checks:

- the direct least/greatest-owner coefficient identity;
- the exact joint min--max hazard weights and their unit total mass;
- the cell critical-point/Turán sign equivalence;
- a finite monotone control for the divergent one-sided marginal mechanism.

The replay is deliberately fail-closed:

```text
AEP100612         not proved;
DNT100612         not proved;
Riemann Hypothesis not established.
```

The verifier authenticates the algebraic implication matrix, not the two
remaining long-collar arithmetic estimates.