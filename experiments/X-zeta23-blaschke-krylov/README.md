# X-zeta23-blaschke-krylov

Exact standard-library regression for the Blaschke–Krylov finite-packet theorem.

Run:

```bash
python3 experiments/X-zeta23-blaschke-krylov/verify.py
```

The verifier uses only `fractions.Fraction`. It checks:

- the reflected inner identity and scalar \(J\)-unitarity;
- the exact Krylov reflected-pair eigenvalues;
- the minimum pair capture formula;
- the model-kernel telescoping identity;
- one eight-point finite packet;
- convergence toward the exact Szegő-Schur capture limit \(9800/81\).

The replay certifies finite algebra only. It does not certify the full
unseen-zero tail passage or RH.
