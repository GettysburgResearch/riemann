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
| Every zero with `0 < t <= 1000` is on the critical line and simple | `t <= 1000` | L-0004 (box count 649 = 649 sign changes) | `X-0001/results/census-T1000.json` |
| Every zero with `0 < t <= 500` is on the critical line and simple | `t <= 500` | L-0004 (box count 269 = 269 sign changes) | `X-0001/results/census-T500.json` |
| No zero with `\|Re s - 1/2\| >= 0.01`, `0 <= t <= 500` | `t <= 500` | L-0002, independent of the above | same |
| Every zero in four boxes spanning `12 <= t <= 48` is on the line | those boxes | T-0001 (Hankel positive definite) | `X-0002/results/certificates-nsub32.json` |
| The four tightest Lehmer pairs below `T = 2000` (`gamma = 1977.17, 1329.04, 1415.59, 1054.78`) have both zeros on the line | those boxes | T-0001 **and** L-0004, independently, on each | `X-0002/results/lehmer-pair*.json` |
| 1517 certified on-line zero ordinates for `0 < t <= 2000` | `t <= 2000` | sign change + bisection (existence only; not a completeness claim without the box count) | `X-0004/results/lehmer-T2000.json` |
| Deficit `N_box - m` is `0` in all 24 height bands to `T = 500` | `t <= 500` | M-0005 ledger | `X-0001/results/deficit-ledger.json` |
| **Every zero with `0 < t <= 1000` is simple and has `\|Re rho - 1/2\| <= 2.94e-11`** | `t <= 1000` | L-0007 interval Newton + the certified box count 649 | `X-0007/results/newton-T1000.json` |
| Same at `t <= 100`, with the sharper bound `2.24e-14` | `t <= 100` | same | `X-0007/results/newton-T100.json` |
| The classical Lehmer pair (`gamma ~ 7005.06`, normalised gap 0.042) has both zeros on the line | that box | T-0001 **and** L-0004 | `X-0002/results/lehmer-pair-7005.json` |
| Weil quadratic forms positive definite at `gamma_0 = 0, 14, 100, 500, 1977, 7005` | those filters | T-0002, from 143 prime powers and `Gamma` -- no `zeta` anywhere | `X-0006/results/matched-filter.json` |
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

* **T-0001 detector.**  First, the distinction that matters: T-0001(c) is an
  *equivalence*, so a `PD` verdict excludes an off-critical zero in that box at
  **every** displacement, however small — there is no exclusion floor.  The
  floors below are for the opposite direction: how large a real counterexample
  must be before the method *announces* it (`NOT_PSD`) instead of abstaining.
  Measured floors on the planted-pair box:
  `delta = 0.1` at `nsub = 16`, `0.02` at `32`, `0.005` at `64` (the smallest
  displacement tested, not a limit of the method).  Each doubling of effort
  buys a factor of 4-5 in `delta`, confirming the `nsub^{-2}` law; since a
  doubling costs only a factor of 2 in work, **`delta` improves like
  (work)^{-2}**, and `10^-4` looks reachable at these heights.  (R-0006.)
  An earlier version of this line said the floor was `0.1` and that `10^-3`
  would cost `10^4` times the work; that was an artefact of the test harness's
  own interval enclosures, not of the method (R-0007).
  On real `zeta` boxes the announcement threshold is
  `delta ~ (gap/2) sqrt(rho)` (X-0002b): `0.031 .. 0.280` on ordinary boxes but
  `0.0043 .. 0.0057` on the four Lehmer-pair boxes — fifty times better where
  the zeros are closest, which is why Z-0002 aims there.
* **L-0004 count matching.**  Also exact in displacement — any off-line pair
  anywhere in the box changes the deficit by 2, and unlike T-0001 it *announces*
  at any displacement too, since the deficit is an integer.  Its limit is purely
  the height it can reach: cost is `O(T^2)`, which dies around `T ~ 10^4`.  On
  present evidence this is the strongest tool in the repository, and Q-0001
  (Riemann-Siegel) is what unlocks it.
* **X-0003 arithmetic.**  Exact, but the search set is hopeless to exhaust.  Its
  real output is the *rate* in O-0001, not the search.
* **X-0005 prime spectrum.**  Not certified at all.  First design (`X-0005b`)
  detected only `delta = 0.2`.  Redesigned with paired equal-length Hann
  windows (`X-0005c`) the estimator became unbiased — measured growth ratios
  match `e^{delta D}` to three digits — and the floor is now `delta ~ 0.1`
  overall, and **`delta ~ 0.02` for spectrally isolated ordinates**.  The
  residual was not leakage but *line blending*.  Replacing peak-reading with a
  **joint least-squares fit at the certified ordinates** (`X-0005d`) removed
  blending entirely: baseline scatter `0.168 -> 5e-15`, and the estimator
  tracks `e^{delta D}` to five digits down to a planted `delta = 0.0005`.
  The screen's real-data floor is now `~ 0.02`, set by *model mismatch* — the
  unmodelled band above `gamma = 78`, and the non-zero terms of the explicit
  formula — every piece of which is a writable term.  Its cost does not grow
  with the height of the target, but its resolvable band grows only like
  `log X`.

The honest ranking of "chance of finding a counterexample per unit of compute"
is therefore **L-0004 deficit scan -> T-0001 on Lehmer pairs -> X-0005 ->
X-0003**.

That ranking moved three times in one session, which is worth recording.  I first
put X-0005 top, on the strength of its cost not growing with height.  The
planted-zero test (M-0003) immediately refuted that — floor `0.2`, useless —
and I dropped it last.  Redesigning the window comparison bought a factor of
ten on isolated lines; replacing peak-reading with a joint fit then removed the
estimator as a limitation altogether.  Each step was driven by a measurement
that contradicted the previous judgement, which is the whole argument for
M-0003.

The awkward part of the middle stage — that the screen was weakest exactly at
close pairs, i.e. at the Lehmer pairs T-0001 most wants to examine — was
dissolved by the joint fit, since fitting neighbouring lines together does not
care how close they are.  That is now an argument for the screen rather than
against it.

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
* Certified heights (`T <= 1000`; a `T = 2000` box count was attempted and lost
  to a container restart after 47 minutes) are trivial next to the
  published record.  The repository's claim to usefulness is reproducibility
  and witness formats, not range.
* `O-0001`'s central identification `b = Theta - 1` is textbook but written
  informally here (Q-0008).
* Two unverified citations are in play (Q-0005, Q-0007); neither can produce a
  false counterexample, and both are flagged in place per M-0004.
* **Provenance caveat.**  Several result JSONs record `git_sha = 4bb7e26`, the
  commit that existed when the run started — i.e. before the code being
  measured had been committed.  The runs are reproducible from the code now in
  the tree, but the recorded SHA does not pin it.  Anyone re-running should
  regenerate the certificates and confirm the SHA matches; `X-0002`'s was
  regenerated for exactly this reason after the R-0007 harness fix.
