# Hyperbolic log-log compression of the native beta criterion

## Result

The compact detector on PR #759 has exact finite support but pays a frequency
window of essentially `log X`, producing almost quadratic rank.

The new fixed multiplier

```text
exp(1-cosh t)
```

has the zero-free bilateral Laplace continuation

```text
exp(1-cos s).
```

Its frequency tail is double-exponential, while its physical kernel has an
exponential tail in every strip of width less than `pi/2`.

Paying the noncausal physical aliases requires a period of order `log X`.
Deleting the frequency tail requires only a bandwidth of order `loglog X`.
The native RH criterion therefore has deterministic feature dimension

```text
O(log X loglog X).
```

## Binding boundary

This is an unconditional analytic compression and an RH-equivalent criterion.
It is not an estimate of the native feature norm and does not prove RH.

The live gate is

```text
HNBV107020:
  the hyperbolically smoothed native beta feature vector has norm squared
  X^o(1).
```
