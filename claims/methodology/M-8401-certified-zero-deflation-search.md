# M-8401 — Proof-producing certified-zero-deflation search

Proposal ID: M-8401  
Status: PROPOSED  
Authoring agent: `gpt56-06-e`  
Created: 2026-07-25  
Dependencies: L-8401–L-8404; Issue #39 Arb primitives; PR #50 uncertainty closure; PR #60 conic portfolios

## Objective

Turn independently certified critical-line zeros from a positive background into
subtractive proof data for `xi'/xi` passivity searches. The final proof object is
not a fitted zero model. It is a direct primitive `F=xi'/xi` enclosure minus
rigorous lower contributions from actual certified line-zero counts.

## Discovery and proof boundary

### Discovery-only layer

Ordinary Riemann-Siegel or Hardy-Z arithmetic may:

- nominate short sign-change brackets;
- estimate local zero density;
- choose scalar sample points;
- choose same-height or cross-height Pick point clouds;
- optimize a floating vector, PSD Gram portfolio, or matrix-deflation target.

None of these decisions enters the final implication until exact rationalization
and directed replay.

### Proof layer

1. Freeze exact rational/dyadic endpoints for every Hardy-Z bracket.
2. Certify opposite nonzero endpoint signs or use another rigorous lower zero
   count.
3. Require pairwise disjoint bins or an exact multiplicity allocation.
4. Evaluate exact passivity points with the proof-grade Issue #39 producer.
5. Reconstruct scalar, fixed-vector, or matrix deflation with a standard-library
   exact checker.
6. Accept only a residual interval whose upper endpoint is strictly negative.
7. Bind every primitive, zero-count bin, logical gate, and checker output by
   digest.
8. Reproduce any negative with a separately structured directed backend.

## Search ladder

### Stage A — scalar deflation

For each exact `(x,T)`:

\[
 R_{\rm scalar}
 =\operatorname{Re}F(1/2+x+iT)
 -\sum_rm_r\frac{x}{x^2+D_r^2}.
\]

This is the cheapest search and requires only real `F` intervals.

### Stage B — fixed-vector Pick deflation

Choose exact same-height or cross-height points and vector `v`. Contract the Pick
matrix first, then enclose primitive values. For each zero bin, enclose
`Phi_v(I)` and subtract a lower modulus-square contribution.

Rank vectors by a normalized residual moat after both primitive and zero-bin
uncertainty. Large raw vector scales are not a ranking criterion.

### Stage C — whole-matrix deflation

Construct Loewner-lower zero-bin Gram blocks from L-8403. Search the residual
matrix through:

- exact fixed vectors;
- exact positive Gram portfolios;
- whole-matrix negative or positive closure;
- robust conic portfolios over shared primitives.

The zero count is certified once and may be reused by many vectors.

### Stage D — adaptive tightening

If a finalist is unresolved:

1. rank primitive `F` points by their exact contribution to interval width;
2. rank zero bins by loss from bin width;
3. refine only the highest-impact `F` points or Hardy-Z brackets;
4. stop as soon as the remaining worst-case radius cannot change the sign.

## Local-zero certification choices

- **Hardy-Z sign change:** lower count one, no simplicity or uniqueness needed.
- **Interval Newton:** narrow unique-zero bin when a sharper subtraction is worth
  the derivative cost.
- **Argument principle:** exact count in a small rectangle intersecting the line;
  must prove the counted zeros lie on the critical line before scalar deflation.
- **Turing/zero-count difference:** useful for bulk completeness, but not required
  for the basic method.

The cheapest sound lower count should be preferred.

## Certificate schemas

### Primitive passivity record

```json
{
  "id": "F-point-...",
  "s_exact": {"x": [1, 1024], "t": [0, 1]},
  "f_via_xi": {},
  "f_via_parts": {},
  "zeta_abs_lower": {},
  "producer_fingerprint": "..."
}
```

### Zero-bin record

```json
{
  "id": "Z-bin-...",
  "lower": [0, 1],
  "upper": [0, 1],
  "count_lower": 1,
  "kind": "hardy-z-sign-change",
  "endpoint_intervals": [],
  "producer_fingerprint": "..."
}
```

### Final deflated record

The X-8401 checker consumes exact rational versions of these records, reconstructs
every contribution, and emits the residual interval and strict moat.

## Uncertainty ledger

Quantitative channels include:

- primitive `F` rectangles;
- zero-bin endpoints;
- zero counts, when greater than a sign-change lower count;
- `Phi` interval or matrix-bin approximation loss;
- exact vector rationalization;
- any parameter-cell movement.

Logical gates include:

- D-3201/L-3201 or D-3201/L-3202;
- completed-xi normalization;
- each Hardy-Z or alternative zero-count theorem;
- zero-bin disjointness;
- analytic-domain and denominator exclusions.

A numerical moat cannot compensate for a blocking logical gate.

## Strategic targets

1. Cross-height Pick clouds from PR #70, because they retain complex phase and can
   design `Phi_v` to be large at certified line zeros.
2. Direct scalar points near passivity local minima, after local Hardy-Z bins are
   certified.
3. New ordinate windows rather than further optimization on the exact feature
   tables closed by PR #67.
4. Direct-xi modulus candidates from PR #76: their Hardy-Z scans and xi
   primitives can share a local-zero producer with this route.

## Success criterion

A route advances only when the exact checker gives

```text
CERTIFIED_NEGATIVE_DEFLATED_WITNESS
```

with a positive robust moat, every zero-bin count is independently certified,
and the primitive special-function values are reproduced by a second directed
implementation.

## Failure value

A nonnegative residual is still useful. It quantifies how much certified
critical-line background was removed and prevents future agents from mistaking
that local positive mass for evidence that no off-line component could be
present.
