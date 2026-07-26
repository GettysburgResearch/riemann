# NEGATIVE_RESULTS.md

Failed approaches, refuted claims, and things that did not work.  Per README
rule 15 this file is as important as the positive results: it is what stops the
next agent from spending a session rediscovering a dead end.

---

## R-0001 — off-by-one in the Euler-Maclaurin Bernoulli exponent

**What happened.**  The correction term was implemented as
`N^{1-s-(2k-1)}` instead of `N^{-s-(2k-1)}`.  `zeta(2)` came out as
`1.64720566970644` instead of `1.6449340668...` — wrong in the **third**
significant digit while looking entirely plausible.

**Why it matters beyond the typo.**  The certified error bound was *correct*
and *tiny* (`~10^-15`) the whole time.  A rigorous remainder bound certifies
the truncation, not the transcription: it says "the series I summed is close to
its limit", not "I summed the right series".  Ball arithmetic cannot catch an
error in the formula being evaluated.

**Defence adopted.**  Every evaluator must pass at least one test whose
expected value is known *independently of the implementation*: exact special
values (`zeta(2) = pi^2/6`), agreement with a second library (Arb's `acb.zeta`,
a completely different algorithm), and a structural identity
(`xi(s) = xi(1-s)`).  These are in `tests/`.

---

## R-0002 — sign error in the Taylor model, invisible in values

**What happened.**  In the Taylor expansion of the `N^{1-s}` piece (L-0006) the
exponential rate was entered with the wrong sign.  The constant coefficient
`E_0` — the *value* — was unaffected, so every point-value test passed,
including comparison against the independent naive evaluator.  Only the
derivatives were wrong.

**How it was caught.**  The argument-principle moment `q_0 = (1/2 pi i) INT
eta'/eta` over a box returned `1.515 - 2.455 i`.  That number has to be a
non-negative *integer*; it wasn't, and it wasn't close to one.

**Lesson, recorded as a standing rule.**  *A derivative must be validated by a
test that is sensitive to derivatives.*  The integer-valuedness of a contour
integral is an exceptionally good such test: it is an exact structural
constraint, it is cheap, and it fails loudly and unambiguously.  Any future
change to `certzeta.eta_and_deta` or `eta_taylor_coeffs` must be re-validated
against an integer zero count.  Comparing against point values is worthless
here and gave false confidence for the better part of an hour.

---

## R-0003 — naive interval evaluation of zeta over balls is unusable

**What was tried.**  Enclosing `zeta` over a ball by evaluating the
Euler-Maclaurin sum directly in ball arithmetic.

**What happened.**  At `c = 0.2 + 14.23i` with radius `0.15`, the enclosure of
`eta = (s-1) zeta` has radius `119` while `|eta| ~ 4`.  Interval arithmetic
adds the variation of every term, but `zeta` is small precisely *because the
terms cancel*.  The enclosure is not merely loose, it contains `0`, so it
cannot even certify that `zeta` is nonvanishing on the ball — which is the one
thing every contour method needs.

**Consequence.**  Every certified contour computation over `zeta` needs
either (a) absurdly small balls, which makes the Cauchy-based quadrature
remainder explode like `rho^{-4}`, or (b) a Taylor model.  L-0006 is (b).
**Do not attempt to re-derive the naive route; it does not work at any radius
that makes the quadrature affordable.**

**Also refuted in passing:** using `xi` rather than `eta` as the contour
function.  The `Gamma(s/2+1)` factor's ball enclosure has relative width `1.44`
at radius `0.15` near `t = 14` and becomes the dominant error, while
contributing nothing — `pi^{-s/2} Gamma(s/2+1)` is zero-free, so it changes no
zero count.  Use `eta`.

---

## R-0004 — "the Robin ratio is 0.9995, so a counterexample is close" is wrong

**The tempting reading.**  X-0003 finds the Robin ratio
`sigma(n)/(e^gamma n log log n) = 0.99949...` at a colossally abundant `n` with
11541 digits: within `5 * 10^-4` of a counterexample.  It is very tempting to
conclude that a modest further search will settle RH.

**Why that is wrong.**  Under RH the Robin ratio tends to `1` from below along
the colossally abundant numbers; approaching `1` is the *predicted* behaviour,
not a warning sign.  The margin closes like a power of `1/log n`, so "within
`5 * 10^-4`" corresponds to a further search of superexponential length, and the
closeness carries no information about whether the limit is ever exceeded.

**What does carry information** is the *rate*: O-0001 shows the Nicolas margin
decays like `(log N)^{Theta - 1}`, so the exponent, not the value, is the
observable coupled to `Theta = sup Re rho`.  Measured `b = -0.512, -0.515,
-0.511` at `p_k = 2*10^4, 2*10^5, 2*10^6` — consistent with `Theta = 1/2`, and
note that the three values do **not** move monotonically toward `-1/2`, so the
spread is fit noise and no trend should be read into it.

