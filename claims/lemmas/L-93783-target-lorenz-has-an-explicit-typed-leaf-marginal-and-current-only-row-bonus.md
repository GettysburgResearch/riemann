# L-93783 — Target-Lorenz has an explicit typed leaf marginal and a current-only row bonus

Claim ID: `L-93783`  
Status: **PROVED EXACT LEAF COMPILER ON `L-93602`**  
Created: 2026-08-15  
Depends on: `L-91720`, `L-93602`  
Replay: `X-93781-target-lorenz-typed-ledger`  
RH status: **unproved**

This theorem makes the source/physical type boundary in `L-93603` explicit.
It does not assert that every nonnegative physical row is itself a positive
arithmetic source packet.

## 1. Literal leaf labels

A stopped occurrence is labelled by

\[
\omega=(n,h,i,d,\varepsilon,c),
\tag{L-93783.1}
\]

where

```text
n             complete integer endpoint cell;
h             ordered rough-prime history;
i             unique least-rough-prime owner, or root owner;
d|P61         small divisor;
epsilon       Möbius parity;
c             complete causal current/child path.
```

The frozen stopping-line and first-owner identities make these labels disjoint
and exhaustive. A label is never erased before the one global quantizer.

## 2. One coefficient vector

At a terminal leaf write the positive even and odd source packets as `E` and
`O`. Let the ordered even atoms have targets `t_e>0`, and let

\[
0\le u_e\le1,
\qquad
\sum_eu_et_e=T(O),
\tag{L-93783.2}
\]

be the literal leftmost Target-Lorenz coefficients:

```text
u_e = 1     before the cutoff;
u_e = theta on the cutoff;
u_e = 0     after the cutoff.
```

The same `u_e` is used in target, declared score, every component row and every
subsequent ordinary observation. Define the positive residual source

\[
\nu=E-U,
\qquad U=\sum_eu_eE_e.
\tag{L-93783.3}
\]

The source occurrence coefficient is split exactly once between `U` and `nu`.

## 3. The three leaf outputs

The exact Target-Lorenz conclusions are

\[
T(U)=T(O),
\tag{L-93783.4}
\]

\[
S(U)\le S(O),
\tag{L-93783.5}
\]

and, by the complete AVLT,

\[
B:=R(U)-R(O)\ge0
\tag{L-93783.6}
\]

componentwise in every physical row. Put

\[
\sigma:=S(O)-S(U)\ge0.
\tag{L-93783.7}
\]

The typed positive leaf datum is the direct-sum object

\[
\boxed{G_\omega=(\nu_\omega;B_\omega;\sigma_\omega).}
\tag{L-93783.8}
\]

Its exact marginals are

\[
\boxed{T(\nu)=T(E)-T(O),}
\tag{L-93783.9}
\]

\[
\boxed{S(\nu)=S(E)-S(O)+\sigma,}
\tag{L-93783.10}
\]

and

\[
\boxed{R(\nu)+B=R(E)-R(O).}
\tag{L-93783.11}
\]

Thus `nu` is the literal positive residual arithmetic source; `B` is a
leaf-owned, current-only nonnegative physical row; and `sigma` is explicit
score surplus. The theorem assigns **zero source target** to `B`. It never
relabels `B` as a positive source atom or sends it to a child.

Equation (L-93783.11) proves the actual physical marginal directly. No abstract
joint coupling and no promotion of an actual child response to a full child
capacity is required.

## 4. Ordinary and radix-four coordinates

Apply the resident positive ordinary response map to (L-93783.11) separately at
`q` and at `4q`. Sum all leaves with their actual path coefficients. Only after
that common ordinary sum define

\[
\Xi(q)=\Gamma(q)-2\Gamma(4q).
\tag{L-93783.12}
\]

Hence target, score and every row use one coefficient vector, while the
radix-four coordinate is formed from the resulting single physical row. This
is the complete leaf-level source-to-physical compiler needed by the common
parent.
