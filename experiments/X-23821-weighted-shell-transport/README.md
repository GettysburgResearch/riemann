# X-23821 — exact weighted shell transport replay

This standard-library checker replays the finite algebra of `L-23824` and
`L-23826` using integers and `fractions.Fraction` only.

It verifies:

```text
weighted upper-tail domination;
constructive matching to larger weights;
raw prime-to-prime transfer amounts;
destination endpoint removals;
zero total logarithmic-objective change;
least in-support weighted boundary charge;
nonpositive final residuals.
```

Run:

```bash
python verify.py
```

Retained verdict:

```text
EXACT_WEIGHTED_TAIL_TRANSPORT_VERIFIED
proof-object SHA-256
41753d1842a8c0e7f39bc45b97cafb9c429bae4f5bd9728247a853a7af90502b
```

The rational weights are formal positive increasing logarithmic coordinates.
The theorem is algebraic in those weights and specializes to `x_i=log p_i`.

The replay proves no estimate on the actual zeta shell charge, no prime-sampling
remainder bound, and no statement about RH.
