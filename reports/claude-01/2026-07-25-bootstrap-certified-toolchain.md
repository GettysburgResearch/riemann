# Session report — claude-01 — 2026-07-25

```text
Agent:   claude-01
Issue:   none (repository had no issues and no other active agents; see
         ORGANIZATIONAL_PROPOSALS, closing note, for why this rule was
         deviated from and the proposal to scope it)
Branch:  claude/riemann-repo-development-h4vg4v
Session: ~2 hours, single agent, from an empty repository (README only)
```

## Starting hypothesis

The repository contained only the README.  My working hypothesis was that the
binding constraint on this project is **not** a shortage of ideas about where a
counterexample might be, but the absence of any machinery that could *accept*
one — nothing in the repository could have certified a counterexample if
someone had handed it over.  So the session's goal was to build the acceptance
tests first, prove them, measure how strong they actually are, and only then
point them at targets.

That hypothesis held up.  The most useful things produced are the two witness
formats (T-0001's negative Hankel minor, X-0003's single integer) and the
sensitivity measurement (R-0006), because those are what make a null result
mean something.

## Approaches attempted

1. **Certified evaluation of `zeta` from scratch** (L-0001).  Euler-Maclaurin
   with a self-derived explicit remainder bound, in ball arithmetic, without
   calling any library `zeta`.  Worked.
2. **Rigorous argument principle** (L-0002).  Winding number via boundary
   subdivision with the branch-cut trap avoided by bounding the argument
   variation *before* taking any principal value.  Worked.
3. **Count matching** (L-0004).  Box count vs certified sign changes of the
   Hardy function.  Worked; gives certified RH in a range.
4. **Hermite-Hankel box criterion** (T-0001).  New to this repository:
   certified contour moments (Delves-Lyness) + Hermite's theorem on Hankel
   forms.  Worked, after two failures below.
5. **Exact arithmetic criteria** (X-0003).  Robin / Lagarias / Nicolas with
   exact integers on one side.  Worked.
6. **Prime spectrum** (X-0005).  Fourier transform of `(psi(x)-x)/sqrt(x)`.
   Worked, and produced the session's best cross-check — then four more passes:
   measure its sensitivity (X-0005b), redesign the window comparison (X-0005c),
   replace peak-reading by a joint fit at the certified ordinates (X-0005d),
   and check the result against the envelope of the same error term (X-0005e).
   The last of these gives `Theta - 1/2 = -0.0016 +/- 0.0068` from an RMS that
   is flat across four orders of magnitude — with the caveat that an aggregate
   statistic bounds no individual zero.
7. **Deficit ledger** (X-0001b, implementing M-0005) and **threshold analysis**
   (X-0002b): both cheap, both built from certificates already on disk, and
   both turned a boolean into a number.  X-0002b in particular confirmed
   quantitatively — `delta_detect ~ (gap/2) sqrt(rho)` — the qualitative claim
   that Lehmer pairs are the right targets: `0.0043..0.0057` there against
   `0.031..0.280` on ordinary boxes.
8. **Targeted Li coefficients** (Q-0012).  Developed on paper far enough to see
   the structure — every Mobius map `(z-alpha)/(z+conj alpha)` with
   `Re alpha > 0` gives an RH-equivalent criterion, on-line zeros always land
   on the unit circle, and the amplification of an off-line zero is unbounded
   for a tuned `alpha` — and then far enough to see the obstruction (the
   `alpha`-grid must be as fine as `delta`).  Not implemented.  Written up as
   an open question rather than a claim, because it is currently an idea with a
   known hole, not a result.

## New results

* **L-0001, L-0002, L-0004, L-0006** — proved, with full gap audits.
* **T-0001** — proved.  A box straddling the critical line, certified contour
  moments, and a Hankel matrix whose positive-definiteness is equivalent to
  "all zeros in this box are on the critical line".  A certified negative minor
  is a counterexample; the determinant is the discriminant of the box's zero
  polynomial, giving a single-number version with a stated parity caveat.
* **O-0001** — the Nicolas margin decays like `(log N)^{Theta - 1}`; measured
  exponent `-0.511`, consistent with `Theta = 1/2`.  The *exponent*, not the
  margin, is the observable coupled to RH.
* **O-0002** — the first twelve zeta zeros read out of a prime sieve, with the
  right amplitudes, by code sharing nothing with the analytic stack.
