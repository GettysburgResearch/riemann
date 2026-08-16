# X-94120 projective native–Lorenz replay

The experiment regenerates the complete `X=536` squarefree/source registry,
checks an exact finite source-only stopping/causal commuting square, the causal budget on the live `X=536` and `(67,13)` scales, locks
the four 94020 proof objects, retains the exact q=2 negative-child obstruction,
and rejects every operation that would expose it branchwise.

It deliberately does not rerun PR #508's 51,118,080-event directed tail sweep.
The imported directed margins are theorem dependencies and remain separately
replayable at the frozen PR #508 head.

```bash
python3 projective_gluing.py --output results/projective_certificate.json
python3 verify.py --mutations --output results/verification.json
python3 -m unittest discover -s tests -v
```
