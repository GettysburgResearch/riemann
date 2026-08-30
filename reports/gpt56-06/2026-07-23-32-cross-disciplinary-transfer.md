# Session report — Issue #32 cross-disciplinary theorem transfer

Agent: `gpt56-06`  
Date: 2026-07-23  
Branch: `agent/gpt56-06/32-cross-disciplinary-transfer`  
Issue: #32  
Status: completed research handoff; no RH counterexample candidate

## Objective

Read the repository protocol and active work, treat the existing RH literature
atlas as an exclusion map, and search distant fields for theorem shapes that
solve current bottlenecks rather than merely naming another equivalent
criterion.

## Repository sweep

The sweep covered the README, current state and open issues, plus active draft
work on:

- finite Weil matrices and carrier-shifted/multi-carrier searches;
- Robin/CA reconnaissance, exact one-integer verification, canonical
  exponent-vector reduction, and proof-producing branch-and-bound;
- Li coefficients and scale windows;
- direct contour, Speiser, and de Bruijn--Newman routes;
- the conventional literature claim atlas;
- cross-route hinge lemmas for perturbation, tails, contours, and pruning.

The main shared bottlenecks are exact finite certificates, safe global
coverage, proof-producing pruning, and independent reconstruction. Obvious RH
criteria were therefore excluded from the search target.

## Strongest connection: passive networks and positive-real interpolation

Let

\[
F(s)=\xi'(s)/\xi(s).
\]

Lagarias proved that RH is equivalent to

\[
\operatorname{Re}F(s)>0
\quad\text{for every }\operatorname{Re}s>1/2.
\]

The paper also remarks that a rotated version is a Pick function. The useful
cross-disciplinary step is to treat `F` as a passive impedance/positive-real
transfer response and make its finite data kernel explicit:

\[
K_{jk}=\frac{F(s_j)+\overline{F(s_k)}}
{s_j+\overline{s_k}-1}.
\]

Under RH, the zero expansion gives

\[
K_{jk}=\sum_\gamma
\frac1{(s_j-1/2-i\gamma)
(\overline{s_k}-1/2+i\gamma)},
\]

so every finite `K` is a Gram matrix. Two compact disproof objects follow:

1. one exact point with a rigorous `Re F<0` interval;
2. exact sample points and a fixed exact vector with a rigorous `v*Kv<0`
   interval.

The one-point route is existentially complete: every off-line zero to the
right creates an open negative region immediately to its left. Unlike a
contour certificate, the witness need not isolate or count the zero.

### Why this can move the project

- Proof cost is finite point evaluation plus one sign, not a whole contour.
- The current direct-zero route can reuse its Arb/zeta infrastructure.
- Positive-real interpolation and passivity optimization provide principled
  adaptive proposal mechanisms.
- A fixed-vector Rayleigh checker is tiny and independent of the discovery
  eigensolver.

### Correction audit

The 2005 Lagarias erratum corrects a later quantitative Lemma 3.1 and changes
the erroneous sign before `1/(s-1)` in equation (3.8) to positive. It does not
retract the foundational Theorem 1.1. D-3201 uses the corrected evaluator
formula.

## Prototype X-3201

A deterministic `mpmath` prototype validates the normalization but is
explicitly non-rigorous.

Commands:

```bash
python experiments/X-3201-xi-passivity/prototype.py --dps 80 \
  --output experiments/X-3201-xi-passivity/results/calibration.json
python -m unittest discover \
  -s experiments/X-3201-xi-passivity/tests -v
python -m py_compile \
  experiments/X-3201-xi-passivity/prototype.py \
  experiments/X-3201-xi-passivity/tests/test_prototype.py
```

Results:

- 7/7 tests passed;
- on-line synthetic `3x3` Pick minimum: about `+0.0582185316491`;
- off-line synthetic scalar at `0.55+20i`: about `-13.3332708346`;
- off-line synthetic `2x2` Pick minimum: about `-315.300391406`;
- six actual low-height scalar calibrations were positive;
- actual low-height `4x4` Pick minimum: about `+0.0925292686838`;
- calibration JSON SHA-256:
  `763c6176a0b5b478e4be5855048f0e5d50957d30eb62e5dd711a8a4a71713986`.

