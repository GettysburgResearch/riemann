# X-27302 — Prime-incidence greedy suffix charge

This standard-library exact checker validates the finite algebra of
`L-27303`.

Run:

```bash
python verify.py --self-test --output results/exact-verification.json
```

It verifies:

- positive blocks between consecutive ordinary primes;
- exact response at both prime endpoints;
- zero response on every proper prime-power row;
- the greedy residual recursion;
- the maximum-positive-suffix closed form;
- the exterior boundary charge;
- six central and mutation tests.

Retained verdict:

```text
PASS_EXACT_PRIME_INCIDENCE_GREEDY_ALGEBRA
```

Proof-object SHA-256:

```text
b8644a8f098bba2ec275ff6646811971f3b5aebb41f6886b7e79802c14a0552b
```

This is synthetic exact algebra. It does not prove the all-scale Prime Tail
Charge theorem or RH.
