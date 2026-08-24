# L-106027 — Two owner quadratic classes preserve the sharp local leverage

Claim ID: `L-106027`  
Programme aliases: `LFAM1.OWNER_SQUARECLASS_PARTITION`, `STRESS.TWO_CLASS_OCCUPANCY`  
Status: **PROVED EXACT GLOBAL-INDEXING CORRECTION**  
Created: 2026-08-24  
Depends on: `L-106020`, `L-106024`; `R-106020`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

The strict square-phase contraction is a theorem for packets supported in one
multiplicative squareclass modulo the phase prime. When many owner pairs are
assembled at one conductor, their owner products need not all lie in the same
squareclass. This theorem gives the exact required partition.

Fix an odd owner conductor `rho`, and let `kappa_rho` be its quadratic
character. For every clean owner pair `P`, define

\[
\sigma(P)=\kappa_\rho(P)\in\{+1,-1\}.
\tag{L-106027.1}
\]

Partition the source-owned packet into

\[
\mathcal P_+=\{P:\sigma(P)=+1\},
\qquad
\mathcal P_-=\{P:\sigma(P)=-1\}.
\tag{L-106027.2}
\]

## 1. One squareclass per sector

For fixed `sigma`, all physical residues

\[
P a^2\pmod\rho,
\qquad P\in\mathcal P_\sigma,
\]

lie in one coset of the square subgroup of `F_rho^*`. Therefore the complete
coherent field inside that sector is still a packet of the form required by
`L-106020` and `L-106024`, after choosing one representative `u_sigma` of the
coset.

Consequently, if `F_(sigma,h)` is the coherent additive phase field of the
sector, then

\[
\boxed{
\|F_{\sigma,0}\|^2
\le{\rho-1\over\rho+1}
\sum_{h\ne0}\|F_{\sigma,h}\|^2.
}
\tag{L-106027.3}
\]

The inequality remains sharp within each sector.

## 2. Principal/quadratic root fibre

Under the Gauss--Mellin transform, the two roots of the principal even
character are `1` and `kappa_rho`. On `mathcal P_sigma`,

\[
\kappa_\rho(P)=\sigma
\]

is constant. Hence the coherent quadratic-root field is exactly `sigma` times
the coherent principal-root field. Their squared Gauss weights combine as

\[
1+\rho.
\]

Thus the coefficient `(rho+1)/(rho-1)` in the local principal embedding remains
valid **after coherent summation inside one owner quadratic class**.

## 3. Recombination cost

The full unphased field is

\[
F_0=F_{+,0}+F_{-,0}.
\]

Therefore

\[
\boxed{
\|F_0\|^2
\le2\bigl(\|F_{+,0}\|^2+\|F_{-,0}\|^2\bigr)
\le2{\rho-1\over\rho+1}
\sum_{\sigma=\pm1}\sum_{h\ne0}\|F_{\sigma,h}\|^2.
}
\tag{L-106027.4}
\]

Only the absolute constant `2` is paid. There is no conductor or family-size
loss.

## 4. Firewall

If the two owner quadratic classes are aggregated before the square-phase
transform, the residues may occupy all of `F_rho^*`. On the full residue space,
the phase Gram `rho I-J` has constant-mode eigenvalue `1`, and the physical
observation norm squared becomes `rho-1`; the strict contraction disappears.

Thus every coherent owner-conductor moment must retain the index

```text
sigma = kappa_rho(P)
```

until after the local occupancy theorem is applied. This index is included in
the explicit moment `T-106030`.

The theorem proves no cross-conductor assembly and no RH result.
