# X-23801 — exact carry-envelope algebra replay

This experiment checks the finite identities used by `D-23801`.

It reconstructs, using only Python integers and `fractions.Fraction`:

- the complete carry matrix `beta_(nq)`;
- a nonnegative packing from a profile curvature;
- direct componentwise ramp residuals;
- the independent Möbius-curvature residual reconstruction;
- the exact packing-mass telescope;
- the exact coefficient-mass telescope.

## Replay

```bash
python verify.py certificates/synthetic.json \
  --output results/synthetic-verification.regenerated.json
```

Expected classification:

```text
EXACT_CARRY_ENVELOPE_ALGEBRA_VERIFIED
```

Retained proof-object digest:

```text
9dfff56752131b31ae6bb5def0e456147cb441fbdac69f24cc934f1ec310ed7f
```

## Boundary

The certificate uses synthetic rational weights. It validates the exact finite
carry/Möbius factorization and checker logic only. It does not certify:

- directed logarithms or square roots for the actual prime ramp;
- the entropy-optimal packing at any real endpoint;
- the reflected two-contact theorem `L-23803`;
- an asymptotic carry deficit;
- RH.
