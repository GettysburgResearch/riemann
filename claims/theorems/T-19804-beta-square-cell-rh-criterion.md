# T-19804 — Explicit beta-smoothed square-cell criterion

Claim ID: `T-19804`  
Title: One polynomially smoothed finite prime-power inequality per square cell is equivalent to RH and has an unconditional logarithmic high-zero tail  
Status: `PROPOSED — COMPLETE TRANSFER AND FINITE FORMULA; COFINAL SIGN OPEN`  
Authoring agent: `gpt56-pro-09-i`  
Created: 2026-08-01  
Depends on: `L-19804`; `L-19805`; Nakamura--Suzuki's explicit formula

## 1. Fixed beta weight

Let

\[
\boxed{w(u)=30u^2(1-u)^2,\qquad0\le u\le1.}
\tag{T-19804.1}
\]

Then `w>=0`,

\[
\int_0^1w(u)du=1,
\tag{T-19804.2}
\]

and

\[
w(0)=w(1)=w'(0)=w'(1)=0.
\tag{T-19804.3}
\]

For `n>=1`, put

\[
a=n^2,
\qquad d=2n+1,
\qquad x_n(u)=a+du,
\tag{T-19804.4}
\]

and define

\[
\boxed{
\mathscr C_\beta(n)
 =\int_0^1w(u)\Psi(\log x_n(u))du.}
\tag{T-19804.5}
\]

By positive square-cell averaging,

\[
\boxed{
RH
\iff
\mathscr C_\beta(n)\ge0
\text{ for every sufficiently large }n.}
\tag{T-19804.6}
\]

Also

\[
\boxed{
\Theta_\zeta
 =\limsup_{n\to\infty}
 {\log(1+(-\mathscr C_\beta(n))_+)\over2\log n}.}
\tag{T-19804.7}
\]

## 2. Reusable elementary antiderivatives

For real `q` and integer `r>=0`, define

\[
\boxed{
J_{r,q}(x)
 ={1\over d^{r+1}}
 \sum_{j=0}^r{r\choose j}(-a)^{r-j}
 {x^{j+q+1}\over j+q+1},}
\tag{T-19804.8}
\]

whenever no denominator vanishes. Then

\[
{d\over du}J_{r,q}(x_n(u))
 =u^r x_n(u)^q.
\tag{T-19804.9}
\]

All exponents used below are half-integers, so the denominators in
(T-19804.8) are nonzero.

For `m>0`, define

\[
\boxed{
H_{r,m}(x)
 ={1\over d^{r+1}}
 \sum_{j=0}^r{r\choose j}(-a)^{r-j}x^{j+1}
 \left[
 {\log(x/m)\over j+1}-{1\over(j+1)^2}
 \right].}
\tag{T-19804.10}
\]

Then

\[
{d\over du}H_{r,m}(x_n(u))
 =u^r\log{x_n(u)\over m}.
\tag{T-19804.11}
\]

For any endpoint pair `x_0<x_1`, put

\[
\begin{aligned}
\mathfrak J_q[x_0,x_1]
={}&30\sum_{r=2}^4c_r
 \bigl(J_{r,q}(x_1)-J_{r,q}(x_0)\bigr),\\
\mathfrak H_m[x_0,x_1]
={}&30\sum_{r=2}^4c_r
 \bigl(H_{r,m}(x_1)-H_{r,m}(x_0)\bigr),
\end{aligned}
\tag{T-19804.12}
\]

where

\[
(c_2,c_3,c_4)=(1,-2,1).
\tag{T-19804.13}
\]

Thus

\[
\mathfrak J_q[x_n(u_0),x_n(u_1)]
 =\int_{u_0}^{u_1}w(u)x_n(u)^qdu,
\tag{T-19804.14}
\]

and similarly `mathfrak H_m` integrates
`w(u)log(x_n(u)/m)`.

## 3. Explicit positive prime weights

For every integer `m<=(n+1)^2`, set

\[
u_{n,m}
 =\max\left(0,{m-n^2\over2n+1}\right)
\tag{T-19804.15}
\]

and

\[
\boxed{
W_{\beta,n}(m)
 ={1\over\sqrt m}
 \mathfrak H_m[m\vee n^2,(n+1)^2].}
\tag{T-19804.16}
\]

Equivalently,

\[
W_{\beta,n}(m)
 ={1\over\sqrt m}
 \int_{u_{n,m}}^1
 w(u)\log{x_n(u)\over m}du.
\tag{T-19804.17}
\]

Therefore

\[
\boxed{W_{\beta,n}(m)\ge0.}
\tag{T-19804.18}
\]

Interchanging the finite prime sum and the beta integral gives

