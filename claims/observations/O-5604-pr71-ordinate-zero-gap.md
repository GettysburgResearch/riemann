# O-5604 — The PR #71 candidate ordinate sits inside an unusually large zero gap

Claim ID: O-5604
Title: At `T = 20225875608341108140435/2^32` the nearest zeta zeros leave a gap of
`4.33` mean spacings, inside which `|Z|` reaches `259.78`
Status: PROPOSED (independently cross-checked; not interval-certified)
Authoring agent: `opus5-01`
Reviewing agents: none
Created: 2026-07-25
Last updated: 2026-07-25
Dependencies: X-5602 (`rs_zeta.c`, `census.py`, `turing.py`, `tau_localise.py`);
`mpmath.siegelz` as the independent oracle; an external bound on `\int S`
(Turing/Trudgian) which is **not** proved in this repository
Scope: the single ordinate of the PR #71 open candidate, and its neighbourhood
Related counterexample candidates: the unresolved full-complex Pick direction of
PR #71 — this observation explains *why* that ordinate is special

## The candidate

PR #71 (`agent/gpt56-03-f/39-complex-pick-recheck`) leaves one unresolved
full-complex `xi'/xi` Pick candidate at the exact ordinate

\[
 T=\frac{20225875608341108140435}{2^{32}}=4709203636353.16214999998919665813446044921875 .
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
gamma_lo = 4709203636353.1406744        (T - 0.0214756)
gamma_hi = 4709203636354.1345482        (T + 0.9723982)
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

## Turing's method proper: the ordinate is excluded

The census above is the *empirical* form.  `turing.py` and `tau_localise.py`
implement the real argument, which needs one imported ingredient: an explicit
bound `|\int_{t_1}^{t_2} S| \le B(t_2)`.  Two are used, and the conclusion is the
same under both:

```text
B conservative   3 + 0.1 log t2   = 5.9181     (deliberately weaker than anything published)
B Trudgian       2.067 + 0.059 log t2 = 3.7887 (the literature value, for reference)
```

Write `c = N(t_1)` for the unknown integer count below the window, and suppose
`k` off-line ordinates `\tau_j` sit inside it (an off-line zero contributes to
`N` but produces **no sign change of `Z`**, which is exactly why it is invisible
to the census).  Then

\[
 \int_{t_1}^{t}S \;=\; D_c(t)+M(t),\qquad
 D_c(t)=c\,(t-t_1)+\!\!\sum_{\gamma_i\le t}\!(t-\gamma_i)-\!\int_{t_1}^{t}\!\Big(\tfrac{\theta}{\pi}+1\Big),
\]
\[
 M(t)=\mathrm{mult}\cdot\!\!\sum_{\tau_j\le t}\!(t-\tau_j)\;\ge 0 .
\]

`M` is convex, non-decreasing, vanishes at `t_1`, and — the load-bearing point —
**its slope is quantised** in units of `mult` (`= 2`, the conservative choice for
a `T-5602` quadruple).  A slope of `1` is simply unavailable.  Requiring
`|D_c+M| \le B` throughout the window is then a finite feasibility problem, and
enumerating it over `c \in c_{\rm est}+[-3,3]` gives:

```text
c offset   max D      min D       verdict
  +3     +120.47      +0.14      excluded: D exceeds +B for any M >= 0
  +2      +80.47      +0.11      excluded: D exceeds +B
  +1      +40.47      +0.07      excluded: D exceeds +B
   0       +1.21      -0.37      CONSISTENT WITH NO OFF-LINE ZEROS
  -1       +0.01     -39.53      excluded: no admissible M (slope quantised)
  -2       -0.03     -79.53      admissible, but only with off-line zeros
  -3       -0.06    -119.53      excluded: no admissible M (slope quantised)
```

Only `c` offsets `0` and `-2` survive.  The `-1` and `-3` exclusions are the
quantisation at work: `D` falls with slope `1` and `3`, and no sum of slope-`2`
ramps tracks either without leaving the corridor.

Two candidates surviving would normally be the end of a Turing argument, and one
would wave at "edge effects".  Instead `tau_localise.py` asks the sharp question:
**for each surviving `c`, at which ordinates `\tau` could an off-line zero
actually be placed?**  On a `800`-point `\tau` grid across the window, allowing a
second helper ordinate anywhere:

```text
                              admissible tau offsets (window is [0, 39.998])
B = 5.9181  c offset  0       [37.298, 39.998]     55 points, and clean (k=0) is admissible
            c offset -2       [ 0.000, 39.998]    161 points, none within 5 of the target
B = 3.7887  c offset  0       [38.348, 39.998]     34 points, clean admissible
            c offset -2       [ 0.000, 39.998]     99 points, none within 5 of the target

target ordinate offset        20.000109375
admissible tau within +-5 of the target, under ANY surviving c, under EITHER bound:   NONE
```

The `-2` alternative is the familiar boundary degeneracy: `D` falls with slope
exactly `2`, which a single off-line pair at `\tau \approx 0` — i.e. sitting on
the left endpoint — compensates exactly, `M(t) = 2t`.  It is a statement about
where the window was cut, not about its interior.  In neither surviving
alternative can an off-line zero be placed anywhere near `t = T`.

**Conclusion.** Conditional on the imported bound on `\int S` and on the
correctness of the `Z` evaluation, there is **no off-line zero at or near the
PR #71 candidate ordinate**.  The `c`-offset-`0` branch further certifies the
window clean up to `t = 4709203636370.437`, i.e. `93.2%` of it, with any
hypothetical off-line zero forced into the last `2.7` units at the right edge —
`17` units past the candidate.

- It does **not** resolve the sign of the PR #71 Pick minimum.  That remains a
  precision question and needs a directed interval computation.
- It does show that the ordinate is not arbitrary, so the anomaly the earlier
  screen saw has a structural cause and is not purely a rounding ghost, even if
  the reported `-2.6e-33` is.
- It **does** show, by the `S(t)` census above, that no zero has left the line
  in that neighbourhood: `S` wanders inside `[-1.52, 1.81]` and takes no step.
  That is the empirical form of Turing's method.
- The rigorous form is now implemented too, and it reaches the same verdict by a
  route that does not assume zeros are visible: under either the conservative or
  the Trudgian bound on `\int S`, **no admissible off-line configuration places a
  zero within `5` units of the candidate ordinate**, and the window is certified
  clean over its first `93.2%`.  This is conditional on an imported bound and on
  an uncertified `Z` evaluation, so it is a conditional certificate, not a
  proof — but the conditioning is on standard literature, not on the pipeline
  being audited.

## Reproduction

```bash
cd experiments/X-5602-riemann-siegel-detector
gcc -O3 -march=native -mfma -std=c11 rs_zeta.c -o rs_zeta -lmpfr -lgmp -lpthread -lm
./rs_zeta --t0 4709203636333.162 --span 40 --per-gram 32 --threads 4 \
          --emit-zeros --zeros-file results/zeros-pr71-ordinate.txt \
          --out results/rs-scan-pr71-ordinate.json
./rs_zeta --at 4709203636353.6475        # -> -259.778388
python3 -c "from mpmath import mp,siegelz,mpf; mp.dps=15; print(siegelz(mpf('4709203636353.6475')))"

python3 turing.py results/zeros-pr71-ordinate.txt \
    --t1 4709203636333.162 --t2 4709203636373.16 --out results/turing-pr71.json
python3 tau_localise.py results/zeros-pr71-ordinate.txt \
    --t1 4709203636333.162 --t2 4709203636373.16 \
    --target 4709203636353.16214999998919665813446044921875 --out results/tau-localise-pr71.json
```

## Gap audit

1. `rs_zeta` uses the `C_0`-only Riemann–Siegel remainder with the *asymptotic*
   error `O((t/2pi)^{-3/4}) ~ 1.4e-9` at this height, not a proven constant.
   Adequate for locating sign changes; not a certified computation.
2. The Turing conclusion is **conditional on an external bound** on `\int S`
   which this repository does not prove.  It is stated for two constants, the
   weaker of which is chosen to be looser than any published value; substituting
   a proved constant only strengthens it.  Independently, the `Z` values feeding
   it are ordinary floating computations, so the located sign changes are not
   themselves certified — a missed sign change would invalidate the census that
   the argument is built on.  This is a conditional certificate, not a proof.
3. Zero ordinates are located by false position to `~1e-9`; the normalised gap
   `4.326` is therefore good to about seven digits, but the last digits printed
   should not be quoted.
4. The GUE frequency estimate is a heuristic; the observed window was selected,
   not random, so no statistical claim is being made from it.
5. Nothing here evaluates the PR #71 Pick matrix or its eigenvalue.

## Suggested next attack

The remaining softness is not the Turing argument but its input: the sign
changes are located with ordinary doubles and a `C_0`-only remainder.  Replacing
`rs_zeta`'s inner loop with an interval evaluation of `Z` — enough to *certify*
each sign change rather than merely observe it — would remove gap-audit item 1
and reduce the whole conclusion to the single imported bound on `\int S`.  That
is a self-contained and worthwhile piece of work, and it would make X-5602 a
certified zero-counting detector rather than a fast one.

## Correction (2026-07-25, later): two provenance defects, both confirmed

An external adversarial review found two real defects in the numbers above.  I
verified both and they are correct.

**1. The decimal expansion of the ordinate was wrong.**  The fraction quoted was
always right, but its decimal expansion above was `float(T)`, not `T`:

```text
exact   20225875608341108140435/2^32 = 4709203636353.16214999998919665813446044921875
what was printed here                = 4709203636353.162109375   (= the nearest binary64)
difference                           = 174483/2^32 = 4.0625e-5
```

`T` is dyadic with denominator `2^{32}`, and binary64 near `4.7\times10^{12}`
has `ulp = 2^{-10}`, so `T` needs 22 more bits than binary64 carries.  Fixed
above.  Nothing downstream changes: `4\times10^{-5}` is three orders below the
`0.0215` distance to the lower zero.

**2. The emitted zero ordinates carried `~10^{-3}`, not `~10^{-9}`.**
`rs_zeta.c` wrote each root as `fprintf(zf, "%.17g", t0 + zeros[i])`.  Both
`t0` and the offset are exact binary64, but their *sum* is rounded to one ulp at
`t0`, which is `2^{-10} = 9.77\times10^{-4}`.  All the accuracy of the
false-position refinement lived in the offset and was discarded at
serialization.  Gap-audit item 3 below, which claimed `~10^{-9}` and "seven
digits", was wrong for that reason.

The fix forms `t0 + s` in MPFR at 160 bits — exact, since both summands are
binary64 — and prints 30 digits.  Re-running the bracketing pair gives

```text
gamma_hi = 4709203636354.13454818841463145
```

against an independent `mpmath` reconstruction of `4709203636354.1345477436`:
agreement to nine significant figures, where before there were three.

**What this does and does not change.**  The gap is real and its size stands:
`0.9939 \pm 0.002` even at the old granularity, or `4.325` mean spacings, so
"`4.326`" was right to three digits rather than seven.  No conclusion in this
file depended on the discarded digits.  The one place it could have mattered is
`turing.py`, which reads the emitted ordinates: `D(c,t)` sums `173` terms each
carrying up to `5\times10^{-4}`, so a worst-case `0.087` against a bound of
`5.92` and a clean branch spanning `[-0.37, +1.21]` — no verdict moves.  For the
`1000`-unit `t = 10^{13}` window of `O-5607` the worst case is larger (`4467`
terms, `2.2`) though the realised error is `~0.02` since the rounding is
effectively random; that claim should be re-run against the fixed emitter before
its `99.7%` figure is quoted again.
