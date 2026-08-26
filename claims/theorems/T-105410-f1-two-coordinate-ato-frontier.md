# T-105410 — F1 two-coordinate Hodge package and exact arithmetic-trace frontier

Claim ID: `T-105410`

Status: **PROVED GEOMETRIC/TRACE PACKAGE; ONE ARITHMETIC OFF-DIAGONAL OPEN**

This is checkpoint two on dedicated PR #730.

## Exact advances

- `L-105403` gives a positive exponential prime-box spline whose Laplace
  transform contains the exact finite native Euler numerator.
- `L-105404` diagonalizes the primitive three-ray Hodge norm:
  \[
  \mathcal H_{\rm prim}=A^2/24+2(G-A)^2.
  \]
  The cofinal Hodge theorem is therefore exactly a conjunctive
  activation-curvature plus filtered-disk-slope estimate.
- `L-105405` constructs the physical observation as one compact PSD Gram trace,
  writes its exact gcd/adelic coordinates, and removes every diagonal,
  same-product and far-ratio sector using frozen PR #719 inputs.
- `R-105410` prevents finite Hodge positivity from being promoted to a cofinal
  size estimate.

## Current status of the original programme targets

```text
NPR105300 native finite realization             PROVED
AHG105301 finite source-twisted Hodge gap        PROVED, normalized gap 1
finite ATO mixed trace                           PROVED
ATO diagonal/same-product/far-ratio sectors      PROVED / CLOSED
ATO distinct-product off-diagonal                OPEN as F1ATO105405
fixed-detector composition                       PROVED CONDITIONAL ON F1ATO
Riemann Hypothesis                               UNPROVED
```

The single surviving implication is

\[
\boxed{
\mathrm{F1ATO105405}
\Longrightarrow
\mathrm{RH}.
}

`F1ATO105405` is an exact compact-shell, source-faithful, distinct-product
near-collision estimate. It is the arithmetic trace theorem requested by the
programme, now stripped of every geometric and diagonal ambiguity.
