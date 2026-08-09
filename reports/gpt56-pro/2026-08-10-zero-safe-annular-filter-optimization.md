# Zero-safe optimization of the annular prime-endpoint criterion

Date: 2026-08-10  
Authoring agent: `gpt56-pro`  
Status: **new exact filter family + factor-81 zero-safe RH criterion; RH remains unproved**

## 1. Starting point

The first annular construction used

```text
3A(X)-7A(X/9)+5A(X/81)-A(X/729),
```

with multiplier `(1-y)^2(3-y)`. It deletes every radical/ramp coordinate below `X/729`, retains every off-line zero, and under RH has a fixed negative margin exceeding `1.48`.

The next goal was to reduce the annular width without sacrificing zero safety.

## 2. Cubic family and factor 125

For every radix `R>1`, the unique cubic filter killing the constant scale mode, its logarithmic derivative, and the critical `X^-1/2` seed mode is

```text
P_R(y)=(1-y)^2(1-R^-1/2 y).
```

Its exact support is `(X/R^3,X]`. The phase-blind RH margin is

```text
m(R)
 =-(1+zeta(1/2))/2 * (1-R^-1/2)log^2 R
  -4(1+R^-1/2)(log xi)''(1/2).
```

This margin is strictly increasing in `R`. It is negative at `R=4` and positive at `R=5`, so radix five is the smallest integer radix certified by the absolute-zero bound. This gives the factor-125 criterion

```text
sqrt(5) A_(125N)
-(2sqrt(5)+1) A_(25N)
+(sqrt(5)+2) A_(5N)
-A_N < 0 eventually.
```

The first aligned endpoint `X=125` is a finite nonnegative exception; every tested aligned endpoint from `250` through five million is negative. This finite behavior is not used in the theorem.

## 3. The factor-64 false lead and its firewall

A degree-six radix-two filter can be tuned so that a numerical phase-blind margin becomes positive and the formal support shrinks to factor 64. The apparent improvement is invalid for the RH converse: the extra cubic factor found by unconstrained optimization has roots strictly inside the unit disk.

For a hypothetical off-line zero `rho`, the scale variable satisfies

```text
|2^(-(rho-1/2))|<1.
```

An interior filter root can therefore cancel precisely the pole the Landau argument must retain. Such a filter is inadmissible no matter how favorable its RH-side norm looks.

This is the correct optimization constraint:

```text
annular moment cancellation
+ phase-blind critical-line norm
+ no filter zero in |y|<1.
```

The rejected factor-64 candidate is not committed as a theorem or producer.

## 4. Zero-safe quartic improvement: factor 81

The simple extra factor `1+y` has its only zero on the unit circle, so it cannot cancel an off-line pole. At radix three define

```text
P_3(y)=(1-y)^2(1-y/sqrt(3))(1+y).
```

This degree-four filter has exact support `(X/81,X]`. At aligned endpoints the integer-scale criterion is

```text
3A_(81N)
-(3+sqrt(3))A_(27N)
+(-3+sqrt(3))A_(9N)
+(3+sqrt(3))A_(3N)
-sqrt(3)A_N.
```

The unit-circle norm has the exact real form

```text
|P_3(e^{it})|^2
=8(1-x)^2(1+x)(4/3-2x/sqrt(3)),
x=cos t.
```

An exact four-cell Bernstein certificate over `Q(sqrt(3))` proves

```text
|P_3(e^{it})|^2<18.
```

This yields the fixed RH-side margin

```text
limsup V_3(X) <= -0.1163536095...
```

and hence `V_3(X)<-0.1` eventually under RH. Conversely every off-line zero survives because the filter roots are `1,-1,sqrt(3)`, all of modulus at least one. Eventual one-sidedness therefore implies RH by Landau.

The factor-81 criterion is now the narrowest zero-safe annular criterion on this branch with an exact phase-blind proof and small integral-radix scales.

## 5. Finite replay

`X-90017` checks every aligned endpoint through five million. There are 46 nonnegative small endpoints, the last at `X=6399`; all later retained aligned endpoints are negative. The exact Bernstein certificate, not the finite sign scan, is the load-bearing numerical artifact.

## 6. Frontier

The preferred conclusion-producing target is

```text
3A_(81N)
-(3+sqrt(3))A_(27N)
+(-3+sqrt(3))A_(9N)
+(3+sqrt(3))A_(3N)
-sqrt(3)A_N < 0
```

for all sufficiently large `N`.

It has:

```text
fixed arithmetic support [N,81N];
no off-line-zero blind spot;
an exact RH-side margin separated from zero;
finite exceptions explicitly isolated.
```

An unconditional proof of this annular inequality would prove RH. No such proof is claimed here.
