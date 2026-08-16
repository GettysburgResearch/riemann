# L-96501 — The complete first-owner tree terminates at finite depth for every endpoint

Claim ID: `L-96501`  
Status: **PROPOSED COMPLETE SOURCE-EXHAUSTION THEOREM — HOSTILE REVIEW REQUIRED**  
Created: 2026-08-17  
Depends on: `L-96500`; frozen first-owner stopping-line typing from PR #550

## 1. Labelled state

A node is a tuple

\[
v=(\gamma_v,Z_v,\mathfrak h_v,P_v),
\]

where `gamma_v>=0`, `P_v` is positive labelled source, `Z_v` is its endpoint
scale, and `h_v` is the ordered rough-prime history. The root is the exact
positive parity-labelled native source

\[
\mathscr N_X=
\bigoplus_{\substack{k\le X/2\\\mu(k)\ne0}}
{1\over\sqrt k}\,\mathscr Q_{X/k}^{\operatorname{parity}(\mu(k))}.
\tag{L-96501.1}
\]

Its signed component-row marginal is the native Möbius row `c_X`.

## 2. Expansion rule

At an unresolved node with `Z_v>=67`, apply (L-96500.1) on each first-owner
source slice. Deposit the survivor and all current paired-edge terms in the
current ledger. Export only the positive `alpha_i` children, with history
`h_v` extended by their unique least owner.

The expansion is source-disjoint because the first-owner slices are disjoint.
It is source-exhaustive because (L-96500.1) is an equality before any
observation. Paired edge terms remain paired; the negative side is never
promoted to a positive physical row.

## 3. Finite depth

Every unresolved child obeys

\[
Z_{v'}\le {Z_v\over67}.
\tag{L-96501.2}
\]

Thus every path has length at most

\[
D_X=\max\!\left(0,
\left\lceil {\log(X/67)\over\log67}\right\rceil+1\right).
\tag{L-96501.3}
\]

After `D_X` layers all leaves have scale below 67. There is no infinite tree,
no limiting frontier, and no interchange of a limit with a row observation.

## 4. Exact finite stopping line

Iterating the finite equalities yields

\[
\boxed{
\mathscr N_X
 =\mathscr C_X
 \oplus
 \bigoplus_{\ell\in\mathcal L_X}
   \gamma_\ell\,
   \mathscr D(p_\ell,y_\ell,d_\ell),}
\tag{L-96501.4}
\]

where

```text
C_X        is current positive source plus paired current edges;
L_X        is a finite set of terminal first-owner leaves;
p_l>=67;
1<=y_l<67;
d_l divides P_61 and mu(d_l) is nonzero;
gamma_l>=0.
```

Every root source occurrence has exactly one terminal/current owner, and the
same path coefficient is present in target, score, every component row,
ordinary `q`, ordinary `4q`, and detail. No rough-prefix reservoir appears.

The proof is induction on

\[
\operatorname{rk}(v)=\min\{m:Z_v/67^m<67\}.
\]

Rank zero is terminal. For positive rank, (L-96500.1) partitions the source;
all unresolved children have lower rank by (L-96501.2), so the induction closes
in finitely many steps. Source disjointness is inherited from the unique
first-owner label at each step.
