# L-93304 — The cubic endpoint scalar has an exact third-difference local inversion

Claim ID: `L-93304`  
Status: **PROVED EXACT DISCRETE IDENTITY**  
Created: 2026-08-16  
Depends on: the cubic kernel of `L-93250`  
RH status: **unproved**

For an arbitrary finitely supported coefficient sequence `c(m)`, define

\[
A_c(N)=\sum_{m\le N}c(m)K(m/N)
\]

and

\[
P_c(N)=3N^3A_c(N).
\]

Let `Delta f(N)=f(N+1)-f(N)`. Then

\[
\boxed{
\Delta^3P_c(N)
=(N+1)(N+2)
[c(N+2)-c(N+1)].
}
\tag{L-93304.1}
\]

## Proof

For one source atom at `m`,

\[
3N^3K(m/N)
=-mN^2+3m^2N-2m^3
\]

for `N>=m`, and it is zero before activation. The third forward difference vanishes away from the activation boundary. At `N=m-2` it is `m(m-1)`, and at `N=m-1` it is `-m(m+1)`. Summing the two possible active atoms at a fixed `N` gives (L-93304.1).

## Consequences

1. The cubic transform loses no local arithmetic information: adjacent source differences are recovered exactly.
2. Endpoint-variation methods must exploit the sign and sparsity of the actual Q4 source; smoothness of the cubic kernel alone cannot prove the square-root bound.
3. The identity gives a deterministic finite regression for every proposed interpolation or endpoint recurrence.

For `c=c_circ`, the right side is supported only at prime powers, shifted prime powers, and four-adic gauge activations. This is the exact sparse endpoint forcing available to a future discrete-dispersion attack.
