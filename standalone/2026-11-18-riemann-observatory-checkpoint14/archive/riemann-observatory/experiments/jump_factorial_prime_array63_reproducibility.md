# Full-error enclosures for the tapered factorial target

These certificates enclose the squared approximation error for the prescribed $k=2$ array at three finite lengths. The partial sum and the upper bound on its infinite remainder use real ball arithmetic. The computation is unconditional and concerns the specified array. [Current calculator](code/jump_factorial_prime_array63_arb.py) · [Independent finite certificate audit](../audits/adversarial_reviews/jump_factorial_prime_array63_finite_qa.md)

## Quantities and tail

For each integer $n\ge1$, set $q=\lfloor n/2\rfloor$ and
$$
R_n=\log\frac{4^q(q!)^2}{n!},\qquad
a_d=\left(2\mathbf 1_{2\mid d}\Lambda(d/2)-\Lambda(d)+2\log2\,\mathbf 1_{d=2}\right)
     \left(1-\frac{\log d}{\log N}\right)\quad(2\le d\le N).
$$
With $A_N(1)=\sum_d a_d/d$, the anchored physical array is
$$
v_N(n)=\sum_d a_d(\lfloor n/d\rfloor-n/d),\qquad
E_N=\sum_{n\ge1}\frac{(R_n-v_N(n))^2}{n(n+1)}.
$$
The exact cell weight is $\int_n^{n+1}x^{-2}\,dx=1/[n(n+1)]$. The sparse prime-power sieve omits the zero coefficient at $d=N$. The jump sieve uses $v_N(0)=0$ and
$$
v_N(n)-v_N(n-1)=\sum_{d\mid n}a_d-A_N(1),\qquad
R_n-R_{n-1}=(2\mathbf 1_{2\mid n}-1)\log n .
$$
The two derivations establish the target and anchor in the same units. [Independent derivation](../audits/adversarial_reviews/generator63_tapered_prime_array_skeptic.md) · [Factorial-target derivation](../audits/adversarial_reviews/jump_factorial_prime_array63_proponent.md)

For even $n=2m$, $R_n$ is the sum of $\log(2j/(2j-1))$ for $1\le j\le m$. It lies between $0$ and $\log(2m)$ by induction. The following odd cell subtracts $\log(2m+1)$, so $|R_n|\le\log n$, which implies the requested coarser $|R_n|\le2\log n$. Also $|v_N(n)|\le S_N:=\sum_d|a_d|$. The majorant $(2\log x+S_N)^2$ increases for $x\ge1$. With $Y=X+1$ and $u=2\log Y+S_N$,
$$
0\le E_N-\sum_{n=1}^{X}\frac{(R_n-v_N(n))^2}{n(n+1)}
\le \int_Y^\infty (2\log x+S_N)^2\frac{dx}{x^2}
=\frac{u^2+4u+8}{Y}.
$$
The upper endpoint in each result adds the tail majorant to the finite sum with Arb and takes the outward endpoint. The lower endpoint comes from the finite sum alone. The same interval construction with the positive factor $\log N$ gives the scaled error.

## Certified intervals

The three rows below come from the two archived version 1 runs. A separate version 2 replay confirms the $N=10$ row.

| $N$ | Last summed cell $X$ | Full squared error $E_N$ | $\log(N)E_N$ |
|---:|---:|---|---|
| 10 | 4,000,000 | `[0.342801539918328691, 0.343111054662620134]` | `[0.789329715671346933, 0.790042399707614272]` |
| 30 | 8,000,000 | `[0.247656566621497315, 0.247904631616511935]` | `[0.842328865944475814, 0.843172583956001572]` |
| 100 | 16,000,000 | `[0.179598089981701525, 0.179908683595524940]` | `[0.827079769444138383, 0.828510105894476267]` |

The raw error intervals are disjoint and decrease over these three lengths. The scaled interval at $N=30$ lies above the scaled interval at $N=100$. The widths of the raw error intervals are each below 0.18% of their lower endpoints. These comparisons are finite statements. Convergence of the array as $N$ tends to infinity is the separate RH-equivalent question in the analytic derivation.

