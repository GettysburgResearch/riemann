# R-91561 — Target minus declared score is not the actual row-entropy debt

Claim ID: `R-91561`  
Status: **EXACT LOSS-DICTIONARY FIREWALL / CORRECTED BOUNDED-DEBT REPLACEMENT**  
Created: 2026-08-13  
Frozen target: PR #424 at `7c0927e9364e191c720d5a618928d99847ac8edd`  
Depends on: `L-91540`, `T-91541`, `T-91551`, PR #352  
RH status: **unproved**

## 1. Three different ledgers

A paired type carries:

\[
 T=\text{carry/SHARP target},
 \qquad
 S=\text{declared endpoint entropy score},
 \qquad
 R=(R_j)_{j\ge2}=\text{finite row}.
\]

The conclusion-producing packing score is

\[
 \mathcal H(R)=\sum_{j\ge2}R_jG_j.
\]

The native loss of PR #352 is of the form

\[
 \boxed{S-\mathcal H(R),}
\tag{R-91561.1}
\]

not `T-S`.

`L-91540.15` instead defines the local typed debt as

\[
 [D_T-D_S]_+.
\tag{R-91561.2}
\]

That quantity does not control (R-91561.1).

## 2. Exact one-atom countermodel

Take the admissible abstract paired type

\[
 (a_T,b_T,a_S,b_S,\kappa)=(1,0,1,0,0)
\]

at any `Y>0`, with one positive atom and no child. Then

\[
 D_T=D_S=\sqrt Y,
 \qquad
 D_R=0.
\]

Hence the debt declared in `L-91540` is

\[
 [D_T-D_S]_+=0,
\]

while the actual row-entropy loss is

\[
 D_S-\mathcal H(D_R)=\sqrt Y>0.
\]

Therefore

\[
\boxed{
 [D_T-D_S]_+
 \not\ge
 [D_S-\mathcal H(D_R)]_+.
}
\tag{R-91561.3}
\]

## 3. Correct actual debt

The correct current-generation quantity is

\[
 \boxed{
 E^{\rm ent}
 =[D_S-\mathcal H(D_R)]_+.
 }
\tag{R-91561.4}
\]

For the physical survival/hazard corridors one has, for every parent and every
geometric difference,

\[
 0\le D_S\le2D_T.
\tag{R-91561.5}
\]

Because `D_R>=0` and `G_j>=0`,

\[
 \mathcal H(D_R)\ge0.
\]

Consequently

\[
\boxed{
 E^{\rm ent}\le D_S\le2D_T.
}
\tag{R-91561.6}
\]

After target normalization, the genuine local entropy debt is therefore at
most two, not automatically zero or one.  A substochastic tree still gives
`O(log X)` total debt.  `T-91562` records the corrected consumer.

## 4. Relation to T-91551

The algebraic gluing lemma in `T-91551` correctly uses a packet score `J(P)` and
the actual row entropy.  The remaining issue is its invocation of the typed
consumer `T-91541`: the local bound must be established using (R-91561.4), not
by citing (R-91561.2).

For canonical component rows, `L-91561` proves a much stronger entropy bound on
the inherited active sector.  The crude corridor estimate (R-91561.6) is enough
for the abstract `O(log X)` conclusion.

```text
T-S as actual packing loss                         FALSE
actual loss S-H(row)                               NORMATIVE
physical-corridor actual local debt <=2 target     EXACT
substochastic target tree -> O(log X)              RETAINED
native score/row producer identification           STILL REQUIRES AUDIT
Riemann Hypothesis                                 UNPROVEN
```
