# L-91852 — Complete tagged cells, one quantizer and one discard marginal close the boundary interfaces

Claim ID: `L-91852`  
Status: **PROVED EXACT INTERFACE THEOREM**  
Created: 2026-08-15  
RH status: **unproved**

## 1. Tagged cells

The tagged target `coprod_n {n}x[0,1)` is a literal disjoint union. Restriction to a set of whole tags therefore occurs before quadrature and creates neither a partial-cell error nor a lower-cutoff atom. The retained adjacent defect is exactly the sum over retained tags.

## 2. Quantizer contract

A physical quantizer is a Markov kernel `Q(j|n,u)` satisfying

\[
 Q(j|n,u)\ge0,
 \qquad
 \sum_jQ(j|n,u)=1,
\]

and its support lies in the fixed finite stencil of that tagged cell. No internal colour appears in its domain. A family `Q_a` indexed by child or Hall label is a different construction and is forbidden.

## 3. Scalar thinning

For common thinning `tau`, define the retained coupling `tau Gamma^0` and the two discarded Hall input marginals `(1-tau)E`, `(1-tau)O`. Then retained plus discarded equals the original input on every measurable source class. The discard is unused current-generation source and is never exported.

## 4. Port decompilation

The construction uses component rows, same-index child placement, scalar restriction, one endpoint Markov kernel and signed response comparison. None is a coloured state completion or Schur-complement correction. Hence the auxiliary matrix-port demand is identically zero. Intrinsic boundary coordinates transported by the row remain ordinary typed observations and are not an auxiliary port.

## 5. Boundary

```text
partial cell                           absent by tagged support
cutoff atom                            absent
per-colour quantizer                   forbidden by type
unowned thinning loss                 absent by discard marginal
auxiliary Schur demand                 zero
Riemann Hypothesis                     unproved
```
