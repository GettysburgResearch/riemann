# X-25601 — Exact RBC depth/reserve regression

This standard-library experiment verifies the finite algebra introduced in the
RBC reserve-completion pass.

It checks:

- the nilpotent matrix inverse;
- the matrix logarithmic derivative;
- the correct last-row anchor for the declared forward shift;
- the exact finite endpoint tail;
- zero aggregate Schur reserve with a nonzero packet-kernel control;
- root-of-unity depth Parseval;
- meromorphic charge conservation controls;
- cancellation of far-right residual decay by physical deweighting;
- the distinction between rank-one charge and full-shell support.

Run:

```bash
python verify.py certificates/synthetic.json
python -m unittest discover -s tests -v
```

Retained verdict:

```text
PASS_EXACT_RBC_DEPTH_RESERVE_CLASSIFICATION
8/8 mutation tests
proof-object SHA-256
f9804f4155ea5f88754f6bafc8b988542f3472b9570188269d283d876092a3be
```

This is exact synthetic algebra only. It does not evaluate zeta, construct a
source-specific anchor reserve, prove the fixed-ratio shell estimate, or prove
RH.
