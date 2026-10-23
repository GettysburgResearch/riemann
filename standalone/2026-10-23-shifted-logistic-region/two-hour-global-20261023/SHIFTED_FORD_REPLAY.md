# Shifted detector: author replay receipt

23 October 2026. This is an author/coauthor check, not an independent
mathematical certification. The root and type agents separately review
the analytic interfaces. No human review is claimed.

Frozen inputs:

- `SHIFTED_CENTER_FORD_DETECTOR.md`:
  `a25dc862eb72cf29a4dc14b9d3dc71f15dce32cf89416106b1dd6a2e7012c024`.
- `verify_shifted_ford.py`:
  `d8093aceece06c1f0b6314b571559cdd523eb3826887a357311ab60774b8cb9f`.
- The imported rational kernel/moment engine `verify_general_ford.py`:
  `da64b1b653dfb771773efc530e2ffbe605f665f835251e578891f888c89cfa27`.

The checker passed both ordinary Python and `python -O`. The resulting
JSON files are byte-identical. Its explicit `require` calls remain
active under optimization. All transcendental acceptance decisions
use rational Taylor or logarithm bounds with outward rounding.

For R=118/25=4.72 and log t=52 the certified scalar lower bound is
greater than0.0002948890299043245. Section7 of the analytic note proves
the reduction from this endpoint to every log t>=52 and every
0<B<=25/118. Other displayed endpoints are high-height results only;
their presence in the JSON does not assert that their complementary
low-height rectangles hold. In particular the R=4.70 endpoint alone
does not establish a global R=4.70 region.

The replay also verifies the kernel curvature and cubic remainder,
the real archimedean gain, the explicit-formula integral bound, the
minimum-window enclosure, and elementary constants in the tail
monotonicity. Two deliberately unsupported endpoints are rejected.

The separate Euler-product hypotheses C(lambda)<.9 and
-zeta'/zeta(1.48)<2 are supplied by the root's
`../two-hour-root-20261023/SHIFTED_EULER_BOUNDS.md` and exact checker
SHA `aa9f8bc15a384712d14eb6037837769c3b82ecc8d8dc2ef023985c2a688d01bc`.
I independently read that checker and its analytic tails: the sieve
enumerates all prime powers through10000, the exponent in C's tail
is2-3lambda, and the denominator is bounded at10001. The logarithmic
majorant decreases throughout the integrated tail. No mismatch in
the finite/continuous split or monotonic lambda endpoint was found.
That reading is an independent review of the Euler component;
the present receipt does not claim an additional independent replay
of its1280-term calculation.

The imported explicit formula, corrected Ford detector, Revers bound,
finite zero verification, and minimum-attainment argument are analytic
dependencies, not conclusions of these finite checks. A global result
also requires the complementary low rectangle and an assembly review.
This receipt proves neither RH nor a world-record priority claim.
