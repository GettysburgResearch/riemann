# M-20203 — Full-proof attack after the sharp prime-debt barrier

Claim ID: `M-20203`  
Title: Pay the unavoidable half-knot debt by a centered prime-bulk transport, not by another signed filter  
Status: **PROPOSED RESEARCH PROGRAM**  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: `T-20201/T-20203`; `R-20202`; `L-20208`--`L-20210`; PR #219 prime polygon; PR #216 Selberg log-convolution energy  
Scope: the remaining global RH-bearing arithmetic theorem

## 1. Starting point

For a nonnegative finite screw filter

\[
 P_N(x)=|(1-e^{ix})Q_N(e^{ix})|^2
\]

with coefficient vector `q^(N)`, the complete prime term is

\[
 -2t_N\sum_{m=0}^{N}W_m(t_N)d_m^{(N)},
\]

where

\[
 d_m^{(N)}=\operatorname{Re}\sum_jq_{j+m}^{(N)}\overline{q_j^{(N)}}
\]

and `W_m>=0` is the complete prime-power deposition ledger.

Every finite or stable fixed positive filter satisfies

\[
 L_{P_N}(1/2)>0.
\]

At base support `t=log4`, this is a strictly adverse `q=2` prime coefficient.
The optimal degree-`N` debt is exactly

\[
 \sin^2\!\frac{\pi}{2(N+1)}
 \sim\frac{\pi^2}{4N^2}.
\]

Therefore the full proof must **pay**, not delete, the debt.

## 2. Canonical endpoint profile

Use the sharp alternating-sine Fejer factor

\[
 q_j^{(N)}=(-1)^j
 \sin\!\frac{(j+1)\pi}{N+1}.
\]

Its exact autocorrelations are

\[
\boxed{
 d_m^{(N)}
 ={(-1)^m\over2}
 \left[
  (N-m)\cos\!\frac{m\pi}{N+1}
  +{\sin((m+1)\pi/(N+1))\over\sin(\pi/(N+1))}
 \right].}
\]

In particular,

\[
 d_0^{(N)}={N+1\over2},
\]

and for fixed terminal distance `ell`,

\[
 d_{N-\ell}^{(N)}
 =(-1)^{N-\ell}
 \left[
 {\ell(\ell+1)(\ell+2)\over6}
 {\pi^2\over(N+1)^2}
 +O_\ell(N^{-4})
 \right].
\]

This gives an explicit `O(N^-2)` terminal autocorrelation profile matching the
sharp half-knot debt.

## 3. Center before estimating

The prime terminal mass and the polar rank-one channel are individually
exponential and cancel at leading order. Every proof object must first form the
exact centered quantity, either through:

1. the centered prime/pole convolution of `L-20705`;
2. the terminal-prime distribution of PR #165/#177;
3. the prime-polygon margin `B_j-F*(A_j)` of PR #219.

No operator norm or entrywise absolute value may be taken before this
cancellation.

## 4. Desired Selberg square

Let `nu` be the centered weighted prime measure in logarithmic coordinates.
PR #216 records the nonlinear Selberg identity schematically as

\[
 y\,d\nu+2dP_0*d\nu+d\nu*d\nu=dR.
\]

The target is an exact filtered identity

\[
\boxed{
 \mathcal S_{P_N}(t_N)
 =\|\mathcal B_N\nu\|_2^2
  +\mathcal E_N,
}
\]

or an equivalent prime-polygon transport, with

\[
 \mathcal E_N
 \ge-o(1)
\]

and the explicit adverse boundary contribution bounded by the sharp
`O(N^-2)` Fejer debt.

A sufficient cofinal rate is

\[
 (-\mathcal S_{P_N}(t_N))_+
 =\exp(o(Nt_N)),
\]

provided the chosen growing family retains the pole-descent/zero-exposure gate.

## 5. Independent scalar replay

Every proposed quadratic estimate must be replayed against the convex-dual
scalar margin

\[
 M_j=B_j-F^*(A_j).
\]

The recurrence

\[
 M_j-M_{j-1}
 =\int_{A_{j-1}}^{A_j}
  [\log q_j-\tau_F(A)]\,dA
\]

is the correct block-transport ledger. The filtered matrix proof and polygon
proof must bind one prime manifest and agree on the centered scalar coordinate.

## 6. Production obligations

1. exact alternating-sine/autocorrelation artifact for each `N`;
2. duplicate-free complete prime-power deposition through `exp(Nt_N)`;
3. exact pole/archimedean centering before widening;
4. directed Selberg-convolution or block-transport residual;
5. independent scalar polygon replay;
6. a cofinal symbolic bound, not a finite trend;
7. an explicit false-RH exposure theorem for the growing family.

## 7. Nonclaims

The endpoint profile and its `O(N^-2)` debt are exact. No Selberg square or
cofinal remainder bound is proved here. This file identifies the narrowest
remaining positive attack after the invalid terminal-flat shortcut was removed.
