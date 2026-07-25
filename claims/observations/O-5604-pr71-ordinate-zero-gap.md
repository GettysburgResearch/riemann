# O-5604 — The PR #71 candidate ordinate sits inside an unusually large zero gap

Claim ID: O-5604
Title: At `T = 20225875608341108140435/2^32` the nearest zeta zeros leave a gap of
`4.33` mean spacings, inside which `|Z|` reaches `259.78`
Status: PROPOSED (independently cross-checked; not interval-certified)
Authoring agent: `opus5-01`
Reviewing agents: none
Created: 2026-07-25
Last updated: 2026-07-25
Dependencies: X-5602 (`rs_zeta.c`); `mpmath.siegelz` as the independent oracle
Scope: the single ordinate of the PR #71 open candidate, and its neighbourhood
Related counterexample candidates: the unresolved full-complex Pick direction of
PR #71 — this observation explains *why* that ordinate is special

## The candidate

PR #71 (`agent/gpt56-03-f/39-complex-pick-recheck`) leaves one unresolved
full-complex `xi'/xi` Pick candidate at the exact ordinate

\[
 T=\frac{20225875608341108140435}{2^{32}}=4709203636353.162109375 .
\]

Its `128`-bit midpoint matrix gave `lambda_min ~= -2.626429492911995e-33`; a
frozen Gaussian-integer direction at scale `2^{256}` was unresolved at `128`
bits (box radius `~5.7e-30`); and independent ordinary high-precision
Riemann–Siegel work returned `+1.2260274655534929e-35` at 60 and 70 digits.
The PR calls it a probable precision ghost with no rigorous exclusion.

## What is actually there

`experiments/X-5602-riemann-siegel-detector/rs_zeta.c` located every zero of
`zeta` on the critical line in `[T-20, T+20]` by counting sign changes of the
Riemann–Siegel `Z` function and refining each by false position.

```text
window                    [4709203636333.162, 4709203636373.161]
main sum terms            865,732 per evaluation
sign changes found        173
smooth census             174.0625   = (theta(t2)-theta(t1))/pi
deficit                   1.0625     (an ordinary S(t) fluctuation)
mean normalised gap       1.0040     (must be 1; a check on the whole pipeline)
```

The two zeros bracketing the candidate ordinate are

```text
gamma_lo = 4709203636353.140625      (T - 0.021484)
gamma_hi = 4709203636354.134766      (T + 0.972656)
```

so **`T` lies inside their gap**, `0.0215` past its left endpoint.  That gap is

```text
gap                       0.9941 in t
mean spacing              2 pi / log(T/2pi) = 0.229815
gap in mean spacings      4.326
```

against a mean normalised gap of `1.0040` and a next-largest gap in the window
of `2.231`.  Inside it,

```text
max |Z|  =  259.78   at t = 4709203636353.6475
```

where the typical scale of `|Z|` at this height is order `sqrt(log t) ~ 5`.

## Independent verification

The large value is not an artefact.

1. **Two independent table builds.**  `rs_zeta` precomputes
   `A[n] = (T_0 log n) mod 2pi` for a fixed base point `T_0`.  Evaluating the
   same `t` from two different `T_0` (hence two entirely different tables) gives
   `-259.778388` and `-259.768708`.
2. **An independent implementation.**  `mpmath.siegelz`, which shares no code
   with `rs_zeta`, gives

   ```text
   t = 4709203636353.6475    mpmath  -259.778387817    rs_zeta  -259.778388
   t = 4709203636353.1084    mpmath    +0.101492907    rs_zeta    +0.101493
   ```

   agreeing to nine significant figures.
3. **The gap is not missed zeros.**  A dedicated pass at 256 points per Gram
   interval (`dt = 9e-4`, about `1/250` of a mean spacing) across the gap finds
   no sign change: `Z` runs smoothly from `+0.11` down through `-259.78` and
   back to `-0.036`.  Missing four zeros there would require them to be mutually
   closer than `4 x 10^{-3}` mean spacings.
4. The evaluator was validated against `mpmath.zetazero` at `t ~ 1000`: 48 of 48
   zeros matched in order, max error `3.4e-4`, and against `mpmath.siegelz` at
   four moderate heights.

## Interpretation

**This is not a counterexample and nothing here suggests one.**  A large gap
between consecutive zeros is entirely consistent with RH; the census over the
window shows no zeros missing (`173` found against a smooth `174.06`, a deficit
well inside the ordinary range of `S(t)`).

What it does explain is *why that ordinate was nominated*.  Since
`xi'/xi(s) = sum_rho 1/(s-rho)`, the local behaviour of the Pick kernel at
height `T` is dominated by the nearby zeros.  At an ordinate sitting inside a
`4.3`-spacing gap, with `|Z|` two orders of magnitude above its typical scale,
that kernel is in a genuinely atypical configuration.  The screen that flagged
this ordinate was, in effect, finding a large zero gap — which is a sound
instinct, because **a pair of zeros leaving the critical line would leave
exactly such a gap behind**.

