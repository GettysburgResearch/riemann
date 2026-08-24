# X-105430 replay

Run:

```bash
python3 verify.py
python3 tests/test_verify.py
```

The replay checks exact rational versions of:

- the homotopy variance identity;
- the edge constant/star/cycle projection;
- the degree-two toric intersection identity;
- the Lefschetz signature formula;
- the equal-pair to extreme-pair cost;
- fail-closed status mutations.

It does not prove the Selberg--Delange asymptotic, `F1STAR105431`,
`F1CYCLE105431`, `F1HCNC105430`, or RH.
