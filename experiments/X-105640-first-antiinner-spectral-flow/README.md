# X-105640 — First anti-inner spectral-flow replay

This exact rational disk-model replay checks the finite algebra underlying
`L-105640--L-105642`:

```text
B(z) B(w) K_(A/B)(z,w) = K_A(z,w)-K_B(z,w);
K_(B_r) is rank one;
first anti-inner Hankel charge is attenuated by |A(r)|^2;
visible band charge + signed complement = complete charge.
```

Run:

```bash
python experiments/X-105640-first-antiinner-spectral-flow/verify.py
```

Expected verdict:

```text
PASS_X_105640_FIRST_ANTIINNER_SPECTRAL_FLOW
checks=260
```

The script computes and prints a deterministic SHA-256 proof object from its
canonical result payload. It authenticates exact finite algebra only. It does
not prove Xi descent below `beta_1`, the pointwise microscope sign, or RH.
