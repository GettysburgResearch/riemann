# X-105655 — Cauchy translation trace correction replay

Run:

```bash
python -B experiments/X-105655-cauchy-translation-trace/verify.py
```

Expected controlling verdict:

```text
PASS_X_105655_CAUCHY_TRANSLATION_TRACE_CORRECTION
checks=39605
```

The replay uses exact `Fraction` arithmetic. It checks:

- the binding two-factor distinction between canonical model overlap and the complex cross-Dirichlet scalar;
- the exact one-factor phase-defect/current-reserve identity on an `80 x 80` rational grid;
- strict `CTI105655` on every declared collinear two-factor fixture with depths and shift in `1,...,20`.

The replay does **not** prove the general complex multipacket Cauchy trace inequality, the cofinal Xi passage, the physical pointwise microscope, or RH.
