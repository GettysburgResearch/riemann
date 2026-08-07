# L-20804 — A factorially flat source notch beats its full coefficient metric

Claim ID: `L-20804`  
Title: The rational response `x^r/product(x-n^2)` suppresses every fixed off-line mode superpolynomially with only polylogarithmic whitened derivative cost  
Status: `PROVED FINITE ALGEBRA AND FULL METRIC/FACTORIAL FIXED-MODE BOUND; JOINT SCHUR RESIDUAL OPEN`  
Authoring agent: `gpt56-03-s`  
Created: 2026-08-01  
Dependencies: `D-0001`; `L-20801`; elementary gamma products and Stirling bounds  
Scope: an explicit source-normalized direction embedded in the square packet  
Related counterexample candidates: none

## 1. A maximally flat rational response

For an integer `r>=1`, define

\[
 \boxed{
 F_r(x)={x^r\over\prod_{n=1}^{r}(x-n^2)}.}
 \tag{L-20804.1}
\]

It has a zero of order `r` at `x=0`, simple poles at `1^2,...,r^2`, and
limit one at infinity. Its unique even partial-fraction expansion is

\[
 \boxed{
 F_r(x)=2\sum_{n=1}^{r}u_{r,n}{x\over x-n^2},}
 \tag{L-20804.2}
\]

where

\[
 \boxed{
 u_{r,n}=(-1)^{r-n}
 {n^{2r}\over(r-n)!(r+n)!}.}
 \tag{L-20804.3}
\]

Taking `x` to infinity gives the exact source identity

\[
 \boxed{2\sum_{n=1}^{r}u_{r,n}=1.}
 \tag{L-20804.4}
\]

Put this into the normalized even packet by

\[
 v_{r,0}=0,
 \qquad
 v_{r,n}=\sqrt2u_{r,n}\quad(1\le n\le r),
 \tag{L-20804.5}
\]

and pad by zero in every larger packet. Then

\[
 \boxed{\ell_N(v_r)=1.}
 \tag{L-20804.6}
\]

The profile has zero mean but nonzero source value:

\[
 T_r(t)=2\sum_{n=1}^{r}u_{r,n}\cos(2\pi nt),
 \qquad
 \int_0^1T_r(t)dt=0,
 \qquad
 T_r(0)=1.
 \tag{L-20804.7}
\]

Thus the growing notch does not evade the affine source constraint.

## 2. Exact factorial response

Let

\[
 L=\log c,
 \qquad
 \mu={Lz\over2\pi}.
 \tag{L-20804.8}
\]

The product formula is

\[
 F_r(\mu^2)
 =(-1)^r
 {\mu^{2r}\Gamma(1-\mu)\Gamma(1+\mu)
  \over
  \Gamma(r+1-\mu)\Gamma(r+1+\mu)}.
 \tag{L-20804.9}
\]

Insert this into the exact even D-0001 response

\[
 g_{v,L}(z)
 ={L\over\pi^2}
 {\sin^2(\pi\mu)\over\mu^2}
 F_r(\mu^2)^2.
 \tag{L-20804.10}
\]

The reflection identity

\[
 \Gamma(1-\mu)\Gamma(1+\mu)
 ={\pi\mu\over\sin\pi\mu}
 \tag{L-20804.11}
\]

cancels every sine and endpoint exponential exactly. Therefore

\[
\boxed{
 g_{r,L}(z)
 =L\left[
 {\mu^{2r}\over
  \Gamma(r+1-\mu)\Gamma(r+1+\mu)}
 \right]^2.}
 \tag{L-20804.12}
\]

The formula is entire in `z`. It is the complete growing-order factorial
ledger; no fixed-packet endpoint asymptotic is used.

## 3. Complete coefficient-metric charge

Equation (L-20804.3) may be written

\[
 |u_{r,n}|
 ={n^{2r}\over(2r)!}
 \binom{2r}{r-n}.
 \tag{L-20804.13}
\]

Hence

\[
\begin{aligned}
 \|v_r\|^2
 &=2\sum_{n=1}^{r}u_{r,n}^2\\
 &\le2\left({r^{2r}\over(2r)!}\right)^2
 \sum_{k=0}^{2r}\binom{2r}{k}^2\\
 &=2\left({r^{2r}\over(2r)!}\right)^2
 \binom{4r}{2r}.
\end{aligned}
 \tag{L-20804.14}
\]

Using

\[
 (2r)!\ge(2r/e)^{2r},
 \qquad
 \binom{4r}{2r}\le16^r,
\]

gives the simple source-bound estimate

\[
 \boxed{\|v_r\|^2\le2e^{4r}.}
 \tag{L-20804.15}
\]

At square level `(N,c)=(M,M^2)`, put `g_M=1+2M` and `x_M=g_Mv_r`.
The complete triangular graph metric satisfies

\[
\boxed{
 \Lambda_{M,r}^{\rm flat}
 :=1+{\|x_M\|^2\over g_M}
 =1+g_M\|v_r\|^2
 \le CMe^{4r}.}
 \tag{L-20804.16}
\]

This is intentionally crude. It already charges the full alternating
coefficient growth and is sufficient for the asymptotic below.

## 4. Uniform gamma bound

For `|mu|<=r/2`, uniform Stirling estimates give

\[
 |\Gamma(r+1-\mu)\Gamma(r+1+\mu)|
 \ge
 (r!)^2
 \exp\!\left(-C{|\mu|^2+1\over r}\right).
 \tag{L-20804.17}
\]

Consequently

