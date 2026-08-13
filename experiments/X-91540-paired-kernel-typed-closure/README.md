# X-91540 — paired-kernel typed branching

This replay checks the exact algebra used by `L-91540`:

- the survival/hazard target telescope;
- the favorable score telescope;
- the uniform physical-corridor inequalities for both branch types;
- the binary return matrix identities;
- exact positive residual identities for arbitrary subprobability endpoint branching;
- the unit local target-debt bound.

It deliberately does **not** replay the imported directed Hall certificates, the
finite component-row certificate, the full factor-54 integration, or RH.

Run:

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```
