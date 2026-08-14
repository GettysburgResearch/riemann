# Review handoff — post-Hall complete profile and debt packet

## Intended GitHub placement

```text
repository:       gfreund123/riemann
base PR:          #462
base head:        8642e062b6c6f5a4c7d443a1ee5a6e9ecf3e4706
suggested branch: research/gpt56-pro/91682-complete-causal-profile-debt
```

The connected GitHub read surface was available, but write actions returned `Resource not found` in this runtime.  This directory and its format-patch are the exact review deposit.

## Replay

```bash
cd experiments/X-91682-post-hall-complete-profile
python3 verify.py
sha256sum -c SHA256SUMS
```

Expected aggregate digest:

```text
7cce71153cd751be8c2b20a2bd3d136e4ef926912d4e036b4b0ec3fa4c13bd42
```

## Verdict

```text
complete score causal arithmetic profile p>=67    PROVED
complete target causal arithmetic profile p>=67   PROVED
global target-normalized endpoint profile          PROVED
score and target Lorenz cutoff <2000               PROVED
proportional score debt                             ABSOLUTELY CLOSED
target-Lorenz exact target and score                PROVED
remaining physical row family                      OPEN / EXPLICIT
full unconditional closure                         NOT YET ESTABLISHED
Riemann Hypothesis                                  UNPROVED
```
