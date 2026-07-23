# X-3901 — Adversarial xi-passivity scan at optimized carrier basins

Experiment ID: `X-3901`  
Issue: #39, independent parallel attempt  
Agent: `gpt56-02-e`  
Status: ordinary high-precision reconnaissance plus exact rational kernel tests  
Created: 2026-07-23

## Question

Do the unusually low finite-Weil carrier basins near

```text
4709203636353.65
3157430112465.87
```

also exhibit scalar, value-only secant, differential, sampled-Pick, or
shifted-Stieltjes failures for `F=xi'/xi`?

A genuine off-line zero would create compact finite witnesses. This experiment
attempts to distinguish those signals from high-phase input errors,
Riemann--Siegel remainder effects, cancellation in small-offset jets, and nearly
singular matrix arithmetic.

## Exact kernels

### L-3901 barycentric product form

`barycentric.py` implements L-3901 with `Fraction` arithmetic. For distinct
positive offsets `x_i`,

```text
c_i = 1 / product_{j != i} (x_i-x_j).
```

Under RH its Pick quadratic form is

```text
sum_gamma 1 / product_i (x_i^2 + (T-gamma)^2) >= 0.
```

For a same-ordinate off-line pair at displacement `delta`, its contribution is

```text
2 / product_i (x_i^2-delta^2).
```

### L-3902 two-channel detector

The same two values `R_j=Re F(1/2+x_j+iT)` give

```text
A = (R_1/x_1 - R_2/x_2)/(x_2^2-x_1^2)
B = (x_2 R_2 - x_1 R_1)/(x_2^2-x_1^2).
```

RH implies `A>=0` and `B>=0`. For a pole pair with `d=delta^2`,

```text
B_pair/A_pair = -d.
```

A straddling pair has `A_pair<0`; a same-side pair has `B_pair<0`. A negative
same-side channel can therefore estimate the horizontal displacement, after
which a straddling channel supplies an independent second nomination.

## Numerical layers

- `xi_jets.py` assembles simultaneous Riemann--Siegel zeta derivatives through
  order four and converts them to `F` derivatives and low Stieltjes moments.
- `nufft_curvature.py` builds three logarithmic Hardy moments once and evaluates
  a deterministic exact-decimal ordinate grid by a moment-corrected FFT.
- Fast no-remainder curvature remains nomination-only.
- Every matrix nomination is replaced by a fixed exact vector before precision
  escalation.
- The final proof path requires directed complex balls and independent
  reproduction.

## Results

Neither carrier produced a surviving negative.

At the optimized PR #44 center:

- scalar `Re F`: positive on the tested offset ladder;
- L-3902 channels at `x=1e-4,1e-3`: approximately `A=+73.1161`, `B=+30.7585`;
- differential localizer: positive;
- `2 x 2` Hankel and localizing matrices: positive after sufficient precision;
- eight-point Pick/barycentric negative midpoints: precision artifacts that
  stabilize positive.

At the second carrier, adjacent L-3902 channels on offsets through `1e-2`
remained approximately `A=+165.30..+165.42` and `B=+39.288..+39.307`.

## Curvature provenance correction

The first draft quoted two negative no-remainder curvature values that were not
bound to a frozen exact-input program. They do not reproduce at the stored
decimal labels and are withdrawn by R-3901.

The replacement scan is serialized in `results/curvature-nufft.json`:

```text
center:  4709203636353.6309
spacing: 0.01
points:  65536
window:  -327.68 .. +327.67
negative samples: 0
minimum: +30.742555369264693
```

Direct reconstruction at the minimum decimal ordinate gives
`+30.742489343830005`.

## Reproduce

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python -m compileall -q barycentric.py xi_jets.py nufft_curvature.py tests
python nufft_curvature.py \
  --center 4709203636353.6309 \
  --spacing 0.01 --points 65536 --order 18 \
  --output /tmp/curvature-nufft.json
```

The barycentric tests use exact standard-library arithmetic. The Riemann--Siegel
and FFT controls require mpmath and NumPy.

## Proof boundary

- Exact rational barycentric/two-channel identities: algebraic tests.
- Riemann-xi point values and FFT grid: ordinary arithmetic, not intervals.
- Raw NUFFT Taylor bounds do not enclose a final curvature quotient near small
  Hardy values.
- No negative directed sign exists.
- No `Z-####` candidate is created.

## Suggested next search

Use a value-only Arb batch that returns both L-3902 channels and their shared
uncertainty moat. Require a negative same-side `B` plus a compatible negative
straddling `A` before escalating a high-height basin to multi-point or jet
certification. Separately, freeze the PR #44 carrier vector and perform the
directed complete-prime scalar pass against PR #51's exact correction gate.