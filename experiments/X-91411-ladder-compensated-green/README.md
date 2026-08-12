# X-91411 — Gamma-ladder, compensated Wick–Green, and plastic-alignment replay

This finite replay supports:

- `L-91411` — gamma ladder minus one pole channel;
- `L-91412` — compensated Wick–Green identity;
- `L-91413` — plastic-aligned positive Lévy increment;
- the normal-form statements in `T-91402`.

It checks:

1. the exact digamma/gamma-ladder identity for the completed archimedean phase derivative;
2. the rank-one nature of one exponential Hardy Hankel rung and the norm
   `1/(2 alpha)`;
3. an exact rational two-label compensated Wick–Green identity, including its
   finite `C,J` connection vectors;
4. the unique residual switch and the plastic-constant alignment;
5. nonnegativity of the aligned density product at representative points;
6. the exact aligned increment identity
   ```text
   A_a(x)-A_a(0)
    =2 a^-4 int (1-cos(xu)) e^(-u/2) B(u) r_a(u) du;
   ```
7. a safe-line numerical value of the full recurrence anchor at the aligned
   scale.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_LADDER_COMPENSATED_GREEN_ALIGNMENT
```

The replay proves the finite rational compensated identity exactly and checks
analytic identities numerically at high precision.  It does not prove CPPD,
the prime-log sampling inequality, the delayed screw Gram sign, or RH.
