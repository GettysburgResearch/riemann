# T-108400 — Hellinger-stable shared-fibre relative-trace frontier

Claim ID: `T-108400`  
Status: **EXACT OCCUPANCY-TO-TRACE BRIDGE; ARITHMETIC HELLINGER ESTIMATE AND RH OPEN**  
Created: 2026-08-31  
Base: PR #776 at `098802565e3f9a00b7f4d0e4e77855620e446e7f`  
Sibling inputs: PR #771 and PR #774  
RH/GRH status: **unproved**

PR #776 proves that all positive fixed-fibre Wick energy lives in the
occupancy quotient

\[
Q(D)=D^{1/2}SD^{1/2}-dI.
\]

This packet quantifies the remaining failure of partial-Frobenius symmetry.

For every grouped live fibre \(\iota\), choose the complete or orbitwise
Frobenius-symmetric comparator \(\bar D_\iota\). Define

\[
\mathfrak E_{\rm occ}(X)
=
2\sum_\iota
\sqrt{N_\iota}
\|D_\iota^{1/2}-\bar D_\iota^{1/2}\|_{\mathcal S_2}.
\tag{T-108400.1}
\]

`L-108402` gives

\[
\boxed{
\text{live positive trace}
\le
\text{symmetric comparator trace}
+
\mathfrak E_{\rm occ}.
}
\tag{T-108400.2}
\]

The comparator trace is exactly the object diagonalized by PR #771's
rank-free twisted squareclass Plancherel theorem on complete deep
nonresonant fibres.

Define `FROBHELL108400` by the source-faithful estimate that, after the exact
same-arithmetic-tuple history recombination,

\[
\boxed{
\mathfrak E_{\rm occ}(X)=X^{o(1)}
}
\tag{T-108400.3}
\]

in the normalization required by the parent connected-Kummer consumer.
For rectangular panels it is enough to prove

\[
2\sum_\iota N_\iota
\sqrt{
\eta_{L,\iota}
+\eta_{R,\iota}
-\frac12\eta_{L,\iota}\eta_{R,\iota}
}
=
X^{o(1)}.
\tag{T-108400.4}
\]

Retain `QRESBIND107300` for the at-most-three explicit quadratic resonance
rows, incomplete masks, endpoints and principal member.

Then the exact composition is

\[
\boxed{
\mathrm{FROBHELL}_{108400}
\ \wedge\
\mathrm{QRESBIND}_{107300}
\Longrightarrow
\mathrm{LIVEBOUND}_{107301}
\Longrightarrow
\mathrm{CBKM}_{106130}
\Longrightarrow
\mathrm{BCI}_{102990}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-108400.5}
\]

Every arrow before the two named arithmetic premises is source typed. The
packet proves neither premise.

## What changed

The previous frontier was a qualitative live-occupancy census or exact
partial-Frobenius lift. The new frontier is quantitative and one-sided:

```text
complete symmetric fibre             handled by rank-free Plancherel;
failure of the atom lift              exact Hellinger occupancy debt;
two-sided rectangular occupancy       two one-sided Hellinger defects;
same-cell histories                    paid before occupancy;
quadratic resonances/principal member  retained separately.
```

`R-108400` shows that total mass or support information cannot supply the
new estimate formally.

```text
positive quotient restriction          INHERITED PROVED
Hellinger trace stability               PROVED EXACT
rectangular one-sided tensorization     PROVED EXACT
complete-fibre Plancherel composition   PROVED EXACT
FROBHELL108400                           OPEN
QRESBIND107300                           OPEN
RH / GRH                                UNPROVED
```
