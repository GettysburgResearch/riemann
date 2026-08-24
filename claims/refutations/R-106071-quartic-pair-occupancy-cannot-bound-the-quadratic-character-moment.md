# R-106071 — Quartic matched-pair occupancy cannot bound the quadratic character moment

Claim ID: `R-106071`  
Status: **PROVED EXACT HOMOGENEITY AND OWNER-COHERENCE FIREWALL**  
Created: 2026-08-25  
Depends on: `L-106001`, `L-106060`, `L-106071--L-106073`, `T-106070`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

The first version of `T-106070` attempted to replace the quadratic
same-residue occupancy in the character moment by a sum of squared
rank-one owner-pair tensors.  This replacement is false.

## 1. The exact quadratic family object

For one unramified block-colour packet write its Hilbert-valued source atoms as

\[
z_{P,c},
\qquad n=P c^2,
\]

and, modulo the selected prime \(\ell\), put

\[
A_r=
\sum_{P c^2\equiv r\pmod\ell}z_{P,c}.
\tag{R-106071.1}
\]

Complete character orthogonality gives the exact normalized family moment

\[
\boxed{
\frac1{\ell-1}
\sum_{\chi\;({\rm mod}\ \ell)}
\left\|
\sum_{P,c}\chi(Pc^2)z_{P,c}
\right\|^2
=
\sum_{r\ne0}\|A_r\|^2.
}
\tag{R-106071.2}
\]

Both sides are homogeneous of degree two in the source atoms.

## 2. The quantity used in the failed adapter is quartic

For a fixed matched owner pair \((P,Q)\), `L-106071` formed rank-one vectors

\[
W_{P,Q;d}
=z_{P,c(d)}\otimes\overline{z_{Q,d}}
\]

and bounded

\[
D_{P,Q}
=
\sum_d\|W_{P,Q;d}\|^2
=
\sum_d
\|z_{P,c(d)}\|^2\|z_{Q,d}\|^2.
\tag{R-106071.3}
\]

After summing owner pairs this remains homogeneous of degree four.  Therefore
no source-independent estimate of the form

\[
\sum_r\|A_r\|^2
\ll
\ell\sum_{P,Q}D_{P,Q}
\tag{R-106071.4}
\]

can hold: replacing every source atom by \(\lambda z_{P,c}\) multiplies the
left side by \(|\lambda|^2\) and the right side by \(|\lambda|^4\).

## 3. Exact finite counterfixture

Take \(N\) distinct owner labels, one core label, and arrange all physical
indices in one nonzero residue class.  Let

\[
z_j=N^{-1}e
\qquad(1\le j\le N)
\]

for a unit Hilbert vector \(e\).  Then

\[
\sum_r\|A_r\|^2
=
\left\|\sum_{j=1}^Nz_j\right\|^2
=1,
\tag{R-106071.5}
\]

whereas the complete quartic owner-pair tensor occupancy is

\[
\sum_{i,j}\|z_i\|^2\|z_j\|^2
=
\left(\sum_j\|z_j\|^2\right)^2
=
\frac1{N^2}.
\tag{R-106071.6}
\]

For \(N>\sqrt{C\ell}\), (R-106071.4) fails for any proposed absolute constant
\(C\).

The fixture is exactly the owner-coherence left unresolved by the partial
matching theorem: scale matching prevents several **cores** for one fixed
owner pair from occupying one root residue, but it does not prevent many
owner packets from occupying the same physical residue cell.

## 4. What remains valid

The following statements survive unchanged:

```text
three-prime linear block palette;
coefficientwise unramified principal recovery;
partial-matching geometry for each fixed owner pair;
representation aggregation for one physical core;
quartic Hilbert--Schmidt bound for matched owner-pair tensors;
conductor payment for that quartic tensor quantity.
```

What does not survive is the implication from that quartic quantity to the
quadratic family moment or to `HBCQDSP102888`.

## 5. Correct replacement

The conclusion-facing object must retain the coherent sum over all owners in
each residue cell:

\[
\boxed{
\mathcal Q_{\mathcal B,A}(X)
=
\sum_{r\in\mathbf F_\ell^*}
\left\|
\sum_{P c^2\equiv r\pmod\ell}
 z_{P,c}(X)
\right\|^2.
}
\tag{R-106071.7}
\]

The exact missing estimate is a quadratic, scale-matched owner-residue
occupancy theorem for \(\ell\mathcal Q_{\mathcal B,A}\), stated in
`T-106071`.  It is a block-coordinate form of the global physical occupancy
frontier `BPOE103300`.

## Binding consequence

`L-106073` and the first version of `T-106070` are retracted.  Their failure is
not in Bertrand's postulate, line injectivity, or the block energy estimate; it
is specifically the false quartic-to-quadratic adapter.

This refutation prevents an invalid claim of the Riemann Hypothesis and defines
the exact theorem still required.