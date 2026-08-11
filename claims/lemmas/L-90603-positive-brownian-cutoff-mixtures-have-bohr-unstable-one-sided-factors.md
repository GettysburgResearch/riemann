# L-90603 — Every sufficiently spread positive Brownian cutoff mixture has Bohr-unstable one-sided factors

Claim ID: `L-90603`  
Status: **PROPOSED COMPLETE UNCONDITIONAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-21705`; the coefficient estimates of `L-90601`; PNT, Kronecker and Hurwitz  
Scope: logarithmic Nörlund and central-binomial Brownian mixtures, before functional-equation symmetrization

## 1. Positive cutoff mixtures

Let

\[
 \lambda_{N,K}\ge0,\qquad
 \sum_{K=1}^N\lambda_{N,K}=1,
 \tag{L-90603.1}
\]

and define

\[
 m_{\lambda,N}(s)=\sum_{K=1}^N\lambda_{N,K}m_K(s)
 =\pi^{-s/2}\Gamma(1+s/2)D_{\lambda,N}(s).
 \tag{L-90603.2}
\]

By `L-21705`,

\[
 D_{\lambda,N}(s)=sB_{\lambda,N}(s)+A_{\lambda,N}(s),
 \tag{L-90603.3}
\]

where

\[
 \boxed{
 B_{\lambda,N}(s)=\sum_{n=1}^Nb_{N,n}n^{-s},
 \qquad
 b_{N,n}=\frac12\sum_{K=n}^N\lambda_{N,K}C_{K,n}>0.
 }
 \tag{L-90603.4}
\]

Assume that the mixture retains at least logarithmic mass on its top half:

\[
 \boxed{
 \sum_{N/2\le K\le N}\lambda_{N,K}\ge\frac{c_0}{\log N}
 }
 \tag{L-90603.5}
\]

for one fixed `c_0>0` and all large `N`.

### Theorem

Fix

\[
 \frac12<\beta<1.
\]

Under (L-90603.5), for every sufficiently large `N`, `D_(lambda,N)` and `m_(lambda,N)` have infinitely many zeros `s_j` satisfying

\[
 |\operatorname{Im}s_j|\to\infty,
 \qquad
 \operatorname{Re}s_j\to\beta.
 \tag{L-90603.6}
\]

Thus no such one-sided positive mixture is zero-free in the full RH-facing half-strip `Re s>1/2`.

## 2. Uniform selected-prime estimates

Again take

\[
 \mathcal P_N=\{p\text{ prime}:2\sqrt N\le p\le3\sqrt N\}.
 \tag{L-90603.7}
\]

For `K in [N/2,N]`, `p in P_N`, and all large `N`, the same product estimate as in `L-90601` gives

\[
 C_{K,p}\ge4e^{-40}.
 \tag{L-90603.8}
\]

Indeed `p^2/(2K+1)<9`, and all the relevant `x_k=(2k+1)/(2K+1)` are at most `1/4`.

Therefore (L-90603.5) yields

\[
 \boxed{b_{N,p}\ge\frac{2c_0e^{-40}}{\log N}.}
 \tag{L-90603.9}
\]

If `m>=2` and `mp<=N`, then, term by term for every `K>=mp`,

\[
 \frac{C_{K,mp}}{C_{K,p}}
 \le e^{-5(m^2-1)},
\]

because `p^2>=4N>=4K`. Hence

\[
 \boxed{
 \frac{b_{N,mp}}{b_{N,p}}
 \le e^{-5(m^2-1)}.
 }
 \tag{L-90603.10}
\]

Finally, since `C_(K,n)<=4` and the `lambda`'s sum to one,

\[
 \boxed{0<b_{N,n}\le2.}
 \tag{L-90603.11}
\]

## 3. Torus cancellation

At the fixed line `Re s=beta`, set

\[
 a_n=b_{N,n}n^{-\beta}.
 \tag{L-90603.12}
\]

Randomise all primes outside `P_N` by independent Steinhaus phases. The residual `R` from integers divisible by no selected prime satisfies

\[
 \mathbb E|R|^2\le4\sum_{n=1}^\infty n^{-2\beta}=4\zeta(2\beta),
 \tag{L-90603.13}
\]

so one twist has `|R|<=2 sqrt(zeta(2 beta))`.

For each selected prime, collect

\[
 B_p=\sum_{m\le N/p}a_{pm}\omega(m).
 \tag{L-90603.14}
\]

By (L-90603.10),

\[
 |B_p-a_p|\le\eta_\beta a_p,
 \qquad
 \eta_\beta:=\sum_{m\ge2}e^{-5(m^2-1)}m^{-\beta}<10^{-6}.
 \tag{L-90603.15}
\]

By (L-90603.9) and the PNT,

\[
 \sum_{p\in\mathcal P_N}|B_p|
 \gg_{\beta,c_0}
 \frac{N^{(1-\beta)/2}}{(\log N)^2}\to\infty,
 \tag{L-90603.16}
\]

whereas

\[
 \max_p|B_p|=O_\beta(N^{-\beta/2}).
 \tag{L-90603.17}
\]

For large `N` the selected vectors can therefore cancel the bounded residual exactly by the polygon lemma. This gives a completely multiplicative unimodular `chi` with

\[
 \boxed{
 \sum_{n=1}^Nb_{N,n}\chi(n)n^{-\beta}=0.
 }
 \tag{L-90603.18}
\]

A generic arbitrarily small perturbation of the selected phases splits any multiple zero, so the twist may be chosen with a simple zero `w_0` as close to `beta` as desired and still satisfying

\[
 \frac12<\operatorname{Re}w_0<1.
 \tag{L-90603.19}
\]

(The multiple-zero equations add the independent complex condition `B'_(lambda,N,chi)=0`; the polygon solution set has positive dimension once the selected block is large, and is not contained in that proper real-analytic subset.)

