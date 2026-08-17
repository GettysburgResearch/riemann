# R-97000 — The two prime-sieved transport firewalls remain binding

Claim ID: `R-97000`  
Status: **EXACT SCOPE FIREWALL**  
Created: 2026-08-17  
Frozen source: PR #552 at `81df9c3f507aba0e5f21187044583a0d6fb90db9`

The candidate does not use either rejected mechanism:

1. fixed-product divisor cubes cannot create a three-knot convex packet; at
   `(j,P,n)=(3,6,24)` the same-knot residual is exactly `-1`;
2. a `P`-rough reservoir cannot be lower-bounded by the unrestricted integer
   block; at `(P,p,u)=(30,5,2)` the actual rough block contains only `7` and
   has mass `1/sqrt(7)<1/2`, whereas the unrestricted surrogate is `>2`.

The present packet keeps complete parity-labelled source packets grouped until
terminal common coupling. It never promotes a fixed-product residue, an
all-integer rough block, or an oriented child into the positive physical cone.
