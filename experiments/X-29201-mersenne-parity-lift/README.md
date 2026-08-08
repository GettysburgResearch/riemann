# X-29201 — Exact Mersenne-collar and parity-sibling regression

Run:

```bash
python experiments/X-29201-mersenne-parity-lift/verify.py
```

The checker uses only Python integers and `fractions.Fraction`. It verifies:

1. `chi_(n,n)(j)=1`, the diagonal fact behind the automatic collar bound;
2. all three even-column sibling identities;
3. both odd divisor-dipole identities;
4. preservation of the MCF binary-window support for every non-Mersenne lower edge in the retained range;
5. exact Möbius inversion on a synthetic odd-column residual.

Retained local replay:

```text
PASS_EXACT_MERSENNE_COLLAR_AND_PARITY_SIBLING_ALGEBRA
sibling_checks 2064160
support_checks 33150
odd_mobius_inversion_checks 63
diagonal_parent_checks 130816
```

This is finite exact algebra only. It does not prove parity-network feasibility, the Mersenne boundary reconstruction, PPMFL, MCF, or RH.