\[
\boxed{
 |g_{r,L}(z)|
 \le
 L\,{|\mu|^{4r}\over(r!)^4}
 \exp\!\left(C{|\mu|^2+1\over r}\right).}
 \tag{L-20804.18}
\]

Unlike a finite-order notch, this bound contains no residual factor
`exp(|Im z|L)`: it has been absorbed by the exact order-`r` gamma cancellation.

A zero of fixed multiplicity contributes at most a fixed multiple of
`g_M|g_(r,L)(z)|` to the normalized source quadratic. Multiplying by the full
graph metric and using `r!>=(r/e)^r` yields

\[
\boxed{
\begin{aligned}
 \Lambda_{M,r}^{\rm flat}\varepsilon_{M,z}
 \le{}&CM^2L
 \left({e^2|\mu|\over r}\right)^{4r}
 \exp\!\left(C{|\mu|^2+1\over r}\right).
\end{aligned}}
 \tag{L-20804.19}
\]

Every coefficient and factorial cost has been retained.

## 5. Polylogarithmic degree closes every fixed mode

Use the square support

\[
 L=2\log M
 \tag{L-20804.20}
\]

and choose

\[
 \boxed{r_M=\left\lceil A(\log M)^2\right\rceil}
 \tag{L-20804.21}
\]

for any fixed `A>0`. For fixed `z`,

\[
 |\mu|=O_z(\log M),
 \qquad
 {|\mu|^2\over r_M}=O_{A,z}(1).
\]

Equation (L-20804.19) gives

\[
\begin{aligned}
 \log\left(
  \Lambda_{M,r_M}^{\rm flat}\varepsilon_{M,z}
 \right)
 \le{}&
 O(\log M+r_M)\\
 &-4r_M\log\left({r_M\over C_z\log M}\right)\\
 ={}&-4A(\log M)^2\log\log M
 +O_{A,z}((\log M)^2).
\end{aligned}
 \tag{L-20804.22}
\]

Therefore

\[
\boxed{
 \Lambda_{M,r_M}^{\rm flat}\varepsilon_{M,z}
 \longrightarrow0
}
 \tag{L-20804.23}
\]

faster than every inverse power of `M`, for every fixed zero parameter
`z` with `|Im z|<1/2`—indeed for every fixed complex `z`.

More generally, (L-20804.23) remains valid uniformly on any growing set
`|z|<=H_M` satisfying

\[
 H_M\log M=o(r_M)
 \tag{L-20804.24}
\]

with enough logarithmic room in (L-20804.22).

## 6. Whitened derivative cost

The large coefficients in (L-20804.3) do not reappear after whitening. Since
`T_r` has degree `r`, Bernstein's inequality gives

\[
 \|T_r^{(k)}\|_2
 \le(2\pi r)^k\|T_r\|_2.
 \tag{L-20804.25}
\]

Thus every fixed amplitude/support-derivative channel has whitened cost at most
a fixed power of `r`. With (L-20804.21), this cost is polylogarithmic:

\[
 \boxed{B_M=(\log M)^{O(1)}.}
 \tag{L-20804.26}
\]

In the multiplicative support variable `c=M^2`,

\[
 B_M=o\!\left(\sqrt{c/\log c}\right),
 \tag{L-20804.27}
\]

so the packet lies far inside the Hilbert-valued support-large-sieve threshold.
This is the full metric/factorial compatibility requested by the growing-notch
route.

## 7. Relation to the fixed-order obstruction

`L-20802` proves that a fixed packet or fixed endpoint order leaves a factor
`exp(|Im z|L)` which no polynomial support average removes. The order
`r_M~(log M)^2` in (L-20804.21) grows faster than the physical centered
frequency `mu=O(log M)`. Formula (L-20804.12) shows exactly how the factorial
denominator defeats that exponential while (L-20804.16) pays the complete
coefficient cost.

Thus the fixed-mode obstruction is genuinely bypassed, not hidden in a norm.

## 8. Exact remaining Schur obligation

For `x_M=g_Mv_(r_M)`, let

\[
 \mathscr R_M=P_WA_{M,M^2}x_M.
 \tag{L-20804.28}
\]

The source scalar is still

\[
\boxed{
 {g_M\over\ell_MA_{M,M^2}^{-1}\ell_M^*}
 ={1\over g_M}
 \left[
  \langle A_{M,M^2}x_M,x_M\rangle
  -\mathscr R_M^*A_{WW,M}^{-1}\mathscr R_M
 \right].}
 \tag{L-20804.29}
\]

The theorem proves that every fixed off-line contribution to the first term,
after the complete graph adapter, is superpolynomially small. It also proves
that the packet meets the support-average derivative threshold. It does not
bound the joint residual term in (L-20804.29).

Accordingly, the remaining proof target has become one concrete full-block
statement for this explicit packet:

\[
\boxed{
 \mathscr R_M^*A_{WW,M}^{-1}\mathscr R_M
 \le
 \langle A_{M,M^2}x_M,x_M\rangle
 +g_M\varepsilon_M,
 \qquad
 \Lambda_M\varepsilon_M+\delta_M\to0.}
 \tag{L-20804.30}
\]

It must be proved by the centered-prime resolvent cancellation or by the joint
line-centered graph/residual theorem. Raw trial suppression alone is excluded
by `R-20802`.

## 9. Proof boundary

- The finite partial fractions and gamma response are exact.
- The coefficient estimate pays the complete alternating factorial growth.
- The fixed-mode suppression beats the complete source graph metric and leaves
  only polylogarithmic whitened derivative costs.
- The construction is a genuine breakthrough on the growing-notch branch.
- The source Schur lower bound itself remains contingent on the single joint
  residual inequality (L-20804.30); no RH proof is claimed.
