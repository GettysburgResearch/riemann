# Maxwell-equivalent Xi current metric and a universal height-owner law

This continuation began with an immutable remote audit of PR #729. The branch
was zero commits behind its parent, and the PR summary was corrected from the
older `beta_0` boundary to the already-proved source-energy descent down to
`beta_1`.

## 1. Uniform curvature becomes a metric theorem

The strong source bound

\[
-(\log\Phi)''>{20476\over2345}
\]

controls the complete exterior-square conditional law. That law is
monotone-likelihood dominated by the Maxwell density

\[
g_\kappa(x)
={4\kappa^{3/2}\over\sqrt\pi}x^2e^{-\kappa x^2}.
\]

The Maxwell hyperbolic moment is exactly

\[
\mathbb E_g{\sinh(2HX)\over2HX}=e^{H^2/\kappa}.
\]

Hence the actual current profile satisfies

\[
e^{-H\xi-H^2/\kappa}
\le R_H(\xi)\le e^{-H\xi}.
\]

For `H<=1/2`, the lower multiplicative factor exceeds `97/100`. The canonical
exponential Paley--Wiener metric is therefore a quantitatively accurate model
of the actual current metric, not merely an upper proxy.

## 2. A boundary zero has an exact source price

For one shifted Blaschke zero at depth `y`,

\[
\operatorname{tr}_{K_B}M_{e^{-H\xi}}
={2y\over H+2y}.
\]

The actual current charge lies within three percent of this value throughout
the critical-height range. A fixed-depth anti-inner packet is paid; only a
vanishing depth collar can be source-cheap.

## 3. The topological unit reappears across scales

At one fixed height the charge tends to zero with the depth, while the degree
remains one. The correct resolution is to let the height vary. For one zero
`rho=alpha+i gamma`, put

\[
Q_\rho(H)
=2(\gamma-H)
\int_0^\infty
R_H(\xi)e^{-2(\gamma-H)\xi}d\xi.
\]

The profile decreases with both height and frequency, while the normalized
model vector shifts stochastically toward higher frequencies. Consequently

\[
Q_\rho(0)=1,
\qquad
Q_\rho(H)\downarrow0
\quad(H\uparrow\gamma).
\]

Thus

\[
d\nu_\rho=-dQ_\rho
\]

is a positive probability measure. Every Xi-prime zero owns exactly one unit
across descent heights.

## 4. The owner law is almost explicit

The exponential reference metric gives

\[
S_\gamma(H)
={2(\gamma-H)\over2\gamma-H},
\qquad
-dS_\gamma
={2\gamma\over(2\gamma-H)^2}dH.
\]

The Maxwell sandwich yields

\[
{97\over100}S_\gamma(H)
<Q_\rho(H)
\le S_\gamma(H).
\]

Therefore the actual and explicit owner laws have Kolmogorov distance below
three percent. The reference mean is

\[
2\gamma(1-\log2),
\]

and the actual mean differs by less than `0.03 gamma`.

## 5. New closure interface

The pointwise differential microscope and the integrated shell/index programme
can now be asked to consume one common positive measure:

```text
HOWNXFER105644

Identify the current-height owner law with the signed height flow of the
physical Xi-prime allpass, retaining two-trace evaluation, common-zero
confluence and the cofinal endpoint ledger.
```

This is stronger and more source-faithful than estimating raw negative Hardy
energy or trying to turn a single weighted trace into degree.

## 6. Status

```text
uniform strong log-concavity                 PROVED / REVIEW
Maxwell current-profile sandwich             PROVED / REVIEW
actual/exponential metric equivalence        PROVED TO 3%
positive one-zero owner probability          PROVED EXACT
universal owner law                          PROVED TO 3%
height-owner physical transfer               OPEN / RH-BEARING
pointwise evaluation                         OPEN / RH-BEARING
Riemann Hypothesis                           UNPROVEN
```

Replay:

```text
PASS_X_105640_STRONG_LC_DEPTH_COLLAR
checks=4223
b8d2c8770f38dbcace6a481f540d2fad1af8c01ad04fabde2ecc8167890adcf0
RH_UNPROVEN
```