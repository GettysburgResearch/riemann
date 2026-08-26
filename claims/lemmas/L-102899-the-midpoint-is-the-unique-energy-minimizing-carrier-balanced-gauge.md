# L-102899 — The midpoint is the unique energy-minimizing and carrier-balanced gauge

Claim ID: `L-102899`  
Status: **PROVED UNCONDITIONAL LABELLED-ENERGY THEOREM**  
Created: 2026-08-24  
Depends on: `L-102898`; the labelled duplicate-\(67\) convention  
RH status: **not assumed**

Write

\[
(1-x)(1+x)^t
=
\sum_{k\ge0}a_k(t)x^k.
\]

Then

\[
a_0(t)=1,
\qquad
a_1(t)=t-1.
\]

Uniformly for \(0\le t\le1\),

\[
\sum_{k\ge0}|a_k(t)|^2p^{-k}
=
1+\frac{(1-t)^2}{p}+O(p^{-2}).
\tag{L-102899.1}
\]

The error is uniform because the generalized binomial coefficients are
bounded on the compact temperature interval.

## 1. Source-energy exponents

Euler-product comparison gives

\[
\boxed{
\sum_{n\le Y}\frac{|\sigma_t(n)|^2}{n}
\ll
(\log(2Y))^{(1-t)^2}.
}
\tag{L-102899.2}
\]

The extra labelled \(67\) changes only an absolute constant.  The complementary
factor satisfies

\[
\boxed{
\sum_{n\le Y}\frac{|\sigma_{1-t}(n)|^2}{n}
\ll
(\log(2Y))^{t^2}.
}
\tag{L-102899.3}
\]

Hence the free tensor energy of the polarized factorization is

\[
\boxed{
\|\sigma_t\|_{\rm src}^2
\|\sigma_{1-t}\|_{\rm src}^2
\ll
(\log(2Y))^{(1-t)^2+t^2}.
}
\tag{L-102899.4}
\]

Since

\[
(1-t)^2+t^2
=
\frac12+2(t-\tfrac12)^2,
\]

the unique minimizing temperature is

\[
\boxed{t=\frac12.}
\tag{L-102899.5}
\]

At the midpoint the combined exponent is \(1/2\), while either endpoint has
exponent \(1\).

## 2. Exact first-chaos balance

The first labelled-prime coefficients of the complementary factors are

\[
a_1(t)=-(1-t),
\qquad
a_1(1-t)=-t.
\]

Their sum is the fixed native first-chaos coefficient

\[
\boxed{a_1(t)+a_1(1-t)=-1,}
\tag{L-102899.6}
\]

while their imbalance is

\[
\boxed{a_1(t)-a_1(1-t)=2t-1.}
\tag{L-102899.7}
\]

Thus \(t=1/2\) is also the unique gauge in which the deterministic prime
carrier is divided equally between the two fields.

## 3. Tangent-energy cost

The temperature tangent is

\[
\dot\sigma_t=\sigma_t*\Lambda,
\qquad
\Lambda=\sum_\ell\log(1+x_\ell).
\]

On a finite horizon,

\[
\boxed{
\sum_{n\le Y}\frac{|\dot\sigma_t(n)|^2}{n}
\ll
(\log(2Y))^{(1-t)^2}
(\log\log(3Y))^2,
}
\tag{L-102899.8}
\]

uniformly on compact temperature intervals.  The factor
\((\log\log Y)^2\) is the free first-chaos energy of the logarithmic
generator; higher prime powers are smaller.

For the complex complementary line \(t=1/2+i\tau\), the local first-chaos
magnitude is

\[
|t-1|^2=\frac14+\tau^2.
\]

Consequently the combined source-energy exponent is

\[
\boxed{
\frac12+2\tau^2,
}
\tag{L-102899.9}
\]

again uniquely minimized at \(\tau=0\).

## Meaning and scope

The arithmetic midpoint is simultaneously:

```text
the unique real phase-transition temperature;
the unique symmetric complementary factorization;
the unique first-chaos carrier-balanced split;
the unique minimum of the free labelled tensor energy;
the center of the complex complementary-temperature line.
```

This theorem controls free source and tangent energy.  It does not turn the
arithmetic convolution product into a pointwise scalar square and does not
prove the physical negative-mass criterion.
