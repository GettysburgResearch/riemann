```text
Claim ID:       O-0002
Title:          The zeta zeros appear as spectral lines in the primes:
                a cross-validation, and an all-heights screen
Status:         EMPIRICAL
Authoring agent: claude-01
Reviewing agents: (none yet)
Created:        2026-07-25
Last updated:   2026-07-25
Dependencies:   explicit formula for psi (unconditional); X-0005
Scope:          sieve limit X <= 4 * 10^7, ordinates gamma <= 60
Related counterexample candidates: Z-0004
```

## Statement (what was measured)

Let `f(u) = (psi(e^u) - e^u) / e^{u/2}` and let

```
A(g) = (2/W) | INT_{u0}^{u1} f(u) e^{-i g u} du | ,      W = u1 - u0 .
```

Computed from a prime sieve alone (no evaluation of `zeta` anywhere in the
computation), with `u0 = log 1000`, `u1 = log X`:

| `X` | resolution `2pi/W` | top peaks (in order) |
|---|---|---|
| `10^6` | 0.91 | 14.12, 21.04, 25.02, 32.88, 30.54, 40.94, 37.66, 43.24, 47.84, 49.86, 52.94, 59.44 |
| `4*10^7` | 0.59 | 14.140, 21.020, 25.000, 30.420, 32.940, 37.640, 40.900, 43.300, 47.980, 49.880, 56.380, 53.000 |

These are the first twelve nontrivial zero ordinates.  Measured amplitudes
agree with the predicted `2/|rho|` to within about 10% (e.g. `A = 0.1447` at
`gamma = 14.140`, predicted `0.1414`), and the peak positions move **toward**
the true ordinates as `X` grows, as they must.

## Why this is worth a claim ID

**As a cross-check.**  The zero ordinates were obtained independently in
X-0001/X-0004 by certified sign changes of the Hardy function — analytic
machinery, Euler-Maclaurin, ball arithmetic.  X-0005 shares *no code and no
mathematics* with that: it is a sieve and a Fourier sum, and it never evaluates
`zeta`.  Two disjoint computations landing on the same twelve numbers, with the
right amplitudes, is the strongest evidence available here that neither is
systematically wrong.  Given that this session found two real bugs in the
analytic stack (R-0001, R-0002), an independent confirmation of that stack is
not a formality.

**As a search.**  Every certified method in this repository costs more as the
height rises; `L-0004` is `O(T^2)`.  This screen's cost is *independent of the
height of the zero it is looking for* — one sieve and one transform examine
every `gamma` in the resolvable band at once.  By the explicit formula a zero
with `Re rho = 1/2 + delta` contributes a component of amplitude growing like
`X^delta`, so:

* an **extra** peak not matching a known ordinate, or
* a peak whose amplitude **grows** as `X` increases,

is exactly the signature of a counterexample.  Neither was seen.

## Measured sensitivity — and a correction to the paragraph above

Per M-0003 the screen was then run against a planted off-critical zero
(`X-0005b`, `validate.py`).  The result is much less flattering than the
cross-validation, and it supersedes any impression that this screen is a strong
detector:

```
growth of a line's amplitude between X1 = 10^6 and X2 = 4*10^7 is (X2/X1)^delta
on-line baseline scatter (should be 1.000):  0.85 .. 1.12   =>  scatter 0.15
planted delta = 0.2   ratio 1.61   DETECTED (> 3x scatter)
planted delta = 0.1   ratio 1.26   not detected
planted delta = 0.05  ratio 1.15   not detected
planted delta <= 0.02 ratio ~1.09  not detected
=> sensitivity floor: delta >= 0.2
```

**The screen cannot currently see a displacement below `delta ~ 0.2`.**  That
is far worse than the certified tools: L-0004's count-matching has *no*
displacement floor at all (any off-line pair changes an integer by 2), and
T-0001 reaches `delta ~ 0.1` at modest effort.  The scatter is dominated by
spectral leakage from the rectangular window and by the fact that changing `X`
changes the window as well as the data, so the two amplitudes being compared
are not measured under the same conditions.

Applying the same test to the **real** sieve data gives implied displacements
for the first thirteen zeros between `-0.045` and `+0.031`, all consistent with
zero — but given a floor of `0.2` this is a statement about the screen's
resolution, not a bound on the zeros.  It should not be quoted as one.

