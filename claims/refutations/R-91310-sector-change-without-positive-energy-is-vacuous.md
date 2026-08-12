# R-91310 — Sector change and boundary unitarity without positive energy are vacuous for RH

Claim ID: `R-91310`  
Status: **EXACT ARCHITECTURAL FIREWALL**  
Created: 2026-08-12  
Depends on: `L-91332/L-91333`  
RH status: **unproved**

The critical Jordan product sectors are mutually disjoint under nontrivial prime-log translation. That fact motivated an unbounded sector-changing wave operator in `T-91307`.

`L-91332` shows that sector change itself is not the conclusion-producing theorem. One may always:

1. assign a Hilbert fiber \(\mathcal H_t\) to every boundary parameter;
2. transport exactly between fibers;
3. form the direct integral;
4. obtain a strongly continuous unitary translation group;
5. place the boundary-unitary section \(\Theta_\omega(t)r(t)\Omega_t\) in that Hilbert space.

All of this holds independently of the location of the zeros.

The missing property is not Hilbert-space existence but

\[
\Theta_\omega r\in H^2(\mathbb C_+),
\tag{R-91310.1}
\]

equivalently positive energy/causality.

By `L-91333`,

\[
\|P_-(\Theta_\omega r)\|^2
=
\|P_{K_{B_\omega}}(\mathfrak A_\omega r)\|^2.
\tag{R-91310.2}
\]

A planted crossed zero gives a nonzero right-hand side while preserving boundary unitarity and the direct-integral representation.

Therefore reject any claimed completion that proves only:

```text
existence of a sector bundle;
unitary transport between sectors;
strong continuity of translations;
equality of boundary norms;
a unitary scattering multiplier on L2(R).
```

The RH-bearing theorem must prove that the distinguished completed section lies in the positive-energy Hardy subspace, or equivalently that the crossed-zero model projection vanishes.
