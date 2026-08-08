# X-27601 — Exact averaged-carry commutator replay

Run:

```bash
python experiments/X-27601-averaged-carry-commutator/verify.py
```

Expected verdict:

```text
PASS_EXACT_AVERAGED_CARRY_COMMUTATOR_ALGEBRA
```

The standard-library `Fraction` checker verifies:

```text
uniform carry-position average -> canonical continuum kernel
omega_2 inverse coefficients
first logarithmic commutator -> top-quarter generalized-prime contrast
second commutator -> generalized Selberg forcing
continuum/discrete carry boundary formula
compact two-band filter coefficients
three source-coefficient mutations
```

The formal logarithm assigns independent integer weights to the primes and extends completely additively. The commutator and boundary identities are therefore checked coefficientwise rather than only after substituting floating logarithms.

Proof-object SHA-256:

```text
4b82004193838f2ca5ba5295bf9d55199bf36d3c7e5f643304a9ffce71fbd82b
```

## Boundary

This replay certifies finite algebra only. It does not prove the prime-annulus energy estimate `PAC-E`, a subpower top-quarter contrast, or RH.
