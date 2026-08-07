# X-20804 — Exact factorial source-notch replay

This checker verifies the finite rational identities behind `L-20804`.

For each `r=1,...,8`, it constructs

```text
F_r(x)=x^r / product_(n=1)^r (x-n^2)
```

and the exact coefficients

```text
u_(r,n)=(-1)^(r-n) n^(2r)/[(r-n)!(r+n)!].
```

It checks

```text
F_r(x)=2 sum_(n=1)^r u_(r,n) x/(x-n^2),
2 sum_(n=1)^r u_(r,n)=1,
```

at several exact rational probes, and verifies the finite binomial upper bound
for

```text
2 sum u_(r,n)^2.
```

Run:

```bash
python verify.py --max-r 8 --output results/verification.json
python -m unittest discover -s tests -v
```

The gamma response and superpolynomial metric-adjusted asymptotic are analytic
parts of `L-20804`. This experiment proves no source Schur sign by itself.
