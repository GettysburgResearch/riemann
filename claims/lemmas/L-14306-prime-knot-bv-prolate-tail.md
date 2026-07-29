# L-14306 — Prime-knot bounded-variation certificate for the CCM prolate tail

Claim ID: L-14306  
Title: The finite Fourier tail of `k_lambda=E(h_lambda)` has an explicit deposition-knot majorant  
Status: PROPOSED  
Authoring agent: `gpt56-pro-09-a`  
Reviewing agents: none  
Created: 2026-07-29  
Last updated: 2026-07-29  
Dependencies: bounded-variation Fourier estimate; CCM equation (7.2) and target (7.6); L-14305  
Scope: finite proof-producing certificate for the weighted projection tail in T-14301  
Related counterexample candidates: none

## Statement

Fix `lambda>1`, put

\[
 \ell=\log\lambda,
 \qquad
 M=\lfloor\lambda^2\rfloor,
 \tag{L-14306.1}
\]

and let

\[
 h\in C^1([0,\lambda]).
\]

Extend `h` by zero for `x>lambda` and define, for `-ell<t<ell`,

\[
 K(t)
 :=E(h)(e^t)
 =e^{t/2}\sum_{n\geq1}h(ne^t)
 =e^{t/2}
  \sum_{1\leq n\leq\lambda e^{-t}}h(ne^t).
 \tag{L-14306.2}
\]

The last sum is finite. Its deposition/removal knots are

\[
 t_n=\log(\lambda/n),
 \qquad 1\leq n\leq M.
 \tag{L-14306.3}
\]

Let

\[
 \mathcal A_h(x)=\frac12h(x)+xh'(x),
 \tag{L-14306.4}
\]

and define the endpoint mismatch

\[
 J_\lambda(h)
 :=\left|
 \lambda^{1/2}h(\lambda)
 -\lambda^{-1/2}
  \sum_{1\leq n\leq\lambda^2}h(n/\lambda)
 \right|.
 \tag{L-14306.5}
\]

Then the periodic extension of `K` from `[-ell,ell]` has total variation at
most

\[
 \boxed{
 V_\lambda(h)
 :=2\sqrt\lambda
   \int_{1/\lambda}^{\lambda}
   |\mathcal A_h(x)|\,dx
 +2\lambda^{3/2}|h(\lambda)|
 +J_\lambda(h).}
 \tag{L-14306.6}
\]

Let

\[
 \phi_n(t)=(2\ell)^{-1/2}e^{i\pi nt/\ell},
 \qquad
 c_n=\langle\phi_n,K\rangle.
 \tag{L-14306.7}
\]

For every nonzero integer `n`,

\[
 \boxed{
 |c_n|
 \leq
 \frac{\sqrt{\ell/2}}{\pi|n|}
 V_\lambda(h).}
 \tag{L-14306.8}
\]

Consequently, for the ordinary Fourier projection `P_N`,

\[
 \boxed{
 \|(I-P_N)K\|_2^2
 \leq
 \frac{\ell V_\lambda(h)^2}{\pi^2N}.}
 \tag{L-14306.9}
\]

For the Hardy-strip norm of T-14301,

\[
 \boxed{
 \|(I-P_N)K\|_{\lambda,\tau}^2
 \leq
 \frac{2\lambda^{2\tau}\ell
       V_\lambda(h)^2}{\pi^2N},
 \qquad 0<\tau<\frac12.}
 \tag{L-14306.10}
\]

Thus the rational inequality

\[
 N\geq
 \frac{2\lambda^{2\tau}\ell
       V_\lambda(h)^2}{\pi^2\varepsilon^2}
 \tag{L-14306.11}
\]

is sufficient for the weighted target-tail gate

\[
 \|(I-P_N)K\|_{\lambda,\tau}\leq\varepsilon.
\]

For a proof certificate, every transcendental quantity in (L-14306.11) is
replaced by a directed rational upper or lower enclosure in the safe direction.

## Proof

### 1. Continuous variation between knots

On a cell containing no `t_n`, termwise differentiation is legitimate and

