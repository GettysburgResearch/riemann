# Independent replay of `X-91125` — `P_79` one-prime inherited-row positivity

Date: 2026-08-13  
Source commit: `4b8b4306142e92d66bc27f7eda10f64a703ed3d8`  
Source checker blob: `86bf8bcd5b5361a39d8fdccd3e809be4832cf7d3`  
Source result blob: `7fd799e03c5f702f5418c203fc1ea2f2454ae6a0`  
Independent environment: CPython `3.13.5`  
Verdict: **PASS — retained mathematical outputs reproduced exactly**

## Command

```bash
python3 experiments/X-91125-p79-one-prime-row-splice/verify.py
```

The source checker was reconstructed byte-for-byte from the frozen GitHub blob
and executed independently.

## Reproduced result

```text
PASS_P79_ONE_PRIME_ROW_SPLICE
```

All mathematical output fields agree with the retained result:

```text
global states                    4,194,304
beta                             0.0013424741937663638
maximum absolute M prefix        1.4292396711387123 at 341
maximum absolute E prefix        1.3350166016823197 at 2717
maximum geometry mass            1.2150313676695992 at j=82
maximum KR geometry bound        3.8653634562569104 at j=82
p=83 finite margin               38381/90000
large-prime analytic margin      18779/1417500
crossover                        328/9
```

The independent runtime was approximately `10.93` seconds with maximum resident
memory approximately `123 MB`; runtime is intentionally not compared to the
retained nondeterministic timing field.

## Scope

This replay materially supports the claim

\[
 D_{Pp}(py;j)>0
 \qquad(p\ge83,\ 1\le y<83,\ 2\le j\le y).
\]

It does not certify:

```text
rows j>y;
the terminal P79 projection;
the one-use frontier/collar assembly;
the score recurrence;
RH.
```

```text
checker integrity                         REPRODUCED
retained directed extrema                 REPRODUCED
exact finite and analytic margins         REPRODUCED
inherited-row theorem                     SUPPORTED / ANALYTIC REVIEW STILL REQUIRED
complete factor-54 proof                  NOT CERTIFIED
Riemann Hypothesis                        UNPROVEN
```
