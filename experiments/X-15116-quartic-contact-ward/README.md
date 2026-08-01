# X-15116 — Exact quartic finite-jet contact Ward regression

This experiment verifies the finite algebra in `L-15134/R-15111` using only
Python integers, `fractions.Fraction`, JSON, and SHA-256.

## Control

The raw and renormalized spectra are

```text
A :  1, -1, 2, -2
K : 11/5, -11/5, 2/5, -2/5
D=A-K.
```

One grading swaps each positive/negative pair. Consequently every odd trace
vanishes. The quadratic traces agree exactly:

```text
Tr(A^2)=Tr(K^2)=10.
```

The supplied linear one-contour counterterm at order four is zero, but the
required nonlinear cyclic contact counterterm is

```text
-8064/625.
```

Thus

```text
raw scalar order four - renormalized cyclic order four = -8064/625.
```

This is the first nontrivial even obstruction after quadratic matching and
cubic parity.

## Reproduction

```bash
python3 verify.py certificates/graded-order4-obstruction.json
python3 -m unittest discover -s tests -v
```

The verifier also accepts the exact nonlinear Ward repair when the supplied
counterterm is changed to `-8064/625`.

## Trust boundary

This is an exact finite counterexample to automatic contact cancellation. It
does not evaluate the manuscript's Riemann contour tensors and does not prove
that their quartic anomaly has this numerical value. It proves that common
linear subtraction, grading, and lower-moment agreement do not imply the
contact-free diagonal theorem.
