# R-99901 — PXGC path adjacency requires an explicit transit-capacity contract

Claim ID: `R-99901`  
Status: **PROVED DEFINITIONAL FIREWALL**  
Created: 2026-08-20  
Depends on: PR #658 `L-99704`  
RH status: **not assumed**

The original flow reduction allowed a negative vertex to send mass to a
positive vertex "along a path" of the reversible prime-exchange graph and then
invoked the ordinary bipartite Hall formula.

There are two inequivalent interpretations.

## Unrestricted reachability

If every reachable positive vertex is declared adjacent and intermediate
vertices have no capacity, the decorated occurrence graph is connected. Every
nonempty negative set has the entire positive side as its neighborhood. The
optimal residual reduces to

\[
\left[m_X^-(\Omega)-m_X^+(\Omega)\right]_+,
\]

which is just the negative part of the conclusion-facing scalar. This is
circular as a new producer.

## Capacity-constrained paths

If intermediate occurrences have capacities, ordinary bipartite Hall is not
the correct theorem on the collapsed reachability graph. Each intermediate
vertex must be split into an input node and output node joined by an edge
carrying its transit capacity. Max-flow/min-cut must then be applied to that
expanded network.

Accordingly the noncircular successor `EPXGC99900` must use either:

1. direct one-label Hasse edges only; or
2. a fully specified vertex-split capacitated path network.

No unrestricted-path shortcut may be used.
