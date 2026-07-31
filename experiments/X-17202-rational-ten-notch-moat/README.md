# X-17202 — Exact rational ten-notch RH moat

Experiment ID: `X-17202`  
Issue: #172  
Agent: `gpt56-172n-01`  
Claim: `L-17201`  
Status: independently audited exact certificate; zero census has one backend

## Question

Can a completely exact finite notched filter be given a small, rigorous
critical-line moat without subtracting cumulative zero-count upper bounds?

## Result

Yes, conditionally on RH and the `T-15404` explicit-formula normalization.
The filter uses ten exact rational notch widths and four exact dyadic widths in
the profile, then takes a convolution square and the exact `log(4)` pole shift.

The checker proves with fractions only:

```text
listed-zero contribution       < 1.404e-77
unlisted-zero contribution     < 3.987e-18
complete nontrivial-zero moat  < 4.000e-18
raw Q tail-domain moat, x>=28  < 1.000e-17
all-real raw Q moat             18000
```

The all-real constant is intentionally crude.  It includes a direct absolute
bound for the compact startup interval.  The `4e-18` number alone is not a
valid raw-prime bound there.

## Commands

Pure exact-rational replay, requiring only Python 3.12:

```powershell
python .\verify.py
```

Arb replay of the zero census, pi interval, `xi` reciprocal sum, and the
`x>=28` trivial-zero estimate:

```powershell
$env:PYTHONPATH='C:\path\to\riemann\repo\.deps'
python .\verify.py --arb --output .\results\verification.json
```

The retained producer used `python-flint 0.9.0` at 320-bit precision.  The
`.deps` directory is deliberately ignored and is not part of the certificate.

Run adversarial unit tests from this directory with:

```powershell
python -m unittest -v tests.test_verify
```

## Certificate architecture

- `certificate.json`: exact filter widths, zero intervals/count jumps, pi
  enclosure, count partition, and declared rational moats;
- `verify.py`: recomputes every attenuation and Hadamard-tail inequality using
  `fractions.Fraction`; `--arb` recomputes analytic enclosures and counts;
- `tests/test_verify.py`: rejects count and pi-ledger mutations;
- `results/verification.json`: retained checker output.

For the tail, the positive Hadamard mass of the ten listed pairs is subtracted
from the proved positive total

```text
2 + EulerGamma - log(4*pi).
```

This is a valid remainder-mass partition.  It is not the invalid operation of
subtracting two cumulative upper bounds.

## Environment

- Windows, 64-bit;
- bundled CPython 3.12.13;
- exact backend: Python `fractions.Fraction`;
- directed analytic backend: python-flint 0.9.0 / Arb at 320 bits;
- no random seed;
- no FFT, fitted window, or ordinary floating comparison in the verifier.

## Limitations

- The Arb zero census has not yet been reproduced by an independent backend.
- The explicit-formula normalization and the extension from smooth windows to
  this `C_c^26` spline remain source-level review dependencies.
- No prime-side interval exceeding either moat was found or certified.
- A useful all-real constant needs a directed compact-interval spline sweep;
  `18000` is merely a fail-closed theorem constant.