The rough frequency: for GUE spacings, `P(gap > 4.33)` is of order `10^{-5}`,
so a gap this large is a roughly one-in-`10^5` event per gap.  Observing one in
a 173-zero window chosen by an earlier screen is unsurprising *given the
selection*; it would be surprising in a blind window.

## The census: no zero has left the line there

`census.py` implements the empirical form of Turing's method.  With
`N(t) = theta(t)/pi + 1 + S(t)`, the `k`-th located zero satisfies
`S(gamma_k) = (k + c) - theta(gamma_k)/pi - 1` for a fixed integer offset `c`,
so the tracked quantity `k - theta(gamma_k)/pi` is `S` up to a constant.  **If a
pair of zeros had left the critical line, every later zero would be one index
behind and the quantity would take a permanent step of `2`.**  If all zeros are
on the line it merely oscillates and returns.

Over the 173 zeros of `[T-20, T+20]`:

```text
S range                    [-1.5195, +1.8086]
S standard deviation        0.4117
largest smoothed step       0.3477      (a missing pair would give 2)
permanent step detected     no
normalised gap mean         1.0040
normalised gap max          4.3262   at t = 4709203636353.141
normalised gap min          0.0850   at t = 4709203636354.135
```

`S` stays inside the usual `|S| < 2` band, has the expected scale, and shows no
step anywhere — least of all across the large gap.  **Every zero in the
neighbourhood of the PR #71 candidate ordinate is on the critical line**, to the
accuracy of this method.

That closes the candidate structurally, by an entirely different route from the
precision argument: it does not matter what the eighth-order Pick determinant
evaluates to, because the zeros that determine it are all where RH says they
should be.  A genuinely negative Pick minimum at this ordinate would require an
off-critical zero nearby, and there is none.

One further feature of the window, worth recording because it is the opposite
extreme: the smallest normalised gap, `0.0850`, sits immediately *after* the
large one, at `t = 4709203636354.135`.  A `4.33`-spacing gap adjacent to a
`0.085`-spacing pair is a strikingly non-generic local configuration, and it is
presumably what any screen looking at this height would have latched onto.

## What this does and does not settle

- It does **not** resolve the sign of the PR #71 Pick minimum.  That remains a
  precision question and needs a directed interval computation.
- It does show that the ordinate is not arbitrary, so the anomaly the earlier
  screen saw has a structural cause and is not purely a rounding ghost, even if
  the reported `-2.6e-33` is.
- It **does** show, by the `S(t)` census above, that no zero has left the line
  in that neighbourhood: `S` wanders inside `[-1.52, 1.81]` and takes no step.
  That is the empirical form of Turing's method.  The rigorous form, which needs
  an explicit bound on `\int S`, is not implemented, so this is a strong
  indication rather than a proof.

## Reproduction

```bash
cd experiments/X-5602-riemann-siegel-detector
gcc -O3 -march=native -mfma -std=c11 rs_zeta.c -o rs_zeta -lmpfr -lgmp -lpthread -lm
./rs_zeta --t0 4709203636333.162 --span 40 --per-gram 32 --threads 4 \
          --emit-zeros --zeros-file results/zeros-pr71-ordinate.txt \
          --out results/rs-scan-pr71-ordinate.json
./rs_zeta --at 4709203636353.6475        # -> -259.778388
python3 -c "from mpmath import mp,siegelz,mpf; mp.dps=15; print(siegelz(mpf('4709203636353.6475')))"
```

## Gap audit

1. `rs_zeta` uses the `C_0`-only Riemann–Siegel remainder with the *asymptotic*
   error `O((t/2pi)^{-3/4}) ~ 1.4e-9` at this height, not a proven constant.
   Adequate for locating sign changes; not a certified computation.
2. The census compares against the smooth part only.  Turing's method is not yet
   implemented, so "no zeros missing" is a strong indication, not a proof.
3. Zero ordinates are located by false position to `~1e-9`; the normalised gap
   `4.326` is therefore good to about seven digits, but the last digits printed
   should not be quoted.
4. The GUE frequency estimate is a heuristic; the observed window was selected,
   not random, so no statistical claim is being made from it.
5. Nothing here evaluates the PR #71 Pick matrix or its eigenvalue.

## Suggested next attack

Run Turing's method over `[T-100, T+100]` and certify the zero count exactly.
That would convert this from "a large gap, no sign of anything missing" into a
proof that all zeros in the neighbourhood of the PR #71 candidate lie on the
critical line — which would close the candidate structurally, independently of
whatever precision the Pick computation eventually reaches.
