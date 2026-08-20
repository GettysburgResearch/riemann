# L-100410 — Minimal-wavelet largest-prime reduction and smooth-sector removal

Claim ID: `L-100410`  
Status: **PROVED EXACT DECOMPOSITION + ASYMPTOTIC SMOOTH BOUND**  
Created: 2026-08-20  
Depends on: PRs #674–#675  
RH status: **not assumed**

Let `K_0` be the compact ordinary-Möbius wavelet kernel of PR #674, supported
on `[1,8]`, and put

\[
G_\mu(X)=\sum_{n\ge1}{\mu(n)\over\sqrt n}K_0(X/n).
\]

The support condition restricts the sum to `X/8<=n<=X`.

## 1. Unique largest-prime ownership

Every squarefree `n>1` has a unique representation

\[
n=pm,
\qquad
p=P^+(n),
\qquad
P^+(m)<p.
\]

Moreover `mu(pm)=-mu(m)`.  Hence

\[
\boxed{
\begin{aligned}
G_\mu(X)=K_0(X)
-\sum_{p\le X}{1\over\sqrt p}
\sum_{\substack{X/(8p)\le m\le X/p\\P^+(m)<p}}
{\mu(m)\over\sqrt m}K_0(X/(pm)).
\end{aligned}
}
\tag{L-100410.1}
\]

For `X>8`, the root term `K_0(X)` vanishes.  Every nonunit source integer is
spent exactly once.

## 2. Smooth sector

Let

\[
Y_X=(\log X)^{3/2},
\qquad
\sigma_X={1\over3}+{1\over\sqrt{\log\log X}}.
\]

Rankin's inequality gives

\[
\Psi(X,Y_X)
\le X^{\sigma_X}
\prod_{p\le Y_X}(1-p^{-\sigma_X})^{-1}.
\]

For large `X`,

\[
\log\prod_{p\le Y_X}(1-p^{-\sigma_X})^{-1}
\ll\sum_{n\le Y_X}n^{-\sigma_X}
\ll Y_X^{1-\sigma_X}=o(\log X).
\]

Therefore

\[
\boxed{\Psi(X,Y_X)=X^{1/3+o(1)}.}
\tag{L-100410.2}
\]

Every contributing wavelet integer satisfies `n>=X/8`; since `K_0` is bounded,
the complete contribution from `Y_X`-smooth integers is

\[
\boxed{G_{\rm sm}(X)=X^{-1/6+o(1)}.}
\tag{L-100410.3}
\]

## 3. Rough largest-prime form

The sole remaining term is

\[
\boxed{
G_{\rm rough}(X)=
-\sum_{p>(\log X)^{3/2}}{1\over\sqrt p}
\sum_{\substack{X/(8p)\le m\le X/p\\P^+(m)<p}}
{\mu(m)\over\sqrt m}K_0(X/(pm)).
}
\tag{L-100410.4}
\]

This is a source-faithful Type-I/Type-II object with one exact largest-prime
owner and a fixed ratio-eight kernel.
