# L-23708 — Base-`p` digit phase kernels

Claim ID: `L-23708`  
Title: Every prime-base digital freeze has a positive `p-1` phase decomposition, and the four phases at `p=5` are the canonical boundary states for the outer carry recurrence  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Dependencies: `L-23703`, `L-23707`; PR #236 `L-23011/L-23012`  
Scope: exact digit, Dirichlet-series, and causal-convolution identities; no coercivity or renewal estimate

## 1. Euler-aligned prime-base source

Fix a prime `p`. Define

\[
b_p(n)=\mu(n)-\mathbf1_{p\mid n}\mu(n/p).
\tag{L-23708.1}
\]

Its Dirichlet series is

\[
\boxed{
B_p(s)=\sum_{n\ge1}\frac{b_p(n)}{n^s}
=\frac{1-p^{-s}}{\zeta(s)}.}
\tag{L-23708.2}
\]

Let `v_p(n)` be the ordinary `p`-adic valuation and put

\[
\boxed{c_p(n)=1-(p-1)v_p(n).}
\tag{L-23708.3}
\]

Using

\[
\sum_{n\ge1}\frac{v_p(n)}{n^s}
=\zeta(s)\frac{p^{-s}}{1-p^{-s}},
\]

one obtains

\[
\boxed{
C_p(s)=\sum_{n\ge1}\frac{c_p(n)}{n^s}
=\zeta(s)\frac{1-p^{1-s}}{1-p^{-s}}.}
\tag{L-23708.4}
\]

Therefore

\[
\boxed{C_p(s)B_p(s)=1-p^{1-s}.}
\tag{L-23708.5}
\]

Equivalently,

\[
\boxed{c_p*b_p=d_p,}
\tag{L-23708.6}
\]

where

\[
d_p(1)=1,
\qquad
d_p(p)=-p,
\qquad
d_p(n)=0\quad(n\ne1,p).
\tag{L-23708.7}
\]

## 2. Positive digit partial sums

Let `s_p(N)` be the sum of the base-`p` digits of `N`. Legendre's formula gives

\[
v_p(N!)=\frac{N-s_p(N)}{p-1}.
\]

Hence

\[
\boxed{
\sum_{n\le N}c_p(n)=s_p(N)\ge0.}
\tag{L-23708.8}
\]

The increment identity is

\[
\boxed{s_p(N)-s_p(N-1)=1-(p-1)v_p(N)=c_p(N).}
\tag{L-23708.9}
\]

Define the positive causal digit kernel

\[
\boxed{
S_p(t)=e^{-t/2}s_p(\lfloor e^t\rfloor),}
\tag{L-23708.10}
\]

with value zero for `t<0`. Then

\[
S_p\ge0,
\qquad
S_p\in L^1\cap L^2,
\]

and in distributions

\[
\boxed{
\left(\partial_t+\frac12\right)S_p
=\kappa_p,
\qquad
\kappa_p=\sum_{n\ge1}\frac{c_p(n)}{\sqrt n}\delta_{\log n}.}
\tag{L-23708.11}
\]

Let

\[
\beta_p=\sum_{n\ge1}\frac{b_p(n)}{\sqrt n}\delta_{\log n}.
\tag{L-23708.12}
\]

The normalized form of (L-23708.6) is

\[
\kappa_p*\beta_p
=\delta_0-\sqrt p\,\delta_{\log p}.
\tag{L-23708.13}
\]

Consequently

\[
\boxed{
S_p*\beta_p
=w_\infty-\sqrt p\,\tau_{\log p}w_\infty,}
\tag{L-23708.14}
\]

where

\[
w_\infty(t)=e^{-t/2}\mathbf1_{t\ge0}.
\]

Thus every prime-base aligned Möbius shell has one explicit positive digital
Green kernel and one elementary two-tap output.

## 3. `p-1` positive phase combs

For `1<=r<=p-1`, define

\[
\boxed{
P_{p,r}(t)
=e^{-t/2}
\mathbf1_{\{\lfloor e^t\rfloor\bmod p\ge r\}}.}
\tag{L-23708.15}
\]

These kernels are nonnegative and belong to `L1 intersect L2`.

If `epsilon_j(N)` denotes the `j`-th base-`p` digit of `N`, then

\[
\epsilon_j(N)
=\sum_{r=1}^{p-1}
\mathbf1_{\{\lfloor N/p^j\rfloor\bmod p\ge r\}}.
\]

Summing over all digit positions gives the exact positive phase decomposition

\[
\boxed{
S_p(t)
=\sum_{j\ge0}p^{-j/2}
 \sum_{r=1}^{p-1}
 P_{p,r}(t-j\log p).}
\tag{L-23708.16}
\]

The series is pointwise nonnegative and converges in both `L1` and `L2`.

For `s=z+1/2` in the initial convergence half-plane, direct integration over
the residue intervals gives

\[
\begin{aligned}
\widehat P_{p,r}(z)
&=\frac1s\sum_{m\ge0}
 \left[(pm+r)^{-s}-(p(m+1))^{-s}\right]\\
&=\boxed{
\frac{p^{-s}}s
\left[\zeta\left(s,\frac rp\right)-\zeta(s)\right].}
\end{aligned}
\tag{L-23708.17}
\]

For `p=2,r=1`, this reduces to the parity-comb transform

\[
\widehat P_{2,1}(z)=\frac{\eta(s)}s.
\]

## 4. Why `p=5` is canonical for the carry outer theorem

The exact outer carry theorem closes the four quotient bands

\[
\left(\frac1{r+1},\frac1r\right],
\qquad r=1,2,3,4,
\]

before the coefficient `mu(5)=-1` enters. Equation (L-23708.16) shows that the
same number four is not accidental: base five has exactly four positive digit
phases

\[
P_{5,1},P_{5,2},P_{5,3},P_{5,4}.
\]

Together with the exact frozen-corridor identity of `L-23707`, these are the
canonical finite states for a one-fifth scale recurrence. They retain the full
Euler-aligned Möbius source through (L-23708.14); no generic positive kernel or
unsigned carry row is substituted.

## 5. Proof-facing recurrence interface

A complete carry recurrence may now be posed as a finite-state positive renewal:

1. use the four unconditional outer carry atoms at one endpoint;
2. decompose their cross-residue spill into the four phase kernels
   `P_(5,r)`;
3. send the multiple-of-five corridor through the exact smaller carry matrix of
   `L-23707`;
4. use (L-23708.14) to retain and audit the aligned Möbius boundary term;
5. prove that the four-phase boundary operator has a strict reserve after its
   critical digit mode is routed to the smaller endpoint.

The algebra above proves the correct state space and the exact source mutation.
It does not prove the final reserve.

## 6. Proof boundary

Closed exactly:

- the general prime-base Euler-aligned coefficients;
- positive base-`p` digit partial sums;
- the causal two-tap convolution;
- the `p-1` positive phase decomposition;
- the Hurwitz-zeta phase transforms;
- the identification of the four base-five phases with the four outer carry
  bands.

Open:

- the source-bound map from outer carry spill to the phase kernels;
- a strict four-phase recurrence or Schur reserve;
- Greedy Slack/DCRS;
- RH.
