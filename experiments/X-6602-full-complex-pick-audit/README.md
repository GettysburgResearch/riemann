# X-6602 — Full complex Pick audit of the high-carrier Arb grid

Experiment ID: `X-6602`  
Agent: `gpt56-05-h`  
Issue: #66  
Status: exact fixed-vector verification plus nonrigorous discovery searches  
Date: 2026-07-25

## Objective

The retained X-3902 artifact evaluates

\[
 F(s)=\frac{\xi'(s)}{\xi(s)}
\]

at 520 exact points:

- 65 ordinate offsets `j/32`, `-32 <= j <= 32`;
- eight horizontal offsets `2^-17,2^-15,2^-13,2^-11,2^-10,2^-9,2^-7,2^-5`;
- 128-bit Arb arithmetic;
- two overlapping primitive assemblies, `f_via_xi` and `f_via_parts`.

Earlier contractions used same-ordinate channels. X-6602 forms the full shifted Pick kernel across every pair of the 520 points and subjects every apparent negative direction to an exact fixed-vector replay.

## Source artifact

GitHub Actions artifact:

```text
name        arb-xi-high-carrier-grid
artifact ID 8564022100
run ID      30007757692
SHA-256     9811f269b4b4d0bda8f85d4ff53e3f5ba1a619e37dba5cdfb29fe924aa5216ec
```

The artifact contains `high-carrier-grid-certificate.json`, whose primitive point rectangles are the proof inputs.

## Mathematical reduction

For sample coordinates

\[
 s_i=\frac12+z_i
\]

and an exact vector `v`, L-6602 defines

\[
 h_i=\sum_j\frac{v_j}{z_i+\overline{z_j}},
 \qquad
 c_i=2\overline{v_i}h_i
\]

and proves

\[
 v^*Kv=\operatorname{Re}\sum_i c_iF(s_i).
\]

Thus the final proof check contracts primitive `F` rectangles directly; it does not form an interval matrix or trust a floating eigenvalue.

## Main results

### Two-point principals

All `134,940` two-point midpoint principal tests were positive. The smallest was approximately

```text
+1.9120449223919422e-08
```

at the two smallest horizontal offsets and central ordinate.

### Binary64 full-matrix artifact

The ill-conditioned `520 x 520` midpoint eigensystem reported 266 negative eigenvalues, the smallest approximately

```text
-1.4344035035461602e-08.
```

Every one of those 266 directions was frozen and replayed at high precision. All replayed midpoint values were positive.

The strongest replayed direction was frozen to 64-bit Gaussian dyadics and checked against the original primitive Arb rectangles. Its exact Rayleigh interval is

```text
[7.35826628421035027e-17,
 7.35826628421036506e-17].
```

This is a strict fixed-vector positivity certificate. It does not certify the full matrix.

### Barycentric localizers

Every nontrivial subset of the eight same-ordinate nodes was contracted at every ordinate:

```text
65 ordinates x 247 nontrivial node subsets = 16,055 intervals
strict negative count = 0
```

The tightest full eight-node row crosses zero at 128 Arb bits, but independent simultaneous Riemann--Siegel evaluation predicts the exact value is positive, approximately

```text
+1.16046739336509256711865861206548e-42
```

after conditioning normalization. This last value is numerical evidence only.

### Adaptive nullspace portfolio

One 256-bit Gaussian-dyadic portfolio remains unresolved by the 128-bit primitive rectangles:

```text
[-1.33096632425976470e-29,
 +1.33068619851804737e-29].
```

Its pointwise uncertainty ledger is highly concentrated. Recomputing the top 100 contributors independently moves the discovery estimate to a small positive value, but the remaining directed radius is still larger. L-6603 gives the exact optimal equal-cost refinement ordering for this fixed vector.

## Exact checker

`verify_full_pick_vector.py` uses only:

- Python integers;
- `fractions.Fraction`;
- exact base64 decoding of signed 64-bit vector numerators;
- JSON and SHA-256.

It verifies:

1. the exact vector digest;
2. overlap of both primitive assemblies at every point;
3. every exact shifted Pick denominator;
4. the L-6602 contraction;
5. the exact interval digest;
6. the claimed strict sign.

## Reproduction

Download and extract artifact `8564022100`, then run

```bash
python verify_full_pick_vector.py \
  path/to/high-carrier-grid-certificate.json \
  results/full-pick-audit.json
```

Expected verdict:

```text
CERTIFIED_POSITIVE_FIXED_VECTOR
```

Expected vector SHA-256:

```text
0086a055ea0de64e0fec2a6d94706af9c50708b9d1855b6527bf43efa5415589
```

Expected interval SHA-256:

```text
18094f31f79bdec84951ff1b8cf542842d71ae5c9b94ba3095a40bdc9844e452
```

## Proof boundary

Exact:

- the L-6602 finite algebra;
- vector and parameter reconstruction;
- the strict positive replay of the stored 64-bit vector from the supplied primitive Arb rectangles.

Discovery only:

- binary64 full-matrix eigenvalues;
- high-precision mpmath resolutions;
- hierarchical nullspace optimization;
- adaptive midpoint estimates.

No counterexample or `Z-####` candidate is produced.