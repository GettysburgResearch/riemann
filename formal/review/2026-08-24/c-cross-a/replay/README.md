# Replay

`run_requested_build.sh` requires a full Git checkout containing the frozen target `92f70a3b49b9295b5efb88491107670065b03317` and a networked Lean/Lake environment. It creates a detached worktree and executes the exact command sequence requested by the cross-review.

`check_static_target.py REPO` performs the fail-closed source audit against the same SHA. It is expected to **pass by detecting** the published build blocker and normalization omissions; it does not assert that the target builds.

`verify_packet.py` validates the review artifact schema and final fail-closed classification.

Observed in this review environment:

```text
exact target metadata read: PASS
static missing-declaration blocker: FOUND
full Lake build: no authoritative run available; statically blocked
RH proved: false
```
