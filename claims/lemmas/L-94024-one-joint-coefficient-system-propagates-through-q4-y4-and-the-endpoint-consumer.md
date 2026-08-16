# L-94024 — One joint coefficient system propagates through `q/4q`, `Y_4`, and the endpoint consumer

Claim ID: `L-94024`
Status: **PROVED EXACT CONDITIONAL COMPOSITION**
Created: 2026-08-16
Depends on: `L-94021`, `L-94023`; `L-91377/L-91378`; PR #508 all-column and endpoint locks
RH status: **conditional on the joint anchored producer**

Assume that for every sufficiently large integer `X`, the anchored problem
`L-94023.1` returns one joint certificate.  Let `d_X^anc` be its total
nonnegative row and let `d_X^out` be the exact outer row of `L-94021`.  Put

\[
 d_X^0=d_X^{anc}+d_X^{out}.
\tag{L-94024.1}
\]

The source partition is exact and the same coefficient system is used in every
native coordinate.  Apply the one common thinning, one parent pushforward and
one positive global quantizer from the frozen PR #508 operation list.  Keep
finite/continuum, collar and terminal data in the signed observation ledger.

Because ordinary `q` and ordinary `4q` were evaluated on the same row,

\[
 \Xi_{d_X}(q)=
 C_{d_X}(q)-2C_{d_X}(4q).
\tag{L-94024.2}
\]

The frozen all-column estimate, including `2<=q<K`, and the terminal omission
then give

\[
 C_{d_X}(q)\le w_X(q),
 \qquad
 \Xi_{d_X}(q)\le\Omega_X(q).
\tag{L-94024.3}
\]

Only now define

\[
 r_X=\Omega_X-\Xi_{d_X}
 \ge0.
\]

The direct sparse-dual pricing is the unchanged PR #508 ledger

```text
common thinning               <12012
nonterminal signed comparison <4
terminal signed comparison    <48972
literal positive omissions    <1
port / large-X base           0
-----------------------------------
Y4-weighted native deficit    <60989<61000.
```

Hence

\[
 0\le J_\Lambda(X)-\mathcal H(d_X)<61000
 =o(\log^2X).
\tag{L-94024.4}

The frozen finite dual has the one-sided orientation

\[
 F_\Lambda(X)
 \le J_\Lambda(X)-\mathcal H(d_X).
\]

On the frozen prime-square moat and Mellin--Landau inputs, the joint anchored
certificate would therefore yield the proposed RH conclusion.  Nothing in
this implication replaces the open joint producer by synthetic fixtures or by
branchwise positive children.
