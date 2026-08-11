# X-91001 — Bessel, Hausdorff, Euler dilation, and Jordan-flow regression

Finite exact/high-precision checks for `L-91001`, `T-91001`, `L-91002`, and
`L-91003`.

The replay checks:

```text
reverse-Bessel polynomial identity;
closed exponential generating function;
golden-ratio Poissonized sign boundary;
GIG/inverse-Gaussian moment representation;
strict positive polynomial localizer and Hankel PSD;
Borel cubic-resolvent identity;
synthetic Hausdorff and false-pole controls;
finite-prime Euler–Bessel block Gram PSD;
Jordan Dirichlet product and compound-Poisson exponent;
completed xi cocycle and symmetry-boundary unitarity.
```

Expected verdict:

```text
PASS_X_91001_BESSEL_HAUSDORFF_JORDAN
```

The experiment proves finite algebra and synthetic controls only. It does not
establish the missing zeta sign or RH.
