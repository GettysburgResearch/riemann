# The undifferenced prime endpoint is the minimal RH criterion

Date: 2026-08-09  
Authoring agent: `gpt56-pro`  
Status: **new exact RH equivalence; unconditional sign open; RH unproved**

## Result

For

```text
A(X)=sum_(p<=X) log(p) r_X(p),
```

`T-90008` proves

```text
RH
<=> A(X)<0 eventually
<=> A(X) is eventually one-signed.
```

The exact Mellin transform from `L-90004` has

```text
Ahat(z)
 =(1+zeta(1/2))/(2z^3)
 +c1/z^2+c0/z+holomorphic.
```

Thus under RH,

```text
A(X)
 =(1+zeta(1/2))/4 * log^2 X
 +O(log X),
```

with coefficient

```text
(1+zeta(1/2))/4
 =-0.1150886272023967032223747881... <0.
```

Every off-line zero survives with residue

```text
m_rho/(rho-1/2)^2.
```

Consequently eventual one-sidedness gives RH directly by Landau, while RH gives
eventual strict negativity because the critical-line zero series is absolutely
bounded.

## Relation to the shell results

The fixed-ratio criteria are scale differences of this scalar:

```text
A(X)-A(cX)
 =-(1+zeta(1/2))log(c)/2 * log X+O_c(1)
```

under RH.  They remain useful because:

- every fixed ratio is itself a direct RH criterion (`T-90007`);
- at `c=1/2`, z-collapse upgrades endpoint negativity to `B_X=0` eventually
  (`T-90002/T-90006`).

But no shell is logically necessary for the RH converse.  The smallest finite
producer is the single inequality

```text
A_N<0 for all sufficiently large integers N.
```

## Current obstruction

The finite regression through `10^6` is strictly negative.  Proving this sign
cofinally would prove RH.  The exact explicit formula shows why the remaining
gap is irreducible by routine floor estimates: a hypothetical off-line zero
contributes `X^(Re rho-1/2)` and eventually overwhelms the negative quadratic
logarithmic drift along suitable phases.

RH remains unproved.
