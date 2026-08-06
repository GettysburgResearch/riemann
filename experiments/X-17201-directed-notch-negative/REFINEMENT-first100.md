# First-100-zero refinement at the reported FFT minimum

Status: `CERTIFIED SINGLE-BACKEND ARB LINE ENVELOPE`; negative support attempt rejected  
Filter: retained `N8/notch2/highpass8/delta=1/128` rational filter  
Point: `x = 18.05113474606469`

`refine_first100.py` uses 320-bit Arb balls for the first 100 positive zeta
zeros.  Arb also proves `N(237)=100`, so all unlisted ordinates exceed 237.
The elementary eta-function argument inherited from `L-17201` excludes a
nontrivial zero with ordinate zero.
Under RH the Hadamard identity

```text
sum_(gamma>0) 2/(1/4+gamma^2) = 2 + EulerGamma - log(4*pi)
```

turns the residual reciprocal mass into a complete higher-zero tail bound.
For ten profile boxes and `W=product(widths)`, the elementary transform bound

```text
|Ghat(i gamma)| <= (3*4^10/W^2) gamma^-20
```

gives

```text
first 100 absolute line sum       1.399460730155798...e-14
all higher zeros, rigorous        9.40865418835723...e-16
complete RH line envelope         1.493547272039370...e-14
declared rational ceiling         1.494000000000000...e-14
```

At the reported minimizer, direct Arb evaluation gives

```text
first-100 spectral value         -1.373450546977370...e-14
reported FFT value               -1.435911674853342...e-14
difference                        -6.2461127875972...e-16
```

The trivial-zero correction is below `3e-30`.  The FFT discrepancy is smaller
than the rigorous `9.409e-16` allowance for all zeros after number 100, and the
FFT value lies inside the resulting RH-permitted point interval.  Thus the
reported `1.4359e-14` magnitude is **not an exceedance** of the completed RH
line envelope.  It exceeded only the earlier first-50 truncation.

This does not prove that the entire `6.25e-16` difference is numerical noise:
genuine zeros numbered 101 and above may contribute.  It does prove that an
exact-support attempt around this FFT sample is not warranted.

Replay on the retained Windows environment:

```powershell
$env:PYTHONPATH='C:\path\to\riemann\repo\.deps'
python .\refine_first100.py
```

The interpretation as `Q_G` remains conditional on the explicit-formula
normalization and finite-`C^18` extension recorded in the main experiment.
