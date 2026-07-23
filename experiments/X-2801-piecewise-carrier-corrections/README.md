# X-2801 — Exact piecewise-carrier correction and fixed-vector certificates

Experiment ID: `X-2801`  
Agent: `gpt56-04-c`  
Issue: #28  
Status: `PARTIAL / exact algebraic checkers`  
Date: 2026-07-23

## Question

Can the optimized D-0801 carrier screen be converted into a complete,
proof-producing fixed-vector sign certificate?

## Independent source reconstruction

L-2801 independently reduces the exact archimedean and pole terms to compact
cellwise Toeplitz formulas, without importing the X-0701/X-0801 numerical core.
The validation module checks those formulas at moderate carriers against
separately arranged expressions.

## Two exact correction certificates

### Self-contained fallback budget

L-2802 derives a deliberately coarse rational bound directly from Parseval,
Fourier total variation, digamma estimates, and finite cell transforms. At

```text
c = 10^11
K = 1024
T = 4709203636353.65
```

`verify_correction_budget.py` proves

```text
correction radius =
98759175269343099756340 /
79835755999127184820324325961

correction radius < 1/750000
```

This route is independent of the concurrent sharper operator argument.

### Exact specialization of the sharper operator bound

While this branch was in progress, the PR #44 base added L-0901, which obtains
a much sharper `O(1/T)` uniform operator bound by integrating the oscillatory
archimedean residual by parts. L-2803 independently checks its target constants
using exact rational arithmetic.

`verify_variation_budget.py` proves

```text
variation radius =
136091541158257193750 /
292731105330133011007855861857

variation radius < 1/2000000000
```

The exact value is approximately `4.6490290468e-10`.

PR #44's empirical leading margin is approximately `2.6896626427e-4`, about
`5.785e5` times the exact variation radius. That leading value is not a directed
interval and is not promoted by this experiment.

## Sharded fixed-vector checker

L-2804 and `verify_fixed_vector_certificate.py` implement the quantitative
composition needed by a real prime producer.

Schema:

```text
riemann.piecewise-carrier-fixed-vector.v1
```

The certificate contains:

- one exact dyadic complex vector;
- exact vector and parameter SHA-256 fingerprints;
- a rational interval for `alpha(T)`;
- scalar directed intervals for `x^*S_r x` from multiple prime shards;
- contiguous half-open segment ranges;
- prime and higher-power counts;
- exactly one separately flagged higher-prime-power stream.

The checker computes the exact vector norm, sums the shard intervals, forms

```text
alpha_interval * norm_squared - complete_prime_interval,
```

recomputes the L-2803 correction radius, widens by

```text
correction_radius * norm_squared,
```

and returns a strict positive, strict negative, or unresolved fixed-vector
verdict.

It rejects gaps, overlaps, mixed vectors, mixed parameters, duplicated or
missing higher-power streams, count mismatches, zero vectors, malformed types,
and intervals widened through zero.

Segment coverage proves consistency of the declared finite ledger; it does not
prove correct primality enumeration or analytic interval provenance inside a
shard. Those remain producer contracts.

## Checker schemas

```text
riemann.piecewise-carrier-correction-budget.v1
riemann.piecewise-carrier-variation-budget.v1
riemann.piecewise-carrier-fixed-vector.v1
```

All checkers use Python integers, `fractions.Fraction`, JSON, and, for integrity
binding, SHA-256. They call no prime routine, special function, FFT,
trigonometric function, eigensolver, or floating-point operation.

## Reproduction

```bash
python -m unittest discover -s tests -v
python verify_correction_budget.py \
  certificates/target-budget-c1e11.json
python verify_variation_budget.py \
  certificates/target-variation-budget-c1e11.json
python verify_fixed_vector_certificate.py \
  certificates/synthetic-fixed-vector-negative.json
```

The committed transcripts contain 30 passing tests in total. They cover:

- exact target fractions and strict threshold comparisons;
- safe synthetic positive and negative intervals;
- zero-touch rejection;
- schema and integer-type failures;
- non-power-of-two cell handling;
- cellwise autocorrelation endpoints;
- compact versus finite-transform pole evaluation;
- the `K=1` compact archimedean formula in two algebraic arrangements;
- fixed-vector digest binding;
- parameter digest binding;
- segment gaps and overlaps;
- higher-power-stream uniqueness;
- term-count consistency;
- zero-vector rejection.

Synthetic fixtures test checker logic only and are not mathematical candidates.

## Files

- `verify_correction_budget.py` — self-contained fallback rational checker;
- `verify_variation_budget.py` — exact specialization of L-0901;
- `verify_fixed_vector_certificate.py` — sharded fixed-vector merger/checker;
- `compact_corrections.py` — independent non-rigorous formula validation;
- target budget requests and exact outputs;
- synthetic fixed-vector positive, negative, and zero-touch controls;
- exact retained test transcripts;
- `tests/` — adversarial arithmetic, formula, coverage, and integrity checks.

## Classification

- L-2801 formulas: `PROPOSED` pending independent review.
- L-2802 fallback inequality: `PROPOSED` pending independent review.
- L-0901 sharper operator inequality: concurrent `PROPOSED` dependency.
- L-2803 rational specialization: `PROPOSED` pending review of L-0901.
- L-2804 interval composition: `PROPOSED`.
- Checker arithmetic and retained fractions: exact finite computation.
- Compact mpmath controls: ordinary high precision, not certified.
- PR #44 leading margin: empirical and never used as proof input.
- Counterexample status: none.

## Remaining proof bottleneck

The exact consumer is complete. The missing object is the analytic producer:

1. preserve the `c=10^11`, `K=1024` discovery vector as dyadic data;
2. enclose each `T log(q)` phase with certified range reduction;
3. evaluate one fixed-vector scalar term per prime power with balls;
4. accumulate one directed interval per coverage-checked shard;
5. emit a rigorous `alpha(T)` interval;
6. pass the result to the fixed-vector checker.

M-2801 records the fail-closed producer protocol. Conditional on L-0901,
separation from zero by `1/2000000000` is sufficient at the current target.
