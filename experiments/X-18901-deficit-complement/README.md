# X-18901 — Canonical deficit augmentation

This standard-library-only experiment replays the finite arithmetic of
`L-18901`.

Given a positive metric, an exact operator lower model

```text
A >= g G-D,   D>=0,
```

an initial packet `U0`, a proposed high-deficit augmentation `W`, and a proposed
safe complement `C`, the checker verifies:

1. positivity of the metric and deficit;
2. the exact lower-model Loewner inequality;
3. a complete metric-orthogonal decomposition `U0 direct_sum W direct_sum C`;
4. strict deficit above `g-Gamma` on `W`;
5. deficit at most `g-Gamma` on `C`;
6. exact high/safe spectral decoupling;
7. the final complement floor `A|C >= Gamma G`.

The retained exact control has

```text
g                         2
Gamma                     1
danger threshold          1
initial packet rank       1
augmentation rank         2
safe complement rank      1
final floor slack         3/4
```

The unaugmented packet misses the exact negative direction `e2`. The canonical
augmentation captures `e2,e3`, and the surviving complement has operator value
`7/4`.

Run:

```bash
python experiments/X-18901-deficit-complement/verify.py \
  experiments/X-18901-deficit-complement/certificates/synthetic.json

python -m unittest discover -s \
  experiments/X-18901-deficit-complement/tests -v
```

## Proof boundary

The checker validates finite rational metric, lower-model, spectral-split, and
floor arithmetic. It does not prove the Suzuki lower symbol, compactness or
trace-class properties of its positive deficit, nor that the initial
cardinal–radical packet already contains the added high-deficit directions.
