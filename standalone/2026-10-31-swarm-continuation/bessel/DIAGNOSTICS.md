# Reproducing the cofinal companion checks

The analytic claims are in `COFINAL_COMPANION.md`; the independent mathematical review binds that manuscript in `REVIEW_COFINAL.md`. The finite rational checker and the numerical diagnostics have different evidentiary scopes.

## Exact finite structure

```sh
python -I -S -B verify_companion_structure.py
python -I -S -B -O verify_companion_structure.py
```

Both commands use only the standard library. Their outputs agree byte for byte with `STRUCTURE_CHECKS.json`. They check 24 independent order-versus-differential recurrence identities, 48 coefficient-sign conditions, three low-order formulas, exact concentration constants, and the special-value ODE factor. These are finite algebraic checks of ingredients used in the manuscript.

## Ordinary source quadrature

```sh
python -B companion_probe.py
```

This program needs SciPy. It writes `COMPANION_PROBE.json`. It evaluates the two terms of the companion integral and the derivative of the actual source transform at three nearby real roots. The starting locations only seed brackets. The integration and theta sums use finite cutoffs; no directed bounds are produced. Higher rows were omitted because cancellation made binary64 quadrature unreliable.

The retained approximate values of `J_infinity(E)/X'(E)` are `1.48571e10`, `5.06735e14`, and `3.66755e17`. A separate negative-energy control compares the quadrature at `E=-1/16` with the proved exact value `-1/(2*sqrt(2)*pi)`. The output records their observed difference, which is a numerical consistency check.

## Ordinary cofinal residue calculations

```sh
python -B residue_scaling_diagnostic.py 240
python -B residue_scaling_diagnostic.py 360
python -I -S -B summarize_residue_scaling.py
```

These use the standard library. The first two runs can take several minutes. They evaluate the literal sampled source using ordinary Decimal arithmetic, with the source-polynomial routines copied from the PR #1026 Decimal diagnostic and credited in `source_polynomials.py`.

The selected schedule is `M=ceil(a*(3+2*log(a)))`, with `(a,M)` equal to `(20,180)`, `(40,416)`, `(80,942)`, and `(160,2105)`. Thus the sampling ratio increases along the schedule. The program locates the first three real sign changes in energy up to 250; it does not count all complex zeros or all real poles.

For a located denominator root lambda, the reported scaling is

\[
\frac{\operatorname{Res}_{E=\lambda}(-A/B)}{2\pi a e^{-2a}}.
\]

The analytic theorem predicts convergence to the source ratio above when the target zero is simple and the limiting companion is nonzero. The last column compares the scaled value with the six-digit quadrature target; it is not an independently certified limiting constant.

| a | M | First ratio | Second ratio | Third ratio |
|---:|---:|---:|---:|---:|
| 20 | 180 | 0.00399834 | 0.000108620 | 0.0000204454 |
| 40 | 416 | 0.0405541 | 0.00555760 | 0.00456987 |
| 80 | 942 | 0.169038 | 0.0613833 | 0.0822383 |
| 160 | 2105 | 0.391544 | 0.238892 | 0.314271 |

The two saved full receipts agree across their 48 numeric fields with maximum relative discrepancy `3.965590643223e-106`. `RESIDUE_SCALING_SUMMARY.json` records this comparison, compact values, and hashes of the full receipts and their producer code. Precision agreement is not a rigorous error bound: both runs share the same algorithm and finite stopping rules. The table illustrates the slow approach and the residue scale; neither it nor these computations is a proof of a residue sign or a complete pole census.
