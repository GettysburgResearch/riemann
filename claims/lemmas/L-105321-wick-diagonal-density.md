# L-105321 — The first-chaos-cancelled coefficient energy is below 7/320

Claim ID: `L-105321`  
Status: **PROVED FROM THE PRIME NUMBER THEOREM**  
Created: 2026-08-23  
Depends on: `L-105320`  
RH status: **not assumed**

Let

\[
c_m=\sum_{j=0}^m{(-1)^j\over j!}
\]

and, for `L>0`, define the normalized first-chaos-cancelled arithmetic
coefficients

\[
\boxed{
a_L(n)=
\sum_{m=2}^{\Omega(n)}c_mL^{-m}\Lambda^{*m}(n).}
\tag{L-105321.1}
\]

These are the nonconstant coefficients of

\[
L e^{-A/L}(L-A)^{-1}.
\]

## 1. Fixed source degree

If `n=p_1...p_m` is squarefree with `m` distinct prime factors, then

\[
\Lambda^{*m}(n)=m!\prod_{j=1}^m\log p_j,
\]

and every other convolution order vanishes at `n`. Hence the degree-`m`
squarefree contribution to

\[
\sum_{n\le e^L}{a_L(n)^2\over n}
\]

is

\[
c_m^2L^{-2m}(m!)^2
\sum_{p_1<\cdots<p_m\atop p_1\cdots p_m\le e^L}
\prod_{j=1}^m{(\log p_j)^2\over p_j}.
\tag{L-105321.2}
\]

The prime number theorem in Stieltjes form gives, for every fixed `m`,

\[
L^{-2m}
\sum_{p_1<\cdots<p_m\atop p_1\cdots p_m\le e^L}
\prod_j{(\log p_j)^2\over p_j}
\longrightarrow
{1\over m!(2m)!}.
\tag{L-105321.3}
\]

Indeed, after `u_j=log p_j/L`, the limiting measure is
`u_j du_j`, and

\[
\int_{u_j\ge0,\ \sum u_j\le1}\prod_ju_j\,du
={1\over(2m)!}.
\]

Thus the fixed-degree limit is

\[
\boxed{c_m^2{m!\over(2m)!}.}
\tag{L-105321.4}
\]

## 2. Repeated-prime terms

Group a nonsquarefree integer by its prime exponents and by the number of
von Mangoldt convolution factors assigned to each prime. At least one local
factor then contains a convergent sum

\[
\sum_p{(\log p)^r\over p^e},\qquad e\ge2,
\]

instead of a scale-`L^2` prime integral. After the normalization in
(L-105321.1), every fixed exponent pattern is `O(L^-2)` relative to its
squarefree partner. Hence, for fixed source degrees `m,k`,

\[
L^{-m-k}
\sum_{n\le e^L}{\Lambda^{*m}(n)\Lambda^{*k}(n)\over n}
\longrightarrow
\begin{cases}
 m!/(2m)!,&m=k,\\
 0,&m\ne k.
\end{cases}
\tag{L-105321.5a}
\]

For completeness, the interchange of the source-degree sum and the limit has
a uniform elementary majorant. The pointwise bound

\[
0\le\Lambda^{*m}(n)\le(\log n)^m\le L^m
\]

and the standard reciprocal von-Mangoldt convolution estimate

\[
\sum_{n\le e^L}{\Lambda^{*m}(n)\over n}
\le{(L+mK)^m\over m!}
\tag{L-105321.5b}
\]

for one absolute `K` give

\[
L^{-2m}\sum_{n\le e^L}{(\Lambda^{*m}(n))^2\over n}
\le{(1+mK/L)^m\over m!}.
\tag{L-105321.5c}
\]

Since `m<=Omega(n)<=L/log 2`, the right side is bounded by
`C^m/m!` for one absolute `C`, uniformly in `L`; mixed degrees are bounded by
Cauchy--Schwarz. Thus `sum C^(m/2)/sqrt(m!)` is a uniform summable majorant.
This justifies dominated convergence without any growing-degree assumption.

Consequently

\[
\boxed{
\lim_{L\to\infty}
\sum_{n\le e^L}{a_L(n)^2\over n}
=\mathcal D_W
:=\sum_{m=2}^\infty c_m^2{m!\over(2m)!}.}
\tag{L-105321.5d}
\]

The same proof is uniform for `n<=e^(theta L)` on compact `theta`-intervals,
with the factor `theta^(2m)` in the summand.

## 3. Explicit rational upper bound

The first three summands are

\[
{1\over48},
\qquad
{1\over1080},
\qquad
{3\over35840}.
\]

For `m>=2`, the alternating-series estimate gives `0<c_m<=1/2`. Put
`t_m=m!/(2m)!`. For `m>=5`,

\[
{t_{m+1}\over t_m}={1\over2(2m+1)}\le{1\over22}.
\]

Therefore

\[
\sum_{m\ge5}c_m^2t_m
\le {1\over4}{t_5\over1-1/22}
={11\over1270080}.
\]

Hence

\[
\boxed{
\mathcal D_W
\le {1\over48}+{1\over1080}+{3\over35840}
+{11\over1270080}
<{7\over320}.}
\tag{L-105321.6}
\]

Numerically `mathcal D_W=0.0218476222...`; the decimal is diagnostic only.

## 4. Meaning

The raw degree-one source contributes `1/2`. The zero-free Wick congruence
removes it exactly and leaves less than `7/320` of one-sided normalized
coefficient energy. This is an unconditional arithmetic improvement, not an
assumption about Xi zeros.