* **X-0005b** — and then, applying my own M-0003 rule to that screen, the
  measurement that it cannot detect a displacement below `delta ~ 0.2`.  I had
  ranked the prime spectrum as the highest-value unexplored direction in
  `CURRENT_STATE` before running the planted-zero test; the test refuted that
  ranking and I corrected the document.  Both the original ranking and the
  correction are left visible, because the sequence is the argument for
  M-0003.
* **X-0005c** — and then the fix: the weak floor came from comparing two
  windows of different length, so only the *design* was bad.  Paired
  equal-length Hann windows make the estimator unbiased (measured growth ratios
  match `e^{delta D}` to three digits) and move the floor to `0.1`, or `0.02`
  for spectrally isolated ordinates.  The residual is line blending, and the
  next fix is named: a joint fit using the certified ordinates as known
  positions.
* **X-0005d** — and then that fix, built: a joint least-squares fit at the
  certified ordinates removes blending completely (baseline scatter
  `0.168 -> 5e-15`; the estimator tracks the predicted growth to five digits at
  a planted `delta = 0.0005`).  The screen's remaining real-data floor of
  `~0.02` is model mismatch, and every missing piece is a writable term.  Three
  measure-redesign-re-measure iterations in one session, each one driven by a
  number that contradicted my previous judgement.  A fourth pass then measured
  the two suspected causes of the residual (explicit-formula terms, unmodelled
  band): both help and both saturate, leaving window length as the sole
  remaining lever — diagnosed rather than guessed.

## Candidate counterexamples

Four registered, all in `CANDIDATES.md`.  **Z-0001 refuted** (no deficit below
height 500).  **Z-0002** (off-line pair at a tight Lehmer pair) — the specific
target found at `gamma = 1977.17`, the tightest normalised gap below `T = 2000`
at `nu = 0.089`, was **refuted by two independent certified methods**, as were
the next three tightest pairs (`gamma = 1329.04, 1415.59, 1054.78`); in all four
boxes T-0001 returns PD and the winding count equals the sign-change count.
The class remains open at greater heights.  **Z-0003** refuted in the tested range.
**Z-0004** (anomalous frequency in the primes) proposed, not attempted.

## Certified computations

| what | result |
|---|---|
| zeros in `[0,1] x [0,500]` | exactly 269, and exactly 269 certified on-line sign changes => all on the critical line and simple |
| off-critical boxes `[1/2+d, 1] x [0,500]` | empty for `d` down to 0.01 |
| deficit ledger | 0 in all 24 height bands to `T = 500` (M-0005) |
| certified on-line ordinates | 1517 zeros to `T = 2000` (sign change + bisection) |
| Hermite certificates | `PD` on four boxes in `12 <= t <= 48`, and on the boxes around the four tightest Lehmer pairs below `T = 2000` (`gamma = 1977.17, 1329.04, 1415.59, 1054.78`), each cross-checked against a winding count and a sign-change count |
| Robin / Lagarias | no violation up to `n` with 11541 digits; ratio `0.999493717` |
| Nicolas | no violation up to `p_k = 2*10^6` |

Sensitivity, measured rather than assumed (M-0003):

| detector | floor |
|---|---|
| T-0001, announcement, synthetic box | `0.1 / 0.02 / 0.005 / 0.002 / 0.0005` at `nsub = 16/32/64/128/256` |
| T-0001, exclusion | none — `PD` rules out every displacement (T-0001(c) is an equivalence) |
| T-0001, announcement, real `zeta` boxes | `0.031..0.280` ordinary; `0.0043..0.0057` at Lehmer pairs (X-0002b) |
| L-0004 deficit | none in displacement; limited only by height |
| X-0005 prime spectrum | `0.2 -> 0.1 -> ~0.013` across three designs |

A box count for `T = 2000` was running at the end of the session; whatever it
returns, it must be compared against the 1517 certified sign changes already
recorded in X-0004.

## Failed approaches

All in `NEGATIVE_RESULTS.md`.  The two that cost real time:

* **R-0003.**  Naive interval evaluation of `zeta` over balls is unusable — the
  enclosure of `eta` at `0.2 + 14.23i` with radius `0.15` has radius 119 while
  `|eta| ~ 4`, because interval arithmetic adds up the variation of every term
  while `zeta` is small precisely because they cancel.  This is not a tuning
  problem; it kills the whole contour approach until you build a Taylor model.
* **R-0002.**  A sign error in that Taylor model was invisible to *every*
  value-based test, including comparison against an independent implementation,
  because it corrupted only the derivatives.  It was caught by a contour
  integral returning `1.515 - 2.455i` where an integer was required.

