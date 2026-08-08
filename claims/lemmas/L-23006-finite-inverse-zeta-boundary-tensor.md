# L-23006 — Finite inverse-zeta boundary tensor

Claim ID: `L-23006`  
Title: The exact finite Heath--Brown inverse differs from Möbius by a K-fold boundary residual whose first shell is itself Möbius  
Status: **PROPOSED — COMPLETE DIRICHLET-CONVOLUTION ALGEBRA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-o`  
Created: 2026-08-07  
Dependencies: `L-15159`; elementary Dirichlet convolution  
Scope: exact source identity; no estimate of the boundary tensor

## 1. Truncated inverse and residual

Fix integers

\[
 K\ge1,
 \qquad V\ge1.
\]

Let

\[
 \mu_V(n)=\mu(n){\bf1}_{n\le V},
\]

let `1` be the constant-one arithmetic function, and put

\[
 B_V=\mu_V*\mathbf1,
 \qquad
 r_V=\varepsilon-B_V.
\tag{L-23006.1}
\]

Define the finite Heath--Brown inverse packet

\[
 A_{K,V}
 =\sum_{j=1}^{K}(-1)^{j-1}{K\choose j}
  \mu_V^{*j}*\mathbf1^{*(j-1)}.
\tag{L-23006.2}
\]

## 2. Global exact identity

Convolving (L-23006.2) with `1` and applying the binomial theorem gives

\[
 A_{K,V}*\mathbf1
 =\varepsilon-r_V^{*K}.
\tag{L-23006.3}
\]

Convolve with `mu`, using `1*mu=epsilon`. One obtains the global coefficient
identity

\[
 \boxed{
 A_{K,V}
 =\mu-\mu*r_V^{*K}.}
\tag{L-23006.4}
\]

This strengthens the finite-range statement `A_(K,V)=mu` through `V^K` by
identifying the complete error beyond that range.

Because `r_V(n)=0` for `n<=V`, no coefficient of `r_V^{*K}` can occur at an integer `n<=V^K`. (The first possible integer is `(V+1)^K`; its coefficient may vanish.) Equation (L-23006.4) therefore recovers

\[
 A_{K,V}(n)=\mu(n)
 \qquad(n\le V^K).
\tag{L-23006.5}
\]

## 3. The first residual shell is Möbius

For

\[
 V<n\le2V,
\]

every proper divisor of `n` is at most `n/2<=V`. Hence

\[
 \sum_{\substack{d\mid n\\d\le V}}\mu(d)
 =\sum_{\substack{d\mid n\\d<n}}\mu(d)
 =-\mu(n).
\]

Since `epsilon(n)=0` for `n>1`, this gives

\[
 \boxed{
 r_V(n)=\mu(n)
 \qquad(V<n\le2V).}
\tag{L-23006.6}
\]

Thus the first shell of the pole-cancelling residual is not a benign positive
or divisor-bounded source. It is the actual Möbius function.

## 4. First K-fold boundary layer

No representation contributing to `r_V^{*K}` can have product below `(V+1)^K`. If

\[
 (V+1)^K\le n<(2V+1)(V+1)^{K-1},
\tag{L-23006.7}
\]

then every factor in every representation

\[
 n=n_1\cdots n_K,
 \qquad n_i>V,
\]

satisfies `n_i<=2V`. Therefore (L-23006.6) applies to every factor and

\[
 \boxed{
 r_V^{*K}(n)
 =\left(
  \mu\,{\bf1}_{(V,2V]}
 \right)^{*K}(n)
}
\tag{L-23006.8}
\]

through the complete boundary range (L-23006.7).

Moreover, if

\[
 n<2(V+1)^K,
\]

then in `(mu*r_V^{*K})(n)` the leading Möbius factor must equal one. Hence on
the overlap of these two ranges,

\[
 \boxed{
 \mu(n)-A_{K,V}(n)
 =\left(
  \mu\,{\bf1}_{(V,2V]}
 \right)^{*K}(n).}
\tag{L-23006.9}
\]

## 5. Interpretation

The finite inverse-zeta packet is analytic at every nontrivial zeta zero because
its pole is cancelled by the residual tail in (L-23006.4). Equation
(L-23006.9) identifies the first piece of that tail: it is a K-fold tensor of
lower-scale Möbius shells.

This explains simultaneously why:

1. finite coefficient exactness through `V^K` does not provide a norm bound;
2. the all-truncated boundary corner is not removed by terminal Euler summation;
3. a factorwise tensor estimate lands at the critical scale rather than below
   it;
4. the fixed-logarithm slice of `L-15159` retains the rightmost-zero exponent.

The tail which cancels the reciprocal-zeta pole is made from the same Möbius
source whose cancellation one is trying to prove.

## 6. Proof boundary

The convolution identities and first-shell description are exact. They do not
bound the K-fold Möbius boundary tensor. A full proof still requires a
source-specific signed cancellation across this boundary layer, or an exact
cross-order identity that makes it a positive lower-scale reserve.
