# X-14315 — Cardinal–radical finite-section verifier

Claim ID: `X-14315`  
Title: Exact rational replay of the supported cardinal repair, zero-kernel radical graph, and Schur floor  
Status: `EMPIRICAL — EXACT SYNTHETIC ARITHMETIC`  
Dependencies: `T-14306`

The verifier uses only integers and `fractions.Fraction`. The retained proof
object certifies

```text
V C_tilde = I,
V K = 0,
rank[C_tilde,K] = 2,
Q(C_tilde,C_tilde) = I + Q(Delta_C,Delta_C),
Q(K,K) = Q(E,E),
Q(C_tilde,K) = Q(Delta_C,E),
Schur-corrected low block >= -(1/62) packet Gram.
```

Eight adversarial tests fail closed. The retained proof-object SHA-256 is

```text
afe08c8b34ce1b1b8339d213ed306e2b0b26f17fc9a16a371c32b5c3a7795cc5
```
