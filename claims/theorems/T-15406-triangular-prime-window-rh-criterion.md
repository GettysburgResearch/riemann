# T-15406 — One finite triangular prime-power window is equivalent to RH

Claim ID: `T-15406`  
Title: A three-piece linear weight gives pointwise, mean-square, and Laplace-Hardy criteria for RH  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: `L-15409`; the smoothed von Mangoldt explicit formula; elementary Laplace theory  
Scope: positive route through one exact finite prime-power statistic  
Related counterexample candidates: none

## Statistic

Let `h=log 4` and let `G_h` be the finite triangular signed window of
`L-15409`. Define

\[
 Q_h(x)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 G_h(x-\log n).
 \tag{T-15406.1}
\]

Only prime powers in

\[
 e^{x-3h}\le n\le e^x
 \tag{T-15406.2}
\]

occur.

## Main equivalence

The following are equivalent.

1. The Riemann Hypothesis is true.
2. There are `x_0,C` such that
   \[
    \boxed{|Q_h(x)|\le C\qquad(x\ge x_0).}
    \tag{T-15406.3}
   \]
3. There are `x_0,C` such that
   \[
    \boxed{
    \sup_{X\ge1}\frac1X
    \int_{x_0}^{x_0+X}|Q_h(x)|^2dx\le C.}
    \tag{T-15406.4}
   \]
4. The Abel--Hardy quantity
   \[
   \boxed{
   \sup_{\sigma>0}
   \frac{\sigma}{2\pi}
   \int_{-\infty}^{\infty}
   \left|
   \widehat G_{h,L}(\sigma+it)
   \frac{\zeta'}{\zeta}
    \left(\frac12+\sigma+it\right)
   \right|^2dt<\infty}
   \tag{T-15406.5}
   \]
   after removal of one fixed compact initial interval.

The compact initial interval changes every criterion by only a finite constant.

## RH implies boundedness

Under RH, the shifted nontrivial zeros are `i gamma`. The smoothed explicit
formula gives

\[
 Q_h(x)=
 -\sum_\rho m_\rho e^{i\gamma x}
  \widehat G_{h,L}(i\gamma)
 +E_h^{\rm triv}(x),
 \tag{T-15406.6}
\]

where coincident zeros are grouped by multiplicity and the trivial/endpoint
term is bounded and eventually exponentially decaying.

By `L-15409`,

\[
 |\widehat G_{h,L}(it)|=O_h((1+|t|)^{-2}).
\]

Together with the standard unit-interval zero-count bound this implies

\[
 \sum_\rho m_\rho
 |\widehat G_{h,L}(i\gamma)|<\infty.
 \tag{T-15406.7}
\]

Thus the series in (T-15406.6) converges absolutely and uniformly. This proves
(T-15406.3), hence (T-15406.4).

## Mean square implies holomorphy

Set

\[
 f(t)=|Q_h(x_0+t)|^2,
 \qquad
 F(T)=\int_0^Tf(t)dt.
\]

If (T-15406.4) holds, then `F(T)<=CT`. Integration by parts gives, for every
`sigma>0`,

\[
 \int_0^\infty e^{-2\sigma t}f(t)dt
 =2\sigma\int_0^\infty e^{-2\sigma t}F(t)dt
 \le\frac{C}{2\sigma}.
 \tag{T-15406.8}
\]

Cauchy--Schwarz therefore proves absolute convergence of the Laplace transform
of `Q_h` throughout `Re z>0`.

For `Re z>1/2`, direct termwise integration gives

\[
 \mathcal LQ_h(z)=
 -\widehat G_{h,L}(z)
 \frac{\zeta'}{\zeta}\left(z+\frac12\right).
 \tag{T-15406.9}
\]

The left side extends holomorphically to `Re z>0`. The factor
`widehat G_(h,L)` cancels the zeta pole at `z=1/2` and is nonzero throughout
`0<Re z<1/2`. Hence the logarithmic derivative has no pole there. There is no
zero with real part greater than `1/2`; the functional equation proves RH.

This proves (3) implies (1). The implication (2) implies (3) is immediate.

## Abel--Cesaro equivalence

For any nonnegative locally integrable `f`, define

\[
 C_f=\sup_{X\ge1}\frac1X\int_0^Xf(t)dt,
 \qquad
 A_f=\sup_{\sigma>0}
 \sigma\int_0^\infty e^{-2\sigma t}f(t)dt.
\]

The preceding integration gives

\[
 A_f\le\frac12C_f.
 \tag{T-15406.10}
\]

Conversely, for `sigma=1/X`,

\[
 \frac1X\int_0^Xf(t)dt
 \le e^2\sigma
 \int_0^\infty e^{-2\sigma t}f(t)dt,
 \tag{T-15406.11}
\]

so

\[
 C_f\le e^2A_f.
 \tag{T-15406.12}
\]

Laplace Plancherel applied to (T-15406.9) proves the equivalence of
(T-15406.4) and (T-15406.5).

## Boundary variance under RH

Under RH, the Abel quantity has the finite boundary limit

\[
 \boxed{
 \lim_{\sigma\downarrow0}
 \frac{\sigma}{2\pi}
 \int_{\mathbb R}
 \left|
 \widehat G_{h,L}(\sigma+it)
 \frac{\zeta'}{\zeta}
  \left(\frac12+\sigma+it\right)
 \right|^2dt
 =\sum_{\gamma>0}m_\gamma^2
  |\widehat G_{h,L}(i\gamma)|^2.}
 \tag{T-15406.13}
\]

The right side is one half of the Bohr mean square of `Q_h`. Locally near a
boundary pole, the integral contributes `pi m_gamma^2 |Ghat(i gamma)|^2/sigma`;
absolute summability justifies summing the residues and taking the limit.

Equation (T-15406.13) supplies a precise positive target: prove the uniform
weighted Hardy estimate (T-15406.5) directly from primes.

## Why this is a genuine simplification, not a solution

The infinite-convolution window in `T-15404` made the explicit formula rapidly
convergent but introduced an infinite evaluator. The triangular window keeps all
logical sensitivity and reduces the producer to three linear pieces.

However, (T-15406.5) is still critical. A pole at

\[
 z=\rho-1/2,
 \qquad\operatorname{Re}\rho>1/2,
\]

forces its left side to blow up as the vertical line approaches that pole. Any
proof of the uniform estimate is therefore already a proof of RH.

## Gap audit

- The explicit formula must be reconstructed with the exact convention for
  trivial zeros and endpoint terms.
- The triangular breakpoints require half-open conventions, although the window
  itself is continuous.
- Laplace Plancherel is applied after discarding a finite initial segment and
  extending by zero.
- The boundary-limit formula groups equal zero ordinates before squaring.
- A bound for `sigma>=sigma_0>0` is not cofinal and does not prove RH.
- This theorem identifies a finite exact target; it does not establish the
  target estimate.
