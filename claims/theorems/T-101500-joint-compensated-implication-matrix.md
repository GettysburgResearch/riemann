# T-101500: joint compensated implication matrix

Inherit from PR #697 the exact fixed-detector decomposition

```text
G_beta = C + Q + A,
```

where `C` is compactly supported calibration and `Q,A` are the quadratic and activation/largest-prime bridge coordinates.

## Matched terminal conditions

For every horizon `Y`, suppose there exists one measurable transfer `tau_Y(X)` such that

```text
QMT101500:
int_1^Y (Q(X)+tau_Y(X))_- dX/X = Y^o(1),

AMT101500:
int_1^Y (A(X)-tau_Y(X))_- dX/X = Y^o(1).
```

## Conclusion

Then

```text
int_1^Y (G_beta(X))_- dX/X = Y^o(1).
```

Hence the fixed Mellin-Landau consumer inherited from PR #697 yields RH.

## Proof

By L-101500,

```text
(Q+A)_- <= (Q+tau_Y)_- + (A-tau_Y)_-.
```

The calibration is supported on one fixed compact interval and contributes `O(1)`. Integrate and invoke the inherited fixed-detector consumer.

## Boundary

This theorem is an exact conditional implication. Neither `QMT101500` nor `AMT101500` is proved here, and RH remains unproved.
