# X-106800 — Beta spectral-abscissa replay

Run:

```bash
python -B experiments/X-106800-beta-spectral-abscissa/verify.py
```

The replay checks:

- exact exponent bookkeeping on a rational grid;
- finite summation-by-parts identities;
- the terminating duplicate-67 prefix inverse;
- the endpoint-only maximal-prefix firewall;
- the critical \(3/40+11/500=97/1000\) ledger;
- that the Vinogradov–Korobov scale dominates the critical square-root-log
  phase loss.

It does not reprove the classical Mertens zero-abscissa theorem, rerun the
Lee–Leong explicit Mertens analysis, evaluate zeta, prove a fixed power
saving, establish a new zero-free half-plane, prove RH, or prove GRH.
