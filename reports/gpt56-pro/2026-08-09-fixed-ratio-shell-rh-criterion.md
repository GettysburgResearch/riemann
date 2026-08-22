# Every fixed-ratio endpoint shell is an RH criterion

Date: 2026-08-09  
Authoring agent: `gpt56-pro`  
Status: **new exact RH equivalence; unconditional sign remains open; RH unproved**

## 1. Result

For the prime endpoint scalar

```text
A(X)=sum_(p<=X) log(p) r_X(p),
```

fix any real ratio `c` with `0<c<1` and define

```text
T_c(X)=A(X)-A(cX).
```

`T-90007` proves

```text
RH
<=> T_c(X)<0 eventually
<=> T_c(X) is eventually one-signed.
```

This equivalence holds separately for every fixed ratio `c`.

## 2. Exact transform and drift

From `L-90004`,

```text
That_c(z)
 =(1-c^z)Ahat(z)
 =(1-c^z)G(z+1/2)/z^2.
```

At the origin,

```text
G(1/2+z)=(1+zeta(1/2))/(2z)+O(1),
```

so

```text
That_c(z)=kappa_c/z^2+O(z^-1),
kappa_c=-(1+zeta(1/2))log(c)/2<0.
```

Under RH the remaining nontrivial-zero residue series is absolutely bounded,
and therefore

```text
T_c(X)=kappa_c log X+O_c(1)<0
```

eventually.

## 3. Why the old blind-spot warning does not block a converse

At a hypothetical off-line zero

```text
rho=1/2+delta+i gamma,
delta>0,
```

the shell residue is multiplied by

```text
1-c^(rho-1/2).
```

But

```text
|c^(rho-1/2)|=c^delta<1,
```

so this factor cannot vanish.  A frequency-lattice zero can occur only when
`delta=0`, i.e. for a zero already on the critical line.  Such a zero is
consistent with RH and irrelevant to excluding off-line zeros.

Hence eventual shell one-sidedness directly implies RH by Landau; no
undifferenced endpoint fallback is required.

The corrected scope statement is:

```text
A fixed-ratio shell may suppress selected critical-line modes,
but it never suppresses a zero to the right of the critical line.
```

## 4. Relation to dyadic z-collapse

At `c=1/2`, `T-90002` proves the additional finite-geometric theorem that the
maximum over all tail thresholds is controlled by the endpoint. Thus

```text
RH <=> B_X=0 eventually.
```

For the endpoint sign alone, however, `T-90007` is independent of the z-collapse
argument and applies to every fixed ratio.

## 5. Proof-search consequence

The front door is now parameter-free in substance:

```text
choose any fixed c in (0,1);
prove A(X)-A(cX) is eventually one-signed;
Landau gives RH.
```

Changing `c` changes only the deterministic negative drift and the bounded
critical-line filter.  It does not change the off-line pole set.  Therefore a
ratio optimization may improve constants or finite behavior, but cannot evade
the RH obstruction.

RH remains unproved.
