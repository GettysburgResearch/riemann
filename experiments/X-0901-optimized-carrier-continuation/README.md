# X-0901 — Optimized piecewise-carrier continuation

Experiment ID: `X-0901`  
Status: `EMPIRICAL_NOT_CERTIFIED`  
Agent: `gpt56-01-c`  
Issue: #42  
Stacked dependency: X-0801 / draft PR #37

## Question

Does the unusually low D-0801 carrier basin near

```text
T = 4709203636353.65
```

cross the high-carrier leading level when the complete prime-power cutoff or piecewise-envelope resolution is increased?

This experiment also asks whether the same height is anomalous for the independent Lagarias positive-real criterion `Re(xi'/xi)>0`.

## Classification

The prime stream has exact integer coverage metadata, but matrix arithmetic is ordinary floating point. The displayed matrix is

```text
log(T/(2*pi))/(2*pi) I - S_K(T,c)
```

and omits the exact D-0801 archimedean and pole corrections. Therefore:

- a positive output proves nothing beyond the numerical cell;
- a negative output would still be only a nomination;
- no output in this directory is an RH proof or counterexample.

## Complete cutoff ladder

`results/continuation-summary.json` records complete prime-power evaluations at `c=10^8,10^9,10^10,10^11`, including every prime and every higher prime power. The smallest retained value was

```text
+2.6896626427230785e-4
```

at `c=10^11`, `K=1024`. No negative occurred.

The `c=10^11` run used:

```text
segment size     20,000,000 integers
segments         5,000
shards           50 contiguous ranges of 100 segments
primes           4,118,054,813
higher powers    28,156
total terms      4,118,082,969
```

Exactly one shard contained the higher-prime-power stream. Merging was allowed only after parameter equality, contiguous coverage, and unique special-stream checks.

## Reproduction

The complete stream and merger are inherited unchanged from X-0801:

```bash
python ../X-0801-piecewise-carrier-tail/stream.py \
  --cutoff 100000000 \
  --carrier 4709203636353.65 \
  --cells 1024 \
  --segment-size 20000000 \
  --start-segment 0 --end-segment 5 \
  --include-higher-powers \
  --output shard.json

python ../X-0801-piecewise-carrier-tail/merge.py shard.json \
  --output merged.json
```

For larger cutoffs, partition the declared segment range into disjoint shards. Only one shard may use `--include-higher-powers`. The X-0801 merger fails closed on a gap, overlap, parameter mismatch, incomplete range, or duplicated/missing higher-power stream.

Audit the compact committed summary with:

```bash
python analysis.py results/continuation-summary.json
python -m unittest discover -s tests -v
```

## Resolution and carrier audits

At `c=10^10`, increasing `K` from 1,024 to 2,048 changed the margin by only about `4.90e-6`, indicating finite-resolution saturation for equal cells at this point.

The `K=1024` leading vector was frozen and the complete prime Rayleigh moments through order six were accumulated. The direct value was reconstructed to about `8.9e-16`. `analysis.py` implements the remainder

```text
W exp(eta) eta^(R+1)/(R+1)!,  eta=|delta| log(c),
```

used to reject polynomial-only carrier crossings. No local fixed-vector negative was found.

## Independent xi cross-check

`xi_crosscheck.py` contains two distinct discovery layers:

1. a fast no-remainder Riemann--Siegel curvature screen;
2. simultaneous high-precision Riemann--Siegel evaluation of `zeta` and `zeta'`, inserted into the corrected `xi'/xi` formula from D-3201.

The deterministic 401-point grid on `T+-4` found no negative curvature. At its minimum, all three high-precision scalar controls in `results/xi-crosscheck.json` had positive real part. They are not interval certificates.

Example:

```bash
python xi_crosscheck.py curvature 4709203636353.6309
python xi_crosscheck.py point 4709203636353.6309 \
  --sigmas 0.5001 0.501 0.505 --dps 35
```

## Files

- `analysis.py` — summary validation and fixed-vector Taylor bounds;
- `xi_crosscheck.py` — independent Riemann--Siegel/`xi'/xi` reconnaissance;
- `results/continuation-summary.json` — complete cutoff and resolution ladder;
- `results/xi-crosscheck.json` — deterministic high-height pointwise audit;
- `tests/test_analysis.py` — regression and invariant checks;
- `SHA256SUMS` — digests of retained compact results.

## Main limitations

- phase reduction, accumulation, and eigensolving are not directed rounded;
- exact D-0801 archimedean and pole blocks remain absent;
- the explicit-formula and admissibility interface remains proposed;
- the fast curvature screen omits the Riemann--Siegel remainder;
- finite positive values do not imply positivity elsewhere.
