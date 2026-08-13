# X-91114 — Rough endpoint ports do not tensorize

Companion exact counterexample for `R-91303`.

```bash
python3 experiments/X-91114-rough-port-nontensorization/verify.py
```

Expected verdict:

```text
PASS_ROUGH_PORT_NON_TENSORIZATION_COUNTEREXAMPLE
```

The standard-library checker uses exact `Fraction` arithmetic and directed
rational square-root enclosures with denominator `10^70`. It proves that the
mixed `(67,71)` endpoint-port detail is below `-1.33` at `x=4690`.
