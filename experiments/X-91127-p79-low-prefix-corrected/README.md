# X-91127 — Corrected exact `P_79` low-prefix Hall replay

This checker is the proof object for `L-91350`.

It fixes the proof-engineering defect recorded in `R-91308`: a global convex
minimum is never inserted unless its vertex lies in the active cell.  Instead,
the checker proves the convex-cell derivative has one sign throughout every
activation cell.

Replay:

```bash
python3 verify.py
```

Retained local replay:

```text
PASS_P79_LOW_PREFIX_CORRECTED_CELL_DERIVATIVE
383472 directed interval checks
target Hall margin > 1
score Hall margin  > 1
```

The actual directed minima are above `4.31` and `5.27`, respectively.

Scope: separate target and score Hall feasibility.  A common transport, source
row typing and RH are not certified by this checker.
