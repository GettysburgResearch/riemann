# X-106151 — Reflection complementarity

Standard-library exact replay for:

- reflection as a self-adjoint involution;
- even/odd orthogonal projection energies;
- constant norm complementarity;
- reflection-signature and mismatch formulas;
- equivalence of the even, odd and self-convolution differential gates for
  every zero-mode-killing operator.

Run:

```bash
python3 verify.py
```

Expected:

```text
PASS_X_106151_REFLECTION_COMPLEMENTARITY
exact_checks=183600
proof_object_sha256=d24b5505bd463acc7396590c8ddfe5a1fe811eb3c2d7921a37c9d98490c28183
```

The replay does not prove `REFSIG106150`, `SFSC106150`, `WKSFSC106150`,
`BCI102990`, or RH.
