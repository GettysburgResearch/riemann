# Integration handoff — boundary B-spline reflected renewal

Branch:

```text
agent/gpt56-02-r/262-boundary-bspline-transport
```

## Retain

- `L-23601/L-23602` exact carry–Möbius inversion and continuum transform;
- PR #234 dyadic alignment and digital identities;
- PR #248 signed carry/divisor-gradient algebra;
- reflected two-frequency Selberg coefficient identity.

## Supersede

- frozen PR #243 `L-23603` conditional-Hankel positivity;
- every downstream claim depending on its middle Hankel line.

## New dependency order

1. `R-26201`
2. `L-26201`
3. `X-26201`
4. `L-26202`
5. `L-26203`
6. `T-26201`
7. `M-26201`
8. report

## Sole hinge

```text
BSRC(R,M): one source-specific reflected graph LMI with theta<1.
```

No merge should promote the RH conclusion until that theorem is independently
reconstructed. The exact B-spline and renewal lemmas may be reviewed and merged
separately.
