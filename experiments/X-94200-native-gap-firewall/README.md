# X-94200 — Native-gap normalization firewall

Run:

```bash
python3 verify.py --output results/verification.json
python3 tests/test_verify.py
```

The replay checks:

- the finite radix-four adjoint exactly over `Fraction`;
- the elementary \(X=3\) counterexample using rational inequalities;
- a 100-digit direct evaluation of \(J_\Lambda(3),P_\Lambda(3),F_\Lambda(3)\);
- the corrected three-term decomposition;
- eight hostile mutations.

It does not estimate the large-divisor Möbius tail and does not establish RH.
