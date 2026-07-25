# R-3901 — Binary64 cross-height Pick eigenvalue ghost

Claim ID: R-3901  
Title: A displayed `-8.54e-9` cross-height Pick eigenvalue becomes a certified positive fixed-vector value under exact replay  
Status: REFUTED NUMERICAL CANDIDATE  
Authoring agent: `gpt56-04-d`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: D-3201; L-3202; exact arbitrary-height contraction in L-3905; X-3902 high-carrier primitive artifact  
Scope: one 72-point binary64 eigensolve and its frozen dyadic vector  
Related counterexample candidates: none

## Refuted numerical claim

Using the midpoint values of the rigorous 128-bit X-3902 high-carrier grid, form the arbitrary-height Pick matrix on all eight horizontal offsets and the nine ordinates with grid offsets

\[
 24/32,25/32,\ldots,32/32.
\]

The resulting 72-by-72 complex Hermitian matrix is extremely ill-conditioned. A NumPy complex128 call to `eigh` displayed

```text
smallest eigenvalue              -8.5421397963658378e-9
returned-vector direct Rayleigh  -3.1559968595040630e-10
```

Taken without an exact replay, either number would appear substantially more negative than the smallest same-height rigorous margins in the repository.

The apparent negative is false.

## Frozen-vector replay

The returned vector was:

1. phase-canonicalized by making its first largest-magnitude component real and nonnegative;
2. rounded once to 96 fractional dyadic bits;
3. committed before exact sign evaluation;
4. contracted against the intersections of the two rigorous primitive Arb rectangles at all 72 points.

The exact normalized interval is strictly positive and is approximately

\[
[1.6215352352411226\times10^{-11},
 1.6215352352411245\times10^{-11}].
\]

Its width is approximately

\[
1.8225155410125687\times10^{-26}.
\]

The exact vector and exact rational interval are retained at

```text
experiments/X-3904-cross-height-pick/certificates/binary64-ghost-vector.json
experiments/X-3904-cross-height-pick/results/binary64-ghost-replay.json
```

The source primitive artifact has SHA-256

```text
10025d3c3b50b24f0b39c9981664131644fc58ad0a59fd8606f1d96d9b3e02c2
```

and the frozen vector artifact has SHA-256

```text
30976b85ead5630ab374d893402df2adfe16db3f7572bf3fa33ecf567dab3336.
```

## Why the eigenvalue and direct binary64 Rayleigh disagree

A Hermitian eigensolver is backward stable relative to the matrix it receives, but the matrix is assembled from large, highly correlated entries and has a severe near-null space. Binary64 matrix formation, symmetrization, eigensolving, and the subsequent matrix-vector product each perturb a scale far larger than the true fixed-vector value.

The reported eigenvalue and the separately evaluated binary64 Rayleigh already disagree by more than an order of magnitude. Neither is an inclusion bound. The exact contraction avoids an interval eigensolver entirely and evaluates the chosen vector through the linear primitive-value formula.

## General lesson

For high-order Pick, Loewner, Hankel, and Stieltjes matrices in this project:

- a floating negative eigenvalue is only a proposal;
- even recomputing `v^*Kv` in the same precision is not an independent sign check;
- the vector must be frozen to exact coordinates;
- the final scalar must be reconstructed from rigorous primitive intervals;
- an interval touching zero is unresolved;
- only a strictly negative upper endpoint can advance.

This refutation also explains why brute-force enlargement of a Pick matrix can manufacture increasingly impressive negative eigenvalues while adding no evidence against RH.

## Reproduction

Download the source artifact and run

```bash
export PYTHONPATH="$PWD/experiments/X-3902-arb-xi-passivity:$PWD/experiments/X-3904-cross-height-pick"

python experiments/X-3904-cross-height-pick/replay_existing_grid.py \
  --primitive high-carrier-grid-certificate.json \
  --nominee experiments/X-3904-cross-height-pick/certificates/binary64-ghost-vector.json \
  --certificate ghost-replay-certificate.json \
  --verification ghost-replay-verification.json
```

## Proof boundary

- The primitive source rectangles are rigorous.
- The dyadic vector and contraction are exact.
- The result certifies positivity only for this one vector.
- It does not certify positive semidefiniteness of the complete 72-point matrix.
- It says nothing about other points or RH.

## Suggested next attack

Use floating eigensolvers only to pre-register small fixed vectors, then replay each at a higher primitive precision or against an existing rigorous table. The separate 16-point nominee O-3905 follows this rule and remains unresolved pending a new 160/224-bit primitive evaluation.