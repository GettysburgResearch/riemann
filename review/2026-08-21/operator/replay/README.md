# Reviewer B light exact replays

These replays authenticate only small symbolic or rational identities used in the review. They intentionally do **not** rerun the external zeta-zero verification, Brownian campaigns, Q4 endpoint scans, large matrix searches, MPFR sweeps, or any other heavy computation.

Run:

```bash
cd review/2026-08-21/operator/replay
python3 run_all.py
```

Expected terminal verdict:

```text
PASS_REVIEWER_B_ALL_LIGHT_REPLAYS
```

The generated `verification.json` and per-script JSON files are retained as review evidence. The analytic arguments, external-input legality, quantifier checks, and first-broken-arrow classifications are recorded in the parent review files; a passing replay never upgrades an open or RH-equivalent theorem.
