# Critical-line entropy: direct upper-bound attempt

Status: PROPOSED COMPONENT PROOFS; the full RH proof was not obtained.
Scope: the exact ordinary-prime completion from PR811, every real X>=2,
and the entire Cauchy-weighted frequency line. Independent review pending.
Parent: b6635a70a75b60050177d5cde67e911093698664.
What was run: bounded exact/rational-interval checks; see VALIDATION.md.
Smallest remaining gap: the source-specific subpower upper bound for W(X).

[PROOF.md](PROOF.md) proves an exact nonlinear work identity and

    |2 E_(1/2)(X)-W(X)| < 8+24 log(1+log X).

All higher prime powers and convex jump remainders are paid by the stated
log-log budget. The still-unproved signed work has bounded, predetermined
feedback tanh(log|A_(x-)|); it is not a selected test or a random-prime model.
This is a component upper bound for the remainder, NOT an upper bound for W.

[ATTEMPT.md](ATTEMPT.md) shows why the proposed independent-phase completion
fails: analytic moments agree with independent prime Poisson laws, but mixed
moments do not. There is no uniform PSD domination in either direction.
The exact actual-prime 2/3 covariance is 1/4.

The parent zero-detection implication is inherited at its frozen source.
Neither RH nor a new unconditional zero-free strip is proved. The conditional
RH deduction is written out only after an explicitly OPEN work bound.
No source or metric is changed to make that bound hold.

Read PROOF, ATTEMPT, CLAIMS, SOURCES and VALIDATION in that order.
The code uses Python's standard library. Run `python checks.py` or
`python checks.py --check checks.normal.json`; also test with `python -O`.
`python validate.py` authenticates this packet's listed file bytes, not the
analytic truth of its infinite theorems or external Git history.
