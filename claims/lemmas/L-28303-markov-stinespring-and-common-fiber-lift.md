# L-28303 — Markov–Stinespring and common-fiber lift

Claim ID: `L-28303`  
Title: The state-dependent carry factor defines a completely positive two-frequency map and commutes with common arithmetic fiber congruence  
Status: **PROPOSED COMPLETE ABSTRACT OPERATOR LEMMA**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #283  
Dependencies: `L-28301`; PR #241 `L-9518`; PR #282 `L-28102`  
Scope: positive matrix/source adapter; no arithmetic recurrence

## 1. Markov isometry

Let `Pi(dt,ds)=p(t)dt kappa_t(ds)` be the positive joint measure of
`L-28301`, and let

\[
y=t+s.
\]

Define

\[
(Vf)(t,s)=f(t+s).
\]

Then

\[
\|Vf\|_{L^2(\Pi)}^2
=
\int_0^\infty |f(y)|^2g(y)dy.
\]

Thus

\[
\boxed{
V:L^2(g(y)dy)\longrightarrow L^2(\Pi)
\text{ is an isometry.}
}
\tag{L-28303.1}
\]

The scalar independent-convolution model would identify

\[
L^2(\Pi)=L^2(p)\otimes L^2(\nu).
\]

No such tensor-product factorization is required here.

## 2. Completely positive map

For a finite matrix-valued function `F(y)`, define

\[
(\Phi F)(t)=\int\kappa_t(ds)F(t+s).
\tag{L-28303.2}
\]

Because `Phi` is integration against a probability kernel, it is unital and
completely positive.  In particular, for every vector family `H_a(y)`,

\[
\boxed{
\int g(y)H_a(y)\overline{H_b(y)}dy
=
\int p(t)\int\kappa_t(ds)
H_a(t+s)\overline{H_b(t+s)}.
}
\tag{L-28303.3}
\]

Every mixed cross term is retained.

This is the appropriate positivity notion for the independent-frequency
physical block.  Specializing `a=b` only after (L-28303.3) gives the Hermitian
square; no scalar analytic square is substituted.

## 3. Finite Gram consequence

Let `h_1,...,h_d` be any finite source family and put

\[
G_{ab}
=
\int g(y)h_a(y)\overline{h_b(y)}dy.
\]

Then

\[
G
=
\int p(t)G(t)dt,
\]

where

\[
G(t)_{ab}
=
\int\kappa_t(ds)
h_a(t+s)\overline{h_b(t+s)}
\succeq0.
\tag{L-28303.4}
\]

Thus the sharp Gamma Gram is a positive mixture of state-resolved carry Grams.
A finite production certificate may approximate the state integral by directed
positive quadrature without losing matrix positivity.  The approximation error
and endpoint collar must still be bounded source specifically.

## 4. Common arithmetic fiber

Let `M_H` be any linear source map representing a complete arithmetic fiber,
for example the reciprocal-free top fiber of PR #282.  If a base matrix
inequality is

\[
A-\kappa G\succeq0,
\]

then congruence gives

\[
\boxed{
M_H^*(A-\kappa G)M_H\succeq0.
}
\tag{L-28303.5}
\]

The Markov lift and the common-fiber lift commute, because both are linear
before the quadratic form is taken:

\[
M_H^*\left(\int G(t)d\mu(t)\right)M_H
=
\int M_H^*G(t)M_Hd\mu(t).
\tag{L-28303.6}
\]

Therefore one fixed state-resolved carry/Pascal theorem can be lifted to every
complete top Möbius fiber without a new endpoint-count or moving-order
argument.

## 5. Source and cutoff firewall

The abstract equality does not authorize any of the following operations:

1. deleting the state `t` before finite arithmetic realization;
2. applying the Markov kernel separately to diagonal blocks and discarding
   cross terms;
3. splitting a complete odd-core or top residual fiber before congruence;
4. commuting a hard physical cutoff through `M_H` without exporting the
   commutator;
5. replacing the full two-frequency block by a one-frequency vertical integral;
6. inferring a strict reserve from positivity alone.

A production object must emit the complete state/source manifest, every
cutoff commutator, and a strict reserve-minus-lower-block recurrence.

## 6. Role in the global proposal

There are two consumers of the same state-resolved construction:

```text
elementary consumer:
    Markov state -> Pascal cycles -> subpower cycle debt -> prime ramp -> RH;

reflected consumer:
    Markov state -> two-frequency CP Gram -> common top fiber
                 -> strict physical recurrence -> RH.
```

A successful `SAPC` proof may therefore close the elementary route directly or
serve as the missing fixed-source matrix producer for the fibered factor-five
route.

## 7. Proof boundary

Closed exactly:

- the Markov isometry;
- complete positivity;
- the two-frequency Gram identity;
- positive finite Gram decomposition;
- commutation with common-fiber congruence.

Open:

- finite directed state quadrature with subpower collar;
- Pascal realization and debt contraction;
- a strict reflected recurrence;
- RH.