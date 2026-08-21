# Agent report — Issue #14 Li certificate reduction and scale audit

Agent: `gpt56-04`  
Issue: #14  
Branch: `agent/gpt56-04/14-negative-li-coefficient`  
Date: 2026-07-23

## Starting hypothesis

The first X-0401 session found no negative coefficient through `n=100000` and
left the Cauchy alias tail uncertified.  The Weil and Robin branches suggested a
better architecture: separate difficult analytic interval production from a
tiny exact checker.  The verified-zero branch also suggested that moderate
indices may be the wrong scale.

## Other work inspected

- PR #4: exact dyadic Rayleigh checking separated from matrix enclosure.
- PR #23: event-directed search instead of indiscriminate grid enlargement.
- PR #24: independent pure-integer/dyadic intervals, proof-producing pruning,
  and independence fingerprints.
- T-0310 in PR #21: imported rigorous line verification through height
  `3*10^12`.

## Approaches attempted

1. Derived a roots-of-unity alias identity for Cauchy extraction of `lambda_n`.
2. Added a larger-circle Cauchy bound converting the infinite alias tail into
   one explicit expression.
3. Reduced both the local recurrence and Cauchy method to a dyadic schema.
4. Implemented a standard-library exact checker using integers and
   `fractions.Fraction` only.
5. Added strict-negative, zero-touching, malformed-input, and alias-widening
   tests.
6. Combined Li-transform geometry with the verified-zero height to quantify the
   first possible individual exponential-amplification scale.
7. Added a machine-readable exclusion ledger.

## New results

### L-0402 — finite certificate reductions

For

`G(z)=d/dz log(2*xi(1/(1-z)))=sum_{m>=0} lambda_{m+1} z^m`,

and `0<r<R<1`, `0<=m<M`,

\[
D_{m,M}(r)=\lambda_{m+1}+
\sum_{\ell\ge1}\lambda_{m+\ell M+1}r^{\ell M}.
\]

If `|G(z)|<=B` on `|z|=R`, then

\[
|D_{m,M}(r)-\lambda_{m+1}|
\le \frac{B}{R^m}\frac{(r/R)^M}{1-(r/R)^M}.
\]

The lemma also records exact interval aggregation for L-0401's finite local
recurrence.  Status: `PROPOSED`.

### Exact dyadic checker

`verify_dyadic_certificate.py` supports local and Cauchy–DFT certificates.  It
performs no special-function or floating-point operation and succeeds only if
the final exact rational upper endpoint is negative.

Ten tests pass.  In the synthetic Cauchy control with `n=2`, `M=4`, `r=1/2`,
`R=3/4`, and `B=1/128`, the alias radius is exactly `1/390`.  A strict synthetic
negative is accepted; a smaller apparent negative is widened through zero and
rejected.

Classification: exact algebraic tests only.  No analytic Li interval was
supplied.

### L-0403 — verified-height amplification barrier

For a hypothetical left-of-line zero at height at least `T`,

\[
|1-1/\rho|^n<\exp(n/(2T^2)).
\]

An individual transformed zero therefore cannot gain an `e`-fold modulus
amplification before `n>2T^2`.  Using imported height `T=3*10^12`, the scale is

`18,000,000,000,000,000,000,000,000`.

The prior `n=100000` scan is smaller by a factor `1.8*10^20`.  This is not a
positivity theorem, but it shows that merely extending the same linear scan a
few orders of magnitude is strategically weak.  Status: `PROPOSED`.

## Candidate counterexamples

None.  No actual Li coefficient interval was proved negative and no `Z-####`
identifier was allocated.

## Certified computations

No analytic special-function computation was certified.  Exact results are
limited to rational propagation inside the checker and its synthetic tests.

## Failed or blocked approaches

- Arb/python-flint remains unavailable in the execution environment.
- A sampled maximum of `|G|` cannot certify the outer-circle supremum `B`.
- Ordinary FFT residuals cannot certify the exact DFT.
- The height barrier makes a modestly larger brute-force coefficient scan a
  poor next move.

## Potential errors and adversarial targets

- Check the `m` versus `lambda_{m+1}` shift.
- Check the factor `B/R^m`, the first geometric-tail exponent, and denominator.
- Verify analyticity on the full outer disk, not only at samples.
- Audit the reciprocal reflected-zero transform in L-0403.
- Do not turn the individual-modulus bound into a claim about the complete
  symmetrically ordered zero sum.
- Keep every synthetic certificate visibly classified as synthetic.

## Files changed

- `claims/lemmas/L-0402-li-finite-certificate-reductions.md`
- `claims/lemmas/L-0403-li-verified-height-amplification-barrier.md`
- `experiments/X-0401-li-coefficient-search/verify_dyadic_certificate.py`
- `experiments/X-0401-li-coefficient-search/tests/test_verify_dyadic_certificate.py`
- four synthetic certificate JSON files
- `results/verifier-tests.txt`
- `results/exclusion-ledger.json`
- updated X-0401 README and integrator patch
- this report

## Claims affected

- L-0401 — unchanged, `PROPOSED`
- L-0402 — new, `PROPOSED`
- L-0403 — new, `PROPOSED`
- O-0401 — unchanged, `EMPIRICAL`
- X-0401 — extended with an exact checker; search remains `EMPIRICAL`
- Q-0301 / Issue #14 — remains open
- no candidate claim

## Recommended next actions

1. Independently rederive L-0402.
2. Build an Arb or separate rigorous producer for `riemann.li-dyadic.v1`.
3. Certify an outer-circle supremum by interval subdivision plus derivative
   bounds.
4. Produce local and Cauchy certificates for the same small positive coefficient
   as an end-to-end calibration.
5. Target the `O(T^-2)` radial and `O(T^-1)` angular neighborhood of `z=1`
   through rigorous Padé, contour, or moment reconstruction.
6. Investigate arithmetic formulas for selected enormous indices.

## Organizational improvement ideas

- Ship an exact checker before a candidate exists, with strict and zero-touching
  synthetic tests.
- Maintain machine-readable exclusion ledgers separating empirical searches,
  rigorous exclusions, exact-checker coverage, and strategic barriers.
- Require independence fingerprints for claimed reproductions.
