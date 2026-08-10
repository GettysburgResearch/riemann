# X-32401 — exact two-contact Brownian/source replay

Run

```bash
python experiments/X-32401-two-contact-brownian/verify.py
```

The verifier uses only the Python standard library and `fractions.Fraction`.

It checks:

- 640 local-Euler coefficient/source classifications for `lambda=-1,-1/2,0,1/2,1` through `n=128`;
- 10,000 exact source-convolution carry-wavelet identities;
- 961 centered-interval Brownian/min Gram identities;
- three direct-Gram versus cumulative-tail layer-cake energy identities;
- seven exact linear-growth controls for `R-32401`.

Retained verdict:

```text
PASS_EXACT_TWO_CONTACT_BROWNIAN_NORMAL_FORM
```

Proof-object digest:

```text
41ee0afdaed3eed68a293ca33466d0462bd1535e4c75eb53bea213d334cccbfd
```

The replay certifies finite/formal algebra only. It does **not** prove `NTBR`, a subexponential energy estimate, or RH.
