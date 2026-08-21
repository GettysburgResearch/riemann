# X-27901 — Cycle-dual rigidity exact regression

This standard-library experiment replays the finite algebra attached to
`L-27901`, `L-27902`, and `R-27901`.

It verifies:

- the scaled `q=2` floor atom has exactly the `q=2` carry defect on every tested
  balanced split;
- its capacity defect and dyadic curvature alternate forever, rejecting a
  generic monotone/completely-monotone inference;
- for exact rational target controls, every floor atom pairs with the target
  divergence exactly as claimed, and its sawtooth defect has the opposite sign.

Run:

```bash
python experiments/X-27901-cycle-dual-rigidity/verify.py
```

Retained classification:

```text
EXACT_CYCLE_DUAL_RIGIDITY_MUTATIONS_VERIFIED
```

Proof-object SHA-256:

```text
20575c92c63194adfb31a1beca9c45fdfc1456e92f76cd09b975cf71fcf05c49
```

The experiment does **not** prove that every global dual is floor-atomic. It
does not prove DCD, Cycle Debt, WSTS, RH, or any cofinal asymptotic theorem.
