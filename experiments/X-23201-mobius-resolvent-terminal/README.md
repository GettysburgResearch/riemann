# X-23201 — Möbius resolvent and terminal-adapter exact regression

This standard-library experiment checks only the finite algebra used by the
Issue #232 proposal.

It verifies:

1. the exact finite Möbius resolvent identity through a declared endpoint;
2. support of the residual strictly above the truncated Möbius cutoff;
3. exact inversion of geometric Mertens differences of orders 1 through 5;
4. one finite positive-Hankel terminal domination and Selberg forcing ledger;
5. one exact finite complexity-DAG elimination;
6. deterministic proof-object hashing.

Run:

```text
python3 verify.py
python3 -m unittest discover -s tests -v
```

Retained proof-object SHA-256:

```text
611f6dcf0dc450e58209b078cf0596d634d8d01b4ccb58f28e57d16085aa1911
```

Classification:

```text
EXACT_SYNTHETIC_PROPOSAL_REGRESSION
```

The experiment does not evaluate zeta, primes, a production Selberg packet, the
terminal certificate `STC(K)`, or RH.
