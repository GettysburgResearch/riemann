# X-90502 — Pole-null Lévy/heat replay

Run:

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```

The replay checks:

- the explicit Cauchy–Sobolev kernel against its defining bilateral integral;
- strict positivity of a finite evaluation Gram;
- the two exact pole-cardinal values;
- the hyperbolic pole index shift `q -> q+1` and pole-null index `q` on exact synthetic blocks;
- the digamma/Lévy jump identity on three Gaussian tests at 70 digits;
- the heat-trace sign for positive spectra and exponential detection of one negative eigenvalue;
- the globally convergent heat-moment expansion;
- the Fredholm/heat integral identity on a positive finite spectrum.

The computation does not prove the analytic trace-class lemmas, a prime-side sign theorem, or RH.
