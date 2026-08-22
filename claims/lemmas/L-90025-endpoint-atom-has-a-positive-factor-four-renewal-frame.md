# L-90025 — The critical endpoint atom has a positive factor-four renewal frame

Claim ID: `L-90025` (provisional range; branch-qualified)  
Title: The critically normalized endpoint kernel strictly increases under every factor-four scale step; its factor-four difference is positive and generates the whole endpoint atom by a positive renewal sum  
Status: **PROPOSED COMPLETE EXACT POSITIVITY / RENEWAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-10  
Depends on: the endpoint kernel formula of PR #265 `L-26204`; the effective square-root-sum bracket of `T-90002`  
Scope: the positive continuum endpoint atom; no sign theorem for the arithmetic equality weight and no RH conclusion

## 1. The endpoint kernel

Retain the scale-invariant endpoint response kernel

\[
 k(u)=2N-\frac{S_N}{\sqrt u},
 \qquad
 \frac1{N+1}<u\le\frac1N,
\tag{L-90025.1}
\]

where

\[
 S_N=\sum_{j=1}^{N}j^{-1/2}.
\]

In logarithmic coordinates put

\[
 \boxed{
 \varrho(t)=e^{-t/2}k(e^{-t}),
 \qquad t\ge0.
 }
\tag{L-90025.2}
\]

Writing

\[
 x=e^t,
 \qquad n=\lfloor x\rfloor,
\]

gives the exact cell form

\[
 \boxed{
 \varrho(t)=\frac{2n}{\sqrt x}-S_n.
 }
\tag{L-90025.3}
\]

PR #265 proves `varrho>0` and identifies it as the positive endpoint-scale convolution kernel. The new result is the strict factor-four scale inequality

\[
 \boxed{
 \varrho(t)>\varrho(t-\log4)
 \qquad(t\ge\log4).
 }
\tag{L-90025.4}
\]

## 2. Reduction to four quotient cases

Fix `x>=4` and put

\[
 m=\left\lfloor\frac x4\right\rfloor,
 \qquad
 n=\lfloor x\rfloor=4m+r,
 \qquad r\in\{0,1,2,3\}.
\tag{L-90025.5}
\]

Then

\[
\begin{aligned}
 \varrho(\log x)-\varrho(\log(x/4))
 &={2(n-2m)\over\sqrt x}-(S_n-S_m).
\end{aligned}
\tag{L-90025.6}
\]

For fixed `m,n`, the first term decreases with `x`. Since `x<n+1`, it is enough to prove

\[
 \boxed{
 S_n-S_m<{2(n-2m)\over\sqrt{n+1}}.
 }
\tag{L-90025.7}
\]

We treat `r=1,2,3` by convex midpoint integration and `r=0` by the effective Euler--Maclaurin bracket already resident in `T-90002`.

## 3. The three nonaligned cases

The function `f(x)=x^{-1/2}` is strictly convex. Hence Jensen's inequality on every unit interval centered at an integer gives

\[
 {1\over\sqrt k}
 <\int_{k-1/2}^{k+1/2}x^{-1/2}\,dx.
\]

Summing from `k=m+1` to `n` yields

\[
 \boxed{
 S_n-S_m
 <2\left(\sqrt{n+\frac12}-\sqrt{m+\frac12}\right).
 }
\tag{L-90025.8}
\]

It remains to show

\[
 \sqrt{n+\frac12}-\sqrt{m+\frac12}
 <{n-2m\over\sqrt{n+1}}.
\tag{L-90025.9}
\]

Both sides are positive. Put

\[
 A={n-2m\over\sqrt{n+1}},
 \qquad
 B=\sqrt{n+\frac12}-\sqrt{m+\frac12}.
\]

For `n=4m+r`, direct elimination of the remaining square root proves `A^2-B^2>0`. More explicitly, after moving the unique radical to the left and squaring, the positive remainders are

\[
\begin{array}{c|c}
 r&4(n+\frac12)(m+\frac12)-C_r(m)^2\\ \hline
1&{8m+3\over4},\\[1mm]
2&{64m^3+135m^2+92m+20\over(4m+3)^2},\\[1mm]
3&{96m^3+272m^2+240m+63\over16(m+1)^2},
\end{array}
\tag{L-90025.10}
\]

where

\[
 C_1(m)={8m+3\over2},
 \quad
 C_2(m)={16m^2+19m+5\over4m+3},
 \quad
 C_3(m)={16m^2+24m+7\over4(m+1)}.
\]

Every displayed numerator is strictly positive. Thus (L-90025.9), hence (L-90025.7), holds for `r=1,2,3`.

## 4. The aligned case

