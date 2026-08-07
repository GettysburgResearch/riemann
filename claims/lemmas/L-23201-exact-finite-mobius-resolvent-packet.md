# L-23201 — Exact finite Möbius resolvent

Claim ID: `L-23201`  
Title: A truncated Möbius inverse and its residual geometric series give an exact finite signed expansion through every prescribed endpoint  
Status: **CORE VERIFIED BY REVIEW; PACKET CLASSIFICATION REMAINS A SCHEMA**  
Authoring agent: `gpt56-pro-21`  
Created: 2026-08-07  
Corrected: 2026-08-07 after review of frozen PR #233  
Issue: #232  
Dependencies: elementary Dirichlet convolution  
Scope: exact scalar Möbius expansion; no packet estimate or RH input

## 1. Definitions

Let `epsilon` be the Dirichlet-convolution identity and let `1` denote the
constant-one arithmetic function. For integers `X>=2` and `K>=2`, put

\[
V=\lceil X^{1/K}\rceil,
\qquad
\mu_V(n)=\mu(n)\mathbf1_{n\le V},
\]

and

\[
\boxed{
r_V=\epsilon-\mathbf1*\mu_V.
}
\tag{L-23201.1}
\]

For every `n<=V`, all divisors of `n` occur in the truncated Möbius sum, so

\[
r_V(n)=0.
\tag{L-23201.2}
\]

Thus every nonzero coefficient of `r_V` is supported on an integer at least
`V+1`.

## 2. Exact finite resolvent

The identity

\[
\epsilon=\mathbf1*\mu_V+r_V
\]

and `mu*1=epsilon` give

\[
\mu=\mu_V+\mu*r_V.
\]

Iterating `K` times,

\[
\mu
=
\sum_{j=0}^{K-1}\mu_V*r_V^{*j}
+
\mu*r_V^{*K}.
\tag{L-23201.3}
\]

Every nonzero coefficient of `r_V^{*K}` is supported at an integer at least

\[
(V+1)^K>V^K\ge X.
\]

Consequently, coefficient by coefficient for every `n<=X`, including the
endpoint,

\[
\boxed{
\mu(n)
=
\sum_{j=0}^{K-1}
(\mu_V*r_V^{*j})(n).
}
\tag{L-23201.4}
\]

This is an exact finite geometric resolvent for `1/zeta`; there is no endpoint
remainder.

## 3. Tuple expansion

The `j`-th row is a finite sum over

\[
(d;n_1,\ldots,n_j),
\qquad
d\le V,
\quad n_i>V,
\quad dn_1\cdots n_j=n,
\]

with coefficient

\[
\mu(d)r_V(n_1)\cdots r_V(n_j).
\]

For `n>1`,

\[
r_V(n)
=-\sum_{\substack{d\mid n\\d\le V}}\mu(d),
\]

so every residual factor may be expanded into actual Möbius/divisor signs.

## 4. Fixed-ratio scalar identity

For `0<c<1`, summation of (L-23201.4) gives

\[
\boxed{
M(X)-M(cX)
=
\sum_{j=0}^{K-1}
\sum_{cX<n\le X}
(\mu_V*r_V^{*j})(n),
}
\tag{L-23201.5}
\]

with the usual floor convention in `M(cX)`.  At `c=2/3`, this is the scalar
coordinate decoded by the first critical Farey cell.

## 5. Packet-schema boundary

The tuple formula permits a deterministic first-crossing classification into
balanced, reduced Type-I, and terminal rows.  At the frozen PR #233 head this
was described too strongly as a complete source-bound dictionary.

What is supplied here is only the **rule** for generating such a dictionary.
A production packet must still emit:

```text
complete tuple manifest
actual complexity rank
signed destination recombination
all factor and cutoff boundaries
all source-specific routing identities
```

The corrected source reduction is stated separately in `L-23206`; the balanced
analytic estimate is `BTP(K)` in `L-23207`.

## 6. Proof boundary

Verified by the review:

- support of `r_V` above `V`;
- the finite resolvent identity through `X`;
- the fixed-ratio scalar expansion.

Not supplied by this lemma:

- a production packet manifest;
- balanced or reduced-row energy estimates;
- an unbounded recurrence;
- RH.