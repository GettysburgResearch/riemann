# R-108400 — Total occupancy and complete-fibre Plancherel do not control live occupancy fluctuation

Claim ID: `R-108400`  
Status: **PROVED EXACT COUNTERMODEL**  
Created: 2026-08-31  
RH/GRH status: **not assumed**

Fix \(m\ge2\) cells and total occupancy \(N=m^2\).

The uniform occupancy is

\[
E=mI_m
\]

and has zero Hellinger defect from its Frobenius average.

The concentrated occupancy is

\[
D=\operatorname{diag}(m^2,0,\ldots,0).
\]

It has the same total mass, but

\[
\boxed{
\|D^{1/2}-E^{1/2}\|_{\mathcal S_2}^2
=
2m^2\left(1-\frac1{\sqrt m}\right).
}
\tag{R-108400.1}
\]

Thus the normalized defect tends to \(2\), not zero.

Consequently none of the following can replace `FROBHELL108400`:

```text
the total number of atoms;
the number of occupied conductors;
a complete-fibre Fourier/Plancherel bound;
support collision alone;
bounded cell-kernel rank;
partial Frobenius on the cell set without an atom lift.
```

The arithmetic grouping order is also load bearing. Splitting one already-paid
history group into many identical literal histories can create a large
occupancy defect without changing the grouped principal source.
