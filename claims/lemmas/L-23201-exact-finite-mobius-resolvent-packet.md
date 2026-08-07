# L-23201 — Exact finite Möbius resolvent packet

Claim ID: `L-23201`  
Title: A truncated Möbius inverse and its residual geometric series give an exact finite signed packet through every prescribed endpoint  
Status: **PROPOSED EXACT ALGEBRAIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-21`  
Created: 2026-08-07  
Issue: #232  
Dependencies: elementary Dirichlet convolution  
Scope: direct scalar Möbius packet; no RH input

## 1. Definitions

Let `epsilon` be the Dirichlet-convolution identity and let `1` denote the
constant-one arithmetic function. For integers `X>=2` and `K>=2`, put

\[
V=\lceil X^{1/K}\rceil,
\qquad
\mu_V(n)=\mu(n)\mathbf 1_{n\le V},
\tag{L-23201.1}
\]

and define the residual

\[
\boxed{
r_V=\epsilon-\mathbf 1*\mu_V.
}
\tag{L-23201.2}
\]

For every `n<=V`, all divisors of `n` occur in the truncated Möbius sum, so

\[
r_V(n)
=
\epsilon(n)-\sum_{d\mid n}\mu(d)
=
0.
\tag{L-23201.3}
\]

Thus every nonzero coefficient of `r_V` is supported on an integer strictly
larger than `V`.

## 2. Exact finite resolvent identity

The convolution identity

\[
\epsilon=\mathbf1*\mu_V+r_V
\]

and `mu*1=epsilon` give

\[
\mu=\mu_V+\mu*r_V.
\tag{L-23201.4}
\]

Iterating `K` times yields

\[
\mu
=
\sum_{j=0}^{K-1}\mu_V*r_V^{*j}
+
\mu*r_V^{*K}.
\tag{L-23201.5}
\]

Every nonzero coefficient of `r_V^{*K}` is supported above `V^K`, while

\[
V^K\ge X.
\]

Consequently, coefficient by coefficient for every `n<=X`,

\[
\boxed{
\mu(n)
=
\sum_{j=0}^{K-1}
\left(\mu_V*r_V^{*j}\right)(n).
}
\tag{L-23201.6}
\]

This is the Möbius analogue of a finite Heath–Brown identity. It is a finite
geometric resolvent for `1/zeta`; there is no asymptotic remainder at or below
the declared endpoint.

## 3. Explicit tuple packet

The `j`-th row in (L-23201.6) is a finite sum over tuples

\[
(d;n_1,\ldots,n_j),
\qquad
d\le V,\quad n_i>V,\quad
dn_1\cdots n_j=n,
\tag{L-23201.7}
\]

with exact signed coefficient

\[
\mu(d)r_V(n_1)\cdots r_V(n_j).
\tag{L-23201.8}
\]

The residual coefficient itself is source bound:

\[
r_V(n)
=
-\sum_{\substack{d\mid n\\d\le V}}\mu(d)
\qquad(n>1).
\tag{L-23201.9}
\]

Hence every tuple can be expanded, if desired, into a finite divisor packet
whose only signs are actual Möbius signs. No arbitrary vector or generic
cluster coefficient enters the identity.

## 4. Fixed-ratio interval form

For `0<c<1`, summing (L-23201.6) over

\[
cX<n\le X
\]

gives the exact finite identity

\[
\boxed{
M(X)-M(cX)
=
\sum_{j=0}^{K-1}
\sum_{cX<n\le X}
(\mu_V*r_V^{*j})(n).
}
\tag{L-23201.10}
\]

For large `X`, the `j=0` row vanishes because its support is at most `V`. The
complete first critical Farey cell of `L-23003` is the specialization
`c=2/3`.

Equation (L-23201.10) is the correct scalar replacement for the uniform
Farey-cluster operator refuted in `R-22802`: the actual divisor signs remain
inside every row until the final contraction.

## 5. Deterministic first-crossing dictionary

Fix a threshold `0<delta<1/2`. Order the tuple variables as written in
(L-23201.7) and stop at the first partial product at least `X^delta`.

Each tuple receives exactly one label:

1. **balanced Type II**, if the stopped product and its complement are both at
   most `X^(1-delta+o_K(1))`;
2. **reduced-complexity Type I**, if one side is below `X^delta` and expanding
   its residual coefficient lowers the number of unresolved residual factors;
3. **terminal Type I**, if no strict complexity reduction is obtained.

All rows having the same label must be recombined with the signs in
(L-23201.8) before Cauchy–Schwarz, divisor majorization, or total variation.

This gives a finite combinatorial dictionary for each fixed `K`. It does not
supply an analytic estimate for any packet.

## 6. Relationship to the prime packet

The exact finite Heath–Brown packet of `L-15156` decomposes `Lambda`, whereas
(L-23201.6) decomposes `mu`. They are two sides of the same inverse-zeta
geometry:

- the prime packet is the natural input to the centered Selberg quadratic
  identity and its positive Hankel adjoints;
- the Möbius packet exposes the coherent first-cell Mertens mode that every
  successful prime-energy proof must ultimately control.

The proposed completion in Issue #232 uses the prime packet as the positive
energy engine and the Möbius packet as a mandatory scalar audit coordinate.

## 7. Proof boundary

Closed here:

- residual support above `V`;
- the exact finite geometric resolvent;
- the complete tuple signs and divisor formula;
- a deterministic finite packet dictionary.

Open:

- every terminal packet estimate;
- the vanishing-rate scale contraction;
- RH.
