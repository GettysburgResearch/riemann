# R-96300 — The PR #534 endpoint close and Volterra-to-canonical family switch are superseded

Claim ID: `R-96300`
Status: **PROVED INTERFACE CORRECTION / NORMATIVE SUPERSESSION**
Created: 2026-08-16
Frozen target: PR #534 at `ef18bdda5a65334695008e4c1f5986833160d84f`
Primary correction: PR #541 at `e381f444191e214cc992208b16d30a8d5fd461ac`
RH status: **unproved**

## 1. The `<3457` packing ledger is not the complete arithmetic deficit

For every finite ordinary response `C`, the exact radix-four adjoint is

\[
 \langle Y_4,\mathcal D_4C\rangle=\langle\Lambda,C\rangle.
\]

Hence the native target satisfies

\[
 \langle Y_4,\Omega_X\rangle=P_\Lambda(X),
\]

not `J_Lambda(X)`.  For a physical row `d`,

\[
 \mathcal H(d)=\langle Y_4,\Xi_d\rangle,
\]

and therefore

\[
 \boxed{
 J_\Lambda(X)-\mathcal H(d)
 =F_\Lambda(X)+
  \langle Y_4,\Omega_X-\Xi_d\rangle.
 }
\]

The physical packing term cannot absorb the independent arithmetic gap
`F_Lambda=J_Lambda-P_Lambda`.  Consequently `L-94122`, `L-94123` and the
endpoint-closing part of `T-94120` are not load-bearing in this successor.

## 2. The Volterra infinitesimal family may not be sent through the canonical causal theorem

PR #503 gives the exact counterexample

```text
(p,y,s,j)=(67,15,1005,14)
p_1005(14)-67^(-1/2)p_15(14)<0.
```

Thus a positive Volterra fibre `p_s` cannot be replaced, inside a causal edge,
by the canonical family `Q_s` merely because both appear in endpoint
representations.  The original `L-94121` begins with the Volterra/equality
profiles `E_x,R_x` and later invokes canonical `Q_(py/d)-p^(-1/2)Q_(y/d)`
terminal leaves.  That change of source family is not used here.

## 3. Correct replacement

This successor starts and ends in one family: the literal canonical native
Möbius row

\[
 c_X(j)=\sum_{k\le X/j}{\mu(k)\over\sqrt k}Q_{X/k}(j).
\]

The exact paired stopping tree only regroups these canonical occurrences.  Its
terminal current differences are exactly the canonical Target-Lorenz objects.
Once `c_X(j)>=0` is obtained, the conclusion is taken by its own reciprocal-zeta
Mellin transform and Landau's theorem.  No native endpoint benchmark or packing
identity is used.

```text
PR #534 abstract source-only gluing               retained with correction
PR #534 Volterra/canonical family transition      superseded
PR #534 <3457 endpoint close                      superseded by #541
canonical projective full-row identity            replacement
fixed-row Mellin-Landau consumer                  replacement
RH                                                unproved pending review
```
