# R-103110 — Quarter-power fixed-owner Type-I does not close the coherent owner collapse

Claim ID: `R-103110`  
Status: **BINDING PROOF-GAP CORRECTION; QUARTER-POWER SUPPORT LEMMA RETAINED**  
Created: 2026-08-26  
Reviewed target: PR #719 quarter-power packet landed at `e56c9813`; reconstructed at live head `8eea03836b23154a0990a4a870aa5bb3ecb7510d`  
Depends on: `L-102747`, `L-102953`, `R-102840`, `R-102875`, historical quarter-power files  
RH status: **unproved**

## 1. What survives

Fix one dyadic physical block `Y<=X<2Y`, one dyadic owner-product block
`A<=P<2A`, and

\[
 V_A=\left\lfloor(2Y/A)^{1/4}\right\rfloor .
\]

For a fixed owner/exclusion fibre, the squarefree zero-moment lattice gives

\[
 \left|\mathcal T^{K,(R)}_{V_A,\mathrm{sf}}(X/P)\right|
 \ll Y^{o(1)}V_A(X/P)^{-1/4}=Y^{o(1)}.
\]

The balanced equal-pair core at the same cutoff is support-empty because every
nonzero core contains two disjoint factors larger than `V_A`, and hence
`P a^2>2Y>X`.

These are valid fixed-fibre and support statements.

## 2. The first invalid implication

The historical `L-103070.6` passed from the fixed-owner estimate to the
complete physically collapsed owner sum using only:

```text
canonical equal-pair multiplicity O(log^2 Y);
O(log Y) dyadic owner-product blocks.
```

That is not sufficient. `L-102747` controls only the several owner-pair
coordinates representing the **same labelled occurrence/equal physical
product**. It does not control coherent cross terms between distinct physical
products having different owner products.

The frozen theorem `L-102953` controls the squarefree core lattice in one fixed
owner/exclusion fibre (and the historical unpaired Type-I row). It does not
prove a contraction for the block-dependent equal-pair lift

\[
 \bigoplus_P \mathcal T_{V(P)}
 \longrightarrow
 \sum_P^{\rm physical}\mathcal T_{V(P)}.
\]

The latter map is exactly the owner-indexed physical restriction isolated by
`R-102875` and the source-blind coherence countermodel `R-102840`.

## 3. Exact diagnostic: the new Type-I row is the hard row

Let `E_P` denote the canonical equal-pair lift in owner fibre `P`, and let
`Pi_A` project onto `A<=P<2A`. The Boolean identity gives, coefficientwise,

\[
 E_P\mu_{\rm sf}=E_P\mathcal T_{V_A}+E_P\mathcal B_{V_A}.
\]

The quarter-power support theorem gives

\[
 \mathcal O_{K_L}[E_P\mathcal B_{V_A}]=0
\]

on the dyadic block. Therefore

\[
\boxed{
 \mathcal O_{K_L}[E_P\mu_{\rm sf}]
 =
 \mathcal O_{K_L}[E_P\mathcal T_{V_A}].
}
\tag{R-103110.1}
\]

After summing owner fibres, the right side is not an easier inherited Type-I
object. It is exactly the harmonic/BCI physical field in a new coordinate.
Thus a subpower estimate for the complete quarter-power Type-I lift is already
conclusion-bearing.

## 4. Source-blind finite model

Let `e_j` be orthonormal owner labels and let `phi` be one compact field. The
labelled packet

\[
 F_N=N^{-1/2}\sum_{j=1}^N e_j\phi
\]

has bounded labelled norm. Physical collapse sends every `e_j phi` to the same
field and gives

\[
 \|\operatorname{Coll}F_N\|^2=N\|\phi\|^2.
\]

This model satisfies fixed-fibre bounds and contains no same-occurrence
multiplicity problem. It disproves the inference from those facts to a uniform
physical collapse bound. It is an implication counterexample, not a
counterexample to the literal arithmetic estimate.

## 5. Disposition

```text
quarter-power balanced support-empty theorem          VERIFIED
fixed-owner/core Type-I endpoint                       VERIFIED
complete coherent owner assembly in old L-103070.6    UNPROVEN / GAP
old L-103072 BCI conclusion                            UNPROVEN / GAP
old T-103080 complete proposal                         SUPERSEDED
BCI102990                                               OPEN / RH-BEARING
RH                                                      UNPROVED
```

The corrected frontier is `T-103110`.