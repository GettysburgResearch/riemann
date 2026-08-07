# X-20807 — Exact Lévy and finite-Euler flow regression

This standard-library-only checker replays the finite algebra identities used by
the new prime-transport continuation.

## Run

```bash
python experiments/X-20807-levy-euler-flow/verify.py
```

Expected verdict:

```text
PASS_EXACT_L20810_L20812_L20813_IDENTITIES
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

### Finite Euler Riccati and triangular recombination

For

```text
r=1/2, a=3, K=4,
```

the checker proves with `fractions.Fraction`

```text
P_local                    45/16
Q_local                    117/8
E_cut                      441/256
triangular retained power  99/16
```

and verifies both exact reconstructions

```text
Q_local = P_local^2 + a P_local - E_cut,
Q_local = a P_local + triangular retained power.
```

The triangular term is independently replayed as

```text
a^2 sum_(ell=2)^K (ell-1) r^ell
=
a^2 sum_(m,n>=1, m+n<=K) r^(m+n).
```

Thus the cutoff defect is exactly the part of the local collision square lying
beyond the retained power triangle. The surviving finite Euler flow is wholly
positive, as asserted by `L-20813`.

## Proof boundary

The checker contains no zeta values, prime manifest, Fenchel special functions,
or asymptotic inference. It validates the exact finite algebra only. The
cofinal shifted-prime inequality in `T-20803` remains open.