## Fixing it: paired equal-length windows (X-0005c)

The diagnosis above says the comparison was badly designed, not that the idea
is bad: transforming over `[u0, log X1]` and `[u0, log X2]` compares two
windows of *different length*, so resolution and leakage change along with the
data.  Replacing that with **two equal-length sub-windows of a single sieve**,
one early and one late, plus a Hann taper:

```
                                   old design      paired windows
sensitivity floor (planted zero)   delta >= 0.2    delta >= 0.1
ratio at planted delta = 0.2       1.61            2.886  (predicted 2.885)
ratio at planted delta = 0.1       1.26            1.697  (predicted 1.699)
ratio at planted delta = 0.05      1.15            1.299  (predicted 1.303)
ratio at planted delta = 0.01      1.09            1.047  (predicted 1.054)
```

The estimator is now essentially **unbiased** — measured ratios agree with
`e^{delta D}` to three digits at every planted displacement, including ones far
below the detection floor.  So the floor is set entirely by the *scatter* among
on-line lines, not by any systematic error in the estimator.

## Where the residual scatter actually comes from

Not leakage.  **Line blending.**  Splitting the twelve on-line lines by their
nearest-neighbour distance against the Hann resolution (`2.372` at
`X = 4 * 10^7`):

```
well-separated lines (10 of 12):   scatter 0.0389   ->  delta floor 0.022
blended (gamma = 48.005, 49.774,
 separation 1.769 < resolution):   scatter 0.1682   ->  sets the global floor
```

The two lines that ruin the average are exactly the closest pair in the range,
and they are also exactly the two whose implied displacements looked largest in
the real data (`+0.022`, `+0.031`, against `<= 0.006` for the well-separated
lines).  So:

* for a **well-separated** ordinate the screen already resolves
  `delta ~ 0.02` — an order of magnitude better than the first measurement;
* the global floor of `0.1` is a statement about *close pairs*, and close pairs
  are precisely the Lehmer-pair configurations this project most wants to
  examine.  That is an unfortunate coincidence and it is the crux of Q-0010.

## The fix, implemented (X-0005d)

Blending is only a resolution limit when the line positions are unknown, and
they are not: X-0001/X-0004 supply certified ordinates.  Replacing peak-reading
with a joint least-squares fit of

```
f(u) = c + sum_j [ a_j cos(gamma_j u) + b_j sin(gamma_j u) ],   gamma_j fixed
```

over each window, and taking `A_j = sqrt(a_j^2 + b_j^2)`:

```
                              periodogram   paired windows   joint fit
baseline scatter (synthetic)    0.1494         0.1682         4.9e-15
sensitivity floor (planted)     0.2            0.1            <= 0.0005
```

The scatter falls to machine precision and the measured growth ratios track
`e^{delta D}` to five digits at every planted displacement down to `0.0005`,
where I stopped testing.  Blending is gone.

**Read that number carefully.**  The synthetic test feeds the estimator data
generated by *exactly* the model it fits — same twenty zeros, no noise — so
`0.0005` is a floor for the **estimator**, and its real content is negative
information: the estimator is no longer the limiting factor.  It is *not* the
screen's floor on real data.

On the real sieve the implied displacements now spread over `+/- 0.019`
(`gamma = 56.45` is the extreme), against `+/- 0.006` for well-separated lines
in the previous design.  That residual is **model mismatch**, not blending:
zeros above the modelled band, the neglected `-log(2 pi)` and
`-(1/2) log(1 - x^-2)` terms of the explicit formula, and a window short enough
that the tail of the zero sum matters.  So the honest current statement is:

* estimator floor: `<= 0.0005` (measured, synthetic);
* **real-data floor: `~ 0.02`, set entirely by what is left out of the model.**

Two of those omissions were then tested directly:

```
adding the e^{-u/2} column (the -log(2 pi) term of the explicit formula):
    max |implied delta|  0.01857 -> 0.01754
widening the modelled band (X = 4*10^7, window fixed):
    20 lines  (to gamma = 77)   0.01872
    60 lines  (to gamma = 163)  0.01421
   120 lines  (to gamma = 270)  0.01307
```

Both help, and both saturate.  So the remaining `~0.013` is **not** the
unmodelled band and **not** the non-zero terms: it is the window length itself
— the estimator has genuine variance over a window of only `5.3` in `u`, and
the tail of the zero sum does not average out over so short a stretch.

