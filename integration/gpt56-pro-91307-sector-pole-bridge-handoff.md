# Integration handoff — sector threshold, pole bridge, and corrected completion

## Target branch

```text
research/gpt56-pro/91302-triune-adelic-scattering
```

## Parent at authoring time

```text
df0c04b4c4be3c04cd503db971b869efdb19bee3
```

Recheck the live branch before integration.

## Review order

1. `L-91327` — product-sector and translation threshold.
2. `L-91328` — cylinder distribution and weighted norm.
3. `L-91329` — Green/convolution commutation and orientation.
4. `L-91330` — endpoint expansion and pole bridge.
5. `R-91308` — correction to the naive Julia–Wick wave operator.
6. `R-91309` — pole-node source norm mismatch.
7. `T-91307` — corrected full proposal.
8. `O-91305` — current boundary.
9. experiment and retained result.
10. full report.

## Supersession

`T-91305` and `T-91306` remain useful provenance, but their preferred same-vacuum/Wick language must be read through `R-91308`. `T-91307` is the corrected production target.

The all-generation vector of `L-91319` remains an exact positive source object but may not be called the exhausted pole-node model source without a new normalization theorem; `R-91309` proves the asymptotic mismatch.

## Promotion status

```text
exact theorem packet:             ready for hostile review
corrected full proposal:          yes
full proof of RH:                 no
conclusion-producing theorem:     EPBOT_omega remains open
```
