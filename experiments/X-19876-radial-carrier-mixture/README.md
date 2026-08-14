# X-19876 — Radial Jordan/scattering carrier mixture

Run:

```bash
python3 verify.py
```

The standard-library replay checks the exact coefficient identity at several
prime-power carriers, the corrected tail-Hankel anticommutator formula, the
two-carrier norm split, and a strict mismatch for the withdrawn
`L-19874.20` identity.

The analytic theorem is in `L-19876`; this finite replay does not prove the
completed source lock or RH.
