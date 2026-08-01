# Directed complete-alias production result

Agent: `gpt56-pro-14`  
Date: 2026-08-01  
Issue: #162  
PR: #164  
Experiment: `X-16208`

## Result

The last null complete-alias field in the gamma=4096 source packet is closed:

```text
complete_arithmetic_alias.cross_error_upper = 27/32
complete_arithmetic_alias.full_upper         = 18
```

The checker proves

```text
||C_cross|| <= 27/32 < 0.9999999
D_full >= 0.1562499 I.
```

The proof is an exact rational phase/curvature and operator-budget replay. It
includes both stationary branches, higher-alias nonstationary pieces, the Airy
fold, normalized radial endpoint/polylogarithm channels, the post-cutoff tail,
and source ODE/template errors.

## Production promotion

The source-bound packet is promoted to

```text
PRODUCTION_PROFILE_GRAM_CLOSED
```

and the integrated fail-closed wrapper returns

```text
classification                  PRODUCTION_COMPLETE_ALIAS_WRAPPER_CLOSED
good-support measure lower      13/16
relative epsilon upper          31/32
ground correction ratio         63/563
```

The integrated proof-object SHA-256 is

```text
cbfcdca4414912ccef1c2537750a05083fd99d0c2cadf438ccd55c11297e946d
```

## Cofinal law

The complete alias operator error is bounded by

```text
18/sqrt(gamma)+2/cuberoot(gamma)+1792/gamma,
```

which tends to zero. The next scheduled scale, gamma=32768, has the directed
bound

```text
5019/23168 < 0.217.
```

No larger block was produced in this pass. The next task is to run the same
source-bound producer at the declared cofinal scales and verify that the full
wrapper correction ratio tends to zero.

## Proof boundary

The midpoint 2x2 matrix is a diagnostic only. The proof uses the exact
stationary-root/curvature calculation and outward stationary, nonstationary,
Airy, normalized endpoint, post-cutoff, ODE/template and finite-cell budgets.

This result closes one real finite production block. It does not by itself prove
RH. A cofinal sequence of passing blocks, the target-projection schedule, and
an independent audit of the CCM finite-real-zero implication remain required.
