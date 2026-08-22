# Light replay

These scripts validate packet structure and exact small fixtures only. They do
not run high-zero verification, broad scans, MPFR campaigns, matrix searches,
prime searches, Nyström sweeps, or full Lean builds.

Run:

```bash
python3 validate_packet.py
python3 light_fraction_fixtures.py
python3 cross_review_followup_fixtures.py
python3 validate_pass1.py
```

The cross-review fixture checks the fixed 5:3 factorization, PR #383
periodized-carry and fourteen-row identities, PR #386 finite energy expansion,
the PR #439 packet budget, the PR #540 divisor recursion, Y4-zero and Volterra
fixtures, same-row score locking, and the retained heavy-record schema. It does
not authenticate any heavy campaign or prove a terminal RH-bearing estimate.

The pass-one validator checks exact metadata recovery for PRs #399–#499, the #417 no-object record, 171 issue dispositions, the 67-row pass-two queue, and the fail-closed issue-to-theorem firewall.

## Final pass

`validate_final.py` is the normative final-pass check. It requires zero
`TARGETED_REVIEW_STILL_REQUIRED` rows, exact 40-hex heads for every actual PR,
and exactly one blank no-object sequence record (#417). `validate_pass1.py`
now validates the historical pass-one artifacts rather than requiring the
current census to remain in its intermediate state.
