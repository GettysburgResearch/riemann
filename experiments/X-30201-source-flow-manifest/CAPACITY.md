# Central-capacity addendum

`verify_capacity.py` authenticates the exact positive central-tree layer cake for
decreasing divisor sources.

It verifies:

```text
eta source / central-tree load equality       44,850 cases
root capacity A_k-B_k, not A_k                10,000 cases
general decreasing source layer cakes          6,318 cases
```

For the eta source `c_n=1/n`, the canonical positive realization places

```text
A_k-B_k = 1/[2k(2k+1)]
```

on the relevant root central edge, while the proposed sibling replacement needs

```text
B_k=1/(2k+1).
```

The exact ratio is `2k`. This proves that source monotonicity alone does not
supply the required edge capacity. It does not rule out a different
cycle-adjusted positive realization; that is the finite `SFC` problem.