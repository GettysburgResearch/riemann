# R-101201 — Untyped producer coverage is not a proof of cell coverage

Claim ID: `R-101201`  
Status: **BINDING COMPOSITION FIREWALL**  
Created: 2026-08-21

The conditional cell-cover theorem counts a cell only when a proof establishes nonnegativity of the **same fixed detector** on the whole cell.

The following do not count automatically:

1. positivity of an endpoint-dependent finite completion (`PR #684`);
2. positivity after a signed or alternating inverse;
3. a regional source estimate that destroys a carrier cancellation (`PR #694`);
4. the withdrawn dilation-to-divisor-renewal arrows in the audited `PR #691`;
5. positivity in an auxiliary normalization or for a different kernel.

Accordingly, the phrases “finite squaring covers this cell” and “double-owner machinery covers that cell” are placeholders until a typed map

```text
(source object, normalization, kernel, endpoint cell)
    -> proof that the fixed G(X)>=0 for every X in that cell
```

is committed. The hyperedge is valid; the repository-specific certificate incidence theorem remains open.
