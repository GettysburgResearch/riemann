# Integration handoff — Haar/r-adic dyadic prime transport

Status: `PROPOSED`, pending independent review. RH is not claimed proved.

## Preferred order

1. `T-20201` — Haar pole-descent criterion.
2. `T-20203` — critical-mesh `r`-adic generalization.
3. `T-20207` — shrinking-cell tiling criterion.
4. `T-20208` — first-knot correction and all-positive dyadic blocks.
5. `L-20210` — fixed-width Taylor/curvature normal form.
6. `L-20211` — exact dyadic streaming formula.
7. `L-20212` — adjacent-cell endpoint stitching.
8. `L-20208/L-20209` — transport reserve minus Bregman square.
9. `T-20206` — curvature-corrected transport criterion.
10. `X-20203` — exact synthetic regression.

## Exact remaining theorem

For every sufficiently large `r`, every prime-power knot in `[2^r,2^(r+1)]` must satisfy, up to `exp(o(r))`,

```text
H_r^*(A_j)-B_j
 >= [A_j-H_r'(log q_j)]^2/(2m_r).
```

The left side is a signed quantile-transport reserve. The right side is a positive centered prime-mass square divided by a directed curvature floor.

## Cross-branch links

- PR #219 should provide/adapt the prime-polygon reserve ledger.
- PR #216 should target the centered mass square through its Selberg/prime-pair machinery.
- PR #208 supplies the square-screw/D-0001 principal-coordinate identity.
- PR #202 supplies the original square-screw and Landau normalization.

These branches must share one prime-power manifest and one archimedean source convention before any combined sign is promoted.

## Merge boundary

Do not merge as an RH result. Review the Landau one-sided upper-bound argument, the `q=2` correction, Legendre orientation, strict concavity at knots, and the cofinal quantifiers independently.
