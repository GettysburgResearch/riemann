# Validation and assurance boundary

## What "certified" means here

All arithmetic is Arb ball arithmetic via `python-flint` 0.9.0 (FLINT/Arb).
A predicate is recorded as violated only when `arb(x) < 0` returns true, which
holds only if **every** point of the ball is strictly negative. Midpoints appear
in the JSON for orientation and are never an acceptance input. Positive verdicts
use the same operator with the opposite sign, and a ball straddling zero is
recorded as `inconclusive` rather than resolved either way.

Arb's `acb.integral` is a rigorous integrator: it returns an enclosure, not an
estimate. It requires a **holomorphic** integrand, which constrains how the
piecewise-polynomial parts of E3 had to be written (below).

## Bugs found and fixed during this work

Both were caught by validation, not by inspection, and both had the potential to
manufacture a false refutation of RH.

1. **E3 reported `RH_REFUTED: true` on its first run.** Cause: the von Mangoldt
   sieve returned the prime `p` where the weight `Lambda(n) = log p` was
   required. With the wrong weight the prime side of the explicit formula is
   inflated by a factor of roughly `p / log p`, the pole/prime cancellation
   fails, `tau(m)` grows instead of staying bounded, and the Toeplitz matrix
   becomes wildly indefinite. Detected by `e3_validate.py`, which showed `tau(0)`
   matching the zero side to `7e-8` while every `m >= 1` was off by orders of
   magnitude and by sign.

2. **The B-spline was evaluated non-rigorously inside the integrand.** Two
   distinct defects: (a) branch selection used certified comparisons, so a ball
   straddling a knot failed every test and silently fell through to the wrong
   polynomial branch; (b) `v.real` appeared inside the integrand, making it
   non-holomorphic and invalidating Arb's rigorous error bounds outright. Fixed
   by splitting every integral at the knots of `E_m` and evaluating each piece
   through an explicit polynomial branch containing no `abs()` and no `.real`.
   `Bspline` retains a ball-safe hull path for point evaluation only.

3. **A regularisation bound, not the arithmetic, limited certification.** The
   archimedean integrand has a removable `1/v` singularity cut at `EPS_CUT`.
   At `2^-80` the explicit remainder bound `~4.1e-25` dominated every `tau`
   radius, and `LDL^T` on the near-singular Toeplitz matrix (radius growth about
   2.5 bits per elimination step) came back `inconclusive` even at 900 bits.
   Setting `EPS_CUT = 2^-400` with working precision 1400–2000 bits made all four
   families certify as positive definite. The earlier `inconclusive` runs are
   retained in `results/e3_weil_hp.json` as the record of that boundary.

## Known reporting limitation

`common.ball()` serialises enclosures as float64. At `z ~ 982` the Laguerre form
is of size `1e-333`, which underflows to `-0.0` in the JSON. The E2 ladder
witness is therefore re-verified and quoted from the Arb string representation
in `RESULTS.md`; the JSON float field for that witness is not meaningful. Future
runs should carry a string field alongside the floats.

## What was executed

* E1 calibration: 12 `delta` values, 40 bisection steps each, 300-bit precision.
* E1 mid band: 9 427 ordinates, 1 913 681 predicate evaluations, 220-bit, 5 400 s.
* E1 high band: 260 ordinates, 52 780 predicate evaluations, 220-bit, 7 008 s.
* E2 self-test: normalisation pinned against the first zeta ordinate.
* E2 census: 4 914 points over `z` in `[26, 1500]`, auto-scaled precision, 5 469 s.
* E2 ladder: 22 bisection steps over 15 probe points, 346 s, witness re-verified
  at 900 bits.
* E3 validation: 569 Hardy Z zeros, `tau(0..8)`, agreement to `~1e-9`, PASS.
* E3: four families, certified `LDL^T`, 1400–2000 bits.

## What was NOT done

* No independent mathematical review of the predicates or of the code.
* No Lean formalisation; no repository-wide build; no remote CI; no replay on a
  second platform or a second implementation.
* No exhaustive ordinate coverage. E1's grids leave gaps: an off-line pair with
  `delta` below the per-band detection threshold, or at any height outside the
  two scanned windows, is untouched. The repository's own warning that
  "existential witness geometry does not say a predetermined finite grid will
  find the witness" applies in full.
* E2's census reaches `gamma = 750`, far below any verification frontier; its
  `Lambda` rung is weaker than the published literature and is superseded
  unconditionally by Rodgers–Tao.
* E3 certifies four finite-dimensional families of compactly supported test
  functions. That is not the full Weil criterion.
* `e3_validate.py` uses mpmath's Hardy Z as an independent zero source. It is a
  cross-check only; no zero data enters any acceptance path in E1, E2 or E3.

## Reproduction

`python3 tests.py` re-runs the fast structural checks: the Arb comparison
semantics this packet depends on, the `Phi` normalisation against the first zeta
ordinate, the E1 predicate detection of an injected off-line pair, the von
Mangoldt weight, and a small certified `LDL^T`. It does not re-run the long
sweeps; those are reproduced with the commands in `README.md`.
