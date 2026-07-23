# Agent report — two-channel synthesis and curvature provenance correction

Agent: `gpt56-02-e`  
Issue: #39, independent parallel attempt  
Branch: `agent/gpt56-02-e/39-xi-passivity-adversarial-scan`  
Date: 2026-07-23  
Status: no counterexample; one new value-only synthesis and one withdrawn scratch result

## Why this append-only correction exists

The earlier session report accurately records the Pick and shifted-Stieltjes
precision ladders, but its two quoted no-remainder curvature negatives were not
bound to committed source and exact decimal inputs. They do not reproduce at
the stored labels. R-3901 withdraws those rows rather than silently editing the
historical report.

## New mathematical synthesis

L-3902 combines the L-3901 Stieltjes channel and the parallel L-4701
complete-Bernstein channel. From two values

```text
R_j = Re xi'/xi(1/2+x_j+iT)
```

one obtains

```text
A = (R_1/x_1 - R_2/x_2)/(x_2^2-x_1^2)
B = (x_2 R_2 - x_1 R_1)/(x_2^2-x_1^2).
```

Under RH both are nonnegative. For a same-ordinate off-line pair with
`d=delta^2`,

```text
A_pair =  2m/((u-d)(v-d))
B_pair = -2md/((u-d)(v-d))
B_pair/A_pair = -d.
```

A straddling pair makes `A` negative; a same-side pair makes `B` negative. This
supplies a paired value-only reconnaissance signature and a pole-displacement
estimator without derivatives or matrix eigenvectors.

## Reproducible curvature replacement

`nufft_curvature.py` uses one moment-corrected FFT to evaluate 65,536 exact
serialized decimal ordinates:

```text
center = 4709203636353.6309
spacing = 0.01
offsets = -327.68 .. +327.67
Taylor order = 18.
```

The high-precision center theta is reduced modulo `2*pi` before a binary64
phase is formed. The scan has zero negative samples. Its minimum is

```text
+30.742555369264693
```

at

```text
4709203636353.6409.
```

Direct reconstruction gives `+30.742489343830005`.

The raw moment Taylor bounds are small, but they are explicitly not promoted to
a final curvature enclosure when the Hardy denominator is small.

## Additional carrier controls

At the PR #44 center, the two channels at `x=1e-4,1e-3` are ordinary positive
midpoints:

```text
A ~ +73.1160957148
B ~ +30.7585109060.
```

At the complete-prime carrier `3157430112465.8695095`, adjacent offsets from
`1e-4` through `1e-2` gave

```text
A ~ +165.30 .. +165.42
B ~ +39.288 .. +39.307.
```

A `T +/- 20`, step-`0.1` no-remainder scan there contained no negative sample.

## Independent carrier-coordinate computation

A fresh reconstruction of the X-0801 stream through `c=10^8` matched the PR #44
`K=1024` leading margin to about `2e-15`:

```text
reconstructed: +0.006643091775831778
PR #44:        +0.006643091775833554.
```

A 26-point logarithmic `K=256` cutoff scan from `10^7` to `10^8` decreased
monotonically on the tested grid. The local cutoff derivative remained negative;
the frozen-vector carrier shift was about `2e-7`, with only `5e-13` quadratic
improvement. This is ordinary floating evidence, not a monotonicity proof.

## Candidate status

None. No directed negative interval or `Z-####` object exists.

## Files added or corrected

- `L-3902-two-channel-xi-pole-localizer.md`;
- `R-3901-nonreproducible-curvature-nominations.md`;
- `nufft_curvature.py` and its tests;
- `results/curvature-nufft.json`;
- corrected O-3901, README, and machine-readable carrier audit;
- this append-only report.

## Recommended next actions

1. Implement a shared Arb batch for the A/B channels.
2. Use `B<0` to estimate `delta^2`, then require a compatible straddling `A<0`.
3. Freeze the PR #44 `c=10^11` vector and run the directed complete-prime scalar
   pass against PR #51's exact `2.5e-10` correction moat.
4. Require exact-input serialization before any future anomaly is retained.
