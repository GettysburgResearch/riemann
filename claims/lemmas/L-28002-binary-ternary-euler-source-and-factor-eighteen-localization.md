# L-28002 — Binary–ternary Euler source and factor-eighteen localization

Claim ID: `L-28002`  
Title: The Euler factors at two and three give a positive-inverse generalized-prime source whose carry image is compact on the binary–ternary fragmentation  
Status: **PROPOSED COMPLETE EXACT ALGEBRA PLUS ELEMENTARY CARRY RESERVE**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: `L-28001`; generalized Selberg coefficient identity

## 1. Euler-aligned source

Define

\[
\boxed{
\omega_{2,3}
=\mu*(\varepsilon-\delta_2)*(\varepsilon-\delta_3).}
\tag{L-28002.1}
\]

Equivalently,

\[
\omega_{2,3}(n)
=\mu(n)
-\mathbf1_{2\mid n}\mu(n/2)
-\mathbf1_{3\mid n}\mu(n/3)
+\mathbf1_{6\mid n}\mu(n/6).
\]

Its Dirichlet series is

\[
\boxed{
\Omega_{2,3}(s)
=\frac{(1-2^{-s})(1-3^{-s})}{\zeta(s)}.}
\tag{L-28002.2}
\]

Neither Euler factor vanishes at a zeta zero in the open critical strip.

## 2. Compact floor and carry wavelet

Since

\[
\mathbf1*\omega_{2,3}
=\varepsilon-\delta_2-\delta_3+\delta_6,
\]

put

\[
G(x)
=\mathbf1_{x\ge1}
-\mathbf1_{x\ge2}
-\mathbf1_{x\ge3}
+\mathbf1_{x\ge6}.
\tag{L-28002.3}
\]

Then for every integer scale `m>=1` and real `x>=0`,

\[
\boxed{
\sum_{k\le x/m}\omega_{2,3}(k)
\left\lfloor\frac{x}{mk}\right\rfloor
=G(x/m).}
\tag{L-28002.4}
\]

Therefore the complete pointwise carry image is

\[
\boxed{
Z_{n,m}(j)
:=\sum_{k\le n/m}\omega_{2,3}(k)\chi_{n,mk}(j)
=G(n/m)-G(j/m)-G((n-j)/m).}
\tag{L-28002.5}
\]

The function `G` is supported on `[1,6)`: it is `+1` on `[1,2)`, zero on
`[2,3)`, and `-1` on `[3,6)`.

For the declared binary and ternary splits define

\[
\overline Z_{n,m}
=\frac12Z_{n,m}(\lfloor n/2\rfloor)
+\frac12Z_{n,m}(\lceil n/3\rceil).
\tag{L-28002.6}
\]

If

\[
n\ge18m-2,
\]

then the parent and every declared child are at least `6m`.  Hence

\[
\boxed{
\overline Z_{n,m}=0
\qquad(n\ge18m-2).}
\tag{L-28002.7}
\]

Thus the actual two-prime Euler source has no infinite quotient tail in the
binary–ternary carry image.  Every source row is confined to one finite
factor-eighteen transition band.

At scale `m=1`, the complete nonzero table is

\[
\boxed{
\begin{array}{c|rrrrrrrrrrrrr}
n&2&3&4&6&7&8&9&10&11&12&13&14&15\\ \hline
\overline Z_{n,1}
&-2&-2&-1&3/2&2&2&3/2&3/2&1&1/2&1/2&1/2&1/2.
\end{array}}
\tag{L-28002.8}
\]

All rows `n>=16` vanish at the bottom scale.

## 3. Positive inverse

The inverse Dirichlet series is

\[
A_{2,3}(s)
=\frac{\zeta(s)}{(1-2^{-s})(1-3^{-s})}
=\sum_{n\ge1}\frac{a_{2,3}(n)}{n^s}.
\]

Writing `v_p(n)` for the p-adic valuation gives the exact formula

\[
\boxed{
a_{2,3}(n)=(v_2(n)+1)(v_3(n)+1)>0.}
\tag{L-28002.9}
\]

The generalized von Mangoldt sequence defined by

\[
\Lambda_{2,3}
=\omega_{2,3}*(a_{2,3}\log)
\]

is

