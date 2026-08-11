# L-91004 — Near-minimal ordered factorizations have polynomial complexity

Claim ID: `L-91004`  
Title: At renewal depth `r`, every integer below a fixed multiple of `2^r` has only a bounded number of nonminimal factors; all depth-`r` Möbius remainders therefore have polynomial combinatorial complexity and exponentially small half-power Riesz weight  
Status: **PROPOSED COMPLETE EXACT COMBINATORIAL/ANALYTIC LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-12  
Dependencies: elementary ordered-factor counting  
Scope: the scale diagonal used by `L-91003`; no sign theorem for the Brun projector

## 1. Ordered factorisation source

Let

\[
h(n)=\mathbf1_{n\ge2}.
\tag{L-91004.1}
\]

Then `h^{*r}(n)` counts ordered factorizations

\[
n=d_1\cdots d_r,
\qquad d_i\ge2.
\tag{L-91004.2}
\]

In particular,

\[
\boxed{h^{*r}(n)=0\quad(n<2^r).}
\tag{L-91004.3}
\]

Fix a real constant `C>=1` and suppose

\[
n\le C2^r.
\tag{L-91004.4}
\]

Let `k` be the number of factors `d_i` which exceed two. Then

\[
\left(\frac32\right)^k
\le\prod_{i=1}^r\frac{d_i}{2}
=\frac n{2^r}
\le C.
\tag{L-91004.5}
\]

Therefore

\[
\boxed{
k\le K_C:=\left\lfloor\frac{\log C}{\log(3/2)}\right\rfloor.}
\tag{L-91004.6}
\]

Thus a bounded multiplicative neighbourhood of the minimal diagonal contains only a bounded number of non-two factors, uniformly in `r`.

## 2. Polynomial count

Every nonminimal factor also satisfies `d_i<=2C`. Hence the number of ordered tuples with product at most `C2^r` is at most

\[
\boxed{
\sum_{k=0}^{K_C}
\binom rk\,[\lfloor2C\rfloor-2]^k
=O_C(r^{K_C}).
}
\tag{L-91004.7}
\]

This deliberately crude bound is enough: the exponent depends only on the fixed diagonal width `C`, not on the renewal depth.

For the canonical first-crossing choice `C=4`,

\[
K_4=3.
\tag{L-91004.8}
\]

Thus the entire remainder diagonal has only cubic ordered-factor complexity.

## 3. One extra arithmetic cofactor

Let `a(m)` be any arithmetic sequence with `|a(m)|<=1`, for example `mu(m)`. The coefficient

\[
(h^{*r}*a)(n)
=\sum_{d_1\cdots d_rm=n\atop d_i\ge2}
 a(m)
\tag{L-91004.9}
\]

has one additional cofactor `m>=1`. If `n<=C2^r`, then `m<=C`, and the same argument gives

\[
\boxed{
\sum_{n\le C2^r}|(h^{*r}*a)(n)|
\ll_C r^{K_C}.
}
\tag{L-91004.10}
\]

The same conclusion holds after convolution by any fixed source supported in `1<=m<=M`: only the constant `C` is replaced by `CM`.

## 4. Exponential half-power Riesz decay

For an arithmetic source `f`, define its half-power Riesz transform

\[
\mathcal R_f(X)
=\sum_{n\le X}\frac{f(n)}{\sqrt n}
  \log\frac Xn.
\tag{L-91004.11}
\]

If `2^r<=X<=C2^r`, every term in `R_(h^r*a)` satisfies

\[
\frac1{\sqrt n}\le2^{-r/2},
\qquad
0\le\log(X/n)\le\log C.
\tag{L-91004.12}
\]

Combining with (L-91004.10) yields

\[
\boxed{
|\mathcal R_{h^{*r}*a}(X)|
\ll_C r^{K_C}2^{-r/2}\log C.
}
\tag{L-91004.13}
\]

For `C=4`,

\[
\boxed{
|\mathcal R_{h^{*r}*a}(X)|
\ll r^3 2^{-r/2}
\qquad(2^r\le X<4\,2^r).
}
\tag{L-91004.14}
\]

The estimate remains valid for a fixed finite linear combination of dyadic shifts.

## 5. Application to the phase-locked remainder

In `L-91003`,

\[
D=Q_r(K)G+K^rD.
\]

The source of `K^rD` is

\[
h^{*r}*(\varepsilon-\ell*\mu),
\tag{L-91004.15}
\]

where `ell` is the fixed phase-locked dyadic source. Equation (L-91004.13), with a constant enlarged only by the support of `ell`, gives

\[
\boxed{
|K^rD(X)|
\ll r^{K}2^{-r/2}
}
\tag{L-91004.16}
\]

through the scale-adapted diagonal `X<4*2^r`, for one fixed exponent `K`.

Thus the Möbius-bearing remainder is not merely delayed: it is exponentially small at the exact scale where the Brun projector is to be proved nonnegative.

At a hypothetical first negative point it is also nonnegative by causality. These two facts make the diagonal projector a genuinely finite conclusion-producing target rather than another uncontrolled reciprocal-zeta tail.

## 6. Interpretation

The renewal depth `r` should be viewed as a multiplicative analogue of heat or Hermite order. At the natural diagonal `X asymp 2^r`, increasing the order does not create exponentially many active configurations. Almost all factors are forced to be the minimal atom two, and only `O_C(1)` defects remain.

This is the combinatorial reason a moving-depth proof can plausibly succeed where a fixed-depth source fails.

## 7. Proof boundary

Closed exactly here:

1. minimal support `2^r`;
2. bounded number of nonminimal factors;
3. polynomial ordered-factor count;
4. extension to one bounded arithmetic cofactor and fixed local sources;
5. exponential half-power Riesz decay of the depth remainder;
6. application to the phase-locked renewal.

Open:

1. positivity of the Möbius-free Brun projector itself;
2. optimisation of an even-depth probability mixture;
3. RH.