No high-height search and no candidate claim were made.

## Second promoted connection and route correction: thermodynamic convex envelopes for CA states

Write

\[
x_n=\log n,
\qquad y_n=\log(\sigma(n)/n).
\]

A CA state maximizing `sigma(n)/n^(1+epsilon)` is an exposed point of the upper
convex envelope of `(x_n,y_n)`; `epsilon` is its supporting slope. Consecutive
transition states at one exact event boundary lie on the same global support
line.

The deeper literature sweep also found that Robin's Proposition 1 is repeatedly
cited as proving that RH false implies infinitely many CA violations. Thus CA
search is already a complete counterexample route in the infinite sense, not
merely a heuristic subsequence. T-3201 records this imported result as
`PARTIAL` because the original 1984 pages were not obtained directly in this
session.

The logged Robin barrier is

\[
B(x)=\gamma+\log\log x,
\]

which is strictly concave. Therefore, if both contact endpoints satisfy Robin,
all integers between them satisfy Robin. This elementary convex-duality lemma
is L-3203.

The consequence for X-0201 is substantial: its route-level completeness should
be corrected, while its present finite run remains empirical. After replacing
binary64 event order with exact interval ordering and certifying endpoint signs,
the 5.7-million-event ledger can certify whole integer intervals up to its
43.43-million-digit endpoint, rather than just report a negative CA subsequence
scan.

## Transfers investigated but not promoted as theorems

### Generalized KYP and trigonometric SOS

Potentially attractive for global carrier-band certificates, but the current
prime block uses incommensurable log-prime frequencies and has no exact finite
rational state-space realization. Direct application would be unjustified.

### Loewner rational realization

Useful to propose hidden poles/nonpassive bands from samples of `xi'/xi`, but a
fitted pole has no proof value without a uniform residual enclosure. M-3201
keeps it strictly in reconnaissance.

### Certified branch-and-bound proof logging

A strong engineering transfer for Issue #25. It can certify tree coverage and
look-ahead decisions, but transcendental Robin comparisons still need separate
ball lemmas.

### Conley-index continuation

Interesting for de Bruijn--Newman flow, but no rigorous finite-dimensional
isolating reduction was found. Deferred rather than overstated.

## Files added

- `claims/definitions/D-3201-xi-positive-real-kernel.md`
- `claims/lemmas/L-3201-xi-logderivative-point-witness.md`
- `claims/lemmas/L-3202-xi-pick-matrix-witness.md`
- `claims/lemmas/L-3203-ca-support-line-interval-cover.md`
- `claims/theorems/T-3201-robin-ca-completeness.md`
- `claims/methodology/M-3201-xi-passivity-search.md`
- `claims/methodology/M-3202-ca-envelope-certification.md`
- `experiments/X-3201-xi-passivity/*`
- `literature/cross-disciplinary-transfer-ledger.md`
- `integration/gpt56-06-32-cross-disciplinary-transfer.patch.md`
- this report

## Recommended handoffs

1. Open a dedicated implementation issue for the Arb passivity producer/checker
   and coordinate it with Issue #7. Search above `3*10^12`; calibrate below.
2. Hand T-3201/L-3203/M-3202 to the X-0201 and Issue #25 owners. First obtain
   Robin's original pages 203--205, then benchmark exact contact coverage on the
   first 30 CA states before scaling.
3. Retain KYP/SOS and Conley ideas in the ledger until their missing finite
   reductions are actually proved.

## Claim discipline

- No counterexample was found.
- No universal finite verification of RH or Robin is claimed.
- The Lagarias/Hinkkanen positivity viewpoint has literature prior art; the
  repository contribution is the explicit finite Gram certificate,
  proof-producing architecture, prototype, and cross-route integration.
- Robin's CA completeness result also has prior art; L-3203 contributes a
  constructive finite adjacent-contact certificate, not a priority claim.
- Every proposed proof-grade computation remains pending independent review
  and Arb implementation.
