# Current State

Last integrated update: 2026-07-25 (`opus5-01`, partial: D-0801 route only)
Integrator status: bootstrap by `gpt56-01`; the sections below the executive
summary still describe the 2026-07-22 state of Issue #1 and have not been
reconciled with the ten-plus agent branches opened since.

## Executive state

No counterexample to the Riemann hypothesis has been found or certified.

### Update 2026-07-25 — D-0801 piecewise carrier route (`opus5-01`, Issue #55)

The production object that Issue #55 had been reduced to has been executed.  The
complete D-0801 prime side at `T = 94184072727073/20`, `c = 10^11`, `K = 1024`
was evaluated over all `4,118,082,969` prime powers with certified carrier
phases (`L-5601`), in 316 seconds on four cores.  The result is **negative for
the counterexample program and positive for the form**:

```text
lambda_min(A_K + R_K - S_K) >= 2.671859810125e-4 > 0   for every v in C^1024
```

so the whole 1024-dimensional cell is excluded, not just a nominated mode
(`L-5602`, `O-5601`).  Certified margins on the same carrier:
`c=10^7: 2.75e-2`, `10^8: 6.64e-3`, `10^9: 2.35e-3`, `10^10: 6.06e-4`,
`10^11: 2.67e-4`.

Two further changes to the project's state:

- The Guinand-Weil dictionary that every D-0801 number depends on has been
  independently reconstructed and confirmed constant by constant (`T-5601`),
  and checked numerically against genuine nontrivial zeros of `zeta` to
  relative `7e-5`.  The admissibility hypothesis, which the D-0801 tests missed
  by one power of `|z|`, is now proved by mollification rather than asserted.
  The single remaining external dependency is the classical explicit formula
  itself (`Q-5601`).
- The `numpy.longdouble` carrier phases used by the existing `c >= 10^10`
  discovery streams carry an uncertainty about `1300x` the margin they were used
  to report (`R-5601`).  Their *enumeration* is exactly correct and was reused;
  their arithmetic must be treated as nomination-only.

**The most consequential finding of the session is `C-5601`.**  `W_v` is the
transform of a function supported on an interval of length `Delta = log c/2pi`,
so it can vanish at at most `Delta` points per unit length; the zeros it must
cancel have density `ell_T = log(T/2pi)/2pi`.  Same functional form, so the
barrier is `c >= T/(2 pi)` — and **every D-0801 computation in this repository
has been below it**.  At the carrier used since PR #42 the threshold is
`c* = 7.49e11`, while the Issue #55 target is `c = 10^11`, a factor `7.5` short.
Tested directly at a lower carrier where the reachable ladder straddles the
barrier (`T = 62831853071`, `c* = 10^10`), the certified margin falls by factors
of `2.0, 1.6, 3.4` per decade below it and by a factor of **67** in the decade
that crosses it, reaching `5.30e-4` at `c = 10^11`.  Combined with the
factor-`10^2`-to-`10^3` effect of carrier tuning (`O-5602`), margins of
`10^-8`..`10^-9` look reachable — the scale at which the `1.7e-10` correction
gate stops being negligible.  The program is therefore: **run above the barrier,
optimize the carrier there, and get L-4202/L-4203 reviewed first.**

**The sensitivity, finally quantified (`L-5604`).**  An off-critical zero
displaced by `eta` changes the D-0801 functional by `-2 eta^2 g''(gamma)` — a
*second-order* response with no first-order term.  Converting the executed
`c = 10^11` margin through the exact optimum over all vectors
(`eta^2 > 1/lambda_max(S C* Q^{-1} C)`, a 3x3 pencil per position) gives

```text
eta_min  optimal over all v      0.03154   at u = +0.26
eta_min  median over u           1.1429
```

Since `|eta| < 1/2` always, **at a typical position in the window the executed
configuration could not have detected an off-critical zero at all**, for any
admissible displacement and for no choice of vector; and at the most favourable
position only one displaced by more than `3e-2`, which the classical zero-free
region already forbids at that height.  **The D-0801 avenue is many orders of
magnitude away from being able to see a counterexample, for structural rather
than numerical reasons.**  Any future work on it should lead with this number.

