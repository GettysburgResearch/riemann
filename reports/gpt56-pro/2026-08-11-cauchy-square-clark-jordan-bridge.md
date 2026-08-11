# Cauchy-square / Clark / generalized-Jordan continuation

## Status

```text
branch: research/gpt56-pro/91008-cauchy-square-clark-jordan
base:   PR #394 head 82ee32348b05512514462966bfeb4e2de4ae5ecf
RH:     UNPROVED
```

This continuation attacks PR #394's sole open sign rather than adding an
unrelated criterion.

## Main advance: one Cauchy-square soft count

The radial curvature is the derivative of

\[
 \mathcal N_x(a)
 =
 \frac12\left[
 a\Re\frac{\xi'}{\xi}(1/2+a+ix)
 -
 a^2\partial_a
 \Re\frac{\xi'}{\xi}(1/2+a+ix)
 \right].
\]

Under RH this is the squared-Cauchy soft count

\[
 \sum_\gamma m_\gamma
 \left[
 \frac{a^2}{a^2+(\gamma-x)^2}
 \right]^2.
\]

Thus RH is equivalent to monotonicity of a natural local zero count. A matched
off-line pair makes its derivative tend to \(-\infty\) immediately after the
resolution crosses the pair depth.

## Stronger production target: one dyadic gate

Differential monotonicity is unnecessary. The fixed-dilation theorem

\[
 \boxed{
 \mathcal N_x(2a)\ge\mathcal N_x(a)
 \quad(x\in\mathbb R,\ a>0)
 }
\]

is already equivalent to RH. Under false RH, at an ordinate carrying an
off-line zero, choose the maximal horizontal depth \(y\). Then
\(\mathcal N_x(a)\to+\infty\) as \(a\downarrow y\) from the right, while
\(\mathcal N_x(2a)\) remains bounded because there is no deeper same-ordinate
zero at depth \(2y\).

On the critical line the dyadic increment factors exactly as two rational
squares:

\[
 \mathcal n_{2a}(u)-\mathcal n_a(u)
 =|g_{1,a}(u)|^2+|g_{2,a}(u)|^2,
\]

\[
 g_{1,a}(u)=
 {2\sqrt6\,a^3u\over(a^2+u^2)(4a^2+u^2)},
 \qquad
 g_{2,a}(u)=
 {\sqrt{15}\,a^2u^2\over(a^2+u^2)(4a^2+u^2)}.
\]

This is the preferred review and production theorem: a fixed two-channel
Hermitian inequality rather than a continuum of derivatives.

## Exact Fourier and depth geometry

- A line atom has Fourier transform
  \[
  \frac{\pi a}{2}(1+a|\xi|)e^{-a|\xi|}.
  \]
- An active reflected pair inserts the multiplier \(2\cosh(d\xi)\).
- The total mass is a zero-count projector.
- The difference between \(a^2\) times mass and the centred second moment is
  exactly \(\pi a d^2\) per reflected pair.
- Differentiation recovers PR #394's sharp depth projector.

This places the radial criterion directly inside the Zeta23 rank/signature
geometry.

## Clark interpretation

The completed shift ratio

\[
 \Theta_a(s)=\frac{\xi(s-a)}{\xi(s+a)}
\]

is unimodular on the critical boundary. Under RH its boundary phase is a sum of
Poisson kernels all having the same horizontal width \(a\). An off-line pair
splits one width into \(a-d\) and \(a+d\), exactly producing the failed
monotonicity.

## Arithmetic bridge and positive cocycle

The arithmetic shift ratio is

\[
 \frac{\zeta(s-a)}{\zeta(s+a)}
 =
 \sum_{n\ge1}\frac{J_{2a}(n)}{n^{a+s}},
\]

with strictly positive generalized-Jordan coefficients.

The normalized sieve flow

\[
 Q_a(s)=\frac{\zeta(s)}{\zeta(s+2a)}
 =\sum_{n\ge1}\frac{q_a(n)}{n^s},
 \qquad
 q_a(n)=\prod_{p\mid n}(1-p^{-2a}),
\]

obeys

\[
 Q_{a+b}(s)=Q_a(s)Q_b(s+2a)
\]

with coefficientwise positive convolution. At \(a=1/2\),
\(q_a(n)=\varphi(n)/n\); the unnormalized source is
\(\varphi(n)/\sqrt n\). Thus the dyadic Clark gate and the repository's
analytic-totient/Jordan programme are the same horizontal deformation.

## Honest boundary

The positive Euler expansions live in their absolute half-planes, whereas the
Clark boundary is \(\Re s=1/2\). The missing continuation of the two-channel
Hermitian inequality across that gap is RH-bearing. Unweighted centre averages
are also blind, because they count off-line pairs positively.

The exact remaining theorem is the **Dyadic Cauchy-Square Gate**. No proof of
RH is claimed.
