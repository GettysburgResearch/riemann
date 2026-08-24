# T-106060 — Two-phase collision lines reduce to one root-residue occupancy

Claim ID: `T-106060`  
Programme aliases: `LFAM1.ROOT_RESIDUE_OCCUPANCY`, `LFAM2.ARTIN_SCHREIER_OCCUPANCY`, `STRESS.TWO_PHASE_LINE_FRONTIER`  
Status: **EXACT REDUCTION; SUPERSEDED AS THE LIVE FRONTIER BY `T-106070`**  
Created: 2026-08-24  
Updated: 2026-08-25  
Depends on: `L-106001`, `L-106060`; `R-106060`; `T-106001`  
Programme issues: #743, #736, #737  
RH status: **see the unvalidated full proof proposal `T-106070`**

## Supersession notice

The reduction and two-phase inequalities below remain exact.  Its original
version required a predeclared subpower modulus and left `CROP106060` open.
`L-106070--L-106073` instead use a linear block/colour partition and a
scale-matched modulus \(16B<\ell<256B\).  The retained block energy pays the
full factor \(\ell\), producing the proposed closure in `T-106070`.

This file is retained as the exact interface which identifies the root-residue
quantity.  The current conclusion-facing claim is `T-106070`, and its hostile
review contract is `M-106070`.

The auxiliary completed-family route reduces every surviving clean owner ratio
to one of two lines

\[
c=\pm\tau d\pmod\ell.
\]

One inherited linear phase is insufficient: `R-106060` exhibits an exact
`ell-1` loss. Two source-exact phases together give the sharp contraction of
`L-106060`.

## 1. Exact line packet

For every dyadic block, marked local sector, auxiliary modulus `ell`, owner-
ratio root `tau`, line sign and deterministic source region, aggregate the
literal residual coefficients with the same root residue `d mod ell` into a
Hilbert vector

\[
w_{\mathfrak a,d}(X).
\]

The index `mathfrak a` retains every owner, cutoff, gauge, shell and completion
label not represented by `d`.

Put

\[
S_{\mathfrak a}(X)
=
\sum_{d\ne0}w_{\mathfrak a,d}(X)
\]

and

\[
D_{\mathfrak a}(X)
=
\sum_{d\ne0}\|w_{\mathfrak a,d}(X)\|^2.
\tag{T-106060.1}
\]

After inserting the two nonzero phases on `c` and `d`, the original coherent
line sum is recovered exactly. The two-phase frame gives

\[
\|S_{\mathfrak a}(X)\|^2
\le
(\ell-1)D_{\mathfrak a}(X),
\tag{T-106060.2}
\]

and, more structurally,

\[
\|S_{\mathfrak a}\|^2
\le
\frac{\ell-1}{\ell^2-\ell-1}
\sum_{\alpha,\beta\ne0}
\|F_{\mathfrak a;\alpha,\beta}\|^2.
\tag{T-106060.3}
\]

The first inequality displays the exact remaining obstruction: coherent
aggregation inside one root residue.

## 2. Historical root-residue occupancy theorem

The original formulation used a predeclared auxiliary-modulus schedule
satisfying

\[
\ell=X^{o(1)}
\]

on logarithmic blocks and defined

```text
CROP106060:
  after the full-source completion and exact HBC residual functor, the
  extraction-normalized, source-weighted logarithmic integral of

      sum_mathfrak_a ell * D_(mathfrak a)(X)

  over all surviving distinct-product collision-line sectors is Y^o(1).
```

The direct-sum Hilbert index `mathfrak a` is chosen before physical observation,
so no line is duplicated. The already-closed equal-product and parent long-
core rows are excluded.

By (T-106060.2), `CROP106060` controls the complete collision-line energy of
the auxiliary family. Hence the exact historical implication is

\[
\boxed{
\mathrm{CROP}_{106060}
\Longrightarrow
\mathrm{HCLM}_{106001}
\Longrightarrow
\mathrm{HBCQDSP}_{102888}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-106060.4}

`L-106072` proves the required weighted occupancy in the scale-matched,
block-coloured form, and `L-106073` composes it directly into the native HBC
residual.

## 3. Why this is a genuine conjunction

The two phase statements are individually insufficient:

```text
phase on c alone: exact dimension loss ell-1;
phase on d alone: exact dimension loss ell-1.
```

Only their same-occurrence product gives the order-`1/ell` contraction in
(T-106060.3). The phases may not be proved on separate source marginals and
multiplied after physical collapse.

## 4. Function-field consequence

For an irreducible conductor of degree `r`, the residue field has size
`Q=q^r`. On core degree shells below `r`, reduction is injective and the exact
same two-phase frame applies to arbitrary Möbius/Vaughan/Kummer weights.

Define `FFCROP106060` as the coherent owner-irreducible assembly of the
resulting root-residue energies. A geometric proof should identify whether
this occupancy is controlled by monodromy, a relative trace formula, or a
Deligne estimate after the constant/resonant strata are removed.

## Exact boundary

```text
one-phase collision-line control             REFUTED
exact two-phase line energy                   PROVED EXACT
sharp two-phase contraction                   PROVED EXACT
line sum -> root-residue occupancy            PROVED EXACT
historical small-modulus CROP formulation      SUPERSEDED
scale-matched weighted occupancy               CLAIMED PROVED IN L-106072
native HBC composition                         CLAIMED PROVED IN L-106073
full conclusion                                SEE T-106070 / M-106070
```
