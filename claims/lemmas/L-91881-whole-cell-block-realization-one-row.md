# L-91881 — The inner native source tree terminates in positive residual sources and row-only bonuses

Claim ID: `L-91881`  
Status: **PROPOSED COMPLETE SOURCE-TREE / TWO-SORTED LEAF THEOREM ON FROZEN DIRECTED INPUTS — REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `L-91880`; frozen stopping-line and first-owner identities; `L-91690`; directed AVLT hardening `L-93782`; typed leaf theorem `L-93783`  
RH status: **unproved**

## 1. Literal inner occurrence labels

Every finite native occurrence in `c_{X,\mathrm{in}}` receives the immutable label

\[
 \omega=(m,k,d,h,i,\varepsilon,c),
\]

where `m` is the finite cell, `k` the original squarefree Möbius colour, `d|P_61` its small-prime part, `h` the ordered rough history, `i` the unique least rough owner or root owner, `epsilon=mu(k)`, and `c` the complete causal path.

The exact stopping-line and least-owner identities partition these labels. A source occurrence is never reconstructed from the row-first rough lift.

## 2. Compact transition leaves

Any inner transition cell with `1<X/m<67` uses the deterministic compact target-Hall flow. For positive nodes `E`, negative nodes `O`, and flow `t_(o,e)`, define

\[
 c_e=1-\frac1{T(e)}\sum_ot_{o,e}\ge0
\]

and

\[
 B_j=\sum_{o,e}t_{o,e}
 \left[\frac{R_j(e)}{T(e)}-\frac{R_j(o)}{T(o)}\right]\ge0.
\]

Then

\[
 T(c)=T(E)-T(O),
\tag{L-91881.1}
\]

\[
 S(c)\ge S(E)-S(O),
\tag{L-91881.2}
\]

and

\[
 R(c)+B=R(E)-R(O).
\tag{L-91881.3}
\]

Only `c` is a complete positive target-bearing source packet. `B` is a current-only nonnegative row. The exact `x=2` score obstruction from `R-91880` is normative.

## 3. Deep anchored leaves

For every stopped deep leaf with `x>=67`, the frozen compact theorem covers `x<166000` and the directed hardening covers `x>=166000`; the half-open domains meet exactly. The complete AVLT supplies literal cutoff coefficients `u_e` using the same vector in target, declared score and every row.

Write

\[
 U=\sum_eu_eE_e,
 \qquad
 \nu=E-U,
\]

\[
 B=R(U)-R(O)\ge0,
 \qquad
 \sigma=S(O)-S(U)\ge0.
\]

The exact typed leaf identities are

\[
\boxed{T(\nu)=T(E)-T(O),}
\tag{L-91881.4}
\]

\[
\boxed{S(\nu)=S(E)-S(O)+\sigma,}
\tag{L-91881.5}
\]

\[
\boxed{R(\nu)+B=R(E)-R(O).}
\tag{L-91881.6}
\]

Again, `nu` is the positive residual arithmetic source and `B` is a row-only current bonus. The bonus has zero source target, one leaf owner, no rough owner, and no causal child.

## 4. Residual-only causal paths

Least-prime ownership and every causal split are applied only to the target-bearing residual source. At each positive split the outgoing source weights sum to the incoming source weight. Child coefficients are included in the same-index physical placement exactly once.

The row bonus is terminal. It passes through an identity row channel and is never:

```text
re-Hallized;
assigned a rough owner;
split causally;
exported as a child;
assigned a declared-score packet coordinate.
```

The exact directed counterexample in `R-91880.2` also forbids substituting a Volterra `p_s` row for any causal residual source.

## 5. Exact inner physical row

Let `lambda_omega>=0` be the product of the exact stopping-line, first-owner, causal and terminal incidence weights. Keep the two positive output sorts separate:

\[
 d_{X,\mathrm{src}}^{0}
 =\sum_\omega\lambda_\omega q(\nu_\omega)\ge0,
 \qquad
 B_{X,\mathrm{in}}
 =\sum_\omega\lambda_\omega B_\omega\ge0.
\tag{L-91881.7}
\]

Define

\[
\boxed{
 d_{X,\mathrm{in}}^0
 =d_{X,\mathrm{src}}^0+B_{X,\mathrm{in}}\ge0.
}
\tag{L-91881.8}
\]

Summing (L-91881.3) and (L-91881.6) over the disjoint source tree gives

\[
\boxed{d_{X,\mathrm{in}}^0=c_{X,\mathrm{in}}}
\tag{L-91881.9}
\]

coefficientwise in every component row. The residual-source and row-bonus channels are therefore distinct before realization, but their common output is exactly the signed finite inner native row. Target and declared-score inequalities remain attached only to the residual source ledger.

## 6. One-use audit

Every original inner occurrence follows exactly one path:

```text
finite cell
 -> small-prime stopping-line branch
 -> unique least rough owner or root owner
 -> residual-only causal path
 -> one terminal residual source or one row-only bonus
 -> one physical placement.
```

No source occurrence, row bonus, child coefficient or endpoint correction is duplicated.
