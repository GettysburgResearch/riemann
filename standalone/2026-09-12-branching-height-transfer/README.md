# BHT26: unbounded-height transfer is not unbounded-height confinement

**Proposed component proofs; independent analytic review required. RH is not proved.**

The user requested extension of the permanently protected height-30 window to
unbounded heights. This attempt obtains an explicit unbounded-height TRANSFER
result, but does not establish the missing critical-line location of the
reference clusters. Read [PROOF.md](PROOF.md) Sections 1, 4–6 first.

For every integer `N >= 2^18`, set

```
ell = ceil(log_2(N+12))
k   = floor(N/(500 ell))
eps = 2^(-k)
```

For every later branching depth `m >= N`, all zeros of the literal `H_m` in
`0 <= Re(s) <= 1, |Im(s)| <= N` are within `eps` of actual xi zeros. Small
clusters have complete matching multiplicities and diameter at most
`96 log(N+12) eps`. The source error and the minimum-modulus comparison both
have proved height dependence; no unknown derivative lower bound or simplicity
premise enters. All real convex interpolations of these functions and xi obey
the same cluster counts.

These are clusters around the **actual entire zero set**, not a supplied list
of critical-line zeros. No new contour census, numerical xi value, or reference
cluster was computed. The exact line-confined window remains the parent's
height 30 at all depths at least 32. The new result would turn RH into explicit
shrinking-width confinement, but does not establish RH.

## Contents

- [PROOF.md](PROOF.md): widened source error, explicit Euler/Jensen/Binet
  lower bound, all-N comparison, complete cluster argument, and exact
  location of the failed finishing step.
- [REVIEW.md](REVIEW.md): load-bearing analytic checks and exclusions.
- [SOURCES.json](SOURCES.json): frozen parent and primary classical references.
- [VALIDATION.md](VALIDATION.md): bounded checks actually performed.
- `check.py`, `test_check.py`, `result.json`, `SHA256SUMS`: standard-library
  exact controls, not machine verification of an infinite theorem.

```
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
python -I -S -B test_check.py
python -I -S -B -O test_check.py
```

The checker uses integers/Fractions and complete rational series remainders
only for a printed comparison-speed interval. It evaluates no actual zero.
The ten real CLI refusal cases per test run are bounded implementation tests,
not independent analytical acceptance. No parent quadrature or repository-wide
validator is run by these commands.

Proposed publication is an add-only branch from PR #870 at
`ee7f76736c235714496526f999e028d181302b56`. The authoring session has NOT pushed
this continuation. The delivered publication handoff records the access limit.
