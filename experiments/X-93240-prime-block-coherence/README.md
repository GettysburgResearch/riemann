# X-93240 — Exact replay for prime-block coherence

Arithmetic class: `EXACT_RATIONAL`  
Claims checked: `L-93240`, the finite algebra used by `L-93241`, the complete Q4 source decomposition in `L-93242`, and the algebraic reduction used by `T-93243`

Run from this directory:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_X_93240_PRIME_BLOCK_COHERENCE
```

The checker uses only Python's standard library and exact `Fraction` arithmetic. It replays:

- the complete Hilbert diagonal/cross identity;
- the square-root-free positive-projection and half-carrier inequalities;
- the nonnegative rank-one cross certificate;
- finite and closed geometric same-prime-tower identities;
- the complete Q4 source decomposition by prime base;
- the Q4 endpoint-row reconstruction and Gram split;
- three adversarial mutations.

It does **not** authenticate the frozen analytic inputs from PRs #390, #392, or #474. In particular it does not prove the first-Hermite explicit formula, the coefficient-energy asymptotic, the Mellin pole-to-energy implication, a deterministic resonance exclusion, or RH.
