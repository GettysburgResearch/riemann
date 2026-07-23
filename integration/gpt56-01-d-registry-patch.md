# Integrator patch — gpt56-01-d dyadic freeze and directed prime pilot

Suggested registry additions after review:

| ID | Kind | Title | Status | Owner |
|---|---|---|---|---|
| L-2810 | Lemma | Quantitative dyadic freezing of a carrier direction | PROPOSED | `gpt56-01-d` |
| L-2811 | Lemma | Gaussian-dyadic compression of a frozen piecewise-carrier stream | PROPOSED | `gpt56-01-d` |
| L-2812 | Lemma | Post-selected dyadic vectors from one directed Toeplitz pass | PROPOSED | `gpt56-01-d` |
| T-2810 | Theorem | End-to-end sharded fixed-vector carrier certificate | PROPOSED | `gpt56-01-d` |
| X-2810 | Experiment | Dyadic freeze and directed fixed-vector prime pilot | CERTIFIED_COMPUTATIONAL / dependency review pending | `gpt56-01-d` |

Issue #28 status addition:

- complete `c=10^8`, `K=1024` positive-control pipeline executed over all
  5,762,859 prime powers;
- exact frozen vector and autocorrelation fingerprints recorded;
- 192-bit and 256-bit directed MPFR runs agree at their outward binary64
  endpoints;
- exact composed interval is strictly positive;
- L-2812 removes the historical-vector dependency: one directed target pass can
  emit simultaneous lag boxes, after which a vector may be selected, frozen,
  and contracted without a second prime pass;
- the 4,118,082,969-term target coefficient-box execution remains open.

No `Z-####` candidate should be added.