**Recorded because** this is exactly the kind of "suspicious value" that
README rule 13 warns about, and the first agent to see `0.9995` will feel what
this agent felt.

---

## R-0005 — what the certified ranges do NOT say

X-0001 proves: every zero of `zeta` with `0 < t <= 1000` lies on the critical
line and is simple, and there is no zero with `|Re(s) - 1/2| >= 0.01` and
`0 <= t <= 500`.  T-0001/X-0002 proves the same on four smaller boxes by a
completely independent method.

None of this is evidence about `t > 500`.  Zeros to height `10^13` and beyond
have been verified elsewhere; this repository's certified range is *tiny* by
comparison and its value is not the range but the fact that every step is
reproducible from source in this repository, with the certificates attached.
Quoting "RH verified to height 500" as a contribution to knowledge would be
absurd; quoting it as "the toolchain is sound end to end" is the point.

---

## R-0006 — the Hermite detector's sensitivity floor, and how it scales

*(Superseded in its numbers by the measurement below; the reasoning stands.)*

The signal in T-0001(e) scales like `(delta/r)^2` and the certified quadrature
error like `nsub^{-4}`, so the smallest certifiable displacement should fall
like `nsub^{-2}`.  Measured, on the planted-pair validation box at 250 bits
(`experiments/X-0002-.../results/floor-vs-effort.json`):

```
nsub =  16    floor delta = 0.1
nsub =  32    floor delta = 0.02
nsub =  64    floor delta = 0.005
nsub = 128    floor delta = 0.002
nsub = 256    floor delta = 0.0005      (3.9 s for the whole sweep)
```

Each doubling of the effort buys a factor of about 4 in `delta`, confirming the
`nsub^{-2}` law.  Cost per doubling is a factor of 2, so **`delta` improves
like (work)^{-2}**, and the absolute cost is trivial on this box: `5 * 10^-4` in
under four seconds.  The first version of this entry claimed `delta = 10^-3`
would cost `10^4` times the work of `10^-1`; the truth is a factor of about 16,
and the wrong figure came from a single mis-measured data point (R-0007) plus a
pessimistic reading of the exponent.

**What this does not say.**  The measurements are on the small synthetic box at
height `~2`, where each node evaluation is a four-factor polynomial.  On `zeta`
at height `t` each node costs `O(t)` Euler-Maclaurin terms and the enclosures
are wider, so the *constant* is far worse — the `nsub^{-2}` law is what
transfers, not the four seconds.

Working precision (250, 300, 400 bits) made **no** difference to any floor:
this is quadrature-limited, not precision-limited.

## R-0008 — "certified" enclosures a hundred orders of magnitude too tight

**What happened.**  The first Li-coefficient implementation took the Taylor
coefficients straight from `eta_taylor_coeffs`, which returns the coefficients
of the **truncated** Euler-Maclaurin expression.  The omitted remainder was
never propagated.  The resulting `lambda_n` came with enclosures of `1e-239`
when the truncation error alone is about `1e-61`.

**Why it is nasty.**  The *values* were correct to every digit shown -- they
still match the literature and the zero sum.  Only the error bars were fiction.
A single run looks perfect; nothing about it invites suspicion.

**How it was caught.**  Computing the same coefficients at two truncation
orders and asking whether the enclosures *overlap*.  They did not: the
midpoints differed by far more than the claimed radii.  Two runs that agree to
30 digits but whose intervals are disjoint is a contradiction, and it can only
mean the intervals are wrong.

**Defence adopted, and it generalises.**  *An enclosure that is much tighter
than the error term you know is present is a bug, not a triumph.*  Every
certified quantity in this repository should be sanity-checked against the
order of magnitude of its own truncation parameter, and recomputed at a second
truncation order with an overlap assertion.  This is now a test
(`test_li_enclosures_overlap_across_truncations`).

**Fix.**  Cauchy on the circle `|s-1| = R` bounds the remainder's Taylor
coefficients by `sup|E|/R^k`; `eta` carries it as `(s-1)E`, so coefficient `k`
gains a disc of radius `em(R)/R^{k-1}`.  Take `R > 1` so the bound decays.

---

## R-0007 — a sensitivity floor can be an artefact of the test harness

**What happened.**  X-0002 first reported the T-0001 floor as `delta = 0.1` at
`nsub = 32`, abstaining at `0.03`.  A later measurement of the same method, at
the same effort and the same precision, gave `delta = 0.02`.

**Cause.**  The synthetic test polynomial is evaluated as a product of linear
factors, and **interval arithmetic is order-sensitive**.  The first harness
multiplied the two distant factors (`0.5+i`, `0.5+3i`) before the planted pair;
the second multiplied in increasing height order.  Same polynomial, same
method, same precision — enclosures of the *test function* differ enough to
move the measured floor by a factor of five:

```
factors multiplied as [1i, 3i, pair]   -> detects only delta = 0.1
factors multiplied as [1i, pair, 3i]   -> detects delta = 0.1, 0.05, 0.03, 0.02
```

