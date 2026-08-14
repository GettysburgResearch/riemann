# X-91685 — Target-Lorenz common-source vector primal/dual replay

Run the exact replay:

```bash
python3 verify.py
python3 -m py_compile verify.py
```

Expected verdict:

```text
PASS_TARGET_LORENZ_VECTOR_PRIMAL_DUAL
```

The verifier uses the Python standard library, exact `Fraction` arithmetic and
integer square-root enclosures. It checks:

```text
simultaneous leftmost-target bathtub optimality;
exact box-image support-function duality fixtures;
an explicit failed-row cutoff Farkas separator;
full target-determinant sufficiency;
the radical inequalities used in the py<5j theorem.
```

Its retained proof-object digest is written to `results/verification.json`.
The replay proves the abstract theorem and the exact low-quotient result. It
does **not** certify the full actual `P_61` row family or RH.

Optional deterministic reconnaissance:

```bash
python3 reconnaissance.py
```

This requires NumPy and writes `results/reconnaissance.json`. It uses float64,
is explicitly classified `FLOATING_RECONNAISSANCE`, and never decides a proof
status.
