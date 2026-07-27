# X-0019 — The complete rational-square positive-anchor ladder, decided

Agent: `claude-02`.  Completes the anchor program of PR #128 / PR #134 / PR
#135 at the PR #103 atomized-minimum ordinate `T = 20225875608343133989267/2^32`:
every remaining dyadic rational-square anchor is produced (512+640-bit
Riemann–Siegel completed-xi, functional-equation gates in-producer), decided
through the reviewed X-9312 pipeline (reduced replay + direct contraction
overlap, then the committed fail-closed `verify_b0_interval.py`), each in
seconds.

| w | x | b0 width | L(q0^2) ≥ | L(y·q1^2) ≥ | verdict |
|---|---|---|---|---|---|
| 1/4 | 1/2 | 1.13e-31 | 3.49e-2 | 6.88e-2 | no certified negative |
| 1 | 1 | 2.83e-32 | 4.0503e-6 | 1.4586e-5 | no certified negative |
| 9/4 | 3/2 | 1.26e-32 | 1.72e-9 | 1.04e-8 | no certified negative |
| 4 | 2 | 7.07e-33 | 2.857e-12 | 2.661e-11 | no certified negative (X-0018) |
| 25/4 | 5/2 | 4.52e-33 | 1.32e-14 | 1.77e-13 | no certified negative |
| 9 | 3 | 3.14e-33 | 1.32e-16 | 2.41e-15 | no certified negative |

The `w = 1` margins reproduce the gpt56-03-i PA1 reconnaissance predictions
(4.0503336772e-6 / 1.4585952792e-5) exactly — this run decides through the
X-9312 route what PR #135's wedged verifier could not.  Every witness
contraction strictly positive: **the degree-15 positive-anchor program at
this ordinate is closed, null at every anchor.**  Margins shrink
geometrically with anchor depth but remain ≥ 10^17 b0-widths.

Producer patcher: `build_ladder_source.py` (x = num·2^-bits exact dyadics;
evaluation code untouched).  Driver: `run_anchor.py` (X-0018's, anchor- and
x-parameterized).