## 4. Actual one-sided zeros

Kronecker supplies `t_j->infinity` for which the ordinary vertical translates converge to the chosen twist. Consequently

\[
 \frac{D_{\lambda,N}(w+it_j)}{it_j}
 \longrightarrow
 B_{\lambda,N,\chi}(w)
 \tag{L-90603.20}
\]

locally uniformly. Hurwitz gives simple zeros

\[
 s_j=w_j+it_j,
 \qquad
 w_j\to w_0,
 \tag{L-90603.21}
\]

of `D_(lambda,N)`. The gamma prefactor in (L-90603.2) has no zeros, so these are also zeros of `m_(lambda,N)`. This proves the theorem.

## 5. The two repository mixtures satisfy the hypothesis

### Logarithmic Nörlund weights

For

\[
 \lambda_{N,K}=\frac1{KH_N},
\]

one has

\[
 \sum_{N/2\le K\le N}\lambda_{N,K}
 =\frac{\log2+o(1)}{\log N},
 \tag{L-90603.22}
\]

so (L-90603.5) holds.

### Central-binomial Green weights

For

\[
 \omega_K=\left[\binom{2K}{K}4^{-K}\right]^2,
 \qquad
 \lambda_{N,K}=\frac{\omega_K}{\sum_{J\le N}\omega_J},
\]

Wallis gives `omega_K>=1/(4K)` and trivially `omega_K<=1/K`. Hence the numerator mass on `[N/2,N]` is bounded below by a positive constant, while the full denominator is `O(log N)`, so (L-90603.5) again holds.

Thus both one-sided producers used in PR #296 are Bohr-unstable in every fixed half-strip `1/2<Re s<1` for all sufficiently large `N`.

## 6. Proof boundary

Proved here:

- a general top-mass criterion for one-sided Brownian cutoff mixtures;
- selected-prime torus zeros for every fixed `1/2<beta<1`;
- infinitely many actual high-frequency zeros;
- application to logarithmic Nörlund and central-binomial Green weights.

Not yet used here:

- functional-equation symmetrization;
- the real-zero claims BLNRZ/BGRRZ;
- RH.

`L-90604` shows that functional-equation symmetrization does not remove these zeros.
