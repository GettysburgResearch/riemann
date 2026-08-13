# L-91416 — Positive equality/reserve measures have direct nonnegative row realizations

Claim ID: `L-91416`  
Status: **PROVED FROM RESIDENT NORMALIZED COMPONENT KERNELS**  
Created: 2026-08-13  
RH status: **unproved**

For `a=1,2`, retain

\[
w_a(x,k)=\frac{a\sqrt x}{k}-\frac1{\sqrt k}
\]

and the positive component atom `k^(-1/2)Q_(x/k)(j)`. Whenever `w_a>0`,

\[
\boxed{
k^{-1/2}Q_{x/k}(j)
=w_a(x,k)\frac{Q_{x/k}(j)}{a\sqrt{x/k}-1}.}
\]

The normalized profile is nonnegative by the resident component-row theorem.
Therefore arbitrary positive mass in the reserve channel `a=1` or equality
channel `a=2` produces a coefficientwise nonnegative row vector by integration.
The construction is linear and closed under positive restriction and addition.

For positive labelled measures `lambda_L,lambda_R`, the target and score are

\[
T=\lambda_L+2\lambda_R,
\qquad
S=2\lambda_L+\lambda_R.
\]

Adding the two channel row realizations gives a direct positive realization of
that `(L,R)` packet. Hence every same-endpoint output of `L-91415` has
nonnegative component rows without another Hall transport.

Ordinary/radix-four allocation and the finite boundary charge use the resident
positive linear maps after all packets are summed once.

```text
positive channel row realization       EXACT
arbitrary positive L/R measures         EXACT
same-endpoint output typing             EXACT
finite physical boundary allocation     IMPORTED
Riemann Hypothesis                      UNPROVED
```
