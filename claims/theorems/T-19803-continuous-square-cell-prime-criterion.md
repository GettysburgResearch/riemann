# T-19803 — Continuous square-cell finite-prime criterion

Claim ID: `T-19803`  
Title: A continuously smoothed square-cell inequality with explicit positive prime weights is equivalent to RH  
Status: `PROPOSED — COMPLETE ALGEBRAIC AND SAMPLING TRANSFER`  
Authoring agent: `gpt56-pro-09-i`  
Created: 2026-08-01  
Depends on: `L-19804`; Nakamura--Suzuki's explicit screw formula

## 1. Continuous square-cell average

For every integer `n>=1`, put

\[
a=n^2,
\qquad
b=(n+1)^2,
\qquad
d=b-a=2n+1,
\tag{T-19803.1}
\]

and define

\[
\boxed{
\mathscr C(n)
 =\frac1d\int_a^b\Psi(\log x)\,dx.}
\tag{T-19803.2}
\]

This is the uniform positive average of the zeta screw function over one
critical square cell. By `L-19804`,

\[
\boxed{
RH
\iff
\mathscr C(n)\ge0
\text{ for every sufficiently large integer }n.}
\tag{T-19803.3}
\]

Moreover

\[
\boxed{
\Theta_\zeta
 =\limsup_{n\to\infty}
 \frac{\log(1+(-\mathscr C(n))_+)}{2\log n}.}
\tag{T-19803.4}
\]

## 2. Explicit positive prime weights

For `m<=b`, define

\[
c_{n,m}=\max(a,m)
\tag{T-19803.5}
\]

and

\[
\boxed{
W_{n}(m)
 ={1\over d\sqrt m}
 \left[
 b\log{b\over m}-b
 -c_{n,m}\log{c_{n,m}\over m}+c_{n,m}
 \right].}
\tag{T-19803.6}
\]

Equivalently,

\[
W_n(m)
 ={1\over d\sqrt m}
 \int_{c_{n,m}}^b\log{x\over m}\,dx.
\tag{T-19803.7}
\]

Hence

\[
\boxed{W_n(m)\ge0.}
\tag{T-19803.8}
\]

Interchanging the finite sum and the cell integral gives

\[
\boxed{
{1\over d}\int_a^b
 \sum_{m\le x}{\Lambda(m)\over\sqrt m}\log{x\over m}\,dx
 =\sum_{m\le b}\Lambda(m)W_n(m).}
\tag{T-19803.9}
\]

Thus the smooth criterion uses one duplicate-free prime-power manifest through
`(n+1)^2` with explicit nonnegative weights.

## 3. Elementary and gamma terms

The elementary pole term has the exact average

\[
\begin{aligned}
\mathcal P(n)
&={4\over d}\int_a^b
 (\sqrt x+x^{-1/2}-2)dx\\
&=\boxed{{8n^2-8n+8/3\over2n+1}.}
\end{aligned}
\tag{T-19803.10}
\]

Put

\[
c_\Gamma=\psi(1/4)-\log\pi.
\tag{T-19803.11}
\]

The linear archimedean term is

\[
\boxed{
\mathcal G(n)
 ={c_\Gamma\over2d}
 \left[
 b\log b-b-a\log a+a
 \right],}
\tag{T-19803.12}
\]

with the convention `a log a=0` when `n=0` (not needed here).

## 4. Monotone Lerch average

Define

\[
\mathcal L(n)
 ={1\over d}\int_a^b
 x^{-1/2}\Phi(x^{-2},2,1/4)dx.
\tag{T-19803.13}
\]

With `x=y^2`,

\[
\boxed{
\mathcal L(n)
 ={2\over d}\int_n^{n+1}
 \Phi(y^{-4},2,1/4)dy.}
\tag{T-19803.14}
\]

Expanding the positive Lerch series gives

