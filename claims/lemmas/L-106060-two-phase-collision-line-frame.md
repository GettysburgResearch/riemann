# L-106060 — Two nonzero linear phases give a sharp collision-line contraction

Claim ID: `L-106060`  
Programme aliases: `LFAM1.TWO_PHASE_LINE_FRAME`, `LFAM2.ARTIN_SCHREIER_LINE_FRAME`, `STRESS.COLLISION_LINE_CONTRACTION`  
Status: **PROVED EXACT HILBERT-VALUED FRAME THEOREM**  
Created: 2026-08-24  
Depends on: finite additive orthogonality; `R-106060`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Let `k=F_Q` be a finite field, let `H` be a complex Hilbert space, let `psi`
be a nontrivial additive character, and fix `tau in k^*`. For an arbitrary
packet `(w_x)_(x in k^*)`, put

\[
S=\sum_{x\in k^*}w_x,
\qquad
D=\sum_{x\in k^*}\|w_x\|^2.
\tag{L-106060.1}
\]

For either choice of sign, define

\[
F_{\alpha,\beta}^{\pm}
=
\sum_{x\in k^*}
 w_x\psi((\pm\tau\alpha+\beta)x),
\qquad
\alpha,\beta\in k^*.
\tag{L-106060.2}
\]

## 1. Exact two-phase energy

For `x=y`, each nonzero phase sum contributes `Q-1`. For `x!=y`, each
contributes `-1`. Therefore

\[
\boxed{
\sum_{\alpha,\beta\ne0}
\|F_{\alpha,\beta}^{\pm}\|^2
=
Q(Q-2)D+\|S\|^2.
}
\tag{L-106060.3}
\]

The identity is independent of `tau` and of the sign.

Equivalently, the phase-pair map

\[
(\alpha,\beta)\longmapsto\pm\tau\alpha+\beta
\]

has multiplicity `Q-1` over zero and `Q-2` over every nonzero field element.
Combining this count with additive Plancherel gives the same formula.

## 2. The coherent phase sum

Because `x!=0`,

\[
\sum_{\alpha\ne0}\psi(\pm\tau\alpha x)=-1,
\qquad
\sum_{\beta\ne0}\psi(\beta x)=-1.
\]

Hence

\[
\boxed{
\sum_{\alpha,\beta\ne0}
F_{\alpha,\beta}^{\pm}=S.
}
\tag{L-106060.4}
\]

Since there are `Q-1` root residues,

\[
\|S\|^2\le(Q-1)D.
\]

Substitution into (L-106060.3) yields the sharp contraction

\[
\boxed{
\left\|
\sum_{\alpha,\beta\ne0}F_{\alpha,\beta}^{\pm}
\right\|^2
\le
\frac{Q-1}{Q^2-Q-1}
\sum_{\alpha,\beta\ne0}
\|F_{\alpha,\beta}^{\pm}\|^2.
}
\tag{L-106060.5}
\]

Equality holds when all aggregated root-residue vectors `w_x` are equal. The
constant is asymptotic to `1/Q`.

By contrast, `R-106060` proves that one phase direction alone can cost `Q-1`.
The contraction is genuinely conjunctive: both source-exact phase variables
are necessary.

## 3. Auxiliary character collision lines

In `L-106001`, complete character orthogonality reduces a surviving clean
squareclass correlation to

\[
c=\pm\tau d\pmod\ell.
\]

Because `c,d` are nonzero modulo `ell`, the two Ramanujan identities

\[
\sum_{\alpha\ne0}e_\ell(\alpha c)=-1,
\qquad
\sum_{\beta\ne0}e_\ell(\beta d)=-1
\]

insert the two phases without changing the physical source. On the collision
line they become exactly (L-106060.2).

After all source terms with the same root residue `d mod ell` are aggregated
into a Hilbert vector `w_d`, the only quantity not diagonalized by the theorem
is

\[
\boxed{
D_\ell=\sum_{d\in\mathbf F_\ell^*}\|w_d\|^2.
}
\tag{L-106060.6}
\]

Thus the collision-line problem is reduced to a same-root-residue occupancy,
not an arbitrary coherent line sum.

## 4. Function-field degree shells

Let `mathfrak l` be irreducible of degree `r` over `F_q`, so its residue field
has cardinality `Q=q^r`. If the polynomial core degree is less than `r`, its
reduction is injective. Formula (L-106060.3) then applies directly to arbitrary
Möbius/Vaughan/Kummer weights on that degree shell after aggregation.

This is the exact Artin--Schreier phase mechanism required by the function-
field programme; geometric input is needed only for assembly across owner
irreducibles and for source pieces not covered by complete phase pairs.

## Scope

The theorem proves a sharp local line frame and identifies the remaining root-
residue occupancy. It does not bound that occupancy coherently over owner pairs,
prove `CROP106060`, `HCLM106001`, or RH.
