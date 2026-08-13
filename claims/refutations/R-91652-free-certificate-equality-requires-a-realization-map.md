# R-91652 — A free provenance certificate is not its physical realization

Claim ID: `R-91652`  
Status: **EXACT TYPE FIREWALL**  
Created: 2026-08-13  
RH status: **unproved**

Let `A_X` and labelled causal symbols `C_(p;X)` generate a free positive
certificate cone. The physical relation

\[
C_{p;X}\mapsto A_X-p^{-1/2}A_{X/p}
\]

is a linear realization relation; it is not an equality of coefficient vectors
inside the free cone.

Consequently the decomposition

\[
A_X=sA_X+\sum_i\lambda_iC_{p_i;X}
      +\sum_i\alpha_iA_{X/p_i}
\]

must be read after applying a realization map. In the free cone the right side
has current certificate mass `s+sum lambda_i=1` and additional child mass
`sum alpha_i>0`; its coefficient vector is not the one-symbol vector on the
left.

A rigorous packet envelope must therefore distinguish:

```text
free provenance certificate cone;
linear physical realization map;
additive certificate mass;
physical packet deficit pulled back through realization.
```

Quotienting by physical equality before defining mass can make mass
representation-dependent. The repaired theorem packet defines all four objects
explicitly in `L-91652`.