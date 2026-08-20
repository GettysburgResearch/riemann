## Purpose

Freeze PR #664 at exact head `14692244bdaef90793a0c2a1a9bfd6e6b4bb1a2e` and audit its final ratio-67 window against the literal normalized SHARP box source.

**RH remains unproved.**

## Binding normalization correction

The conclusion-facing box is

```text
S_67 h(X) / sqrt(X)
  = sum_(n<=X) beta(n)/n * Phi(X/n).
```

Therefore its native prime operator is `I-p^-1 U_p`, not `I-p^-1/2 U_p`. The latter is the coefficient of the unnormalized kernel.

Consequently the native collar slope is

```text
-3 sum_(X/67<n<=X) beta(n)/sqrt(n)
```

or exactly

```text
-3 [B_1/2(X) -(1+67^-1/2)B_1/2(X/67)
    +67^-1/2 B_1/2(X/67^2)].
```

The unweighted Möbius window in `L-99819` belongs to an auxiliary normalization and cannot be promoted to the literal box.

## New exact GPMOC reduction

For any finite coefficient packet,

```text
Q_tau(c)
 = sum_(m,n) c_m c_n min(m,n)^(2tau)
 = 2tau integral t^(2tau-1) [sum_(n>=t)c_n]^2 dt.
```

The half-order collar window has an exact multiplicative-overlap Gram kernel. Thus the remaining theorem is one source-faithful half-order cumulative-tail/cross-core estimate.

## Replay

```text
PASS_T99900_NATIVE_BOX_HALF_ORDER_AND_HARDY_TAIL
72dad4933ce448abc94c92254f2fe9117205371eb4f244d9f3900be3d3c8c083
```

## Boundary

```text
normalized-box p^-1 operator               proved exact
unweighted-window promotion                refuted at statement-to-use scope
native three-band half-order window        proved exact
Cauchy-Poisson Hardy-tail identity          proved exact
ratio-window Gram identity                  proved exact
half-order one-sided estimate               open / RH-bearing
GPMOC99800                                  open / RH-bearing
Riemann Hypothesis                          unproved
```
