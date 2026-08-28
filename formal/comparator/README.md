# Formal comparator surface

The formal-v0.1 comparator keeps trusted statement files separate from the
sorry-free implementation. Challenge files import only their trusted
ChallengeDeps closure and contain exactly one statement placeholder. Solution
files contain no `sorry`, `admit`, custom `axiom`, `opaque`, or `unsafe`
declaration.

The seven release topics are:

1. `RH`
2. `MellinAPI`
3. `ArithmeticRows23`
4. `FixedDetectorFiveThree`
5. `OperatorPositiveSchurRescue`
6. `XiPickThreeNode`
7. `XiPickOrderThreeConditional`

Run from `formal/`:

```bash
bash scripts/build_local_comparators.sh
bash scripts/check_no_sorry.sh
python3 scripts/verify_all_comparator_types.py --repo ..
```

The exact type audit loads Challenge and Solution declarations in separate
Lean processes, removes only the queried declaration-name prefix and Unicode
whitespace, and rejects any mathematical type difference. The order-three Xi
statement includes repeated-node branches and concludes positive
semidefiniteness only. It does not assert positive definiteness, order four,
or RH.