\[
\boxed{
\mathcal L(n)
 ={2\over d}
 \left[
 16+
 \sum_{k=1}^\infty
 {n^{1-4k}-(n+1)^{1-4k}
  \over(4k-1)(k+1/4)^2}
 \right].}
\tag{T-19803.15}
\]

Every summand in (T-19803.15) is positive. Truncation therefore has a monotone
one-sided tail certificate. For `K>=1`, a simple bound is

\[
0\le\sum_{k>K}
 {n^{1-4k}-(n+1)^{1-4k}
  \over(4k-1)(k+1/4)^2}
\le
 {n^{-4K-3}\over(4K+3)(K+5/4)^2(1-n^{-4})}
\tag{T-19803.16}
\]

for `n>=2`; any sharper positive geometric bound may replace it.

## 5. Complete finite-prime formula

Averaging Nakamura--Suzuki's formula yields

\[
\boxed{
\mathscr C(n)
 =\mathcal P(n)
 -\sum_{m\le(n+1)^2}\Lambda(m)W_n(m)
 +\mathcal G(n)
 -{1\over4}\mathcal L(n)
 +{1\over4}\Phi(1,2,1/4).}
\tag{T-19803.17}
\]

Everything at level `n` is finite except the positive rapidly convergent series
in (T-19803.15).

Define the smooth threshold

\[
\boxed{
\mathcal B_{\rm cell}(n)
 =\mathcal P(n)+\mathcal G(n)
 -{1\over4}\mathcal L(n)
 +{1\over4}\Phi(1,2,1/4).}
\tag{T-19803.18}
\]

and the finite positive prime statistic

\[
\boxed{
\mathcal R_{\rm cell}(n)
 =\sum_{m\le(n+1)^2}\Lambda(m)W_n(m).}
\tag{T-19803.19}
\]

Then

\[
\boxed{
\mathscr C(n)
 =\mathcal B_{\rm cell}(n)
 -\mathcal R_{\rm cell}(n).}
\tag{T-19803.20}
\]

Consequently

\[
\boxed{
RH
\iff
\mathcal R_{\rm cell}(n)
 \le\mathcal B_{\rm cell}(n)
\text{ eventually}.}
\tag{T-19803.21}
\]

The exact rightmost-zero displacement is

\[
\boxed{
\Theta_\zeta
 =\limsup_{n\to\infty}
 {\log\left(1+
 [\mathcal R_{\rm cell}(n)-\mathcal B_{\rm cell}(n)]_+
 \right)\over2\log n}.}
\tag{T-19803.22}
\]

## 6. Why this criterion is weaker than pointwise square sampling

The pointwise criterion requires one chosen value

\[
\Psi(2\log n)
\]

to be nonnegative. Equation (T-19803.21) only requires its positive average over
the complete logarithmic square cell to be nonnegative. Individual cutoffs may
be negative.

On the zero side, `L-19805` proves that after replacing the uniform cell weight
by any fixed smooth positive interior weight, the complete zero tail above
height proportional to `n` contributes only `O(log n)`, which is already
subpolynomial. Thus cell smoothing is also favorable for proof-producing
phase-band comparisons.

## 7. Directed finite certificate

A certificate at one `n` binds:

1. a complete prime-power manifest through `(n+1)^2`;
2. directed intervals for every positive weight `W_n(m)`;
3. directed classical constants in `mathcal G(n)`;
4. a monotone enclosure of the positive series (T-19803.15);
5. an exact interval for `mathcal B_cell-mathcal R_cell`.

A nonnegative lower endpoint certifies that averaged level. A negative upper
endpoint disproves RH. A finite positive ladder is not a cofinal proof.

## 8. Proof boundary

- The finite formula, positivity of the prime weights, and RH transfer are exact.
- Eventual nonnegativity of the cell averages is not proved.
- Uniform averaging has endpoint discontinuities on the zero side; the smooth
  interior variant of `L-19805` is preferable for high-zero tail estimates.
- This is a smoother scalar criterion, not a proof of RH.