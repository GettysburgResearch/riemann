## T-105310 continuation — the actual low-order Levinson step

This pass stays on the dedicated PR and adds a matrix-valued low-order descent.

For finite `p`, the centered Pick kernel of `p/p'` is

```text
K_p(z,w) = -sum_(p'(c)=0) rho_c / [(z-c)(bar(w)-c)],
rho_c=p(c)/p''(c).
```

After any source-fixed finite compression:

- `rho_c<0` is one positive rank-one good-extremum atom;
- `rho_c>0` is negative semidefinite;
- a simple nonreal pair has positive index at most one;
- confluent real/nonreal blocks have exact multiplicity-index bounds.

Combining those bounds with the unconditional xi-prime constants `0.86864`
(simple/on-line) and `0.93432` (distinct) gives nuisance positive index at most
`0.0821 N_xi'`.

Hence normalized effective rank `eta>=0.919` for one fixed Xi/Xi-prime Pick
compression would give

```text
N_0/N >= 0.6738-o(1),
```

counting on-line zeros with multiplicity, above the published
Montgomery–Taylor constant `0.672500703679...`. The simple-zero upgrade remains
separate and explicit.

A Cauchy-power gamma model has effective rank at least `49/51`; one-percent trace/HS
perturbations still give `eta>=0.923110...`, corresponding to `0.682020...`.
The remaining arithmetic theorem is `LPRT105310`, the source-faithful Xi
trace/HS and canonical-product-tail estimate.

```text
finite residue Pick decomposition          PROVED EXACT
confluent/off-line inertia budget           PROVED EXACT
0.86864/0.93432 nuisance cap 0.0821         PROVED
Cauchy-power gamma reserve                         PROVED
0.919 -> 0.6738 implication                 PROVED CONDITIONAL
LPRT105310                                  OPEN
new proportion / RH                         UNPROVED
```