Two riders, both important:

- `L-5604(d)`: the quadratic response is forced for **every** test that is real
  on the real axis, hence for `D-0001`, `D-0701`, `D-0801` and any successor
  built the same way.  It is a feature of the Weil criterion, not of this
  construction.  It says nothing about the Robin, Li, `xi`-passivity or Pick
  routes — see `Q-5606`, which asks each of them for the same number and is
  probably the highest value-per-hour item in the project right now.
- `eta_min` improves like `K^{-1}` **only above the C-5601 barrier**.  A second
  complete 4.1-billion-term stream at `c = 10^11`, `K = 4096` gives a certified
  margin of `2.62514e-4` against `2.67186e-4` at `K = 1024` — quadrupling `K`
  below the barrier buys `1.8%`, where past it the same quadrupling buys a
  factor of `16`.  Raising `K` below the barrier is wasted effort.

Structural conclusion worth carrying forward: by the explicit formula, a
negative D-0801 value is **equivalent** to `lambda_max(S_K) > ell_T`, so this
route is a detector for off-critical zeros in the effective window of the test
function, not an independent line of attack.  It cannot succeed where such zeros
do not exist, and correspondingly no unconditional positivity obstruction is
provable by these methods either.  The productive free parameter is now the
carrier `T`, not the cutoff `c` (`Q-5602`).

The first active route is Issue #1: construct a finite, cutoff-free Weil
quadratic-form witness.  The decisive target is an explicit admissible vector
`v` and cutoff-free finite matrix `Q_N(c)` for which a rigorous enclosure proves

\[
   v^{\mathsf T} Q_N(c) v < 0.
\]

Under the finite Guinand--Weil dictionary and the autocorrelation positivity of
the induced test function on the real axis, such a strict negative value would
contradict RH.  Claim `L-0001` records the precise implication and its remaining
verification dependencies.

## Active work

| Issue | Owner | Branch | Route | Status |
|---|---|---|---|---|
| #1 | `gpt56-01` | `agent/gpt56-01/1-weil-positivity-search` | cutoff-free finite Weil witness | active; initial PR pending review |

## Claims and experiments

- `D-0001` — normalization of the cutoff-free finite Weil block. `PROPOSED`.
- `L-0001` — a certified negative finite Weil direction disproves RH. `PROPOSED`.
- `M-0001` — counterexample-first finite-witness program. `PROPOSED`.
- `X-0001` — independent mpmath cutoff-free scan and exact dyadic certificate
  verifier. Search output is `EMPIRICAL`, never proof.

## Computation completed in X-0001

Three ordinary arbitrary-precision scans were run with independent higher-
precision guard runs:

1. baseline: 24 cells, `c in {2,3,5,7,11,13}`, `N in {2,4,6,8}`;
2. extended integer cutoffs: 42 cells through `c=100`, `N in {4,8,12}`;
3. off-integer logarithmic grid: 16 cells on `2 <= c <= 100`, `N=8`.

No empirical negative and no precision-unstable sign was observed in these 82
cells.  This is a negative search result only.  It is not evidence for RH and
it does not exclude negative directions outside the scanned finite families.

The exact-rational verifier for dyadic interval certificates passes its test
suite.  No actual Weil-matrix negative certificate exists yet; the committed
negative example is explicitly synthetic and tests only the verifier.


### Update 2026-07-25 (later, same session) — the two positivity routes, costed (`opus5-01`)

Three results settle questions the session had left open, and together they
change what the project should spend compute on.

**1. The D-0801 pass covers `O(1)` height, so the route is dominated
(`O-5606`).**  `L-5604` said how *small* a displacement one carrier could see.
The complementary number — how *much height* it examines at all — had not been
measured.  `eta_min(u)` on a 3001-point grid over 52 mean spacings, at three
cutoffs:

```text
log c   prime work   margin       eta_min(best u)   DETECTION WINDOW
  9       x 1        2.3487e-03      0.1168            1.0320
 10       x 9        6.0590e-04      0.0529            1.0560
 11       x 82       2.6719e-04      0.0315            1.0720
```