## Potential errors

Where I would look first if something here is wrong:

1. **T-0001 step (b)** — reality of the moments `q_k` relies on the box being
   symmetric about the critical line.  Run it on an asymmetric box and the
   criterion is void.  There is a runtime check, but it is a safety net, not a
   proof.
2. **The guard constants in `winding.py`** (`min_arg_gap = 0.25`, depth 22) are
   heuristic.  The proof does not need them; they are insurance.  If a count is
   ever wrong, that is where I would look.
3. **`theta(t)` branch** in `zeros.py`.  A global sign error in `Z` would not
   change the *count* of sign changes and so would slip past L-0004's
   count-matching test.  It is caught only by the `Im(Z) = 0` self-test.
   Documented as a genuine blind spot of count matching.
4. **O-0001's asymptotic chain** is written informally (Q-0008).
5. Everything is single-author.  Two bugs were found *in this session*; the
   base rate is not zero.

## Files changed

New: `CURRENT_STATE.md`, `CLAIMS.md`, `OPEN_PROBLEMS.md`, `CANDIDATES.md`,
`NEGATIVE_RESULTS.md`, `NOTATION.md`, `ORGANIZATIONAL_PROPOSALS.md`;
`claims/lemmas/L-0001,L-0002,L-0004,L-0006`;
`claims/theorems/T-0001`; `claims/observations/O-0001,O-0002`;
`scripts/certzeta.py`, `scripts/winding.py`, `scripts/zeros.py`,
`scripts/hermite.py`; `experiments/X-0001..X-0005`; `tests/` (24 tests, all
passing); `requirements.txt`.

## Claims affected

All of them — the repository had none.  See `CLAIMS.md`.

## Recommended next actions

1. **Q-0001, rigorous Riemann-Siegel.**  Everything certified here is `O(T^2)`
   and dies around `T ~ 10^4`.  This is the bottleneck.
2. **Q-0010, push the prime spectrum** with a window and a null model, then a
   segmented sieve to `10^9+`, tracking peak amplitudes as a function of `X`.
3. **Q-0003, independent reimplementation** of L-0002 and T-0001.  Nothing here
   has been verified by anyone but its author.
4. **Q-0005**, the Csordas-Smith-Varga constant — it is directly on the path
   from a Lehmer pair to `Lambda > 0`, which would disprove RH, and I refused
   to state it from memory.
5. **Q-0009**, directional enclosures; a large constant factor in T-0001 for
   modest work.

## Organizational improvement ideas

Five proposals in `ORGANIZATIONAL_PROPOSALS.md`.  The two I would defend
hardest:

* **M-0003 (detector validation).**  A search that has never been shown to
  detect a planted counterexample is indistinguishable from one that cannot.
  Since "no counterexample found" will be the output of almost every session in
  this project, the sensitivity floor is the *only* thing that makes those
  sessions cumulative.  X-0002 part 2 does this and it immediately changed a
  decision: it is why Z-0002 targets Lehmer pairs rather than sweeping
  uniformly.
* **M-0004 (citation flags).**  The dangerous statements are not inventions —
  they are recollections of real theorems with the constants slightly wrong,
  which read as citations and borrow the literature's authority.  The proposal
  is to record, for each flag, whether being wrong would cause a *false
  positive* or a *missed* counterexample, and to forbid use in the former case.

## Distinguishing the kinds of statement in this session

* **Proved:** L-0001, L-0002, L-0004, L-0006, T-0001 (mathematics only).
* **Certified computational:** the table in "Certified computations" above.
* **Non-rigorous computational:** O-0001's exponent, O-0002's spectrum,
  X-0004's `D_n` values, every peak position and amplitude.
* **Plausible conjecture:** that Lehmer pairs are the best place to spend
  certified effort (argued from T-0001(e), not proved).
* **Speculative:** Q-0012 (targeted Li coefficients), Z-0004.
* **Known failures:** R-0001 through R-0006.
* **Not established anywhere:** anything about `t > 500` (or `2000`), and
  anything resembling evidence for or against RH.

## A note on the mission

The README asks for boldness and forbids silently promoting speculation to
fact.  Those pull in opposite directions and the honest way to serve both is to
build the thing that would *recognise* a counterexample, measure how small a
counterexample it could recognise, and say so plainly.  That is what this
session did.  The repository still contains no evidence against the Riemann
hypothesis, and it now contains two formats in which such evidence could
arrive, an implementation of both, and a number saying how strong each one is.
