# X-26203 — Critical digital prefix bank

This standard-library exact regression supports `L-26210`.

It verifies:

- the convolution identity
  
  \[
  c_2*\omega_2=\varepsilon-\frac52\delta_2+\delta_4;
  \]
- the strict finite hyperbola-prefix identity at nine cutoffs;
- the exact \(\mathbb Q(\sqrt2)\) lower-frame constant
  
  \[
  \kappa_*=(\sqrt2-1)(1-2^{-3/2})=\frac{5\sqrt2-6}{4};
  \]
- the local bound \(|\omega_2(n)|\le5/2\), which yields
  \(W_R^2\le25R\).

Run:

```bash
python experiments/X-26203-critical-prefix-bank/verify.py
```

Expected verdict:

```text
PASS_EXACT_CRITICAL_DIGITAL_PREFIX_BANK
```

Proof-object SHA-256, computed before inserting the digest field:

```text
8b74e20b45ff4acca5071ab4acd2a6db5a10b3ad1165133204cafbfe2b41362b
```

## Scope

The checker certifies finite convolution, prefix-bank, and algebraic constant identities only. It does **not** certify a physical upper estimate for the bank observations, a uniform factor-five transition theorem, or RH.
