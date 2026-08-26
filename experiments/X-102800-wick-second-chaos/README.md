# X-102800 — Wick second-chaos reduction

This standard-library replay checks:

- the exact local Wick factorization;
- the second-order Taylor/Duhamel identity;
- disappearance of root and first chaos;
- a representative free labelled `H^4` energy bound;
- representative same-product divisor multiplicity.

It does **not** certify the distinct-product physical restriction
`WNC102743`, the outer-ray estimate, or RH.

```bash
python3 verify.py --output /tmp/t102800.json
cmp /tmp/t102800.json results/verification.json
```

Expected:

```text
PASS_T102800_WICK_SECOND_CHAOS_REDUCTION
ac7e0c8a2cb5f9ac660e5b53e29ba526b58ae19791bbd5a39a689adb68bf6535
```
