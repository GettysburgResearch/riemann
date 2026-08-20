# X-100100 — Two-route synthesis replay

Run:

```bash
python3 experiments/X-100100-two-route-synthesis/verify.py
```

The replay checks finite geometric completion through order eight, both
critical-carrier Harnack inequalities across activation cells, the monotone
completion-corridor diagnostics, and sample zero-free multipliers.

Expected:

```text
PASS_T100100_TWO_ROUTE_CLOSURE_SYNTHESIS
```

The result is fail-closed:

```text
dce100100_proved  = false
qpet100101_proved = false
rh_established    = false
```

It authenticates finite algebra and diagnostics only.  It does not prove the
PNT asymptotics, either producer gate, or RH.
