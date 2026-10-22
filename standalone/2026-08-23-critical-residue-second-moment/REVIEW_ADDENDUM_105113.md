# Review addendum — L/T/R/M-105113 buffered-selector shell averaging

Checkpoint base:
53c3a24b23335e7b4e77a703b2c3c224821ed749.

## What changed

A complete outer actual-pole manifest is used to construct selectors whose
target jets are confined to a fixed inner core.  All buffer events are
canceled to full actual order.  This freezes both residue charges across
all raw-regular intermediate rectangles and supports an exact signed
two-parameter shell average.

The associated Tonelli mean supplies a common good rectangle only after a
nonnegative weight pair is prescribed.  The quantifiers are

\[
\text{for every prescribed }(\lambda_1,\lambda_2),
\quad\text{there exists a common rectangle},
\]

not the existence of one universal rectangle for all weights.

## Hostile checks

- Require the complete outer actual-pole manifest, not a core-only list.
- Verify full zero congruences at all outer nontargets.
- Keep \(q_H\) unnormalized and retain both \(2\pi\) factors.
- Keep \(+i\operatorname{sgn}(x)\) vertically and
  \(-\operatorname{sgn}(y)\) horizontally.
- Pair the vertical shell with \(1/\Delta_T\) and the horizontal shell
  with \(1/\Delta_\eta\).
- Form one aggregate nonnegative cost for each prescribed weight pair.
- Retain the complete product costs of both weighted carriers.
- Verify all cubic residues, raw charge jumps, selector congruences, and
  canceled-carrier identities exactly.
- Reject any inference from finite shell integrability to a cofinal Xi
  estimate.
- Confirm that Xi manifest authentication, signed first-moment growth,
  RCMV104530, and RH remain open.

Exact replay:

    python -B experiments/X-105113-buffered-selector-shell-average/tests/test_verify.py
    python -B -O experiments/X-105113-buffered-selector-shell-average/tests/test_verify.py

Expected:

    PASS_T105113_BUFFERED_SELECTOR_SHELL_AVERAGE
    18 / 18
    44e0cffca9d4d680555287e8290cfa645d979dc76b064f0ab6914ace88c7d560

The finite shell identity is exact.  The cofinal Xi shell estimate and all
later programme gates are not supplied by this packet.
