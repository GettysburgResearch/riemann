# T-106451 — Denominator-free full-signature frontier for ninety percent

Claim ID: `T-106451`  
Status: **EXACT REDUCTION; HBSIG106451 OPEN**  
Created: 2026-08-25  
Depends on: `L-106451`; pinned unconditional fixed-order input `R_4/N>2487/2500-o(1)`  
RH status: **unproved**

Let `p_T` be a symmetric regular canonical-product truncation of Xi on one
dyadic window and put

\[
q_T=p_T^{(4)}.
\]

Define the real Hermite--Bézout matrix

\[
\boxed{
\mathfrak B_T
 =\operatorname{Bez}
  \left(p_Tq_T,
        p_T'q_T-p_Tq_T'\right).
}
\tag{T-106451.1}

`L-106451` proves

\[
\boxed{
\operatorname{sig}\mathfrak B_T
 =R_0(T,2T)-R_4(T,2T)+o(N(T,2T)).
}
\tag{T-106451.2}

The endpoint, common-factor and confluent corrections are finite-rank and are
retained in the `o(N)` ledger under the usual regular exhaustion.

## 1. Exact fixed-constant target

The pinned unconditional fourth-derivative theorem gives

\[
{R_4(T,2T)\over N(T,2T)}
 >{2487\over2500}-o(1).
\]

Therefore

```text
HBSIG106451:

liminf_(T->infinity)
  sig(B_T)/N(T,2T)
> -237/2500
```

implies

\[
\boxed{
\liminf_{T\to\infty}
{N_0(T,2T)\over N(T,2T)}>0.9.
}
\tag{T-106451.3
}

This target is exactly equivalent to the desired fixed-order descent at the
truncation scope.  Its value is organizational: unlike the resolvent Hankel
norm, `B_T` is polynomial and denominator-free, and its CRT source labels are
literal.

## 2. Source-normalized rank--trace route

Let `S_T` be any predeclared injective source map into the coefficient space of
`B_T`, and put

\[
M_T=S_T^*\mathfrak B_TS_T.
\]

A proof may use any positive source metric `G_T>0`; congruence gives

\[
\operatorname{sig}M_T
 =\operatorname{sig}\mathfrak B_T
\]

when `S_T` is square and invertible, and gives the corresponding lower
interlacing bound under controlled codimension otherwise.

The concrete source-side theorem to seek is

```text
HBRT106451:
  construct a source-owned G_T and a codimension-o(N) map S_T such that a
  verified rank--trace/stability inequality forces

    sig(G_T^(-1/2) M_T G_T^(-1/2))
      > -(237/2500-o(1))N.
```

The endpoint exterior-square density of `L-106440` identifies every matrix
entry of the perturbation source; the fixed-order Xi derivative theorem pays
the high endpoint.  The missing input is the source-basis signature estimate,
not a denominator inversion.

## 3. Relation to PR #726

PR #726 develops a full-signature Hermite--Pick/Wick rank--trace machine.  The
matrix `B_T` supplies a collision-safe conclusion-facing target for that
machinery:

```text
no holomorphic identity carrier;
no denominator-multiplied Hankel source;
no post hoc sign selection;
literal p-root versus p^(4)-root CRT fibres.
```

Importing any PR #726 inequality requires an exact source-map and normalization
match; theorem names alone are not a composition.

## 4. Boundary

```text
endpoint Hermite--Bezout identity             PROVED EXACT
CRT +/- root-fibre diagonalization            PROVED EXACT
signature = R_0-R_4                           PROVED EXACT
HBSIG106451 fixed 9.48% signature estimate    OPEN / RECORD-BEARING
HBRT106451 source rank--trace realization     OPEN
ninety percent for zeta                       UNPROVED
density one                                   UNPROVED
Riemann Hypothesis                            UNPROVED
```