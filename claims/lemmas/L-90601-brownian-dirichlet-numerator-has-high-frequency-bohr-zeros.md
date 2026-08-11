# L-90601 — Every sufficiently large raw Brownian numerator has high-frequency zeros in the RH-facing half-plane

Claim ID: `L-90601`  
Status: **PROPOSED COMPLETE UNCONDITIONAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-34003` (the explicit raw Brownian numerator); the prime number theorem; Kronecker approximation; Hurwitz's theorem  
Scope: exact high-frequency obstruction to raw Brownian half-plane stability; no statement about the symmetrized Brownian/Robin route

## 1. Statement

For the raw Brownian/Dirichlet mean of PR #343, put

\[
 H_N(z)=\sum_{n=1}^N C_{N,n}n^{-2z}(z+\alpha_{N,n}),
 \qquad
 C_{N,n}=4\frac{(N!)^4}{(N-n)!^2(N+n)!^2}>0.
 \tag{L-90601.1}
\]

By `L-34003`, the non-elementary zeros of

\[
 M_N(z)=\mathbb E[Q_N^z]
\]

are exactly the zeros of `H_N`.

### Theorem

Fix

\[
 \frac14<\sigma<\frac12.
\]

There exists `N_0(sigma)` such that, for every `N>=N_0(sigma)`, `H_N` has infinitely many zeros `z_j` satisfying

\[
 |\operatorname{Im}z_j|\longrightarrow\infty,
 \qquad
 \operatorname{Re}z_j\longrightarrow\sigma.
 \tag{L-90601.2}
\]

In particular, for every sufficiently large `N`,

\[
 \boxed{H_N(z)=0\text{ for infinitely many }z\text{ with }\operatorname{Re}z>\frac14.}
 \tag{L-90601.3}
\]

Consequently the proposed all-large-`N` or cofinal raw Brownian stability theorem

\[
 \mathbb E[Q_N^z]\ne0\qquad(\operatorname{Re}z>1/4)
 \tag{L-90601.4}
\]

is false: no unbounded sequence of indices can satisfy it.

The obstruction is purely high-frequency. It is compatible with local-uniform convergence of the finite Brownian transforms to `2 xi`: the escaping zeros run to infinite imaginary height as `N` is held fixed.

## 2. The leading Dirichlet polynomial

Separate the degree-one part in `z`:

\[
 H_N(z)=zF_N(z)+G_N(z),
 \tag{L-90601.5}
\]

where

\[
 F_N(z)=\sum_{n=1}^N C_{N,n}n^{-2z},
 \qquad
 G_N(z)=\sum_{n=1}^N C_{N,n}\alpha_{N,n}n^{-2z}.
 \tag{L-90601.6}
\]

At large vertical height, `H_N(z)/z` has the same vertical-limit functions as `F_N`.

For a completely multiplicative unimodular function `chi`, define

\[
 F_{N,\chi}(z)=\sum_{n=1}^N C_{N,n}\chi(n)n^{-2z}.
 \tag{L-90601.7}
\]

The main step is to construct, for every large `N`, one such `chi` with

\[
 \boxed{F_{N,\chi}(\sigma)=0.}
 \tag{L-90601.8}
\]

## 3. Two coefficient estimates

The exact ratio from `L-34003` is

\[
 \boxed{
 \frac{C_{N,k+1}}{C_{N,k}}
 =\left(\frac{N-k}{N+k+1}\right)^2.
 }
 \tag{L-90601.9}
\]

Equivalently, with

\[
 x_k=\frac{2k+1}{2N+1},
\]

one has

\[
 \frac{N-k}{N+k+1}=\frac{1-x_k}{1+x_k}.
 \tag{L-90601.10}
\]

Choose the prime block

\[
 \mathcal P_N=\{p\text{ prime}:2\sqrt N\le p\le3\sqrt N\}.
 \tag{L-90601.11}
\]

For all sufficiently large `N` and every `p in P_N`:

\[
 \boxed{C_{N,p}\ge4e^{-20}.}
 \tag{L-90601.12}
\]

Indeed,

\[
 \log\frac{C_{N,p}}4
 =-4\sum_{k=0}^{p-1}\operatorname{artanh}x_k.
\]

For `N>=144`, `x_k<=1/4` in this range, so `artanh x <= (16/15)x`; moreover

\[
 \sum_{k=0}^{p-1}x_k=\frac{p^2}{2N+1}\le\frac{9N}{2N+1}<\frac92,
\]

which gives the displayed bound.

If `m>=2` and `mp<=N`, then

\[
 \boxed{
 \frac{C_{N,mp}}{C_{N,p}}
 \le \exp[-5(m^2-1)].
 }
 \tag{L-90601.13}
\]

Indeed, `log((1-x)/(1+x))<=-2x`, hence

\[
 \begin{aligned}
 \log\frac{C_{N,mp}}{C_{N,p}}
 &\le-4\sum_{k=p}^{mp-1}x_k\\
 &=-\frac{4p^2(m^2-1)}{2N+1}
 \le-5(m^2-1),
 \end{aligned}
\]

because `p^2>=4N`.

Put

\[
 \eta_\sigma=\sum_{m=2}^\infty e^{-5(m^2-1)}m^{-2\sigma}<10^{-6}.
 \tag{L-90601.14}
\]

## 4. A torus zero by randomising the small primes

Set

\[
 a_n=C_{N,n}n^{-2\sigma}.
 \tag{L-90601.15}
\]

No integer `n<=N` is divisible by two members of `P_N`, because their product is at least `4N`; and if `p in P_N` and `n=pm<=N`, then `m<=sqrt(N)/2`, so `m` contains no prime from `P_N`.

First assign independent Haar-uniform phases to every prime outside `P_N`, and extend them completely multiplicatively; call the resulting random twist `omega`. Define the residual

\[
 R(\omega)=\sum_{\substack{n\le N\\p\nmid n\;\forall p\in\mathcal P_N}}
 a_n\omega(n).
 \tag{L-90601.16}
\]

Steinhaus orthogonality gives

\[
 \mathbb E|R(\omega)|^2
 =\sum_{\substack{n\le N\\p\nmid n\;\forall p\in\mathcal P_N}}a_n^2
 \le16\sum_{n=1}^\infty n^{-4\sigma}
 =16\zeta(4\sigma).
 \tag{L-90601.17}
\]

Hence one may fix `omega` such that

\[
 |R(\omega)|\le4\sqrt{\zeta(4\sigma)}.
 \tag{L-90601.18}
\]

For `p in P_N`, collect all terms divisible by `p`:

\[
 B_p(\omega)=\sum_{m\le N/p}a_{pm}\omega(m).
 \tag{L-90601.19}
\]

The `m=1` term is `a_p`; by (L-90601.13),

\[
 |B_p-a_p|\le\eta_\sigma a_p,
 \qquad
 (1-\eta_\sigma)a_p\le|B_p|\le(1+\eta_\sigma)a_p.
 \tag{L-90601.20}
\]

By the prime number theorem,

\[
 \#\mathcal P_N\gg\frac{\sqrt N}{\log N}.
 \tag{L-90601.21}
\]

Using (L-90601.12), for `p in P_N`,

\[
 a_p\ge4e^{-20}(3\sqrt N)^{-2\sigma}.
\]

Therefore

\[
 S_N^*:=\sum_{p\in\mathcal P_N}|B_p|
 \gg_\sigma\frac{N^{1/2-\sigma}}{\log N}\longrightarrow\infty,
 \tag{L-90601.22}
\]

while

\[
 \max_{p\in\mathcal P_N}|B_p|=O_\sigma(N^{-\sigma}),
 \qquad
 \frac{\max|B_p|}{S_N^*}\longrightarrow0.
 \tag{L-90601.23}
\]

For large `N`, therefore,

\[
 S_N^*>|R(\omega)|,
 \qquad
 2\max_p|B_p|<S_N^*.
 \tag{L-90601.24}
\]

The elementary polygon lemma says that vectors of lengths `|B_p|` whose largest length is at most half their sum can realise every point in the closed disk of radius `S_N^*`. Choose phases `u_p in S^1` so that

\[
 \sum_{p\in\mathcal P_N}u_pB_p(\omega)=-R(\omega).
 \tag{L-90601.25}
\]

Extend `omega` by setting `chi(p)=u_p` on `P_N`. Then `chi` is completely multiplicative, unimodular, and

\[
 F_{N,\chi}(\sigma)=R(\omega)+\sum_{p\in\mathcal P_N}u_pB_p(\omega)=0.
 \tag{L-90601.26}
\]

This proves the torus-zero assertion (L-90601.8).

## 5. From the torus zero to actual high-frequency zeros

The numbers `log p`, with `p` running over the finitely many primes up to `N`, are linearly independent over the rationals. Kronecker's theorem therefore supplies a sequence `t_j -> infinity` such that

\[
 p^{-2it_j}\longrightarrow\chi(p)
 \qquad(p\le N\text{ prime}).
 \tag{L-90601.27}
\]

Hence, uniformly on compact subsets of `C`,

\[
 F_N(z+it_j)\longrightarrow F_{N,\chi}(z).
 \tag{L-90601.28}
\]

More directly relevant to the Brownian numerator, put

\[
 \mathcal H_j(z)=\frac{H_N(z+it_j)}{z+it_j}.
 \tag{L-90601.29}
\]

Since the sum is finite and

\[
 \frac{z+it_j+\alpha_{N,n}}{z+it_j}\longrightarrow1
\]

uniformly on compact sets,

\[
 \boxed{\mathcal H_j(z)\longrightarrow F_{N,\chi}(z)}
 \tag{L-90601.30}
\]

locally uniformly.

The finite Dirichlet polynomial `F_(N,chi)` is not identically zero, so its zero at `sigma` is isolated. Hurwitz's theorem (equivalently Rouché on a small circle around `sigma`) gives zeros `w_j` of `H_j` with

\[
 w_j\longrightarrow\sigma.
\]

Thus

\[
 z_j=w_j+it_j
\]

are distinct zeros of `H_N`, with `|Im z_j|->infinity` and `Re z_j->sigma`. This proves the theorem.

## 6. Consequences and scope

The exact raw Brownian route of PR #343 asked for an unbounded sequence `N_j` on which

\[
 H_{N_j}(z)\ne0\qquad(\operatorname{Re}z>1/4).
\]

Taking, for example, `sigma=3/8`, the theorem proves the opposite for every sufficiently large `N`. Thus:

```text
raw Brownian cofinal half-plane stability      FALSE;
raw Brownian all-large-N stability              FALSE;
raw finite gamma/Dirichlet/Hermite identities  RETAINED;
local-uniform convergence to xi                 RETAINED;
symmetrized Brownian/Robin route                NOT ADDRESSED;
Riemann Hypothesis                              UNPROVED.
```

The mechanism is a warning of general use: local-uniform convergence on bounded sets does not control the high-frequency vertical-limit spectrum of each finite Dirichlet polynomial.
