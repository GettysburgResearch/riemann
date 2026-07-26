# O-9311 — Unverified extensions of the zero-anchor moment method

Status: **UNVERIFIED RESEARCH NOTE**  
Authoring agent: `gpt56-01-o`  
Date: 2026-07-26

Nothing in this file is used by L-9311, X-9309, or any counterexample status.

## 1. General positive-node Geronimus recurrence

For an additional positive node `w`, zero-extending an old response portfolio
suggests the exact recurrence

```text
a_k = b_(k+1) + w b_k.
```

Thus all new moments are affine functions of one new scalar. The corresponding
Hankel matrices are rank-one affine pencils. A complete theorem should derive
the exact admissible interval for that scalar and an explicit polynomial
witness at either endpoint.

Missing obligations:

- a clean orientation-independent derivation of the response-map identity;
- an exact interval-pencil certificate handling singular endpoint blocks;
- proof that the proposed witness extractor is complete in degenerate cases.

## 2. Continued-fraction scheduling of several new nodes

Iterating the one-node recurrence resembles a finite Stieltjes/Geronimus
continued fraction. It may turn several new direct-xi values into a sequence of
scalar Schur gates rather than one large moment SDP.

Missing obligations:

- exact multi-step normalization and sign conventions;
- a proof that interval widening does not destroy equivalence;
- a rational witness reconstruction from the first failed gate.

## 3. Critical-line anchor as a center-ranking statistic

For fixed old moments, the zero-anchor Schur gap

```text
b0 - v^T A^-1 v
```

is a single scalar measure of how close an ordinate is to violating the full
next-degree cone. It may be much cheaper to rank candidate ordinates by an
ordinary approximation of this gap before paying for a full directed table.

Missing obligations:

- a stable discovery implementation that does not confuse barycentric
  cancellation with a small true gap;
- a quantitative rule for escalating only reproducible candidates;
- evidence across independent high-height windows.

## 4. Matrix-valued zero anchors

Using several horizontal primitive families at the same critical-line anchor
may produce a block moment problem whose first failed Schur complement yields a
matrix-valued polynomial-square witness. This could escape scalar closures such
as PR #116.

Missing obligations:

- an RH-valid block canonical-product or Gram representation;
- exact block count deflation without double counting;
- a finite rational block-SOS certificate.

## 5. Endpoint sensitivity dual

The coefficient of the new critical-line residual in `b0` is enormous. A dual
formulation may isolate the exact required width of the `x=0` rectangle and
thereby choose the minimum FLINT precision before production.

Missing obligations:

- a rigorous decomposition of every old-moment and logarithm uncertainty;
- a proof that Decimal-directed accumulation meets the resulting budget;
- independent reproduction with a different contraction order.
