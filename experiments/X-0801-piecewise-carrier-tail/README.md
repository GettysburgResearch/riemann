# X-0801 — Complete-tail piecewise carrier search

Experiment ID: X-0801  
Agent: `gpt56-04-b`  
Issue: #29  
Status: EMPIRICAL  
Date: 2026-07-23

## Research question

Can the carrier-localized Weil search be scaled to hundreds of millions of
complete prime-power terms and a much richer envelope without using a truncated
prime matrix, and does the resulting leading operator become negative?

## Method

D-0801 partitions the compact physical support into equal cells and uses an
autocorrelation carrier whose real-axis spectral test is nonnegative.  L-0801
reduces the complete finite prime side to `K` complex lag coefficients and a
Hermitian Toeplitz matrix.

For `q=p^a<=c`, put `r=K*log(q)/log(c)`.  The term is deposited linearly into the
two neighboring integer lags.  The implementation streams primes in contiguous
integer segments and enumerates higher powers separately.

`stream.py` emits mergeable shards.  `merge.py` rejects gaps, overlaps, parameter
mismatches, and missing or duplicated higher-power streams before computing the
leading eigenvalue.

## Reproduction

Small complete run:

```bash
python stream.py \
  --cutoff 1000000 \
  --carrier 3157430112465.8695095 \
  --cells 256 \
  --segment-size 200000 \
  --include-higher-powers \
  --output shard.json
python merge.py shard.json --output result.json
```

A large run can be split, for example:

```bash
python stream.py --cutoff 10000000000 --carrier 3157430112465.8695095 \
  --cells 1024 --segment-size 20000000 --start-segment 0 --end-segment 125 \
  --output shard-0.json
```

Continue with adjacent ranges through the declared `total_segments`; add
`--include-higher-powers` to exactly one shard, then merge every shard together.

Tests:

```bash
python -m unittest discover -s tests -v
```

Six tests pass.

## Main result

The complete `K=1024`, `c=10^10` leading margin was

```text
+0.010646422368668418
```

with all 455,062,595 prime-power terms included.  The result is positive and
therefore not a candidate counterexample.  See
`results/decade-continuation.json` and O-0801.

## Source and result digests

| file | SHA-256 |
|---|---|
| `stream.py` | `ca10e60fc2b42555aa1425da55ffc9c0329323b481a6f78151e631d4a619532f` |
| `merge.py` | `ac5f277e07120b9ef2705f16b2a9f8c09d9b28e0937a71261edeb382e3bbf7f1` |
| `tests/test_stream.py` | `8b20c59e87b3fc06e0a9633d8abe0910ea98b125e2fb04acf1fa9f013f77b6a1` |
| `results/decade-continuation.json` | `96c70782b248fb3bccb77e1c3f17551738f8ac055505077cc1cfdb914ad32410` |
| `results/tests.txt` | `60c8c9df1eb4c0dbe1b06d1743b475d4b79f768decb3b4bde6bf23d320bc7dbe` |

## Numerical environment

The discovery session used CPython 3.13, NumPy 2.3, Linux x86-64.  Phase
products and reduction used NumPy `longdouble`; trigonometry, accumulation, and
eigensolving used binary64.

## Proof boundary

- Complete prime coverage is enforced, but numerical values are not intervals.
- The finite prime Toeplitz formula is exact conditional on the project
  explicit-formula sign and normalization.
- The displayed margin uses the high-carrier archimedean scalar, not the exact
  D-0801 archimedean and pole matrices.
- A negative output would be a nomination for Issue #28, never an immediate RH
  counterexample.

## Next attack

Build exact cellwise archimedean/pole blocks and a dyadic fixed-vector checker,
then accumulate several cell resolutions in the same complete prime pass while
searching adaptive cutoff intervals.
