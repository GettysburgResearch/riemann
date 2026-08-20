# L-100182 — The activated large-prime collar is depth one; the signed positivity argument is withdrawn

Claim ID: `L-100182`  
Status: **PROVED EXACT ACTIVATED-SECTOR GEOMETRY; GLOBAL POSITIVITY WITHDRAWN**  
Created: 2026-08-20  
Depends on: corrected `L-100180`  
RH status: **unproved**

Fix an endpoint `X` and choose

\[
Z\ge X^{9/10}.
\]

After finite squaring of primes `p<=Z`, unsquared labels have primes `p>Z`.

## 1. Exact activated-sector geometry

For a source state whose complete label product is at most `X`, two distinct unsquared labels cannot occur.  Indeed, if `p,q>Z`, then

\[
pq>Z^2\ge X^{9/5}>X.
\]

Thus the portion of the completed source with label product `<=X` has at most one unsquared large prime.  In that **activated sector** the large-prime collar is depth one.

## 2. Noncompact-tail correction

The final critical Peano kernel is not compactly supported.  Source products greater than `X` still contribute through its positive continuation.  Such inactive states may contain more than one prime greater than `Z`; the preceding product argument does not remove them.

Their aggregate belongs to the inactive tail `R_m(X,Z)` in corrected `L-100180` and is controlled there by the supercritical estimate

\[
R_m(X,Z)
\ll_m
\sqrt X\sum_{p>\max(X,Z)}p^{-3/2}.
\]

The earlier assertion that the **entire** large-prime source was depth one is therefore withdrawn.

## 3. Signed-core firewall

Even within the activated sector, the squared small-prime core is a signed Euler packet.  A termwise kernel inequality for one large-prime child does not imply

\[
\text{child}_p\le p^{-1}\text{parent}
\]

after summing that signed core.  Such an implication would require a separate Harnack/order-preservation theorem for the squared-core observation.  No such theorem was proved here.

Consequently the former parent-minus-children positivity proof is withdrawn.

## 4. Surviving conclusion

```text
activated source products <=X: at most one unsquared p>Z   PROVED;
inactive noncompact tail:                                  INCLUDED IN L-100180;
signed squared-core parent/child domination:               OPEN;
standalone positivity theorem from depth-one geometry:     WITHDRAWN.
```

The completed critical positivity corridor remains available only through the corrected all-level estimate of `L-100180`, which keeps the inactive tail and all signed levels in one adjacent-level ledger.
