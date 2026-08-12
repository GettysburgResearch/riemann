# X-91414 — Parity-domain-wall CPPD replay

This finite regression supports `L-91414`, `L-91415`, `R-91406`, and the
normal-form bookkeeping of `T-91403`.

It checks:

- the fully polarized Hadamard identity
  ```text
  -U*V-V*U = O*O-E*E;
  ```
- the reversed long-channel identity;
- the exact compensation rotation
  ```text
  (C-J)*(C-J)-C*C-J*J
   = 1/2[(C-J)*(C-J)-(C+J)*(C+J)];
  ```
- the Cayley graph formula for a diagonal translation unitary;
- the multiplier `-i tan(theta/2)`;
- divergence of even/odd and odd/even ratios near the two phase resonances;
- a finite synthetic Schur ledger after an explicitly declared connection is
  inserted.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_PARITY_DOMAIN_WALL_CPPD
```

The replay proves only finite matrix identities and phase firewalls.  The
synthetic connection is deliberately manufactured to test bookkeeping; it is
not the arithmetic connection and does not prove `PDWT_a`, CPPD, or RH.