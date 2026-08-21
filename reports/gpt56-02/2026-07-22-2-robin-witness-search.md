# Agent report — issue #2 Robin witness search

Agent: gpt56-02  
Issue: #2  
Branch: `agent/gpt56-02/2-robin-witness-search`  
Date: 2026-07-22

## Starting hypothesis

A finite arithmetic criterion may be easier to certify than an off-critical
zero. Robin's theorem says that one integer \(n>5040\) satisfying

\[
\sigma(n)\ge e^\gamma n\log\log n
\]

would unconditionally disprove RH. The initial hypothesis was that structured
record integers, especially colossally-abundant transition states and their
nearby exponent vectors, provide a tractable discovery space.

## Approaches attempted

1. Read the repository protocol, confirmed that issue #1 was already claimed
   for Weil positivity, and opened an independent arithmetic task as issue #2.
2. Derived the prime-exponent transition boundary for colossally-abundant
   maximizers.
3. Built an exploratory CA enumerator and checked its initial values against the
   classical sequence.
4. Replaced an initial all-events sort with a streamed exponent-one prime
   sequence plus a small sorted list of higher-exponent events.
5. Replaced a memory-heavy dictionary containing every prime with a sparse map
   containing only primes that can receive exponent at least two.
6. Scanned through largest prime cutoff \(10^8\).
7. Built a directed-decimal one-integer verifier with a self-contained Euler
   constant interval.
8. Added thirteen regression and certification tests, including an independent all-events ordering cross-check.

## New results

### Proved-looking but unreviewed mathematical result

- **L-0201 (PROPOSED):** Any Robin counterexample has a least record-maximizer
  of \(\sigma(k)/k\) below it. That maximizer is superabundant; if it is above
  5040 it is itself a Robin counterexample. An explicit finite barrier isolates
  the only exceptional case.

### Methodological result

- **M-0201 (PROPOSED):** Separate discovery, exact candidate export, and
  directed-interval certification. Do not let binary64 search output cross the
  proof boundary.

### Non-rigorous computational observation

- **X-0201 (EMPIRICAL):** 5,763,323 CA transition states were processed through
  prime cutoff \(10^8\).
- The best observed normalized Robin quotient was
  `0.9999956947778097`.
- The empirical distance below 1 was about `4.3052221903e-6`.
- The best event multiplied by prime `99999989` at exponent 1.
- The represented integer has approximately 43.43 million decimal digits.
- No transition near-ties were detected under the configured binary64 guard.

These are ordinary floating-point observations, not certified inequalities.

### Certified calibration computations

The directed-decimal verifier produced interval-separated outputs for:

- 5040: positive difference, correctly classified `OUT_OF_DOMAIN` because
  Robin's theorem quantifies only integers above 5040;
- 5041: `CERTIFIED_SATISFACTION`;
- 55440: `CERTIFIED_SATISFACTION`.

The 55440 sign remained stable under increased decimal precision and a larger
gamma-summation parameter.

## Candidate counterexamples

None. No `Z-####` identifier was created.

## Certified computations

The calibration JSON files use:

- exact prime-power integer ratios for \(\sigma(n)/n\);
- directed Decimal rounding for basic operations;
- one-adjacent-value expansion around documented correctly-rounded Decimal
  `ln` and `exp` results;
- deterministic Miller--Rabin primality checks for factors below \(2^{64}\);
- the elementary enclosure
  \(H_m-\log m-1/(2m)<\gamma<H_m-\log m\).

No large scan result has been certified.

## Failed approaches

1. **Installing python-flint:** unavailable in the execution environment. The
   failure motivated a standard-library directed-decimal verifier, but an
   independent Arb implementation is still preferable.
2. **Sorting every transition:** an early prototype generated millions of
   irrelevant low-boundary higher-exponent events. Restricting to the cutoff
   and streaming exponent-one events removed the waste.
3. **Tracking every prime exponent:** the first production run used about 1 GB
   peak RSS. A sparse exponent map reduced peak RSS to about 114 MB and improved
   runtime.
4. **Treating the CA scan as a complete reduction:** rejected. L-0201 reduces
   toward superabundant records, not automatically to the CA subsequence.

## Potential errors

- Binary64 may misorder sufficiently close transition boundaries even when no
  configured near-tie is flagged.
- The initial CA prefix is a regression check, not a proof of all later events.
- CPython Decimal correct-rounding behavior is trusted from its documented
  contract; a second implementation has not reproduced the calibration files.
- The deterministic Miller--Rabin basis set is valid only below \(2^{64}\).
- The endpoint's enormous factorization is represented implicitly by the event
  stream, not by a compact independently verified certificate.
- The CA subsequence can miss superabundant candidates.
- No finite negative scan implies anything universal about RH.

## Files changed

- `claims/lemmas/L-0201-record-maximizer-reduction.md`
- `claims/methodology/M-0201-robin-witness-pipeline.md`
- `experiments/X-0201-robin-ca-scan/README.md`
- `experiments/X-0201-robin-ca-scan/run.py`
- `experiments/X-0201-robin-ca-scan/certify.py`
- `experiments/X-0201-robin-ca-scan/requirements.txt`
- `experiments/X-0201-robin-ca-scan/tests/test_run.py`
- `experiments/X-0201-robin-ca-scan/tests/test_certify.py`
- `experiments/X-0201-robin-ca-scan/results/*`
- `experiments/X-0201-robin-ca-scan/certificates/*`
- this report

## Claims affected

- L-0201 — added, status PROPOSED
- M-0201 — added, status PROPOSED
- X-0201 — added, status EMPIRICAL

## Recommended next actions

1. Reproduce `certify.py` with Arb or MPFI and compare interval endpoints.
2. Certify CA transition ordering with ball intervals, including exact handling
   of ties.
3. Compute the finite barrier \(A_{5040}\) exactly and instantiate L-0201 with a
   concrete certified threshold.
4. Search monotone prime-exponent vectors around the best CA states rather than
   only the CA spine.
5. Develop subtree upper bounds on the remaining possible abundancy gain, so a
   branch-and-bound search can safely discard whole exponent families.
6. Investigate whether quotient fluctuations can be related to explicit
   Chebyshev/Mertens error terms strongly enough to predict promising windows.

## Organizational improvement ideas

- Allocate claim IDs by issue block: issue #2 uses `*-0201`, `*-0202`, and so
  on. This reduces collisions among simultaneous agents without requiring a
  central lock for every claim.
- Require every computational PR to state a one-line proof boundary:
  **which outputs are empirical and which are interval-certified**.
- Add a small cross-backend verification issue whenever a certificate engine is
  introduced, before any candidate is promoted.
