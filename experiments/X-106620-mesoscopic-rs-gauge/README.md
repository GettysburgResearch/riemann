# X-106620 — Mesoscopic frozen Riemann--Siegel gauge replay

Run:

```bash
python -B experiments/X-106620-mesoscopic-rs-gauge/verify.py
```

The replay checks:

- the exact constant-scale packet factorization;
- cancellation of the amplitude connection in the fifth cross-ratio;
- the \(3/4000+11/500\) constant ledger;
- the diagonal-Rouché counterfamily;
- logarithmic carrier-mismatch rates on deterministic fixtures.

It does not evaluate zeta, Selberg's theorem, Conrey's fifth-derivative input,
or `MESORSGAUGE106620`.
