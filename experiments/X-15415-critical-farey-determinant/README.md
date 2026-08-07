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
verify.py Git blob SHA-1:
221c574a92c7f8950c8db9beecba59af43cd0c73
result Git blob SHA-1:
261ef51b7073f12847a57ead8c6330e999690afe
```

The Git blob identities bind the exact committed bytes. A future SHA-256 ledger
should be generated from a checkout of the frozen review head rather than copied
from a pre-commit local prototype.

## Scope boundary

This regression does **not** verify the global coefficient statement
`L-15448.25` or the all-row summability estimate `L-15448.29`. It proves only
that the exact completion, reduced-frequency bookkeeping, and elementary
numerator identities used by the proposal are internally consistent on finite
controls.

A proof-grade review must add the exhaustive four-class coefficient ledger and
the Jordan-coverage/multiplicity replay specified in `M-15409`.
