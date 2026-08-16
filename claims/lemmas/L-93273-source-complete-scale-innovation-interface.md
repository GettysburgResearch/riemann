# L-93273 - Source-complete scale-innovation interface for the cubic and heat routes

Claim ID: `L-93273`
Status: **PROPOSED COMPLETE EXACT REDUCTION ON FROZEN INPUTS - INDEPENDENT REVIEW REQUIRED**
Created: 2026-08-16
Depends on: `L-93265`, `L-93270`, `L-93272`; PR #379 and PR #531 at their exact frozen heads
Scope: exact producer statements and implications; neither producer is proved

## 1. Static large-divisor producer

Let `W_C` be the centered-cubic two-switch kernel. PR #531 proves

\[
\mathcal L_C(X)
=\sum_{n\le X}\Lambda(n)W_C(n/X)
\tag{L-93273.1}
\]

and the exact large-divisor localization

\[
\mathcal L_C(X)
=\mathcal B_C(X)+O(\log X),
\tag{L-93273.2}
\]

where

\[
\boxed{
\mathcal B_C(X)
=\sum_{2\le m<\sqrt X}(\log m)
  \sum_{\sqrt X<d\le X/m}
  \mu(d)W_C(md/X).
}
\tag{L-93273.3}
\]

The static producer is

\[
\boxed{
\mathrm{SID}_0:
\quad
|\mathcal B_C(X)|
\ll \sqrt X\,(\log(2X))^A
}
\tag{L-93273.4}
\]

for one fixed exponent `A`. By the frozen Mellin pole audit, `SID_0` implies RH. Conversely RH gives a bound of this shape through the classical square-root prime error, so `SID_0` is RH-equivalent rather than an assumed auxiliary estimate.

## 2. Carrier-resolved scale-field producer

Let `F_C(r,t)` be (L-93272.14). The exact First-Hermite formula of PR #379 has a gamma reserve of order

\[
\frac{\log(2+|t|)}{q^{3/2}}
\tag{L-93273.5}
\]

against the normalized prime polynomial. The legal source-complete producer is

\[
\boxed{
\mathrm{SID}_H:
\quad
\|\mathcal F_C(\cdot,t)\|_2
\le
C\frac{\log(2+|t|)}{q^{1/4}}
}
\tag{L-93273.6}
\]

uniformly in the `q,t` range consumed by the First-Hermite criterion, with a constant small enough relative to the explicit gamma reserve after the fixed normalization is inserted.

By (L-93272.17), `SID_H` bounds the complete First-Hermite prime polynomial at the required scale. The exact first-Hermite explicit formula then gives nonnegativity and RH.

The normalization constant is deliberately not hidden: a reviewer must compare the produced constant directly with PR #379's pole and gamma terms.

## 3. Why these are not CPBD renamings

`SID_0` is one explicit balanced Möbius bilinear form after every small-divisor term has been paid unconditionally.

`SID_H` is a carrier-resolved `L2` estimate for one finite-at-each-scale prime field, connected to First-Hermite by an explicit Schwartz transform.

Neither statement follows from:

1. block cardinality;
2. common-half-plane alignment;
3. a generic large sieve applied after absolute values;
4. positivity of the Peano transport;
5. a pointwise bound for a truncated Euler product.

## 4. Common completion architecture

The two proof chains are

\[
\mathrm{SID}_0
\Longrightarrow
\text{centered cubic square-root bound}
\Longrightarrow RH,
\tag{L-93273.7}
\]

and

\[
\mathrm{SID}_H
\Longrightarrow
\text{First-Hermite positivity}
\Longrightarrow RH.
\tag{L-93273.8}
\]

`L-93270` and `L-93271` supply a positive source-complete scale bank in which either producer may be attacked. The two producer estimates remain open.
