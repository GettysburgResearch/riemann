# X-20807 — Exact Lévy and finite-Euler flow regression

This standard-library-only checker replays two finite algebra identities used by
the new prime-transport continuation.

## Run

```bash
python experiments/X-20807-levy-euler-flow/verify.py
```

Expected verdict:

```text
PASS_EXACT_L20810_L20812_IDENTITIES
```

## What is checked

### Lévy cumulant transport

A synthetic arithmetic compound-Poisson law with jumps `1` and `5`, each of
intensity `1`, has

```text
mean      6
variance 26
```

The reference minimizer `chi(p)=1+p` has variance `24`, initial reserve `1`, and
Fenchel barrier `23`. The checker verifies exactly

```text
reserve = 26 - 23 = 1 + 26 - 24 = 3.
```

This is the finite model of `L-20810`.

### Finite Euler Riccati defect

For

```text
r=1/2, a=3, K=4,
```

the checker proves with `fractions.Fraction`

```text
P_local = 45/16
Q_local = 117/8
E_cut   = 441/256
Q_local = P_local^2 + a P_local - E_cut.
```

It evaluates the cutoff defect both as a positive finite sum and through the
closed bracket formula. This is the core local identity of `L-20812`.

## Proof boundary

The checker contains no zeta values, prime manifest, Fenchel special functions,
or asymptotic inference. It validates the exact finite algebra only. The
cofinal shifted-prime inequality in `T-20803` remains open.