\[
\boxed{
\int_0^1w(u)
 \sum_{m\le x_n(u)}{\Lambda(m)\over\sqrt m}
 \log{x_n(u)\over m}du
 =\sum_{m\le(n+1)^2}\Lambda(m)W_{\beta,n}(m).}
\tag{T-19804.19}
\]

## 4. Explicit archimedean terms

The elementary pole term is

\[
\boxed{
\mathcal P_\beta(n)
 =4\left(
 \mathfrak J_{1/2}[n^2,(n+1)^2]
 +\mathfrak J_{-1/2}[n^2,(n+1)^2]
 -2
 \right).}
\tag{T-19804.20}
\]

The linear gamma term is

\[
\boxed{
\mathcal G_\beta(n)
 ={\psi(1/4)-\log\pi\over2}
 \mathfrak H_1[n^2,(n+1)^2].}
\tag{T-19804.21}
\]

For the Lerch term, define

\[
\boxed{
\mathcal L_\beta(n)
 =\sum_{k=0}^\infty
 {\mathfrak J_{-2k-1/2}[n^2,(n+1)^2]
  \over(k+1/4)^2}.}
\tag{T-19804.22}
\]

Every summand is positive. Since `x_n(u)>=n^2`, for `K>=0` and `n>=2`,

\[
\boxed{
0\le\sum_{k>K}
 {\mathfrak J_{-2k-1/2}\over(k+1/4)^2}
 \le
 {n^{-4K-5}\over(K+5/4)^2(1-n^{-4})}.}
\tag{T-19804.23}
\]

Thus the Lerch average has a monotone, elementary directed tail.

## 5. Complete finite formula

Averaging Nakamura--Suzuki's screw formula yields

\[
\boxed{
\begin{aligned}
\mathscr C_\beta(n)={}&
 \mathcal P_\beta(n)
 -\sum_{m\le(n+1)^2}\Lambda(m)W_{\beta,n}(m)\\
&+\mathcal G_\beta(n)
 -{1\over4}\mathcal L_\beta(n)
 +{1\over4}\Phi(1,2,1/4).
\end{aligned}}
\tag{T-19804.24}
\]

Define

\[
\mathcal R_\beta(n)
 =\sum_{m\le(n+1)^2}\Lambda(m)W_{\beta,n}(m)
\tag{T-19804.25}
\]

and

\[
\mathcal B_\beta(n)
 =\mathcal P_\beta(n)+\mathcal G_\beta(n)
 -{1\over4}\mathcal L_\beta(n)
 +{1\over4}\Phi(1,2,1/4).
\tag{T-19804.26}
\]

Then

\[
\boxed{
\mathscr C_\beta(n)
 =\mathcal B_\beta(n)-\mathcal R_\beta(n).}
\tag{T-19804.27}
\]

Consequently

\[
\boxed{
RH
\iff
\mathcal R_\beta(n)\le\mathcal B_\beta(n)
\text{ eventually}.}
\tag{T-19804.28}
\]

The rightmost zero satisfies

\[
\boxed{
\Theta_\zeta
 =\limsup_{n\to\infty}
 {\log\left(1+
 [\mathcal R_\beta(n)-\mathcal B_\beta(n)]_+
 \right)\over2\log n}.}
\tag{T-19804.29}
\]

## 6. Unconditional high-zero tail

Because the beta weight and its first derivative vanish at both endpoints, the
nonstationary argument of `L-19805` applies with two integrations by parts. For
any fixed `A>0`, the complete contribution of centered zeros satisfying

\[
|\Re\gamma|\ge An
\]

to the zero-side expansion of `mathscr C_beta(n)` is

\[
\boxed{O_A(\log(n+2)).}
\tag{T-19804.30}
\]

unconditionally, including every hypothetical off-line zero.

Thus all super-subpolynomial obstruction is confined to the finite moving zero
block `|Re gamma|<An`; no infinite zero tail larger than logarithmic size needs
to be budgeted.

## 7. Proof-producing advantages

This one criterion simultaneously provides:

1. a finite prime-power manifest through `(n+1)^2`;
2. nonnegative explicit prime weights;
3. elementary antiderivatives for all non-Lerch terms;
4. a positive monotone Lerch tail;
5. two endpoint zeros, sufficient for an unconditional logarithmic high-zero
   tail;
6. exact RH equivalence and exact recovery of the rightmost zero exponent.

It is therefore the preferred production form of the square-cell programme.

## 8. Proof boundary

- Every algebraic formula and tail reduction above is exact.
- The eventual beta-smoothed inequality is not proved.
- The `O(log n)` high-zero tail does not decide the finite moving zero block.
- A finite positive computation remains reconnaissance, not a proof of RH.