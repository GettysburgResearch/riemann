# X-97700 - LAPBR large-prime algebra and negative-control replay

Run:

```bash
python3 verify.py --output results/verification.json
```

The replay checks:

- the exact noncommutative Duhamel identity;
- exact largest-prime Bellman telescoping;
- unique largest-prime ownership for every finite subset;
- the Type-I/Type-II partition;
- an exact rational Poisson-layer fixture in which the adaptive residual is
  more negative than the positive small cube;
- mutation rejection for a lost sign, duplicated owner, and wrong cutoff.

It replays the exact elementary-symmetric collision inequality, but does **not** numerically prove the Mertens asymptotics or `BLPTE67`. Those boundaries are explicit in the result JSON.
