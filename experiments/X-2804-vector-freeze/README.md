# X-2804 — Deterministic preservation of a carrier discovery vector

Experiment ID: `X-2804`  
Agent: `gpt56-04-c`  
Issue: #28  
Status: exact dyadic export from empirical shards  
Date: 2026-07-23

## Question

Can a complete X-0801/X-0901 prime stream be converted immediately into a
canonical, machine-readable, exact dyadic vector so that the proof pass never
depends on an uncommitted eigensolver object?

## Result

`freeze_vector.py` accepts the original coverage-checked prime shard JSON files,
reconstructs their complete Hermitian Toeplitz midpoint matrix, computes its top
eigenpair, canonicalizes the arbitrary global phase, and exports exact dyadic
real and imaginary numerators.

The phase convention is deterministic:

1. choose the first largest-magnitude component;
2. rotate it to be real;
3. require it to be nonnegative.

Each binary64 component is rounded to the nearest dyadic at a user-declared
fractional bit depth, with exact ties-to-even integer arithmetic. The default is
96 fractional bits; the PR #44 target request asks for at least 80.

The exported object is bound to the D-0801 normalization digest

```text
65bacffb2e03518fa6ffb771f79d276b0018f7a22a1b17f3a7566d119024c8be
```

and records:

- exact dyadic coordinates;
- canonical vector SHA-256;
- complete coverage counts;
- empirical eigenvalue and residual;
- midpoint rounded-vector norm and prime Rayleigh value;
- rounding displacement;
- numerical backend classification.

## Reproduction

Given the complete original shard files:

```bash
python freeze_vector.py shard-*.json \
  --scale-bits 96 \
  --output frozen-vector.json
```

Tests:

```bash
PYTHONPATH=. python -m unittest discover -s tests -v
```

Seven tests cover ties-to-even rounding, phase canonicalization, Hermitian
orientation, shard-order invariance, complete coverage, and higher-power-stream
uniqueness.

## The PR #44 provenance failure

PR #44's committed `c=10^11` summary contains the largest eigenvalue and residual
but not:

- the 1,024-component eigenvector;
- the 1,024 merged complex Toeplitz coefficients;
- the original 50 shard files.

Its inherited merger calls `numpy.linalg.eigvalsh`, which returns eigenvalues
only. Therefore the historical vector is not mathematically reconstructible
from the committed scalar eigenvalue. X-2804 resolves the preservation mechanism,
but recovery of that exact historical discovery object requires either the
original uncommitted shards or a complete regeneration of the stream.

A blocking artifact request has been posted on PR #44. If the shards are
recovered, this script produces the requested vector immediately. If they are
not, a regeneration must use this exporter in the same command pipeline so the
vector is committed before temporary shard deletion.

## Proof boundary

- The dyadic vector itself is exact.
- The eigensolve and rounded-vector diagnostic are ordinary complex128
  computations.
- The proof does not need to preserve the floating eigenvector's sign: the
  directed producer evaluates the exported exact dyadic vector itself.
- Correct prime enumeration, phase evaluation, and accumulation remain separate
  producer contracts.
- A SHA-256 digest is an integrity binding, not analytic evidence.

## Process rule

No future complete carrier run should be considered reproducible unless it
retains at least one of:

1. all merged Toeplitz coefficients;
2. all original shard files; or
3. a canonical dyadic finalist vector plus its exact regeneration inputs.
