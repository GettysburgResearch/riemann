# R-107400 — Hardy transfer and source softening do not remove the unit index

Claim ID: `R-107400`  
Status: **BINDING TOPOLOGICAL FIREWALL**  
Created: 2026-08-30  
Depends on: `L-106674`, `L-106700`, `L-107402`  
Programme issue: #744  
RH status: **unproved**

`L-107402` repairs the radial-to-input multiplier mismatch exactly. It does
not pay the topological block.

Let \(B_-=B\) be any finite inner function of degree \(d\), let \(B_+=1\), and
take the perfect source multiplier \(R=I\). Then:

```text
radial reserve       = 0;
Hardy-input reserve  = 0;
phase commutator     = 0;
```

but

\[
\boxed{
\|H_{\overline B}\|_{\mathcal S_2}^2=d,
\qquad
-\operatorname{wind}(\overline B)=d.
}
\tag{R-107400.1}
\]

Thus even exact source transport with no reserve leaves the complete unit
spectrum when the numerator model has insufficient dimension.

For the Xi odd-endpoint quotient this unit block is

\[
(R_K-R_0)_+
\]

up to the declared regularization ledger. Any theorem bounding the complete
endpoint charge below its allowance necessarily proves a new zero-count
statement; it cannot follow from diagonal source softening alone.

The new order-31 margin in `T-107400` is genuine, but the physical
source-to-index theorem remains indispensable.
