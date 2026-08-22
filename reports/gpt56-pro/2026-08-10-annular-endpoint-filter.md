# Fixed-annulus continuation of the prime endpoint route

Date: 2026-08-10  
Authoring agent: `gpt56-pro`  
Status: **new exact annularization + robust RH-equivalent sign criterion; RH unproved**

## Result

The endpoint scalar of PR #352 admits the four-scale filter

```text
U_9(X)=3A(X)-7A(X/9)+5A(X/81)-A(X/729).
```

The multiplier is

```text
3-7y+5y^2-y^3=(1-y)^2(3-y),  y=9^-z.
```

The double root at `y=1` kills the constant and logarithmic scale modes. The root at `y=3` kills the critical `X^-1/2` seed mode. Consequently every seed and prime-ramp term below `X/729` cancels exactly in radical-switching coordinates.

At `X=729N`, the criterion is the finite annular expression

```text
3A_(729N)-7A_(81N)+5A_(9N)-A_N.
```

Every hypothetical off-line zero survives because `|9^(-(rho-1/2))|<1`, while the filter roots are `1` and `3`.

## Robust RH margin

Under RH,

```text
U_9(X)
 = (1+zeta(1/2)) log^2(9)
   + critical-line zero series
   + o(1).
```

The deterministic constant is

```text
-2.22249758405246967649...
```

and the exact total square mass of the critical zeros is

```text
(log xi)''(1/2)=0.04620998623083794157...
```

Since the multiplier has modulus at most 16 on the unit circle, the whole zero series has absolute value at most

```text
0.73935977969340706524...
```

and therefore

```text
limsup U_9(X) <= -1.4831378043590626...
```

under RH. In particular RH gives `U_9<-1.4` eventually. Conversely any eventual one-sign law gives RH by Landau.

## Relation to the prime-power moat

Applying the same filter to the globally decreasing moat of `L-90014` gives unconditionally

```text
3M(X)-7M(X/9)+5M(X/81)-M(X/729)
 -> (1+zeta(1/2))log^2(9).
```

So the fixed negative constant is entirely zero-insensitive. All remaining arithmetic obstruction lies in the correspondingly filtered complete-prime-power deficit.

## Finite replay

The retained scan checks every multiple of 729 through five million and finds no nonnegative value. This is reconnaissance only; the proof value is the exact annular support and the analytic margin.

## Frontier

The preferred new target is:

```text
prove a fixed negative margin for
3A_(729N)-7A_(81N)+5A_(9N)-A_N
using only the factor-729 annular radical ledger.
```

This target is scale-stationary, keeps every off-line zero, and has an RH-side margin separated from zero. RH remains unproved.