## Reproduction

Run from the Observatory root with Python and python-flint 0.9.0. The commands use the supplied installation in `/workspace/riemann-runtime`, which reports FLINT 3.6.0. Use the byte-preserved [version 1 source](code/history/jump_factorial_prime_array63_arb_v1.py) for the original results.

```bash
PYTHONPATH=/workspace/riemann-runtime python experiments/code/history/jump_factorial_prime_array63_arb_v1.py \
  --case 10:4000000 --case 30:8000000 --case 100:16000000 \
  --precision 160 --block-cells 32768 \
  --out experiments/results/jump_factorial_prime_array63_arb.json

PYTHONPATH=/workspace/riemann-runtime python experiments/code/history/jump_factorial_prime_array63_arb_v1.py \
  --case 10:4000000 --case 30:8000000 --case 100:16000000 \
  --precision 224 --block-cells 8191 \
  --out experiments/results/jump_factorial_prime_array63_arb_recheck.json
```

Version 2 computes the same squares with explicit ball multiplication, which can enclose a square even when an inexact ball is centered at zero. It reports nonfinite endpoint failures with case context. Low precision can produce much wider intervals. Reproduce the separate [version 2 replay](results/jump_factorial_prime_array63_arb_v2_n10.json) with the current calculator.

```bash
PYTHONPATH=/workspace/riemann-runtime python experiments/code/jump_factorial_prime_array63_arb.py \
  --case 10:4000000 --precision 160 --block-cells 32768 \
  --out experiments/results/jump_factorial_prime_array63_arb_v2_n10.json
```

The JSON stores exact dyadic endpoints as an integer mantissa times $2$ to the recorded exponent, alongside decimal endpoints rounded outward to 18 places. Its SHA-256 field pins the computing source. Each run uses one Arb thread and stores the sieve only for the current block. The direct cell checks compare the recurrence with the defining floor sum and compare the log jumps with independent log-gamma evaluations of the factorials. The checkpoints include the first cells, neighborhoods of $N$ and a sieve block boundary, the middle, and the final cells. A disjoint pair of balls stops the run. [Primary enclosure](results/jump_factorial_prime_array63_arb.json) · [Higher-precision recheck](results/jump_factorial_prime_array63_arb_recheck.json)

## Verification

The 224-bit finite-sum balls lie inside the corresponding 160-bit finite-sum balls. The enclosures for $A_N(1)$, $S_N$, the tail majorant, and both full-error quantities overlap between runs. All 48 selected cells per run passed both direct-value checks. Independently recomputing $\Lambda$ by trial factorization also agreed with all 140 coefficients across the three lengths, including the zero endpoints and the special term at $d=2$. The zero-polynomial case $N=2$, $X=1$ gave the exact zero finite sum.

These runs took 55.7 and 55.2 seconds on the Observatory machine. Peak process memory was 28,592 KiB and 27,004 KiB, respectively.

The independent version 2 run took 6.80 seconds for $N=10$, $X=4{,}000{,}000$, with peak process memory of 27,764 KiB. Its main dyadic enclosures overlap the original and give the same outward decimals in the table. The $N=30$ and $N=100$ rows retain the original version 1 executions.

| Artifact | SHA-256 |
|---|---|
| Version 1 source | `11ee04883dec90fae9f1bf878f178140c5c06445467117eb1ea85efe9e62e559` |
| Version 1 160-bit result | `4ca1192bda3438d0ebf5d680fa637341b920da4c0e8a657b25f2d9bbebd441cf` |
| Version 1 224-bit result | `9bcd06e799148309077b9befb6b11b7afac1ddc548eacb18998e37218667e8a9` |
| Version 2 source | `65e6445595292e30faeb241310a7610aa1dafe88c1a89261cb392f80abf551d3` |
| Version 2 160-bit $N=10$ result | `574efa5d18210fcb39165cffc55a94f935d3fb644681bf8dd86ffaf709b364d6` |
