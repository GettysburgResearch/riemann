# Factor 64: the minimal phase-blind integer annulus

Date: 2026-08-10  
Authoring agent: `gpt56-pro`  
Status: **exact zero-safe annular criterion + minimality theorem; RH remains unproved**

## 1. Filter

The optimized zero-safe filter is

```text
P_64(y)
=(1-y)^2(1-y/sqrt(2))(1+y)(1+y+y^2)
=(1-y^2)(1-y^3)(1-y/sqrt(2)).
```

Its roots are

```text
1 (double), sqrt(2), -1, exp(±2pi i/3).
```

Every root has modulus at least one, so no hypothetical off-line pole can be canceled.

The aligned endpoint criterion is

```text
sqrt(2) A_(64N)
-A_(32N)
-sqrt(2) A_(16N)
+(1-sqrt(2)) A_(8N)
+A_(4N)
+sqrt(2) A_(2N)
-A_N.
```

Every radical/ramp coordinate below `N` cancels exactly; the arithmetic support is `[N,64N]`.

## 2. Exact RH-side margin

On the unit circle, with `x=cos t`,

```text
|P_64(e^(it))|^2
=8(1-x)^2(1+x)(3/2-sqrt(2)x)(1+2x)^2.
```

An exact `Q(sqrt(2))` Bernstein replay on 1,024 rational subintervals proves

```text
max_|y|=1 |P_64(y)|^2 < 16.
```

The prime-square moat is below `-0.194`; the complete critical-line zero series is below `0.185`. Hence the unscaled RH-side margin exceeds `0.009`, and the aligned scalar has margin exceeding `0.012`. RH therefore gives the displayed factor-64 scalar `<-0.01` eventually.

Conversely every off-line zero survives the multiplier, so eventual one-sidedness implies RH by Landau.

## 3. Minimality

For integer radix two, any annulus factor below 64 has total degree at most five, so the dressing polynomial has degree at most two. Normalize it by `Q(1)=1`.

A positive phase-blind margin would force

```text
||B_2 Q||_infinity < 0.71,
B_2(y)=(1-y)^2(1-y/sqrt(2)).
```

Evaluating at the fourth roots of unity gives very small bounds on `Q(-1)` and `Q(±i)`. But every degree-at-most-two polynomial obeys

```text
Q(1)+iQ(i)-Q(-1)-iQ(-i)=0.
```

The resulting triangle inequality demands simultaneously

```text
1-|Q(-1)| > 0.895
```

and

```text
|Q(i)|+|Q(-i)| < 0.582,
```

which is impossible.

At radix three the only smaller annulus is the unique cubic factor-27 member, whose phase-blind margin is negative. Radix at least four already has degree-three annulus factor at least 64. Thus factor 64 is minimal in the finite integer-radix polynomial class using the absolute critical-zero norm bound.

## 4. State reduction

The cyclotomic factorization yields

```text
C(X)=A(X)-A(X/2)/sqrt(2),
G(X)=C(X)-C(X/4),
U_64(X)=G(X)-G(X/8).
```

So the seven-scale theorem is one factor-eight monotonicity law for a factor-four critical state.

The complete finite coordinate is also explicit:

```text
annular radical seed
-
log(2) times a signed prime-ramp spline.
```

The ramp spline has a unique sign change at

```text
u=5-sqrt(2),  u=log_2(X/p).
```

Critical cancellation forces this spline to change sign; a termwise-positive ramp proof is impossible. This is distinct from the zero-safety firewall, which excludes filter roots in the open unit disk.

## 5. Frontier

The preferred open statement is

```text
sqrt(2) A_(64N)
-A_(32N)
-sqrt(2) A_(16N)
+(1-sqrt(2)) A_(8N)
+A_(4N)
+sqrt(2) A_(2N)
-A_N < 0
```

for every sufficiently large `N`.

It is the minimal phase-blind integer-annulus target, has a strict RH-side margin, and retains every off-line zero. An unconditional proof would prove RH. RH remains unproved.
