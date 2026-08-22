# Light replay

These scripts validate packet structure and exact small fixtures only. They do
not run high-zero verification, broad scans, MPFR campaigns, matrix searches,
prime searches, Nyström sweeps, or full Lean builds.

Run:

```bash
python3 validate_packet.py
python3 light_fraction_fixtures.py
python3 cross_review_followup_fixtures.py
```

The cross-review fixture checks the fixed 5:3 factorization, PR #383
periodized-carry and fourteen-row identities, PR #386 finite energy expansion,
the PR #439 packet budget, the PR #540 divisor recursion, Y4-zero and Volterra
fixtures, same-row score locking, and the retained heavy-record schema. It does
not authenticate any heavy campaign or prove a terminal RH-bearing estimate.