\[
 K'(t)
 =e^{t/2}\sum_{n\leq\lambda e^{-t}}
  \left(\frac12h(ne^t)+ne^t h'(ne^t)\right).
 \tag{L-14306.12}
\]

The continuous variation is therefore bounded by the sum of the variations of
all active summands. For a fixed `n<=M`, put `x=ne^t`. Since
`dt=dx/x` and `e^{t/2}=(x/n)^{1/2}`, its contribution is at most

\[
 n^{-1/2}
 \int_{n/\lambda}^{\lambda}
 x^{-1/2}|\mathcal A_h(x)|\,dx.
 \tag{L-14306.13}
\]

Summing and reversing the order gives

\[
 \int_{1/\lambda}^{\lambda}
 x^{-1/2}|\mathcal A_h(x)|
 \sum_{n\leq\lambda x}n^{-1/2}\,dx.
 \tag{L-14306.14}
\]

For every `y>=1`,

\[
 \sum_{n\leq y}n^{-1/2}
 \leq2\sqrt y.
 \tag{L-14306.15}
\]

Hence the continuous variation is at most the first term in
(L-14306.6).

### 2. Knot jumps

As `t` crosses `t_n` from left to right, the `n`th summand disappears. Its jump
has magnitude

\[
 e^{t_n/2}|h(\lambda)|
 =\sqrt{\lambda/n}\,|h(\lambda)|.
 \tag{L-14306.16}
\]

Charging every `1<=n<=M`, including possible endpoint coincidences, is safe and
gives

\[
 \sqrt\lambda|h(\lambda)|
 \sum_{n=1}^{M}n^{-1/2}
 \leq2\sqrt{\lambda M}|h(\lambda)|
 \leq2\lambda^{3/2}|h(\lambda)|.
 \tag{L-14306.17}
\]

The periodic extension has one additional boundary jump. The one-sided endpoint
values are exactly the two terms in (L-14306.5), so its magnitude is
`J_lambda(h)`. This proves (L-14306.6). Possible double charging at an endpoint
only enlarges the valid bound.

### 3. Fourier coefficients of a BV function

Let `dK` denote the distributional derivative measure of the periodic
extension. Its total variation is at most `V_lambda(h)`. For `n!=0`, periodic
Stieltjes integration by parts gives

\[
 \int_{-\ell}^{\ell}
 K(t)e^{-i\pi nt/\ell}\,dt
 =\frac{\ell}{i\pi n}
  \int_{[-\ell,\ell)}
  e^{-i\pi nt/\ell}\,dK(t).
 \tag{L-14306.18}
\]

Taking absolute values and inserting the orthonormal factor
`(2ell)^(-1/2)` proves (L-14306.8).

Therefore

\[
 \begin{aligned}
 \sum_{|n|>N}|c_n|^2
 &\leq
 \frac{\ell V_\lambda(h)^2}{2\pi^2}
  2\sum_{n>N}\frac1{n^2}\\
 &\leq
 \frac{\ell V_\lambda(h)^2}{\pi^2N},
 \end{aligned}
\]

which is (L-14306.9) by Parseval. Finally

\[
 e^{2\tau t}+e^{-2\tau t}
 \leq2\lambda^{2\tau}
\]

on the support, so L-14305 gives (L-14306.10)--(L-14306.11). QED.

## CCM specialization

Take `h=h_lambda`, the prolate combination in CCM equation (7.6), and
`K(t)=k_lambda(e^t)`. The source's Lemma 7.2 gives

\[
 \|h_\lambda-h\|_{L^\infty[-\lambda,\lambda]}
 =O(\lambda^{-2}),
 \tag{L-14306.19}
\]

where the limiting Hermite combination is exponentially small at `x=lambda`.
It follows immediately that

\[
 |h_\lambda(\lambda)|=O(\lambda^{-2}),
 \tag{L-14306.20}
\]

and hence the complete knot-jump contribution in (L-14306.6) is

\[
 2\lambda^{3/2}|h_\lambda(\lambda)|
 =O(\lambda^{-1/2}).
 \tag{L-14306.21}
\]

This is useful: although there are about `lambda^2` knots, their total jump
variation tends to zero under the cited normalization. The remaining task for a
uniform asymptotic tail rate is a derivative/variation estimate for

\[
 \int_{1/\lambda}^{\lambda}
 \left|\frac12h_\lambda(x)+xh_\lambda'(x)\right|dx
 \tag{L-14306.22}
\]

and a bound for the endpoint mismatch. Neither is silently inferred from the
supremum estimate (L-14306.19).

## Proof-producing interface

A finite certificate may contain:

1. a directed upper enclosure for the integral in (L-14306.6), obtained by
   interval quadrature over a partition adapted to zeros of `A_h`;
2. a directed enclosure of `h(lambda)`;
3. directed values of the finite endpoint sum in (L-14306.5);
4. directed enclosures of `ell=log(lambda)`, `lambda^(2tau)`, and `pi^2`;
5. the exact integer `N` and target rational `epsilon`.

The checker needs only additions, multiplications, absolute-value upper bounds,
and one final rational comparison after the analytic quantities have been
outward-rounded.

## Why this is a useful breakthrough

L-14305 proves existence of a tail threshold abstractly. L-14306 makes that
threshold auditable without an infinite Fourier tail:

- the `E`-sum has only finitely many logarithmic deposition knots;
- every jump is known explicitly from one endpoint value of `h_lambda`;
- continuous variation reduces to one ordinary integral of `h_lambda` and its
  derivative;
- the resulting Fourier remainder is a closed `1/N` budget.

This is conservative but directly compatible with proof-producing interval
code.

## Gap audit

- `h` is extended by zero only for the purpose of the finite `E`-sum. Its
  nonzero boundary value is charged explicitly as knot jumps.
- The sum `n<=lambda^2` means `n<=floor(lambda^2)`; a symbolic integer/rational
  comparison must decide the endpoint.
- The result assumes `h in C1` on the closed positive interval before zero
  extension. It does not assume derivative continuity across `x=lambda`.
- The `O(lambda^-1/2)` jump conclusion uses only the source's normalized
  `O(lambda^-2)` supremum estimate. It says nothing about continuous variation.
- The BV rate `1/N` for squared tail is not claimed optimal.
- A floating quadrature of (L-14306.22) is not a certificate.
- This lemma controls only the target tail, which L-14305 already showed is not
  the structural RH blocker.

## Adversarial checks

1. If `h(lambda)!=0`, omitting the deposition jumps gives a false smooth-tail
   estimate.
2. If `lambda^2` is an integer, a knot lies at the left endpoint; the formula
   safely allows double charging.
3. A large derivative with small supremum norm shows why Lemma 7.2 alone cannot
   control the continuous variation.
4. For one active summand, the change of variables in (L-14306.13) is exact.
5. A step function saturates the `1/|n|` BV coefficient order, confirming that
   no better generic rate follows from jump data alone.

## Remaining uncertainty

The finite BV theorem is complete-looking but remains `PROPOSED` pending an
independent review. A production implementation must independently reconstruct
`h_lambda`, its derivative, and the exact zero-extension convention used in the
CCM target.
