# L-29802 — Positive boundary cone and eta–Pascal invariance

Claim ID: `L-29802`  
Title: Every sign-normalized cutoff jet propagates inside one positive lower-scale Pascal cone, with strict eta mass-plus-cost factor below one and no feedback into the analytic bulk  
Status: **PROPOSED COMPLETE SOURCE-TYPING LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro-global`  
Created: 2026-08-08  
Issue: #298  
Dependencies: `L-29801`; PR #286 `L-28402`; PR #294 `L-28301/L-28302`; PR #272 balanced Pascal current algebra  
Scope: all-generation boundary source typing; no final RH conclusion

## 1. The eta boundary pair

For `k>=1`, put

\[
 a_k={1\over2k},
 \qquad
 c_k={1\over2k+1}.
\tag{L-29802.1}
\]

The complete logarithmic eta boundary source is

\[
 \mathfrak b
 =\sum_{k\ge1}[a_ke_{2k}-c_ke_{2k+1}].
\tag{L-29802.2}
\]

For each pair,

\[
\boxed{
 a_ke_{2k}-c_ke_{2k+1}
 =(a_k-c_k)e_{2k}+c_k(e_{2k}-e_{2k+1}).
}
\tag{L-29802.3}
\]

Both coefficients on the right are nonnegative and `c_k<a_k`.

The dipole is the exact carry image of the balanced sibling switch

\[
 [2k+2k]\longrightarrow[(2k-1)+(2k+1)]
\tag{L-29802.4}
\]

at parent `4k`.  Its exact logarithmic objective cost is

\[
 c_k\log{2k+1\over2k}.
\tag{L-29802.5}
\]

The switch consumes only `c_k` of the available central coefficient `a_k`, leaving the nonnegative residual `a_k-c_k`.

## 2. Strict local budget

The residual mass is

\[
 \rho=\sum_{k\ge1}(a_k-c_k)=1-\log2.
\tag{L-29802.6}
\]

Using `log(1+x)<x`,

\[
 c_k\log{2k+1\over2k}
 <{1\over2k(2k+1)}
 =a_k-c_k.
\tag{L-29802.7}
\]

Therefore the complete logarithmic cost satisfies

\[
 \mathfrak c
 =\sum_{k\ge1}c_k\log{2k+1\over2k}
 <\rho,
\tag{L-29802.8}
\]

and

\[
\boxed{
 \theta_*:=\rho+\mathfrak c
 <2(1-\log2)<1.
}
\tag{L-29802.9}
\]

The strict inequality follows already from

\[
 \log2=2\left({1\over3}+{1\over3^3\cdot3}+\cdots\right)>{2\over3}.
\]

Hence one may use the rational review bound

\[
 \theta_*<{2\over3}.
\tag{L-29802.10}
\]

## 3. Tensoring with an arbitrary positive jet type

Let `v` be any formal boundary-source type with nonnegative coefficient.  It may represent:

- a Peano finite-difference jet of any fixed order;
- an endpoint delta-jet type;
- an exact Euler remainder type;
- a finite vector of common-destination source coefficients.

Tensoring (L-29802.3) with `v` gives

\[
 a_k(e_{2k}\otimes v)-c_k(e_{2k+1}\otimes v)
 =(a_k-c_k)(e_{2k}\otimes v)
 +c_k[(e_{2k}-e_{2k+1})\otimes v].
\tag{L-29802.11}
\]

The first term remains in the same positive jet type.  The second is realized by the same balanced sibling switch, now carrying the complete internal label `v`.

Because translation, finite difference, and the Pascal boundary operator commute with the formal jet label, no new sign is introduced.  The capacity inequality remains `c_k<a_k` coefficientwise.

Thus the eta–Pascal dictionary is valid simultaneously for every jet order and every nonnegative Peano source coefficient.

## 4. Euler transformation does not enlarge the boundary budget

For a positive decreasing sequence `A_j`, the exact finite Euler expansion is

\[
 \sum_{j\ge K}(-1)^{j-K}A_j
 =\sum_{m=0}^{M-1}2^{-m-1}\Delta^mA_K
  +2^{-M}\sum_{j\ge K}(-1)^{j-K}\Delta^MA_j.
\tag{L-29802.12}
\]

All source coefficients on the right are nonnegative by `L-29801`.  The scalar weights satisfy

\[
 \sum_{m=0}^{M-1}2^{-m-1}+2^{-M}=1.
\tag{L-29802.13}
\]

Therefore Euler export merely partitions one unit of positive boundary source among finitely many jet labels and one exact remainder.  Applying the eta–Pascal dictionary after this partition still costs at most `theta_*` times the incoming boundary source.  The Euler remainder does not create an additional same-scale loss.

This is the precise reason the constants `2^{-M}` and `theta_*` must not be added as unrelated operator norms.

## 5. No boundary-to-bulk feedback

The analytic bulk consists of unrestricted pure-power channels.  The boundary cone consists of first-omitted quotient jets and their Pascal-current realizations at the next half endpoint.

PR #286 `L-28402` proves that every boundary destination is attached to

\[
 N^+=\left\lfloor{N+1\over2}\right\rfloor.
\tag{L-29802.14}
\]

PR #294 `L-28302` realizes every eta dipole entirely inside the balanced Pascal current space at that destination.  No operation in (L-29802.11)--(L-29802.13) recreates an unrestricted current-endpoint power tail.

Consequently the exact source graph is triangular:

```text
analytic bulk  -> analytic bulk + lower-scale boundary cone;
boundary cone  -> lower-scale boundary cone only.
```

In particular, the block from the boundary state back to the current analytic bulk is exactly zero.  This no-feedback statement is load bearing.

## 6. Common-destination recombination

Several Euler jets or eta pairs may arrive at the same arithmetic destination.  They are added in the positive source coefficient before a capacity or debt norm is taken.

Because all incoming coefficients in the sign-normalized boundary cone are nonnegative, recombination cannot create a negative source coordinate.  The corresponding sibling-switch amounts add, and their total remains bounded by the total available central coefficient at that destination:

\[
 \sum c_k v_k\le\sum a_k v_k.
\tag{L-29802.15}
\]

This is exactly the source-level capacity condition.  It does not require a generic ambient operator norm or a post hoc clipping step.

## 7. Finite collar

The finitely many rows below the analytic threshold, the first omitted quotient conventions, and endpoint coincidences are retained as one collar state.  PR #286 gives a polylogarithmic first-generation capacity bound for this complete ledger.

Under half-scale iteration there are only `O(log X)` endpoint levels.  A polynomial or polylogarithmic collar forcing is therefore harmless once the homogeneous boundary transition has factor `theta_*<1`.

No boundary row is deleted; the collar is an explicit inhomogeneous term in the recurrence of `L-29803`.

## 8. Proof boundary

Closed here, subject to independent review:

1. the strict eta mass-plus-cost budget;
2. exact local capacity feasibility of every sibling switch;
3. tensoring with every positive Peano/endpoint jet type;
4. conservation of source mass under finite Euler export;
5. invariance of the positive boundary cone;
6. the exact absence of boundary-to-bulk feedback;
7. common-destination capacity preservation.

Not proved in this file:

1. the global two-state recurrence;
2. Cycle Debt;
3. RH.
