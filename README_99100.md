# T99100 — Discounted literal-score debt supermartingale

This add-only hostile successor to PR #620 replaces its fragile distinguished
`X/(d 67^j)` score path by a typed Bellman argument on the actual branching
factor-67 source tree.

The central observation is that **only normalized alpha-children recurse**.
The exact target-mass identity splits each packet into current-owned mass and
recursive child mass. If the terminal literal-score shortfall is bounded by
`D0` per unit target mass, then the function

```text
B(packet) = D0 * target_mass(packet)
```

is a superharmonic debt envelope. Branch count, varying rough primes, and
history depth cannot amplify it.

For the fixed `P_61` root ledger the directed bound is

```text
D0 * product_(p<=61)(1+p^(-1/2))
  < 3534.675221310728
  < 3600.
```

This closes the **all-depth score-debt interface** of PR #620, conditional on
its local typed identities and terminal unit-debt bound. It does not validate
its compact Hall campaign, equality endpoint measure, all-column estimate, or
Mellin–Landau consumer. RH remains unproved.

Replay:

```bash
python3 experiments/X-99100-score-debt/verify.py
```

Expected:

```text
PASS_T99100_DISCOUNTED_SCORE_DEBT_SUPERMARTINGALE
553024df67144d7027a7675c31238e8b090d4368c51acecf8701de682fb5ce4c
```
