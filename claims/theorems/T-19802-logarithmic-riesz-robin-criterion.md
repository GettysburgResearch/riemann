# T-19802 — Robin-style logarithmic Riesz criterion for RH

Claim ID: `T-19802`  
Title: RH is equivalent to one explicit upper inequality for a finite logarithmic Riesz mean of the von Mangoldt function  
Status: `PROPOSED — COMPLETE ALGEBRAIC CONSEQUENCE OF T-19801`  
Authoring agent: `gpt56-pro-09-i`  
Created: 2026-08-01  
Depends on: `T-19801`; `L-19802`

## 1. Finite logarithmic Riesz mean

For every integer `N>=2`, define

\[
\boxed{
\mathcal R(N)
 =\sum_{m\le N^2}
 \frac{\Lambda(m)}{\sqrt m}
 \left(1-\frac{\log m}{2\log N}\right).}
\tag{T-19802.1}
\]

Every weight in (T-19802.1) is nonnegative, and the endpoint weight at
`m=N^2` is zero.

Define the explicit archimedean threshold

\[
\boxed{
\begin{aligned}
\mathcal B(N)={}&
 \frac{2(N+N^{-1}-2)}{\log N}
 +\frac12\bigl(\psi(1/4)-\log\pi\bigr)\\
&-\frac{1}{8\log N}
 \left[
 N^{-1}\Phi(N^{-4},2,1/4)
 -\Phi(1,2,1/4)
 \right].
\end{aligned}}
\tag{T-19802.2}
\]

The square-screw scalar satisfies the exact identity

\[
\boxed{
\mathscr S(N)
 =2\log N\,[\mathcal B(N)-\mathcal R(N)].}
\tag{T-19802.3}
\]

This follows immediately by factoring `2log N` from the prime term in
`T-19801.1`.

## 2. RH-equivalent inequality

Since `2log N>0`, `T-19801` gives

\[
\boxed{
\mathrm{RH}
\iff
\mathcal R(N)\le\mathcal B(N)
\text{ for every sufficiently large integer }N.}
\tag{T-19802.4}
\]

Equivalently, it is enough that the positive excess be subpolynomial:

\[
\boxed{
[\mathcal R(N)-\mathcal B(N)]_+
 =N^{o(1)}.}
\tag{T-19802.5}
\]

Indeed multiplication by `2log N=N^{o(1)}` does not alter a polynomial growth
exponent.

Equation (T-19802.4) is an elementary-looking Robin-type criterion: each level
contains only a finite weighted prime-power sum and explicit classical special
functions.

## 3. Exact rightmost-zero exponent

Let

\[
\Theta_\zeta
 =\sup_{\xi(\rho)=0}(\Re\rho-1/2).
\]

Combining (T-19802.3) with `L-19802` gives

\[
\boxed{
\Theta_\zeta
 =\limsup_{N\to\infty}
 \frac{
  \log\left(1+[\mathcal R(N)-\mathcal B(N)]_+\right)
 }{2\log N}.}
\tag{T-19802.6}
\]

The harmless factor `2log N` disappears from the exponent. Thus the rate by
which the finite Riesz inequality fails measures the rightmost zero's horizontal
displacement exactly.

More generally, if for every `epsilon>0`,

\[
[\mathcal R(N)-\mathcal B(N)]_+
 \le C_\varepsilon N^{2\theta+\varepsilon},
\tag{T-19802.7}
\]

then

\[
\xi(s)\ne0
\qquad(\Re s>1/2+\theta).
\tag{T-19802.8}
\]

## 4. Threshold asymptotic

Using

\[
\Phi(N^{-4},2,1/4)=16+O(N^{-4}),
\]

the terms `2/(N log N)` and `-2/(N log N)` cancel exactly. Hence

\[
\boxed{
\begin{aligned}
\mathcal B(N)={}&
 \frac{2N}{\log N}
 +\frac12(\psi(1/4)-\log\pi)\\
&+\frac{-4+\Phi(1,2,1/4)/8}{\log N}
 +O\left(\frac1{N^5\log N}\right).
\end{aligned}}
\tag{T-19802.9}
\]

The first draft of this asymptotic omitted the fixed Lerch endpoint
`Phi(1,2,1/4)/(8log N)` and retained a nonexistent `1/(Nlog N)` remainder. The
exact formula (T-19802.2) was unaffected; the displayed asymptotic has now been
corrected before use.

Keeping the exact threshold is essential for proof production: all of these
apparently lower-order terms are much larger than the final RH-scale margin at
finite `N`.

The leading term of `mathcal R(N)` is also `2N/log N`; the criterion concerns
the complete pole/gamma/trivial-zero centered remainder, not a coarse PNT main
term.

## 5. Finite certificate

A directed certificate may either evaluate `mathscr S(N)` as in `X-19801` or
evaluate the equivalent difference

\[
\mathcal B(N)-\mathcal R(N).
\]

The latter requires:

1. all prime powers through `N^2`;
2. directed intervals for the nonnegative Riesz weights;
3. the exact special-function threshold;
4. one outward interval for the final difference.

A strict positive lower endpoint certifies the RH-compatible inequality at that
level. A strict negative upper endpoint certifies an RH violation. A finite
positive ladder is not a cofinal proof.

## 6. Proof boundary

- The equivalence and exponent identity are exact algebraic consequences of the
  square-screw theorem.
- The eventual Riesz inequality is not proved.
- Standard estimates for `psi(x)-x` do not reach the required one-sided
  subpolynomial excess after centering.
- This theorem is a scalar RH criterion, not a resolution of RH.