# L-106071 — Scale-matched collision lines are partial matchings of physical cores

Claim ID: `L-106071`  
Programme aliases: `LFAM1.INJECTIVE_COLLISION_LINES`, `STRESS.ROOT_RESIDUE_MATCHING`, `LFAM2.ARTIN_SCHREIER_BLOCK_MATCHING`  
Status: **PROVED EXACT CORE-MATCHING THEOREM; QUARTIC SHADOW NON-CONCLUSION-FACING**  
Created: 2026-08-25  
Corrected: 2026-08-25  
Depends on: `L-106001`, `L-106060`, `L-106070`; parent `L-102883--L-102886`; `R-106071`  
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

Hence the equal-owner diagonal is isolated without a repeated-core residue
multiplicity.

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

## 4. Valid quartic matched-pair shadow

For one fixed owner pair and line, form the rank-one tensor

\[
W_{P,Q,\pm;d}
=
Z_{P,c(d)}\otimes\overline{Z_{Q,d}}.
\tag{L-106071.7}
\]

Then

\[
\|W_{P,Q,\pm;d}\|^2
=
\|Z_{P,c(d)}\|^2\|Z_{Q,d}\|^2.
\]

Because the line is a partial matching,

\[
\boxed{
\sum_d\|W_{P,Q,\pm;d}\|^2
\le
\left(\sum_c\|Z_{P,c}\|^2\right)
\left(\sum_d\|Z_{Q,d}\|^2\right).
}
\tag{L-106071.8}
\]

Equation (L-106071.8) is a correct quartic Hilbert--Schmidt estimate for the
matched owner-pair tensor.  It is useful as a mutation check and for genuinely
quartic observables.

It is **not** the quadratic occupancy required by the character family.  The
exact family quantity is instead

\[
\sum_{r\ne0}
\left\|
\sum_{Pc^2\equiv r}Z_{P,c}
\right\|^2,
\]

as proved in `L-106074`.  `R-106071` gives a scaling counterexample to replacing
that quadratic Gram by the quartic left side of (L-106071.8).

## 5. What the matching theorem actually removes

The theorem removes:

```text
multiple lifts of one core residue in a dyadic block;
multiple partners for one fixed core inside one fixed owner-pair line;
overlap of the plus and minus square-root lines;
representation multiplicity beyond the divisor-function ledger.
```

It does not remove:

```text
many different owner packets occupying the same residue cell;
quadratic coherence among those owner packets;
the global physical observation norm BPOE103300.
```

## Scope

The exact core matching and representation statements remain proved.  The
original claim that (L-106071.8) was the missing conclusion-facing occupancy
estimate is withdrawn.  The corrected quadratic normal form is `L-106074`, and
the current frontier is `T-106071`.