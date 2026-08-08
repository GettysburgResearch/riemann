# X-26801 — Final consolidation firewalls

This standard-library-only checker validates the exact finite claims used in
`R-26801`:

1. the positive inverse/source convolution
   \[
   a_\omega*\omega_2=\varepsilon
   \]
   through `n=128`;
2. two source-sibling mutations are rejected;
3. the rational and integer inequalities proving
   \[
   \widetilde{\mathcal R}_\omega(4)<0.
   \]

Run:

```bash
python experiments/X-26801-final-consolidation/verify.py
```

Expected verdict:

```text
EXACT_FINAL_CONSOLIDATION_FIREWALLS_VERIFIED
```

This checker does **not** prove Bottom-Charge Positivity, F5PBT, the Landau
analytic transfer, or RH.
