# Cauchy-square / Clark / generalized-Jordan continuation

## Status

```text
branch: research/gpt56-pro/91008-cauchy-square-clark-jordan
base:   PR #394 head 82ee32348b05512514462966bfeb4e2de4ae5ecf
RH:     UNPROVED
```

This continuation attacks PR #394's sole open sign rather than adding an
unrelated criterion.

## Main advance

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

Therefore RH is equivalent to monotonicity of one natural local zero count in
the resolution parameter \(a\). A matched off-line pair makes its derivative
tend to \(-\infty\) immediately after \(a\) crosses the pair depth.

## Exact new geometry

- The Fourier transform of one line atom is
  \[
  \frac{\pi a}{2}(1+a|\xi|)e^{-a|\xi|}.
  \]
- An active reflected pair inserts the exact multiplier
  \(2\cosh(d\xi)\).
- The total mass is a zero-count projector.
- The difference between \(a^2\) times mass and the centred second moment is
  exactly \(\pi a d^2\) per reflected pair.
- Differentiation recovers PR #394's sharp depth projector.

This places the radial criterion directly inside the Zeta23
rank/signature geometry.

## Arithmetic bridge

The arithmetic part of the completed shift ratio is

\[
 \frac{\zeta(s-a)}{\zeta(s+a)}
 =
 \sum_{n\ge1}
 \frac{J_{2a}(n)}{n^{a+s}},
\]

with strictly positive generalized-Jordan coefficients. At \(a=1/2\), this is
the Euler-totient source \(\varphi(n)/\sqrt n\); at \(a=1\), it is
\(J_2(n)/n\). The exact shifted cocycle is positive.

Thus the radial/Clark route and the repository's analytic-totient/Jordan
programme are two coordinates of the same horizontal deformation.

## Honest boundary

The positive coefficient expansion lives in \(\Re s>1+a\), whereas the
Clark boundary is \(\Re s=1/2\). The missing continuation of monotonicity
across that gap is RH-bearing. Unweighted centre averages are also blind,
because they count off-line pairs positively.

No proof of RH is claimed.
