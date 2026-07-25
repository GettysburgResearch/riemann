# X-5603 — The noise floor of a 128-bit Pick `lambda_min` screen

Agent: `opus5-01`   Issue: #55   Claim: `R-5603`

## What this measures

The `xi`-passivity route nominates candidate ordinates by computing
`lambda_min` of the `8 x 8` Pick matrix

```text
K_jk = ( F(s_j) + conj F(s_k) ) / (x_j + x_k),   s_j = 1/2 + x_j + iT,  F = xi'/xi
x    = 2^-17, 2^-15, 2^-13, 2^-11, 2^-10, 2^-9, 2^-7, 2^-5
```

from a **128-bit** midpoint matrix, and flagging ordinates where it comes out
negative.  Under RH `K` is a Gram matrix, so `lambda_min >= 0` and a certified
negative would disprove RH.

The usual way to assess such a screen is to propagate errors and quote a
condition number.  This experiment does something more direct: it computes the
true `lambda_min` to far more digits than any effect being measured, then
**simulates** `p`-bit evaluation by perturbing the eight kernel values by
independent relative errors of size `2^-p`, and measures how often the screen
then reports a negative.

That number — the **flag rate** at an ordinate whose truth is positive — is the
screen's false-positive rate, and it is the only statistic that says whether a
nomination means anything.

## Result

```text
true lambda_min   +1.2259907375435524056e-35        (positive)
condition number   1.4266243e+39                    (39.15 digits)

 p     flag rate    1-sigma spread    most negative in 300 trials
128      0.533        2.99e-33            -5.42e-33
136      0.173        1.18e-35            -8.47e-36
144      0.000        4.45e-38            +1.218e-35
160      0.000        7.03e-43            +1.226e-35
192      0.000        1.58e-52            +1.226e-35
```

**At 128 bits the screen is a coin flip.**  The signal is `244` times below the
noise, and the strongest reported nomination, `-2.626429492911995e-33`, is
`0.88` spreads from the median of pure noise — a completely typical draw.

The screen becomes informative between `136` and `144` bits.  **Screen at
`>= 160`**, and raise it further if nodes are added: the spectrum falls by about
`3.4e9` per added node, so a ninth node costs another `~32` bits.

## Why the matrix is this ill-conditioned

The bare Cauchy matrix `1/(x_j + x_k)` on these nodes has condition number of
order `10^5`; the `10^39` is not geometry.  Under RH `K` is a superposition of
rank-one Poisson kernels, one per zero, so an eight-node sample of an operator
of infinite rank has super-geometrically decaying trailing eigenvalues.  Adding
nodes makes this worse.

On top of that, `Re F` vanishes identically on the critical line by
`xi(s) = xi(1-s)`, so `Re F ~ x` as `x -> 0` and is itself a near-total
cancellation between `zeta'/zeta ~ -13.5` and the archimedean part `~ +13.52`,
against `|F| ~ 69.35`.  The part of the kernel the positivity question is about
is a small difference of large quantities before the matrix is even formed.

## Files

```text
noise_floor.py          the experiment
results/F-nodes.json    cached xi'/xi at the eight nodes (dps 60)
results/noise-floor.json  the ladder
```

## Run

```bash
python3 noise_floor.py --dps 60 --trials 300
```

About nine minutes for the eight kernel evaluations (`mpmath` `zeta` and its
derivative at height `4.7e12` cost ~58 s each), then a few minutes for the
ladder.  The kernel values are cached, so re-running the ladder is cheap.

## Boundaries

- The "true" `lambda_min` is ordinary high-precision arithmetic, **not** a
  directed interval.  Two independent audits converged on the same value to 20+
  digits, so it is not in doubt — but this is not a certified computation and
  must not be quoted as one.
- The noise model is uniform, independent, one-ulp-relative per node.  A real
  Arb implementation's errors are none of those things.  The flag rate is
  indicative; what is robust is the two-order-of-magnitude gap between noise
  scale and signal at 128 bits.
- `300` trials resolves a rate to about `+-0.03`, so "`0.000`" means "below
  `~0.01`", not "impossible".
- One ordinate.  That the same holds at the other fourteen nominated ordinates
  is an inference from the shared node ladder, not a measurement.
