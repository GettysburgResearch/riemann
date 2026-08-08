# X-26202 — Bottom-two carry-charge exact regression

Run:

```bash
python experiments/X-26202-bottom-charge/verify.py
```

Expected verdict:

```text
EXACT_BOTTOM_TWO_CARRY_CHARGE_ALGEBRA_VERIFIED
```

The standard-library checker verifies:

- `omega_2=b_2-(1/2)delta_2*b_2`;
- the exact carry image `(-5/6,-1/2,0,...)`;
- formal backward substitution for the finite carry inverse;
- the coefficientwise identity
  ```text
  5*c_X(2)+3*c_X(3)
   =-6*sum_(q=2)^X omega_2(q)w_X(q);
  ```
- three sibling/filter mutations fail.

The checker uses integers, `fractions.Fraction`, and formal sparse linear forms.
It does **not** verify the eventual sign of the bottom charge, the Landau
continuation argument, or RH.

Retained result digest, excluding its own digest field:

```text
37ab4afbde40b155e5918f63456e64a9beaf544564f364fb7d883fba2789c612
```
