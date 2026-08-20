# L-100710 — The short double-owner sector has an unavoidable prime main term

Claim ID: `L-100710`  
Status: **PROVED UNCONDITIONAL ASYMPTOTIC**  
Created: 2026-08-20  
Base: PR #693 at `2cc70798b453ce4e5059dcc25d8d3fb7c38e172e`  
Depends on: PRs #674/#689 minimal ordinary-Möbius wavelet; the classical prime number theorem  
RH status: **not assumed**

Let `K_0` be the ratio-eight kernel of PR #674 and

\[
G_\mu(X)=\sum_{X/8\le n\le X}{\mu(n)\over\sqrt n}K_0(X/n).
\]

Apply the coefficient-level least/greatest-prime decomposition used in
`L-100704`. Write

\[
G_\mu(X)=G_{\rm sh}(X)+G_{\rm lo}(X),
\]

where `G_sh` contains the singleton blocks and every squarefree integer with

\[
{P^+(n)\over P^-(n)}\le8,
\]

while `G_lo` contains the remaining squarefree integers.

Put

\[
\boxed{
\kappa_0=\widehat K_0(1/2)
=8\log2\left(1-2^{-1/2}\right)^2>0.
}
\tag{L-100710.1}
\]

Then

\[
\boxed{
G_{\rm sh}(X)
=-\kappa_0{\sqrt X\over\log X}
+O\!\left({\sqrt X\over\log^2X}\right).
}
\tag{L-100710.2}
\]

## 1. Singleton-prime contribution

The singleton blocks are

\[
S_1(X)=-\sum_p{1\over\sqrt p}K_0(X/p).
\]

The kernel is compactly supported on `[1,8]`, piecewise `C^1`, and vanishes at
its two support endpoints. Partial summation against the prime number theorem
gives

\[
\begin{aligned}
\sum_p{1\over\sqrt p}K_0(X/p)
&=\sqrt X\int_1^8
 {K_0(y)y^{-3/2}\over\log X-\log y}\,dy
 +O\!\left(\sqrt X e^{-c\sqrt{\log X}}\right)\\
&={\sqrt X\over\log X}
 \int_1^8K_0(y)y^{-3/2}\,dy
 +O\!\left({\sqrt X\over\log^2X}\right).
\end{aligned}
\tag{L-100710.3}
\]

The Mellin formula from PR #674 is

\[
\widehat K_0(s)
=(1-\sqrt2\,2^{-s})(1-2^{-s})^2
 {s+\frac32\over s^2(s-\frac12)}.
\]

At `s=1/2`, the zero of `1-sqrt(2)2^(-s)` removes the displayed pole and

\[
\widehat K_0(1/2)
=8\log2(1-2^{-1/2})^2.
\]

Hence

\[
S_1(X)=-\kappa_0{\sqrt X\over\log X}
+O(\sqrt X/\log^2X).
\tag{L-100710.4}
\]

## 2. All composite short blocks are one logarithm smaller

Let `N_k(X)` count squarefree integers `n in [X/8,X]` with `omega(n)=k>=2`
and `P^+(n)<=8P^-(n)`. Put `Lambda=log_2 X`. If

\[
2^m\le P^-(n)<2^{m+1},
\]

then every prime factor of `n` lies in `[2^m,2^(m+4))`. The product condition
forces

\[
{\Lambda-3\over k}-4<m\le{\Lambda\over k},
\]

so at most six dyadic prime windows occur for each `k`.

For `k<=Lambda/10`, Chebyshev's prime-counting bound gives, uniformly in every
admissible window,

\[
\#\{p:2^m\le p<2^{m+4}\}
\ll {X^{1/k}k\over\log X}.
\]

Therefore

\[
N_k(X)
\ll X{(Ck/\log X)^k\over k!}
\ll X\left({C'\over\log X}\right)^k.
\tag{L-100710.5}
\]

For `k>Lambda/10`, the least prime is bounded by an absolute constant; all
prime factors then belong to one fixed finite set, so this range is empty for
all sufficiently large `X`. Summing (L-100710.5) gives

\[
\sum_{k\ge2}N_k(X)\ll {X\over\log^2X}.
\tag{L-100710.6}
\]

Since `|K_0|` is bounded and `n>=X/8`, the total absolute contribution of all
composite short blocks is

\[
O\!\left({\sqrt X\over\log^2X}\right).
\tag{L-100710.7}
\]

Combining (L-100710.4) and (L-100710.7) proves (L-100710.2).

## Meaning

The diagonal singleton blocks are not a harmless Type-I residue in the
short/long implication matrix. They carry a genuine deterministic term of
size `sqrt(X)/log X`. Its cancellation partner lies in the long sector.
Any norm that takes the short sector in absolute value before that cancellation
is necessarily power-sized.
