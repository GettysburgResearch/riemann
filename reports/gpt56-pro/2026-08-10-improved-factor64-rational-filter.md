# Improved minimal factor-64 endpoint filter

Date: 2026-08-10  
Authoring agent: `gpt56-pro`  
Status: **minimal phase-blind annulus + improved zero-safe member + exact finite normal forms; RH remains unproved**

## 1. Endpoint coordinate

The surviving scalar is

```text
A(X)=sum_(p<=X) log(p) r_X(p).
```

Its exact Mellin transform retains every nontrivial zeta zero with residue

```text
m_rho/(rho-1/2)^2,
```

while the prime-square copy of the main zeta pole supplies the deterministic negative `log^2 X` drift. Eventual one-sidedness of `A` is equivalent to RH.

The decomposition

```text
A(X)=Delta_Lambda(X)+M(X)
```

separates the zero-sensitive complete-prime-power coordinate from a zero-insensitive moat. The moat is strictly negative and decreasing for every real `X>=2`.

## 2. Minimal annulus

The simple zero-safe filter

```text
P_64(y)
=(1-y)^2(1-y/sqrt(2))(1+y)(1+y+y^2)
```

has exact support `(X/64,X]`, retains every off-line pole, and admits an exact `Q(sqrt(2))` Bernstein certificate

```text
max_|y|=1 |P_64(y)|^2 < 16.
```

A four-point DFT contradiction rules out every radix-two filter of total degree at most five. The cubic-margin theorem rules out the only remaining integer annulus below 64. Thus factor 64 is minimal among finite integer-radix polynomial filters whose RH side is proved by an absolute critical-zero norm.

The cyclotomic member also factors as

```text
C(X)=A(X)-A(X/2)/sqrt(2),
G(X)=C(X)-C(X/4),
U_64(X)=G(X)-G(X/8).
```

It is therefore a factor-eight decrement of one factor-four critical state.

## 3. Improved rational unit-circle member

The preferred filter is

```text
P_64^*(y)
=(1-y)^2(1-y/sqrt(2))(1+y)(1+3y/4+y^2).
```

The quadratic roots form a conjugate unit-circle pair because their product is one and the discriminant is negative. Every filter root consequently has modulus at least one; a hypothetical off-line pole cannot be canceled.

At aligned endpoints the scalar is

```text
4sqrt(2) A_(64N)
-(4+sqrt(2)) A_(32N)
+(1-3sqrt(2)) A_(16N)
+(3-3sqrt(2)) A_(8N)
+(3-sqrt(2)) A_(4N)
+(1+4sqrt(2)) A_(2N)
-4 A_N.
```

Every radical/ramp coordinate below `N` cancels exactly.

On the unit circle,

```text
|P_64^*(e^(it))|^2
=8(1-x)^2(1+x)(3/2-sqrt(2)x)(2x+3/4)^2,
x=cos t.
```

A 1,024-cell exact Bernstein certificate over `Q(sqrt(2))` proves

```text
max_|y|=1 |P_64^*(y)|^2 < 11.
```

The filtered prime-square moat is below `-0.178`; the complete critical-line zero contribution is below `0.154`. Thus the unscaled RH margin exceeds `0.024`, and the displayed aligned scalar has a theorem-grade RH margin exceeding `0.13`.

Consequently

```text
RH
<=> the improved factor-64 scalar is eventually negative
<=> it is eventually one-signed.
```

The converse is direct Landau: every off-line pole survives and there is no positive-real singularity.

## 4. Exact finite normal form

The improved filter is a positive three-tap smoothing of a factor-16 critical shell:

```text
C=(I-S/sqrt(2))A,
H=(I-S)C,
G=(I-S^2)H,
U_64^*=(I+3S/4+S^2)G,
```

where `Sf(X)=f(X/2)`.

Its compact ramp spline has exactly one sign change at

```text
u*=16/3-7/(3sqrt(2)),
u=log_2(X/p).
```

The complete finite expression is

```text
annular radical seed
-
log(2) times a signed two-sector prime ramp,
```

supported entirely on `[X/64,X]`.

Critical seed cancellation forces every nontrivial compact ramp spline to change sign, so a coefficientwise-positive ramp proof is impossible. Separately, zero safety forbids filter roots in the open unit disk. These are distinct permanent firewalls.

## 5. Verification

The retained exact/floating replay is

```text
experiments/X-90019-factor64-rational/verify.py
```

It verifies:

```text
exact Q(sqrt(2)) moments;
unit-circle root geometry;
1,024-cell Bernstein norm certificate;
rigorous moat/zero-series margin corridors;
every aligned endpoint through five million.
```

The finite scan is reconnaissance only. The exact Bernstein and pole arguments are the proof objects.

## 6. Preferred open theorem

The current conclusion-producing statement is

```text
4sqrt(2) A_(64N)
-(4+sqrt(2)) A_(32N)
+(1-3sqrt(2)) A_(16N)
+(3-3sqrt(2)) A_(8N)
+(3-sqrt(2)) A_(4N)
+(1+4sqrt(2)) A_(2N)
-4 A_N < 0
```

for every sufficiently large `N`.

It is supported on the minimal phase-blind integer annulus `[N,64N]`, retains every off-line zero, and has a rigorous aligned RH-side margin exceeding `0.13`. An unconditional proof would prove RH. No such proof is claimed here.

## 7. Exact boundary

```text
minimal phase-blind integer annulus             proved / review
simple cyclotomic factor-64 certificate         proved / review
improved rational factor-64 certificate         proved / review
RH-side fixed margin >0.13                      proved / review
eventual one-sign -> RH                         proved / review
exact state/spline/radical normal forms         proved / review
unconditional improved factor-64 sign           open / RH-equivalent
Riemann Hypothesis                              unproved
```