**That is the finding.**  Three plausible culprits were each measured and two
were eliminated, which leaves a single lever — a longer window, i.e. a larger
sieve — but now for a diagnosed reason rather than as a guess.  Window length
grows like `log X`, so the residual falls slowly; the honest expectation is a
real-data floor of a few times `10^-3` at `X ~ 10^{12}`, not `10^-5`.

For orientation: L-0004's deficit test has *no* displacement floor at all, so
this screen will never compete with it on sensitivity.  Its distinct value is
that its cost does not grow with the height of the target — it is the only tool
here that can look at `gamma ~ 200` for the same price as `gamma ~ 20`.

**Conclusion, revised twice.**  The screen's demonstrated value is (i) the
cross-validation of two disjoint code paths, which is real, and (ii) an
all-heights probe with a *measured* floor of `delta ~ 0.02` on isolated
ordinates and `~0.1` where lines blend.  That is no longer negligible, but it
is still far behind L-0004's exact deficit test, and it certifies nothing.
The arc — measure, find the floor unusable, redesign, re-measure, diagnose the
residual, name the next fix — is the intended use of M-0003.

## Gap audit

* **Nothing here is certified.**  Floating-point sieve, floating-point
  transform, truncated window.  Per README rule 2 this output is not evidence
  in the proof sense.  A lead must be converted into a rectangle and handed to
  L-0002 / T-0001.
* **Sidelobes masquerade as peaks.**  A rectangular window of length `W` has
  sidelobes at `~1.4 * 2pi/W` from each line.  The single "unexplained" peak in
  the top 14 at each `X` (`gamma = 12.84` at `X = 10^6`) sits at exactly that
  distance from the dominant 14.13 line and is a sidelobe, not a discovery.
  **Any future claim of an unexplained peak must first apply a window
  (Hann/Kaiser) and re-check.**  This is the single most likely way for this
  screen to produce a false alarm, and it will produce one eventually.
* **Amplitude comparison is crude.**  The 10% agreement conflates window
  leakage, the finite `u0` cutoff, and the neglected `-log(2pi)` and
  `-(1/2)log(1-x^-2)` terms.  It is a sanity check, not a measurement.
* **Resolution limits reach.**  Zeros are spaced `~2pi/log(gamma/2pi)`, which
  falls below the window resolution `2pi/W = 2pi/log(X/1000)` once
  `gamma` is large; beyond that, lines blur together.  At `X = 4*10^7` the
  usable band is roughly `gamma <= 60`.  Reaching `gamma ~ 10^3` needs
  `X ~ 10^{40}` — **this screen cannot be pushed to arbitrary heights by
  brute force**, and that limitation should temper the "all heights at once"
  claim above: it is all heights *in the resolvable band*, and the band grows
  only logarithmically in `X`.
* **`psi` vs `theta`**: `psi` was used deliberately, so no `sqrt(x)` term from
  prime squares contaminates the normalisation.
* No error bars, no significance test.  A real screen needs a null model
  (what does the largest spurious peak look like?) before "unexplained" means
  anything.  Not done: this is the first thing to build (Q-0010).

## Adversarial tests

* **Convergence.**  Peak positions must approach the true ordinates as `X`
  grows.  They do: `14.12 -> 14.140` (true `14.1347`), `30.54 -> 30.420`
  (true `30.4249`).  A screen whose peaks *drifted* would be broken.
* **Amplitude law.**  Peaks should scale like `2/|rho|`, i.e. decay like
  `1/gamma`.  They do.
* NOT YET DONE, and both are cheap and important: (i) a planted-zero synthetic
  test — build a synthetic `psi` from a zero set containing an off-line zero
  and confirm the growing-amplitude signature is visible; (ii) a null model for
  the spurious-peak distribution.  Until (i) is done, the *sensitivity* of this
  screen to a real counterexample is unknown, exactly the gap M-0003 exists to
  prevent.

## Suggested next attack

1. Windowing (Hann) + a null model, so that "unexplained peak" is a
   quantitative statement.  Without this the screen cannot produce a usable
   lead.
2. Segmented sieve to `10^9`-`10^{11}`, tracking each known peak's amplitude as
   a function of `X`.  A zero at `1/2 + delta` shows up as a *trend*, and a
   trend is far easier to see than an absolute anomaly.
3. The planted-zero validation of M-0003.
