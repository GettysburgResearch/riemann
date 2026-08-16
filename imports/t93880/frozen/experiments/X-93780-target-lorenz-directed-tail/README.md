# X-93780 — Directed hardening of the PR #497 Target-Lorenz tail

This experiment replaces PR #497's unprotected extended-`long double` tail
values by hardware-directed interval enclosures while preserving its exact
unsigned-128-bit event order and analytic envelope.

## Quick replay

```bash
python3 verify.py --output /tmp/x93780.json
```

Quick mode re-proves the zeta primitives, rebuilds and reruns the extremal row
66, audits the retained all-row directed proof object, checks the exact
compact/tail join and runs hostile mutations.

## Full replay

```bash
python3 verify.py --full --workers 4 --output /tmp/x93780-full.json
```

Full mode independently reruns all 65 rows and all `51,118,080` event records.
It requires a C++17 compiler, Boost.Numeric.Interval and working hardware fenv
rounding. Compilation uses `-frounding-math -fno-fast-math`.

Expected verdict:

```text
PASS_TARGET_LORENZ_DIRECTED_TAIL_HARDENING
```

The replay does not independently reproduce the frozen compact campaign or
establish RH.
