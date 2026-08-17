# X-97400 independent reconstruction

Run:

```bash
python3 verify.py --output results/verification.json
```

The executable uses exact rational arithmetic for the coefficient, parity, scalar-tradeoff, Lorenz primal/dual, and Mellin-numerator identities. It also checks the certified odd-history target gap and hostile mutations.

It does **not** prove the uniform completed-parity Lorenz inequality `CPSL67`, replay the full 51-million-event MPFR terminal campaign, Landau's theorem, or RH.
