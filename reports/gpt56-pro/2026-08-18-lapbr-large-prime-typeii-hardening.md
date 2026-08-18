# Large-prime parity boundary: no-go, Bellman rewrite, and Type-II frontier

## Result

The requested residual attack produces a decisive correction rather than a
positive proof of `LAPBR67`.

The small-prime cube from PR #578 is positive. However, its adaptive depth is
only `O(log log log X)`, while the total reciprocal mass of active rough primes
is `~log log X`. A product-safe elementary symmetric-sum estimate shows that the last
odd layer dominates. The complete depth current is eventually negative, so the
large-prime residual satisfies

```text
large-prime residual < - small-prime cube < 0.
```

Thus `LAPBR67` cannot be the missing theorem.

## Repair

The source must be resummed across all large-prime depths. The packet proves:

1. the **complete** small-prime cube through `Z=(log X)^(1/4)` is positive;
2. every large-prime history has one exact largest-prime owner;
3. the full source is small cube minus one largest-prime Bellman budget;
4. the terminal range `p>X/Z` is `o(small cube)`;
5. every remaining term is one signed prime-versus-Mobius Type-II correlation.

The exact remaining theorem is `BLPTE67`:

```text
balanced Type-II Bellman budget
    <= complete small-prime cube - terminal Type-I budget.
```

It keeps all signs, activation sides, and owners. It is not a large-sieve norm.

## Scientific status

```text
LAPBR67                         refuted
complete small-prime cube       proved positive
largest-prime Bellman identity  proved exact
terminal Type I                 closed
BLPTE67                         open / RH-bearing
RH                              unproved
```
