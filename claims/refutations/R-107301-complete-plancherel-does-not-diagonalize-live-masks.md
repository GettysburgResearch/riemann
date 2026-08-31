# R-107301 — Complete twisted Plancherel does not diagonalize joint live-source masks

Claim ID: `R-107301`  
Status: **BINDING COMPLETE-VERSUS-INCOMPLETE FIREWALL**  
Created: 2026-08-30  
Depends on: `L-107304`; PR #765 live occupancy ledgers  
Programme issues: #763, #737, #739  
RH/GRH status: **unproved**

The rank-free norm in `L-107304` requires a complete physical fibre of the
form

\[
A(x)B(y)\mathbf1_{xy^2=r}.
\]

The live Boolean/Wick source also contains shell, coprimality, owner/core,
common-factor, marked-prime and physical-cutoff masks. A joint mask
\(M(x,y)\) need not factor as \(M_1(x)M_2(y)\), and then the map

\[
(A,B)\longmapsto
\sum_{xy^2=r}M(x,y)A(x)B(y)
\]

is not diagonalized by the one-variable formula
\(\widehat A(\chi)\widehat B(\chi^2)\).

A minimal exact fixture is the diagonal mask

\[
M(x,y)=\mathbf1_{x=y}.
\]

For a group with more than two elements this matrix has rank greater than one,
so it cannot equal \(M_1(x)M_2(y)\). Its physical output depends on the joint
map \(y\mapsto y^3\), not on the separate owner and core Fourier coefficients
of `L-107304.2`.

Two invalid promotions are therefore forbidden:

```text
complete-shell twisted Plancherel
  -> arbitrary incomplete shell or source mask;

orthogonalize owner labels before physical collapse
  -> bound the physical cross-owner Gram.
```

The correct remaining task is to complete, decompose, or geometrically push
forward the joint masks while retaining their signed boundary. This is the
`LIVEBOUND107301` gate of `T-107301`.