Let `n=4m`. `T-90002` proves the effective bounds

\[
 {1\over2\sqrt N}-R_S(N)
 \le S_N-2\sqrt N-\zeta(1/2)
 \le {1\over2\sqrt N},
\tag{L-90025.11}
\]

with

\[
 R_S(N)={1\over16}N^{-5/2}+{1\over24}N^{-3/2}.
\tag{L-90025.12}
\]

Therefore

\[
 S_{4m}-S_m
 \le2\sqrt m-{1\over4\sqrt m}+R_S(m).
\tag{L-90025.13}
\]

Put `y=1/(4m)`. The alternating binomial expansion, truncated after its negative cubic term, gives

\[
 (1+y)^{-1/2}
 \ge1-{y\over2}+{3y^2\over8}-{5y^3\over16}
 \qquad(0\le y\le1).
\tag{L-90025.14}
\]

Hence

\[
 {4m\over\sqrt{4m+1}}
 -\left(2\sqrt m-{1\over4\sqrt m}\right)
 \ge {3\over64m^{3/2}}-{5\over512m^{5/2}}.
\tag{L-90025.15}
\]

Subtracting (L-90025.12), the right side remains positive whenever

\[
 {1\over192m^{3/2}}-{37\over512m^{5/2}}>0,
\]

i.e. whenever `m>=14`. Thus

\[
 S_{4m}-S_m<{4m\over\sqrt{4m+1}}
\tag{L-90025.16}
\]

for every `m>=14`.

The thirteen remaining values are finite radical inequalities. The directed checker `X-90021` proves them with the uniform positive lower bounds

\[
\begin{array}{c|ccccccccccccc}
 m&1&2&3&4&5&6&7&8&9&10&11&12&13\\ \hline
10^4\,\delta_m
&43&23&14&10&7&6&4&4&3&2&2&2&2,
\end{array}
\tag{L-90025.17}
\]

where

\[
 \delta_m={4m\over\sqrt{4m+1}}-(S_{4m}-S_m)>0.
\]

The table rounds downward and is only a readable summary; the retained rational square-root enclosures are the proof object.

Sections 2--4 prove (L-90025.4).

## 5. A positive factor-four detail atom

Define causally

\[
\boxed{
 \eta_4(t)=\varrho(t)-\varrho(t-\log4),
 \qquad \varrho(s)=0\ (s<0).
}
\tag{L-90025.18}
\]

Then

\[
\boxed{
 \eta_4(t)>0\qquad(t>0).
}
\tag{L-90025.19}
\]

For `0<t<log4` this is just positivity of `varrho`; for later times it is (L-90025.4).

The Laplace transform is

\[
\boxed{
 \widehat\eta_4(z)
 =(1-4^{-z})\widehat\varrho(z)
 =(1-4^{-z})
 \zeta\left(z+\frac12\right)
 {z-\frac12\over z(z+\frac12)}.
}
\tag{L-90025.20}
\]

No off-line zero is canceled: if `Re z>0`, then `|4^{-z}|<1`.

The endpoint atom has the exact positive renewal expansion

\[
\boxed{
 \varrho(t)
 =\sum_{j=0}^{\lfloor t/\log4\rfloor}
   \eta_4(t-j\log4).
}
\tag{L-90025.21}
\]

This is finite at every physical time and follows by telescoping.

## 6. Relation to the preferred factor-64 state

Let `S` denote delay by `log2`. The improved factor-64 multiplier is

\[
 P_{64}^*(S)
 =\left(1+{3\over4}S+S^2\right)
  (1-S)(1-2^{-1/2}S)(1-S^2).
\tag{L-90025.22}
\]

The last factor produces exactly the positive block atom:

\[
 (1-S^2)\varrho=\eta_4>0.
\tag{L-90025.23}
\]

Consequently the preferred endpoint criterion can be read as

```text
positive factor-four endpoint block
-> critical Haar detail (1-S/sqrt(2))
-> ordinary scale detail (1-S)
-> positive three-tap smoothing.
```

All remaining signedness is confined to the two first-order detail filters acting on the positive renewal atom `eta_4`; it is no longer hidden in the endpoint kernel itself.

## 7. Proof boundary

Closed exactly, subject to review:

1. strict factor-four monotonicity of the critically normalized endpoint kernel;
2. the positive detail atom `eta_4`;
3. the exact positive renewal decomposition of the endpoint atom;
4. the zero-safe transform identity;
5. localization of the preferred factor-64 signedness to two first-order details of a positive block atom.

Still open:

1. a finite martingale/carry lift for the two detail filters;
2. the factor-64 three-window inequality of `L-90024`;
3. RH.
