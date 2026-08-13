# X-91131 — Nonduplicating causal-packet budget

Companion replay for `L-91355`.

```bash
python3 experiments/X-91131-nonduplicating-causal-packet-budget/verify.py
```

Expected verdict:

```text
PASS_NONDUPLICATING_CAUSAL_PACKET_BUDGET
```

The standard-library checker uses exact `Fraction` arithmetic to verify representative finite sequences of rough-scale parameters. It checks:

- the constant-mode survival/hazard telescope;
- the exact identity `survival + sum(lambda_j) = 1`;
- the safe-child inequalities `alpha_j <= h_j^X,h_j^Y`;
- the causal packet coefficient relation `alpha_j = r_j lambda_j`;
- the child-mass bound `sum(alpha_j) <= r_1 sum(lambda_j) < 1/8`.

The universal theorem is symbolic; the replay is a regression check, not a finite proof of physical packet typing or RH.
