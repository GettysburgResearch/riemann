# Repair of the MFT-to-prime-ramp implication

The earlier MFT proposal used a lower entropy bound together with an upper
capacity bound. That orientation cannot yield a lower bound for the entropy.

The corrected proof compares two quantities row by row:

```text
log binom(n,j)
```

and

```text
kappa(n,j)=sum_q chi_(n,j)(q).
```

Both equal `n h(j/n)` up to `O(sqrt(n))`. A nonnegative balanced feasible flow
has only `O(log^2 X)` total square-root row mass because every row carries all
columns between its larger child and its parent. Therefore the packet-level
comparison loses only `O(log^2 X)`.

Since the unweighted target mass is exactly

```text
sum_q q^(-1/2) log(X/q)=4 sqrt(X)+O(log X),
```

a flow with total slack `Sigma_X` has entropy

```text
4 sqrt(X)-Sigma_X+O(log^2 X).
```

Legendre's formula then gives the same lower bound for the complete prime-power
ramp.

This repairs the conditional MFT, FGCM, and Greedy-Slack front ends without
proving any of their existence theorems. RH remains unproved.
