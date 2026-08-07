# X-15415 — Critical Farey determinant regression

This standard-library-only checker exercises the exact finite algebra at the
front of `L-15448`.

It verifies:

1. the completed packet identity
   ```text
   2 E_U(x)
   = S_D(x)+1+M(D)/3+x^2 sum_(D<d<=U) mu(d)/d^2
   ```
   on three exact rational dyadic cells;
2. duplicate-free reduction of every finite `(d,h)` Fourier source to one
   rational frequency `a/q`;
3. the determinant identities
   ```text
   v/b-q/a=(av-bq)/(ab),
   v^2/b^2-q^2/a^2=(av-bq)/(ab)(v/b+q/a);
   ```
4. rejection of the mutated determinant `aq-bv`.

Run:

```bash
python3 verify.py
```

Retained local execution:

```text
verdict: SYNTHETIC_CRITICAL_FAREY_ALGEBRA_VERIFIED
verify.py SHA-256:
b7ebe3aef5eb3c4613a0b3b9250e6a2fe4d5a1a38b701c9011c4ed55679a8ff9
result SHA-256:
6d9da0f0c5d7e37216af156ff8a119749df22b0029137a9010fd2a864dbe6a97
```

## Scope boundary

This regression does **not** verify the global coefficient statement
`L-15448.25` or the all-row summability estimate `L-15448.29`. It proves only
that the exact completion, reduced-frequency bookkeeping, and elementary
numerator identities used by the proposal are internally consistent on finite
controls.

A proof-grade review must add the exhaustive four-class coefficient ledger and
the Jordan-coverage/multiplicity replay specified in `M-15409`.
