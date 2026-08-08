# Integration addendum — endpoint-scale kernel bridge

**Parent branch:** `research/gpt56-pro-262-parabolic-scale-frame`  
**Parent PR:** #265  
**New claim:** `L-26204`  
**Status:** **PROPOSED COMPLETE EXACT TRANSFORM; FINITE POSITIVE MINORANT OPEN**

## Canonical formulas

For the continuum parabolic seed response `F`, the endpoint derivative kernel is

```text
k(u)=-F(u)/2-uF'(u)
    =2N-S_N/sqrt(u)
```

on `1/(N+1)<u<=1/N`.  It is positive and has mass two.

The log-scale kernel

```text
varrho(v)=exp(-v/2) k(exp(-v))
```

has transform

```text
Laplace[varrho](z)
 =zeta(z+1/2)(z-1/2)/[z(z+1/2)].
```

The exact endpoint equality weight is

```text
L_*(t)=sum_(n<=exp(t)) mu(n)/sqrt(n)
       [2 exp((t-log n)/2)-1],
```

with

```text
Laplace[L_*](z)
 =(z+1/2)/[z(z-1/2)zeta(z+1/2)],
Laplace[L_*](1/2)=2.
```

Its endpoint entropy is therefore four.

## Existing-route bridge

If `g_carry` is the canonical carry-resolvent state on PR #252, then exactly

```text
g_carry(t)=L_*(t)+(3/2) integral_0^t L_*(u)du,
```

and

```text
L_*(t)=g_carry(t)
 -(3/2) integral_0^t exp(-3(t-u)/2)g_carry(u)du.
```

The endpoint-scale and DCRS states are stable causal transforms of one another.
No global sign conclusion follows automatically.

## Integration consequence

The positive endpoint-scale greedy is a finite-horizon nonnegative minorant of
this exact Volterra equality state.  `ESBT/ESGS`, DCRS, and FGCM should be
indexed as alternative finite positive-producer theorems attached to the same
reciprocal-zeta pole family, not as independent analytic evidence.
