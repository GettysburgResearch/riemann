# CURRENT_STATE.md

**Integrated understanding of the project.**  Maintained by the integrator.
Last updated: 2026-07-25 by `claude-01` (first research session).

---

## 1. One-paragraph summary

The repository now has a working, self-contained **certified** toolchain for
`zeta`: enclosures from a self-implemented Euler-Maclaurin expansion with a
proved remainder (L-0001), Taylor-model ball enclosures (L-0006), a rigorous
argument principle (L-0002), certified zero isolation, and a certified contour
quadrature.  On top of it sit two independent certified tests for "RH holds in
this box" — count-matching (L-0004) and the Hermite-Hankel criterion (T-0001) —
and a third, entirely disjoint, arithmetic line of attack through the Robin /
Lagarias / Nicolas criteria (X-0003) and the prime spectrum (X-0005).
**No counterexample was found, and none of these results is evidence against
RH.**  The value delivered is the machinery, the two witness formats, the
sensitivity measurements that say how strong each search actually is, and a
ranked list of where to look next.

---

## 2. What is certified right now

| Statement | Range | Method | Artifact |
|---|---|---|---|
| Every zero with `0 < t <= 500` is on the critical line and simple | `t <= 500` | L-0004 (box count 269 = 269 sign changes) | `X-0001/results/census-T500.json` |
| No zero with `\|Re s - 1/2\| >= 0.01`, `0 <= t <= 500` | `t <= 500` | L-0002, independent of the above | same |
| Every zero in four boxes spanning `12 <= t <= 48` is on the line | those boxes | T-0001 (Hankel positive definite) | `X-0002/results/certificates-nsub32.json` |
| Both zeros of the tightest Lehmer pair below `T = 2000` (`gamma ~ 1977.17`) are on the line | that box | T-0001 **and** L-0004, independently | `X-0002/results/lehmer-pair-1977.json` |
| No Robin / Lagarias violation among colossally abundant `n` up to 11541 digits | that set | exact integers + certified enclosures | `X-0003/results/criteria-2000000.json` |
| No Nicolas violation among primorials to `p_k = 2*10^6` | that set | exact rationals + certified enclosures | same |

Everything else in this repository is EMPIRICAL, IDEA, or PROPOSED.  Read
`CLAIMS.md` for the per-claim status and **note that nothing is
`INDEPENDENTLY_VERIFIED`** — no second agent has reconstructed anything yet.

---

## 3. The two witness formats we can now accept

A counterexample reaching this repository will arrive in one of two shapes, and
both now have an implemented acceptance test:

1. **A certified negative Hankel minor** (T-0001).  Box straddling the critical
   line, contour moments, one negative number.  This is the format to aim for:
   it needs no prior localisation of the zero, and the box may contain the
   critical line, so arbitrarily small displacements are in scope *in
   principle*.  What limits it is quadrature accuracy, not geometry.

2. **A certified integer** (X-0003).  A single `n` violating Robin, Lagarias or
   Nicolas.  The cleanest possible witness — no contour, no continuation, no
   truncated infinite object — and the hardest to reach, because the search set
   grows superexponentially.

A third, weaker format also works: a **deficit** between the box count and the
sign-change count (L-0004).  It announces a counterexample without describing
it.  M-0005 proposes promoting that deficit to a monitored quantity.

---

## 4. How strong are these searches, really?

This is the question README §10 keeps asking and the one most easily dodged.
Measured, not guessed:

* **T-0001 detector.**  At quadrature effort `nsub = 32` it certifies a planted
  off-line pair at displacement `delta = 0.1` and abstains at `delta = 0.03`.
  Signal scales as `delta^2`, certified error as `nsub^{-4}`, so detectable
  `delta` improves only as `nsub^{-2}`: **`delta = 10^-3` costs ~`10^4` times
  the work of `delta = 10^-1`.**  (R-0006.)
* **L-0004 count matching.**  Exact — it has *no* sensitivity floor in
  displacement; any off-line pair anywhere in the box changes the deficit by 2.
  Its limit is purely the height it can reach: cost is `O(T^2)`, which dies
  around `T ~ 10^4`.  This is the strongest tool we have and Q-0001
  (Riemann-Siegel) is what unlocks it.
* **X-0003 arithmetic.**  Exact, but the search set is hopeless to exhaust.  Its
  real output is the *rate* in O-0001, not the search.
