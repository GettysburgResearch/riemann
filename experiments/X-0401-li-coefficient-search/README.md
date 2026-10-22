# X-0401 — Li-coefficient discovery and exact certificate reductions

Experiment ID: X-0401  
Agent: `gpt56-04`  
Issue: #14  
Status: EMPIRICAL search plus exact algebraic checker  
Dates: 2026-07-22 to 2026-07-23

## Research question

Can either of two independent numerical representations reveal a negative
standard Li coefficient, and can any nominated index be reduced to a compact
certificate whose final sign is checked with exact rational arithmetic?

A rigorously proved value `lambda_n<0` would be a finite RH counterexample
witness through T-0303.  No such value has been found here.

## Discovery methods

### Calibration method A: local Stieltjes/eta recurrence

`calibrate.py` implements Formula A of L-0401.  It obtains the formal
logarithmic derivative of `t*zeta(1+t)` from Stieltjes constants and forms the
finite binomial transform for `lambda_n`.

### Calibration method B: direct high-precision Cauchy extraction

The same script independently samples

`d/dz log(2*xi(1/(1-z)))`

on a circle and computes each small coefficient by a direct discrete Fourier
sum using 100-decimal `mpmath` arithmetic.  It does not reuse the recurrence.

### Wide discovery method: binary64 Cauchy--FFT

`run.py` samples the logarithmic derivative with `mpmath.fp`, applies a NumPy
FFT, and rescales by the Cauchy radius.  Isolated zeta-derivative failures are
recomputed with 40 decimal digits and counted.

This method remains discovery-only.  It has no directed rounding, certified
special-function values, or certified DFT.

## Exact certificate layer

L-0402 supplies two finite reductions implemented by
`verify_dyadic_certificate.py` under schema `riemann.li-dyadic.v1`.

### Local certificate

Given dyadic intervals for `a1` and every `B_k` in

\[
\lambda_n=n a_1+\sum_{k=2}^{n}\binom nk B_k,
\]

the checker propagates the interval using exact Python integers and
`fractions.Fraction`.

### Cauchy--DFT certificate

For

\[
G(z)=\sum_{m\ge0}\lambda_{m+1}z^m,
\]

sampling at radius `r` with `M` roots of unity gives the exact alias identity

\[
D_{m,M}(r)=\lambda_{m+1}+
\sum_{\ell\ge1}\lambda_{m+\ell M+1}r^{\ell M}.
\]

If `G` is analytic on `|z|<=R`, `r<R<1`, and `|G(z)|<=B` on `|z|=R`, L-0402
bounds the alias tail by

\[
E=\frac{B}{R^m}\frac{(r/R)^M}{1-(r/R)^M}.
\]

The checker widens the supplied exact DFT interval by `[-E,E]` and reports a
certified negative only when the final rational upper endpoint is strictly
below zero.

The checker deliberately does not call `zeta`, `Gamma`, an FFT, or any other
transcendental backend.  It verifies interval propagation only.  A complete
certificate still needs an independent producer proving the function-value
intervals, the outer-circle bound, and analyticity of the full outer disk.

## Reproduction

Environment used for the committed discovery outputs:

- CPython `3.13.5`
- `mpmath 1.3.0`
- `numpy 2.3.5`
- Linux `6.12.13`, x86-64, glibc `2.41`

Discovery commands:

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

Exact-checker commands:

```bash
python -m unittest discover -s tests -v
python -m compileall -q verify_dyadic_certificate.py tests

python verify_dyadic_certificate.py \
  certificates/synthetic-local-negative.json

python verify_dyadic_certificate.py \
  certificates/synthetic-cauchy-negative.json
```

Ten adversarial checker tests pass.  In the synthetic Cauchy control with
`n=2`, `M=4`, `r=1/2`, `R=3/4`, and `B=1/128`, the alias radius is exactly
`1/390`.  A strict synthetic negative is accepted, while a smaller apparent
negative is widened through zero and rejected.  These objects test only the
checker and are not Li coefficient claims.

## Original source and result digests

| File | SHA-256 |
|---|---|
| `calibrate.py` | `3f0cd618cfc62e1b32ad6387cd591772d3253876c7f601a73c3617ae287d70ce` |
| `run.py` | `4bedceff625a490685aa2dc3d8159f5e3da758741bb5ded83e6a62205020ed06` |
| `results/calibration-n50.json` | `26b3350185e6c759fe3b22de1b0ba3a0b38a83963542235ff60fa7df8900502d` |
| `results/scan-n100000-alpha10.json` | `71126df63e002dc243abfc08dfe066f6483fd21f9b2547d73e5ded0c6380df5c` |
| `results/scan-n100000-alpha12.json` | `815f66d7577236d35104fe44f4a0239695b647be7a09f2d8ec678aa877595ed7` |

## Discovery results

The two calibration methods agree to approximately 74 decimal places through
`n=50`.  No negative coefficient was observed.

Both wide scans report `negative_count=0` through `n=100000`.
Representative alpha-12 values are:

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

## Radius, alias, and scale audits

For `r=exp(-alpha/n_max)`, L-0401 reduces transformed disk zero-freeness to
checking zeros below

`H(r)=1/sqrt(1-r*r)`.

The required heights are approximately `70.7143` for alpha 10 and `64.5536`
for alpha 12.  A rigorous successor must explicitly import or reproduce the
relevant verified-zero theorem.

The original FFTs have `r^M` approximately `4.12e-12` and `2.18e-14`, but
small damping alone is not an alias proof.  L-0402 identifies the missing
larger-circle factor and exact geometric bound.

L-0403 combines Li-transform geometry with the imported verified height
`3*10^12`.  A single hypothetical off-line zero above that height cannot gain
an `e`-fold transformed-modulus amplification before index

`18,000,000,000,000,000,000,000,000`.

This is not a Li-positivity theorem.  It is a strategic warning that extending
the same linear scan by a few orders of magnitude does not approach the
natural single-zero amplification scale.

## Machine-readable ledger

`results/exclusion-ledger.json` records the normalization, searched range,
method, certification level, result files, unresolved error classes, exact
checker coverage, and the height-to-index strategic barrier.

## Interpretation

No unconditional counterexample was found.  No `Z-####` identifier is
allocated.  X-0401 now contains:

- a reproducible empirical nomination engine;
- two exact finite certificate reductions;
- a standard-library rational checker with strict and zero-touching controls;
- a scale audit redirecting future work toward singularity reconstruction or
  selected enormous indices.

## Remaining blockers

- rigorous Stieltjes and recurrence input enclosures;
- rigorous zeta, digamma, and transformed-function values;
- a certified outer-circle supremum and full-disk analyticity proof;
- rigorous DFT or contour summation enclosures;
- an independent analytic producer and end-to-end positive calibration;
- a targeted method for the near-`z=1` scale rather than a modestly larger scan.
