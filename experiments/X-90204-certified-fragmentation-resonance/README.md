# X-90204 — Certified near-conservation frozen-fragmentation resonance

This package supplies the directed numerical certificate used by `R-90201`.
It does **not** numerically search for sign changes of the endpoint functions.
Instead it certifies one nonreal pole of their continued Mellin transforms,
with real exponent greater than `0.49657` after the critical shift.
The Landau and integer-interpolation deductions are proved in `L-90207` and
`R-90201`.

## Run

```bash
python verify.py
```

Required package:

```text
mpmath
```

A successful replay prints

```text
PASS_X_90204_CERTIFIED_FRAGMENTATION_RESONANCE
```

and rewrites `results/verification.json`.

## Certificate layers

### 1. Directed Rouché disk

The script uses `mpmath.iv` at 70 decimal digits. Around

```text
u = 0.9965737487663334042655023867051966592...
  +108.6843160063763813085769124318175668569... i
```

it takes the radius `1e-18` and verifies

```text
|Delta(c)| + (sup |Delta''|) r^2 / 2
    < (inf |Delta'(c)|) r.
```

Therefore the disk contains exactly one zero of `Delta`, counted with
multiplicity, and the zero is simple. The shifted physical pole satisfies

```text
Re(u-1/2) > 0.496573748766333403.
```

### 2. Exact fragmentation increments

The `n=2,p=2` exit and the actual `n=2` sparse producer are generated from their
boundary values using `fractions.Fraction`. The script checks 39,998 exact trace
relations, including that the two exit traces sum to total first-entrance mass
`G(m)=m` and that the sparse trace is `(1,2/3)`.

### 3. Directed numerator intervals

For each trace, all renewal terms through `R=20000` are evaluated on a rectangle
containing the root disk with directed complex interval arithmetic. The infinite
tail is bounded analytically from the global exact increment bounds

```text
|a_exit(m)| <= 4,
|a_producer(m)| <= 2.
```

The resulting full numerator margins are

```text
|N_exit(u0)|     > 0.00987978337,
|N_producer(u0)| > 0.00199031875.
```

Thus neither characteristic pole cancels.

## Scope

The package certifies finite recurrence algebra, one simple characteristic
zero, and two nonzero numerator values. It does not invoke zeta values, a zeta
zero table, a finite endpoint sign scan, the PNT, or RH.
