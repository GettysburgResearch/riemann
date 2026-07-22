# Agent report — Issue #14 negative Li coefficient search

Agent: `gpt56-04`  
Issue: #14  
Branch: `agent/gpt56-04/14-negative-li-coefficient`  
Date: 2026-07-22

## Starting hypothesis

A negative Li coefficient might occur at a moderate index and be discoverable
without a zero list by comparing a local expansion at `s=1` against an
independent Cauchy coefficient extraction.  Any candidate would then be sent to
ball-arithmetic certification.

## Approaches attempted

1. Reconstructed the exact standard `xi` normalization and Li derivative
   definition from the seed material in draft PR #21.
2. Derived a finite Stieltjes-to-eta recurrence for `lambda_n` without a
   truncated nontrivial-zero sum.
3. Derived independently the generating function
   `log(2*xi(1/(1-z)))=sum lambda_n z^n/n` and its logarithmic derivative.
4. Calibrated the two formulas through `n=50` at 100 decimal digits.
5. Implemented a binary64 Cauchy--FFT discovery scan with precision escalation
   for isolated zeta-derivative failures.
6. Scanned every index through `n=100000` at two distinct contour radii.
7. Audited how much published low-height zero verification is sufficient to
   justify each chosen transformed disk, independently of RH at larger heights.

## New results

### Proved in the submitted, unreviewed lemma

L-0401 gives:

- the exact triangular recurrence for the coefficients of
  `(t*zeta(1+t))'/(t*zeta(1+t))`;
- the exact finite formula
  `lambda_n = n*a1 + sum_{k=2}^n binom(n,k) B_k`;
- the independent Cauchy generating function and logarithmic derivative;
- the radius reduction `H(r)=1/sqrt(1-r^2)` for excluding transformed zero
  singularities from a disk, conditional only on verified critical-line
  location below that explicit height.

Status remains `PROPOSED` pending independent review.

### Non-rigorous computational observations

- The recurrence and direct 100-decimal Cauchy calculation agree through
  `n=50` with maximum reported discrepancy
  `4.61109413898154153607909649279e-75`.
- Two FFT scans, each with `262144` samples and different radii, found no
  negative coefficient for any `1<=n<=100000`.
- From `n>=1000`, the smallest observed coefficient is approximately
  `lambda_1000=2326.05316`.
- The two scans differ by at most about `1.41e-4` at their stored checkpoints.
- The scan encountered 25 and 27 binary64 zeta-derivative convergence failures,
  respectively; each was recomputed at 40 decimal digits and counted.

These are `EMPIRICAL`, not certified facts.

## Candidate counterexamples

None.  No strict negative value was observed, no interval sign was produced,
and no `Z-####` identifier was allocated.

## Certified computations

None.  The session did not obtain a working Arb/python-flint backend in the
execution environment, and neither aliasing nor roundoff was enclosed with
directed arithmetic.

## Failed approaches

- A direct high-precision recurrence becomes expensive quickly because it
  requires many Stieltjes constants and an `O(n^2)` binomial transform.  It was
  used only for small-index calibration.
- An initial `n=100000`, oversampling-8 contour run was computationally
  inefficient.  Moving the contour inward with alpha 10 and 12 reduced the
  sample count while keeping the coefficient amplification modest.
- A truncated zero sum was deliberately rejected: without a proved symmetric
  tail it can report a false sign and is not a valid Li coefficient evaluation.
- The available package index did not provide python-flint, so the intended
  interval-certification phase was not completed.

## Potential errors

- The local recurrence depends on the exact Stieltjes sign convention; an
  independent reviewer should rederive it from the Laurent expansion.
- The FFT results may contain aliasing, zeta-evaluation, and binary64 rounding
  errors.  The reported roundoff scalar is only a rough diagnostic.
- The precision fallback mixes high-precision zeta values with ordinary
  digamma evaluation; this is acceptable only for discovery and must not enter
  a proof.
- The low-height radius lemma must be paired with a rigorously imported
  verified-zero theorem before it is used in a certificate.
- The two wide scans perturb the radius but share code and therefore do not
  constitute independent implementations.

## Files changed

- `claims/lemmas/L-0401-li-local-cauchy-formulas.md`
- `claims/observations/O-0401-no-negative-li-through-100000.md`
- `experiments/X-0401-li-coefficient-search/README.md`
- `experiments/X-0401-li-coefficient-search/calibrate.py`
- `experiments/X-0401-li-coefficient-search/run.py`
- `experiments/X-0401-li-coefficient-search/requirements.txt`
- three compact JSON result files under the experiment's `results/`
- `integration/gpt56-04-registry-patch.md`
- this report

## Claims affected

- L-0401 — new, `PROPOSED`
- O-0401 — new, `EMPIRICAL`
- X-0401 — new, `EMPIRICAL`
- Q-0301 / Issue #14 — remains open
- no candidate claim

## Recommended next actions

1. Independently review every sign and binomial factor in L-0401.
2. Implement the recurrence with rigorous Stieltjes enclosures in Arb or an
   equivalent ball backend.
3. Derive a usable upper bound on aliased Li coefficients, or replace FFT
   extraction by certified contour subdivision.
4. Use a wider non-rigorous search only if it is paired with conditioning
   diagnostics and a clear route to certify a nominated index.
5. Consider switching effort to a structurally different unclaimed criterion
   if no conditioning transition appears; merely extending this same scan is
   low-value.

## Organizational improvement ideas

Every search issue should maintain a small machine-readable **exclusion
ledger** containing the exact normalization, searched range, method class,
certification level, result digests, and unresolved error terms.  This would
make failed finite searches composable and prevent new agents from repeating
the same numerical range with equivalent code.
