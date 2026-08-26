# L-106021 — Square-phase contraction retains every selected owner weight

Claim ID: `L-106021`  
Programme aliases: `LFAM1.OWNER_CONDUCTOR_SHARP_BOUND`, `STRESS.SQUARE_PHASE_OWNER_RESERVE`  
Status: **PROVED UNCONDITIONAL FIXED-PACKET IMPROVEMENT**  
Created: 2026-08-24  
Depends on: `L-106020`; PR #719 `L-102836`, `L-102860--L-102865`, `L-102887--L-102888`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Work after the exact shared-owner and owner/core-overlap renewals. Let

\[
N=pq\,a^2,
\qquad
M=rs\,b^2
\]

be a clean four-distinct-owner packet in core octaves

\[
A\le a<2A,
\qquad
B\le b<2B.
\]

The theorem is independent of whether the deterministic owner pair arose from
the former largest-two gauge or the horizon-safe pair gauge.

Choose any odd opposite owner

\[
\rho\in\{r,s\}
\]

for the `N` field and any odd opposite owner

\[
\pi\in\{p,q\}
\]

for the `M` field. Cleanliness gives

\[
\rho\nmid N,
\qquad
\pi\nmid M.
\]

Let `F_h^(N)` and `G_k^(M)` be the corresponding nonzero square-phase fields,
including the literal coefficients `(pq)^(-1/2)` and `(rs)^(-1/2)`.

The two Ramanujan identities give

\[
\mathcal C_{P,Q}
=
\left\langle
\sum_{h=1}^{\rho-1}F_h^{(N)},
\sum_{k=1}^{\pi-1}G_k^{(M)}
\right\rangle.
\tag{L-106021.1}
\]

By `L-106020.7`, the two coherent phase sums are the negatives of the
unphased fields. By the sharp square-phase contraction,

\[
\left\|\sum_hF_h^{(N)}\right\|^2
\le{\rho-1\over\rho+1}
\sum_h\|F_h^{(N)}\|^2,
\tag{L-106021.2}
\]

and similarly for the `M` field.

The existing fixed-side phase-energy estimates give

\[
\sum_h\|F_h^{(N)}\|^2
\ll
{1\over pq}\left(1+{\rho\over A}\right),
\tag{L-106021.3}
\]

\[
\sum_k\|G_k^{(M)}\|^2
\ll
{1\over rs}\left(1+{\pi\over B}\right).
\tag{L-106021.4}
\]

Consequently

\[
\boxed{
|\mathcal C_{P,Q}|
\ll
{1\over\sqrt{pqrs}}
\left(1+{\rho\over A}\right)^{1/2}
\left(1+{\pi\over B}\right)^{1/2}.
}
\tag{L-106021.5}
\]

The strict factors `((rho-1)/(rho+1))^(1/2)` and
`((pi-1)/(pi+1))^(1/2)` have merely been suppressed in the displayed bound.

## 1. Small-owner choice

For a fixed packet, (L-106021.5) is minimized by choosing the smaller opposite
owners:

\[
\boxed{
|\mathcal C_{P,Q}|
\ll
{1\over\sqrt{pqrs}}
\left(1+{s\over A}\right)^{1/2}
\left(1+{q\over B}\right)^{1/2}.
}
\tag{L-106021.6}
\]

This retains all four owner weights. In the doubly long range `A>=s` and
`B>=q`,

\[
\boxed{
|\mathcal C_{P,Q}|\ll(pqrs)^{-1/2}.
}
\tag{L-106021.7}
\]

## 2. General selected phase sets

Let `S_N` be a nonempty subset of `{r,s}` and `S_M` a nonempty subset of
`{p,q}`. Put

\[
L_N=\prod_{\ell\in S_N}\ell,
\qquad
L_M=\prod_{\ell\in S_M}\ell.
\]

The tensor form `L-106020.9` replaces phase-cardinality Cauchy in every selected
coordinate. With the existing product-modulus phase energy one obtains

\[
\boxed{
|\mathcal C_{P,Q}|
\ll
{1\over\sqrt{pqrs}}
\left(1+{L_N\over A}\right)^{1/2}
\left(1+{L_M\over B}\right)^{1/2}.
}
\tag{L-106021.8}
\]

The former factor `(L_N L_M)^(1/2)` is absent.

Multiple phase directions may still be useful for **global coherent packing**;
(L-106021.8) asserts only that their cardinalities are not an intrinsic
fixed-packet cost.

## Scope

This theorem supersedes the phase-cardinality step in the fixed-pair estimates
without refuting their validity. It does not sum owner quadruples coherently.
That remaining operation is recast as an owner-conductor L-family moment in
`L-106022` and `T-106020`.