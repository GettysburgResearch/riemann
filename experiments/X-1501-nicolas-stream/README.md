# X-1501 — Restartable Nicolas primorial search

Experiment ID: X-1501  
Issue: #15  
Agent: `gpt56-02-c`  
Branch: `agent/gpt56-02-c/15-nicolas-streaming-search`  
Status: EMPIRICAL; no counterexample candidate  
Created: 2026-07-22

## Research question

Can a one-dimensional streaming search find an index `k>=2` for which

\[
 \frac{N_k}{\varphi(N_k)}\le e^\gamma\log\log N_k,
 \qquad N_k=\prod_{j\le k}p_j,
\]

thereby producing a finite Nicolas-criterion witness against RH?

## Proof boundary

`scan.cpp` is discovery code. The sieve is exact integer code, but the two
transcendental sums and the final sign use ordinary `long double`. A nonpositive
output is only a candidate. A positive finite range is not evidence for RH.

## Files

- `scan.cpp` — segmented, restartable prime stream and logarithmic recurrence.
- `tests/test_small.py` — restart determinism and independent 80-digit control.
- `results/scan-through-1e10.json` — compact retained endpoint and checkpoint table.
- `results/tests.txt` — validation transcript.

## Mathematical recurrence

Write

\[
 \theta_k=\sum_{j\le k}\log p_j,
 \qquad
 A_k=\prod_{j\le k}\frac{p_j}{p_j-1}.
\]

Since `log N_k=theta_k`, the Nicolas inequality is equivalent to

\[
 d_k:=\log A_k-\gamma-\log\log\theta_k>0.
\]

The code updates

\[
 \theta_{k+1}=\theta_k+\log p_{k+1},
 \qquad
 \log A_{k+1}=\log A_k-\log(1-1/p_{k+1}).
\]

It never constructs the enormous primorial.

## Build and control tests

```bash
g++ -O3 -std=c++17 -Wall -Wextra scan.cpp -o scan
python -m unittest discover -s tests -v
```

Run and resume blocks:

```bash
./scan 1000000000 state.txt block-1e9.json
./scan 2000000000 state.txt block-2e9.json
```

The state file is a discovery checkpoint, not a proof certificate.

## Main result

The retained run processed all 455,052,511 primes through `10^10`. At the last
prime `9,999,999,967`, the observed logarithmic defect was approximately

```text
8.52461732729062e-7
```

and the normalized ratio was approximately

```text
1.0000008524620961
```

No floating sign failure occurred. The defect decreased at every stored prime
transition after `k=2` at this working precision.

## Validation

The tests compare a one-shot scan to `10^6` with a split/resumed scan, recover
`pi(10^6)=78,498` and last prime `999,983`, and compare the accumulated values
with independent 80-digit mpmath sums.

## Limitations

- No outward rounding or interval arithmetic.
- No exact hash/certificate for each billion-prime block.
- Euler's constant is a decimal long-double literal.
- The original Nicolas theorem still needs independent source-level review.
- The first possible failure, if RH is false, has no practical upper bound.

## Suggested next attack

Add exact block provenance and an interval accumulator. The smallest retained
margin is still large relative to the control-run rounding discrepancy, so the
main value of immediate certification is infrastructure rather than candidate
promotion.
