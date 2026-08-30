# T-108430 — Source-weighted shared-fibre frontier

Claim ID: `T-108430`  
Status: **EXACT MINIMAL POSITIVE-SOURCE REDUCTION; ARITHMETIC CELL ENERGY AND RH OPEN**  
Created: 2026-08-31  
Depends on: `L-108430`, `R-108430`; the reduced Kummer and principal-binding ledger of PR #771  
RH/GRH status: **unproved**

For each grouped live shared-conductor fibre `iota`, retain the literal
source-dual coefficients

\[
z_{\iota,\omega}(t)
\]

with every mask, owner, cofactor, endpoint, marked-prime and Mellin label
fixed as in the frozen source. Define the physical cell sum

\[
Z_{\iota,a}(t)
=
\sum_{\omega:r_\iota(\omega)=a}
z_{\iota,\omega}(t).
\tag{T-108430.1}
\]

Let `w_iota` denote the exact positive exterior weight already present in the
connected-Kummer consumer and let `dmu` be its original Mellin measure. Put

\[
\boxed{
\mathfrak C_{\rm cell}(X)
=
\sum_\iota w_\iota
\int
\sum_a|Z_{\iota,a}(t)|^2\,d\mu(t).
}
\tag{T-108430.2}
\]

`L-108430` proves that the complete positive nonresonant Wick contribution of
the literal source is at most (T-108430.2). No occupancy multiplicity,
faithful carrier rank, Hellinger distance or source-piece triangle inequality
appears.

Define

```text
COEFCELL108430:
  the quantity in (T-108430.2), together with the exact live-mask completion
  boundary at the same normalization, is X^o(1).
```

Retain

```text
QRESBIND107300:
  the at-most-three quadratic/constant resonance rows, endpoints and
  principal member are recombined and bound with their exact weights.
```

Then the existing source-locked adapters give

\[
\boxed{
\mathrm{COEFCELL}_{108430}
\wedge
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
\tag{T-108430.3}
\]

Neither premise is proved.

## 1. Rectangular character form

For a native rectangular piece with

\[
z_{ij}=\overline{a_i}b_j,
\]

write `A_y` and `B_x` for the one-sided coefficient aggregates. Then

\[
\boxed{
\sum_{x,y}|Z_{x,y}|^2
=
\left(\sum_y|A_y|^2\right)
\left(\sum_x|B_x|^2\right).
}
\tag{T-108430.4}
\]

By Parseval, this is exactly the product of two complete one-sided character
energies, including the principal and quadratic modes. The nonresonant modes
may be compared with PR #771's rank-free twisted Plancherel theorem only after
the literal source masks and coefficient weights are retained.

## 2. Source pieces must be assembled first

If several source-authorized rectangles land in the same cell, their
coefficients are summed in (T-108430.1) before taking the square. This permits
cross-rectangle cancellation. The positive Hellinger mixture theorem remains
valid, but applying it piecewise can lose precisely this native interference.

Thus `FROBMIX108420` is demoted from the canonical target to a stronger
source-blind sufficient condition. It is not used in (T-108430.3).

## 3. What remains genuinely arithmetic

The unresolved object is now one literal signed coefficient energy:

```text
full native source
  -> exact physical cell aggregation
  -> one squared norm
  -> explicit finite resonance/principal ledger.
```

This is the same kind of source-faithful cross-group cancellation that appears
in the core-wavelet, XD and connected-Kummer formulations. It has not been
proved by the finite operator algebra in this branch.

```text
positive source-vector quotient bound      PROVED EXACT
native rectangular factorization           PROVED EXACT
unweighted occupancy as necessary target   REFUTED
FROBMIX108420 canonical status              SUPERSEDED BY SHARPER GATE
COEFCELL108430                              OPEN
QRESBIND107300                              OPEN
RH / GRH                                    UNPROVED
```
