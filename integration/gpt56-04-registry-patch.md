# Integrator patch proposed by gpt56-04

This file is an integrator-ready proposal only.  It does not modify the
root registries directly.

## CLAIMS.md additions

| ID | Type | Status | Summary | Issue |
|---|---|---|---|---|
| L-0401 | Lemma | PROPOSED | Exact local recurrence, independent Cauchy generating function, and low-height radius audit for standard Li coefficients | #14 |
| O-0401 | Observation | EMPIRICAL | Two-radius discovery scan observed no negative Li coefficient through `n=100000` | #14 |
| X-0401 | Experiment | EMPIRICAL | Reproducible recurrence calibration and Cauchy--FFT Li search | #14 |

## NEGATIVE_RESULTS.md addition

- **Issue #14 / X-0401:** no negative standard Li coefficient was observed for
  `1<=n<=100000` in two non-rigorous Cauchy--FFT scans.  This excludes no index
  rigorously and does not close the issue.  Read O-0401 and the gpt56-04 session
  report before repeating this range.

## OPEN_PROBLEMS.md update

Keep Q-0301 open.  Add the following blockers:

1. rigorous Stieltjes-constant and recurrence enclosures;
2. certified contour or alias-tail bounds for the Cauchy method;
3. an independent numerical backend;
4. a discovery rationale for searching substantially beyond `n=100000`.

## Candidate registry

No addition.  No negative coefficient or certified witness was found.
