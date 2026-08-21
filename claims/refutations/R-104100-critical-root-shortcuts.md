# R-104100: exact countermodels to critical-root shortcuts

Claim ID: `R-104100`  
Status: **PROVED EXACT FIREWALLS**  
Created: 2026-08-21  
RH status: **unproved**

## 1. Every supercritical moment may be positive while the critical moment is negative

Let

```text
nu = (2/5) delta_2 - delta_1.
```

Then the critical first moment is

```text
int t dnu(t) = 4/5-1 = -1/5 < 0.
```

For every real `m>=2`,

```text
int t^m dnu(t) = (2/5)2^m-1 >= 3/5 > 0.
```

Thus positivity of the complete supercritical hierarchy does not determine the
critical sign.

## 2. A positive-definite Gram does not orient a signed linear scalar

Take

```text
K = [[1,3/4],[3/4,1]].
```

Its determinant is `7/16>0`, so `K` is positive definite.  Nevertheless, for
`c=(1,-2)`,

```text
c dot K e_1 = 1-3/2 = -1/2 < 0.
```

PSD or positive Fourier geometry cannot be promoted to a signed linear sign.

## 3. Root-free excess may vanish while the root is arbitrary

For

```text
Q=x^2+e^2,
```

set `e=0`.  The excess is zero for every real `x`; no root bound follows.

## 4. Pairwise positive products need not generate an all-factor positive cone

For commuting scalar operators

```text
A=B=C=-1,
```

all pair products equal `+1`, while

```text
ABC=-1.
```

Pairwise Euler-block positivity therefore needs a genuine composition theorem
before it can be used at all prime depths.

## 5. Coefficient one is not a strict return

If

```text
|g|^2 <= Q = |g|^2+E,
```

then the statement is tautological and absorbs nothing.  The strict condition
`theta<1`, with a controlled reciprocal moat, is essential.
