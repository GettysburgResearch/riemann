# Finite scout for the compact beta boundary field

Status: **bounded floating-point experiment through `Y=2^18`; no asymptotic,
RH, or GRH inference**

Replay:
[`ffps_boundary_field_finite_scout.py`](ffps_boundary_field_finite_scout.py).
Canonical summary:
[`ffps_boundary_field_finite_scout.json`](ffps_boundary_field_finite_scout.json).

Read the exact theorem first:
`FFPS_MOLLIFIED_BETA_BOUNDARY_SHELL_IDENTITY.md`. This scout evaluates its
compact boundary field `G`; it does not supply any part of that proof.

## 0. Outcome

The box-free primitive detector has even cleaner finite near-logarithmic
behavior than the mollified density which led to it. On the fine mesh:

| `Y` | negative mass of `G` | absolute mass of `G` | signed mass |
|---:|---:|---:|---:|
| `2^10` | `60.661` | `122.349` | `1.028` |
| `2^14` | `80.520` | `161.465` | `0.425` |
| `2^18` | `102.449` | `203.051` | `-1.848` |

Over the finite window `2^10,...,2^18`, least squares gives

\[
 \int_0^{\log Y}(G(t))_-dt
 \approx5.143\log_2Y+9.061,
\]

and

\[
 \int_0^{\log Y}|G(t)|dt
 \approx10.159\log_2Y+19.754.
\]

The maximum residuals are only `1.019` and `1.007`. The exact theorem says
that subpower negative mass of `G` is equivalent to RH. These rows do **not**
prove that bound, estimate an asymptotic constant, or constitute evidence for
RH. They nominate the much sharper finite-data conjecture

\[
 \int_0^{\log Y}|G(t)|dt=O(\log Y)
\]

for structural investigation. Even a polylogarithmic theorem here would be
RH-strength, so the conjecture must not be treated as an approachable routine
estimate.

## 1. What is evaluated

The exact boundary packet defines

\[
 G(t)=\sum_{n\ge1}{\beta(n)\over\sqrt n}
 K_{\rm bd}(t-\log n),
\]

where

\[
 K_{\rm bd}
 =(1-\tau_L)^2(1-\sqrt2\tau_L)^2
 1_{t\ge0}(13+3t-8e^{t/2}),
 \qquad L=\log2.
\]

The finite differences make this kernel compact in `[0,4L]`. Causality means
the source truncation at `n<=Y` is exact at every displayed horizon apart
from the inherited nearest-log-node placement. The producer imports the
independently audited beta sieve, snapped-source convention, dyadic
coefficients, and linear FFT convolution from the preceding finite scout,
and content-checks that current imported implementation against its frozen
git blob.

No zeta zero, finite field, curve, conductor family, or L-function family is
enumerated.

## 2. Exact identities used as numerical controls

At the same midpoint resolution, the exact first-difference theorem gives

\[
 h_{L/2}={G-\tau_{L/2}G\over L/2}.
\]

The array formed from this difference agrees with a separate direct
convolution by the mollified kernel to maximum absolute error
`2.13e-13`, or relative error `1.05e-15`, at the full fine panel. This is a
floating-point implementation control, not an independent proof of the
identity.

The ordinary Jordan identity gives, at every horizon,

\[
 \int|G|=2\int G_-+\int G.
\]

The JSON records both the signed mass and the independently formed residual
`absolute-2*negative`; they agree to the published precision. The small
signed column explains the nearly `2:1` masses without suggesting that either
Jordan side is small asymptotically.

## 3. Resolution and comparison with the mollified scout

The two panels use `256` and `512` cells per doubling. Their maximum relative
mass difference across all thirteen horizons is `0.002535`. At the largest
horizon the negative masses are `102.470` and `102.449`.

The earlier mollified density had finite-window slopes about `19.325` and
`38.380` per doubling. Integrating once to `G` reduces those visible slopes
to about `5.143` and `10.159`. That comparison is descriptive. The exact
first-difference identity explains why differentiation can amplify local
oscillation, but it does not force either fitted slope or its stability.

## 4. Replay and resource cap

```text
python -B research/l-families/atlas/function_field/ffps_boundary_field_finite_scout.py --check
python -B -O research/l-families/atlas/function_field/ffps_boundary_field_finite_scout.py --check
python -B -m unittest tests.test_ffps_boundary_field_finite_scout
python -B -O -m unittest tests.test_ffps_boundary_field_finite_scout
```

The producer makes three source-building passes, each using indices only
through `262,144`, for at most `786,432` source-placement-loop visits. The
fine pass has `9,216` source-grid cells; the direct control has `2,304`
kernel-grid cells and `11,519` linear-convolution cells. The maximum FFT
length is `16,384`. The replay runs three boundary convolutions and one
direct mollified-kernel control, and completes in a few seconds. It performs
no broad arithmetic search.