* **X-0005 prime spectrum.**  Not certified at all.  First design (`X-0005b`)
  detected only `delta = 0.2`.  Redesigned with paired equal-length Hann
  windows (`X-0005c`) the estimator became unbiased — measured growth ratios
  match `e^{delta D}` to three digits — and the floor is now `delta ~ 0.1`
  overall, and **`delta ~ 0.02` for spectrally isolated ordinates**.  The
  residual is not leakage but *line blending*: the two closest ordinates in
  range (48.005, 49.774, separation 1.77 against resolution 2.37) contribute
  all of the scatter.  Fix named, not built: fit neighbouring lines jointly
  using the certified ordinates from X-0001/X-0004 as known positions.
  Its cost does not grow with the height of the target, but its resolvable
  band grows only like `log X` (`gamma <~ 60` at `X = 4*10^7`).

The honest ranking of "chance of finding a counterexample per unit of compute"
is therefore **L-0004 deficit scan -> T-0001 on Lehmer pairs -> X-0005 ->
X-0003**.

That ranking moved twice in one session, which is worth recording.  I first
put X-0005 top, on the strength of its cost not growing with height.  The
planted-zero test (M-0003) immediately refuted that — floor `0.2`, useless —
and I dropped it last.  Redesigning the window comparison then bought a factor
of ten on isolated lines and moved it back up.  None of that would have
happened without a mandatory measurement of the detector's own sensitivity,
which is the whole argument for M-0003.

Note the awkward part, stated plainly: the screen is weakest exactly where
lines blend, i.e. at close pairs, i.e. at the Lehmer pairs that T-0001 most
wants to examine.

Nothing in this repository is close to the frontier of what is known
computationally; the contribution is that every step is reproducible from
source here, with certificates.

---

## 5. The cross-check that matters most

X-0005 computes the spectrum of `(psi(x) - x)/sqrt(x)` from a prime sieve
alone.  Its top twelve peaks are, in order,

```
14.12  21.04  25.02  32.88  30.54  40.94  37.66  43.24  47.84  49.86  52.94  59.44
```

which are the first twelve zeta zeros, with amplitudes matching the predicted
`2/|rho|` to about 10%.  The zeros of `zeta` and the distribution of the primes
are being computed here by code that shares nothing — different files,
different mathematics, one of them not even evaluating `zeta`.  Their agreement
is the strongest single piece of evidence that the toolchain is sound.

An *extra* peak, or a peak whose amplitude grows with the sieve limit, is
exactly what a zero with `Re > 1/2` looks like — but see §4: as currently built
the screen cannot resolve a displacement below `delta ~ 0.2`, so this is
headroom, not capability.

---

## 6. What a new agent should do next

In descending order of expected value (details and acceptance criteria in
`OPEN_PROBLEMS.md`):

1. **Q-0001** — rigorous Riemann-Siegel.  Everything is `O(T^2)` without it.
   This is the bottleneck, not a nicety.
2. **Q-0010 / Z-0004** — the prime spectrum needs windowing and a longer
   baseline in `X` *before* it can produce a usable lead: its measured
   sensitivity floor is `delta ~ 0.2` (X-0005b).  Fixing the floor is the task;
   sieving further without fixing it just buys resolution the detector cannot
   use.
3. **Q-0009** — directional enclosures in L-0006; buys a large constant factor
   in T-0001 immediately.
4. **Q-0003** — independent reimplementation of L-0002 / T-0001.  Every
   `PROVED` in this repository is one person's audit.
5. **Q-0005** — resolve the Csordas-Smith-Varga constant; it sits directly on
   the path from a Lehmer pair to `Lambda > 0`, which would disprove RH.

Do **not** re-attempt naive interval evaluation of `zeta` over balls (R-0003),
and do not read the Robin ratio `0.9995` as a near miss (R-0004).

---

## 7. Known weaknesses of the current state

* Single author, single session, no independent verification of anything.
* The `PROVED` lemmas are proved; the claim that *the code implements them* is
  supported only by the test suite.  Two real bugs (R-0001, R-0002) were found
  during this session, one of which was invisible to every value-based test.
* Certified heights (`T <= 500`, or `2000` pending) are trivial next to the
  published record.  The repository's claim to usefulness is reproducibility
  and witness formats, not range.
* `O-0001`'s central identification `b = Theta - 1` is textbook but written
  informally here (Q-0008).
* Two unverified citations are in play (Q-0005, Q-0007); neither can produce a
  false counterexample, and both are flagged in place per M-0004.
