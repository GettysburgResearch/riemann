# L-26903 — Positive inverse wavelet synthesis and generalized-prime reserve

Claim ID: `L-26903`  
Title: The actual generalized prime carry profile is a positive synthesis of the opposite-parity wavelets, and the uniform Schur reserve survives its dyadic correction  
Status: **PROPOSED COMPLETE EXACT ALGEBRA PLUS ELEMENTARY ASYMPTOTIC RESERVE**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: `L-26901`, `L-26902`; generalized Selberg coefficient algebra  
Scope: actual source in carry feature space; physical two-frequency transference remains open

## 1. Positive inverse of the opposite-parity source

Retain

\[
\Omega_2(s)
=\sum_{n\ge1}{\omega_2(n)\over n^s}
={ (1-2^{-s})(1-2^{-s-1})\over\zeta(s)}.
\tag{L-26903.1}
\]

Let

\[
A_2(s)=\Omega_2(s)^{-1}
={\zeta(s)\over(1-2^{-s})(1-2^{-s-1})}
=\sum_{n\ge1}{a_2^\omega(n)\over n^s}.
\tag{L-26903.2}
\]

The power-of-two factor has expansion

\[
{1\over(1-x)(1-x/2)}
=\sum_{r\ge0}(2-2^{-r})x^r.
\tag{L-26903.3}
\]

If `v=v_2(n)`, convolution with `zeta` gives

\[
\boxed{
a_2^\omega(n)
=\sum_{r=0}^{v}(2-2^{-r})
=2v+2^{-v}>0.
}
\tag{L-26903.4}
\]

Thus the actual inverse coefficients are explicit and strictly positive.

## 2. Positive generalized von Mangoldt sequence

Define

\[
\Lambda_\omega
=\omega_2*(a_2^\omega\log),
\tag{L-26903.5}
\]

so its Dirichlet series is `-A_2'/A_2`. Logarithmic differentiation of
(L-26903.2) gives

\[
\boxed{
\Lambda_\omega(q)
=\Lambda(q)
 +(\log2)(1+2^{-r})\mathbf1_{q=2^r},
\qquad r\ge1.
}
\tag{L-26903.6}
\]

Every coefficient is nonnegative. In particular, at a power of two the total
weight is

\[
(2+2^{-r})\log2.
\]

The exact generalized Selberg identity is

\[
\boxed{
\omega_2*(a_2^\omega\log^2)
=\Lambda_\omega\log
 +\Lambda_\omega*\Lambda_\omega.
}
\tag{L-26903.7}
\]

The quadratic coefficient channel is therefore a genuine positive reflected
prime forcing for this exact source.

## 3. Exact positive synthesis of the prime carry profile

For a fixed carry row `n`, define

\[
P_n(j)
=\sum_{q\le n}\Lambda_\omega(q)\chi_{n,q}(j).
\tag{L-26903.8}
\]

For every scale `m`, let `Z_(n,m)` be the pointwise source wavelet of
`L-26901`:

\[
Z_{n,m}(j)
=\sum_{k\le n/m}\omega_2(k)\chi_{n,mk}(j).
\]

Using (L-26903.5) and interchanging finite sums gives

\[
\begin{aligned}
\sum_{m\le n}a_2^\omega(m)\log m\,Z_{n,m}(j)
&=\sum_{m,k}a_2^\omega(m)\log m\,
  \omega_2(k)\chi_{n,mk}(j)\\
&=\sum_{q\le n}\Lambda_\omega(q)\chi_{n,q}(j).
\end{aligned}
\]

Hence

\[
\boxed{
P_n
=\sum_{m\le n}
 a_2^\omega(m)\log m\,Z_{n,m},
\qquad
 a_2^\omega(m)\log m\ge0.
}
\tag{L-26903.9}
\]

This is the exact source map inside carry feature space. The generalized prime
profile is not an arbitrary second vector; it is a positive synthesis of the
same opposite-parity wavelets whose transition geometry was isolated in
`L-26901`.

Consequently

\[
\boxed{
\|P_n\|_n^2
=\sum_{m,r\le n}
 a_2^\omega(m)a_2^\omega(r)\log m\log r
 \langle Z_{n,m},Z_{n,r}\rangle_n.
}
\tag{L-26903.10}
\]

Every cross term is retained.

## 4. Ordinary Kummer profile plus a small digital correction

Kummer's theorem gives