\[
\boxed{
\Lambda_{2,3}(q)
=\Lambda(q)
+(\log2)\mathbf1_{q=2^r}
+(\log3)\mathbf1_{q=3^r},
\qquad r\ge1.}
\tag{L-28002.10}
\]

Every coefficient is nonnegative.  The exact generalized Selberg identity is

\[
\boxed{
\omega_{2,3}*(a_{2,3}\log^2)
=\Lambda_{2,3}\log
+\Lambda_{2,3}*\Lambda_{2,3}.}
\tag{L-28002.11}
\]

This supplies the correct reflected positive forcing for the actual source.

## 4. Positive synthesis of the generalized-prime carry profile

For a fixed parent row `n`, put

\[
P_n(j)=\sum_{q\le n}\Lambda_{2,3}(q)\chi_{n,j}(q).
\]

Finite convolution switching gives

\[
\boxed{
P_n
=\sum_{m\le n}a_{2,3}(m)\log m\,Z_{n,m},
\qquad a_{2,3}(m)\log m\ge0.}
\tag{L-28002.12}
\]

All source cross terms are thereby retained.  Moreover

\[
P_n(j)=\log\binom nj+D_n(j),
\]

where

\[
0\le D_n(j)
\le2\log n+\log6.
\tag{L-28002.13}
\]

The correction has relative row `L2` norm `O(log n/n)` compared with the
ordinary Kummer profile.

## 5. Uniform carry-feature reserve

The wavelet `Z_(n,m)(j)` can change only when `j` crosses one of

\[
m,2m,3m,6m,n-m,n-2m,n-3m,n-6m.
\]

On the central interval

\[
I_n=
[\lceil n/4\rceil,\lfloor(n-2)/3\rfloor]\cap\mathbb Z,
\]

the ordinary Kummer profile

\[
F_n(j)=\log\binom nj
\]

increases by at least `log 2` at each step.  The at most eight source jumps cut
`I_n` into at most nine constant-source runs.  One run has length at least
`n/135` for all sufficiently large `n`.

The pairwise variance identity therefore gives, uniformly in `m` and every real
`c`,

\[
\boxed{
\sum_{j=0}^{n}(F_n(j)-cZ_{n,m}(j))^2
\ge\frac1{120,000,000}
\sum_{j=0}^{n}F_n(j)^2}
\tag{L-28002.14}
\]

once `n` exceeds one absolute finite threshold.  The finitely many smaller rows
belong in the production table.

By (L-28002.13), after enlarging that finite threshold the same statement holds
for the actual generalized-prime profile `P_n`, with another absolute positive
constant.  Thus the carry-side source has a genuine strict Schur reserve.

This does **not** identify the carry Gram with the physical independent-frequency
normal block.  That source map remains a separate proof obligation.

## 6. Ternary contraction back to the dyadic source

The sources satisfy

\[
\boxed{
\omega_{2,3}=b_2*(\varepsilon-\delta_3).}
\tag{L-28002.15}
\]

For their logarithmic Riesz signals,

\[
R_{2,3}(x)
=R_2(x)-3^{-1/2}R_2(x/3).
\tag{L-28002.16}
\]

Consequently, a nonpositive `R_(2,3)` on every sufficiently large scale,
together with the finitely checked base interval, iterates through the strict
factor `3^(-1/2)` to give `R_2(x)<=0`.  `L-28001` then gives RH.

The source signal is also a finite bottom combination of the producer:

\[
\boxed{
R_{2,3}(X)=
-2A_X(2)-2A_X(3)-A_X(4)
+\frac32A_X(6)+2A_X(7)+2A_X(8)
+\frac32A_X(9)+\frac32A_X(10)+A_X(11)
+\frac12\sum_{n=12}^{15}A_X(n).}
\tag{L-28002.17}
\]

Thus the full reciprocal-zeta obstruction is visible in thirteen bottom
producer coordinates and one finite factor-eighteen source family.

## 7. Proof boundary

Closed exactly or elementarily:

1. the compact scaled Euler carry wavelet;
2. factor-eighteen localization;
3. the complete bottom table;
4. positive inverse coefficients and generalized-prime weights;
5. positive wavelet synthesis;
6. a uniform carry-feature Schur reserve;
7. ternary contraction to the dyadic bottom charge.

Open:

1. the physical-normal-to-carry source map on the finite transition band;
2. a proof of the nonpositive `R_(2,3)` boundary charge;
3. RH.
