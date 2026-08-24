# L-106071 — Scale-matched collision lines are partial matchings of physical cores

Claim ID: `L-106071`  
Programme aliases: `LFAM1.INJECTIVE_COLLISION_LINES`, `STRESS.ROOT_RESIDUE_MATCHING`, `LFAM2.ARTIN_SCHREIER_BLOCK_MATCHING`  
Status: **PROVED EXACT HILBERT-OCCUPANCY THEOREM**  
Created: 2026-08-25  
Depends on: `L-106001`, `L-106060`, `L-106070`; parent `L-102883--L-102886`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Fix one block-colour piece \((\mathcal B,A)\) of `L-106070`, write

\[
B=UVM,
\qquad
\ell=\ell(B,A),
\]

and retain all finite carrier, marked-prime, gauge and outer-observation
labels.  Every core lies in \([B,8B)\), every owner product in the colour is
coprime to \(\ell\), and

\[
\ell>16B.
\tag{L-106071.1}
\]

## 1. Character collisions

For two owner squareclasses \(P,Q\) in the same colour, complete character
orthogonality selects

\[
P c^2\equiv Q d^2\pmod\ell.
\tag{L-106071.2}
\]

In a marked-\(67\) sector \((e,f)\in\{0,1\}^2\), replace the ratio by

\[
67^{f-e}QP^{-1}\pmod\ell.
\]

Since \(\ell\ne67\), the following argument is unchanged.

If the owner ratio is a nonsquare, the sector is empty.  If it is a square,
choose \(\tau\in\mathbf F_\ell^\times\) with the appropriate square and obtain
the two exact lines

\[
\boxed{
c\equiv \tau d\pmod\ell
\quad\text{or}\quad
c\equiv-\tau d\pmod\ell.
}
\tag{L-106071.3}
\]

## 2. Each line is a partial matching

The interval \([B,8B)\) has length \(7B<\ell\).  For fixed \(d\), either
congruence in (L-106071.3) therefore has at most one lift \(c\) in the block.
Because multiplication by \(\tau\) is invertible, the same is true with
\(c,d\) interchanged.

Thus each sign in (L-106071.3) defines a partial matching

\[
\mathcal L_{P,Q,\pm}
\subset [B,8B)\times[B,8B).
\tag{L-106071.4}
\]

The two matchings are disjoint: an intersection would give
\(2\tau d\equiv0\pmod\ell\), impossible because \(\ell\) is odd and
\(0<d<\ell\).

For \(P=Q\) in the unmarked sector, the plus line is exactly \(c=d\).  The
minus line is empty because

\[
0<c+d<16B<\ell.
\]

Hence the equal-owner diagonal is isolated without a residue multiplicity.

## 3. Representation aggregation

Let \(z_{P;u,v,m}\) be the complete Hilbert-valued source atom attached to one
literal representation \(c=uvm\), including its coefficient, fixed kernel
translate and every retained finite label.  Aggregate only equal physical
cores:

\[
\boxed{
Z_{P,c}
=
\sum_{\substack{u\sim U,\,v\sim V,\,m\sim M\\uvm=c}}
 z_{P;u,v,m}.
}
\tag{L-106071.5}
\]

The number of representations in a fixed block is at most \(d_3(c)\), and the
complete inherited representation ledger is \(X^{o(1)}\).  Therefore

\[
\boxed{
\sum_c\|Z_{P,c}\|^2
\le
X^{o(1)}
\sum_{u,v,m}\|z_{P;u,v,m}\|^2.
}
\tag{L-106071.6}
\]

No different physical products have been identified in (L-106071.5).

## 4. Root-residue occupancy has product-energy cost

For a surviving line, let \(W_{P,Q,\pm;d}\) be its root-residue vector after
the inherited bounded phase, carrier and observation maps.  Before the final
bounded observation it is a rank-one tensor of the matched core aggregates;
there is an absolute kernel constant \(C_K\) such that

\[
\|W_{P,Q,\pm;d}\|^2
\le
C_K
\|Z_{P,c(d)}\|^2
\|Z_{Q,d}\|^2.
\tag{L-106071.7}
\]

Define

\[
D_{P,Q,\pm}
=
\sum_{d:\,(c(d),d)\in\mathcal L_{P,Q,\pm}}
\|W_{P,Q,\pm;d}\|^2.
\]

Because the line is a partial matching,

\[
\boxed{
D_{P,Q,\pm}
\le
C_K
\left(\sum_c\|Z_{P,c}\|^2\right)
\left(\sum_d\|Z_{Q,d}\|^2\right).
}
\tag{L-106071.8}
\]

This is the missing local occupancy estimate in `T-106060`: no coherent sum
over several physical cores remains inside one root residue.

Common-square extraction only inserts the favorable factor \(g^{-2}\), and
internal discrepancy phases are unitary.  Hence (L-106071.8) is uniform over
the equal-core, one-sided and two-sided packets when they remain recombined in
the complete source ledger.

## Scope

The theorem proves exact injectivity and reduces root-residue occupancy to the
product of two aggregated diagonal energies.  It does not yet show that the
factor \(\ell\) required by principal leverage is harmless.  That quantitative
payment is the content of `L-106072`.