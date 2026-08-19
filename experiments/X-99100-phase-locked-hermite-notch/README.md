# X-99100 — Phase-locked Hermite notch exact algebra

Run:

```bash
python3 verify.py --output results/verification.json
```

Expected:

```text
PASS_T99100_PHASE_LOCKED_HERMITE_NOTCH_ALGEBRA
```

The replay verifies exact rational exponent algebra, pole preservation, safe saddle annihilation, the optimal notch order, annular localization, and the strict magnitude/pole gap at six rational values of `delta`.

It does not prove the phase-locked arithmetic cancellation `PLHAC99100` and does not establish RH.