\[
F_n(j):=\log\binom nj
=\sum_{q\le n}\Lambda(q)\chi_{n,q}(j).
\tag{L-26903.11}
\]

By (L-26903.6),

\[
\boxed{
P_n(j)=F_n(j)+D_n(j),
}
\tag{L-26903.12}
\]

where

\[
D_n(j)
=(\log2)
\sum_{2^r\le n}(1+2^{-r})\chi_{n,2^r}(j)
\ge0.
\tag{L-26903.13}
\]

Since every carry indicator is at most one,

\[
\boxed{
0\le D_n(j)\le\log n+\log2.
}
\tag{L-26903.14}
\]

Thus the generalized-prime correction has only logarithmic pointwise size.

## 5. The correction is negligible in row energy

Let

\[
k=\left\lfloor{n\over3}\right\rfloor.
\]

For `n>=12`, `k>=n/4`. Moreover

\[
\binom nk
=\prod_{r=1}^k{n-k+r\over r}
\ge3^k,
\tag{L-26903.15}
\]

because `n-k>=2k`. For every `k<=j<=n-k`, binomial monotonicity and symmetry
give

\[
F_n(j)\ge k\log3\ge{n\log3\over4}.
\]

There are at least `n/3` such indices. Therefore

\[
\boxed{
\sum_{j=0}^nF_n(j)^2
\ge{(\log3)^2\over48}n^3.
}
\tag{L-26903.16}
\]

On the other hand, (L-26903.14) gives

\[
\sum_{j=0}^nD_n(j)^2
\le(n+1)(\log n+\log2)^2.
\tag{L-26903.17}
\]

Hence

\[
\boxed{
{\|D_n\|_2\over\|F_n\|_2}
=O\left({\log n\over n}\right).
}
\tag{L-26903.18}
\]

All constants are absolute and elementary.

## 6. The strict source reserve survives

Let

\[
\kappa_0={1\over60,000,000}.
\]

`L-26902` proves, for every `n>=210`, every `m`, and every scalar `a`,

\[
\|F_n-aZ_{n,m}\|_2
\ge\sqrt{\kappa_0}\,\|F_n\|_2.
\tag{L-26903.19}
\]

By (L-26903.18), for all sufficiently large `n`,

\[
\|D_n\|_2
\le{\sqrt{\kappa_0}\over2}\|F_n\|_2.
\tag{L-26903.20}
\]

Therefore, uniformly in `m` and `a`,

\[
\begin{aligned}
\|P_n-aZ_{n,m}\|_2
&\ge
\|F_n-aZ_{n,m}\|_2-\|D_n\|_2\\
&\ge{\sqrt{\kappa_0}\over2}\|F_n\|_2.
\end{aligned}
\tag{L-26903.21}
\]

Also `||P_n||_2<=(1+o(1))||F_n||_2`, so after enlarging the finite threshold,

\[
\boxed{
\min_{a\in\mathbb R}
\|P_n-aZ_{n,m}\|_2^2
\ge{\kappa_0\over16}\|P_n\|_2^2.
}
\tag{L-26903.22}
\]

Thus the actual generalized-prime carry profile has an absolute strict Schur
reserve against every scaled source wavelet. The finitely many rows below the
threshold belong in the production boundary table.

## 7. Consequence for the transition programme

The source-specific carry side of `F5TC` is now complete at three levels:

1. `L-26901` localizes every potentially negative ordinary Kummer row to
   `2m<=n<5m`;
2. `L-26902` proves a uniform reserve for the ordinary logarithmic profile;
3. this lemma identifies the actual generalized-prime profile as a positive
   synthesis of the wavelets and transfers the reserve to it.

What remains is not another carry-space sign or reserve theorem. It is the exact
bounded map from PR #241's physical independent-frequency transition matrix to
this generalized-prime carry Gram, together with the consumer map to DSS or
shell energy.

## 8. Proof boundary

Closed exactly or elementarily:

1. explicit positive inverse coefficients;
2. positive generalized von Mangoldt weights;
3. exact positive wavelet synthesis of the prime carry profile;
4. exact digital correction to ordinary Kummer;
5. its `O(log n/n)` relative row-energy bound;
6. survival of an absolute source-specific Schur reserve.

Open:

1. physical-normal-to-carry transference;
2. finite boundary matrices;
3. DSS/shell contraction;
4. RH.
