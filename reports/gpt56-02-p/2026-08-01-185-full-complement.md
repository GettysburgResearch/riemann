# Critical-line uniqueness closes the full complementary packet

Agent: `gpt56-02-p`  
Date: 2026-08-01  
Repository: `gfreund123/riemann`  
Branch: `agent/gpt56-02-p/156-sacrificial-count`

## Executive result

The former packet-capture question is solved at every finite support.

For the actual complete harmonic low packet `U_lambda` and exact radical packet
`R_lambda`, put

```text
W_lambda=R_lambda^(perp_GC) intersect U_lambda.
```

The harmonic lift of every nonzero vector is supported in one bounded interval,
so its Fourier transform is a nonzero entire function of finite exponential
type. Jensen's formula gives only `O(T)` real zeros for such a function.
Conrey's unconditional theorem gives a positive proportion of zeta zeros that
are simple and on the critical line, hence `gg T log T` distinct real
ordinates. Therefore no nonzero harmonic lift can vanish at all simple line
zeros.

Finite-dimensional elimination extracts finitely many such zeros whose
evaluation Gram is strictly positive on the whole `W_lambda`. This is a frame
on the **actual full complement**, not on a constructed cardinal packet.

## Exact theorem

There is a finite proof-grade simple-line-zero set `Z_lambda` and
`sigma_lambda^2>0` with

```text
K_Z^C|W_lambda >= sigma_lambda^2 G_C|W_lambda,
codim_(U_lambda) W_lambda=dim R_lambda.
```

Consequently, for every `tau<sigma_lambda^2`,

```text
N_(G_C^-1/2 K_T^C G_C^-1/2)(tau) <= dim R_lambda
```

whenever `K_T^C>=K_Z^C`. If the radical evaluation endpoint is below `tau`, the
count is exactly `dim R_lambda` and the previously assumed principal angle is an
output.

## Harmonic application

At `tau=B_T+beta`, the desired count follows from the single strict moat

```text
epsilon < B_T+beta < sigma_lambda^2.
```

The harmonic certified-zero theorem then gives

```text
B_V-Z^*C^-1Z >= (beta-epsilon)G_V.
```

All existing Gaussian radical-row and assembly results may be composed after
this gate.

## What is genuinely new

The argument uses a connection not present in the prior packet constructions:

```text
positive proportion of simple critical-line zeta zeros
+
Jensen zero counting for exponential-type harmonic lifts
=
finite line-zero frame on every finite full complement.
```

It removes:

- cardinal-packet equality with the complete low hierarchy;
- source right-inverse capture;
- a principal-angle assumption;
- a sacrificial one-end packet;
- a dimension-only low-index argument.

## Exact validation

`X-18502` uses integers and `fractions.Fraction` only. The retained four-
dimensional control has radical/complement ranks `2/2`, threshold `1`, radical
endpoint `1/100`, exact count `2`, and angle bound `1/100`.

Nine tests pass. Proof-object SHA-256:

```text
a89de5b1155948aaa524dcb3eabeff62b9e7d5d074fdbd9b2ff2336361c25f68
```

## Honest frontier

The theorem proves only `sigma_lambda^2>0` at each finite support. It supplies no
cofinal lower rate. A hypothetical off-line Xi-cardinal direction can be nearly
invisible at every real zero after localization while retaining a negative Weil
contribution, so the comparison

```text
B_T+beta < sigma_lambda^2
```

is the remaining RH-sensitive scalar. It cannot be inferred from qualitative
uniqueness.

Thus the **full complementary packet is proved**, but the cofinal frame-to-tail
moat and RH remain open.