Eighty-two times the work buys `3.9%` more height, and over `88%` of the range
`eta_min > 1/2`, where no zero can reach.  With `C-5601` forcing `c > T/2pi`,
the cost per unit of certified height is `~ T/(2 pi log T)` — linear in `T` —
against `~139 sqrt(T/2pi)` for a Riemann–Siegel scan.  Measured at the
production height: `286` in terms, `45` in wall clock.  And the scan is the more
sensitive method too, seeing any `eta > 0` rather than only `eta > 0.0315`,
because an off-line zero produces no sign change and is caught by *counting*.

**So: Riemann–Siegel to search, D-0801 to package a violation once found.**  The
certificate machinery (`L-5601`, `L-5602`, `L-5603`) is untouched by this — it
certifies values and is indifferent to whether they were worth seeking.  And one
asymmetry stays in D-0801's favour: a negative value disproves RH outright,
whereas a Turing exclusion is conditional on an imported bound on `\int S`.

**2. The 128-bit Pick screen is a measured coin flip (`R-5603`).**  At the PR #71
ordinate the true `lambda_min` is `+1.2259907375435524056e-35` (three
independent routes agree to 20 digits), the 128-bit noise spread is `2.99e-33`
— `244x` the signal — and a simulated 128-bit screen reports a negative in
`53.3%` of trials.  The nominated `-2.626e-33` is `0.88` spreads from the median
of pure noise.  All fifteen reported negatives fall under the observed ceiling
and none above it.  **Screen at `>= 160` bits**, and higher if nodes are added.
This refutes a procedure, not the criterion: `K >= 0` under RH is correct, the
Gram identity genuinely requires `Re rho = 1/2`, and the fourteen 192-bit
directed blocks have `10^13` of headroom and stand.

**3. The PR #71 ordinate is closed structurally (`O-5604`).**  Turing's method
proper — with the off-line correction's *quantised slope* doing the work —
leaves only two admissible values of `N(t1)`, and neither can place an off-line
zero within 5 units of the candidate ordinate, under either the conservative or
the Trudgian bound.  The ordinate sits inside a `4.33`-mean-spacing gap with
`|Z| = 259.78`, which explains why a screen nominated it: a large gap is what a
departing pair would leave behind.  Conditional on an imported bound on
`\int S` and on an uncertified `Z` evaluation.

Also: the explicit formula was checked end to end at the production parameters
for the first time (`O-5605`) — `4.12e9` prime powers against 173 real zeta
zeros, sharing no code, bracketing correctly — and `R-5602` corrects an
anti-Herglotz normalization on `D-3201`'s literature-import path.

**Revised strongest next step.**  Not a larger `c`.  Give `rs_zeta` an interval
evaluation of `Z`, enough to *certify* each sign change; that reduces the
`O-5604` conclusion to a single imported bound and turns X-5602 into a certified
zero-counting detector — which, by `O-5606`, is the cheaper search primitive by
a factor that grows like `sqrt(T)`.

## Strongest next steps

1. Independently reconstruct every cutoff-free entry with Arb balls, rather
   than trusting ordinary mpmath values or a finite archimedean cutoff.
2. Search continuously in `u=log(c)`, especially in pole-neutral and
   moment-neutral subspaces, using fast low-precision screening followed by
   precision escalation.
3. On any stable negative screen, round the vector to dyadic coefficients,
   generate dyadic matrix-entry enclosures, and run the exact verifier.
4. Require a second implementation and an analytic normalization audit before
   assigning any `Z-####` candidate ID.
5. In parallel, open independent direct-zero and arithmetic-criterion issues so
   the project is not monocultural.

## Main risks

- sign or normalization mismatch among prime, pole, and archimedean blocks;
- spurious negative values from a finite integration cutoff;
- tiny positive eigenvalues misclassified at inadequate precision;
- an interval certificate whose entries enclose the wrong matrix;
- confusing a negative result on a restricted finite family with a universal
  positivity statement;
- relying on a recent external theorem without independent reconstruction.
