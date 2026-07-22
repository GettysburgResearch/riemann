# X-0401 — Independent Li-coefficient discovery search

Experiment ID: X-0401  
Agent: `gpt56-04`  
Issue: #14  
Status: EMPIRICAL  
Date: 2026-07-22

## Research question

Does either of two independent numerical representations reveal a negative
standard Li coefficient, which could then be sent to interval certification as
a finite RH counterexample candidate?

## Methods

### Calibration method A: local Stieltjes/eta recurrence

`calibrate.py` implements Formula A of L-0401.  It obtains the formal
logarithmic derivative of `t*zeta(1+t)` from Stieltjes constants and then forms
the finite binomial transform for `lambda_n`.

### Calibration method B: direct high-precision Cauchy extraction

The same script independently samples

`d/dz log(2*xi(1/(1-z)))`

on a circle and computes each small coefficient by a direct discrete Fourier
sum using 100-decimal `mpmath` arithmetic.  It does not reuse the recurrence.

### Wide discovery method: binary64 Cauchy--FFT

`run.py` samples the same logarithmic derivative with `mpmath.fp`, applies a
NumPy FFT, and rescales the coefficients by the Cauchy radius.  Isolated zeta
derivative convergence failures are recomputed with 40 decimal digits and are
counted in the output.

This wide method is deliberately labeled discovery-only.  It has no interval
enclosures and no rigorous aliasing bound.

## Reproduction

Environment used for the committed results:

- CPython `3.13.5`
- `mpmath 1.3.0`
- `numpy 2.3.5`
- Linux `6.12.13`, x86-64, glibc `2.41`

Commands:

```bash
python calibrate.py \
  --n-max 50 --dps 100 --radius 0.5 --samples 256 \
  --output results/calibration-n50.json

python run.py \
  --n-max 100000 --oversample 2 --alpha 10 \
  --output results/scan-n100000-alpha10.json

python run.py \
  --n-max 100000 --oversample 2 --alpha 12 \
  --output results/scan-n100000-alpha12.json
```

## Source and result digests

| File | SHA-256 |
|---|---|
| `calibrate.py` | `3f0cd618cfc62e1b32ad6387cd591772d3253876c7f601a73c3617ae287d70ce` |
| `run.py` | `4bedceff625a490685aa2dc3d8159f5e3da758741bb5ded83e6a62205020ed06` |
| `results/calibration-n50.json` | `26b3350185e6c759fe3b22de1b0ba3a0b38a83963542235ff60fa7df8900502d` |
| `results/scan-n100000-alpha10.json` | `71126df63e002dc243abfc08dfe066f6483fd21f9b2547d73e5ded0c6380df5c` |
| `results/scan-n100000-alpha12.json` | `815f66d7577236d35104fe44f4a0239695b647be7a09f2d8ec678aa877595ed7` |

## Results

The two calibration methods agree to approximately 74 decimal places through
`n=50`.  No negative coefficient was observed.

Both wide scans report `negative_count=0` through `n=100000`.  Representative
alpha-12 values are:

| n | observed `lambda_n` |
|---:|---:|
| 1 | `0.02309573196825454` |
| 10 | `2.279339386184925` |
| 100 | `118.60377539968356` |
| 1000 | `2326.0531617081347` |
| 10000 | `34736.5797322616` |
| 100000 | `462580.78255525156` |

The alpha-10 and alpha-12 checkpoint values differ by at most about `1.41e-4`.
This is a stability diagnostic, not a certified enclosure.

## Radius and singularity audit

For `r=exp(-alpha/n_max)`, L-0401 shows that transformed disk zero-freeness
reduces to checking zeros below

`H(r)=1/sqrt(1-r*r)`.

The required heights are approximately `70.7143` for alpha 10 and `64.5536`
for alpha 12.  The experiment does not itself import or machine-check the
external verified-zero theorem; a rigorous successor must make that dependency
explicit and certified.

The discrete Fourier coefficient also contains alias contributions multiplied
by powers of `r^M`.  Here `r^M` is approximately `4.12e-12` (alpha 10) and
`2.18e-14` (alpha 12), but no bound on the unknown aliased coefficients is
proved.  Small damping alone is not a proof.

## Interpretation

No unconditional counterexample was found.  No `Z-####` identifier is
allocated.  X-0401 narrows this particular route empirically and supplies a
reproducible nomination engine for future interval certification.

## Limitations

- ordinary and high-precision floating point, not ball arithmetic;
- no directed rounding;
- no certified zeta, digamma, or FFT errors;
- no rigorous aliasing tail;
- two wide scans share one implementation;
- a finite positive search says nothing about all later coefficients.
