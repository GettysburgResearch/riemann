# L-25801 — Exact top-depth prime-anchor normal form

Claim ID: `L-25801`  
Title: The last finite-resolvent prime row is a positive divisor-log anchor convolved with a large-factor Möbius tensor, with only one aggregate short coordinate  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #258  
Dependencies: `L-23201`; elementary Dirichlet convolution  
Scope: coefficient range `n<=X<=V^K`; no estimate of the large-factor tensor

## 1. Setup

Let `epsilon` be the convolution identity, let `1` be the constant-one
arithmetic function, and put

\[
\mu_V(n)=\mu(n)\mathbf1_{n\le V},
\qquad
r_V=\varepsilon-\mathbf1*\mu_V.
\tag{L-25801.1}
\]

Then

\[
r_V(n)=0\qquad(n\le V)
\tag{L-25801.2}
\]

and every nonzero coefficient of `r_V^(K-1)` is supported at an integer at
least `(V+1)^(K-1)`.

Let

\[
\ell(n)=\log n
\]

and recall the exact identity

\[
\mu*\ell=\Lambda.
\tag{L-25801.3}
\]

The top row in the finite prime packet is

\[
P_{K,V}=\mu_V*r_V^{*(K-1)}*\ell.
\tag{L-25801.4}
\]

## 2. Top-depth logarithmic transposition

For every `n<=X<=V^K`, one has

\[
\boxed{
P_{K,V}(n)
=(\Lambda*r_V^{*(K-1)})(n).
}
\tag{L-25801.5}
\]

Indeed, write a term of (L-25801.4) as `uv=n`, where
`r_V^(K-1)(v)!=0`. Then

\[
v\ge(V+1)^{K-1}
\]

and consequently

\[
u\le {V^K\over(V+1)^{K-1}}<V.
\tag{L-25801.6}
\]

Every divisor of `u` is therefore at most `V`, so

\[
(\mu_V*\ell)(u)
=(\mu*\ell)(u)
=\Lambda(u).
\]

This proves (L-25801.5) coefficientwise, including the endpoint.

Put

\[
T_{K,V}:=\Lambda*r_V^{*(K-1)}.
\tag{L-25801.7}
\]

This is the source called the top reflected source in PR #250.

## 3. Large-factor Möbius form

Let

\[
\mu_{>V}=\mu-\mu_V.
\]

Since `1*mu=epsilon`,

\[
\boxed{
r_V=\mathbf1*\mu_{>V}.}
\tag{L-25801.8}
\]

Hence

\[
T_{K,V}
=\Lambda*\mathbf1^{*(K-1)}*\mu_{>V}^{*(K-1)}.
\tag{L-25801.9}
\]

Define

\[
g_{K-1}=\Lambda*\mathbf1^{*(K-1)}.
\tag{L-25801.10}
\]

Using `Lambda*1=ell`, equivalently

\[
g_{K-1}=\ell*\mathbf1^{*(K-2)}.
\tag{L-25801.11}
\]

If `d_r=1^(*r)` is the ordered `r`-fold divisor function, symmetry of the
ordered factors gives

\[
\boxed{
g_{K-1}(b)
={d_{K-1}(b)\log b\over K-1}\ge0.}
\tag{L-25801.12}
\]

Therefore

\[
\boxed{
T_{K,V}
=g_{K-1}*\mu_{>V}^{*(K-1)}.
}
\tag{L-25801.13}
\]

This is the prime-anchored normal form.

## 4. One aggregate short coordinate

In every active representation

\[
n=b\,d_1\cdots d_{K-1},
\qquad d_i>V,
\tag{L-25801.14}
\]

with `n<=V^K`, one has

\[
\boxed{
b
\le {V^K\over(V+1)^{K-1}}<V.}
\tag{L-25801.15}
\]

Thus the complete top row has exactly one aggregate short coordinate `b<V`.
The other `K-1` coordinates are the genuine large Möbius factors.

For fixed `K`, standard divisor bounds give

\[
\boxed{
\sum_{b<V}{g_{K-1}(b)\over\sqrt b}
\le V^{1/2+o_K(1)}.}
\tag{L-25801.16}
\]

This proves the representation-level short-coordinate bound. It does not
control the reflected Gram of `mu_(>V)^(K-1)`.

## 5. Why this source is the correct frontier

Every non-top row contains either a complete logarithmic variable or a residual
quotient separated from its cutoff, and is the target of the superorder Euler
closure of `L-24901` after the logarithmic coordinate is retained. The top row
(L-25801.13) is the unique row for which the entire output scale can be carried
by the `K-1` large Möbius factors together with the short anchor.

The top row is therefore not a terminal error. It is the finite packet source
whose fixed-logarithm slices contain the RH-equivalent Mertens shell.

## 6. Proof boundary

Closed exactly, subject to review:

- top-depth logarithmic transposition;
- the positive divisor-log anchor;
- the one-short-coordinate normal form;
- the exact support bound `b<V`.

Not closed:

- cancellation of the large-factor Möbius tensor;
- a reflected reserve;
- `PARC(K)`, `PADT(K)`, or RH.
