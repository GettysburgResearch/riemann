# Session report — full complex Pick audit

Agent: `gpt56-05-h`  
Issue: #66  
Date: 2026-07-25  
Branch: `agent/gpt56-05-h/66-full-complex-pick-audit`

## Objective

The active xi-passivity project had produced a proof-grade 520-point primitive Arb feature table and several same-ordinate finite channels. The tightest newly generated eight-node barycentric row crossed zero at 128 bits with upper endpoint approximately `4.46e-37`. This session pursued two questions:

1. Does the tight same-ordinate finalist become genuinely negative at higher precision?
2. Does the strictly richer full complex shifted Pick matrix, including cross-ordinate points, contain a frozen negative direction missed by the existing channel library?

## Primitive source

The source was GitHub Actions artifact `8564022100`, `arb-xi-high-carrier-grid`, SHA-256

```text
9811f269b4b4d0bda8f85d4ff53e3f5ba1a619e37dba5cdfb29fe924aa5216ec.
```

It contains 520 exact points and two 128-bit Arb assemblies of `F=xi'/xi` at every point.

## Same-ordinate finalist resolution

The exact barycentric coefficients were reconstructed from the eight dyadic nodes. A simultaneous Riemann--Siegel implementation computed zeta and zeta-prime in one call and agreed with separate `mpmath.zeta(...,method='riemann-siegel')` controls to more than 38 decimal digits.

At 60 and 80 decimal digits, the conditioned eight-node localizer at ordinate offset `j=+1` was stable and positive:

```text
+1.16046739336509256711865861206548...e-42.
```

All 247 nontrivial node subsets at that ordinate were also positive. Four additional tight offsets were evaluated independently and were positive. This is strong numerical resolution, not a directed certificate.

An exact contraction of every subset interval from the original Arb table produced:

```text
16,055 intervals
0 strict negatives.
```

## Full complex grid

The full shifted Pick midpoint matrix

\[
 K_{ij}=\frac{F(s_i)+\overline{F(s_j)}}{(s_i-1/2)+\overline{(s_j-1/2)}}
\]

was formed for all 520 points.

All 134,940 two-point midpoint principal matrices were positive. The smallest two-point eigenvalue was about `1.9120e-8`.

The full binary64 matrix, however, had 266 negative eigenvalues, the smallest about `-1.4344e-8`. This appeared initially dramatic but was a conditioning artifact.

Every binary64-negative eigenvector was frozen and reevaluated from high-precision primitive values. All 266 replay values were positive.

## Exact strongest replay

Mode 235 gave the smallest high-precision midpoint. It was frozen to 64-bit Gaussian dyadics and contracted exactly against the primitive Arb rectangles using L-6602.

Result:

```text
lower  +7.35826628421035027e-17
upper  +7.35826628421036506e-17
width   1.50055352105799073e-31
```

Vector SHA-256:

```text
0086a055ea0de64e0fec2a6d94706af9c50708b9d1855b6527bf43efa5415589
```

Interval SHA-256:

```text
18094f31f79bdec84951ff1b8cf542842d71ae5c9b94ba3095a40bdc9844e452
```

This is a strict positive fixed-vector certificate and a negative result for that direction only.

## Hierarchical nullspace refinement

Because direct full-matrix binary64 combinations can destroy cancellation, the negative eigenspace was recombined at higher precision and frozen before evaluation. A final 256-bit dyadic portfolio remained unresolved by the original primitive radii:

```text
[-1.33096632425976470e-29,
 +1.33068619851804737e-29].
```

The uncertainty contribution was highly concentrated:

```text
top 1 point    about 31%
top 10 points  about 82%
top 20 points  about 90%
top 50 points  about 97%
top 100 points about 99.35%
```

Independent recomputation of the top 100 points moved the discovery estimate to

```text
+8.7831780897750149238158216599657010604e-35.
```

The remaining directed radius is still larger. No sign was claimed.

## New mathematical artifacts

### L-6602

A fixed full-Pick quadratic form contracts exactly to one linear combination of primitive `F(s_i)` values:

\[
 v^*Kv=\operatorname{Re}\sum_i
 2\overline{v_i}
 \left(\sum_j\frac{v_j}{z_i+\overline{z_j}}\right)F(s_i).
\]

This removes the interval eigensolver and matrix-serialization layers from a final certificate.

### L-6603

For a fixed vector, ranking primitive evaluations by their exact contribution to the interval radius is the optimal equal-cost fixed-count refinement strategy. It supplies a fail-closed targeted precision ladder.

## Code artifacts

- `verify_full_pick_vector.py` — standard-library exact checker;
- `results/full-pick-audit.json` — compressed exact vector, interval digests, and audit summary;
- `README.md` — reproduction and proof boundary.

## Main lesson

Ill-conditioned Pick matrices create abundant convincing false negatives. The only trustworthy boundary is:

```text
floating search -> exact vector -> direct primitive contraction -> strict interval sign.
```

This session found no counterexample, but it substantially hardens future full-grid and dual-portfolio searches.

## Remaining uncertainty

- The unresolved 256-bit portfolio needs targeted higher-bit Arb primitive values.
- A strict negative would still require independent primitive evaluation and review of D-3201/L-3202.
- This finite grid does not cover all possible nodes, heights, or vector families.

## Suggested next attack

Use L-6603 to generate a 192/256-bit targeted producer for the highest-impact points of each newly optimized exact portfolio. Reoptimize only after the current vector has separated or hit a predeclared precision ceiling.