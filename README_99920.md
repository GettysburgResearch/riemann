# T-99920 — Native priority-Hasse surface reduction

This add-only successor to PR #667 republishes the priority-Hasse idea under the corrected normalized-box source.

The old attempted publication was not on GitHub and used an already occupied PR number.  More importantly, PRs #665/#667 made the binding normalization explicit:

```text
normalized box coefficient: beta(n)/n
native prime activity:       1/p
67 source:                    two labelled activity-1/67 vertices
```

The packet proves an exact global odd-to-even flow on the complete weighted Euler cube, truncates it by the physical activation potential, and bounds every Hasse min-cut by one explicit first-owner upward surface flux.  It also proves the exact Poisson coefficient-tail identity.

The sole open theorem is `UPBF67`, a subpower logarithmic estimate for that native surface flux.  `UPBF67 -> RH`, but neither `UPBF67` nor RH is proved here.

Replay:

```bash
bash experiments/X-99920-native-priority-hasse/replay.sh
```

Expected:

```text
PASS_T99920_NATIVE_PRIORITY_HASSE_SURFACE_REDUCTION
e112c829971ba9f25cdddab7d71edce17aa75a1a87071a7289ef0bf7b83ee208
```
