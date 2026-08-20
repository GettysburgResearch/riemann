## Purpose

Hostilely continue PR #664 and repair its first conclusion-facing
normalization mismatch, while opening PR #659's remaining Poisson square.

```text
base PR:      #664
base SHA:     14692244bdaef90793a0c2a1a9bfd6e6b4bb1a2e
head branch:  review/gpt56-pro/99820-native-box-normalization-audit
```

**The Riemann Hypothesis remains unproved.**

## Binding normalization correction

For the zero-free factor-67 box,

```text
(S_67 h)(X)/sqrt(X) = sum beta(n)/n phi(X/n).
```

Therefore a native normalized prime step is

```text
I-p^(-1)U_p,
```

not `I-p^(-1/2)U_p`. The latter is correct on the unnormalized kernel `W`,
but not after replacing `W` by `phi=W/sqrt(.)`.

Consequently PR #664's half-order annihilation and plain unweighted Mertens
collar coefficient are nonnative in the canonical normalized scalar chain.

## Exact repair

The correct collar coefficient is

```text
-3 sum_(x/67<n<=x) beta(n)/sqrt(n).
```

Its subpower logarithmic negative-mass criterion has transform

```text
(1-67^-s)(1-67^(-(s+1/2))) / [s zeta(s+1/2)]
```

and is equivalent to RH.

The native one-prime and two-prime box blocks remain positive; all-prime
composition remains open.

## New Hardy identity

PR #659's Cauchy–Poisson square is exactly

```text
Q_tau = |sum c_n|^2
        +2tau integral |sum_(n>=v)c_n|^2 v^(2tau-1)dv.
```

Thus GPMOC is a nested real tail-square theorem. Local owner coercivity does
not by itself bound the off-diagonal tails.

## Replay

```bash
python3 experiments/X-99820-native-box-audit/verify.py \
  --output experiments/X-99820-native-box-audit/results/verification.json
python3 -m unittest discover \
  -s experiments/X-99820-native-box-audit/tests -v
sha256sum -c T99820_CONTENT_SHA256SUMS
```

Expected:

```text
PASS_T99820_NATIVE_BOX_NORMALIZATION_AND_HARDY_TAIL
```

## Exact boundary

```text
native normalized coefficient             p^(-1), proved
PR #664 p^(-1/2) normalized operator       refuted as nonnative
native one-/two-prime positivity           proved
native half-order collar window            proved exact
Hardy tail-square factorization            proved exact
window/tail negative-mass estimate         open / RH-equivalent
Riemann Hypothesis                         unproved
```