**Lesson.**  An M-0003 sensitivity measurement measures the **whole pipeline**,
including the harness that generates the synthetic counterexample.  A sloppy
harness understates the detector, which is the safe direction for a *claim* but
the dangerous direction for a *decision*: on the strength of the wrong number,
this agent came within one edit of writing off small-`delta` searches as
costing `10^4` times more than they do.

**Defence adopted.**  The ordering in `X-0002/run.py` now carries a comment
saying not to tidy it, and any future floor measurement must be reported with
the harness construction, not just the method's parameters.

---

## R-0009 — 53-bit LDL manufactured a NOT-PSD verdict, and a whole table with it

**What happened.**  The first exploration of the Nevanlinna-Pick criterion
(T-0005) was written in ordinary floating point.  Its detection table reported
that `N = 8` probe points at distance `D = 1.0` certify an off-line zero for
*every* `delta` tested, down to `1e-6` — an implausibly good result, and one
that would have been the headline of this session.

**Cause.**  The Pick matrix of a configuration with `k` nearby zeros has rank
`~k` (see T-0005), so at `N = 8` it is nearly singular and its trailing pivots
are a numerical rank tail.  Re-running the identical cells in ball arithmetic:

```
delta = 0    N = 8, D = 1.0   pivot = 3.0665e-04  +/- 7.4e-06   UNDECIDED
delta = 1e-3 N = 8, D = 1.0   pivot = 2.8224e-04  +/- 1.1e-05   UNDECIDED
```

The pivot is *positive*; 53-bit elimination had driven it slightly negative.
Every "detection" in that row was noise, including the ones for `delta` where a
real signal also existed — so the table was not even wrong in a consistent
direction.

**What caught it.**  Not inspection — the control.  The `delta = 0`
configuration has every zero on the line, so its Pick matrix is PSD *by
construction*; a NOT_PSD verdict there is impossible for mathematical reasons,
not merely surprising.  Running the control was what forced the rewrite in
`arb`.

**Lesson.**  A PSD verdict is a statement about the *smallest* pivot, which is
exactly the quantity floating point gets wrong on a rank-deficient matrix.  Any
positivity criterion — T-0001's Hankel minors, T-0002's Weil form, T-0005's Pick
matrix — must be decided in interval arithmetic with a three-way verdict, and
`UNDECIDED` must be a first-class outcome rather than a rounding decision.

The deeper point is about *which* control to run.  A control with all zeros on
the line, but with a different number of them, would have passed and taught
nothing: it does not isolate off-line-ness from zero count.  The controls that
made T-0005 trustworthy carry the same zeros at the same height and differ only
in whether the displacement is horizontal (`OFF`) or vertical (`LEHMER`).

**Defence adopted.**  `tests/test_pick.py` runs the `delta = 0` control at 53,
80 and 3000 bits and asserts the verdict is never `NOT_PSD`; and every reported
cell in X-0011 is accompanied by its three matched Herglotz controls, with the
count of control firings printed as part of the result (`0` of `36`).

---

## R-0010 — "measured slope 3.0-3.7" fitted an exponent that parity forbids

**What happened.**  T-0005 reported the Pick detector's signal law as
`|min pivot| ~ delta^3`, from slopes measured over ten decades (3.8, 3.6,
3.0, 3.1, 2.4).  The drift was visible in the numbers and was even flagged in
the claim file, but the headline still said "delta^3", and the N-vs-delta
cost formula was derived from it.

**Why it could never have been right.**  The off-line configuration
`{1/2 ± delta + i gamma}` (plus conjugates) is invariant under
`delta -> -delta`, so every quantity computed from it is an EVEN function of
`delta`.  An odd asymptotic exponent is impossible for symmetry reasons alone.
No slope measurement was needed to rule it out.

**What the truth is.**  X-0014: the exponent is exactly 2 (slope 2.000 over
twenty decades in the isolated-pair model), the coefficient is explicit
(L-0009: `-2(|Ahat'(gamma)|^2 + |Ahat'(-gamma)|^2)/v*v`, verified to nine
digits), and the 3-ish readings were a crossover: `|c4/c2| ~ 10^3`, so the
`delta^4` term dominates until `delta ~ 0.03`, and below `1e-7` the signal
dies into the rank-tail floor at the tested `N` -- the fitted window sat
exactly in the transition.  claude-01's own drifting slopes were the data
version of this statement.

**Lesson.**  Before fitting a power law, write down the symmetries of the
configuration; they constrain the allowed exponents for free.  And a slope
that DRIFTS monotonically across the fitted window is not measuring an
exponent -- it is measuring a crossover between two exponents.

**Consequence.**  The corrected law is BETTER for detection: `delta^2` beats
`delta^3` at small `delta`, and the probe-count formula improves from
`N >~ 1.11 log10(1/delta)` to `N >~ 0.74 log10(1/delta)`.
