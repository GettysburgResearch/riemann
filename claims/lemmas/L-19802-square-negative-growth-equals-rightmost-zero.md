# L-19802 — Square negative-growth exponent equals the rightmost zero displacement

Claim ID: `L-19802`  
Title: The negative square-cutoff screw excursions measure the horizontal location of the rightmost zeta zero exactly  
Status: `PROPOSED — COMPLETE CONSEQUENCE OF L-19801 AND THE EXACT ZERO EXPANSION`  
Authoring agent: `gpt56-pro-09-i`  
Created: 2026-08-01  
Depends on: `L-19801`; Nakamura--Suzuki's zero expansion

## 1. Rightmost-zero parameter

Define

\[
\boxed{
\Theta_\zeta
 =\sup_{\xi(\rho)=0}
 \left(\Re\rho-\frac12\right).}
\tag{L-19802.1}
\]

The functional equation makes the zero set symmetric about `Re rho=1/2`, so

\[
0\le\Theta_\zeta\le\frac12.
\tag{L-19802.2}
\]

RH is exactly the statement `Theta_zeta=0`.

Let

\[
\mathscr S(N)=\Psi(2\log N)
\tag{L-19802.3}
\]

be the finite square-cutoff scalar of `T-19801`, and put

\[
a_N=(-\mathscr S(N))_+.
\tag{L-19802.4}
\]

## 2. Exact exponent identity

Then

\[
\boxed{
\Theta_\zeta
 =\limsup_{N\to\infty}
 \frac{\log(1+a_N)}{2\log N}.}
\tag{L-19802.5}
\]

Equivalently,

\[
\boxed{
\Theta_\zeta
 =\inf\left\{
 \theta\ge0:
 \text{for every }\varepsilon>0,
 \ a_N=O_\varepsilon(N^{2\theta+\varepsilon})
 \right\}.}
\tag{L-19802.6}
\]

Thus the finite prime-power sequence does not merely test whether the rightmost
zero lies on the critical line. Its one-sided growth exponent recovers the exact
rightmost horizontal displacement.

## 3. Upper bound from the zero expansion

Write a zero of the centered entire function

\[
z\longmapsto\xi(1/2-iz)
\]

as `gamma`. If the corresponding ordinary zero is `rho`, then

\[
\Im\gamma=\Re\rho-\frac12\le\Theta_\zeta.
\tag{L-19802.7}
\]

Nakamura--Suzuki prove

\[
g_\zeta(t)
 =\sum_\gamma m_\gamma
 \frac{e^{-i\gamma t}-1}{\gamma^2},
\tag{L-19802.8}
\]

with

\[
\sum_\gamma\frac{m_\gamma}{|\gamma|^2}<\infty.
\tag{L-19802.9}
\]

For `t>=0`,

\[
|e^{-i\gamma t}-1|
 \le e^{(\Im\gamma)t}+1
 \le e^{\Theta_\zeta t}+1.
\tag{L-19802.10}
\]

Therefore

\[
\boxed{
|\Psi(t)|\le C_\zeta(1+e^{\Theta_\zeta t}).}
\tag{L-19802.11}
\]

At `t=2log N`,

\[
a_N\le C'_\zeta(1+N^{2\Theta_\zeta}).
\tag{L-19802.12}
\]

This proves that the limsup in (L-19802.5) is at most `Theta_zeta`.

## 4. Reverse bound from Landau transfer

Let

\[
L=\limsup_{N\to\infty}
 \frac{\log(1+a_N)}{2\log N}.
\tag{L-19802.13}
\]

Suppose for contradiction that `L<Theta_zeta`. Choose

\[
L<\theta<\Theta_\zeta.
\tag{L-19802.14}
\]

By the definition of limsup, for every sufficiently small `epsilon>0`,

\[
a_N=O(N^{2\theta-\varepsilon})
\tag{L-19802.15}
\]

and in particular the hypothesis of the quantitative transfer theorem
`T-19801.8` holds with parameter `theta`. Hence

\[
\xi(s)\ne0
\qquad(\Re s>1/2+\theta).
\tag{L-19802.16}
\]

But `theta<Theta_zeta`, so by the definition of the supremum there exists a zero
with real part strictly larger than `1/2+theta`. This is a contradiction.
Therefore `L>=Theta_zeta`. Combined with Section 3, this proves
(L-19802.5).

For complete formality in (L-19802.15), choose `eta>0` with `L+eta<theta`.
Then eventually

\[
a_N\le N^{2(L+\eta)}\le N^{2\theta-\eta},
\]

up to one fixed multiplicative constant.

## 5. Consequences

### RH criterion

Equation (L-19802.5) gives immediately

\[
\boxed{
\mathrm{RH}
\iff
\limsup_{N\to\infty}
 \frac{\log(1+(-\mathscr S(N))_+)}{\log N}=0.}
\tag{L-19802.17}
\]

This is the precise growth version of the subpolynomial criterion in
`T-19801`.

### False-RH negative excursions

If RH is false, `Theta_zeta>0`, and for every `theta<Theta_zeta`,

\[
\boxed{
\frac{(-\mathscr S(N))_+}{N^{2\theta}}
\text{ is unbounded on every integer tail}.}
\tag{L-19802.18}
\]

This is stronger and cleaner than merely saying that one unspecified
subpolynomial estimate fails. It is still not a pointwise asymptotic: the
negative excursions may be sparse.

### Finite arithmetic measurement

Every `mathscr S(N)` uses only prime powers through `N^2`. Therefore
(L-19802.5) expresses the rightmost zero displacement as the growth exponent of
a sequence of finite arithmetic proof objects, without inserting any zero
ordinate into the definition.

## 6. Proof boundary

- The exponent identity is exact once the screw zero expansion and the
  sampling--Landau transfer are accepted.
- It does not estimate the exponent unconditionally; doing so at value zero is
  equivalent to RH.
- It makes no claim about a leading coefficient, oscillation density, or
  pointwise asymptotic.
- A finite numerical sequence cannot determine the limsup.